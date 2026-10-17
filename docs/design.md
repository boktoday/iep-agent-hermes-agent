# Design notes

## What this is

IEP Ally is the IEP Companion Generator app (v4.0, the local-first build) reborn as a Hermes agent profile. The app was a React single-page app with an intake, a workspace (About Me, goals, support team, notes), an AI advisor and (in v3.0) legacy Supabase auth and Stripe payments. The agent keeps the useful shape and drops the rest.

## Decisions

1. **Plain files are the source of truth.** The app kept data in browser storage (IndexedDB/localStorage). An external agent cannot reliably write browser storage, so the canonical data lives in `shared/profile.json` plus Markdown notes. Human-readable, backup-able, no lock-in.
2. **App-compatible shape.** `profile.json` uses the app's `IEPData` field names, so exports round-trip into the app where families still use it.
3. **The agent replaces the AI Advisor.** No Gemini or OpenRouter key inside the app; the conversation is the advisor.
4. **No auth, no payments, no server.** The v3.0 Supabase/Stripe layer is deliberately absent. Nothing to log into, nothing to buy.
5. **Printable output is the product.** The plan page and the meeting brief are what the family actually carries into the room.
6. **Hard Moments is mandatory.** Every agent in this family carries crisis rails; see `skills/hard-moments/`.
7. **Local model option.** The data is a child's most personal record; see `docs/local-models.md` for keeping everything on the machine.

## Not yet built (ideas)

- A personalised single-file HTML companion page, generated from `profile.json` (the "app in a file" experience without a server).
- Speech read-aloud of the plan page (the app had TTS; a static page can use the browser's own).
- Attendance quest tracking (present in the app; parked here until a family asks).

## Provenance

Built from the IEP Companion Generator app (boktoday/iep-companion-generator-4.0, the cleaned local-first build), with the intake dialogue ported from the app's onboarding flow. Naming: "IEP Companion" retired for the agent; this edition is IEP Ally.
