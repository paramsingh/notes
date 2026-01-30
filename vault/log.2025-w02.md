---
id: runai-2025-w02-9pq3n7
title: RunAI Week 2 (Jan 3-9)
desc: ''
updated: 1736092800000
created: 1736092800000
---

# Week 2 (Jan 3-9)

← prev | [[log.2025-w03|next →]]

## Theme
Launch prep - get ready to charge

## This Week

### 1. Test RevenueCat integration
- [ ] Test purchase flow in sandbox (iOS + Android)
- [ ] Verify subscription status reflected correctly in app
- [ ] Test webhook handling (purchase, renewal, cancellation)
- [ ] Test restore purchases flow
- [ ] Test paywall triggers correctly

### 2. Security audit
- [ ] JWT: token expiry, refresh flow, secure storage
- [ ] Strava tokens: storage, refresh, revocation handling
- [ ] Data isolation: verify users can't see each other's runs/chats
- [ ] API: rate limiting, input validation, SQL injection checks
- [ ] HTTPS everywhere, no secrets in code/logs

### 3. Read Strava brand guidelines
- [ ] Read developer guidelines
- [ ] Note requirements (attribution, logos, naming)
- [ ] Create checklist of changes needed
- [ ] Check if "RunAI" name is compliant

### 4. Play Store listing prep
- [ ] App icon finalized
- [ ] Screenshots (5+ screens)
- [ ] Short & full description
- [ ] Privacy policy URL
- [ ] Data safety form answers

## Daily

### Sat Jan 3

### Sun Jan 4

### Mon Jan 5
**Did:** Set up project tracking system - created backlog, weekly note structure, added workflow to CLAUDE.md
**Blockers:** None
**Notes:** First session, no code work - just planning infrastructure

### Tue Jan 6

### Wed Jan 7

### Thu Jan 8
**Did:**
- Worked on RevenueCat integration - created Google Play Store account, RevenueCat account, set up permissions
- Created product and base plan in RevenueCat
- Fixed credentials issue by regenerating service account credentials
- Kicked off agents for Strava brand guidelines review and security audit - both completed and generated specs
- Tested RevenueCat flow - got buy page showing up for users after login
- Implemented Strava branding compliance: downloaded official assets, replaced button, added 'Powered by Strava' logo to Settings, added 'View on Strava' deep links (branch ready for manual testing)
**Blockers:** Can't test actual payment flow without app installed from Google Play (not local builds). This slows dev loop significantly - need to research workarounds.
**Notes:** RevenueCat integration has lots of edge cases and rough edges to polish. Will continue tomorrow. Strava branding work complete and ready for testing. Have security fixes spec ready to implement.

**Task lists from specs:**

**Strava Branding Compliance:**
- [x] Download official Strava button and logo assets
- [x] Replace custom Strava button with official 'Connect with Strava' asset
- [x] Add 'Powered by Strava' logo to Settings screen
- [x] Add 'View on Strava' deep links to activity detail screens
- ✓ App name "RunAI" is compliant (no Strava references)

**Security Audit - Critical/High:**
- [ ] Remove hardcoded secrets from backend/settings.py and rotate keys
- [ ] Remove DB files from repo, add to .gitignore, purge git history
- [ ] Enforce JWT_SECRET validation - fail fast on startup if missing
- [ ] Fix OAuth callbacks - stop placing JWT/session IDs in redirect URLs
- [ ] Make RevenueCat webhook auth required - reject if secret missing

**Security Audit - Medium:**
- [ ] Restrict CORS origins via env config (backend/app.py)
- [ ] Add rate limiting to API endpoints (/api/chat, /upload, /api/strava/webhook)
- [ ] Add upload size limits and MIME validation (backend/upload.py)
- [ ] Allowlist fields in update_planned_run (backend/db.py:1254-1267)
- [ ] Enforce session revocation in auth checks (validate sessions table)
- [ ] Add OAuth state parameter and PKCE for CSRF protection

### Fri Jan 9
**Did:**
- Manual tested Strava branding changes - looks good, merged to main
- Set up license testing for RevenueCat in Google Play Console - should unblock payment flow testing
- Created comprehensive Play Store listing content (descriptions, keywords, screenshot plan)
- Drafted privacy policy for Play Store submission
- Identified critical launch blockers: Strava user limit approval, pull recent runs on signup, new user UX review
- Started planning Week 3 focus
**Blockers:** None currently - license testing should unblock RevenueCat
**Notes:** Play Store listing materials ready to publish once we have screenshots and privacy policy hosting. Ready to submit Strava approval request.

### Sat Jan 10

### Sun Jan 11

## Review

**What got done:**
- ✅ **Task #3: Strava branding** (100%) - Fully implemented, tested, merged. Official button, "Powered by Strava" logo, compliant.
- 🟡 **Task #1: RevenueCat integration** (40%) - Accounts created, products configured, buy page working, license testing enabled. Payment flow testing NOT done.
- 🟡 **Task #4: Play Store prep** (60%) - Descriptions, privacy policy, and screenshot plan drafted. Need to take actual screenshots, host privacy policy, finalize icon.
- ❌ **Task #2: Security audit** (0%) - None of the 11 critical/medium fixes implemented.

**What didn't get done:**
- RevenueCat end-to-end payment testing (waiting for license testing to work)
- All security fixes (11 items)
- Play Store submission (need screenshots, privacy hosting)
- Strava Developer Program application (drafted but not submitted)

**Why:**
- Blocked on RevenueCat payment testing (resolved Fri with license testing)
- Didn't work Sat/Sun
- Focused on planning and documentation over implementation

**Revenue impact:**
Moderate progress toward launch. Can't charge users until RevenueCat fully tested. Can't launch publicly until Strava approval received (could take 1-2 weeks). Still 1-2 weeks away from being able to generate revenue.

**Critical path blockers identified:**
1. Strava user limit approval (1-2 week wait)
2. Pull recent runs from Strava on signup (new users need data)
3. Complete RevenueCat testing
4. New user UX review and polish
