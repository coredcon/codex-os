#!/usr/bin/env python3
"""
freshdesk-solutions-backup.py
Backs up all Freshdesk Solutions articles to:
  - Full dump: F:/My Drive/Freshdesk-Solutions-Backup/ (all categories)
  - Vault copy: F:/My Drive/Obsidian/Codex.os/06 Resources/Freshdesk-Solutions/ (non-archived, non-draft)

Usage: python freshdesk-solutions-backup.py [--vault-only] [--full-only] [--category "Name"]
"""

import requests
import json
import os
import re
import sys
import time
import argparse
from datetime import datetime
from pathlib import Path
from html.parser import HTMLParser

# --- Config ---
DOMAIN = "qsrautomations.freshdesk.com"
API_KEY = "rJ2cCU5I4jbjyJXGVDqF"
FULL_DUMP_DIR = Path("F:/My Drive/Freshdesk-Solutions-Backup")
VAULT_DIR = Path("F:/My Drive/Obsidian/Codex.os/06 Resources/Freshdesk-Solutions")
SKIP_IN_VAULT = {"Archived", "Draft Articles"}  # Categories to exclude from vault copy

# --- HTML → Markdown (simple) ---
class HTMLToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.in_pre = False
        self.in_code = False
        self._tag_stack = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self._tag_stack.append(tag)
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self.result.append('\n' + '#' * int(tag[1]) + ' ')
        elif tag == 'p':
            self.result.append('\n\n')
        elif tag == 'br':
            self.result.append('\n')
        elif tag == 'strong' or tag == 'b':
            self.result.append('**')
        elif tag == 'em' or tag == 'i':
            self.result.append('_')
        elif tag == 'code':
            self.in_code = True
            self.result.append('`')
        elif tag == 'pre':
            self.in_pre = True
            self.result.append('\n```\n')
        elif tag == 'li':
            self.result.append('\n- ')
        elif tag == 'a' and 'href' in attrs_dict:
            self.result.append('[')
        elif tag == 'hr':
            self.result.append('\n---\n')
        elif tag == 'blockquote':
            self.result.append('\n> ')
        elif tag in ('ul', 'ol'):
            self.result.append('\n')
        elif tag == 'table':
            self.result.append('\n')

    def handle_endtag(self, tag):
        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()
        if tag in ('h1','h2','h3','h4','h5','h6'):
            self.result.append('\n')
        elif tag == 'strong' or tag == 'b':
            self.result.append('**')
        elif tag == 'em' or tag == 'i':
            self.result.append('_')
        elif tag == 'code':
            self.in_code = False
            self.result.append('`')
        elif tag == 'pre':
            self.in_pre = False
            self.result.append('\n```\n')
        elif tag == 'a':
            self.result.append(']')
        elif tag in ('p', 'li', 'blockquote'):
            self.result.append('\n')

    def handle_data(self, data):
        self.result.append(data)

    def get_markdown(self):
        text = ''.join(self.result)
        # Clean up excessive blank lines
        text = re.sub(r'\n{4,}', '\n\n\n', text)
        return text.strip()


def html_to_markdown(html):
    if not html:
        return ""
    parser = HTMLToMarkdown()
    parser.feed(html)
    return parser.get_markdown()


def slugify(name):
    """Convert a name to a safe filename."""
    name = name.lower().strip()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s_]+', '-', name)
    name = re.sub(r'-+', '-', name)
    return name[:80]


def api_get(path, params=None):
    url = f"https://{DOMAIN}/api/v2/{path}"
    r = requests.get(url, auth=(API_KEY, 'X'), params=params)
    if r.status_code == 429:
        print("  Rate limited — waiting 30s...")
        time.sleep(30)
        return api_get(path, params)
    if r.status_code != 200:
        return None
    return r.json()


