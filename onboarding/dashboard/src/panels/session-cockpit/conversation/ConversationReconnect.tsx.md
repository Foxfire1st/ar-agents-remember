# dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The honest **reconnect/failure banner** (design §4.3/§14.5): a projector failure NEVER silently falls
back to raw PTY as if equivalent — it renders a fail-loud structured-surface error with `retry
projection` and `show terminal diagnostics` actions. Transient states keep current items visible and
say what is happening, never a fabricated calm.

## Code Commentary

### Logic

- **`copyFor(phase)`** cit:([`copyFor`], dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx:47-66): the per-`StreamPhase` copy/tone/action map. `connecting`/`reconnecting`/
  `gap` are calm/warn and keep items visible with no destructive action; `identity-changed`/
  `projection-failed`/`failed` are alarm-toned and expose `retry`/`diagnostics`. `live`/`idle` return
  `null` (no banner).
- **Typed reason** (L68-L101, F15): the optional `reason` (the server's typed `ConversationRouteError.detail`)
  is appended as `${copy.text} — ${reason}` so the banner shows the exact server reason (e.g.
  `cursor-reset-required — …`) instead of a generic string. The banner is `role="status"` and carries
  `data-phase` for tests.

### Invariants And Boundaries

- A projector failure is fail-loud — there is never a silent PTY fallback.
- Transient states (`reconnecting`/`gap`) keep current items visible and describe the state honestly.
- When the server supplies a typed reason it is shown; the generic copy is only the fallback.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The phase-to-copy/tone/action map and typed-reason append live in the component. | `copyFor`; `ConversationReconnect` | dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx:47-66; dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx:68-102 |
| The `StreamPhase` union this banner switches on. | `StreamPhase` | dashboard/src/data/conversation/types.ts:391-399 |
| The surface mounts this banner and supplies the typed route-error reason. | `ConversationSurface` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:269-341 |
| The stage body mounts this banner directly without a typed route-error reason. | `ChatsStageBody` | dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:147-489 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-04T12:19:51+02:00 — 260731-EFA-L6 S18-B01 curator: reconciled the bounded worker ledger; source-clear citations were repaired, split, rewritten, or deleted as applicable, then the exact scoped fixer/check passed.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the fail-loud
  reconnect/gap/projection-failed banner — the per-phase copy/tone/action map with retry +
  show-diagnostics and the typed server reason appended (F15), never a silent PTY fallback. Verification
  is pinned to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its
  first source stamp.
