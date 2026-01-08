---
id: runai-2025-w02-9pq3n7
title: RunAI Week 2 (Jan 3-9)
desc: ''
updated: 1736092800000
created: 1736092800000
---

# Week 2 (Jan 3-9)

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
- Kicked off agents for Strava brand guidelines review and security audit - both completed and generated specs
**Blockers:** Permissions error when validating credentials. Might need to publish APK/AAB to Play Console first before RevenueCat can validate. Build is currently in progress.
**Notes:** Making progress on tasks #1, #2, and #3. Have specs ready for security fixes and Strava compliance changes. Can implement once RevenueCat unblocked or in parallel.

**Task lists from specs:**

**Strava Branding Compliance:**
- [ ] Download official Strava button and logo assets
- [ ] Replace custom Strava button with official 'Connect with Strava' asset
- [ ] Add 'Powered by Strava' logo to Settings screen
- [ ] Add 'View on Strava' deep links to activity detail screens
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

## Review
<!-- End of week: what got done, what didn't, why, revenue impact -->
