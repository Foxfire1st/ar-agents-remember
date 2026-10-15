# scripts/sync-skills.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-skills.py` is the repository helper that keeps the root
canonical `skills/` tree synchronized with every generated skill copy shipped in
the MCP package data and harness starter packages.

## Code Commentary

### Logic

The script resolves the repository root from its own path, treats root
`skills/` as canonical, and derives sync targets plus ignore names/suffixes from the single skills projection in `generated-copies.json` through the dependency-free parser owner. `skill_targets(root)` joins those declared target paths to its selected root; the parser itself belongs to this checkout. The current declaration covers:

- MCP package data under `mcp/src/agents_remember/package_data/runtime/skills`
- Claude Code, Codex, Cursor, VS Code/Copilot, Hermes, OpenClaw, Pi, and
  Antigravity starter package skill folders

It computes SHA-256 digests for every non-ignored file under the canonical tree
and each target, then reports missing, extra, and changed files. In normal mode
it copies the complete canonical tree to a sibling staging directory before renaming the live target aside and renaming staging into place,
then runs check mode. Before the first target mutation normal sync computes `projected_profile_bytes`: it validates the input certification profile through its canonical owner and derives only the generated-skills row/scopes and new digest. After the target loop it writes that prepared profile. `--check` compares both copy bytes and the profile projection and exits non-zero on drift. This is prevalidation, not an atomic transaction or rollback across all targets/profile. With `--list-targets`, it
prints the canonical source and all target paths.

### Conventions

`replace_tree` removes stale staging/retired leftovers, completes the new copy, then renames the old target aside and the staged tree into place before removing the retired tree. A copy failure before the first rename leaves the live target intact. The two renames are separate operations; this description does not claim an atomic directory exchange.

Ignore names/suffixes come from the canonical declaration, currently covering local/generated filesystem noise. Keep target declarations explicit so new harness packages consciously opt in; do not maintain a second target or ignore tuple here.

### Invariants And Boundaries

- Root `skills/` is the only canonical source.
- The script refuses to sync a target path that resolves to the canonical
  `skills/` directory.
- Sync mode replaces target skill directories wholesale; do not point a target
  at user-owned or non-generated content.
- The helper manages declared skill copies and their generated-skills certification-profile projection. It does not sync hooks, MCP settings, other instructions/docs or provider/runtime assets. This card is source inspection only: no sync/check invocation or generated/private mirror read/write was performed.

### Todos

No open file-local todos.

## Evidence

- Targets/ignore policy come from the declaration and profile bytes are validated before target replacement, then published and checked beside copy bytes. [5]


### Docs References

No external documentation is needed for this repository-local helper.

No relevant external documentation found.

### Repo-Internal References

- The script defines `skills/` as canonical and enumerates all MCP package-data and harness starter skill-copy targets. [1]
- `--check` compares canonical and target file digests, reports missing/extra/changed paths, and exits non-zero when a target is out of sync. [2]
- Normal sync mode refuses self-sync, replaces each target skill folder, copies canonical skills into place, and then reruns the check. [3]
- The root AGENTS instructions tell contributors to edit root `skills/` first and run `python3 scripts/sync-skills.py` rather than editing generated skill copies directly. [4]

### Cross-Repo References

No sibling repository evidence is needed for this helper.

No meaningful cross-repo references found.
