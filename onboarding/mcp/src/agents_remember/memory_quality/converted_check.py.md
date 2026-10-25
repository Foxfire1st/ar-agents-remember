# mcp/src/agents_remember/memory_quality/converted_check.py

## Governing Overview

[memory_quality route overview](overview.md)

## Purpose

**The memory-quality run on a converted memory tree (MIK-R24 rule 5).** A converted card has no metadata
table, no Update History and no citation tables, so the checks that read those have nothing to check.
Currentness comes from anchors instead, so the integrity slot runs the knowledge validator plus the
stale-reference report. `memory_quality/check.run_memory_quality_check` dispatches here when the tree
holds `knowledge/layout.json`.

## Code Commentary

### Landing-report scope

The converted check optionally joins landing observations to `reportOnlyFindings` and exposes cut-card counts/rows plus added-file counts/bytes/rows. Its `landing_base` is separate from the validator `base`: admitted leaves use the contract base so committed leaf progress remains visible. `include_landing=False` lets the drift summary measure only validator/reference state without acquiring the landing census. Landing rows never enter `findings`, change `ok`, or count as actionable.


- Landing facts join only the report-only population; their leaf base is independent from the validator base.




### Logic


- `converted_knowledge_check(memory_root, code_root, *, base=None)` validates the working tree
  (`validate_tree`) against the code working tree (`CodeDirectory`). Its K_B comes from `_comparison_bases`:
  without a `base` port, the repository's converted `HEAD` when it has one (`_committed_base`); with one
  (L37 review R3-1), whatever the `KnowledgeBasePort` returns, which the application binds to `HEAD` or, when
  `HEAD` is unconverted, to its conversion from the shared converted-base cache (MIK-R24 rule 7). A base the
  port cannot build is one refusing finding, `R24.7-converted-base` at `knowledge/layout.json`
  (`_unbuildable_base`), never a comparison against nothing. The base decides only the base-dependent
  `R22.6-anchor-path` refusal; `R198.1-reference-anchor` is base-independent, so a carried anchor whose
  blob or content identity does not hold at the paired code tree is a finding (MIK-R198 rule 5).
  Refusing violations are findings, stale reference anchors among them; validator reports are
  report-only. The check name is `knowledge.converted`, and the
  result also carries the reference state counts.
- When the base cannot be built, carried-vs-new classification is unknown, so the base-dependent
  anchor-path refusals are withheld instead of being decided against an invented empty base: the named
  unbuildable-base refusal is recorded, every independently measurable reference state keeps being
  reported, and no new/carried base-dependent refusal fires; `R198.1-reference-anchor` reads only the
  candidate and the paired code tree, so it keeps refusing. The result also carries `sidecarCount` and
  `unreadableSidecars` for the drift summary to name what it measured.

### Conventions

- `CONVERTED_KNOWLEDGE_CHECK` names the surviving validator/reference result; retired format check names are not registered.

### Invariants And Boundaries

- A stale reference anchor is a finding here, the validator's `R198.1-reference-anchor` refusal; `citation_fix` or curator re-authoring refreshes it.
- `ok` is exactly `not findings`; stale reference anchors change it, and only landing observations stay report-only. Historical run counts are not a measurement of this candidate.

### Todos

None recorded.

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

The converted validator/reference result and its dispatch boundary.


- K_B is the converted HEAD, when there is one. [2]

- The runner's dispatch to this module. [4]

- Memory quality reads the converted format. [5]


- The validator's bases, and why a converted base could not be built. [6]



- An unbuildable base withholds base-dependent refusals; measurable states keep reporting. [8]



### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.

- The validator's refusals are findings, and a stale reference anchor is one of them; only its reports stay report-only. [3]


- The check takes the base port and reports an unbuildable base as a finding. [7]
