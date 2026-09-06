# mcp/tests/test_citation_deterministic_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_deterministic_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

CCR-R10 forcing fixtures for exact anchor-to-range projection and its integration with the citation fixer. Unique moves bind the frozen source-index snapshot, prior claim digest, oracle extents, final document digest and repair-tool version. The same accepted document batch carries the generated no-content-impact history when a section exists. Multiple definitions, mention-only anchors, renames, deletion, stale snapshots and malformed claims retain explicit refusals without guessing.

This standalone temporary-file suite focuses on projection semantics. The actual publication/conflict/normalization seam is covered in `test_citation_document_transaction.py`; the removed planning-only `TransactionSeamTests` and mocked normalization class are not current coverage.

## Code Commentary

### Logic

`document`, `Tree` and `TreeCase` construct code and memory roots, canonical cards and a fixed-clock fixer invocation. `UniqueMoveProjectionTests` checks complete bindings, parseable newest-first history, prospective dry-run records, repeat no-ops, deterministic replay, absent history sections, multi-anchor extents, in-file tiebreakers and unparsed single occurrences. `ProjectionRefusalTests` covers rename/deletion/ambiguity/mention-only/malformed input and stale snapshots.

`ProjectionBoundaryTests` forces ambiguous or missing repair extents. `ProjectionDeclineThroughFixerTests` now requires a two-file anchor decline to leave the entire document and existing history unchanged, with zero repairs, writes and projections. `StagingGuardTests` retains one run timestamp and exact per-document digests; `ClockContractTests` requires a UTC-aware instant.

### Conventions

Tests drive the real `fixer.fix_onboarding_root` with
`deterministic_projection.now_utc` patched to a fixed instant so replays are byte-for-byte;
refusal assertions read the exact decline codes.

### Invariants And Boundaries

- Only exact unique moves produce a deterministic projection; no old-range fallback or similarity search is admitted.
- A projection decline cannot stage its source edit or history, and never contributes a successful repair count.
- Accepted range and generated history edits share their complete document digest.
- The module does not import test-support fixture modules; real publication interference scenarios live in the adjacent transaction suite.

### Todos

None.

## Docs References

No external Domain Documentation source is configured. This card describes the repository's own implementation and forcing contracts without an external documentation claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

Projection semantics and actual publication interference retain distinct forcing owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two-root fixture drives the actual fixer and range checker. | `Tree` | mcp/tests/test_citation_deterministic_projection.py:72-118 |
| Successful projections bind every packet field and deterministic document/history behavior. | `UniqueMoveProjectionTests` | mcp/tests/test_citation_deterministic_projection.py:147-332 |
| Rename, deletion, ambiguity, mention-only, malformed and stale-snapshot scenarios refuse. | `ProjectionRefusalTests` | mcp/tests/test_citation_deterministic_projection.py:335-431 |
| Missing and multiple exact repair extents cannot produce a projection. | `ProjectionBoundaryTests` | mcp/tests/test_citation_deterministic_projection.py:434-509 |
| A two-file decline leaves exact original document bytes and all successful counters unchanged. | `ProjectionDeclineThroughFixerTests` | mcp/tests/test_citation_deterministic_projection.py:512-550 |
| A full fixer run preserves its timestamp and isolates each document digest. | `StagingGuardTests` | mcp/tests/test_citation_deterministic_projection.py:553-617 |
| The injected clock contract stays UTC-aware. | `ClockContractTests` | mcp/tests/test_citation_deterministic_projection.py:620-631 |
| Publication-time conflicts are exercised through actual document writes in the companion suite. | `test_observed_conflict_refuses_the_whole_document_and_preserves_other_batches` | mcp/tests/test_citation_document_transaction.py:159-192 |
| The projection suite remains an integration-lane member. | "mcp/tests/test_citation_deterministic_projection.py" | mcp/tests/test-evidence-lanes.toml:251-251 |

## Cross-Repo References

This file introduces no separate cross-repository protocol. Local temporary code/memory roots and their application write-scope contract remain distinct from a cross-repository authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No new cross-repository protocol. | N/A | N/A |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Replaced the accepted-decline expectation with exact unchanged-document refusal; routed removed planning-only seam coverage to the real transaction suite and refreshed all live class ranges. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R10 deterministic anchor-range projection forcing suite
  delivered in code commit 709dd076; anchors and ranges derived from the current worktree source
  and pinned to that commit. The suite entered the `integration` lane of
  `test-evidence-lanes.toml` in the same change.
