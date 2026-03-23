#!/usr/bin/env python3
"""
bambu-price-check.py — Track Bambu Lab P2S price over time

Fetches current price from the Bambu US store via JSON-LD,
logs to CSV, and generates a trend graph (PNG + HTML).

Run manually or hook into vox-overnight.py for daily tracking.
"""

import csv
import json
import os
import sys
import urllib.request
from datetime import datetime

try:
    from bs4 import BeautifulSoup
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
except ImportError as e:
    print(f"Missing dependency: {e}")
    sys.exit(1)

VAULT = "F:/My Drive/Obsidian/Codex.os"
DATA_DIR = os.path.join(VAULT, ".claude/data")
CSV_FILE = os.path.join(DATA_DIR, "bambu-p2s-prices.csv")
GRAPH_FILE = os.path.join(DATA_DIR, "bambu-p2s-prices.png")

PRODUCT_URL = "https://us.store.bambulab.com/products/p2s"
ALERT_FILE = os.path.join(DATA_DIR, "bambu-price-alert.txt")
COMBO_VARIANT_KEY = "Bambu Lab P2S - P2S Combo"

CSV_HEADER = ["date", "variant", "price", "currency"]


def fetch_prices():
    """Scrape JSON-LD from Bambu product page, return dict of variant->price."""
    req = urllib.request.Request(
        PRODUCT_URL,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        html = r.read().decode("utf-8", errors="ignore")

    soup = BeautifulSoup(html, "html.parser")
    prices = {}

    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(tag.string or "")
        except Exception:
            continue

        if data.get("@type") == "ProductGroup" and "hasVariant" in data:
            for variant in data["hasVariant"]:
                name = variant.get("name", "")
                offer = variant.get("offers", {})
                price = offer.get("price")
                currency = offer.get("priceCurrency", "USD")
                if price is not None:
                    prices[name] = {"price": float(price), "currency": currency}

    return prices


def log_prices(prices):
    """Append today's prices to CSV."""
    os.makedirs(DATA_DIR, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")

    write_header = not os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(CSV_HEADER)
        for variant, info in prices.items():
            writer.writerow([today, variant, info["price"], info["currency"]])


def read_history():
    """Read CSV into dict of variant -> [(date, price), ...]"""
    if not os.path.exists(CSV_FILE):
        return {}
    history = {}
    with open(CSV_FILE, newline="") as f:
        for row in csv.DictReader(f):
            v = row["variant"]
            if v not in history:
                history[v] = []
            history[v].append((
                datetime.strptime(row["date"], "%Y-%m-%d"),
                float(row["price"]),
            ))
    return history


def generate_graph(history):
    """Generate price trend graph as PNG."""
    if not history:
        print("No history to graph yet.")
        return

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("#1a1a2e")
    ax.set_facecolor("#16213e")

    colors = {"P2S Combo": "#e94560", "P2S": "#0f3460"}
    fallback_colors = ["#e94560", "#0f3460", "#f5a623", "#7ed321"]

    for i, (variant, entries) in enumerate(sorted(history.items())):
        dates = [e[0] for e in entries]
        prices = [e[1] for e in entries]
        color = colors.get(variant, fallback_colors[i % len(fallback_colors)])
        ax.plot(dates, prices, marker="o", label=variant, color=color, linewidth=2, markersize=6)
        if prices:
            ax.annotate(
                f"${prices[-1]:,.0f}",
                xy=(dates[-1], prices[-1]),
                xytext=(6, 4), textcoords="offset points",
                color=color, fontsize=9, fontweight="bold"
            )

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    fig.autofmt_xdate()

    ax.set_title("Bambu Lab P2S — Price Tracker", color="white", fontsize=13, pad=12)
    ax.set_ylabel("Price (USD)", color="#aaaaaa")
    ax.tick_params(colors="#aaaaaa")
    ax.spines["bottom"].set_color("#333355")
    ax.spines["left"].set_color("#333355")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax.legend(facecolor="#16213e", edgecolor="#333355", labelcolor="white")
    ax.grid(True, color="#222244", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig(GRAPH_FILE, dpi=150, facecolor=fig.get_facecolor())
    plt.close()
    print(f"Graph saved: {GRAPH_FILE}")


def get_previous_combo_price(history):
    """Return the most recent logged combo price before today, or None."""
    entries = history.get(COMBO_VARIANT_KEY, [])
    today = datetime.now().date()
    past = [(d, p) for d, p in entries if d.date() < today]
    return past[-1][1] if past else None


def check_price_drop(prices, history):
    """Write alert file if combo price dropped. Clear it if not."""
    combo_info = prices.get(COMBO_VARIANT_KEY)
    if not combo_info:
        return
    current = combo_info["price"]
    previous = get_previous_combo_price(history)

    os.makedirs(DATA_DIR, exist_ok=True)
    if previous is not None and current < previous:
        drop = previous - current
        msg = f"P2S Combo dropped ${drop:,.2f} — now ${current:,.2f} (was ${previous:,.2f})"
        with open(ALERT_FILE, "w") as f:
            f.write(msg)
        print(f"\n*** PRICE DROP: {msg} ***")
    else:
        # Clear any stale alert
        if os.path.exists(ALERT_FILE):
            os.remove(ALERT_FILE)


def main():
    print(f"Fetching prices from Bambu US store...")
    try:
        prices = fetch_prices()
    except Exception as e:
        print(f"Fetch failed: {e}")
        sys.exit(1)

    if not prices:
        print("No prices found in page — site structure may have changed.")
        sys.exit(1)

    print("\nCurrent prices:")
    for variant, info in sorted(prices.items()):
        print(f"  {variant}: ${info['price']:,.2f} {info['currency']}")

    history = read_history()
    check_price_drop(prices, history)
    log_prices(prices)
    print(f"Logged to {CSV_FILE}")

    generate_graph(read_history())


if __name__ == "__main__":
    main()
