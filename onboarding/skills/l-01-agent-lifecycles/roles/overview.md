# skills/l-01-agent-lifecycles/roles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | skills/l-01-agent-lifecycles/roles |
| doc_type | route-local-overview |
| lastUpdated | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`|
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|

## Purpose

### 260713-TES-L1 Rename — Role Wording

The role files under this route were refreshed to agent-notifier wording (watcher-ban and
liveness-supervision prose now name the agent-notifier sweep); no role, seat, or dispatch
semantics changed.

Role-specific dispatch guidance shares the exact session-id handoff, ready proof, delivered-plus-harness-log-confirmed completion, launch-phase sessionCommands, and post-ready promptKeywords timing.

## Hot Path Summary

Role-specific dispatch guidance shares the exact session-id handoff, ready proof, delivered-plus-harness-log-confirmed completion, launch-phase sessionCommands, and post-ready promptKeywords timing.

### 260713-PHA-L5 Route Contract Review

Hosted role dispatch now relies on exact adapter readiness and correlated delivery evidence. The
durable inbox remains the message root, explicit recipient consume remains acknowledgement, and
pane/log classifiers are diagnostics-only. The packaged role briefs and source lifecycle guidance
must stay aligned with this contract.

### 260731-EFA-L6 Curator Self-Check Impact

`curator.md` now requires the curator to green its own change-set before reporting:
`route_index_refresh`, `memory_quality_check`, and `drift_check` are called with the leaf's
enclosure `contract_path`, and each response's `onboardingRoot` must be the memory worktree.
`templates/curator-brief.md` feeds the same contract-path doctrine to the dispatched curator.
The other role briefs are unchanged.

### 260731-EFA-L16 Route Impact — role seats only, and guidelines where code is written

The three prior role files now bind role-seat creation to `spawn_agent_session` explicitly and
remove native sub-agent fan-out from the orchestration seats (orchestrator, manager); the
architect keeps fan-out only for solo build under the worker discipline. The worker role (and
its brief) reads `system/coding-guidelines.md` before the first edit; the reviewer lens verifies
adherence independently; the architect's Opening Move reads `system/tools.md` as the repo's tool
inventory and its drawing-board phase now names `tasks/AGENTS.md` as the problem-decomposition
doctrine (reframe, assumptions/truth gaps/invariants, evidence plan, examples, derived plan);
the curator's checks paragraph names the citation-gate contract (findings clear by
making citations current, never attestations; the same `memory_quality_check` snaps at closeout
before the code commit and test wrapper). Worker, reviewer, and curator fan-out (read/search/
report) is unchanged.

## 260731-EFA-L17 Route Impact — Role Files State The Ladder

`worker.md` (Checks section) and `templates/worker-brief.md` now require the change-set-scoped
leaf check (`agents_remember.code_quality.check --targeted` with the leaf base) and state that
the full wrapper is NOT a leaf check; `manager.md` and `templates/manager-brief.md` name the
leaf targeted contract, the once-per-master full wrapper inside `worktree_integrate`
(memory-capped), and the per-leaf `memory_quality_check` carve-out; `orchestrator.md` owns the
master-gate full wrapper and forbids per-leaf full runs. `curator.md`'s contract-path-scoped
self-check (L6) is unchanged and is exactly what greens the per-leaf memory-quality gate.

## Update History

- 2026-08-08T21:20+02:00 — 260713-TES-L1 route impact: the role files under this route were
  refreshed to agent-notifier wording (no supervisor/agent-notifier role or seat change); route
  shape unchanged. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the ladder across the worker/
  manager/orchestrator role files and brief templates. Verification metadata stays pinned until
  closeout stamps the 260731-EFA-L17 commit.

- 2026-08-05T22:30+02:00 — 260731-EFA-L16 route impact: recorded the role-seat-only spawn doctrine across architect/orchestrator/manager, the worker/reviewer coding-guidelines reads, and the architect's `system/tools.md` inventory read; hands-on seats' fan-out unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-08-05T03:47+02:00 — 260731-EFA-L6 route impact: recorded the curator self-check contract
  (`contract_path`-scoped memory tools and `onboardingRoot` confirmation) landed in
  `roles/curator.md` and `templates/curator-brief.md`; other role documents are unchanged.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
