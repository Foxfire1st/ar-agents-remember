# mcp/tests/test_lifecycle_operation_dispositions_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operation_dispositions_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces completed-closeout disposition authorization, publication, and recovery at the public and
durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_completed_unintegrated_disposition_preserves_artifacts`,
`test_sprint_orchestrator_status_payload_executes_public_disposition`,
`test_completed_disposition_is_not_advertised_or_executable_by_leaf`,
`test_status_keeps_completed_closeout_actionable_beside_newer_cancelled_integrate`, and
`test_public_supersede_recovers_before_and_after_contract_publication`. Retirement uses the
standalone task owner and preserves the existing door publication/history exactly. Supersession
uses the sprint-orchestrator owner, publishes a distinct waiting successor, and moves the prior
door proof into history. A leaf worker remains neither advertised nor accepted.

The suite forces the same authority distinction through public status/control calls, immutable
artifact preservation, coexistence with a newer cancelled integration, exact supersede replay and
competing-declaration refusal. Crash-cut recovery is intentionally supersede-specific because it is
the disposition that publishes a successor door; a pre-write cut returns executable recovery
arguments, while a post-write cut is observed as already successful.

Under CCR-R03@v1 the artifact-preservation contract now requires the current record's declared
dependency set (`require_lifecycle_operation_dependencies`), excludes `dependencies` from the
expected preserved artifacts, and asserts supersede produces a new dependency declaration while
retire/integrate preserve the record's existing one
cit:([`_disposition_preserved_artifacts`, `test_completed_unintegrated_disposition_preserves_artifacts`], mcp/tests/test_lifecycle_operation_dispositions_l2.py:64-77; mcp/tests/test_lifecycle_operation_dispositions_l2.py:116-162).

### Conventions

Tests address operations by task/contract plus kind and generation, assert durable evidence and public legal controls, and compare state across failure cuts. Helpers remain test-only and invoke the same public/domain seams as production.

### Invariants And Boundaries

- A passing assertion must prove the advertised action executes or terminates safely; payload shape alone is insufficient.
- Completed-disposition controls are owner-scoped: standalone ownership and sprint orchestration
  authorize them, while leaf execution is neither advertised nor accepted.
- Queue projection is never accepted as lifecycle evidence, and private operation identifiers do not cross the public test boundary.
- Failure-path assertions check non-mutation or exact same-generation recovery, not merely an exception string.
- Supersede changes the record's dependency declaration (new successor inputs); retire preserves it.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

The test source is the direct evidence for the regression contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The file defines five public completed-closeout disposition forcing seams covering artifact preservation, sprint-orchestrator execution, leaf refusal, multi-operation status projection, and interrupted publication recovery. | `_sprint_owner`; `_disposition_preserved_artifacts`; `test_completed_unintegrated_disposition_preserves_artifacts`; `test_sprint_orchestrator_status_payload_executes_public_disposition` | mcp/tests/test_lifecycle_operation_dispositions_l2.py:54-58; mcp/tests/test_lifecycle_operation_dispositions_l2.py:61-108; mcp/tests/test_lifecycle_operation_dispositions_l2.py:111-155; mcp/tests/test_lifecycle_operation_dispositions_l2.py:158-192 |
| `completed_disposition_authorized` is imported directly and asserts standalone-owner and sprint-orchestrator authorization plus leaf-worker denial before the corresponding public control paths are exercised. | "from agents_remember.application.lifecycle.lifecycle_control_authority import (" | mcp/tests/test_lifecycle_operation_dispositions_l2.py:10-12 |
| A disposition interrupted before contract publication remains recoverable through the returned public control arguments; a cut after the write is observed as successful, and both paths end with proven durable publication. | `test_public_supersede_recovers_before_and_after_contract_publication`; `test_supersede_exact_replay_converges_and_competing_declaration_refuses` | mcp/tests/test_lifecycle_operation_dispositions_l2.py:283-361; mcp/tests/test_lifecycle_operation_dispositions_l2.py:364-407 |
| R03 dependency-required artifact preservation. | `_disposition_preserved_artifacts`; `test_completed_unintegrated_disposition_preserves_artifacts` | mcp/tests/test_lifecycle_operation_dispositions_l2.py:64-77; mcp/tests/test_lifecycle_operation_dispositions_l2.py:116-162 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces completed-closeout integrate, retire, and supersede dispositions while preserving exact artifacts and generation history.

### Current Invariants

- A completed-unintegrated operation remains journal-addressable outside the queue.
- Retirement preserves door publication/history; supersession creates a distinct waiting generation and retains the claimed predecessor in history.

## 260831-CCR-L15 Disposition Cursor Parity

Disposition-preserved artifacts now exclude `meaningfulRevision` alongside
`recordRevision` (both are journal-mutable), and the completed-unintegrated tests assert
the CCR-R15 cursor advances exactly once per accepted store mutation, in parity with
`recordRevision` (retire one advance, supersede two).

## Update History

- 2026-09-05T07:19:22+00:00 — L31-MR-02 history recovery: restored the original dated L18 entry verbatim from memory commit fd41221f11dfe5ac2993520c0d7176ada59ce2ba (its recorded code provenance: f93ac631ca161e5880db3a937728cb256686b13b). This preserves sibling curation history; current body and verification metadata are unchanged.


- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the `meaningfulRevision` disposition-exclusion and cursor-parity assertions.
- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the revision-aware disposition artifacts (retire +1 / supersede +2) and the new dry-run supersede preview forcing. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: split the
  comma-separated source cells into ';'-separated path:start-end citations and widened
  the second range to the test lines that carry the anchor.
- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the dependency-required preservation contract and the supersede-changes/preserve-otherwise declaration assertions; prior disposition-authorization and recovery prose preserved.

- 2026-08-26T10:44:52+02:00 — Corrected the disposition contract: retire preserves the current door under standalone authority, while sprint-owned supersede alone publishes/retries a waiting successor and retains predecessor proof in history.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T17:03+02:00 — 260821-CLIVE-L2: reconciled the reviewed post-clearance
  authorization assertions and direct production-helper import; verification fields remain
  closeout-owned.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.