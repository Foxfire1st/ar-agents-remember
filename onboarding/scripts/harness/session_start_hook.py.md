# scripts/harness/session_start_hook.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/session_start_hook.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../overview.md`                        |

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

`emit(build_payload)` is the whole program: read the sibling `.md` directive file
(`DIRECTIVE_PATH` is the script's own path with a `.md` suffix, which is why the
generator also emits `hooks/agents-remember-session-start.md` as a composed file), wrap
it in the harness's payload envelope, and print the JSON on stdout.

Exactly two things vary, and both are protocol requirements rather than preference:

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The generator that assembles these fragments and emits the conditional `WORKSPACE_ROOT` constant and per-harness trailer. | [sync-harness.py](agents-remember/scripts/sync-harness.py) |
| The directive body every hook reads at run time. | [session-start-directive.md](agents-remember/scripts/harness/shared/session-start-directive.md) |
| The classification recording that the envelope and the workspace guard are protocol requirements. | [README.md](agents-remember/scripts/harness/README.md) |
| Tests that every declared hook fragment exists and each generated program parses with one entry point. | [test_sync_harness.py](agents-remember/mcp/tests/test_sync_harness.py) |

## Update History

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 created this fragment library, collapsing four
  independent session-start hook copies into one checked definition (requirement L2-R12).
  Verification metadata is pinned to the leaf's reformat commit until closeout stamps the
  code commit.
