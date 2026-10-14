# mcp/src/agents_remember/cli/knowledge_validate.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**`agents-remember knowledge-validate MEMORY_ROOT --code CODE_ROOT [--code-commit REV] [--base REV ...] [--json]`: the curator's standalone run of the knowledge validator (MIK-R22 rule 8).** The memory working tree's `knowledge/` and `onboarding/` files are the candidate. `--code` is the paired code checkout (its working tree, or `--code-commit` in it). Each `--base` is a memory commit to compare anchors with: K_B, or both parents of a merge.

## Code Commentary

### Logic

- `add_arguments` declares `memory_root`, required `--code`, `--code-commit`, repeatable `--base`
  and `--json`. `RawDescriptionHelpFormatter` preserves the ten-rule help table: five
  `merge_reports` rules refuse commit/landing but report sync merges (also standalone conversion
  in validator policy); four `migration_debt` rules distinguish new immediate refusals from
  base-carried reports while migration is incomplete; `R13.3-governs` refuses. The five decided
  refusing rules report only inside the writer, and each report names its reason and refusing route.
- `run` reads the candidate with `knowledge_tree_from_directory`, each base with `knowledge_tree_from_git` in the memory root, and the code tree as a `CodeDirectory` or, with `--code-commit`, `code_tree_from_git`. A read failure prints "cannot read the validator's inputs" and returns 2.
- If `validation_applies` is false, it prints that the tree is unconverted and out of scope and returns 0.
- Otherwise it runs `validate_tree` and prints every violation plus a verdict line (or the JSON document), returning 0 when the candidate passes and 1 when a violation refuses it.

### Conventions

- Registered in `cli/__main__.py` with the umbrella's declarative `add_arguments` + `set_defaults(func=run)` pair.
- With no `--base`, every anchor is checked for path existence and legacy debt is new, not carried.
  Curators should supply the actual comparison base(s), e.g. `--base HEAD` for route comparison
  (review R1 finding 9); a based pass does not imply baseless validation passes.

### Invariants And Boundaries

- Every registered rule runs; there is no option that skips one, and `conversion` mode is not exposed.
- It only reads.
- Exit status: 0 passes or out of scope, 1 refused, 2 unreadable input.
- Historical pre-MIK-R37 observation: the then-unconverted real memory worktree was out of scope.
  This read-only command's out-of-scope result is not a current legacy mutation/landing permission.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The adapter reuses the validator package; it adds only argument handling and printing.

- Printing the report or its JSON. [2]
- Inputs, the out-of-scope answer and the exit statuses. [3]
- Registration in the umbrella. [4]

### Cross-Repo References

No meaningful cross-repo references found: the command reads the memory and code checkouts it is given.

No cross-repo boundary is crossed by this file.

- Arguments, RawDescriptionHelpFormatter and the ten-rule reason/refusing-route table. [1]
- Current source assertions distinguish the fixture pass with `--base` (carried legacy report) from the baseless malformed-marker JSON refusal (both marker and legacy debt refuse); no command was run for this account. [5]
- Current source delta inspected statically: Add the preserved help-table policy and correct the stale blanket fixture-pass caption while retaining arguments, read-only/no-skip behavior and exit codes. [6]
