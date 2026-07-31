# mcp/tests/_control_plane.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_control_plane.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

`LiveHost` (L79-L82) is the minimal terminal-host stand-in; `FakeControlAdapter` (L89-L425) is the structural
interrupt/asset-capable adapter at the far edge (no PTY, no runner log, no fixture authority) that
plays codex/pi/claude native shapes — including `pi_emit_message_end`/`pi_release` and the composed
`pi_settle_with_content` helper that mirror `pi_rpc_events` message_end emission exactly (event kind
`transcript`, monotonic `TranscriptEntry`, the full frame under `AR_EVIDENCE_KEY`, completion
release). `ControlledEntry` (L428-L433) is the catalog row wrapper. `ControlHarness` (L436-L518) builds the
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
| The L0 `register_conversation_routes` composition the harness builds. | L15-L35 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The per-app control service and its public `clock` seam + `_SERVICES` memo the harness seeds. | L168-L280 | [control/service.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/service.py) |
| The pi mapper message_end emission shapes the fake adapter mirrors. | L131-L302 | [pi_rpc_events.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_events.py) |
| The real bridge + IPC server on a user-private socket. | L88-L144; L70-L117 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py); [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

The shared control-plane test topology now supports structured interaction replies and native interrupt evidence over a real bridge/IPC path. It remains the common boundary fixture rather than a parallel implementation of production control behavior.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived the 4 self-citations in Logic, which
  named single `class` lines and had all drifted. `LiveHost` L78 -> L79-L82, `FakeControlAdapter`
  L88 -> L89-L425 (the range now holds the `pi_emit_message_end`/`pi_release`/
  `pi_settle_with_content` helpers the sentence describes, at L338/L377/L388), `ControlledEntry`
  L398 -> L428-L433, `ControlHarness` L408 -> L436-L518 (which contains the `NOW`-anchored
  `ConversationControlService` + `_SERVICES` seeding at L495-L498 the same sentence claims). Every
  claim re-verified against the source and unchanged.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations. `router.py`
  is only 35 lines, so `L1-L40` overran it; the composition is now cited at L15-L35 — the
  `CONVERSATION_CHILD_ROUTERS` tuple, the root `APIRouter` that includes them, and
  `register_conversation_routes` itself. The bridge row's `L1-L120` covered imports and
  `BridgeLimits`; it now cites `HarnessControlBridge` + its constructor at
  `harness_control_bridge.py` L88-L144, and — because the row also names the IPC server, which
  never lived in that file — `harness_control_ipc.py` L70-L117, where `LocalControlEndpoint`
  derives the per-identity `.sock` path under a `0o700` parent and `HarnessControlServer.start`
  binds it and chmods it `0o600`. No claim text changed.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/_control_plane.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 7 line(s)
  with no token change whatsoever. Checked by parsing both revisions and comparing the abstract
  syntax trees (identical) and the comment tokens (identical), so no symbol, signature, default,
  decorator, control-flow branch, docstring, or assertion this card describes has moved, and every
  claim this card makes about its own source still holds. Noted while checking: the references
  table also cites line ranges inside `service.py`, `harness_control_bridge.py`,
  `pi_rpc_events.py`; those ranges shifted because this task edited those files, so treat the
  cited numbers as approximate and the linked cards as authoritative.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the shared L3 control
  test topology — the structural fake adapter, the real bridge/IPC/authority/L0 seam, and the
  `NOW`-anchored control service seeded into the `_SERVICES` memo (the accepted residual-repair
  fixture technique). Verification is blank because the new source file is uncommitted; closeout owns
  its first source stamp.
