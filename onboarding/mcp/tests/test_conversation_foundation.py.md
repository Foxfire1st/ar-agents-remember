# mcp/tests/test_conversation_foundation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_foundation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins the cross-route foundation of structured Chats: exact two-port shape, three owned child routers
(the active child carrying exactly its three routes, the library child exactly its five L2
routes, and — since 260718-CHATS-L3 — the control child carrying exactly its seventeen owned routes),
one global registration seam, repository-owned helper dependency resolution with the exact helper
source set, and allow-listed installed-runtime fixtures that cannot enable capabilities.

## Code Commentary

### Logic

The suite introspects exported port types and router objects, reads the global serving source to
prove one registration call — since 260718-CHATS-L0 pinning the exact
`register_conversation_routes(app, runtime)` call that carries the immutable runtime
through the same single seam — parses the helper manifest/lock to prove exact pins, scans production
helper TypeScript for forbidden ambient resolution, validates all three runtime fixtures through
the production Pydantic contract, and rejects raw secret/path/conversation material by pattern.
Since 260718-CHATS-L1 the child-router assertion
(`test_root_composes_three_owned_child_routers`) pins the active production routes: GET page, POST
agent-history hydration, and GET events; since 260718-CHATS-L2 it pins the library child's exact five-route surface;
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
- Child ownership stays disjoint at this gate: the active child carries exactly its three routes,
  the library child exactly its five L2 routes, the control child exactly its seventeen L3
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Root conversation composition defines the exact child tuple and single registration function. | `register_conversation_routes` | mcp/src/agents_remember/serving/conversation/router.py:22-32 |
| The active child's three owned routes pinned by the child-router assertion: page GET, agent-history POST, and events GET. | `conversation_page`; `hydrate_agent_history`; `conversation_events` | mcp/src/agents_remember/serving/conversation/active/api.py:126-155; mcp/src/agents_remember/serving/conversation/active/api.py:160-198; mcp/src/agents_remember/serving/conversation/active/api.py:204-247 |
| The library child owns exactly the five L2 routes this suite pins by method and path. | `api_library_list`; `api_library_read`; `api_library_open`; `api_library_open_status`; `api_library_open_reconcile` | mcp/src/agents_remember/serving/conversation/library/api.py:109-130; mcp/src/agents_remember/serving/conversation/library/api.py:133-158; mcp/src/agents_remember/serving/conversation/library/api.py:169-199; mcp/src/agents_remember/serving/conversation/library/api.py:202-221; mcp/src/agents_remember/serving/conversation/library/api.py:224-243 |
| The foundation suite's exact-set assertion pins all seventeen control-child L3 routes by method and path. | `test_root_composes_three_owned_child_routers` | mcp/tests/test_conversation_foundation.py:32-107 |
| The helper manifest declares the repository-owned helper package identity. | "@agents-remember/conversation-library-helper" | mcp/native_helpers/conversation_library/package.json:2-2 |
| The foundation test checks the helper's exact direct dependencies against the lockfile. | `test_helper_package_and_lock_select_only_the_exact_repository_dependencies` | mcp/tests/test_conversation_foundation.py:125-136 |
| Runtime fixture DTOs force allowlist-v1 and `enablesCapabilities=false`. | `allowlist-v1`; `enables_capabilities` | mcp/src/agents_remember/models/conversations/telemetry.py:96-96 |

## Cross-Repo References

No neighboring repository participates in this topology suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260727-CHATS-IM-L2 Active Route-Ownership Delta

The topology pin now asserts three active child routes: page GET, events GET, and the exact
`/agents/{agent_id}/history` POST (cit:([`conversation_page`, `conversation_events`, `hydrate_agent_history`], mcp/src/agents_remember/serving/conversation/active/api.py:126-155; mcp/src/agents_remember/serving/conversation/active/api.py:160-198; mcp/src/agents_remember/serving/conversation/active/api.py:204-247)). Library and control ownership sets remain unchanged.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: regenerated the exact-seventeen route assertion binding with the locked scoped fixer and inspected the complete focused test extent; no approved semantic claim changes.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: bound the exact-seventeen claim to the focused method/path set assertion and returned that source-local test binding to provisional fixer input.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: updated active-route ownership to the current three-route surface and separated helper identity from the exact dependency/lock assertion, using the source test's exact name in the provisional binding.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. `control/api.py` is 686 lines; the seventeen `@router` decorators run from `/conversation/interrupt` at L131 to `/conversation/telemetry` at L612 (handler ends L631), with the prefixed `APIRouter` declared at L58-L61 — counted all seventeen decorators, so the "exactly seventeen" claim still holds. Citation moved from L57-L570 to L58-L61; L131-L631.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the registration-seam pin now asserts
  `register_conversation_routes(app, runtime)` — the composition parameter rename that came with
  the runtime-object seam — so the Logic paragraph's quoted call string was rewritten from the
  old `register_conversation_routes(app, conversation_runtime)` spelling. The count-of-one
  claim, the no-seam-in-`app.py` claim, and the route-ownership, helper-manifest, and
  fixture-redaction claims are untouched, and the single-line replacement left every cited line
  number in place.

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
