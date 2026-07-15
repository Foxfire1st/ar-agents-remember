# mcp/src/agents_remember/serving/harness_control_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the vendor-neutral protocol-adapter boundary, the separate capability-discovery and progressive
capability ports, explicit adapter registration/unsupported behavior, and normalized event reduction
used by hosted control bridges.

## Code Commentary

### Logic

`HarnessProtocolAdapter` now includes synchronous cached `advertise` beside start, snapshot,
subscription, correlated submit/respond/reconcile, and shutdown. `HarnessCapabilityDiscoverer`
separates transient token-free enumeration from a running session. `HarnessCapabilityPort` declares
the L1/L2/L3 progression: advertise, native launch knobs, and honest model/effort setters. The
registry returns a concrete unsupported adapter when no factory exists, and the reducer enforces
identity plus monotonic event sequence while preserving additive raw event detail.

### Conventions

Running advertise is synchronous because it reads a catalog retained during native startup; cold
discovery is asynchronous because it owns a transient protocol process. Built-in ids are exactly
`claude`, `codex`, and `pi`.

### Invariants And Boundaries

- One hosted bridge owns one native adapter; no Toad host, ACP transport, pane parser, regex, or log
  timing fallback is introduced here.
- Unsupported adapters fail catalog reads loudly and report unsupported delivery without pretending
  capability support.
- Capability/protocol/identity mismatches fail before state adoption.
- Possible-send disconnects remain ambiguous and never authorize automatic duplicate submission.
- Durable inbox acceptance and explicit consumption remain distinct from adapter delivery evidence.

### Todos

Concrete L2 launch-knob and L3 mutation implementations remain intentionally outside this L1
foundation.

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
| Normalized model/effort catalogs, ACP-style options, launch knobs, and set evidence are declared separately. | L23-L150 | [harness_capabilities.py](harness_capabilities.py) |
| The bridge validates handshake identity/version/capabilities before adopting adapter state. | L85-L104; L200-L213 | [harness_control_bridge.py](harness_control_bridge.py) |

## Cross-Repo References

No external repository boundary is implemented by this protocol contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented cached advertise, transient
  discovery, and the progressive launch/set capability port while preserving the explicit
  unsupported and hosted-bridge boundaries.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the explicit
  adapter protocol, registry, unsupported path, handshake gate, and event reduction rules.
