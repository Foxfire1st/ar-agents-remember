# mcp/src/agents_remember/memory/conversion/base.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/conversion/base.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The converted base of a comparison (MIK-R24 rule 7).** When a comparison's before side is unconverted
and its after side is converted, the before side is replaced by its conversion, at the after side's pinned
conversion-format version. So the mechanical conversion itself never counts as a change.

## Code Commentary

### Logic

- `pinned_version(tree)` reads the `conversion` value of a converted tree's `knowledge/layout.json`.
- `converted_base(memory_repository, treeish, *, code_repository, code_commit, version)` reads the memory
  tree from Git (`inputs.memory_from_git`) into a temporary scratch, converts it with `convert_memory`, and
  returns it as a `KnowledgeTree`, the way the validator reads trees. Results are memoized per process by
  (repository, tree, version, code commit), with at most 8 entries, because the result is a pure function
  of those inputs.
- `own_paired_code_commit(memory_repository, treeish)` returns the code commit a memory commit's
  `Code-Commit` trailer names.
- `GitBaseConverter` is the composition-bound converter the validator's commit route uses
  (`GitKnowledgeValidation(base_converter=…)`). It converts the base at **its own** paired code tree (its
  `Code-Commit`, when that commit is in the code store) and otherwise falls back to the route's paired
  commit (review R1 finding 8).
- `comparison_sides(before, after, where)` applies rule 7 for any consumer: it returns the pair unchanged
  unless `before` is unconverted and `after` is converted.

### Conventions

- `BeforeSide` names where a before side lives: its memory repository and treeish, and its code
  repository and commit.

### Invariants And Boundaries

- **Known difference, fallback cards only (architect ruling N3).** A crossing sync (rule 8 step 2)
  converts every side at the own side's code tree, while `GitBaseConverter` uses the base's own
  `Code-Commit`. Only for a rule 2 fallback card (a card with no usable `lastVerifiedCommitHash`; 0 in the
  real tree) can the two conversions of one base differ. Every other card is anchored at its own verified
  commit and converts identically either way.
- **Wiring the consumers is theirs.** The validator's commit route is wired here, through
  `application/worktree_services.py`. The history sides (MIK-R07 rule 0), the onboarding gate (MIK-R30),
  the worklist (MIK-R08) and the reviewer (MIK-R25) are to call `comparison_sides` in their own leaves
  (architect ruling).

### Todos

MIK-R07, R30, R08 and R25 consumers still to wire `comparison_sides` (their leaves).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The converter, its binding and the rule 7 helper.

| Finding | Anchor | Source |
| --- | --- | --- |
| The layout marker's pinned version. | `pinned_version` | mcp/src/agents_remember/memory/conversion/base.py:38-44 |
| One base converted and memoized as a validator tree. | `converted_base` | mcp/src/agents_remember/memory/conversion/base.py:59-85 |
| The base's own paired code commit. | `own_paired_code_commit` | mcp/src/agents_remember/memory/conversion/base.py:88-98 |
| The commit route's converter, with the documented fallback-card difference. | `GitBaseConverter` | mcp/src/agents_remember/memory/conversion/base.py:101-139 |
| Rule 7 for any comparison consumer. | `comparison_sides`; `BeforeSide` | mcp/src/agents_remember/memory/conversion/base.py:152-167; mcp/src/agents_remember/memory/conversion/base.py:142-149 |
| The commit route validates against the conversion of an unconverted base, at the base's own code commit. | `test_the_commit_route_validates_against_the_conversion_of_an_unconverted_base` | mcp/tests/test_knowledge_crossing.py:293-336 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
