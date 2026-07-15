# mcp/src/agents_remember/serving/harness_control_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:19+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Implements the bridge's bounded ordered command runner, honest setter-result gate, and bounded
receipt/reconciliation ledger.

## Code Commentary

### Logic

Terminal and durable messages enter the same queue as whole commands. Submit, respond, reconcile,
resolve, model-set, effort-set, and stop commands are executed by one runner against the single
adapter. Setter results must preserve the requested value and use exactly the five normalized
acceptance tokens. `echo-verified` requires success plus an effective value; `immediate`/`queued`
require success without one; `unknown`/`unsupported` cannot claim success or effect. Accepted setter
results refresh and publish the same-identity adapter snapshot. A cancelled caller does not cancel
the already-running command or poison the queue: completion writes only to a still-open future.
Unexpected adapter errors fail the bridge and drain remaining commands explicitly.

### Conventions

One command object represents one semantic operation. Ordering is message/operation-level, never
keystroke-level. Result validation is runtime enforcement; static `Literal` typing alone is not
treated as authority.

### Invariants And Boundaries

- Queue order is message-level, never keystroke-level.
- Prompt, interaction, reconciliation, model-set, and effort-set operations share one order.
- Setter acceptance is fail-closed outside `echo-verified | immediate | queued | unknown |
  unsupported`, with no invented effective values.
- A receipt records acceptance, not completion; unknown remains unresolved until reconciliation.
- Ledger and command/subscriber paths are bounded by configured limits.

### Todos

None known for the L3 ordered mutation gate.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The normalized data module supplies the exact vocabulary; the bridge exposes the ordered methods.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The capability contract declares the five acceptance values and serialization rejects any other token. | L13-L24; L152-L159; L216-L227 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |
| The bridge exposes setters only while running and delegates both to this queue. | L174-L192 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |

## Cross-Repo References

No external repository boundary is implemented by the queue.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented shared setter ordering,
  fail-closed five-value validation, effective-value rules, accepted-set snapshot refresh, and
  cancellation-safe future completion.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for ordered command
  execution, stranded-await failure handling, and bounded unsupported receipt retention.
