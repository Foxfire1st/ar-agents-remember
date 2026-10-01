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

### Logic

- `LEGACY_FORMAT_CHECKS`: `style.update_history.history_order`, `style.citations.range_resolution` and
  `style.citations.claim_reopen`. On a converted tree each returns `not_applicable_on_converted(check)`:
  `ok`, status `not-applicable-converted`, 0 findings.
- `converted_knowledge_check(memory_root, code_root, *, base=None)` validates the working tree
  (`validate_tree`) against the code working tree (`CodeDirectory`). Its K_B comes from `_comparison_bases`:
  without a `base` port, the repository's converted `HEAD` when it has one (`_committed_base`); with one
  (L37 review R3-1), whatever the `KnowledgeBasePort` returns, which the application binds to `HEAD` or, when
  `HEAD` is unconverted, to its conversion from the shared converted-base cache (MIK-R24 rule 7). A base the
  port cannot build is one refusing finding, `R24.7-converted-base` at `knowledge/layout.json`
  (`_unbuildable_base`), never a comparison against nothing. So anchors carried unchanged from `HEAD` are reported only when their path is gone
  (MIK-R22 rule 6). Refusing violations are findings. Report-only violations and every stale reference
  (`reference_state.check_references`) are report-only. The check name is `knowledge.converted`, and the
  result also carries the reference state counts.

### Conventions

- The check names in `LEGACY_FORMAT_CHECKS` are the checks' own `CHECK_NAME` values.

### Invariants And Boundaries

- A stale reference is never a finding here; it is refreshed through the onboarding gate (MIK-R30).
- On the real converted copy the run is `ok` with 0 findings (576 report-only). The installed runtime does
  not carry this dispatch before MIK-R37.

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

The not-applicable result and the converted check.

- The legacy-format checks and their not-applicable result. [1]
- K_B is the converted HEAD, when there is one. [2]
- The validator's refusals are findings; its reports and stale references are report-only. [3]
- The runner's dispatch to this module. [4]
- Memory quality reads the converted format. [5]

- The validator's bases, and why a converted base could not be built. [6]
- The check takes the base port and reports an unbuildable base as a finding. [7]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
