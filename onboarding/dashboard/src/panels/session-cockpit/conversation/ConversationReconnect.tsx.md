# dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The phase-to-copy/tone/action map and typed-reason append live in the component. [1]
- The `StreamPhase` union this banner switches on. [2]
- The surface mounts this banner and supplies the typed route-error reason. [3]
- The stage body mounts this banner directly without a typed route-error reason. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
