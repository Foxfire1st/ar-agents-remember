# mcp/tests/test_closeout_queue_projection.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/tests/test_closeout_queue_projection.py`          |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-09-03T12:30:00+02:00                              |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b`            |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00                              |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Covers closeout projection reconstruction from current task, review, priority, waiting-door, and
source-pair activation truth. The suite proves old rows are never rebuild input, source evidence
drift is fingerprinted, unsafe filesystem authorities fail closed, completed sprints become valid
terminal-empty projections, and multiple live atomic series remain independently observable.

## Code Commentary

### Logic

The fixture publishes canonical tasks and waiting doors, then calls the production rebuild path.
Focused cases mutate one source at a time: task/review/grade evidence, nonregular series or door
entries, a symlinked door ancestor, sprint completion, activation reselection, and malformed
activation. The two-series case selects master A then master B and checks that readiness and
`atomic-series-paused-by` waiting reverse without deleting either series.

The CCR cohort distinguishes completion-readiness invalidation from display/audit changes that stay
outside source currentness, carries composite-binding failures into exact invalid-empty source
problems, proves a candidate-relevant dependency edge changes v2 identity, and checks that both DAG
and graphless atomic-sequential routes share one fingerprint across coherence, door, and queue.

Under CCR-R03@v1 the review-evidence drift case expects `route-review-evidence-stale` as the
projection reason (replacing the former `door-review-provenance-stale`), because review provenance
is now the route-review record digest and evidence-byte drift surfaces through the route-review
currentness seam cit:([`test_review_evidence_drift_changes_source_identity_and_blocks_member`], mcp/tests/test_closeout_queue_projection.py:203-212).

### Conventions

Filesystem hazards use real paths; projection membership is asserted through public model fields.
Selector corruption is injected directly only to prove strict observation and scoped invalidation.

### Invariants And Boundaries

- Rebuild inputs are current canonical sources, never old projection rows.
- Multiple live series are valid; selection supplies readiness, not existence or retirement.
- Malformed/nonregular evidence becomes explicit invalid-empty projection evidence, never absence.
- Projection failure does not mutate task truth, selector state, or operation lifecycle evidence.
- Only classified completion-readiness and structural topology facts change currentness; display and
  audit fields do not.
- Coherence, the waiting door, and the rebuilt member must agree on one topology fingerprint.
- Review-evidence drift is reported as `route-review-evidence-stale` under the R03 digest seam.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Rebuild discards old rows and derives membership only from current waiting doors. | `test_rebuild_uses_only_current_waiting_doors_not_old_rows` | mcp/tests/test_closeout_queue_projection.py:41-63 |
| Multiple live series project selected/paused waiting independently. | `test_multiple_live_atomic_series_are_valid_active_paused_waiting_candidates` | mcp/tests/test_closeout_queue_projection.py:307-364 |
| Malformed activation invalidates only the disposable projection and names selection repair. | `test_malformed_activation_invalidates_only_projection_and_names_selection_repair` | mcp/tests/test_closeout_queue_projection.py:366-386 |
| Readiness changes invalidate while display/audit-only edits preserve exact source identity. | "L3 source-census purity, drift fencing, and terminal-empty forcing." | mcp/tests/test_closeout_queue_projection.py:1-1; mcp/tests/test_closeout_queue_projection.py:87-115 |
| Composite-binding refusal and a relevant dependency edge affect the explicit topology source plane. | "L3 source-census purity, drift fencing, and terminal-empty forcing." | mcp/tests/test_closeout_queue_projection.py:1-1; mcp/tests/test_closeout_queue_projection.py:117-168 |
| Graphless and DAG routes share one topology fingerprint across coherence, door, and queue. | "L3 source-census purity, drift fencing, and terminal-empty forcing." | mcp/tests/test_closeout_queue_projection.py:1-1; mcp/tests/test_closeout_queue_projection.py:170-197 |
| Review-evidence drift reason under the R03 evidence digest seam. | `test_review_evidence_drift_changes_source_identity_and_blocks_member` | mcp/tests/test_closeout_queue_projection.py:203-212 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned projection suite.

| Finding | Anchor | Source |
| --- | --- | --- |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces source-census purity, deterministic fingerprints, drift fencing, malformed-neighbor refusal,
waiting-only membership, valid terminal-empty projections, and independent atomic-series activation.
Two simultaneous live series are valid: the selected master can be ready while the other reports
`atomic-series-paused-by`, and switching selection reverses the candidate-local waits. With no
selection, both wait as `atomic-series-not-selected`. Malformed selector evidence invalidates only
the disposable projection and names selecting-dispatch repair; it does not mutate tasks or lifecycle
evidence.

### Current Invariants

- Old queue rows are never rebuild input.
- Source mismatch or unreadable authority is non-admitting and never treated as absence.
- Multiple live series contracts are normal; activation state, not contract census order, supplies
  selection waiting.
- Corrupt activation produces invalid-empty projection and explicit repair rather than stale rows
  or a task-authoring lock.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the `route-review-evidence-stale` projection reason replacing `door-review-provenance-stale`; prior rebuild, activation, and fingerprint prose preserved.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8 follow-up: documented readiness-versus-audit
  invalidation, exact topology refusal, relevant-edge drift, and shared coherence/door/queue v2
  identity for both DAG and graphless modes. Verification remains closeout-owned.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: regenerated the two moved multi-series
  activation ranges after semantic-topology projection cases were added. Verification remains
  closeout-owned.

- 2026-08-26T08:45+02:00 — Replaced obsolete queue-artifact references with the frozen
  door-derived, multi-series activation cases and restored canonical Docs/Cross-Repo sections.

- 2026-08-26T03:37+02:00 — Added real two-live-series activation switching and malformed-selector
  projection-isolation forcing. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.

- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the closeout-queue projection test suite.
  Verification metadata pinned until closeout stamps the L8 commit.