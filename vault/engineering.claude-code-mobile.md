---
id: claude-code-mobile-design-v1
title: Claude Code Mobile - Design Doc
desc: ''
updated: 1738164600000
created: 1738164600000
---

> This note was generated with AI assistance.

# Claude Code Mobile - Design Doc

## Concept

A mobile app that brings the Claude Code experience to your phone. Chat with Claude, and it can read/write files in a notes folder on your device. You can see and edit everything the AI knows about you.

**Core value prop:** "Claude that can read/write your files, and you can see everything it knows."

**Differentiators:**
- Files on YOUR device - portable, private, auditable
- Transparency - see exactly what the AI knows (not a black box like ChatGPT memory)
- Conversational-first - talk to manage your notes, not manual editing
- AI as author - detailed notes because Claude writes them

## MVP Features

### Must have
1. **Chat interface** - conversation with Claude, streaming responses
2. **Notes folder** - designated folder in app documents for markdown files
3. **Claude tools:**
   - `list_files` - see what's in the notes folder
   - `read_file` - read a note's contents
   - `write_file` - create a new note
   - `edit_file` - modify an existing note
4. **File browser** - simple UI to see/read your notes
5. **Markdown rendering** - view notes with basic formatting

### Skip for MVP
- Sync (iCloud, Google Drive, Git)
- Glob/grep search
- Multiple folders/workspaces
- Fancy organization (tags, backlinks, etc.)
- Image support
- Voice input

## Tech Stack

- **Framework:** Expo / React Native (familiar from Coach Vayu)
- **File system:** `expo-file-system`
- **AI:** Claude API with tool use
- **Markdown:** `react-native-markdown-display` or similar
- **State:** React Context or Zustand (keep it simple)

## Architecture

```
┌─────────────────────────────────────────┐
│                Mobile App               │
├─────────────────────────────────────────┤
│  ┌─────────────┐    ┌────────────────┐  │
│  │   Chat UI   │    │  File Browser  │  │
│  └──────┬──────┘    └───────┬────────┘  │
│         │                   │           │
│         ▼                   ▼           │
│  ┌─────────────────────────────────────┐│
│  │         Tool Execution Layer        ││
│  │  (read, write, edit, list files)    ││
│  └──────────────┬──────────────────────┘│
│                 │                        │
│         ┌───────┴───────┐               │
│         ▼               ▼               │
│  ┌────────────┐  ┌─────────────┐        │
│  │ Claude API │  │ File System │        │
│  │ (tool use) │  │ (expo-fs)   │        │
│  └────────────┘  └─────────────┘        │
└─────────────────────────────────────────┘
```

## Claude Tool Definitions

```typescript
const tools = [
  {
    name: "list_files",
    description: "List all files in the notes folder",
    input_schema: {
      type: "object",
      properties: {
        path: {
          type: "string",
          description: "Optional subdirectory path"
        }
      }
    }
  },
  {
    name: "read_file",
    description: "Read the contents of a note",
    input_schema: {
      type: "object",
      properties: {
        filename: {
          type: "string",
          description: "Name of the file to read"
        }
      },
      required: ["filename"]
    }
  },
  {
    name: "write_file",
    description: "Create a new note or overwrite an existing one",
    input_schema: {
      type: "object",
      properties: {
        filename: {
          type: "string",
          description: "Name of the file to write"
        },
        content: {
          type: "string",
          description: "Content to write to the file"
        }
      },
      required: ["filename", "content"]
    }
  },
  {
    name: "edit_file",
    description: "Edit an existing note by replacing text",
    input_schema: {
      type: "object",
      properties: {
        filename: {
          type: "string",
          description: "Name of the file to edit"
        },
        old_text: {
          type: "string",
          description: "Text to find and replace"
        },
        new_text: {
          type: "string",
          description: "Text to replace with"
        }
      },
      required: ["filename", "old_text", "new_text"]
    }
  }
]
```

## System Prompt

```
You are a personal assistant with access to the user's notes folder. You can read, write, and edit markdown files to help them manage their personal knowledge base.

Available tools:
- list_files: See what notes exist
- read_file: Read a note's contents
- write_file: Create or overwrite a note
- edit_file: Modify part of an existing note

Guidelines:
- When the user asks about something, check if there's a relevant note first
- Keep notes well-organized with clear titles
- Use markdown formatting in notes
- When updating notes, preserve existing content unless asked to replace
- Be transparent about what files you're reading/writing
```

## UI Screens

### 1. Chat Screen (main)
- Message input at bottom
- Chat history with streaming responses
- Tool use shown inline (e.g., "Reading notes/daily.md...")
- Quick action to open file browser

### 2. File Browser
- List of files in notes folder
- Tap to view file contents
- Simple create/delete actions
- Back to chat

### 3. File Viewer
- Rendered markdown
- Edit button to open raw editor
- Delete option
- Back to browser

### 4. Settings
- API key input
- Clear chat history
- Export notes (future)

## Data Flow

1. User sends message
2. App sends to Claude API with tools + recent conversation
3. Claude responds, possibly with tool calls
4. App executes tools (file operations)
5. Tool results sent back to Claude
6. Claude responds with final message
7. UI updates with response

## File Structure

```
App Documents/
└── notes/
    ├── inbox.md          (default scratch note)
    ├── daily/
    │   └── 2026-01-29.md
    └── projects/
        └── coach-vayu.md
```

## Open Questions

1. **Naming** - what to call this app?
2. **Pricing model** - free with your own API key? subscription?
3. **Note organization** - flat vs folders vs Dendron-style hierarchy?
4. **Context management** - how much chat history / how many notes to include?
5. **Offline** - cache notes locally, queue messages?

## Future Features (post-MVP)

- iCloud / Google Drive sync
- Glob/grep search across notes
- Multiple workspaces
- Voice input
- Image/PDF support
- Share extension (save links/text to notes)
- Widgets
- Watch app
- Shortcuts/Siri integration

## Milestones

### v0.1 - Proof of concept
- [ ] Expo project scaffold
- [ ] Basic chat UI with Claude API
- [ ] Single tool working (read_file)
- [ ] Hardcoded notes folder

### v0.2 - Core tools
- [ ] All 4 tools working (list, read, write, edit)
- [ ] File browser UI
- [ ] Markdown rendering

### v0.3 - Usable daily driver
- [ ] Polish chat UI
- [ ] Settings screen with API key
- [ ] Basic error handling
- [ ] Test on actual device

### v0.4 - Beta ready
- [ ] Onboarding flow
- [ ] Export notes
- [ ] Crash reporting
- [ ] TestFlight / internal testing
