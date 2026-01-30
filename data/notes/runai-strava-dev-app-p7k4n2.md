
# Coach Vayu Strava Developer Application

> This note was generated with AI assistance.

Application materials for Strava Developer Program to increase athlete capacity beyond Single Player Mode. App formerly known as RunAI, now Coach Vayu.

## Application Email Draft

To: developers@strava.com
Subject: Developer Program Application & Athlete Limit Increase - Coach Vayu (Client ID: 157267)

---

Hi,

I'm Param, and I'm building Coach Vayu - an AI running coach that syncs with Strava. I've been using it myself for the past few months and I'm ready to expand to a limited beta with friends and other running enthusiasts. I'd like to apply for the Developer Program to get my app reviewed and increase the athlete limit (currently 1) to around 100.

Since this is an early beta, the landing page and screenshots aren't super polished yet - but the app itself is functional and ready for testing.

App Details:
  Name: Coach Vayu
  Client ID: 157267
  Website: https://coachvayu.com (work in progress)
  Privacy Policy: https://coachvayu.com/privacy
  Terms of Service: https://coachvayu.com/terms
  Contact: me@param.codes


What it does

Coach Vayu is a conversational AI running coach. Users connect their Strava, and the app automatically imports their runs via webhooks. They can then chat with the AI coach to get personalized feedback on their training - things like pacing analysis, recovery suggestions, and training plans based on their actual run history.


How I use Strava data

  Authentication: Strava OAuth only (no separate passwords)
  Run syncing: Webhook-driven automatic imports
  Data displayed: Distance, duration, pace, heart rate, cadence, splits
  Scopes: read,activity:read_all,read_all


Brand compliance

I've followed the Strava brand guidelines:
  - Official "Connect with Strava" orange button on login (see screenshot 1)
  - "Powered by Strava" logo in Settings (see screenshot 2)
  - "View on Strava" deep links on run details (see screenshot 3)
  - No Strava marks in app name or icon

I've also implemented the deauthorization webhook - when a user revokes access, I delete their tokens and delete their data immediately.


Screenshots attached

  1. Login screen with Connect with Strava button
  2. Settings with Powered by Strava
  3. Run detail with View on Strava link
  4. AI coach chat analyzing a run


Technical details

Stack:
  - Backend: Python Flask on Fly.io
  - Mobile: React Native/Expo (Google Play Store)
  - Database: SQLite with multi-user support
  - AI: Claude

Webhook integration:
  - Subscribed to activity creation events
  - Auto-imports runs when athletes complete activities
  - Only processes run-type activities (Run, TrailRun, VirtualRun)
  - Deauthorization webhook deletes tokens and all user data immediately

Security:
  - HTTPS everywhere
  - JWT session management
  - Complete data isolation between users
  - Strava tokens stored securely, refreshed automatically


Expected API usage

  - Default rate limits (200/15min, 2000/day) should be plenty for now
  - Main API calls: OAuth token exchange, webhook processing, activity fetching
  - Webhook-driven = minimal polling
  - Targeting 50-100 users initially, maybe 200-500 in first 6 months
  - Will request increases if I approach limits


Current status

Ready to launch:
  - Production backend deployed
  - RevenueCat subscriptions working
  - Multi-user data isolation
  - Play Store submission in progress

Let me know if you need anything else.

Thanks,
Param Singh
me@param.codes
https://coachvayu.com

---

## Form Submission Cheat Sheet

Form URL: https://share.hsforms.com/1VXSwPUYqSH6IxK0y51FjHwcnkd8

Fill in with these values:

App/Client ID: 157267
App Name: Coach Vayu
Your Name: Param Singh
Email: me@param.codes
Website: https://coachvayu.com
Privacy Policy: https://coachvayu.com/privacy
Terms of Service: https://coachvayu.com/terms
Support URL: https://coachvayu.com

What does your app do?
Coach Vayu is a conversational AI running coach. Users connect their Strava, and the app automatically imports their runs via webhooks. They can chat with the AI coach to get personalized feedback - pacing analysis, recovery suggestions, and training plans based on their actual run history.

How do you use Strava data?
- Authentication: Strava OAuth only (no separate passwords)
- Run syncing: Webhook-driven automatic imports
- Data displayed: Distance, duration, pace, heart rate, cadence, splits
- Scopes: read,activity:read_all,read_all

How many athletes/users do you need?
Around 100 - this is for a limited beta with friends and running enthusiasts. I've been testing the app myself for months and am ready to expand.

How have you implemented Strava branding?
- Official "Connect with Strava" orange button on login
- "Powered by Strava" logo in Settings
- "View on Strava" deep links on run details
- No Strava marks in app name or icon
- Deauthorization webhook implemented - deletes tokens and all user data immediately when user revokes access

Expected API usage?
- Default rate limits (200/15min, 2000/day) should be plenty
- Webhook-driven architecture = minimal polling
- Targeting 50-100 users initially

Anything else?
This is an early beta - the landing page and screenshots aren't super polished yet, but the app is functional and ready for testing.

Attach screenshots:
1. coach-vayu-01-login-strava-connect.png
2. coach-vayu-02-settings-powered-by-strava.png
3. coach-vayu-03-run-detail-view-on-strava.png
4. coach-vayu-04-ai-coach-chat.png

---

## Attachments

Screenshots ready in `~/Downloads/`:
- [x] `coach-vayu-01-login-strava-connect.png` - Login with "Connect with Strava" button
- [x] `coach-vayu-02-settings-powered-by-strava.png` - Settings with "Powered by Strava" logo
- [x] `coach-vayu-03-run-detail-view-on-strava.png` - Run detail with "View on Strava" link
- [x] `coach-vayu-04-ai-coach-chat.png` - AI coach analyzing a run

