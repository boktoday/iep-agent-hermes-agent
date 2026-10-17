#!/usr/bin/env python3
"""Create the IEP Agent plan folder structure from templates in this repo.

Usage: python setup-plan-folder.py [profile_dir]
Without an argument it asks where your Hermes profile lives.
"""
import json
import pathlib
import shutil
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

def main():
    if len(sys.argv) > 1:
        profile = pathlib.Path(sys.argv[1]).expanduser().resolve()
    else:
        hint = input("Path to your Hermes profile folder (the one with skills/ in it): ").strip()
        if not hint:
            sys.exit("no path given")
        profile = pathlib.Path(hint).expanduser().resolve()
    if not profile.exists():
        sys.exit("folder does not exist: %s" % profile)

    shared = profile / "shared"
    for sub in ("notes", "notes/reports", "exports"):
        (shared / sub).mkdir(parents=True, exist_ok=True)

    target = shared / "profile.json"
    if target.exists():
        print("profile.json already exists; leaving it untouched:", target)
    else:
        shutil.copyfile(REPO / "shared" / "profile.json", target)
        print("created:", target)

    n = shared / "notes" / "my-notes.md"
    if not n.exists():
        n.write_text("# My Notes\n\n", encoding="utf-8")
        print("created:", n)
    t = shared / "notes" / "teacher-notes.md"
    if not t.exists():
        t.write_text("# Teacher Notes\n\n", encoding="utf-8")
        print("created:", t)

    data = json.loads(target.read_text(encoding="utf-8"))
    print("plan folder ready for:", data.get("studentName") or "(no student name yet; run onboarding to fill it in)")
    print("done")

if __name__ == "__main__":
    main()
