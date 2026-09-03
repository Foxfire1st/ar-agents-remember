# test_seat_lifecycle.py

| Field                  | Value                                     |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                               |
| path                   | `mcp/tests/test_seat_lifecycle.py`            |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview      | `overview.md`                                 |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_seat_lifecycle.py` is the regression suite for task-document-owned seat retirement,
renaming, liveness, landing, and completion cleanup. It exercises pure and end-to-end retirement
authority against a real task topology, diagnostic turn-state handling, task-scoped landing, and
the integrate/finalize auto-close or opt-out landing paths. Runtime ids remain test correlations;
task document plus role is the authority under test.


CCR-R22@v1 (L22, commit `685f83c44055`): `_config` now supplies a `repositories` map with a
`RepositoryScope` for the seat-lifecycle fixtures, matching the runtime-config shape that
carries `certification_profile`.

## Code Commentary

L23 moves auto-land/auto-close proof to `integration_completion_payload`, establishing that detached integration completion—not the initiating MCP call—owns seat cleanup.

### Current Structural Seat Regressions

The suite builds a real sprint/master/leaf JSON task topology. Manager authority is confined to
pipeline roles beneath its own master; orchestrator authority covers the sprint; no seat may retire
itself. Failed-dispatch cleanup uses `replacement_for_task_document_ref`, and land/cleanup tests
match canonical task document plus role rather than a leaf string.

### Logic

`_write_task_topology` creates the sprint and two master trees used by structural authority.
`_config` installs that topology in an isolated coordination root. `_entry(session_id, *,
task_document_ref, spawn_role)` builds one running harness row; rarer shapes use `replace(...)` on
the frozen catalog entry. `_post_report` creates a durable turn-report whose role is statically
typed as `AgentRole`, keeping worker/reviewer/curator fixtures inside the owned wire vocabulary.
`_FakeHost` records termination without requiring tmux.

Test classes, in file order:

- **`RetirePolicyMatrixTests`** — pure `check_retire_authority` coverage over
  `TaskDocumentTopology`: manager may retire leaf execution seats and its same-master reviewer but
  not another master or a manager; an architect may retire only its architect-stamped same-sprint
  plan reviewer, not the orchestrator-stamped super reviewer; orchestrator may retire sprint
  descendants; self-retire and unprivileged retire both fail closed.
- **`SessionRetireToolTests`** — the internal exact-session administrative payload against a real
  catalog: unknown actor/target refusals, structural manager/orchestrator authority, failed-dispatch
  replacement-task cleanup, self-retire refusal, and idempotent retirement provenance.
- **`SessionRenameToolTests`** — rename refuses unknown/retired sessions, freezes the original
  spawned label on first rename, preserves it on later renames, and never changes the seat role.
- **`TurnStateClassificationTests`** — scripted pane diagnostics cover busy, input, legacy and
  modern Codex composer, stale, draft, history, and precedence shapes without elevating pane text
  into lifecycle authority.
- **`TurnStateSweepWiringTests`** — liveness keeps pane-derived state diagnostic-only for hosted
  harnesses and never classifies plain terminal rows.
- **`TerminalMarkVsLivenessInterplayTests`** — later liveness cannot resurrect retired rows, and
  idempotent retirement does not fabricate provenance for a previously terminated row.
- **`LandSeatsForTaskTests`** — `land_seats_for_task` lands only the requested task-document/role
  pairs, preserves manager and other-task occupants, records the closure, and skips terminated
  rows.
- **`AutoLandHookIntegrationTests`** — integrate/finalize closes reported leaf-role occupants by
  default, preserves transcript evidence, defers missing or wrong-task reports, never closes the
  manager, and restores task-scoped landing when auto-close is disabled. Edge-gate-off and dry-run
  paths perform neither close nor landing.
- **`RetirementSettingsConfigTests`** — landing gates and completed-seat auto-close all default on.

### Conventions

Plain `unittest.TestCase` classes (not pytest fixtures), matching the repo's dominant test style.
Each stateful test class uses a `tempfile.TemporaryDirectory()` per test in `setUp`/`tearDown`
rather than a shared fixture, so catalog file state never leaks between tests. Role matrices that
feed inbox models use the producer-owned `AgentRole` alias instead of widening to `str`.

### Invariants And Boundaries

- Structural authority is derived from real task documents, never path-segment parsing or spawn
  ancestry.
- Completion cleanup requires the exact task-document/role turn report and preserves evidence.
- Auto-close opt-out restores landing; disabled edge gates and dry runs do neither.
- Pane state remains diagnostic and cannot resurrect terminal lifecycle state.
- Exact-session retire/rename payloads exercised here are internal administration seams, not
  agent-facing routing contracts.

### Todos

No known follow-up in this file.

## Docs References

No Domain Documentation source is configured, and this local regression suite has no external
standard dependency.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation governs this local test suite. | — | — |

## Repo-Internal References

This suite exercises the current task-topology, retirement, landing, liveness, terminal catalog,
completion-cleanup, and internal administrative payload seams.

| Finding | Anchor | Source |
| --- | --- | --- |
| The pure authority matrix uses real task topology. | `RetirePolicyMatrixTests` | mcp/tests/test_seat_lifecycle.py:200-264 |
| Task-scoped landing is exercised directly. | `LandSeatsForTaskTests` | mcp/tests/test_seat_lifecycle.py:674-719 |
| Turn-state classification and liveness wiring remain diagnostic. | `TurnStateClassificationTests`; `TurnStateSweepWiringTests` | mcp/tests/test_seat_lifecycle.py:464-554; mcp/tests/test_seat_lifecycle.py:557-622 |
| Completion cleanup uses `AgentRole`-typed task-owned reports. | `AutoLandHookIntegrationTests`; `_post_report` | mcp/tests/test_seat_lifecycle.py:722-954; mcp/tests/test_seat_lifecycle.py:769-799 |
| Internal retire/rename payloads are exercised end to end. | `SessionRetireToolTests`; `SessionRenameToolTests` | mcp/tests/test_seat_lifecycle.py:270-403; mcp/tests/test_seat_lifecycle.py:409-458 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is exercised by this local test suite. | — | — |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## L23 Lifecycle Model Package Review

The suite imports `IntegrateOperationInput` from `models.lifecycles.operation`, its dedicated
package owner. Structural-seat retirement, landing, and integration lifecycle assertions are
unchanged.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_manager_retires_own_worker`, `test_manager_retires_own_reviewer`, `test_manager_refused_against_other_masters_worker`, `test_manager_refused_against_a_manager_seat`. The L2 additions force locator-rooted journal access, legal task-addressed controls, write-ahead successors, exact worker termination, total expected-failure projection, and same-generation convergence.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current test source exercises `test_manager_retires_own_worker`, `test_manager_retires_own_reviewer`, `test_manager_refused_against_other_masters_worker`, `test_manager_refused_against_a_manager_seat`. | `RetirePolicyMatrixTests` | mcp/tests/test_seat_lifecycle.py:202-266 |

