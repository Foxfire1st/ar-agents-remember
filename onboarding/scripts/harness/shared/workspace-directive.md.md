# scripts/harness/shared/workspace-directive.md

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

The one definition of the session-start directive for harnesses that read their context
file from the **workspace root**. `scripts/sync-harness.py` composes it into **three**
files: `.hermes/HERMES.md`, `.agents/GEMINI.md`, and `.openclaw/workspace/AGENTS.md`.

## Code Commentary

### Logic

The workspace directive routes durable developer work through a separately launched,
sprint-bound architect rather than assigning one global architect identity to every free chat.
For ordinary role-shaped work, free chat resolves the sprint and first leaf, compiles the canonical
architect brief, and calls `dispatch_agent` once on the sprint document with role `architect`; it
hands over after that exact brief is durable and never calls a session primitive. An explicit
developer-declared task-seat takeover instead targets the named role on its canonical task
document. A present role marker must name a canonical role and carry hosted-session identity;
unknown roles and incomplete hosted identity stop instead of falling through. A first-message role
brief is authoritative only when no hosted identity was declared.

The body is the same three-condition routing as `shared/session-start-directive.md`: validate a
declared role plus hosted identity and fail closed if either is invalid; otherwise accept a fresh
first-message role brief only in an identity-free session; otherwise remain free chat, read the
coordinator `AGENTS.md`, answer research inline, and use the one-call architect launcher for
role-shaped work. The complete architect obligations arrive in the pinned canonical brief.

**The two differences from the sibling body are deliberate and are the entire reason two
bodies exist:**

1. The path is written absolute —
   `<PATH/TO/YOUR/PROJECTS_FOLDER>/ar-coordination/AGENTS.md` — because these files are
   mirrored out of the starter package to the workspace root, where a relative
   `ar-coordination/AGENTS.md` would not resolve the same way. The placeholder is
   substituted at render time.
2. It says to **treat those rules as workspace instructions**, which is how Hermes,
   Antigravity and OpenClaw consume a root context file.

### Conventions

- Per-harness framing is declared as `prologue` / `epilogue` in `sync-harness.py`:
  `# OpenClaw Workspace Instructions` and `# Antigravity Workspace Instructions`
  headings, and the `@<PATH/TO/YOUR/PROJECTS_FOLDER>/ar-coordination/AGENTS.md` include
  line for OpenClaw and Antigravity. `HERMES.md` takes the body with no framing at all.
- `write_context_file` (a per-harness fragment in `render_starter.py`, used by Hermes and
  Antigravity) is what mirrors the rendered file to the workspace root, with a merge
  guard.

### Invariants And Boundaries

- Which body a harness takes is a **per-harness fact**; the body itself is not. If a
  wording change applies to the directive rather than to the path convention, it must be
  made in both files.
- A wording change here lands in all three composed files at once. Editing a composed
  copy directly is caught by `sync-harness.py --check` in both hook tiers and by
  `mcp/tests/test_sync_harness.py`.

## Evidence

### Repo-Internal References

- The generator's `HARNESSES` declaration table is defined here. [1]
- The inside-the-workspace variant of the same directive uses the relative coordinator path. [2]
- `write_context_file` mirrors the rendered file to the workspace root for Hermes and Antigravity. [3]
- The classification recording why the two directive bodies differ. [4]
