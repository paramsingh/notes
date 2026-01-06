# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal notes repository using [Dendron](https://wiki.dendron.so/), a hierarchical note-taking system. Notes are published to https://notes.param.codes.

## Commands

**Local development:**
```bash
npx dendron publish dev
```

**Build and export for publishing:**
```bash
npx dendron publish init
npx dendron publish export --target github --yes
```

## Structure

- `vault/` - Main notes directory containing all markdown files
- `vault/assets/images/` - Images referenced in notes
- `phone/` - Notes synced from mobile
- `.github/workflows/publish.yml` - GitHub Actions workflow that builds and deploys to GitHub Pages on push to main

## Dendron Conventions

Notes use hierarchical naming with dots as separators (e.g., `books.the_three_body_problem.md`, `chess.kingside_attack.md`). This creates a tree structure where `chess.md` is the parent of `chess.kingside_attack.md`.

**Frontmatter format** - all notes must have this structure:
```yaml
---
id: some-unique-id-abc123
title: Note Title
desc: ''
updated: 1736092800000
created: 1736092800000
---
```
- `id`: alphanumeric with hyphens (NOT dot notation like `runai.backlog`)
- `created`/`updated`: Unix timestamps in milliseconds (NOT date strings)

## AI-Generated Content

Any note written by AI must include this disclaimer at the top of the file (after the frontmatter):

```
> This note was generated with AI assistance.
```

## RunAI Project Tracking

The user is building RunAI, an AI running coach app (codebase at `~/runai`). There's an AI-assisted workflow for tracking work:

**Files:**
- `vault/runai.backlog.md` - Master backlog, ordered by priority (top = do first)
- `vault/runai.YYYY-wWW.md` - Weekly notes (e.g., `runai.2025-w02.md`)

**Workflow:**
- **Weekly planning**: Review backlog → pick theme + 4-5 tasks → challenge if picks don't align with revenue goal
- **Daily**: User shares what they worked on → update daily section with what done, blockers, notes → brainstorm if stuck → new ideas go to bottom of backlog
- **Weekly review**: Compare done vs planned → assess revenue impact → analyze blockers → feeds into next week's planning

**When user mentions runai work**: Check the current week's note and backlog to understand context. Use the AskUserQuestion tool to interview/clarify when needed.
