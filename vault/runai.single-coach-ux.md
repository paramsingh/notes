---
id: runai-single-coach-ux-7n2k4p
title: RunAI Single Coach UX Exploration
desc: ''
updated: 1737216000000
created: 1737216000000
---

> This note was generated with AI assistance.

# Single Coach Relationship - UX Exploration

## Problem

Current app has multiple chat threads (general chat, chat per run, etc.). This feels like customer support tickets, not a coaching relationship. Users don't build a relationship with their coach.

## Vision

One ongoing conversation with Coach Vayu. Like texting your real running coach.

- **Single thread**: No "new chat" button. Just your coach.
- **Coach remembers everything**: Past conversations, your goals, your injury history, what worked/didn't
- **Runs feed in automatically**: Coach sees your runs and can comment proactively
- **Proactive coaching**: "Nice 5k this morning - saw you negative split the last mile!" or "You mentioned your knee was bothering you, how's it feeling after today's run?"
- **Home screen = coach**: Open app, you're talking to your coach

## Questions to Explore

### Data Model
- How does coach memory work? Separate memory tool that writes to DB?
- What gets remembered vs what's just conversation context?
- How do runs feed into the conversation? As system messages? Tool results?
- Single conversation thread in DB, or something else?

### UI/UX
- What does home screen look like? Just a chat interface?
- Where do runs live? Still a separate tab, or integrated into coach view?
- How does coach initiate? Push notifications? Messages waiting when you open app?
- What happens to existing multiple-chat UI? Migration path?

### Proactive Coaching
- When does coach reach out? After every run? Daily summary? Only notable events?
- How to avoid being annoying?
- Does this require background processing / cron jobs?

### Technical
- How does this change the current chat/conversation architecture?
- What's the minimal change to test this hypothesis?
- Can we prototype with current infra or need new backend work?

## Current Architecture (for context)

Help me understand:
1. Current chat/conversation data model
2. How AI coach currently gets context about runs
3. Where conversation history is stored
4. Current home screen / navigation structure

Then let's sketch out what minimal changes would let us test the single-coach model.
