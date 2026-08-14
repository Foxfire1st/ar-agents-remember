# scripts/harness/session_start_hook.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/session_start_hook.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator that assembles these fragments and emits the conditional `WORKSPACE_ROOT` constant and per-harness trailer. | `WORKSPACE_ROOT` | scripts/sync-harness.py:556-556 |
| The directive body every hook reads at run time. | "Otherwise you are the developer-facing **free chat**: read" | scripts/harness/shared/session-start-directive.md:7-7 |
| The classification recording that the envelope and the workspace guard are protocol requirements. | `started_inside_workspace`; "payload envelope" | scripts/harness/README.md:79-79; scripts/harness/README.md:81-81 |
| Tests that every declared hook fragment exists and each generated program parses with one entry point. | `test_every_declared_fragment_exists_in_its_library`; `test_generated_programs_parse_and_have_an_entry_point` | mcp/tests/test_sync_harness.py:57-65; mcp/tests/test_sync_harness.py:75-87 |

## Update History

- 2026-08-10T10:40+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-03T03:12:31+02:00 — W3-B04 curator: curated 3 table citations (3 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-31T06:30+02:00 — 260731-EFA-L2 created this fragment library, collapsing four
  independent session-start hook copies into one checked definition (requirement L2-R12).
  Verification metadata is pinned to the leaf's reformat commit until closeout stamps the
  code commit.

