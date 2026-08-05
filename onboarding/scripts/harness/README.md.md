# scripts/harness/README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/README.md`                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../overview.md`                        |

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The classification document the generator depends on. Leaf 260731-EFA-L2's open question
was *which* differences among the self-hosted harness trees are genuine per-harness
requirements and which are drift — collapsing them blindly would break a harness — so the
classification had to precede the generator. This file records the answer and the
evidence.

## Code Commentary

### Logic

Three sections carry the durable content:

**Why generate instead of import.** A starter package is copied into a user's workspace
and run from there, so it cannot import a shared module out of this repository. Each
program must stay a single self-contained file, and sharing therefore happens at
generation time.

**Why the fragment libraries are real Python.** Both libraries type-check and lint as
ordinary modules, so the shared body is verified once as a whole instead of once per
copy. Every generated program is a subset of a checked module plus a constants block.

**What is shared and what is per-harness.** A table maps each shared source to the number
of copies it replaces:

| Source | Copies replaced |
| --- | --- |
| `render_starter.py` shared fragments | the body of 8 `render-starter.py` programs |
| `session_start_hook.py` shared fragments | the body of 4 hook scripts |
| `shared/render-starter.sh` | 8 byte-identical copies |
| `shared/render-starter.ps1` | 8 byte-identical copies |
| `shared/agents-remember-settings.json` | 8 byte-identical copies |
| `shared/session-start-directive.md` | 6 copies (4 hook directives, Copilot instructions, Cursor rule) |
| `shared/workspace-directive.md` | 3 copies (`HERMES.md`, `GEMINI.md`, OpenClaw `AGENTS.md`) |

The per-harness list is the ruled classification, each entry with the requirement that
makes it real: `render_<harness>` (which files get placeholder substitution and in what
order); `command_string` (Codex, Cursor, VS Code embed the hook as one command string
while Claude Code takes interpreter and script as separate fields);
`toml_basic_string_content` (Codex configuration is TOML, so an embedded Windows path
needs escaping); `write_context_file` (Hermes and Antigravity read their context file
from the workspace root); the three hook-configuration schemas
(`render_claude_settings` / `render_cursor_hooks` / `render_vscode_hooks`);
`hook_script_path` and `vscode_root` (the VS Code starter ships as `.github-vscode/` so
it does not collide with a repository's own `.github/`, but VS Code reads the hook from
`.github/` and MCP settings from `.vscode/` — it is the one starter that spans two
folders); `started_inside_workspace` (Codex registers session-start hooks globally, so
the hook fires for unrelated sessions and must scope itself); and the payload envelope
(Cursor reads `additional_context`, the other three read `hookSpecificOutput`).

### Invariants And Boundaries

- The two directive bodies differ for one deliberate reason, not cosmetics: files read
  from **inside** the workspace name `ar-coordination/AGENTS.md` relatively; the context
  files Hermes, Antigravity and OpenClaw mirror to the **workspace root** carry the
  rendered absolute path and say the rules are workspace instructions. Which body a
  harness takes is a per-harness fact; the body itself is not.
- Files a starter package owns alone — different serialisation formats (JSON, TOML,
  YAML), different schema keys (`mcpServers` vs `servers` vs `mcp.servers`), and a
  different folder name baked into every path — are explicitly **not** managed by the
  generator and are edited in place.
- The skill trees under each starter package are generated separately, by
  `scripts/sync-skills.py` from root `skills/`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator whose `HARNESSES` table encodes this classification. | `HARNESSES` | scripts/sync-harness.py:202-408 |
| The two fragment libraries this file inventories. | `render_settings`; `hook_specific_output` | scripts/harness/render_starter.py:108-115; scripts/harness/session_start_hook.py:28-34 |
| The verbatim and composed bodies. | "exec python3"; "Join-Path" | scripts/harness/shared/render-starter.ps1:4-4; scripts/harness/shared/render-starter.sh:5-5 |
| The suite check that makes the classification enforceable rather than descriptive. | `test_every_generated_harness_file_matches_its_source` | mcp/tests/test_sync_harness.py:40-51 |

## Update History

- 2026-08-03T03:10:23+02:00 — W3-B05 curator: resolved 3 Tier-2 table findings with exact anchors and current source paths; fixer generated all final ranges.
- 2026-07-31T06:30+02:00 — 260731-EFA-L2 created this classification alongside the
  generator (requirement L2-R12). It is the recorded answer to the leaf's open question
  about genuine per-harness requirements versus drift. Verification metadata is pinned to
  the leaf's reformat commit until closeout stamps the code commit.
