# scripts/harness/render_starter.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/render_starter.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../overview.md`                        |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The single definition of every `render-starter.py` program shipped in the eight
self-hosted harness starter packages. `scripts/sync-harness.py` slices named top-level
definitions out of this module and assembles one standalone program per harness.

**Nothing imports this module at run time.** It exists so that the shared body has
exactly one definition, and so that Ruff and Pyright check that body once, as a whole,
instead of eight times.

## Code Commentary

### Logic

The module is an ordinary, lintable, type-checked Python module whose top-level
definitions are the fragments. Each generated program is a subset of them plus a
per-harness constants block.

Shared by every harness (`SHARED_STARTER_FRAGMENTS` in the generator):
`Renderer`, `infer_workspace_root`, `repository_ids`, `replace_text`, `render_settings`,
`validate`, `main`.

Per-harness, each present because the harness genuinely requires it:

| Fragment | Harnesses | Requirement |
| --- | --- | --- |
| `render_<harness>` | one each | the rendering steps: which files get placeholder substitution, in what order |
| `command_string` | Codex, Cursor, VS Code | those three embed the hook as one command string; Claude Code takes interpreter and script as separate fields |
| `toml_basic_string_content` | Codex | Codex configuration is TOML, so an embedded Windows path must be escaped for a basic string |
| `write_context_file` | Hermes, Antigravity | both read their context file from the workspace root, so the rendered template is mirrored out with a merge guard |
| `render_claude_settings` / `render_cursor_hooks` / `render_vscode_hooks` | one each | three different hook-configuration schemas: nested `hooks.SessionStart[].hooks[]` with `command` + `args`, a flat `hooks.sessionStart[].command` string, and a `command` plus per-platform `windows`/`osx`/`linux` overrides |
| `hook_script_path`, `vscode_root` | VS Code | the starter ships as `.github-vscode/` to avoid colliding with a repository's own `.github/`, but VS Code reads the hook from `.github/` and MCP settings from `.vscode/` |

The module-level constants (`HARNESS_LABEL`, the five placeholders, `PLACEHOLDERS`,
`TARGET_FILES`, `WORKSPACE_TARGET_FILES`, `VSCODE_TARGET_FILES`) are **representative
placeholders only**. The generator never emits them; it emits a per-harness constants
block built from `sync-harness.py`'s `HARNESSES` table, then the requested fragments
verbatim. Keeping the data out of the fragments is what lets `validate` and `main` be
byte-identical in every generated file.

### Conventions

- A fragment must appear in `STARTER_FRAGMENT_ORDER` in `sync-harness.py`. A name that is
  defined here but not ordered there is an error, not a silent drop.
- Import lines are derived by the generator from the names each assembled body uses, so a
  fragment that reaches for a new module cannot leave its import behind. The imports at
  the top of *this* file exist for checking this module, not for any generated one.
- Adding a genuinely-shared behaviour means adding a fragment here and listing it in
  `SHARED_STARTER_FRAGMENTS`; a test fails any harness that drops one.

### Invariants And Boundaries

- This module is a **library of source text**, not a runtime dependency. Generated
  starter programs must stay single self-contained files because they are copied into a
  user's workspace and run from there.
- Editing a generated `.claude/render-starter.py` (or any of the other seven) is wrong
  and will be caught: `sync-harness.py --check` runs in both hook tiers and in
  `mcp/tests/test_sync_harness.py`.
- Every generated program is expected to survive `ruff format --check` unchanged, which
  constrains how the generator emits constants around these fragments.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator that slices, orders, and assembles these fragments. | `generated_files`, `render_starter_program` | scripts/sync-harness.py:522-548; scripts/sync-harness.py:576-621 |
| The classification of which fragments are genuinely per-harness and why. | `## What is shared and what is per-harness` | scripts/harness/README.md:38-94 |
| The hook fragment library with the same contract. | `hook_specific_output`, `emit` | scripts/harness/session_start_hook.py:28-34; scripts/harness/session_start_hook.py:57-59 |
| Tests that every declared fragment exists, every harness carries the shared body, and each generated program parses with one entry point. | `test_every_declared_fragment_exists_in_its_library`, `test_every_starter_carries_the_shared_body`, `test_generated_programs_parse_and_have_an_entry_point` | mcp/tests/test_sync_harness.py:57-65; mcp/tests/test_sync_harness.py:67-73; mcp/tests/test_sync_harness.py:75-87 |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 4 repository-internal generator, README, hook-library, and sync-test references; final scoped result 0 (checker-clean).

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 created this fragment library, collapsing eight
  independent `render-starter.py` copies (96–143 lines each, roughly 940 lines) into one
  checked definition (requirement L2-R12). Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
