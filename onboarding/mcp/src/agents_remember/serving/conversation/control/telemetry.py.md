# mcp/src/agents_remember/serving/conversation/control/telemetry.py

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R6: evidence-bound conversation telemetry. Every projected metric carries value/unit, origin, scope,
observed time, freshness, precision, runtime/helper versions, and fixture evidence. Metrics emit only
when their exact-session capability is `supported`/`partial`; missing native data is absent (never
zero). Since 260718-CHATS-L5F R4 the contract is the only gate: a capability demotes only when its
contract fails verification or was never probed — never on a runtime/helper version-string
comparison — and the runtime/helper versions ride the metric as informational evidence only.

## Code Commentary

### Logic

cit:([`conversation_telemetry`], mcp/src/agents_remember/serving/conversation/control/telemetry.py:41-73) resolves caller/epoch — since 260731-EFA-L16
awaiting the offloaded `service.resolve_entry` (`asyncio.to_thread`), so the catalog read never
runs on the event loop — reads the telemetry capability set, and emits
only capability-cleared metrics. The single currently-supported metric is codex cumulative token
usage: cit:([`_codex_usage`], mcp/src/agents_remember/serving/conversation/control/telemetry.py:76-121) reads the latest `thread/tokenUsage/updated` frame in the bounded evidence
window and projects the cumulative breakdown with unit `tokens`, scope `conversation`, observed time
(frame `createdAt`), and precision `exact`; reasoning tokens have no model field and are omitted rather
than misfiled. cit:([`_freshness`], mcp/src/agents_remember/serving/conversation/control/telemetry.py:124-132) classifies fresh/stale/unknown against the `_FRESH_WINDOW_MS`
15 s window. The telemetry implementation exposes the `revision` value here, cit:([`revision`], mcp/src/agents_remember/serving/conversation/control/telemetry.py:75-75), while `_telemetry_key` constructs the semantic key, cit:([`_telemetry_key`], mcp/src/agents_remember/serving/conversation/control/telemetry.py:135-141). cit:([`_int_or_none`], mcp/src/agents_remember/serving/conversation/control/telemetry.py:150-151) keeps absent values absent.

### Conventions

Absence is the only truthful representation of unobserved native data. Everything else documented but
unobserved (cost, context used/limit, rateLimits, compaction; claude and pi metrics) stays visibly
unverified/unavailable in the capability view rather than being minted here.

### Invariants And Boundaries

- Missing data is absent, never zero; pre-frame usage is `null` on the wire.
- A metric emits only from a `supported`/`partial` capability; the contract is the only gate, so a
  capability demotes on failed or never-run contract verification, never on a version-string
  comparison — the runtime/helper versions ride the metric as informational evidence only.
- The telemetry revision is semantic (stable on no-change reads).
- Codex is the only harness with a landed supported metric; claude (unverified for a never-probed
  contract reason, not a version reason since L5F R4) and pi (schema-documented, not fixture-observed)
  emit no metrics, with the reasons in the capability view.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; the telemetry contract is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The metric DTOs and capability evidence live in the contract; the token-usage frame comes from the
L0E evidence window; the capability gate decides what may emit.

- `MetricEvidence` carries the evidence-bound metric provenance used by telemetry. [1]
- `ConversationTelemetry` is the wire envelope for the projected telemetry metrics. [2]
- `telemetry_capabilities_for` is the telemetry capability-gate entry. [3]
- The harness control bridge appends diverted evidence frames into the bounded evidence buffer. [4]
- The harness control bridge's event-consumption path diverts evidence into the bounded buffer. [5]
- The control client validates and reads evidence-window pages. [6]
- Telemetry scans the resulting token-usage frames. [7]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
