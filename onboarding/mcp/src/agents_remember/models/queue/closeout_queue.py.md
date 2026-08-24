# mcp/src/agents_remember/models/queue/closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/queue/closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

Defines the strict public status/rebuild request and effective response for the disposable sprint
closeout projection.

## Code Commentary

### Logic

`CloseoutQueueRequest` permits only `status` or idempotent `rebuild` for one sprint and caller.
`CloseoutQueueResponse` reports revision, service condition, source classification/fingerprint,
bounded source problems, deterministic waiting-generation members, the first ready generation, and
next action. Projection members carry classification, priority, order, and reasons; no lifecycle or
commit state is modeled.

### Conventions

All nested models are extra-forbid and every public collection/text field is bounded. One effective
priority is projected from candidate override or master default; portfolio comparison remains an
orchestrator decision outside this model.

### Invariants And Boundaries

- Service condition is exactly invalid-empty or valid-built.
- Only waiting door generations may be members.
- No claim, grade mutation, blocker, receipt, commit, certification, integration, or lifecycle
  evidence is modeled.
- A response may be discarded without losing canonical work evidence.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The request permits only status and rebuild. | `CloseoutQueueRequest` | `mcp/src/agents_remember/models/queue/closeout_queue.py` |
| The response carries effective projection condition, source identity, problems, and members. | `CloseoutQueueResponse` | `mcp/src/agents_remember/models/queue/closeout_queue.py` |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## 260821-CLIVE Final Disposable Projection Model

The public request now supports only `status` and idempotent `rebuild`, addressed by sprint ref and
caller. The response reports service condition, revision, source classification/fingerprints,
bounded source problems, members, first ready generation, and next action. Candidate mutation,
grade declaration, claim, certification, blocker, receipt, commit, lifecycle, and integration
actions have been removed. A projection is only `invalid-empty` or `valid-built`; it is a current
scheduling view, never an operation ledger.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced the transitional mutable queue model with the final status/rebuild projection surface. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/models/queue/closeout_queue.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: `CloseoutQueueRequest` gains the optional `caller`
  (`DeclaredCaller`) honored only when no plane-injected seat exists; the exact action/payload
  matrix is unchanged. Verified at code commit a9d50e08.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: added `LANE_OCCUPYING_STATES` (the lane narrows to
  selected/closeout-in-flight/integration-in-flight; certified leaves the lane) and the response
  gained `mode`, `registers`, `laneOwner`, `legalNextOperations`, and `acquisitionFacts` for the
  degraded readout and blocker-acquisition fact reporting. Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: added `LeafPlacementFact` (strict `unplaced-leaf` /
  `unknown-leaf` wire model with derived-segment fields) and the `leafPlacementFacts` field on
  `CloseoutQueueResponse` — the projection had emitted the field without declaring it on the strict
  wire model. Verification remains closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added the `prepare-quality-repair` event to the closeout queue event vocabulary. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — Created for L3's strict closeout-queue wire and durable-state vocabulary; verification remains closeout-owned.
