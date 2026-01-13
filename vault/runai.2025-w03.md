---
id: runai-2025-w03-m8n5p2
title: RunAI Week 3 (Jan 10-16)
desc: ''
updated: 1736611200000
created: 1736611200000
---

# Week 3 (Jan 10-16)

## Theme
First Launch - Get Live

## This Week

### 1. Submit Strava approval request (CRITICAL - DO SUNDAY)
- [ ] Implement "View on Strava" deep links on run detail screens
- [ ] Take required screenshots (login, settings, run details, AI chat)
- [ ] Review and customize application email draft
- [ ] Fill in Client ID, contact info, URLs
- [ ] Submit to developers@strava.com
**Why critical:** 1-2 week approval wait. Blocks public launch. Start clock ASAP.

### 2. Pull recent runs from Strava during signup (LAUNCH BLOCKER)
- [ ] Implement Strava API call to fetch last 30-60 days of runs
- [ ] Import runs automatically after OAuth completes
- [ ] Show loading/progress state during import
- [ ] Handle errors gracefully
**Why critical:** New users with zero runs = no value = churn. Required for launch.

### 3. Complete RevenueCat end-to-end testing
- [ ] Install app from Play Console internal testing (not local build)
- [ ] Test purchase flow with license tester account
- [ ] Verify subscription status shows in app correctly
- [ ] Test restore purchases flow
- [ ] Polish paywall UX and edge cases
**Why critical:** Can't charge users = no revenue until this works.

### 4. New user UX review and polish
- [ ] Walk through full flow: first launch → signup → first run → first chat → subscription
- [ ] Fix confusing flows, missing guidance, unclear CTAs
- [ ] Polish rough edges that would turn off first-time users
- [ ] Test on fresh device/account
**Why critical:** First impressions determine retention. Can't launch with broken onboarding.

### 5. Play Store submission
- [ ] Take 5-7 high-quality screenshots
- [ ] Finalize app icon (if needed)
- [ ] Host privacy policy at public URL
- [ ] Fill out data safety form
- [ ] Submit app for review
**Why critical:** 1-7 day approval process. Parallel path with Strava approval.

### 6. Critical security fixes (minimum to launch)
- [ ] Remove DB files from repo, purge git history
- [ ] Remove hardcoded secrets from backend/settings.py
- [ ] Rotate any exposed tokens
**Why critical:** Can't launch with user data exposed in git history.

## Daily

### Sat Jan 10
**Did:** Nothing
**Blockers:** None
**Notes:** Weekend off

### Sun Jan 11
**Did:**
- Working on onboarding flow PR - fixing tests before merge
- Fixed app crash on startup bug
- Built automation around EAS build → Play Store upload process
- Submitted new build to Play Store for testing
- Auto-import runs from Strava PR ready - Claude completed implementation, needs testing/merging
- Verified build fixed crash but found auth flow bugs while dogfooding
**Blockers:** Critical auth/paywall bugs block new user experience
**Notes:** Major progress on launch blockers: auto-import feature implemented (PR ready), build automation working, crash fixed. However, discovered critical auth flow bugs that break new user onboarding. Need to fix auth issues, then test/merge auto-import PR and ship.

**Reflection:** Velocity is slow because a lot of the code is slop. Moving fast created bugs (auth flow broken, paywall not working) which now block progress. The shortcuts taken to ship quickly are now costing more time in firefighting and bug fixes than writing it carefully would have. At a critical decision point: continue rushing and accept more bugs, or take 2-3 days to get core flows solid before launch. The paradox: rushing creates bugs → bugs block progress → velocity gets slower.

### Mon Jan 12
**Did:**
- Fixed bug where app always redirected to runs page even without login (used Codex)
- Fixed EAS autoincrement
- Fixed navigation bug - clicking anything flickered back to main page (Codex fix, verified working)
**Blockers:** Blocked on builds for a while
**Notes:** Heavy debugging day. Both critical auth/nav bugs from Sunday now fixed - new user flow should be unblocked.

### Tue Jan 13
**Did:**
- Fixed bug where every login started a new trial (subscription tracking issue)
- Added "manage subscription" flow (cancel, etc.)
- Decided on new app name: **Coach Vayu** (coachvayu.com) - domain purchased, landing page deployed with privacy policy & terms of service
- Fixed privacy policy & terms links in app paywall
- Fixed restore purchases - clearer verbiage
**Blockers:** None
**Notes:** Huge progress day. Name decided, domain bought, landing page live, all critical bugs cleared. RevenueCat testing in progress - need to verify cancellation, expiration, and restore flows with new build.

### Wed Jan 14
**Did:**
**Blockers:**
**Notes:**

### Thu Jan 15
**Did:**
**Blockers:**
**Notes:**

### Fri Jan 16
**Did:**
**Blockers:**
**Notes:**

## Review
<!-- End of week: what got done, what didn't, why, revenue impact -->
