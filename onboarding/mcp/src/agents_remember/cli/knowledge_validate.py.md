# mcp/src/agents_remember/cli/knowledge_validate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_validate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The adapter reuses the validator package; it adds only argument handling and printing.

| Finding | Anchor | Source |
| --- | --- | --- |
| Arguments. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_validate.py:39-53 |
| Printing the report or its JSON. | `_print` | mcp/src/agents_remember/cli/knowledge_validate.py:56-66 |
| Inputs, the out-of-scope answer and the exit statuses. | `run` | mcp/src/agents_remember/cli/knowledge_validate.py:69-93 |
| Registration in the umbrella. | "knowledge-validate" | mcp/src/agents_remember/cli/__main__.py:70-75 |
| The command passes the fixture tree and refuses a hand-added marker. | `test_the_standalone_command_validates_a_converted_fixture_tree` | mcp/tests/test_knowledge_validator_routes.py:215-241 |

## Cross-Repo References

No meaningful cross-repo references found: the command reads the memory and code checkouts it is given.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
