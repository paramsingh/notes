---
id: runai-strava-dev-app-p7k4n2
title: RunAI Strava Developer Application
desc: ''
updated: 1736438400000
created: 1736438400000
---

# RunAI Strava Developer Application

> This note was generated with AI assistance.

Application materials for Strava Developer Program to increase athlete capacity beyond Single Player Mode.

## Application Email Draft

**To:** developers@strava.com
**Subject:** Strava Developer Program Application - RunAI (Client ID: [YOUR_CLIENT_ID])

---

Hello Strava Developer Team,

I'm applying to the Strava Developer Program to increase the athlete capacity for my application **RunAI**, an AI-powered running coach.

**Application Details:**

**App Name:** RunAI
**Client ID:** [INSERT YOUR STRAVA CLIENT ID]
**Developer:** [YOUR NAME]
**Contact Email:** [YOUR EMAIL]
**Target Launch Date:** Late January 2026
**Hosting:** Fly.io (backend), Google Play Store (mobile app)

### What RunAI Does

RunAI is a personal AI running coach that provides individualized training guidance through natural conversation. The app:

- Analyzes runners' workout data to provide specific, personalized feedback
- Generates adaptive training plans based on individual fitness levels and goals
- Learns each athlete's unique patterns over time to deliver increasingly relevant coaching
- Offers 24/7 availability at a fraction of the cost of human coaching ($10-12/month vs $50-100/session)

Unlike generic training apps with rigid templates, RunAI builds genuine understanding of each runner through conversational AI, adapting to their life circumstances, feedback, and performance patterns.

### How We Use Strava Data

**Primary Use Cases:**
1. **Authentication:** Strava OAuth is our sole authentication method (no separate passwords)
2. **Automatic Run Syncing:** Real-time activity import via Strava webhooks
3. **AI Coaching Analysis:** Run metrics fuel personalized training recommendations

**Strava Data Displayed:**
- Distance, duration, pace, speed
- Heart rate data (average and maximum)
- Elevation gain
- Cadence, power, and temperature (when available)
- GPS route data and split breakdowns
- Activity timestamps and types

**OAuth Scopes Requested:**
`read,activity:read_all,read_all`

**Data Flow:**
- User authenticates via Strava OAuth
- Strava webhook notifications trigger automatic run imports
- AI coach analyzes run data to provide feedback and generate training plans
- Users chat with AI coach about their runs and training goals

### Strava Brand Compliance

We have implemented all required Strava branding guidelines:

✅ **Official "Connect with Strava" Button:**
- Using official orange button asset from Strava's brand guidelines
- Implemented in login screen with proper dimensions (48px height)
- Links to official Strava OAuth endpoint

✅ **"Powered by Strava" Attribution:**
- Horizontal logo displayed in app Settings screen
- Proper sizing and placement per brand guidelines
- Uses official gray variant asset

✅ **App Naming:**
- App name "RunAI" does not contain Strava references
- No Strava marks in app icon or branding

✅ **Data Attribution:**
- Clear indication that run data comes from Strava
- Proper Strava branding prominence

**Screenshots:** (See attached)
1. Login screen with official "Connect with Strava" button
2. Settings screen showing "Powered by Strava" logo
3. Run detail screen displaying Strava activity data
4. Chat interface with AI coach analyzing Strava runs

### Why We Need Increased Capacity

RunAI is ready for public launch within 1-2 weeks. We've completed:
- Multi-user authentication system with full data isolation
- Production deployment on Fly.io
- RevenueCat subscription integration for monetization
- Play Store submission preparation
- Comprehensive Strava brand compliance

We need to move beyond Single Player Mode (1 athlete limit) to:
1. Conduct beta testing with initial users
2. Launch publicly on Google Play Store
3. Serve paying customers seeking personalized AI coaching

### Technical Implementation

**Architecture:**
- Backend: Python Flask (Fly.io)
- Mobile: React Native/Expo (Google Play Store)
- Database: SQLite with multi-user support
- AI: Anthropic Claude, OpenAI, Google Gemini

**Security & Privacy:**
- HTTPS encryption for all data in transit
- Secure JWT session management
- Complete data isolation between users
- Strava tokens stored securely and refreshed automatically
- Webhook signature validation for security