## Update History
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the repositories/RepositoryScope fixture shape in seat lifecycle tests.


- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: extended the retirement
  matrix to the manager's master reviewer and architect-only plan reviewer while explicitly
  refusing the same-address super reviewer. Verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-16T02:51+02:00 — No content impact: the integration hook fixture now supplies the
  configured contract-path resolver required by the strengthened application boundary; seat
  retirement, landing, and auto-close behavior are unchanged.

- 2026-08-13T09:05+02:00 — L23 curator: recorded the integration-input import move and confirmed the
  seat-lifecycle regression contract is unchanged; final provenance remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T20:28+02:00 — 260731-EFA-L19 closeout-gate repair: replaced the stale leaf-key
  default body with the current task-topology retirement/landing/auto-close contract, corrected the
  governing overview, and recorded the `AgentRole`-typed turn-report fixture. Verification metadata
  remains pinned until governed closeout.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_seat_lifecycle.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: corrected the shared-fixture and injection-seam
  descriptions, which the leaf made false. `_entry` lost three parameters — its documented
  signature `(session_id, *, leaf_key, spawn_role, status, kind)` is now
  `(session_id, *, leaf_key, spawn_role)` and it always mints a `running` `harness` row; the
  terminated row, the plain-terminal row and the unbound `replacement_for_leaf` row are now
  `dataclasses.replace(...)` on the frozen entry, so the "sane defaults" wording was describing
  defaults that no longer exist as parameters. `TurnStateSweepWiringTests` now injects the
  capturer through `probe=LivenessProbe(hysteresis=TerminalCatalogLivenessConfig(),
  pane_capturer=…)` rather than the two loose keywords, and `land_seats_for_leaf` takes a
  positional `SeatClosure(reason, edge, at)` ahead of `leaf_key`/`roles`; both bullets were
  rewritten to match. The whole-module citation in Docs References moved from L1-L743 to L1-L832.
  No test class or method was added, removed or renamed and no assertion changed, so the coverage
  claims themselves are unaffected.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: converted retirement tests to pair identity and added
  unbound failed-dispatch manager cleanup coverage.

- 2026-07-09T13:36+02:00 — 260707-HFX2-L11 round 2: removed the direct
  `retire_seats_for_leaf` tests with the deleted helper, documented the current `LandSeatsForLeafTests`
  and `AutoLandHookIntegrationTests`, and kept manual retire/authority coverage unchanged.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat lifecycle: retirement + live chat
  identity, status, turn-state): the consolidated failing-first + regression suite (45 tests / 5
  subtests per the builder report) covering the retire authority matrix, `session_retire`/
  `session_rename` MCP tools, turn-state classification + L5-sweep wiring, terminal-mark vs.
  liveness interplay, and the integrate/finalize auto-retire automation hooks incl. the R2/F1
  exception-guard-widening regression tests. Verification metadata pinned until closeout stamps the
  HFX-L8 commit.
