# mcp/src/agents_remember/serving/conversation/control/telemetry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/telemetry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

## Docs References

No Domain Documentation source is configured; the telemetry contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The metric DTOs and capability evidence live in the contract; the token-usage frame comes from the
L0E evidence window; the capability gate decides what may emit.

| Finding | Anchor | Source |
| --- | --- | --- |
| `MetricEvidence` carries the evidence-bound metric provenance used by telemetry. | "class MetricEvidence(WireModel" | mcp/src/agents_remember/models/conversations/telemetry.py:30-30 |
| `ConversationTelemetry` is the wire envelope for the projected telemetry metrics. | "class ConversationTelemetry(WireModel):" | mcp/src/agents_remember/models/conversations/telemetry.py:72-72 |
| `telemetry_capabilities_for` is the telemetry capability-gate entry. | `telemetry_capabilities_for` | mcp/src/agents_remember/serving/conversation/control/capabilities.py:342-352 |
| The harness control bridge appends diverted evidence frames into the bounded evidence buffer. | `_append_evidence` | mcp/src/agents_remember/serving/harness_control_bridge.py:505-528 |
| The harness control bridge's event-consumption path diverts evidence into the bounded buffer. | `_run_events` | mcp/src/agents_remember/serving/harness_control_bridge.py:415-458 |
| The control client validates and reads evidence-window pages. | `read_control_evidence` | mcp/src/agents_remember/serving/harness_control_client.py:346-366 |
| Telemetry scans the resulting token-usage frames. | `_codex_usage` | mcp/src/agents_remember/serving/conversation/control/telemetry.py:76-121 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T19:26+02:00 — 260731-EFA-L16 curator: recorded that caller/epoch resolution now awaits
  the async, `asyncio.to_thread`-offloaded `service.resolve_entry` (same convention as the IPC
  reads), so this route's catalog read never parks the uvicorn event loop on the `TerminalCatalog`
  RLock — the loop-side seat of the 2026-08-05 ABBA deadlock. Verification metadata stays pinned
  until closeout stamps the L16 commit.
- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: applied reviewer verdict D1-D25 repairs and the pre-PASS whole-claim audit; narrowed the revision sentence to the generated revision extent while retaining the semantic-key body citation, then rechecked this card through the locked exact-document fixer/check.

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
