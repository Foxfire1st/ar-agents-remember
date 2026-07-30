# mcp/tests/test_conversation_foundation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_foundation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins the cross-route foundation of structured Chats: exact two-port shape, three owned child routers
(the active child carrying exactly its two L1 GET routes, the library child exactly its five L2
routes, and — since 260718-CHATS-L3 — the control child carrying exactly its seventeen owned routes),
one global registration seam, repository-owned helper dependency resolution with the exact helper
source set, and allow-listed installed-runtime fixtures that cannot enable capabilities.

## Code Commentary

### Logic

The suite introspects exported port types and router objects, reads the global serving source to
prove one registration call — since 260718-CHATS-L0 pinning the exact
`register_conversation_routes(app, conversation_runtime)` call that carries the immutable runtime
through the same single seam — parses the helper manifest/lock to prove exact pins, scans production
helper TypeScript for forbidden ambient resolution, validates all three runtime fixtures through
the production Pydantic contract, and rejects raw secret/path/conversation material by pattern.
Since 260718-CHATS-L1 the child-router assertion
(`test_root_composes_three_owned_child_routers`) pins exactly the two owned active production routes
(GET page, GET events); since 260718-CHATS-L2 it pins the library child's exact five-route surface;
and since 260718-CHATS-L3 it pins the control child's exact **seventeen** owned routes by
method+path (interrupt/interrupt-status/interrupt-reconcile; GET operation-queue; withdraw/
withdraw-status/withdraw-reconcile; GET pending-withdrawal-recoveries; withdraw-recovery/
withdraw-recovery-ack; attachments/attachments-rebind; GET+POST attachments/{request_id} status+
reconcile; submit; GET policy; GET telemetry) — GET-only on policy/telemetry/queue/pending. The
control-router prefix `/api/terminal/{ar_session_id}` and the exact path set are asserted (L40, L54-
L82). The helper-source listing expects exactly `claude.ts`, `pi.ts`, `protocol.ts`, and
`protocol.test.ts`.

### Conventions

Source-level topology checks are intentional because this leaf establishes ownership and the exact
route surface as part of the contract. Filling the control shell with its seventeen routes is the
same class of legitimate assertion update L0/L1/L2 recorded for their call-shape/route-surface
changes. Runtime fixtures are parsed data, not snapshots copied into test expectations wholesale.

### Invariants And Boundaries

- Exactly two conversation read ports; no native control port (the control routes are a mutation/
  projection surface, not a third read port).
- Child ownership stays disjoint at this gate: the active child carries exactly its two L1 GET
  routes, the library child exactly its five L2 routes, the control child exactly its seventeen L3
  routes, and all three mount through one root seam.
- Helper dependencies resolve only from this repository package/lock, and production helper source
  contains no incidental module resolution.
- All runtime fixtures are allow-listed, redacted, and explicitly non-enabling.
- Claude helper history remains `not-exercised` until a real installed 2.1.211 history passes the
  replay gate; observed codex/pi rows record evidence shape only.

### Todos

The active/library/control children are now all owned and pinned (since 260718-CHATS-L1/L2/L3); later
leaves replace behavior-empty assertions only when they own and test new production endpoints.

## Docs References

No Domain Documentation source is configured. The repository sources and installed-runtime fixture
contract are direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Root conversation composition defines the exact child tuple and single registration function. | L7-L32 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The active child's two owned GET routes pinned by the child-router assertion. | L56-L59; L121-L160 | [api.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/api.py) |
| The library child owns exactly the five L2 routes this suite pins by method and path. | L93-L198 | [library/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/api.py) |
| The control child owns exactly the seventeen L3 routes this suite pins by method and path. | L57-L570 | [control/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/api.py) |
| The helper manifest owns the exact direct runtime dependencies checked against the lock. | L1-L22 | [package.json](agents-remember/mcp/native_helpers/conversation_library/package.json) |
| Runtime fixture DTOs force allowlist-v1 and `enablesCapabilities=false`. | L1233-L1250 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |

## Cross-Repo References

No neighboring repository participates in this topology suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260727-CHATS-IM-L2 Active Route-Ownership Delta

The topology pin now asserts three active child routes: page GET, events GET, and the exact
`/agents/{agent_id}/history` POST (L32-L57). Library and control ownership sets remain unchanged.

## Update History

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: updated the active child-router ownership
  pin from two routes to three with the selected-child history POST. Verification metadata remains
  pinned while uncommitted.

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: documented the child-router pin now asserting the
  control child's exact seventeen owned routes (GET-only on policy/telemetry/queue/pending) alongside
  the active two and library five — the same class of legitimate route-surface assertion update
  L0/L1/L2 recorded — and added the control/api.py reference row. Verification metadata stays pinned
  at the L1 code commit until L3 closeout stamps the candidate commit.
- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  sidecar with the L1 update after the master memory branch advanced — the child-router pin now
  documents both the active child's exact two L1 routes and the library child's exact five L2
  routes with control behavior-empty, the L2 helper-source-set listing, and both reference rows.
  Verification metadata stays pinned at the L2 code commit until L1 closeout stamps the L1
  candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: documented the renamed child-router pin
  (`test_root_composes_three_owned_child_routers`) asserting exactly the two owned active GET
  routes (page + events) — the same class of legitimate assertion update L0 recorded.
  Verification metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the renamed
  `test_root_composes_three_owned_child_routers` pin — the library child now asserts exactly its
  five owned routes while active/control stay behavior-empty — and the helper-source listing
  extended by `claude.ts`/`pi.ts`; the two-port, registration-seam, dependency-lock, and fixture
  redaction invariants are unchanged. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the updated registration-seam
  assertion pinning the exact `register_conversation_routes(app, conversation_runtime)` call after
  the L0 one-time binding; both other invariants (no `register_conversation_routes`, no
  `include_router` in `app.py`) are unchanged. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the structured-conversation foundation
  test sidecar. Verification is blank until closeout commits and stamps the new source.
