# scripts/harness/shared/session-start-directive.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/shared/session-start-directive.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-31T04:59+02:00                     |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

The one definition of the session-start directive read from **inside** a workspace. It is
the text every session-start hook prints and the text Cursor's always-applied rule and
Copilot's instructions carry. `scripts/sync-harness.py` composes it into **six** files:
the four `hooks/agents-remember-session-start.md` directives, `.cursor/rules/
agents-remember.mdc`, and `.github-vscode/copilot-instructions.md`.

## Code Commentary

### Logic

The shared session-start directive treats an ordinary developer session as free chat that answers
research inline. For ordinary role-shaped work it creates or resolves the sprint and first leaf, compiles
the canonical architect brief, and calls `dispatch_agent` exactly once on the sprint document with
role `architect`. The launcher hands over only after the exact brief is durable and never calls an
internal session primitive. An explicit developer-declared task-seat takeover instead targets the
named role on its canonical task document. A present `AR_SPAWN_ROLE` is not merely a routing hint:
it must resolve to a canonical role file and arrive with `AR_HOSTED_SESSION_ID`. An unknown role or
incomplete hosted identity fails closed instead of falling through. A fresh role brief may start a
role lifecycle only when no hosted identity was declared.

Caller kind remains process-derived: a plane-hosted seat uses structural authority, while absence
of hosted identity selects the ambient launcher. A plane refusal never falls back to ambient.

The body states the three-condition session routing that `l-01-agent-lifecycles` owns:

1. If `AR_SPAWN_ROLE` is set, validate the canonical role and hosted identity first; invalid or
   incomplete identity stops. With valid hosted identity—or with a first-message role brief and no
   declared hosted identity—the session ignores the remaining notice and treats the brief as start.
2. Otherwise the session is developer-facing free chat: read `ar-coordination/AGENTS.md`, answer
   research inline, and use the one-call canonical architect launcher for role-shaped work.
3. The resulting sprint-bound architect receives its complete obligations in the pinned canonical
   brief rather than relying on this launcher directive as a second role brief.

### Conventions

- Per-harness framing is **not** in this file. It is declared as `prologue` / `epilogue`
  in `sync-harness.py`'s `Composed` entries: Cursor's `---`/`alwaysApply: true` front
  matter, the `@<PATH/TO/YOUR/PROJECTS_FOLDER>/ar-coordination/AGENTS.md` include line,
  and Copilot's note about where the path resolves.
- The body is stored without a trailing newline concern; `compose()` strips trailing
  newlines from the body before joining prologue, body and epilogue.

### Invariants And Boundaries

- **This body names `ar-coordination/AGENTS.md` relatively**, because every file composed
  from it is read from inside the workspace. The sibling `workspace-directive.md` is the
  same directive for context files mirrored to the workspace root, which carry the
  rendered absolute path instead. Which body a harness takes is a per-harness fact; the
  body itself is not, and that is the whole reason there are two files rather than nine.
- A wording change here lands in all six composed files at once. Editing a composed copy
  directly is caught by `sync-harness.py --check` in both hook tiers and by
  `mcp/tests/test_sync_harness.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator that composes this body into six files with per-harness framing. | `generated_files`, `compose` | scripts/sync-harness.py:576-621; scripts/sync-harness.py:631-633 |
| The workspace-root variant of the same directive. | "as workspace instructions" | scripts/harness/shared/workspace-directive.md:11-12 |
| The hook fragments that read this file at run time. | `DIRECTIVE_PATH`, `emit` | scripts/harness/session_start_hook.py:23-23; scripts/harness/session_start_hook.py:57-59 |
| The lifecycle this directive routes a session into. | `# l-01-agent-lifecycles — The Agent Lifecycles` | skills/l-01-agent-lifecycles/SKILL.md:6-416 |

## Update History

- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: reconciled the starter
  source's fail-closed role/hosted-identity admission and removed the obsolete claim that any set
  role value could fall through to a pasted brief. Verification remains closeout-owned.

- 2026-08-30T13:59+02:00 — 260821-ARSPAWN-L3 made the process-derived caller-kind boundary and
  no-fallback rule explicit in the shared launcher directive after the targeted Dagger forcing
  check exposed the omission. Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 recorded the one-call canonical architect launcher,
  separated ordinary bootstrap from explicit named-role takeover, and retained the durable-brief
  handoff plus direct-session prohibition. Verification remains closeout-owned.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded the free-chat-to-sprint-architect launcher
  boundary shared by generated harness starters. Verification metadata remains pinned until
  closeout stamps the code commit.

- 2026-08-03T03:06:00+02:00 — Curator W3-B02 repaired 4 Repo-Internal citation rows, resolving 8 manifest findings with exact generator, directive, hook, and lifecycle anchors; verification metadata was preserved.
- 2026-07-31T06:30+02:00 — 260731-EFA-L2 promoted this to the single source for six
  copies of the session-start directive (requirement L2-R12). Verification metadata is
  pinned to the leaf's reformat commit until closeout stamps the code commit.
