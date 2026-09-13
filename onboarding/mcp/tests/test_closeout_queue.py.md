# mcp/tests/test_closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T18:06+02:00 |
| lastVerifiedCommitHash | `e0820b04a499cbfb2079c78485346c50917a238a` |
| lastVerifiedCommitDate | 2026-09-13T18:02:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Disposable task, door and projection fixture shared by lifecycle tests.

## Code Commentary

### Logic

QueueFixture creates real code and optional external-memory repositories, task topology, contracts and shared priority/judgment data. Its helpers declare doors and construct the source/projection conditions required by consumers. The file contains no retained standalone queue tests.

Since 260831-LOCR-L36 the fixture also authors and starts canonical leaves the way the workflow does.
`author_unstarted_leaf` cit:([`author_unstarted_leaf`], mcp/tests/test_closeout_queue.py:318-369)
commands one more canonical leaf **without starting any of its work**: the master's subtask row and
the leaf's own task document are written — an atomic master's review scope has to resolve every
commanded leaf's document — and the leaf's judgment and priority register rows are added, but no
enclosure contract, branch or worktree exists yet. The commanded id is recorded on
`QueueFixture.unstarted_leaf_a`. `start_leaf` cit:([`start_leaf`], mcp/tests/test_closeout_queue.py:370-441) then starts one authored leaf from its
master's branches **as they now stand** (a real enclosure, leaf document, worktrees and branches,
based on the master's current tips rather than the base it had when the leaf was first commanded),
publishes the lifecycle operation location and writes curator evidence. `declare_leaf`
cit:([`declare_leaf`], mcp/tests/test_closeout_queue.py:625-655) declares the closeout door for a leaf that is not yet the
master's current one, reading its own canonical grade from the priority register it was authored with
and naming the master whose command it executes.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Synthetic upstream curator evidence in the convenience declaration is fixture-only; producer-backed memory tests call the real door owner with actual coherence instead. No helper declaration grants production acceptance.

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
| Master. | `_master` | mcp/tests/test_closeout_queue.py:77-105 |
| Leaf. | `_leaf` | mcp/tests/test_closeout_queue.py:106-153 |
| Judgment row. | `_judgment_row` | mcp/tests/test_closeout_queue.py:154-161 |
| Priority row. | `_priority_row` | mcp/tests/test_closeout_queue.py:162-165 |
| Judgment table. | `_judgment_table` | mcp/tests/test_closeout_queue.py:166-169 |
| Priority table. | `_priority_table` | mcp/tests/test_closeout_queue.py:170-173 |
| Grade. | `_grade` | mcp/tests/test_closeout_queue.py:174-180 |
| Queuefixture. | `QueueFixture` | mcp/tests/test_closeout_queue.py:181-722 |
| Command a canonical leaf with no work started: subtask row, leaf document, judgment and priority rows only. | `author_unstarted_leaf` | mcp/tests/test_closeout_queue.py:318-369 |
| Start an authored leaf from its master's current tips, creating the enclosure, worktrees and branches. | `start_leaf` | mcp/tests/test_closeout_queue.py:370-441 |
| Declare the closeout door for a leaf that is not yet the master's current one, with its own authored grade. | `declare_leaf` | mcp/tests/test_closeout_queue.py:625-655 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-13T18:06+02:00 — 260831-LOCR-L36: recorded the fixture's three new workflow-shaped leaf
  helpers. `author_unstarted_leaf` commands one more canonical leaf without starting its work
  (subtask row, leaf document, judgment and priority rows, and the `unstarted_leaf_a` id), `start_leaf`
  starts an authored leaf from its master's **current** tips and creates the real enclosure,
  worktrees, branches, operation location and curator evidence, and `declare_leaf` declares the
  closeout door for a leaf that is not yet the master's current one. Re-derived every reference range
  in this card against the current 722-line source. Verification metadata remains closeout-owned; no
  execution or acceptance claim.

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the fixture profile installation and certificationProfile settings in queue fixtures.


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
