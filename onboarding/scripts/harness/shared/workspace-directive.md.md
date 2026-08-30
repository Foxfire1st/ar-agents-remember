# scripts/harness/shared/workspace-directive.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/shared/workspace-directive.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-30T12:34+02:00                     |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e` |
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|
| governingOverview      | `../../../overview.md`                     |

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
document. Spawned role briefs remain authoritative.

The body is the same three-condition session routing as
`shared/session-start-directive.md` — ignore the notice when `AR_SPAWN_ROLE` is set or
the first message is a role brief; otherwise remain free chat, read the coordinator `AGENTS.md`,
answer research inline, and use the one-call architect launcher for role-shaped work. The complete
architect obligations arrive in the pinned canonical brief.

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator's `HARNESSES` declaration table is defined here. | `HARNESSES` | scripts/sync-harness.py:202-408 |
| The inside-the-workspace variant of the same directive uses the relative coordinator path. | "ar-coordination/AGENTS.md" | scripts/harness/shared/session-start-directive.md:8-8 |
| `write_context_file` mirrors the rendered file to the workspace root for Hermes and Antigravity. | `write_context_file` | scripts/harness/render_starter.py:86-105 |
| The classification recording why the two directive bodies differ. | `## What is shared and what is per-harness` | scripts/harness/README.md:38-94 |

## Update History

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 recorded the one-call canonical architect launcher,
  separated ordinary bootstrap from explicit named-role takeover, and retained exact brief
  durability plus the no-session-primitive boundary. Verification remains closeout-owned.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: refreshed the generated-workspace guidance for the
  sprint-qualified architect launcher. Verification metadata remains pinned until closeout stamps
  the code commit.

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: source-first semantic citation curation; repaired this card's scoped citation findings with frozen-source evidence and corrected stale or pooled claims where needed.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 promoted this to the single source for the three
  workspace-root context files (requirement L2-R12). Verification metadata is pinned to
  the leaf's reformat commit until closeout stamps the code commit.
