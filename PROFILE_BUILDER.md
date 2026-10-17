# PROFILE_BUILDER.md - the guided onboarding

This is the intake: the same questions IEP Companion Generator asked on its onboarding screen, asked conversationally, in your own time. Agent Onboarding runs it. It takes about fifteen minutes with reports to hand, or five without.

## The intake, in order

1. **Who is this plan for?** The child's first name. (The agent uses the first name only, unless the parent asks otherwise.)
2. **Year level.** What year is the child in at school?
3. **The existing IEP.** "If you have the current IEP, paste the whole text here, however messy. If not, skip this and we will build one from scratch."
4. **The Functional Capacity Assessment** (or equivalent report). Paste the whole text if there is one. Skip if not.
5. **Anything else.** Sleep, medication routines, siblings, sensory triggers, what a good day looks like, what the school already knows. Free text.
6. **Term dates and country.** Term start, term end, and country (for school-year and public-holiday context).

Do not block on missing documents. A blank intake that says "no IEP yet" is a valid start; the agent builds the plan page over the following conversations instead.

## Step two: the review

From the pasted text and answers the agent proposes a draft, and the parent edits it before anything is saved:

- **General information:** student name, date of birth, year level, date of plan, next review, key staff member
- **Key information about me:**
  - diagnosis or considerations (as the parent frames them, not as a verdict)
  - strengths (at least three; the child's own words if available)
  - challenges (described with care, never as blame)
  - what helps me learn
  - how I communicate best
- **My Big Goal:** one long-term goal, plus how it links to the curriculum or the school's plan
- **My Daily Wins:** short-term goals, each with a domain (literacy, regulation, social, independence, etc.), the goal, the current level, and 2 to 4 strategies
- **My Support Team:** name, role, contact for each person (parents, teacher, aide, therapists, coordinator)

Read the draft back in a few plain lines and ask: "What did I get wrong?" Fix it before saving.

## Step three: save

Write `shared/profile.json` in the app-compatible shape (see AGENTS.md), copy the pasted reports into `shared/notes/reports/` as dated text files so the source material stays findable, and note the date of plan.

## Rules for this intake

- One question at a time, never a wall of form fields.
- Any question may be skipped; mark skipped fields as unknown rather than inventing them.
- The parent's framing of the child wins over the report's framing, always.
- If the parent becomes upset reading reports back (common; these documents are hard), pause the intake and let Hard Moments take over.
