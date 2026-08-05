# mcp/tests/test_dispatch_expectation_rows.py

| Field                  | Value                                                   |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/tests/test_dispatch_expectation_rows.py`             |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

R2 (260707-HFX2-L1) regression: proves every named dispatch surface — spawn, gate open, signal
post — writes its durable `ExpectationRowStore` row in the SAME call as the dispatch itself, and
that the matching fulfillment call marks that same row `met`, never leaving the write as a
forgettable follow-up step.

## Code Commentary

### 260714-ACPUI-L2 Complete Role Fixture

The spawn expectation-row fixture now writes a complete native Claude role selection
(`harness`, `model`, and `effort`) into the temporary settings authority. This keeps the test on the
real role-dispatch path after L2's structural preflight without changing its subject: spawning a
seat still starts no assignment clocks until a separate durable brief is dispatched.

### 260707-HFX2-L23 Seat-Scoped Dispatch Rows

Spawn expectation assertions now include the derived seat role, proving brief and turn-report
deadlines retain the same leaf-role subject as the spawned catalog row.

### Logic

`SpawnExpectationRowTests` drives the real `spawn_agent_session_payload` through
`test_spawn_agent_session`'s `call_spawn(config, **flat)` shim — the shim packs flat keywords into
the builder's `SpawnSeat`/`RetiredSpawnInputs`/`SpawnedBy`/`SpawnOverrides` parameter objects, so
these call sites keep reading as one spawn request — and reuses the same module's
`_FakeHost`/`_FakePaster` fakes. Against a leaf-attached spawn it asserts
`ExpectationRowStore(...).pending()` holds exactly a `briefed-by` and a `turn-report-by`
row, both stamped with the spawned session id as `sourceId`; a bare command chat with no
`leaf_key` gets only the `briefed-by` row (no leaf to report back into). `GateExpectationRowTests`
drives `gate_tools.gate_create_payload(kind=…, anchor=GateAnchor(lifecycle_id=…))` and asserts it
wrote a single `verdict-by` row keyed to the new gate's id, then drives
`gate_tools.gate_decide_payload(..., verdict=GateVerdict(decision, by, via))` on that gate and
asserts the matching row's `.current()` state flips to `met`. `InboxExpectationRowTests` mirrors
the same shape for the inbox: `operator_inbox_post_payload`, now addressed through
`InboxAddress`/`InboxMessage`/`InboxPoster` plus `delivery=HostedDelivery(enabled=False)`, writes
a single `ack-by` row keyed to the posted entry id, and `operator_inbox_consume_payload` flips it
to `met`. Every test reads the store directly (`ExpectationRowStore(observer_root(self.config))`)
rather than through the observer projection, matching R5's surfacing-only split (the store is the
correctness source, the projection is display-only).

### Conventions

Same `tempfile.mkdtemp()` + `McpRuntimeConfig` harness pattern as the other MCP tool payload-level
test modules; `SpawnExpectationRowTests` additionally seeds a real master/leaf task-document pair
via `write_task_doc` because `spawn_agent_session_payload`'s leaf-attach path resolves the leaf
through the task-document store, and resets the observer ambient singleton in `setUp`/`tearDown`
so tests do not leak lifecycle state across cases.

### Invariants And Boundaries

- These are payload-builder-level regressions, not unit tests of `expectation_rows.py` itself
  (see `test_expectation_rows.py` for the store/settings unit coverage) — they exist specifically
  to catch a dispatch surface that writes its row as a separate, droppable step instead of inside
  the same call.
- A bare command-chat spawn (no `leaf_key`) intentionally gets no `turn-report-by` row; asserting
  otherwise would be a false regression.

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf).

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Spawn writes `briefed-by` (+ `turn-report-by` when leaf-attached) atomically with the dispatch. | `SpawnExpectationRowTests` | mcp/tests/test_dispatch_expectation_rows.py:85-135 |
| Gate create writes a `verdict-by` row; gate decide meets it. | `GateExpectationRowTests` | mcp/tests/test_dispatch_expectation_rows.py:138-169 |
| Inbox post writes an `ack-by` row; consume meets it. | `InboxExpectationRowTests` | mcp/tests/test_dispatch_expectation_rows.py:172-207 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Update History

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
