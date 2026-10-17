# IEP Agent (Hermes edition)

A free, local-first planning agent for parents navigating an IEP (Individual Education Plan). Built on **[Hermes Agent](https://hermes-agent.nousresearch.com/docs)**, it walks beside a parent through onboarding, keeps the child's goals, notes and support team in one place, and gets them ready for every meeting.

No accounts. No subscriptions. Everything lives in your own folder, on your own machine. Telephone or chat optional, via Telegram.

---

> **Download, free for everyone:** [the latest ZIP](https://github.com/boktoday/iep-agent-hermes-agent/archive/refs/heads/main.zip), or use the green **Code → Download ZIP** button on this page.
> Come subscribe to [our community](https://discord.gg/y5FhfKpwKU) for installation help and weekly office hours.
>
> **Licence:** free to use, share and build on for noncommercial purposes with credit (PolyForm Noncommercial 1.0.0, see LICENSE). The IEP Agent, OneToEight and Afterschool names and marks stay ours; bundled third-party parts keep their own licences.

---

## What this is

IEP Agent is the IEP Companion Generator app reborn as a personal agent you own. The app's best ideas stay: a guided intake, a clear About Me picture of the child, one big goal, short-term goals with strategies, a support team, and running notes. What changes is who does the thinking: instead of a web form and a cloud AI key, you talk with an agent on your own computer, and it keeps everything in plain files you can read, back up and take with you.

- **Onboarding, as a conversation.** The agent asks the same questions the app asks (child's name, year level, existing IEP, Functional Capacity Assessment, other context, term dates, country) and builds the plan with you.
- **The workspace.** About Me (strengths, challenges, what helps learning, how communication works best), My Big Goal, Daily Wins (short-term goals with strategies), Support Team, My Notes and Teacher Notes.
- **Meeting prep.** Before any planning meeting it builds a one-page brief: your points, your questions, the goals you are pushing for, and the red flags to watch.
- **Exports that work elsewhere.** A printable plan page for the meeting table, and a JSON export that matches the app's data model.
- **Telegram, if you want it.** Run the agent in a Telegram chat so a note can be captured the moment it happens.

## The team

| Skill | What it does |
|---|---|
| Agent Onboarding | Front door: the guided intake, profile setup, routing |
| About Me | Strengths, challenges, what helps learning, how I communicate |
| Goals | My Big Goal plus short-term goals with strategies |
| Support Team | Who is who, roles and contact details |
| My Notes | Running notes, captured in a sentence each |
| Teacher Notes | Notes by class and teacher, kept in order |
| Meeting Prep | The one-page brief and advocacy letter drafting before meetings |
| Hard Moments | Heated meetings, bad news and hard days: care first, humans always |
| Export | Printable plan page plus app-compatible JSON |

Every skill is written to be plain-spoken, honest and unhurried. See `SOUL.md` for the principles and `AGENTS.md` for how the team works together.

---

## How it works

1. **One shared folder.** Every skill reads and writes the same folder: `shared/profile.json`, `shared/notes/`, `shared/exports/`. You own it; open it, edit it, back it up, or delete it.
2. **One front door.** Agent Onboarding runs the intake and introduces every other skill when its moment comes.
3. **Your pace.** Set the child up in one sitting, or a few minutes a day. Nothing is sent anywhere.
4. **The plan page is the product.** Everything points at the printable plan page you bring to the table.
5. **Honesty about what this is.** Not legal advice, not medical advice, and not a diagnosis. It helps you get clear and prepared; the professionals and the school do the rest.

---

## Install

See `INSTALL.md`. Short version:

1. Install Hermes Agent (one command, any laptop).
2. Copy the `skills/`, `shared/` and `schedules/` folders into your Hermes profile.
3. Run `scripts/setup-plan-folder.py` to create your plan folder.
4. Have your first conversation with Agent Onboarding.
5. Optionally install the schedules so meeting reminders come to you.

---

## Privacy

The agent runs locally. The plan folder never leaves your machine unless you export or share it, and sharing always takes your explicit yes in the moment. For a fully offline setup, run the agent on a local model; see `docs/local-models.md`.

---

## Repository layout

```
skills/            nine skills (each SKILL.md), incl. hard-moments and helplines
shared/            your plan folder templates: profile, notes, exports
schedules/         ready-to-install reminders (meetings, weekly notes)
SOUL.md            the principles every skill lives by
AGENTS.md          how the team works together
INSTALL.md         full setup guide (including fully-offline local models)
PROFILE_BUILDER.md the guided onboarding
config.yaml        example Hermes configuration
scripts/           setup-plan-folder.py
docs/              design notes + local models guide
```

---

## Licence

PolyForm Noncommercial License 1.0.0. Free to use, change and share for any noncommercial purpose, with credit. See `LICENSE`.

Required Notice: Copyright 2026 Brendan O'Keefe (https://onetoeight.org)

Built on the IEP Companion Generator app's data model and intake. The advice in this repo is general; it is not a substitute for your school, your therapists or your own judgement.
