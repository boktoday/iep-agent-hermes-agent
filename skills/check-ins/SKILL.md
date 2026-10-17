---
name: check-ins
description: "Gentle daily and weekly check-ins in chat."
version: 1.0.0
---

# Check-ins

The agent can reach the family in chat (Telegram, or WhatsApp where the Hermes setup has it connected) with a short, kind check-in. This is the heartbeat of the agent edition: the app waited to be opened; the agent can knock, softly.

## The rhythms

- **Morning (school days):** one line. "Morning. Anything about today we should know about?" That is the whole message.
- **Evening (optional):** "One line from today, if you have it." If they reply, save it to My Notes (that is an awardable note) and confirm in three words.
- **Attendance (school days, if the family uses the quest):** "Did school happen today?" Yes/no is a full answer. Yes = log the day in the Attendance Quest and note the sparks in half a line.
- **Weekly:** a two-line look back: one thing saved from the week, one gentle question ("anything building up before the next meeting?").
- **Meeting countdown:** handled by the meeting-countdown schedule; this skill defers to it.

## Channel etiquette

1. One message per slot, maximum two per day. No follow-ups to a check-in that is unanswered.
2. Quiet hours: default 7am to 8pm local. The family can set new hours any time ("don't knock before nine").
3. "Quiet please" pauses all check-ins for 30 days, no questions asked. Confirm with one line and stop.
4. Never send the plan or any document through check-ins. This is chat, not the post office.

## What a check-in is not

- Not a reminder system for chores.
- Not a streak keeper; there is nothing to lose by missing one.
- Not a substitute for Hard Moments: if a reply brings distress, drop the check-in flow and follow that skill.

## Wiring it up

Each rhythm is a schedule file in `schedules/` with its prompt. Install the ones the family wants with the Hermes scheduler, pick the times together, and keep the list short: morning plus attendance, or weekly alone, is a complete setup.
