# dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

Ambient **evidence-bound telemetry** (design §9.9/§12.2; round-1 F3): the landed L3 telemetry route
(codex cumulative token usage is a supported metric) rendered ambiently in the conversation toolbar —
NOT as noisy transcript rows. Every value is absent-not-zero (A2), carries its evidence
(origin/observed/runtime) in a tooltip, and a non-fresh metric degrades to a quiet marker (A4), never
an alarm. This is where the A-convention module (`joinChips`/`freshnessTone`/`humanizeAge`) becomes
product truth (F19), giving the previously-orphaned `fetchConversationTelemetry` a consumer.

## Code Commentary

### Logic

- **`formatTokens`** cit:([`formatTokens`], dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.tsx:25-30): humanizes token counts (`k`/`M`), returns `null` for absent/non-finite
  — the absent-not-zero primitive.
- **`usageChips`** cit:([`usageChips`], dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.tsx:53-61): builds `in/out/cached` token chips, a `ctx %` chip, and a `cost` chip ONLY
  for metrics the harness actually supplies, then `joinChips` (interpunct join, drops empties). A metric
  the harness does not supply produces no chip — never a reassurance `0` (A2).
- **Fetch effect** cit:([`AbortController`], dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.tsx:82-82): `fetchConversationTelemetry(sessionId, epoch, base)` refreshes when the
  turn/status advances (`statusRevision` in deps) — ambient, not per-token; cancellation-guarded.
- **Freshness marker** (L79-L101, A4): renders nothing until telemetry arrives and only if there is at
  least one chip; the primary metric's `freshnessTone` governs a quiet italic `stale` marker (never an
  alarm color); the evidence tooltip is `origin · observed <age> · runtime <version>`.

### Invariants And Boundaries

- Absent-not-zero: a metric the harness does not supply is omitted, never rendered as `0`.
- Telemetry is ambient (toolbar chips), never transcript rows.
- Non-fresh metrics degrade to a quiet marker, never an alarm.
- Evidence (origin/observed/runtime) rides the tooltip so the number is always attributable.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Absent-not-zero chips, ambient refresh, quiet-stale freshness. [1]
- The telemetry read client (previously orphaned, now consumed — F3). [2]
- The A-convention presentation module (`joinChips`/`freshnessTone`/`humanizeAge`). [3]
- The `ConversationTelemetry` wire type. [4]
- The toolbar host that mounts this component. [5]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
