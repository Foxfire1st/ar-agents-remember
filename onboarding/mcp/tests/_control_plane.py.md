# mcp/tests/_control_plane.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_control_plane.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Shared service/route test topology for the 260718-CHATS-L3 control suites. One full running seam —
a structural fake adapter (interrupt- and asset-capable) behind a real `HarnessControlBridge` +
`HarnessControlServer` on a real user-private Unix socket, a real `TerminalCatalog` row, and the L0
`register_conversation_routes` composition — with the harness adapter as the only double. It is
support code, not a test module: the four service/route L3 suites import `ControlHarness` from it.

## Code Commentary

### Logic

`LiveHost` (L78) is the minimal terminal-host stand-in; `FakeControlAdapter` (L88) is the structural
interrupt/asset-capable adapter at the far edge (no PTY, no runner log, no fixture authority) that
plays codex/pi/claude native shapes — including `pi_emit_message_end`/`pi_release` and the composed
`pi_settle_with_content` helper that mirror `pi_rpc_events` message_end emission exactly (event kind
`transcript`, monotonic `TranscriptEntry`, the full frame under `AR_EVIDENCE_KEY`, completion
release). `ControlledEntry` (L400) is the catalog row wrapper. `ControlHarness` (L408) builds the
whole seam per test: bridge + IPC server on a real socket, the real submission authority (which owns
dispatch, provenance, withdrawal, the timeline, and the L2E recovery payload), `register_conversation_
routes`, and — the manager-authorized residual repair — a single `NOW`-anchored
`ConversationControlService(runtime, clock=lambda: NOW)` seeded into the production `_SERVICES`
weak-key memo so the registered routes resolve the same time-consistent instance (the 900 s lease
arithmetic is measured against the `NOW`-stamped records, not real wall-clock).

### Conventions

Only the harness adapter is doubled; everything from the bridge inward is the real production seam.
The `NOW`-anchored service is a legitimate fixture technique (the reviewer ruled it so): `clock` is a
public constructor parameter, the seeded object is the production class resolved through the
unmodified memo, and the memo is a `WeakKeyDictionary` keyed per-test so entries evict with their
runtime — no cross-test leakage.

### Invariants And Boundaries

- The only production substitution is the harness adapter at the far edge and the constructor-injected
  clock; nothing else is stubbed, subclassed, or bypassed.
- The `NOW`-anchored service keeps the records' stamp clock and the lease-expiry clock self-consistent;
  the genuine expiry test (in the queue suite) still advances its own separate frozen clock.
- `pi_settle_with_content` / `pi_emit_message_end` reproduce the production evidence emission so the
  real bridge clip path is the seam under test (including the 40 KB oversized-frame Finding 2 cases).

### Todos

None.

## Docs References

No Domain Documentation source is configured; the topology mirrors the production composition.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The topology composes the real bridge/IPC/authority and the L0 route registration; the seeded service
and its clock seam are the production control service.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The L0 `register_conversation_routes` composition the harness builds. | L1-L40 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The per-app control service and its public `clock` seam + `_SERVICES` memo the harness seeds. | L168-L280 | [control/service.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/service.py) |
| The pi mapper message_end emission shapes the fake adapter mirrors. | L131-L302 | [pi_rpc_events.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_events.py) |
| The real bridge + IPC server on a user-private socket. | L1-L120 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the shared L3 control
  test topology — the structural fake adapter, the real bridge/IPC/authority/L0 seam, and the
  `NOW`-anchored control service seeded into the `_SERVICES` memo (the accepted residual-repair
  fixture technique). Verification is blank because the new source file is uncommitted; closeout owns
  its first source stamp.
