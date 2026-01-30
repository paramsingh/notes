---
id: grimoire-design-v2
title: Grimoire - Design Doc
desc: ''
updated: 1738252800000
created: 1738164600000
---

> This note was generated with AI assistance.

# Grimoire - Design Doc v2

## Concept

**Grimoire** - A mobile app that brings the Claude Code experience to your phone. Chat with Claude, and it can read/write files in a notes folder on your device. Open canvas, user-defined workflows.

**Core value prop:** "Claude that can read/write your files, and you can see everything it knows."

**Differentiators:**
- Files on YOUR device - portable, private, auditable
- Transparency - see exactly what the AI knows (not a black box)
- Conversational-first - talk to manage your notes, not manual editing
- AI as author - detailed notes because Claude writes them
- Open canvas - no opinionated workflow, you define how you use it

## Key Decisions

| Decision | Choice |
|----------|--------|
| **Name** | Grimoire |
| **Pricing** | BYOK (Bring Your Own Key) - no backend |
| **Model** | Claude Opus |
| **Platform** | Android-first (Pixel 10 Pro), iOS via Expo |
| **Home screen** | Chat - open canvas |
| **Conversations** | Session-based (fresh each time, notes persist) |
| **Context limit** | Auto-compact when exceeded |
| **File structure** | Subfolders allowed, Claude organizes |
| **Storage** | App documents (private) |
| **Personality** | Subtle fantasy flavor |
| **Dark mode** | Yes (must-have) |
| **Share extension** | Yes (must-have) |

## Tools (7 total)

Codex-compatible where possible, plus simple write/edit for notes.

```typescript
const tools = [
  // === Codex-compatible read tools ===
  {
    name: "list_dir",
    description: "Lists entries in a directory with type labels (file/dir)",
    input_schema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description: "Path to directory (relative to notes root, defaults to root)"
        },
        offset: {
          type: "number",
          description: "Entry number to start from (1-indexed)"
        },
        limit: {
          type: "number",
          description: "Maximum number of entries to return"
        },
        depth: {
          type: "number",
          description: "Maximum directory depth to traverse (1 = current dir only)"
        }
      }
    }
  },
  {
    name: "read_file",
    description: "Reads a file with 1-indexed line numbers",
    input_schema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description: "Path to file (relative to notes root)"
        },
        offset: {
          type: "number",
          description: "Line number to start reading from (1-indexed)"
        },
        limit: {
          type: "number",
          description: "Maximum number of lines to return"
        }
      },
      required: ["path"]
    }
  },
  {
    name: "grep_files",
    description: "Search for pattern across files, returns matching files sorted by modification time",
    input_schema: {
      type: "object",
      properties: {
        pattern: {
          type: "string",
          description: "Regular expression pattern to search for"
        },
        include: {
          type: "string",
          description: "Glob to filter files (e.g. '*.md', 'projects/**/*.md')"
        },
        path: {
          type: "string",
          description: "Directory to search (defaults to notes root)"
        },
        limit: {
          type: "number",
          description: "Maximum number of results (defaults to 100)"
        }
      },
      required: ["pattern"]
    }
  },
  {
    name: "view_image",
    description: "View an image file from the notes folder",
    input_schema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description: "Path to image file (relative to notes root)"
        }
      },
      required: ["path"]
    }
  },

  // === Notes-specific write tools ===
  {
    name: "write_file",
    description: "Create a new file or overwrite an existing one",
    input_schema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description: "Path to file (can include subdirectories, will be created)"
        },
        content: {
          type: "string",
          description: "Content to write"
        }
      },
      required: ["path", "content"]
    }
  },
  {
    name: "edit_file",
    description: "Edit a file by finding and replacing text",
    input_schema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description: "Path to file"
        },
        old_text: {
          type: "string",
          description: "Text to find (must be unique in file)"
        },
        new_text: {
          type: "string",
          description: "Text to replace with"
        }
      },
      required: ["path", "old_text", "new_text"]
    }
  },
  {
    name: "delete_file",
    description: "Delete a file or empty directory",
    input_schema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description: "Path to file or empty directory to delete"
        }
      },
      required: ["path"]
    }
  }
]
```

## System Prompt

```
You are the spirit of Grimoire, a magical tome that helps the user manage their personal knowledge. You have access to their notes folder and can read, write, edit, search, and view images.

Available tools:
- list_dir: See what files and folders exist (supports depth for nested view)
- read_file: Read a file's contents (supports offset/limit for large files)
- grep_files: Search for patterns across files (supports glob filtering)
- view_image: Look at an image in the notes folder
- write_file: Create or overwrite a file (creates subdirectories as needed)
- edit_file: Modify part of a file by finding and replacing text
- delete_file: Remove a file or empty directory

Guidelines:
- When the user asks about something, check if there's a relevant note first
- Organize notes logically - use subdirectories when it makes sense
- Use markdown formatting in notes
- When updating notes, preserve existing content unless asked to replace
- Be transparent about what files you're reading/writing
- Keep a subtle magical flavor in your responses, but stay practical and helpful
- When the user shares an image, you can save it and reference it in notes

First conversation: Welcome the user and ask what they'd like to use Grimoire for.
```

