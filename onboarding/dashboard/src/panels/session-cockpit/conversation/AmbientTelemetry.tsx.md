# dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

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

- **`formatTokens`** (L25-L30): humanizes token counts (`k`/`M`), returns `null` for absent/non-finite
  — the absent-not-zero primitive.
- **`usageChips`** (L32-L52): builds `in/out/cached` token chips, a `ctx %` chip, and a `cost` chip ONLY
  for metrics the harness actually supplies, then `joinChips` (interpunct join, drops empties). A metric
  the harness does not supply produces no chip — never a reassurance `0` (A2).
- **Fetch effect** (L68-L77): `fetchConversationTelemetry(sessionId, epoch, base)` refreshes when the
  turn/status advances (`statusRevision` in deps) — ambient, not per-token; cancellation-guarded.
- **Freshness marker** (L79-L101, A4): renders nothing until telemetry arrives and only if there is at
  least one chip; the primary metric's `freshnessTone` governs a quiet italic `stale` marker (never an
  alarm color); the evidence tooltip is `origin · observed <age> · runtime <version>`.

### Invariants And Boundaries

- Absent-not-zero: a metric the harness does not supply is omitted, never rendered as `0`.
- Telemetry is ambient (toolbar chips), never transcript rows.
- Non-fresh metrics degrade to a quiet marker, never an alarm.
- Evidence (origin/observed/runtime) rides the tooltip so the number is always attributable.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Absent-not-zero chips, ambient refresh, quiet-stale freshness. | L32-L103 | [AmbientTelemetry.tsx](AmbientTelemetry.tsx) |
| The telemetry read client (previously orphaned, now consumed — F3). | — | [../../../data/conversation/client.ts](../../../data/conversation/client.ts) |
| The A-convention presentation module (`joinChips`/`freshnessTone`/`humanizeAge`). | — | [../../../data/conversation/format.ts](../../../data/conversation/format.ts) |
| The `ConversationTelemetry` wire type. | — | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The toolbar host that mounts this component. | — | [ConversationSurface.tsx](ConversationSurface.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for ambient evidence-bound
  telemetry — absent-not-zero toolbar chips (A2) with a quiet-stale freshness marker (A4) and an
  evidence tooltip, wiring the previously-dead `fetchConversationTelemetry` (F3) and making the
  A-convention module product truth (F19). Verification is pinned to the leaf base (`0be0099`) because
  the new source file is uncommitted; closeout owns its first source stamp.
