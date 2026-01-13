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
  - [ ] Update name throughout frontend (app title, strings, etc.)
- [x] Buy domain and set up landing page
  - [x] Buy domain (coachvayu.com)
  - [x] Host landing page with privacy policy and terms of service
- [ ] Pull recent runs from Strava API during signup (last 30-60 days) - LAUNCH BLOCKER
- [ ] Get Strava approval (brand guidelines review)
  - [ ] Review and customize Strava Developer Program application email draft
  - [ ] Fill in Client ID, name, email, website URL, privacy policy URL
  - [ ] Take required screenshots (login, settings, run details, AI chat)
  - [ ] Implement "View on Strava" deep links (REQUIRED before submission)
  - [ ] Implement deauthorization webhook (delete user data when they disconnect)
  - [ ] Submit application to developers@strava.com
- [ ] Test RevenueCat integration
  - [ ] Cancellation - Play Store → cancel → verify webhook updates status, still have access until expiry
  - [ ] Expiration - Wait for sandbox sub to expire → verify redirect to paywall (status = expired)
  - [ ] Restore purchases - Log out, log back in → "Already subscribed? Tap here" → verify restores access
  - [ ] Plan upgrade - Switch monthly to annual (tests PRODUCT_CHANGE webhook)
  - [ ] Resubscribe after cancel - After cancelling, subscribe again from management screen
  - [ ] New user flow - Fresh account → sees paywall after trial expires
  - [ ] iOS testing - TestFlight if available
- [ ] Security audit
- [ ] Publish to Play Store

**UX Improvements:**

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
- [ ] Chat page doesn't auto-refresh the chats on opening
- [ ] Onboarding flow should allow going back to previous slide