**Webhook Integration:**
- Subscribed to Strava webhook events for activity creation
- Automatic run import when athletes complete activities
- Only processes run-type activities (Run, TrailRun, VirtualRun)
- Generates AI summaries automatically on import

### Expected API Usage

**Rate Limits:**
- Current default limits (200 requests/15 min, 2000/day) should be sufficient initially
- Primary API calls: OAuth token exchange, webhook event processing, activity detail fetching
- Webhook-driven architecture minimizes polling needs

**User Growth:**
- Target: 50-100 beta users in first month
- Expected growth: 200-500 users within first 3 months post-launch
- Will request rate limit increases if we approach capacity with 100+ active users

### Commitment to Strava Community

RunAI enhances the Strava ecosystem by:
- Providing valuable AI coaching services that complement Strava's platform
- Encouraging consistent training and engagement with Strava
- Maintaining high standards for data privacy and security
- Following all Strava API terms and brand guidelines

We're committed to being a responsible developer partner and will:
- Keep Strava branding updated with any guideline changes
- Monitor and optimize API usage efficiency
- Respond promptly to any compliance concerns
- Provide excellent user experience that reflects well on Strava

### Next Steps

Please let me know if you need any additional information or screenshots. I'm happy to provide:
- Demo access to the application
- Additional technical documentation
- More detailed screenshots of Strava integration
- Answers to any questions about our implementation

Thank you for considering this application. I look forward to joining the Strava Developer Program and bringing RunAI's personalized AI coaching to the running community.

Best regards,
[YOUR NAME]
[YOUR EMAIL]
[OPTIONAL: Website URL]

---

## Attachments Checklist

Before sending, prepare these screenshots:

- [ ] Login screen with "Connect with Strava" button (clear, high-res)
- [ ] Settings screen showing "Powered by Strava" logo
- [ ] Run detail screen with Strava data displayed
- [ ] Example of AI coach analyzing a run
- [ ] Chat interface showing personalized training plan
- [ ] (Optional) App icon and branding

**Screenshot Guidelines:**
- High resolution (2x or 3x scale if possible)
- Show the app in use with real data (can blur personal info)
- Highlight Strava branding elements clearly
- Include different screens to show full integration

## Application Form (if web form exists)

If submitting via web form instead of email, use these responses:

**App Name:** RunAI

**App Description (short):**
AI-powered running coach providing personalized training plans and feedback through natural conversation. Uses Strava for authentication and automatic run syncing.

**App Description (detailed):**
[Use "What RunAI Does" section above]

**Website URL:**
[Your website or landing page URL - create if needed]

**Privacy Policy URL:**
[Host the privacy policy and provide URL]

**How does your app use Strava data?**
[Use "How We Use Strava Data" section above]

**What Strava API scopes do you request?**
`read,activity:read_all,read_all`

**OAuth scopes justification:**
- `read`: Access to basic athlete profile information for account creation
- `activity:read_all`: Read all activity data including runs for AI coaching analysis
- `read_all`: Access to detailed activity metrics (heart rate, pace, splits, etc.) needed for personalized feedback

**How have you implemented Strava branding?**
[Use "Strava Brand Compliance" section above]

**Expected number of users:**
50-100 beta users initially, growing to 200-500 within 3 months of public launch

**Expected API request volume:**
Within default rate limits (200/15min, 2000/day). Will request increases if we approach capacity with 100+ active users.

## Before Submitting

- [ ] Insert your actual Strava Client ID
- [ ] Add your name and email
- [ ] Take all required screenshots
- [ ] Ensure "View on Strava" links are implemented (currently missing)
- [ ] Host privacy policy and add URL
- [ ] Create website/landing page if needed
- [ ] Review all screenshots for quality and clarity
- [ ] Double-check all Strava branding is visible and correct
- [ ] Test the full OAuth flow one more time
- [ ] Verify webhook integration is working

## Action Items

**CRITICAL - Implement before submission:**
- [ ] Add "View on Strava" deep links to run detail screens (per Strava brand guidelines)
  - Link format: `https://www.strava.com/activities/{activity_id}`
  - Style: Orange color (#FC5200), bold, or underlined
  - Location: Run detail screens where activity data is shown

**Nice to have:**
- [ ] Create simple landing page (runai.com or GitHub Pages)
- [ ] Host privacy policy at public URL
- [ ] Prepare demo video (optional but impressive)
