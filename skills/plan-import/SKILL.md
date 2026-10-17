---
name: plan-import
description: "Paste in an IEP or assessment; get it organised."
version: 1.0.0
---

# Plan Import

The app's first promise: paste in any IEP or functional assessment and get it organised into something a family can actually read. The agent does the same, with the family's own folder as the desk.

## How it starts

The parent pastes text, drops a photo or PDF, or points the agent at a file. Accept all three. If it is a photo or PDF, read it with the usual document tools before doing anything else.

## What to produce, in this order

1. **Plan at a glance** (chat, half a screen): the child's name, year, the school's word for the support, the two or three goals that matter this term, and who is who in one line each. Plain language. No jargon survives this step.
2. **Questions to ask**: anything the document leaves unclear or that reads like it was written for the school, not the child. Three questions, not thirty.
3. **The structured version**: offer to save it into `shared/`:
   - strengths and what matters → `profile.json` (aboutMe)
   - goals with their wording → `profile.json` (goals), unchanged wording kept alongside a plain version
   - people and roles → `profile.json` (supportTeam)
   - dates, review cycles, and odd terms ("as needed", "where practicable") → `notes/plan-terms.md`
4. **The original** goes to `shared/originals/` untouched, named with the date received. Never edit the source document.

## Rules

1. **Quote, do not invent.** Every goal and every support line comes from the document. If a section is missing, say "the plan does not set out X" and add it to the questions, never fill the gap.
2. **No diagnosis, no verdicts.** You are organising their document, not assessing their child.
3. **Keep both words.** The school's exact wording matters in meetings; keep it verbatim beside the plain version.
4. **Local by default.** The document stays in the family's folder; nothing is uploaded anywhere else.
5. If the document is not an IEP or assessment, say so in one line and offer what would help instead.
