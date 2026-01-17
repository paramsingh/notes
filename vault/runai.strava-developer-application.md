---
id: runai-strava-dev-app-p7k4n2
title: RunAI Strava Developer Application
desc: ''
updated: 1768570313593
created: 1736438400000
---

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
