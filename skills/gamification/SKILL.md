---
name: gamification
description: "Sparks, levels and badges, ported from the app."
version: 1.0.0
---

# Gamification

The original IEP Companion app had a Sparks and badges system, and families liked it. It lives here too, stored in `shared/gamification.json` with the same shape the app used.

## Sparks (award on action)

| Action | Sparks |
|---|---|
| Logging a school day (Attendance Quest) | 100 |
| Completing a short-term goal | 250 |
| Writing a teacher note | 50 |
| Writing a personal note | 25 |
| Asking the agent a question | 10 |
| Personalising the plan page style | 75 |

Levels: **1000 XP per level** (level = floor(total / 1000) + 1), same as the app.

## Achievements (the app's list, adapted)

| Badge | Unlock |
|---|---|
| 🎯 Goal Getter | Complete your first short-term goal |
| 👟 Five Strides | Complete 5 short-term goals |
| 🏅 Weekly Warrior | Log attendance every school day in a single week |
| 🗓️ Attendance Pro | Log 10 total days of attendance |
| 🧠 Curious Mind | Ask the agent 5 good questions (the app called its advisor Sparky) |
| 💌 Super Communicator | Write 3 teacher notes |
| 🗒️ Note Taker | Write 3 personal notes |
| 🎨 Plan Artist | Personalise the plan page style once (app: Theme Artist) |

## The data file

`shared/gamification.json`:

```json
{
  "enabled": true,
  "sparks": 0,
  "level": 1,
  "xpInLevel": 0,
  "unlockedAchievements": [],
  "completedGoalIds": [],
  "stats": {
    "teacherNotesWritten": 0,
    "myNotesWritten": 0,
    "aiQuestionsAsked": 0,
    "themesGenerated": 0,
    "attendedDays": []
  }
}
```

Award and save after the action lands (not before). Announce it in half a line ("+50 sparks, Note Taker unlocked"), never more.

## House rules

1. **Ask once, at onboarding.** "The app had a sparks and badges system. Want it here?" If no, set `enabled: false` and never mention it again unless they raise it.
2. **Sparks celebrate, they do not police.** No streaks to lose, no golden windows, no "you missed yesterday".
3. **Never gate help behind points.** Hard Moments ignores all of this.
4. **Quiet by default in check-ins.** One spark line max, and only when something actually unlocked.
5. **The parent can say "quiet" any time** and gamification goes silent for a month.
