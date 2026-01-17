---
id: runai-2026-w04-k9m3p1
title: RunAI Week 4 (Jan 17-23)
desc: ''
updated: 1737100800000
created: 1737100800000
---

# Week 4 (Jan 17-23)

[[runai.2025-w03|← prev]] | next →

## Theme
Launch Ready - Everything prepared to submit Play Store the day Strava approves

## Context
Strava approval submitted Jan 16, expect response ~Jan 27-30 (7-10 business days). Play Store submission blocked until Strava increases athlete limit (reviewers need to log in). Use this week to get everything else done.

## This Week

### 1. Complete RevenueCat testing (LAUNCH BLOCKER)
- [ ] Cancellation - cancel via Play Store → verify still have access until expiry
- [ ] Expiration - wait for sandbox sub to expire → verify redirect to paywall
- [ ] Restore purchases - log out, log back in → tap restore → verify access
- [ ] New user flow - fresh account → sees paywall after trial expires
**Why:** Can't charge users until payment flow is bulletproof.

### 2. Merge auto-import runs PR (LAUNCH BLOCKER)
- [ ] Test the PR locally/on device
- [ ] Verify runs import correctly after OAuth
- [ ] Handle edge cases (no runs, API errors)
- [ ] Merge to main
**Why:** New users with zero runs = no value = churn.

### 3. Prepare Play Store submission (READY TO SHIP)
- [ ] Take 5-7 marketing-quality screenshots
- [ ] Write store listing (title, short desc, full desc)
- [ ] Fill out data safety form (Strava data, analytics, etc.)
- [ ] Finalize app icon
- [ ] Have everything ready to submit in <1 hour when Strava approves
**Why:** Don't want Play Store prep to delay launch after Strava approves.

### 4. Security fixes
- [ ] Remove DB files from repo, purge git history
- [ ] Remove hardcoded secrets from backend/settings.py
- [ ] Rotate any exposed tokens
**Why:** Can't launch with user data exposed in git history.

### 5. UX polish (if time)
- [ ] Walk through full new user flow
- [ ] Fix any rough edges
- [ ] Test on fresh device/account

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
**Blockers:**
**Notes:**

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
