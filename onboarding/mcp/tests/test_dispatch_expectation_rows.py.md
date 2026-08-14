# mcp/tests/test_dispatch_expectation_rows.py

| Field                  | Value                                                   |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/tests/test_dispatch_expectation_rows.py`             |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Regression suite for expectation-row creation and completion at spawn, gate, and inbox boundaries.

## Code Commentary

### Logic

Spawn alone starts no assignment clocks, including a task-document-bound worker and a bare command chat. Gate creation/decision owns `verdict-by`; inbox post/consume no longer creates or meets an acknowledgement clock.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the public or owning internal seam directly.

### Invariants And Boundaries

Assignment expectations begin only when work is structurally dispatched, not when an occupant is merely spawned or catalog-bound.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `SpawnExpectationRowTests` | mcp/tests/test_dispatch_expectation_rows.py:89-142 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## L23 Structural Fixture Admission

Expectation-row dispatch tests now seed a current task-derived master/leaf
lineage chain before spawning structural seats. Their subject remains durable
expectation-row semantics; the fixture prevents an unrelated fail-closed
lineage gate from masking those assertions.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented current-lineage fixture setup for expectation-row tests; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_dispatch_expectation_rows.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 3 citation claims; scoped recheck clean (0 findings).
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: rewrote the Logic paragraph and all three
  self-file citations to match the parameter-object call sites. `SpawnExpectationRowTests` no
  longer calls `spawn_agent_session_payload` directly — it imports and calls
  `test_spawn_agent_session.call_spawn`, a shim that packs flat keywords into the builder's four
  parameter objects — so the sidecar's "drives the real `spawn_agent_session_payload`" claim was
  literally false about the call site and is now stated as the shim over that same builder. Gate
  creation takes `anchor=GateAnchor(lifecycle_id=…)`, gate decision takes
  `verdict=GateVerdict(decision, by, via)`, and inbox posting takes
  `address=InboxAddress(...)`, `message=InboxMessage(...)`, `poster=InboxPoster(...)` and
  `delivery=HostedDelivery(enabled=False)`; all are recorded. The three Repo-Internal citations
  were re-derived from the current file and verified there: spawn L83-L113 → L85-L135, gate
  L121-L149 → L138-L169, inbox L157-L195 → L172-L206 (the old ranges had drifted enough that the
  "gate" range actually started inside a spawn test). No test was added, removed or renamed and
  every expectation-row assertion is unchanged, so the atomic-write-with-dispatch contract and
  both invariants stand.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented the complete native role fixture
  used to preserve expectation-row semantics and corrected the nearest governing overview link.
  Verification metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added seat-role assertions to dispatch expectation
  rows.

- 2026-07-09T12:04+02:00 — No content impact: 260707-HFX2-L10 adjusted the spawn expectation-row
  fixture to use settings-resolved harness selection instead of the now-refused legacy explicit
  `harness` argument. The expectation-row contract is unchanged: spawn still writes `briefed-by`
  and, when leaf-attached, `turn-report-by` inside the dispatch call. Verification metadata pinned
  until closeout stamps the 260707-HFX2-L10 commit.

- 2026-07-08T16:15+02:00 — Created for 260707-HFX2-L1 (curator delta round 2, closeout-preview
  gap): the R2 atomic write-with-dispatch regression across spawn/gate/inbox. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L1 commit.
