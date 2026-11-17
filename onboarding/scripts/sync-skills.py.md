# scripts/sync-skills.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-skills.py` is the declared skill-copy owner that the instruction-renewal planner loads to project canonical `skills/` into the sole generated skill copy shipped in MCP package data and served to harnesses as resources. The public renewal command coordinates that copy with regenerated instruction facts. [7]

## Code Commentary

### Logic

The script resolves the repository root from its own path, treats root
`skills/` as canonical, and derives sync targets plus ignore names/suffixes from the single skills projection in `generated-copies.json` through the dependency-free parser owner. `skill_targets(root)` joins those declared target paths to its selected root; the parser itself belongs to this checkout. The current declaration covers:

- MCP package data under `mcp/src/agents_remember/package_data/runtime/skills`

It computes SHA-256 digests for every non-ignored file under the canonical tree
and each target, then reports missing, extra, and changed files. In normal mode
it copies the complete canonical tree to a sibling staging directory before renaming the live target aside and renaming staging into place,
then runs check mode. Before the first target mutation normal sync computes `projected_profile_bytes`: it validates the input certification profile through its canonical owner and derives only the generated-skills row/scopes and new digest. After the target loop it writes that prepared profile. `--check` compares both copy bytes and the profile projection and exits non-zero on drift. This is prevalidation, not an atomic transaction or rollback across all targets/profile. With `--list-targets`, it
prints the canonical source and all target paths. When `--check` finds copy or profile drift, its remedy is `run: mcp/.venv/bin/python scripts/renew-instructions.py`. [2]

The renewal planner loads this module through `_skill_owner` and calls its declaration, file-digest, target and certification-profile helpers in `_copy_plan`. That plan copies renewed canonical skill bytes, removes extra generated files and includes the generated-skills profile projection; this script remains the owner of those copy rules. [7]

### Conventions

`replace_tree` removes stale staging/retired leftovers, completes the new copy, then renames the old target aside and the staged tree into place before removing the retired tree. A copy failure before the first rename leaves the live target intact. The two renames are separate operations; this description does not claim an atomic directory exchange.

Ignore names/suffixes come from the canonical declaration, currently covering local/generated filesystem noise. The declared destination is the packaged serving tree; do not maintain a second target or ignore tuple here.

### Invariants And Boundaries

- Root `skills/` is the only canonical source.
- The script refuses to sync a target path that resolves to the canonical
  `skills/` directory.
- Sync mode replaces target skill directories wholesale; do not point a target
  at user-owned or non-generated content.
- The helper manages declared skill copies and their generated-skills certification-profile projection. It does not sync hooks, MCP settings, other instructions/docs or provider/runtime assets. This card is source inspection only: no sync/check invocation or generated/private mirror read/write was performed.

### Todos

The source file declares no TODO or FIXME marker.

## Evidence




### Docs References

No external documentation is needed for this repository-local helper.

`system/sources.md` configures no external domain documentation for this repository.

### Repo-Internal References

- The script defines `skills/` as canonical and derives the sole MCP package-data serving target. [1]

### Cross-Repo References

This card uses repository-owned code and test references and invokes no sibling-repository contract.

### Repo-Internal References (renewed)

- `--check` compares canonical and target file digests and the generated-skills profile projection, reports drift, and exits non-zero with `run: mcp/.venv/bin/python scripts/renew-instructions.py` as the remedy. [2]
- Normal sync mode refuses self-sync, replaces each target skill folder, copies canonical skills into place, and then reruns the check. Anchor: `sync_targets` `sync_target` `replace_tree` [3]
- The script derives the single packaged target from generated-copies.json and checks bytes plus the generated-skills certification projection. Anchor: `skill_targets`, `check_targets` [6]
- The instruction-renewal planner loads sync-skills.py as the declared copy owner and uses its projection, digest, target and profile helpers to plan the generated skill copy beside renewed instruction facts. [7]

## Current source evidence

- Root AGENTS instructions require editing canonical skills/ and running mcp/.venv/bin/python scripts/renew-instructions.py, which renews facts and propagates the generated package copy. [4]

- Targets/ignore policy come from the declaration and profile bytes are validated before target replacement, then published and checked beside copy bytes. [5]
