# mcp/src/agents_remember/cli/knowledge_validate.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**`agents-remember knowledge-validate MEMORY_ROOT --code CODE_ROOT [--code-commit REV] [--base REV ...] [--json]`: the curator's standalone run of the knowledge validator (MIK-R22 rule 8).** The memory working tree's `knowledge/` and `onboarding/` files are the candidate. `--code` is the paired code checkout (its working tree, or `--code-commit` in it). Each `--base` is a memory commit to compare anchors with: K_B, or both parents of a merge.

## Code Commentary

### Logic

- `add_arguments` declares `memory_root`, the required `--code`, `--code-commit`, the repeatable `--base` and `--json`.
- `run` reads the candidate with `knowledge_tree_from_directory`, each base with `knowledge_tree_from_git` in the memory root, and the code tree as a `CodeDirectory` or, with `--code-commit`, `code_tree_from_git`. A read failure prints "cannot read the validator's inputs" and returns 2.
- If `validation_applies` is false, it prints that the tree is unconverted and out of scope and returns 0.
- Otherwise it runs `validate_tree` and prints every violation plus a verdict line (or the JSON document), returning 0 when the candidate passes and 1 when a violation refuses it.

### Conventions

- Registered in `cli/__main__.py` with the umbrella's declarative `add_arguments` + `set_defaults(func=run)` pair.
- With no `--base`, every anchor is checked for path existence; curators should pass `--base HEAD` to match route behaviour (review R1 finding 9).

### Invariants And Boundaries

- Every registered rule runs; there is no option that skips one, and `conversion` mode is not exposed.
- It only reads.
- Exit status: 0 passes or out of scope, 1 refused, 2 unreadable input.
- Before MIK-R37 the real memory worktree is unconverted, so the command reports it as out of scope.

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

- Arguments. [1]
- Printing the report or its JSON. [2]
- Inputs, the out-of-scope answer and the exit statuses. [3]
- Registration in the umbrella. [4]
- The command passes the fixture tree and refuses a hand-added marker (re-read after MIK-R09 moved the case below the new sync-merge cases; unchanged). [5]

### Cross-Repo References

No meaningful cross-repo references found: the command reads the memory and code checkouts it is given.

No cross-repo boundary is crossed by this file.
