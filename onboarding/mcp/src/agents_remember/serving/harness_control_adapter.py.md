# mcp/src/agents_remember/serving/harness_control_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T00:08+02:00 |
| lastVerifiedCommitHash | `22562e0f2161c2d980385a462275dc370deb72eb` |
| lastVerifiedCommitDate | 2026-07-20T00:45:01+02:00|
| governingOverview | `overview.md` |

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
`claude`, `codex`, and `pi`.

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
  acknowledgement without a second native write.

### Todos

None known for the normalized L3 adapter port.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Capability data and mutation evidence have a dedicated model module; bridge lifecycle remains a
separate consumer of the adapter protocol.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Normalized model/effort catalogs, ACP-style options, owned launch knobs, exact acceptance values, and set evidence are declared separately. | L13-L159 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |
| The hosted runner requires the combined launchable seam for preflight, discovery, validation, and runtime construction. | L152-L191 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |
| The bridge validates handshake identity/version/capabilities and routes both setters through its ordered queue. | L146-L171; L422-L428 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The bridge's interrupt dispatch detects `InterruptCapableAdapter` structurally, refuses unsupported harnesses typed naming the adapter, and rejects an adapter-minted epoch. | L268-L295 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The authority routes asset-carrying submissions to `submit_with_assets` and fails non-capable adapters closed with an unsupported receipt. | L210-L217; L694-L712 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| Codex and Pi implement both sub-protocols: exact-active-turn/expected-operation interrupt writes with replay-once, and verified asset construction. | L291-L357 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py); [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) L393-L477 |

## Cross-Repo References

No external repository boundary is implemented by this protocol contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Adapter methods now accept full operation refs and a final guarded-write claim. Preflight is async
and advisory; the authority lock-linearizes the subsequent claim before any native byte. The base
unsupported implementation and reducer callback preserve exact refs so adapters cannot release work
by FIFO or request id alone.

## Update History

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the two runtime-checkable
  structural sub-protocols — `InterruptCapableAdapter.interrupt` (identity guards ride the write;
  replay-once per (expected, active) pair) and `AssetSubmitCapable.submit_with_assets` — with the
  base protocol byte-compatible and structural capability detection failing unsupported harnesses
  closed typed. Verification metadata stays pinned to the last committed source until closeout
  stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented op-aware setter/prompt ports, async preflight, final
  guarded claim, and exact completion refs.

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented setters on the live protocol seam,
  explicit unsupported-adapter results, and queue-routed mutation ownership.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented the combined launchable adapter
  protocol and explicit unsupported launch-knob refusal used by the hosted runner.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented cached advertise, transient
  discovery, and the progressive launch/set capability port while preserving the explicit
  unsupported and hosted-bridge boundaries.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the explicit
  adapter protocol, registry, unsupported path, handshake gate, and event reduction rules.
