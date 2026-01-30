---
id: runai-2026-w04-k9m3p1
title: RunAI Week 4 (Jan 17-23)
desc: ''
updated: 1737100800000
created: 1737100800000
---

# Week 4 (Jan 17-23)

[[runai.2025-w03|← prev]] | [[runai.2026-w05|next →]]

## Theme
Launch Ready + AI Quality - Minimum launch prep, then make the coach worth paying for

## Context
Strava approval submitted Jan 16, expect response ~Jan 27-30 (7-10 business days). Play Store submission blocked until Strava increases athlete limit (reviewers need to log in). Use this time wisely: do minimum launch prep, then focus on AI quality - the thing that actually determines whether users pay.

**Reality check:** "I wouldn't pay $10 for my own app" - the AI coach isn't good enough yet.

## This Week

### Launch Prep (minimum viable)

**1. Merge auto-import runs PR (LAUNCH BLOCKER)** ✓
- [x] Merge to main (tested properly at pre-launch check when Strava limit increases)
**Why:** New users with zero runs = no value = churn.

**2. Security fixes (LAUNCH BLOCKER)** (IN PROGRESS)
- [ ] Remove DB files from repo, purge git history
- [ ] Remove hardcoded secrets from backend/settings.py
- [ ] Rotate any exposed tokens
**Why:** Can't launch with user data exposed in git history.

**3. RevenueCat - final verification** ✓
- [x] New user flow - double check before release
**Why:** Most testing done, just need final sanity check.

**4. Play Store assets (can do last minute)**
- [ ] Take screenshots (doesn't need to be perfect for soft launch)
- [ ] Basic store listing
- [ ] Data safety form
**Why:** Don't gold-plate this - can iterate post-launch.

### AI Quality (the real work)

**5. Streaming status messages (IN PROGRESS)**
- [ ] Add loading/status messages during AI coach tool calls
- [ ] "Analyzing your runs...", "Looking at your pace data...", etc.
**Why:** Makes app feel faster and more responsive.

**6. Fix AI coach bugs**
- [ ] Date/day off-by-one errors in training plans
- [ ] Tool call confusion - AI doesn't realize what happened
- [ ] Uses markdown formatting in chat (should be plain text)
- [ ] Analysis errors - wrong conclusions about runs
**Why:** These make the coach look dumb. Users won't pay for a dumb coach.

**7. Explore core flow rethink (if time)**
- [ ] Sketch out single coach relationship model
- [ ] What would home screen look like?
- [ ] How do runs feed into conversation?
**Why:** Multiple chats feels like customer support tickets, not coaching.

## Daily

### Sat Jan 17
**Did:**
**Blockers:**
**Notes:**

### Sun Jan 18
**Did:**
**Blockers:**
**Notes:**

### Mon Jan 19
**Did:**
**Blockers:**
**Notes:**

### Tue Jan 20
**Did:**
- Removed hardcoded/fallback JWT secrets, enforced JWT_SECRET usage (jwt_auth.py + tests), verified prod secrets in Fly
- Replaced JWT/session IDs in OAuth redirect URLs with one-time auth-code exchange (new auth_codes table + migration, /api/auth/exchange endpoint, updated mobile/web callbacks)
- (in progress) RevenueCat webhook auth - require secret at startup, reject if missing
**Blockers:**
**Notes:**
- Before next deploy: test phone login with auth-code changes, run migrations (automatic run import + auth_codes)

### Wed Jan 21
**Did:**
**Blockers:**
**Notes:**

### Thu Jan 22
**Did:**
**Blockers:**
**Notes:**

### Fri Jan 23
**Did:**
**Blockers:**
**Notes:**

## Review
<!-- End of week: what got done, what didn't, why, revenue impact -->
