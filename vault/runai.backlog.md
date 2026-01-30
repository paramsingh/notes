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

- [ ] Add "Founding Member" lifetime pricing tier
  - $149 / 12,499 INR lifetime access
  - Limited to first 50 members
  - Show remaining count in paywall
  - Founding member badge/perk
  - Remove once sold out, never bring back at this price

- [x] Choose new app name (RunAI is taken) → **Coach Vayu** (coachvayu.com)
  - Blocks: domain, landing page, privacy policy, Strava approval, Play Store
  - [x] Update name throughout frontend (app title, strings, etc.)
- [x] Buy domain and set up landing page
  - [x] Buy domain (coachvayu.com)
  - [x] Host landing page with privacy policy and terms of service
- [x] Pull recent runs from Strava API during signup (last 30-60 days) - LAUNCH BLOCKER ✓
- [ ] Get Strava approval (brand guidelines review) - RESUBMITTED Jan 29
  - [x] Review and customize Strava Developer Program application email draft (RunAI → Coach Vayu)
  - [x] Fill in Client ID, name, email, website URL, privacy policy URL
  - [x] Take required screenshots (login, settings, run details, AI chat)
  - [x] Implement "View on Strava" deep links ✓
  - [x] Implement deauthorization webhook ✓
  - [x] Submit application to developers@strava.com ✓
  - [x] Respond to AI usage clarification request (Jan 29)
  - [x] Update privacy policy & ToS with explicit AI data usage language
  - Waiting for final decision. If rejected, plan is open source minus payments.
- [x] Test RevenueCat integration ✓ (verified Jan 17)
  - [x] Cancellation ✓
  - [x] Expiration ✓
  - [x] Restore purchases ✓
  - [x] Plan upgrade ✓
  - [x] Resubscribe after cancel ✓
  - [x] New user flow - double check before release ✓
  - [ ] iOS testing - later
- [ ] Security audit
- [ ] Final pre-launch check
  - [ ] Auth flows: login, logout, token refresh
  - [ ] Payment flows: subscribe, restore, cancel
  - [ ] Auto-import runs after OAuth
  - [ ] New user end-to-end (signup → import → chat with coach → paywall)
- [ ] Publish to Play Store

**UX Improvements:**

- [ ] Rethink core flow: single coach relationship instead of multiple chats
  - One ongoing conversation with Coach Vayu (not chat per run, general chat, etc.)
  - Coach remembers everything (needs memory tool)
  - Runs feed into conversation as context
  - Coach is proactive ("Nice 5k this morning, saw you negative split")
  - No "start new chat" - just talk to your coach
  - Home screen = your coach conversation
  - Feels like a relationship, not customer support tickets

- [ ] Add loading/status messages during AI coach tool calls (e.g., "Analyzing your runs...", "Looking at your pace data...")
- [ ] Remove "upload FIT file" feature
- [ ] Review end-to-end UX - make sure flows make sense for new users
- [ ] Add tooltips/coach marks for first-time viewing of key pages
- [ ] Improve run page design
- [ ] Start conversation from coach's notes (tap note on run page → opens chat with context)
- [ ] Work on onboarding flow

**Features:**

- [ ] Give coach a memory tool (writes to database) - persistent context across conversations
- [ ] Coach can search/analyze past runs
- [ ] Design and implement onboarding screens with 30-day free trial messaging
- [ ] Add streaming responses to chat interface
- [ ] Finalize app-wide color scheme and redesign entire app based on it

**Launch Strategy:**

Pre-launch:
- [ ] Collect beta tester testimonials (2-3 quotes)
- [ ] Set up analytics (Mixpanel/Amplitude) - track funnel
- [ ] Add email waitlist to coachvayu.com
- [ ] Tease on Twitter/socials before launch

Launch day:
- [ ] Product Hunt launch (coordinate timezone, early upvotes)
- [ ] Hacker News "Show HN" post
- [ ] Reddit: r/running, r/AdvancedRunning, r/triathlon
- [ ] Strava clubs / running Discord servers
- [ ] Personal network push (WhatsApp, LinkedIn)

In-app growth:
- [ ] Review prompt after positive interaction
- [ ] Referral mechanism ("Give a friend 1 month free, get 1 month free")
- [ ] Share run analysis to socials feature

ASO (App Store Optimization):
- [ ] Keywords in title/description (AI running coach, training plan)
- [ ] Screenshots that show value, not just UI
- [ ] Compelling first sentence in description

Post-launch:
- [ ] Respond to every review
- [ ] Weekly content (running tips) for SEO
- [ ] Reach out to running bloggers/YouTubers

**Infrastructure:**

- [x] Automate build and Play Store upload (script EAS build → download AAB → upload to Play Store)
- [ ] Research Strava API user limit increase process and apply for higher limits
- [ ] Create landing page and host privacy policy and other legal docs

**Bugs:**

**AI Coach Quality (embarrassing to show):**
- [ ] Date/day off-by-one errors in training plans (says Thursday but means Friday)
- [ ] Tool call confusion - AI doesn't realize what happened, says "looks like plan is already updated"
- [ ] Uses markdown formatting in chat messages (should be plain text)
- [ ] Analysis errors - wrong conclusions about runs (e.g., "too hard" when clearly zone 2)
- [ ] Too slow - needs performance optimization

**Critical (blocks new user flow):**
- [x] Navigation broken after login - clicking anything flickers and returns to main page
- [x] App opens to runs page by default instead of login page when not authenticated
- [x] Fix privacy policy and terms of service pages on paywall
- [x] Restore purchases button unclear - needs better UX and verification it works

**Medium priority:**
- [x] Manage subscription page should show cancelled status and expiry date when subscription is cancelled
- [ ] Chat page doesn't auto-refresh the chats on opening
- [ ] Onboarding flow should allow going back to previous slide

---

## New Project Ideas

**Grimoire** (exploring while waiting on Strava)
- Mobile app that brings Claude Code experience to phone
- Chat with Claude, it can read/write files in a notes folder
- "Claude that knows your life and can read/write your second brain"
- BYOK (Bring Your Own Key), Android-first, dark mode, fantasy-themed
- Design doc: [[engineering.grimoire]]

---

## Extracted Libraries

Reusable packages extracted from Coach Vayu codebase:

- **vayu-storage** - Cross-platform secure storage (SecureStore/localStorage)
  - https://github.com/paramsingh/vayu-storage
- **vayu-auth** - Token-based auth utilities with auto-refresh
  - https://github.com/paramsingh/vayu-auth
- **vayu-subscriptions** - RevenueCat subscription management wrapper
  - https://github.com/paramsingh/vayu-subscriptions
