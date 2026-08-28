# mcp/tests/_control_plane.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_control_plane.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
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

## Docs References

No Domain Documentation source is configured; the topology mirrors the production composition.

| Finding | Anchor | Source |
| --- | --- | --- |


## Repo-Internal References

The topology composes the real bridge/IPC/authority and the L0 route registration; the seeded service
and its clock seam are the production control service.

| Finding | Anchor | Source |
| --- | --- | --- |
| The L0 `register_conversation_routes` composition the harness builds. | `register_conversation_routes` | mcp/src/agents_remember/serving/conversation/router.py:22-32 |
| The per-app control service and its public `clock` seam plus `_SERVICES` memo the harness seeds. | `ConversationControlService`; `_SERVICES` | mcp/src/agents_remember/serving/conversation/control/service.py:224-362; mcp/src/agents_remember/serving/conversation/control/service.py:365-367 |
| The pi mapper message_end emission shapes the fake adapter mirrors. | `PiRpcEventMapper` | mcp/src/agents_remember/serving/pi_rpc_events.py:59-362 |
| The real bridge on a user-private socket. | `HarnessControlBridge` | mcp/src/agents_remember/serving/harness_control_bridge.py:81-547 |
| The IPC server on a user-private socket. | `HarnessControlServer` | mcp/src/agents_remember/serving/harness_control_ipc.py:103-416 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |


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

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: removed duplicated native precondition and
  idempotence behavior from the shared fake adapter; recorded the exact-one-correlation edge and
  explicit scenario-owned refusal injection.

- 2026-08-25T01:56+02:00 — 260824-PDLS moved provider-frame scripts to their single independent
  evidence owner while retaining topology/state in this harness; verification remains
  closeout-owned.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: removed duplicate service-source segments and generated final citation ranges with the scoped fixer.

- 2026-08-02T18:15+02:00 — 260731-EFA-L6 curator W1-B06: repaired 4 Repo-Internal reference rows, including 2 exact staged ranges, and normalized 1 duplicate range list; scoped result clean (0 findings).

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
