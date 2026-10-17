---
name: export
description: "Printable plan page plus app-compatible JSON."
version: 1.0.0
---

# Export

Two outputs, both local, both the family's to keep.

## 1. The printable plan page

Write `shared/exports/plan-<date>.html`: a single, self-contained page (inline CSS, no internet needed) that prints cleanly:

- Header: the child's first name, year level, date of plan, next review.
- About Me: strengths first, then challenges, what helps learning, how communication works best.
- My Big Goal with its curriculum link.
- My Daily Wins: each goal with current level and strategies.
- Support Team: names and roles (contacts optional in print; ask).
- Footer: "Prepared at home by a parent. Not a clinical or legal document."

Offer to open it in the browser to check before printing. Keep it to three pages when printed; cut, do not shrink.

## 2. The data export

Write `shared/exports/iep-agent-<date>.json`: `profile.json` verbatim plus `exportedAt`. The field names match the IEP Companion Generator app's data model, so the file can be loaded into the app (import) or kept as a portable backup.

## Importing

Given a JSON export (from this agent or the app), validate the shape against AGENTS.md, show the parent a two-line summary of what is inside, and only then write it into `shared/profile.json` (keep a dated copy of the previous file in `shared/exports/backup-<date>.json`).

## Rules

- Never email or share an export unless the parent names the recipient and confirms in the moment.
- Files are local; offer the folder path so the family can back it up themselves.
