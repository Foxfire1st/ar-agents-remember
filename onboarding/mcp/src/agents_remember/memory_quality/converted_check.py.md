# mcp/src/agents_remember/memory_quality/converted_check.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/converted_check.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `overview.md` |

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
- `converted_knowledge_check(memory_root, code_root)` validates the working tree (`validate_tree`) against
  the code working tree (`CodeDirectory`), with the repository's converted `HEAD` as K_B when it has one
  (`_committed_base`). So anchors carried unchanged from `HEAD` are reported only when their path is gone
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

The not-applicable result and the converted check.

| Finding | Anchor | Source |
| --- | --- | --- |
| The legacy-format checks and their not-applicable result. | `LEGACY_FORMAT_CHECKS`; `not_applicable_on_converted` | mcp/src/agents_remember/memory_quality/converted_check.py:31-37; mcp/src/agents_remember/memory_quality/converted_check.py:40-49 |
| K_B is the converted HEAD, when there is one. | `_committed_base` | mcp/src/agents_remember/memory_quality/converted_check.py:52-63 |
| The validator's refusals are findings; its reports and stale references are report-only. | `converted_knowledge_check`; `CONVERTED_KNOWLEDGE_CHECK` | mcp/src/agents_remember/memory_quality/converted_check.py:66-93; mcp/src/agents_remember/memory_quality/converted_check.py:28-28 |
| The runner's dispatch to this module. | `_converted_check` | mcp/src/agents_remember/memory_quality/check.py:163-177 |
| Memory quality reads the converted format. | `test_memory_quality_reads_the_converted_format` | mcp/tests/test_knowledge_conversion_toolchain.py:118-135 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
