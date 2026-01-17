---
id: runai-backlog-8kx7m2
title: RunAI Backlog
desc: ''
updated: 1736092800000
created: 1736092800000
---

# RunAI Backlog

Ordered by priority (top = do first). New ideas go to the bottom.

## Backlog

**High Priority / Launch Blockers:**

- [x] Choose new app name (RunAI is taken) → **Coach Vayu** (coachvayu.com)
  - Blocks: domain, landing page, privacy policy, Strava approval, Play Store
  - [x] Update name throughout frontend (app title, strings, etc.)
- [x] Buy domain and set up landing page
  - [x] Buy domain (coachvayu.com)
  - [x] Host landing page with privacy policy and terms of service
- [ ] Pull recent runs from Strava API during signup (last 30-60 days) - LAUNCH BLOCKER
- [x] Get Strava approval (brand guidelines review) - form submitted Jan 16, 7-10 business days
  - [x] Review and customize Strava Developer Program application email draft (RunAI → Coach Vayu)
  - [x] Fill in Client ID, name, email, website URL, privacy policy URL
  - [x] Take required screenshots (login, settings, run details, AI chat)
  - [x] Implement "View on Strava" deep links ✓
  - [x] Implement deauthorization webhook ✓
  - [x] Submit application to developers@strava.com ✓
- [x] Test RevenueCat integration ✓ (verified Jan 17)
  - [x] Cancellation ✓
  - [x] Expiration ✓
  - [x] Restore purchases ✓
  - [x] Plan upgrade ✓
  - [x] Resubscribe after cancel ✓
  - [ ] New user flow - double check before release
  - [ ] iOS testing - later
- [ ] Security audit
- [ ] Publish to Play Store

**UX Improvements:**

- [ ] Add loading/status messages during AI coach tool calls (e.g., "Analyzing your runs...", "Looking at your pace data...")
- [ ] Remove "upload FIT file" feature
- [ ] Review end-to-end UX - make sure flows make sense for new users
- [ ] Add tooltips/coach marks for first-time viewing of key pages
- [ ] Improve run page design
- [ ] Work on onboarding flow

**Features:**

- [ ] Coach can search/analyze past runs
- [ ] Design and implement onboarding screens with 30-day free trial messaging
- [ ] Add streaming responses to chat interface
- [ ] Finalize app-wide color scheme and redesign entire app based on it

**Infrastructure:**

- [x] Automate build and Play Store upload (script EAS build → download AAB → upload to Play Store)
- [ ] Research Strava API user limit increase process and apply for higher limits
- [ ] Create landing page and host privacy policy and other legal docs

**Bugs:**

**Critical (blocks new user flow):**
- [x] Navigation broken after login - clicking anything flickers and returns to main page
- [x] App opens to runs page by default instead of login page when not authenticated
- [x] Fix privacy policy and terms of service pages on paywall
- [x] Restore purchases button unclear - needs better UX and verification it works

**Medium priority:**
- [x] Manage subscription page should show cancelled status and expiry date when subscription is cancelled
- [ ] Chat page doesn't auto-refresh the chats on opening
- [ ] Onboarding flow should allow going back to previous slide
