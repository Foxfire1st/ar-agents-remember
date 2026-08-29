# mcp/tests/test_closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T11:41+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Exercises the closeout queue's model, authority, ordering, evidence, transition, durability,
capacity, projection-cost, and sprint-publication contracts against real task and Git fixtures.
The small model and split-evidence ownership checks live in `test_closeout_queue_models.py` so this
behavior suite remains below the repository hard size limit.

## Code Commentary

### Logic

`QueueFixture` constructs canonical sprint/master/leaf task documents, contracts, curator artifacts,
register rows, repositories, and ledger facts. Tests cover categorical grading and deterministic
ties, internal/disabled memory, request bounds, authority refusal, predecessor/blocker logistics,
candidate/evidence drift, lifecycle ownership, WAL retry receipts, state bounds, linear fleet work,
cross-sprint refusal, and completion/reopen locking.

The fixture now independently configures master A and master B as atomic, always uses canonical
leaf-B identity, and derives each contract's source branch from that master's own atomic flag. This
lets projection tests represent two simultaneous live series contracts without encoding an
exclusive lane in shared setup.

### Conventions

The suite manipulates the public service and durable store with production-shaped artifacts; exact
failure states are asserted rather than inferred from source strings.

### Invariants And Boundaries

- Judgment and logistics tests remain separate.
- Negative cases mutate one candidate fact at a time.
- Scaling tests compare two fleet sizes and enforce explicit caps.
- Live-series multiplicity is fixture input, not a queue conflict or ownership shortcut.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public request vocabulary exposes projection-only status and invalidation actions, not a selector. | `test_queue_request_has_projection_only_actions` | mcp/tests/test_closeout_queue.py:545-553 |
| Waiting membership appears only after closeout-door publication; an empty queue does not invent candidates. | `test_door_publication_is_the_only_fixture_membership_source` | mcp/tests/test_closeout_queue.py:555-561 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Frozen Current Regression Contract

The current forcing seams are `test_queue_request_has_projection_only_actions` and
`test_door_publication_is_the_only_fixture_membership_source`. They prove the projection-only
request vocabulary and door-derived waiting membership; no selector, lifecycle, commit-evidence,
compatibility-reader, or task-authoring lock behavior is assigned to the queue.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises the projection-only request and door-membership cases. | `CloseoutProjectionSurfaceTests` | mcp/tests/test_closeout_queue.py:534-551 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Provides the shared L3 task/door/projection fixture plus projection-only smoke tests for current closeout scheduling.

### Current Invariants

- Projection membership derives from current task truth and waiting door generations.
- The fixture does not preserve claimed lifecycle, blocker, or commit evidence in queue rows.

## MCAR-L02 Structured Fixture Authority

The shared `write_curator_evidence` helper publishes a real structured coherence authority after
writing the exact quality attestation. Candidate fixtures create agent judgments with explicit
task evidence and invoke prepare/publish through production owners, so queue tests no longer obtain
readiness from a hand-authored curator Markdown file alone. Door declaration now republishes once
after priority/task input changes and again after the door mutation. The production validator thus
sees the exact current topology on both sides of the mutation instead of a fixture-created stale
authority.

## Update History

- 2026-08-29T11:41+02:00 — Moved structured coherence setup into the shared test-support owner and
  made door fixtures explicitly republish around their two task-topology mutations. This preserves
  the production fail-closed validator while repairing fixture ordering. Verification remains
  closeout-owned.

- 2026-08-29T08:52+02:00 — Upgraded queue fixtures to publish the structured curator-coherence
  authority through production code. Verification remains closeout-owned.

- 2026-08-26T08:30+02:00 — Replaced the remaining obsolete transitional-queue regression section
  with the frozen projection-only and door-membership contract.

- 2026-08-26T08:25+02:00 — Removed stale citations to deleted pre-PDLS queue cases and rebound the
  card to its frozen two-case projection-only surface. No retired selector/lifecycle claim remains.

- 2026-08-26T03:37+02:00 — Generalized the shared queue fixture to independent atomic masters so
  multiple live series and activation projection are exercised without an exclusive-lane fixture
  assumption. Verification remains post-Dagger/closeout-owned.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the removed `require_queue_candidate_current` import and
  its direct drift-test call are gone; the atomic-release mock re-points to
  `closeout_queue_blocker.require_atomic_master_landed` after the blocker extraction. No scenario
  changed. Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the segment-graph queue scenarios moved to
  `test_closeout_queue_segments.py` under the file-size rail (fixtures imported from here);
  `QueueFixture` gains segment helpers. Verification remains closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: `QueueFixture` now publishes the real runtime configuration at the workspace-owned path consumed by lifecycle operation inputs.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: shared queue fixtures now render the
  exact canonical Judgment and Priority Register headings, headers, separators, and rows consumed
  by production rather than relying on width-shaped Markdown fragments.
- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: the atomic-series success fixture now proves
  explicit approved human review, preserving its intended all-prerequisites landing path.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: made task rows canonical Markdown refs, stopped the
  negative grade fixture from healing its own corruption, restored exact tree-drift assertions,
  kept persistence-size forcing stable, and moved commit binding to the integration suite.
- 2026-08-15T10:24+02:00 — L3 file-size repair: moved the two small model/ownership checks into
  `test_closeout_queue_models.py`; the fixture and all queue behavior scenarios remain here.
- 2026-08-15T10:10+02:00 — L3 targeted-gate repair: imported the two split evidence modules
  directly and asserted their public owners are callable, allowing deterministic gate-scope
  derivation to select this existing behavior suite.
- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair makes fixture model-validation
  boundaries and external-memory narrowing explicit; the queue scenarios, failure injection, and
  assertions are unchanged.
- 2026-08-15T09:10+02:00 — Created for L3's primary queue behavior and durability suite; verification remains closeout-owned.
