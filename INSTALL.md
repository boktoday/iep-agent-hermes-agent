# INSTALL.md

## Before you start

- A laptop or desktop (Windows, Mac or Linux) from the last several years.
- [Hermes Agent](https://hermes-agent.nousresearch.com/docs) installed (one command on its site).
- Optional: a Telegram account, if you want to reach the agent from your phone.

## 1. Get the files

Download the ZIP from the repo page and unzip it, or clone the repository. You will see `skills/`, `shared/`, `schedules/`, `scripts/` and the docs.

## 2. Put the profile in place

Copy `skills/`, `shared/` and `schedules/` into your Hermes profile folder (the folder Hermes uses for profiles; the Hermes docs show where yours lives). If you use a named profile, put them in that profile's folder.

## 3. Create the plan folder

Run the setup script once:

```bash
python scripts/setup-plan-folder.py
```

This creates `shared/profile.json` from the template and the notes and exports folders, in the profile you point it at (it asks).

## 4. First conversation

Start Hermes and say: **"Start onboarding"** (or "help me set up my child's plan"). Agent Onboarding runs the intake described in `PROFILE_BUILDER.md`.

## 5. Optional: Telegram

Add your Telegram bot token to the profile `.env` (see `.env.example`) and connect Hermes to Telegram as its docs describe. Then a quick note like "add to my notes: swimming went well today" works from the school car park.

## 6. Optional: schedules

`ls schedules/` shows the ready-made reminders (meeting countdown, weekly note prompt). Install whichever you want; each file states its rhythm in its header.

## 7. Fully local (optional, for the privacy-minded)

To keep everything, including the model, on your machine, see `docs/local-models.md`. It walks through picking a model your computer can run (first stop: canirun.ai) and pointing Hermes at it. The daily notes and the plan page work happily on a small local model; use a bigger model occasionally for long document drafting if you have one.

## Checking it worked

Ask: "what do you know about my child's plan so far?" The agent should answer only from `shared/profile.json`, and say plainly when something is not filled in yet. If it invents anything, stop and report it; that is a bug, not a feature.
