# scripts/harness/shared/session-start-directive.md

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

## Evidence

### Repo-Internal References

- The generator that composes this body into six files with per-harness framing. [1]
- The workspace-root variant of the same directive. [2]
- The hook fragments that read this file at run time. [3]
- The lifecycle this directive routes a session into. [4]
