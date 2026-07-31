# scripts/harness/shared/workspace-directive.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/shared/workspace-directive.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

The one definition of the session-start directive for harnesses that read their context
file from the **workspace root**. `scripts/sync-harness.py` composes it into **three**
files: `.hermes/HERMES.md`, `.agents/GEMINI.md`, and `.openclaw/workspace/AGENTS.md`.

## Code Commentary

### Logic

The body is the same three-condition session routing as
`shared/session-start-directive.md` — ignore the notice when `AR_SPAWN_ROLE` is set or
the first message is a role brief; otherwise be the architect, read the coordinator
`AGENTS.md`, run `skills/l-01-agent-lifecycles/roles/architect.md`, and honour the four
named obligations (trust checkpoint, paired `read_ar_files`, retrieval-strategy tally,
notify-and-stop).

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

| Finding | Source Path |
| --- | --- |
| The generator that composes this body into three files with per-harness framing. | [sync-harness.py](agents-remember/scripts/sync-harness.py) |
| The inside-the-workspace variant of the same directive. | [session-start-directive.md](agents-remember/scripts/harness/shared/session-start-directive.md) |
| `write_context_file` mirrors the rendered file to the workspace root for Hermes and Antigravity. | [render_starter.py](agents-remember/scripts/harness/render_starter.py) |
| The classification recording why the two bodies differ. | [README.md](agents-remember/scripts/harness/README.md) |

## Update History

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 promoted this to the single source for the three
  workspace-root context files (requirement L2-R12). Verification metadata is pinned to
  the leaf's reformat commit until closeout stamps the code commit.
