# scripts/harness/session_start_hook.py

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The single definition of the four per-harness session-start hook scripts
(`hooks/agents-remember-session-start.py` in `.claude/`, `.codex/`, `.cursor/` and
`.github-vscode/`). `scripts/sync-harness.py` assembles one standalone program per
harness from these fragments.

As with `render_starter.py`, the hook scripts ship inside a user's workspace and must
stay self-contained, so the sharing happens at generation time and nothing imports this
module at run time.

## Code Commentary

### Logic

`emit(build_payload)` first calls `has_binding` and returns without output for a bound native role agent; otherwise it reads the sibling `.md` directive file
(`DIRECTIVE_PATH` is the script's own path with a `.md` suffix, which is why the
generator also emits `hooks/agents-remember-session-start.md` as a composed file), wrap
it in the harness's payload envelope, and print the JSON on stdout.

`has_binding` reads only labels in the host's authoritative agent record selected by validated PASEO_AGENT_ID under PASEO_HOME and HOST_RECORD_FOLDER. A truthy ar.role label suppresses the free-chat directive on start/reload/resume. Missing/invalid identity, missing/unreadable record or missing label is indeterminate: the hook speaks and never fails session start or prints record contents. This card describes that source algorithm; no actual host/private settings are read by curation.

The following envelope/workspace variations are protocol requirements, not preferences:

| Variation | Fragments | Harnesses |
| --- | --- | --- |
| the payload envelope the harness reads back from stdout | `hook_specific_output` → `{"hookSpecificOutput": {"hookEventName": ..., "additionalContext": ...}}` | Claude Code, Codex, VS Code |
| | `additional_context` → `{"additional_context": ...}` | Cursor |
| whether the hook scopes itself to the workspace | `started_inside_workspace` | Codex only |

`started_inside_workspace()` exists because **Codex registers session-start hooks
globally**, so the hook also fires for sessions that have nothing to do with this
workspace; emitting the directive there would inject unrelated instructions. It resolves
`$PWD` (falling back to the process cwd) and checks it is under `WORKSPACE_ROOT`. Every
other harness scopes its hooks to the folder the configuration lives in and needs no
guard, so their generated programs call `emit(...)` unconditionally.

The `trailer` in each `HookSpec` is what encodes that difference in the generated
`__main__` block — Codex's is `if started_inside_workspace(): emit(hook_specific_output)`,
the others are a bare `emit(...)`.

`WORKSPACE_ROOT` is only emitted into a generated file when `started_inside_workspace` is
among its fragments; the generator inserts the constant conditionally.

### Invariants And Boundaries

- The subject line in each generated docstring (`SessionStart` for Claude Code, Codex and
  VS Code; `sessionStart` for Cursor) is the harness's own event name and comes from
  `HookSpec.subject`.
- The directive body is **not** defined here. It lives in
  `scripts/harness/shared/session-start-directive.md` and is emitted beside each hook as
  a composed file, so a wording change lands once.
- Generated hook scripts are mode `0o644`. They are invoked through a hook command, never
  as `./file`; the executable bit had already drifted onto two of the four copies before
  the generator normalised it.
- Editing a generated hook script directly is caught by `sync-harness.py --check` in both
  hook tiers and by `mcp/tests/test_sync_harness.py`.

## Evidence

### Repo-Internal References

- The generator that assembles these fragments and emits the conditional `WORKSPACE_ROOT` constant and per-harness trailer. [1]
- The directive body every hook reads at run time. [2]
- The classification recording that the envelope and the workspace guard are protocol requirements. [3]
