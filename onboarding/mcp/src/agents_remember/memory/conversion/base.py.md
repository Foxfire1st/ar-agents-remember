# mcp/src/agents_remember/memory/conversion/base.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The converter, its binding and the rule 7 helper.

- The layout marker's pinned version. [1]
- One base converted and memoized as a validator tree. [2]
- The base's own paired code commit. [3]
- The commit route's converter, with the documented fallback-card difference. [4]
- Rule 7 for any comparison consumer. [5]
- The commit route validates against the conversion of an unconverted base, at the base's own code commit. [6]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