---

## Resubmission (2026-01-29)

Strava requested more information about AI usage. This is the follow-up submission.

### Form Submission Cheat Sheet

Form URL: https://share.hsforms.com/1VXSwPUYqSH6IxK0y51FjHwcnkd8

**First name:** Param
**Last name:** Singh
**Email Address:** me@param.codes
**Company Name:** Coach Vayu
**API Application Name:** Coach Vayu
**Strava Client ID:** 157267
**Additional Apps:** 193648
**Number of Currently Authenticated Users:** 1
**Number of Intended Users:** 100
**Support URL:** https://coachvayu.com/support

**Application Description:** (copy below)

---

This is a resubmission for Client ID 157267, following your email requesting more information about AI usage.

Coach Vayu is a conversational AI running coach. Users connect their Strava, and the app automatically imports their runs via webhooks. They can chat with the AI coach to get personalized feedback—pacing analysis, recovery suggestions, and training plans based on their actual run history.

**AI Usage & Compliance**

1. Does the app involve AI?
Yes—users chat with an AI coach (Claude, via Anthropic's API) to get feedback on their training.

2. How is Strava data used with AI?
When a user asks for coaching advice, their activity data is included as context in the request to Claude. The AI analyzes it and returns personalized feedback. No Strava data is ever used to train, fine-tune, or pre-train any AI model—it's only used for real-time analysis to help that individual user.

3. Compliance with your training restrictions?
No Strava data is used to train AI models. Claude is a pre-trained model; we only use it for inference. Anthropic's Commercial Terms (https://www.anthropic.com/legal/commercial-terms) explicitly state "Anthropic may not train models on Customer Content from Services"—so even our AI provider is contractually prohibited from training on this data.

4. Third-party access?
Only Anthropic's Claude API processes the data (for generating responses). They cannot use it for training. No other third parties have access. Each user's data is completely isolated.

**Other API Agreement Compliance**

- Data deletion: Deauthorization webhook immediately deletes all user tokens and data. Activity deletion webhooks remove activities from our database. Users can request full data deletion at any time.
- Data isolation: Each user only sees their own activities. No data is aggregated or shared across users.
- Security: All data transmitted over HTTPS. Strava tokens stored securely and refreshed automatically. JWT-based session management.
- Monetization: Subscription fees are for AI coaching functionality, not for access to Strava data.
- Brand compliance: "Connect with Strava" button on login, "Powered by Strava" in settings, "View on Strava" deep links on activities.

Our privacy policy (https://coachvayu.com/privacy) and terms of service (https://coachvayu.com/terms) explicitly document our AI data practices.

Happy to clarify anything else.

---

**TOS Compliance:** ✓ (check)
**Brand Guidelines Review:** ✓ (check)

**App Images:** (same screenshots as before)
1. coach-vayu-01-login-strava-connect.png
2. coach-vayu-02-settings-powered-by-strava.png
3. coach-vayu-03-run-detail-view-on-strava.png
4. coach-vayu-04-ai-coach-chat.png

---

## If Rejected: Research & Contingency Plan

### Strava API Policy Context (Nov 2024 changes)

Key restrictions:
1. **AI/ML Prohibition** - Third parties cannot use Strava data for AI model training OR AI processing
2. **Data privacy** - Cannot show user data to anyone other than that user (breaks coach-athlete relationships)
3. **No replicating Strava** - Can't copy their look/feel/functionality

### Precedent: Apps That Got Approved Despite Using AI

**Roast My Strava** - AI app that generates humorous commentary from Strava data. Approved, won award at 2025 Strava Developer Summit, 75k+ users. Key pattern: AI analyzes individual user's own data, returns insights to that same user only.

### The Critical Distinction

- **Prohibited**: Training models on Strava data, sharing data with third parties/coaches
- **Potentially allowed**: AI processing individual user's own data to provide insights back to them

Coach Vayu fits the "potentially allowed" pattern:
- Only processes each user's own data ✓
- Insights go back only to that same user ✓
- No model training (Anthropic contractually prohibited too) ✓
- Doesn't replicate Strava functionality ✓

### Risk: Strava Acquired Runna (April 2025)

Runna is an AI running coaching app. Strava may want to own this space themselves and view third-party AI coaches as competition.

### Workarounds Other Devs Have Used

1. **Direct Garmin Connect integration** - TrainerRoad, Intervals.icu did this
2. **Apple Health / device sources** - Bypass Strava entirely
3. **Minimal feature approach** - Strip down to essentials
4. **Appeal with "user-only insights" framing** - Cite Roast My Strava precedent

### Contingency: Open Source

If rejected outright, open source the app (minus RevenueCat/payment bits). Let others self-host with their own Strava API keys in single-player mode.

### Sources

- [Strava's Big Changes Aim To Kill Off Apps - DC Rainmaker](https://www.dcrainmaker.com/2024/11/stravas-changes-to-kill-off-apps.html)
- [Updates to Strava's API Agreement - Strava Press](https://press.strava.com/articles/updates-to-stravas-api-agreement)
- [Developer Voices: Roast My Strava - Strava Community Hub](https://communityhub.strava.com/insider-journal-9/developer-voices-from-weekend-side-project-to-community-sensation-how-i-built-roast-my-strava-12288)
- [Strava to Acquire Runna - Strava Press](https://press.strava.com/articles/strava-to-acquire-runna-a-leading-running-training-app)
