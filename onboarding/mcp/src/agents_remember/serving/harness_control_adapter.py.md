# mcp/src/agents_remember/serving/harness_control_adapter.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the vendor-neutral protocol-adapter boundary, the separate capability-discovery and progressive
capability ports, explicit adapter registration/unsupported behavior, and normalized event reduction
used by hosted control bridges. 260718-CHATS-L2E adds two runtime-checkable structural sub-protocols
— `InterruptCapableAdapter` (the native interrupt write) and `AssetSubmitCapable` (asset-carrying
submit) — so adapters opt into the new seams without any base-contract member.

## Code Commentary

### Logic

`HarnessProtocolAdapter` includes cached `advertise` and async `set_model`/`set_effort` beside
start, snapshot, subscription, correlated submit/respond/reconcile, and shutdown.
`HarnessCapabilityDiscoverer` separates transient token-free enumeration from a running session;
`HarnessCapabilityPort` groups advertise, native launch knobs, and honest setters.
`LaunchableHarnessProtocolAdapter` combines all seams required by the hosted runner. The registry
returns a concrete unsupported adapter when no factory exists; that adapter returns explicit
`unsupported` setter results instead of fabricating a built-in path. The reducer still enforces
identity plus monotonic event sequence while preserving additive raw event detail.

The two L2E sub-protocols are `runtime_checkable` structural ports: `InterruptCapableAdapter.interrupt(*,
turn_id, expected_operation_id)` carries the caller's identity guards with the write — `turn_id` is
the codex native active-turn identity, `expected_operation_id` the AR active-operation identity a
turn-less harness (Pi) must match before any native bytes — and a repeat naming the same
(expected, active) pair replays the first acknowledgement with no second write.
`AssetSubmitCapable.submit_with_assets(request)` is dispatched by the authority only when assets
ride. The base `HarnessProtocolAdapter` stays byte-compatible: neither sub-protocol adds a member
to it, and the bridge/authority detect capability structurally (`isinstance`) so unsupported
harnesses fail closed typed naming the adapter.

### Conventions

Running advertise is synchronous because it reads a catalog retained during native startup; cold
discovery is asynchronous because it owns a transient protocol process. Built-in ids are exactly
`claude`, `codex`, `pi`, and `eve`.

### Invariants And Boundaries

- One hosted bridge owns one native adapter; no Toad host, ACP transport, pane parser, regex, or log
  timing fallback is introduced here.
- Unsupported adapters fail catalog reads loudly and report unsupported delivery without pretending
  capability support; setters preserve the request but never claim success/effect.
- A runner requiring native launch configuration must receive the combined launchable protocol;
  unsupported/custom adapters cannot accidentally inherit a built-in launch path.
- Capability/protocol/identity mismatches fail before state adoption.
- Possible-send disconnects remain ambiguous and never authorize automatic duplicate submission.
- Durable inbox acceptance and explicit consumption remain distinct from adapter delivery evidence.
- The L2E sub-protocols stay structural and additive: the base protocol gains no member, capability
  is detected by `isinstance`, and a harness without the seam fails closed typed naming the adapter
  rather than guessing an interrupt or asset path.
- Interrupt identity guards travel with the write (`turn_id` for codex, `expected_operation_id`
  for turn-less Pi); a repeat of the same (expected, active) pair replays the first
  acknowledgement without a second native write. eve implements the same structural port: its
  `interrupt` is turn-addressed, replayed once per `(observed turn, operation)` pair, and reports
  acceptance only because eve's cancel is cooperative and settles later on the stream.
- eve is registered here through `BUILTIN_PROTOCOL_HARNESSES` only. This set is the
  **protocol-adapter** registry, not the kernel's developer-curated terminal harness set, and the
  two are deliberately separate: eve's runtime is an AR-owned application rather than a `PATH`
  command, so it has no `kernel/harnesses.py` row yet. Until that row exists an `eve` harness id is
  reachable only through the protocol factory, never through terminal launch.

### Todos

None known for the normalized L3 adapter port.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

Capability data and mutation evidence have a dedicated model module; bridge lifecycle remains a
separate consumer of the adapter protocol.

- Normalized model/effort catalogs, ACP-style options, owned launch knobs, exact acceptance values, and set evidence are declared separately. [1]
- The hosted runner requires the combined launchable seam for preflight, discovery, validation, and runtime construction. [2]
- The bridge validates handshake identity/version/capabilities and routes both setters through its ordered queue. [3]
- The bridge's interrupt dispatch detects `InterruptCapableAdapter` structurally, refuses unsupported harnesses typed naming the adapter, and rejects an adapter-minted epoch. [4]
- The authority routes asset-carrying submissions to `submit_with_assets` and fails non-capable adapters closed with an unsupported receipt. [5]
- Codex and Pi implement both sub-protocols: exact-active-turn/expected-operation interrupt writes with replay-once, and verified asset construction. [6]

### Cross-Repo References

No external repository boundary is implemented by this protocol contract.

No meaningful cross-repo references found.

## 260715-FEUI-L5 Submission Authority Delta

Adapter methods now accept full operation refs and a final guarded-write claim. Preflight is async
and advisory; the authority lock-linearizes the subsequent claim before any native byte. The base
unsupported implementation and reducer callback preserve exact refs so adapters cannot release work
by FIFO or request id alone.