def get_all_articles_in_folder(folder_id):
    """Paginate through all articles in a folder."""
    articles = []
    page = 1
    while True:
        data = api_get(f"solutions/folders/{folder_id}/articles", params={"page": page, "per_page": 30})
        if not data:
            break
        articles.extend(data)
        if len(data) < 30:
            break
        page += 1
        time.sleep(0.3)
    return articles


def get_article_detail(article_id):
    return api_get(f"solutions/articles/{article_id}")


def write_article(dest_dir, category_name, folder_name, article):
    """Write a single article as a markdown file."""
    folder_slug = slugify(folder_name)
    out_dir = dest_dir / slugify(category_name) / folder_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    title = article.get('title', 'Untitled')
    article_id = article.get('id')
    status = article.get('status', 0)
    status_label = {1: 'draft', 2: 'published'}.get(status, str(status))
    created = article.get('created_at', '')[:10]
    updated = article.get('updated_at', '')[:10]
    tags = article.get('tags', [])
    views = article.get('views', 0)
    body_html = article.get('description', '') or ''

    body_md = html_to_markdown(body_html)

    frontmatter = f"""---
title: "{title.replace('"', "'")}"
freshdesk_id: {article_id}
category: "{category_name}"
folder: "{folder_name}"
status: {status_label}
created: {created}
updated: {updated}
views: {views}
tags: {json.dumps(tags)}
source: https://{DOMAIN}/a/solutions/articles/{article_id}
---

"""

    filename = f"{slugify(title)}.md"
    filepath = out_dir / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.write(f"# {title}\n\n")
        f.write(body_md)

    return filepath


def run_backup(full_only=False, vault_only=False, category_filter=None):
    print(f"=== Freshdesk Solutions Backup — {datetime.now().strftime('%Y-%m-%d %H:%M')} ===\n")

    categories = api_get("solutions/categories")
    if not categories:
        print("ERROR: Could not fetch categories.")
        sys.exit(1)

    total_articles = 0
    total_written = 0

    for cat in categories:
        cat_name = cat['name']
        cat_id = cat['id']

        if category_filter and cat_name.lower() != category_filter.lower():
            continue

        print(f"\n[CAT] {cat_name}")

        folders = api_get(f"solutions/categories/{cat_id}/folders")
        if not folders:
            print("  (no folders)")
            continue

        for folder in folders:
            folder_name = folder['name']
            folder_id = folder['id']
            article_count = folder.get('articles_count', '?')
            print(f"  [FOLDER] {folder_name} ({article_count} articles)")

            articles = get_all_articles_in_folder(folder_id)

            for article_stub in articles:
                article_id = article_stub['id']
                title = article_stub.get('title', 'Untitled')

                # Fetch full article with body
                article = get_article_detail(article_id)
                if not article:
                    print(f"    [WARN] Could not fetch: {title}")
                    continue

                total_articles += 1

                # Always write to full dump
                if not vault_only:
                    write_article(FULL_DUMP_DIR, cat_name, folder_name, article)

                # Write to vault if not in skip list
                if not full_only and cat_name not in SKIP_IN_VAULT:
                    write_article(VAULT_DIR, cat_name, folder_name, article)

                total_written += 1
                print(f"    [OK] {title[:70]}")
                time.sleep(0.2)  # Be gentle with the API

    print(f"\n=== Done: {total_written}/{total_articles} articles backed up ===")
    if not vault_only:
        print(f"Full dump: {FULL_DUMP_DIR}")
    if not full_only:
        print(f"Vault copy: {VAULT_DIR}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backup Freshdesk Solutions articles")
    parser.add_argument('--vault-only', action='store_true', help='Only write to vault (skip full dump)')
    parser.add_argument('--full-only', action='store_true', help='Only write full dump (skip vault)')
    parser.add_argument('--category', type=str, help='Only back up a specific category by name')
    args = parser.parse_args()

    run_backup(
        full_only=args.full_only,
        vault_only=args.vault_only,
        category_filter=args.category
    )
