# mcp/tests/_control_plane.py

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

cit:([`LiveHost`], mcp/tests/_control_plane.py:90-93) is the minimal terminal-host stand-in; cit:([`FakeControlAdapter`], mcp/tests/_control_plane.py:101-307) is the structural
interrupt/asset-capable adapter at the far edge (no PTY, no runner log, no fixture authority) that
plays codex/pi/claude native shapes — including `pi_emit_message_end`/`pi_release` and the composed
`pi_settle_with_content` helper that mirror `pi_rpc_events` message_end emission exactly (event kind
`transcript`, monotonic `TranscriptEntry`, the full frame under `AR_EVIDENCE_KEY`, completion
release). cit:([`ControlledEntry`], mcp/tests/_control_plane.py:292-297) is the catalog row wrapper. cit:([`ControlHarness`], mcp/tests/_control_plane.py:318-401) builds the
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

## Evidence

### Docs References

No Domain Documentation source is configured; the topology mirrors the production composition.

### Repo-Internal References

The topology composes the real bridge/IPC/authority and the L0 route registration; the seeded service
and its clock seam are the production control service.

- The L0 `register_conversation_routes` composition the harness builds. [1]
- The per-app control service and its public `clock` seam plus `_SERVICES` memo the harness seeds. [2]
- The pi mapper message_end emission shapes the fake adapter mirrors. [3]
- The real bridge on a user-private socket. [4]
- The IPC server on a user-private socket. [5]

### Cross-Repo References

No meaningful cross-repo references found.

## 260718-CHATS-L5I Current Delta

The shared control-plane test topology now supports structured interaction replies and native interrupt evidence over a real bridge/IPC path. It remains the common boundary fixture rather than a parallel implementation of production control behavior.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260824-PDLS Fixture-Authority Split

The harness still owns topology, mutable adapter state, and the real bridge/IPC/control seam. The
provider-frame replay scripts moved once to `_adapter_event_scripts.py`, where independent Codex,
Pi, and Claude terminal worlds are expressed through the narrow `AdapterReplayPort`. This removes
provider evidence construction from the structural harness without introducing a second adapter or
copying production mappers. Tests call those scripts through the existing fake adapter.

## 260824-PDLS Native-Refusal Boundary

The structural fake no longer reimplements Codex/Pi/Claude active-operation validation or its own
interrupt idempotence cache. `interrupt()` accepts exactly one native correlation, records the
call, and returns the edge acknowledgement; scenario tests inject explicit native
`HarnessControlError` outcomes where a rejection is required. Production services therefore own
precondition and replay semantics, while this fixture remains only the controllable adapter edge.