## Context Management (inspired by Codex)

- **On-demand tools** - read files only when needed for the task
- **No auto file list** - Claude discovers via `list_files` when relevant
- **Session-based** - conversation resets on app open, notes persist
- **Auto-compact** - when context limit hit, summarize older messages
- **Environment injection** - tell Claude the notes folder path

## UI/UX

### Loading Messages (whimsical, fantasy-themed)

While Claude is thinking or executing tools:
- "Consulting the archives..."
- "Scrying your notes..."
- "Leafing through the tome..."
- "Channeling ancient wisdom..."
- "Inscribing new knowledge..."
- "Divining connections..."
- "Weaving the threads..."

### Screens

1. **Chat Screen (main)**
   - Full-screen chat, message input at bottom
   - Streaming responses with fantasy loading messages
   - Tool calls shown inline ("📖 Reading projects/coach-vayu.md...")
   - Floating action button to open file browser
   - Camera button to take photo and attach to message
   - Image picker to attach existing photos
   - Dark mode by default

2. **File Browser**
   - List of files/folders with icons
   - Tap folder to navigate, tap file to view
   - Simple create/delete actions
   - Back to chat

3. **File Viewer**
   - Rendered markdown
   - Edit button to open raw editor
   - Delete option
   - Share button

4. **Settings**
   - API key input (secure storage)
   - Export notes (zip)
   - Clear conversation
   - About/version

### First Launch (Guided Intro)

1. API key setup screen
2. Welcome message from Grimoire spirit
3. Claude asks: "Welcome, keeper. What knowledge shall we chronicle together?"

## Architecture

```
┌─────────────────────────────────────────────┐
│                 Grimoire App                 │
├─────────────────────────────────────────────┤
│  ┌─────────────┐    ┌────────────────────┐  │
│  │   Chat UI   │    │   File Browser     │  │
│  │  (streaming)│    │   (expo-router)    │  │
│  └──────┬──────┘    └─────────┬──────────┘  │
│         │                     │             │
│         ▼                     ▼             │
│  ┌─────────────────────────────────────────┐│
│  │          Tool Execution Layer           ││
│  │  list | read | write | edit | search   ││
│  └──────────────┬──────────────────────────┘│
│                 │                            │
│         ┌───────┴───────┐                   │
│         ▼               ▼                   │
│  ┌────────────┐  ┌─────────────┐            │
│  │ Claude API │  │ File System │            │
│  │  (Opus)    │  │ (expo-fs)   │            │
│  └────────────┘  └─────────────┘            │
│                                             │
│  ┌─────────────────────────────────────────┐│
│  │           Local Storage                 ││
│  │  - API key (vayu-storage)              ││
│  │  - Settings (AsyncStorage)             ││
│  └─────────────────────────────────────────┘│
└─────────────────────────────────────────────┘
```

## Tech Stack

- **Framework:** Expo / React Native
- **Navigation:** expo-router
- **File system:** expo-file-system
- **Camera:** expo-camera + expo-image-picker
- **Secure storage:** vayu-storage (already built!)
- **AI:** Claude API with tool use, streaming, vision
- **Markdown:** react-native-markdown-display
- **State:** Zustand (simple, performant)
- **Dark mode:** React Native appearance API

## File Structure

```
App Documents/
└── grimoire/
    └── notes/
        ├── inbox.md
        ├── daily/
        │   └── 2026-01-30.md
        ├── projects/
        │   └── coach-vayu.md
        └── images/
            └── 2026-01-30-receipt.jpg
```

## Milestones

### v0.1 - Proof of concept
- [ ] Expo project scaffold with expo-router
- [ ] Basic chat UI with streaming
- [ ] Claude API integration with tool use
- [ ] Single tool working (read_file)
- [ ] Hardcoded notes folder

### v0.2 - Core functionality
- [ ] All 7 tools working (list_dir, read_file, grep_files, view_image, write_file, edit_file, delete_file)
- [ ] File browser UI
- [ ] Markdown rendering
- [ ] Subfolder support
- [ ] Camera capture + image picker
- [ ] Images sent to Claude via vision API

### v0.3 - Daily driver
- [ ] Settings screen with API key (vayu-storage)
- [ ] Dark mode
- [ ] Whimsical loading messages
- [ ] Tool calls shown inline
- [ ] Auto-compact for long conversations
- [ ] Test on Pixel 10 Pro

### v0.4 - Polish
- [ ] Guided intro / first-run experience
- [ ] Export notes as zip
- [ ] Share extension (receive shared content)
- [ ] Error handling and recovery
- [ ] Subtle fantasy personality in system prompt

### v0.5 - Release ready
- [ ] Play Store listing
- [ ] Basic analytics
- [ ] Crash reporting
- [ ] Internal testing

## Future Features (post-MVP)

- iCloud / Google Drive sync
- Voice input
- PDF support in notes
- Widgets
- Multiple workspaces
- iOS App Store release

## References

- Codex CLI architecture: `~/code/codex` (cloned for reference)
- vayu-storage: `~/code/vayu-storage` (reusable secure storage)
