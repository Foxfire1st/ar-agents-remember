# Structured Conversation Contract Route Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/serving/conversation/` |
| onboardingRoute | `mcp/src/agents_remember/serving/conversation/overview.md` |
| parentOverview | [`serving/overview.md`](../overview.md) |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|

## What This Area Is

This route is the production-owned semantic boundary for native-authoritative structured Chats.
It defines one normalized wire grammar for current conversations, dormant native history,
capability evidence, status, telemetry, control-operation state, attachments, and authoritative
queued withdrawal recovery. It also fixes the two read ports and the three independently owned
FastAPI child-router seams that later production leaves implement.

This is deliberately a contract and composition route. It does not project vendor events, read a
native history store, implement control actions, persist a duplicate conversation database, or
render a UI.

## Hot Path Summary

Start with `models.py` for identity, cursor, status, capability, operation, attachment, and
withdrawal grammar; use `ports.py` to see the only two read boundaries. `router.py` composes the
behavior-empty `active`, `library`, and `control` routers and is mounted once through
`harness_control_api.register_harness_control_routes`.

## What Belongs Here

| Path | Role |
| --- | --- |
| `models.py` | Stable strict wire vocabulary and authority-product validation. |
| `ports.py` | Exactly two read protocols: active conversation and dormant native library. |
| `router.py` | One root composition seam for three disjoint child routers. |
| `active/` | Current exact-session route ownership shell. |
| `library/` | Dormant native list/read/resume route ownership shell. |
| `control/` | Structured control and operation-projection route ownership shell. |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Vendor protocol transport and native process lifecycle | Existing harness adapter modules under `mcp/src/agents_remember/serving/`. |
| Durable agent-to-agent/operator inbox authority | `mcp/src/agents_remember/controlplane/` and its existing serving adapters. |
| Browser conversation rendering and composer state | `dashboard/src/`. |
| Locked Claude/Pi native dependency process | `mcp/native_helpers/conversation_library/`. |

## Structures Found Here

- Strict immutable camel-case Pydantic wire models with unknown fields forbidden.
- Purpose-branded active-page, active-event, library-list, library-read, library-key, resume-target,
  and operation-fingerprint values.
- Stable native and active conversation identities, normalized content blocks, revisions, global
  ordinals, provenance, status, page/event, capability, telemetry, attachment, queue, and recovery
  DTOs.
- `ActiveConversationPort` and `ConversationLibraryPort`; lifecycle/control authority is explicitly
  not a third port.
- Three behavior-empty child routers with separate prefixes and one root registration function.

## Operating Model

1. Vendor-specific projectors or library resolvers observe native state and map it into the strict
   types in `models.py` without promoting unknown evidence.
2. Active readers use exact AR session plus bridge-epoch identity and active-only cursors.
3. Dormant history readers use authorization/project scope, library-only cursors and keys, and a
   server-private native resume target.
4. Capability support is fixture/evidence-bound and demotes on runtime/helper mismatch.
5. Control implementations publish revisioned operation products; contradictory phase/outcome,
   identity/rollback, acknowledgement/settlement, or recovery states fail validation.
6. The root router mounts active, library, and control ownership once; later leaves add endpoints
   only inside their assigned child module.

## Main Flows

### Current conversation read and stream

1. Identify the exact active native conversation through `ActiveConversationPort.identify`.
2. Page using an `ActivePageCursor`; stream using an `ActiveEventCursor`.
3. On an established-stream gap, emit the explicit gap mutation, require repage, and close rather
   than silently resetting.

### Dormant native history and exact resume

1. List within an authorization-bound canonical project scope.
2. Read history with a distinct library-read cursor and stable native identity.
3. Resolve a server-private native resume target; it is not a public authorization grant.

### Authoritative queued withdrawal recovery

1. Only a queued cockpit operation may expose a withdrawal reference and redacted preview.
2. Withdrawal races native dispatch through the owning authority in the later control service.
3. Exact draft text and attachment recovery appear only on a successful withdrawn response;
   pending-recovery projections remain raw-free.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `models.py` | contract/policy | Prevents identity, provenance, capability, status, and operation contradictions at the public boundary. | covered |
