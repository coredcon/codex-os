---
title: "Parsing the Package error on Kitchen Armor device"
freshdesk_id: 17000147072
category: "Support"
folder: "In Progress"
status: published
created: 2025-07-01
updated: 2025-07-16
views: 0
tags: ["Kitchen Armor", "Parsing Package"]
source: https://qsrautomations.freshdesk.com/a/solutions/articles/17000147072
---

# Parsing the Package error on Kitchen Armor device

**Problem:**

The Kitchen Armor screen is displaying the following "There was a problem parsing the package" error message:


**Troubleshooting Steps:**

1. Confirm that the site did recently upgrade to CSK 2025.
2. Confirm that the options to automatically upgrade the Android and Windows display clients are flagged within System Settings.
3. Back up dataset and unflag the options to automatically update the Android Display Client before copying to runtime:
4. Restart Kitchen Server service and confirm that the Kitchen Armor station is displaying its respective order display.