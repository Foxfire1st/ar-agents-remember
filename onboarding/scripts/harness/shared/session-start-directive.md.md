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

The directive addresses an ordinary developer-facing free chat: read ar-coordination/AGENTS.md and answer questions inline. For managed repository work, create or resolve the sprint document and write the developer request there, then call role_start for an Architect without naming a document in that call. Tell the developer the agent is in the dashboard and which sprint holds the request. Start another role this way only when the developer names its role and task.

A session whose first message is a role handover is not meant by the notice. There is no dispatch_agent, AR_SPAWN_ROLE or AR_HOSTED_SESSION_ID routing/admission instruction in this current source. Bound native agent recognition/suppression belongs to session_start_hook.has_binding, not an invented hosted environment capsule.

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
