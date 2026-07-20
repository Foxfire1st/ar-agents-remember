# dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
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

- **`copyFor(phase)`** (L47-L66): the per-`StreamPhase` copy/tone/action map. `connecting`/`reconnecting`/
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The phase→copy/tone/action map and the typed-reason append. | L47-L102 | [ConversationReconnect.tsx](ConversationReconnect.tsx) |
| The `StreamPhase` union this banner switches on. | — | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The surface + stage body that mount this banner and supply the typed reason. | — | [ConversationSurface.tsx](ConversationSurface.tsx) · [../ChatsStageBody.tsx](../ChatsStageBody.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the fail-loud
  reconnect/gap/projection-failed banner — the per-phase copy/tone/action map with retry +
  show-diagnostics and the typed server reason appended (F15), never a silent PTY fallback. Verification
  is pinned to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its
  first source stamp.
