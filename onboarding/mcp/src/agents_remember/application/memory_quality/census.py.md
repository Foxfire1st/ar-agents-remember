# mcp/src/agents_remember/application/memory_quality/census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_quality/census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:45+02:00|
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532` |
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Application overview](../overview.md)

## Purpose

Builds the complete memory-candidate census used before certification admission and adapts every
governed onboarding identity into the curator's one-to-one coherence candidate list. The module
keeps this structural inventory non-certifying: it reports exact rows and blockers without granting
semantic acceptance or a code/memory commit.

## Code Commentary

### Logic

`prepare_memory_census` captures the contract-scoped code and memory candidate pair and builds the
full `MemoryCensusResult`; prepared code recovery supplies the selected code tree as provenance
while retaining the logical pair identity. `publish_memory_census` rereads the scope before
atomically writing the enclosure report, returns bounded diagnostics, and marks any census blockers
without calling the result certified.

`census_curator_candidates` converts every governed census row exactly once to a
`CuratorSourceCandidate`, requiring an onboarding-relative path, canonical source identity, and
unique candidate identity. `_curator_source` reads the exact candidate or baseline sidecar metadata
for file and route artifacts, while entity rows and inline onboarding use their own canonical
identity rules. Missing or ambiguous identity fails closed.

### Conventions

Candidate reports are JSON with a schema version, exact scope, complete census, bounded response
rows, and a SHA-256 of the written bytes. The report is operational evidence only; the lifecycle
coherence authority owns semantic dispositions and publication.

### Invariants And Boundaries

- The captured scope must remain unchanged between preparation and report publication.
- Every governed onboarding artifact must map to one canonical source or entity identity; duplicate
  normalized identities are refused.
- Prepared code-tree input is provenance for recovery comparison and does not fabricate a commit.
- This module does not edit onboarding, decide curator judgments, certify tests, or publish protected
  source changes.

### Todos

None recorded.

## Docs References

The resolved Domain Documentation registry has no entries, so no external documentation claim is
made for this repository-owned census boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | n/a | n/a |

## Repo-Internal References

The source file is the direct implementation evidence; the application and closeout overviews
describe adjacent preparation and certification ownership.

| Finding | Anchor | Source |
| --- | --- | --- |
| Contract-scoped census preparation and selected-tree provenance. | `prepare_memory_census`; `_prepared_code_input` | mcp/src/agents_remember/application/memory_quality/census.py:34-46; mcp/src/agents_remember/application/memory_quality/census.py:139-153 |
| Exact report publication and non-certifying diagnostics. | `publish_memory_census` | mcp/src/agents_remember/application/memory_quality/census.py:49-81 |
| One-to-one curator candidate mapping and canonical identity refusal. | `census_curator_candidates`; `_curator_source` | mcp/src/agents_remember/application/memory_quality/census.py:84-106; mcp/src/agents_remember/application/memory_quality/census.py:109-136 |
| Census publication is diagnostic and non-certifying. | `publish_memory_census` | mcp/src/agents_remember/application/memory_quality/census.py:49-81 |

## Cross-Repo References

No cross-repository implementation or external-system boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo reference applies. | n/a | n/a |

## Source File Binding

The current uncommitted source bytes are SHA-256
`98de0b239e531461170820d022e4901a873f250cde7d6587bd64cdd065863143` (`6245` bytes, `153` lines).
Verification metadata remains blank until closeout creates a genuine code commit.

## Update History
- 2026-09-10T00:20:36+02:00 — CCR-L42 provenance repair: the current census source bytes match the existing code commit `01f1f85d90d2123764a4029d9ed17db28e540eed`; the real source provenance is recorded without asserting task closeout or acceptance.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake repaired the inherited malformed card with the
  canonical metadata, current census/candidate mapping contract, exact source binding, and
  repository-owned references. The source is an uncommitted candidate; no future commit, test,
  review, or acceptance claim is made.
- 2026-09-08T14:45:44+00:00 — CCR-L24 preparation normalized the inherited date-only history bullet to an offset-bearing ISO timestamp while preserving its date and text.
- 2026-09-08T00:00:00+00:00 — Initial creation for MCAR L04