| `ports.py` | boundary | Keeps active and dormant history reads distinct and prevents control authority from becoming a read-store port. | covered |
| `router.py` | composition | Owns the single registration seam and isolates later leaf ownership. | covered |
| `active/api.py` | route shell | Reserves the exact current-conversation URL without implementing behavior early. | covered |
| `library/api.py` | route shell | Reserves the native library URL without claiming history support. | covered |
| `control/api.py` | route shell | Reserves exact-session control ownership without duplicating existing authority. | covered |

## Local Invariants And Traps

- Active and library cursor families are non-interchangeable and must remain bound to purpose,
  authorization, identity/scope, and generation.
- Unknown input and terminal-controlled input never masquerade as exact native evidence.
- `ready` cannot be derived from unknown evidence; waiting and terminal states retain matching
  evidence products.
- `supported`/`partial` capability claims require exact runtime-fixture evidence; fixture presence
  alone never enables a capability.
- Open/failure rollback products are bidirectional: no-launch outcomes carry no spawned identity,
  while identity-bearing failures require catalog proof and the phase-matching rollback state.
- Withdrawal raw recovery is a successful-response-only privacy boundary. Lists and failures stay
  raw-free.
- The child API modules are intentionally behavior-empty in this contract leaf. Do not treat their
  prefixes as implemented features.
- `models.py` is intentionally declaration-heavy. Add behavior in focused services rather than
  turning the contract module into a projector or store.

## Repo-Internal References

The contract is pinned by hostile product-matrix tests and by a topology suite that checks route,
port, helper, fixture, and registration boundaries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Cursor brands, identity bindings, strict wire configuration, and provenance authority are centralized in the contract module. | L25-L194; L315-L403 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Canonical status, capability evidence, open rollback, withdrawal recovery, and fixture non-promotion are fail-closed products. | L406-L678; L786-L889; L924-L1082; L1233-L1250 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Exactly two read ports separate active exact-session reads from dormant native library reads. | L27-L87 | [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py) |
| Three behavior-empty child routers compose through one stable root. | L7-L24 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The foundation suite verifies two-port topology, empty child ownership, one registration seam, exact helper pins, and fixture non-promotion. | L21-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No cross-repository implementation participates in this route. The resolved memory policy allows
no neighboring repository, and the native helper is part of this repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant cross-repo evidence found. | — | — |

## Docs References

The resolved `Domain Documentation` registry has no entries. This route therefore uses the
repository-owned contract, fixtures, and tests as its direct evidence and does not fabricate an
external citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this contract gate. | — | — |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `__init__.py` | [`__init__.py.md`](__init__.py.md) | covered | Public route-registration facade. |
| `models.py` | [`models.py.md`](models.py.md) | covered | Stable normalized grammar and authority guards. |
| `ports.py` | [`ports.py.md`](ports.py.md) | covered | Exact two-port read boundary. |
| `router.py` | [`router.py.md`](router.py.md) | covered | Root child-router composition. |
| `active/__init__.py` | [`active/__init__.py.md`](active/__init__.py.md) | covered | Active route package marker. |
| `active/api.py` | [`active/api.py.md`](active/api.py.md) | covered | Current-conversation ownership shell. |
| `library/__init__.py` | [`library/__init__.py.md`](library/__init__.py.md) | covered | Library route package marker. |
| `library/api.py` | [`library/api.py.md`](library/api.py.md) | covered | Native history ownership shell. |
| `control/__init__.py` | [`control/__init__.py.md`](control/__init__.py.md) | covered | Control route package marker. |
| `control/api.py` | [`control/api.py.md`](control/api.py.md) | covered | Structured control ownership shell. |

## Child Overviews

None. The three child directories are currently behavior-empty ownership shells, so separate
overviews would add routing burden without adding a coherent implemented subsystem.

## How To Use This Area

When changing this route, read this overview and the exact file sidecar first. Changes to public
models require the hostile contract matrix; changes to route/port shape require the foundation
topology suite. Do not infer production capability from fixture existence or an empty router.

## Needs Verification

- Production active projection, native library interoperability, exact resume, control settlement,
  attachments, telemetry, and browser rendering remain separately gated implementations.

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the governing overview for the stable
  structured-conversation grammar, exact two-port split, three behavior-empty route owners,
  evidence/cursor/operation authority, and withdrawal-recovery privacy boundary. Verification is
  blank because the new source route is uncommitted; closeout owns its first source stamp.
