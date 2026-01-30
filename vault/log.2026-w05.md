---
id: runai-2026-w05-x7n4q2
title: RunAI Week 5 (Jan 24-30)
desc: ''
updated: 1738195200000
created: 1738195200000
---

# Week 5 (Jan 24-30)

[[log.2026-w04|← prev]] | next →

## Theme
Strava Response + New Project Exploration

## Context
Strava responded on Jan 29 asking for more details about AI usage. Resubmitted with detailed explanation of inference-only approach. Waiting for final decision. Started exploring Claude Code mobile app idea as potential next project.

## This Week

### Strava Resubmission
- [x] Draft response addressing AI usage questions
- [x] Update privacy policy with explicit AI data usage language
- [x] Update ToS with "AI and Data Usage" section
- [x] Research Strava's history with AI app approvals/rejections
- [x] Submit resubmission

### New Project: Grimoire
- [x] Create design doc v1 (engineering.claude-code-mobile.md)
- [x] Design interview and v2 design doc (engineering.grimoire.md)
- [x] Clone Codex CLI for architecture reference
- [x] Extract reusable libraries from RunAI codebase

### Library Extraction
Created three reusable open-source packages:
- [x] vayu-storage - Cross-platform secure storage
- [x] vayu-auth - Token-based auth utilities
- [x] vayu-subscriptions - RevenueCat wrapper

GitHub repos:
- https://github.com/paramsingh/vayu-storage
- https://github.com/paramsingh/vayu-auth
- https://github.com/paramsingh/vayu-subscriptions


## Daily

### Fri Jan 24
**Did:**
**Blockers:**
**Notes:**

### Sat Jan 25
**Did:**
**Blockers:**
**Notes:**

### Sun Jan 26
**Did:**
**Blockers:**
**Notes:**

### Mon Jan 27
**Did:**
**Blockers:**
**Notes:**

### Tue Jan 28
**Did:**
**Blockers:**
**Notes:**

### Wed Jan 29
**Did:**
- Received Strava email requesting AI usage clarification
- Researched Anthropic's commercial terms (no training on API data)
- Updated privacy.html and terms.html with explicit AI data usage policy
- Drafted and submitted Strava resubmission addressing all 4 questions
- Researched Strava's history with AI apps (Roast My Strava approved, Runna acquired)
- Added contingency plan to strava application note (open source if rejected)
- Created design doc for Claude Code mobile app
- Extracted vayu-storage, vayu-auth, vayu-subscriptions from RunAI
- Created GitHub repos for all three libraries
**Blockers:**
- Waiting on Strava approval
**Notes:**
- Roast My Strava precedent is encouraging - they approved an AI app that analyzes user data
- Risk: Strava acquired Runna (AI coaching app) in April 2025, might see us as competition
- If rejected, plan is to open source Coach Vayu minus payments

### Thu Jan 30
**Did:**
- Deep design session for Grimoire (Claude Code mobile app)
- Cloned Codex CLI repo for architecture reference
- Created comprehensive v2 design doc with all decisions locked
- Researched Codex context management, tools, conversation history
**Blockers:**
- Still waiting on Strava approval
**Notes:**
- Key patterns from Codex: on-demand tools, append-only history, session persistence, truncation
- Grimoire: BYOK, Opus, Android-first, session-based chat, fantasy-themed loading messages
- Ready to start building v0.1 when time allows

## Review
<!-- End of week: what got done, what didn't, why, revenue impact -->
