# mcp/src/agents_remember/serving/conversation/control/telemetry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/telemetry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R6: evidence-bound conversation telemetry. Every projected metric carries value/unit, origin, scope,
observed time, freshness, precision, runtime/helper versions, and fixture evidence. Metrics emit only
when their exact-session capability is `supported`/`partial` with matching observed versions; missing
native data is absent (never zero), and a version mismatch demotes the capability to `unverified` so
the metric stays absent rather than being presented as exact-session truth.

## Code Commentary

### Logic

`conversation_telemetry` (L40) resolves caller/epoch, reads the telemetry capability set, and emits
only capability-cleared metrics. The single currently-supported metric is codex cumulative token
usage: `_codex_usage` (L75) reads the latest `thread/tokenUsage/updated` frame in the bounded evidence
window and projects the cumulative breakdown with unit `tokens`, scope `conversation`, observed time
(frame `createdAt`), and precision `exact`; reasoning tokens have no model field and are omitted rather
than misfiled. `_freshness` (L123) classifies fresh/stale/unknown against the `_FRESH_WINDOW_MS`
15 s window (L37). `_telemetry_key` (L134) drives the semantic revision (stable on no-change,
bumps on new evidence/freshness transitions). `_int_or_none` (L143) keeps absent values absent.

### Conventions

Absence is the only truthful representation of unobserved native data. Everything else documented but
unobserved (cost, context used/limit, rateLimits, compaction; claude and pi metrics) stays visibly
unverified/unavailable in the capability view rather than being minted here.

### Invariants And Boundaries

- Missing data is absent, never zero; pre-frame usage is `null` on the wire.
- A metric emits only from a `supported`/`partial` capability whose observed runtime/helper versions
  match; a version mismatch demotes to `unverified` and the metric stays absent.
- The telemetry revision is semantic (stable on no-change reads).
- Codex is the only harness with a landed supported metric; claude (locked-gate mismatch) and pi
  (schema-documented, not fixture-observed) emit no metrics, with the reasons in the capability view.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the telemetry contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The metric DTOs and capability evidence live in the contract; the token-usage frame comes from the
L0E evidence window; the capability gate decides what may emit.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `ConversationTelemetry`/`MetricEvidence`/`UsageMetricValue` DTOs. | L406-L678 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The telemetry capability gate with observed-version demotion. | L317-L342 | [capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/capabilities.py) |
| The bounded evidence window the `thread/tokenUsage/updated` frame is read from. | L1-L120 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the evidence-bound
  telemetry projection — codex cumulative token usage from the latest tokenUsage frame with full
  provenance, absent-not-zero missing data, and version-mismatch demotion keeping unobserved metrics
  off the wire. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
