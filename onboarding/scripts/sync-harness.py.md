# scripts/sync-harness.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/sync-harness.py`                  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-07T00:31+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-harness.py` generates the **nine self-hosted harness configuration trees**
from one source in `scripts/harness/`, and can verify them without writing. It is the
third member of the repository's generator family beside `sync-skills.py` and
`sync-runtime.py`, and it is wired into the same gates.

The repository dogfoods its own harness starter packages — `.claude/`, `.codex/`,
`.cursor/`, `.github-vscode/` (plus the sibling `.vscode/`), `.hermes/`, `.openclaw/`,
`.pi/` and `.agents/` are real packages a user can copy into a workspace. That is
legitimate. What was not legitimate is that it meant **eight independent copies of the
same programs**: `render-starter.py` existed eight times at 96 to 143 lines each (roughly
940 lines), and the session-start hook four times, so a fix landed in one copy and not
the others.

## Code Commentary

### Logic

```text
python3 scripts/sync-harness.py               # write every generated file
python3 scripts/sync-harness.py --check       # verify only; writes nothing, non-zero on drift
python3 scripts/sync-harness.py --list-targets
```

`HARNESSES` is the declaration table: one `Harness` per tree, each carrying a
`StarterSpec`, an optional `HookSpec`, verbatim `shared` copies, `composed` files, and
`extra_shared` copies whose destination is repo-relative rather than under the harness
directory (this is how `.github-vscode/` reaches its sibling `.vscode/`). 45 files across
the nine trees are generated from seven sources.

Fan-out happens three ways:

1. **Verbatim** — `shared/render-starter.sh`, `shared/render-starter.ps1`,
   `shared/agents-remember-settings.json` are byte-identical copies.
2. **Composed** — one shared body plus per-harness framing (`prologue` / `epilogue`).
   The nine files carrying the session-start directive are not byte-identical, but every
   difference is framing a harness requires: Cursor's `---`/`alwaysApply` front matter,
   the `# … Workspace Instructions` headings, the `@`-include lines, Copilot's note about
   where the path resolves.
3. **Assembled from fragment libraries** — named top-level definitions are sliced out of
   `scripts/harness/render_starter.py` and `scripts/harness/session_start_hook.py` with
   `ast` and re-emitted as standalone programs.

Assembly is deliberately derivation-heavy so nothing can silently drift:

- `fragment_sources()` reads every top-level definition by name as verbatim source text.
- `ordered_fragments()` refuses a fragment name that is undefined in the library **or**
  missing from the declared emission order — either would silently drop code out of a
  generated program.
- `required_imports()` derives each program's import block from the names the assembled
  body actually uses, so adding a fragment that reaches for a new module cannot leave the
  import behind.
- `tuple_literal()` emits tuples the way Ruff's formatter would leave them (a
  single-element tuple collapsed, two or more exploded with a trailing comma), because
  generated files must survive `ruff format --check` unchanged.

`describe_drift()` reports content differences as a unified diff **and** mode
differences. `GENERATED_MODE` is `0o644`: none of these files is executed as `./file`
(they are invoked through `python`, `sh`, or a hook command), so the executable bit is
noise — and it had already drifted onto two of the four hook scripts and not the other
two.

### Conventions

- Edit `scripts/harness/`, never a generated file. Every generated file carries a
  `# Generated file -- do not edit.` header naming its source and the regenerate command.
- Only the files listed in `HARNESSES` are managed. Everything else in a starter package
  — `config.toml`, `settings.json`, `mcp.json`, `mcp_config.json`, `hooks.json`,
  `openclaw.merge.json`, `config.yaml`, `extensions/agents-remember-start.ts` — is a
  genuine single-copy per-harness file and is left alone.
- `scripts/harness/README.md` records the classification of which differences are real
  per-harness requirements and which were drift, with the evidence.

### Invariants And Boundaries

- **Generation, not import.** A starter package is copied into a user's workspace and run
  from there, so each program must stay a single self-contained file. Sharing at run time
  is unavailable; sharing at generation time is what this script provides.
- **`--check` is wired into gates, not left to memory.** Both hook tiers run
  `python3 scripts/sync-harness.py --check` via `.githooks/_gate.sh`, with no claim that the retired harness matrix still runs inside the test suite.
- No two harnesses may claim the same destination path (generator design requirement; the old census test is retired).
- Every harness must carry the full `SHARED_STARTER_FRAGMENTS` set; a target that
  silently dropped one would regrow a private copy (generator design requirement; the old census test is retired).
- Generated `.py` files must parse and carry exactly one `__main__` guard.
- The skill trees under each starter package are **not** this script's business; they are
  generated by `scripts/sync-skills.py` from root `skills/`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fragment library for the eight `render-starter.py` programs. | `render_settings` | scripts/harness/render_starter.py:108-115 |
| Fragment library for the four session-start hook scripts. | `hook_specific_output` | scripts/harness/session_start_hook.py:28-34 |
| The classification of genuine per-harness requirements versus drift, and the shared-source inventory. | `## What is shared and what is per-harness` | scripts/harness/README.md:38-94 |
| Both hook tiers run `--check` beside the skill and runtime generated-copy checks. | "run_fast_checks() {"; "run_full_checks() {" | .githooks/_gate.sh:190-190; .githooks/_gate.sh:242-242 |
| The sibling generators this one is modelled on. | `SkillTarget`; `RuntimeTarget` | scripts/sync-runtime.py:26-30; scripts/sync-skills.py:26-29 |
| Repo instructions route harness edits through `scripts/harness/` and forbid editing generated starter files. | `## Source Layout`; `## Boundaries`; `## Repository Layout` | AGENTS.md:99-145; README.md:192-275 |

## Update History

- 2026-09-07T00:31+02:00 — Retired obsolete deleted-suite proof citations; the documented implementation contracts remain, without claiming those removed tests still protect them. Verification pins unchanged.

- 2026-08-28T15:52:15+02:00 — Rebased both hook-tier citations after the MCP-local interpreter
  selection repair shifted `_gate.sh`; generator behavior and enforcement remain unchanged.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 7 citation claims; scoped recheck clean (0 findings).

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 created the harness generator (requirement
  L2-R12, master decision OQ7). Recorded the three fan-out modes, the derived-imports and
  declared-order refusals, the `0o644` mode contract, and the fact that `--check` is
  enforced by both hook tiers and by the test suite rather than left to memory.
  Verification metadata is pinned to the leaf's reformat commit until closeout stamps the
  code commit.
