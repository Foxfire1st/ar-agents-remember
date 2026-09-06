# mcp/tests/test_memory_quality_runs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_quality_runs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Bounded memory-quality run state and pair-currentness refusal.

## Code Commentary

### Logic

Registry cases retain completed/failed outcomes, unknown-run absence, launch rollback and repository-scoped polling privacy. A controller case changes the code/memory pair while deriving evidence and requires scope-refused with no curator publication.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A scan result cannot publish against a moved pair. Registry state is operational polling data, not a semantic acceptance certificate.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Start poll completed failed and unknown. | `test_start_poll_completed_failed_and_unknown` | mcp/tests/test_memory_quality_runs.py:70-85 |
| Launch failure rolls back the admitted slot. | `test_launch_failure_rolls_back_the_admitted_slot` | mcp/tests/test_memory_quality_runs.py:87-93 |
| Wrong repository poll never discloses any run state. | `test_wrong_repository_poll_never_discloses_any_run_state` | mcp/tests/test_memory_quality_runs.py:95-107 |
| Pair change during derived evidence refuses before curator publication. | `test_pair_change_during_derived_evidence_refuses_before_curator_publication` | mcp/tests/test_memory_quality_runs.py:144-199 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller-under-test row (48-144 to exact spans) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the candidate-tree capture mock in the curator-publication controller case; prior registry, capacity, and pair-forcing prose preserved.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: expanded total controller proof for async
  pair refusal, stale candidate polling, official running/failed polling, final publication
  identity, and pair revalidation. The derived-evidence race now mocks its unrelated Git-owned
  classifier so it reaches the intended third revalidation seam.

- 2026-08-29T21:46+02:00 — MCAR-L03: added exact-pair async start/poll/race/refusal coverage.
  Dagger verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the memory-quality controller/run package extraction; concurrency, saturation, polling, and result-identity behavior are unchanged.
- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: rebuilt the focused registry/controller tests around typed identity, hard live capacity, terminal-only pruning, and nondisclosing poll ownership. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: added the never-settles registry
  regression and made the wrapper start/poll case deterministically observe the running envelope
  before completion. Verified at code commit e5cb139f.

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R7: the run-registry forcing suite
  (start/poll/completed/failed/single-flight/boundedness/TTL eviction) plus the application-wrapper
  tests covering the started/run-not-found/running/failed envelope branches and the key-scoping
  branches (extended in the gate-repair rounds). Verified at code commit de3a0fd9.