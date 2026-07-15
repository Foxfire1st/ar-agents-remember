# mcp/src/agents_remember/serving/harness_control_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:19+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the vendor-neutral protocol-adapter boundary, the separate capability-discovery and progressive
capability ports, explicit adapter registration/unsupported behavior, and normalized event reduction
used by hosted control bridges.

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
| The bridge validates handshake identity/version/capabilities and routes both setters through its ordered queue. | L85-L104; L186-L192 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |

## Cross-Repo References

No external repository boundary is implemented by this protocol contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
