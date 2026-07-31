# mcp/src/agents_remember/serving/conversation/control/telemetry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/telemetry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |  2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

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

`conversation_telemetry` (L41-L73) resolves caller/epoch, reads the telemetry capability set, and emits
only capability-cleared metrics. The single currently-supported metric is codex cumulative token
usage: `_codex_usage` (L76-L121) reads the latest `thread/tokenUsage/updated` frame in the bounded evidence
window and projects the cumulative breakdown with unit `tokens`, scope `conversation`, observed time
(frame `createdAt`), and precision `exact`; reasoning tokens have no model field and are omitted rather
than misfiled. `_freshness` (L124-L132) classifies fresh/stale/unknown against the `_FRESH_WINDOW_MS`
15 s window (L38). `_telemetry_key` (L135-L141) drives the semantic revision (stable on no-change,
bumps on new evidence/freshness transitions). `_int_or_none` (L144-L145) keeps absent values absent.

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
| The `ConversationTelemetry`/`MetricEvidence`/`UsageMetricValue` DTOs. | L1185-L1242 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The telemetry capability gate — contract-verified, no version demotion (L5F R4). | L323-L347 | [capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/capabilities.py) |
| The bounded evidence window the `thread/tokenUsage/updated` frame is read from. | L1-L120 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T18:05+02:00 — 260731-EFA-L2 curator: re-derived 5 stale self-citations (plus the
  `_FRESH_WINDOW_MS` line riding the same sentence). Everything had slipped one or two lines and
  the single-line def citations were widened to the whole function each sentence describes:
  `conversation_telemetry` L40→L41-L73, `_codex_usage` L75→L76-L121, `_freshness` L123→L124-L132,
  `_FRESH_WINDOW_MS` L37→L38, `_telemetry_key` L134→L135-L141, `_int_or_none` L143→L144-L145. No
  claim text changed; every range was read back.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The metric
  DTO block moved to the tail of `models.py`: `T = TypeVar("T")`, `MetricScope`, the generic
  `MetricEvidence`, the five metric-value models and `ConversationTelemetry` now occupy
  L1185-L1242 (the old L406-L678 is the status/capability region). Verified by reading the block
  back; no claim text changed.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R4 version-gate removal — corrected the now-false
  "version mismatch demotes the capability" language. The contract is the only gate: a capability
  demotes only on failed or never-run contract verification, never on a version-string comparison;
  runtime/helper versions are informational metric evidence only. Reworded claude's reason from
  "locked-gate mismatch" to the never-probed contract reason. Change uncommitted; closeout re-stamps
  verification.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the evidence-bound
  telemetry projection — codex cumulative token usage from the latest tokenUsage frame with full
  provenance, absent-not-zero missing data, and version-mismatch demotion keeping unobserved metrics
  off the wire. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
