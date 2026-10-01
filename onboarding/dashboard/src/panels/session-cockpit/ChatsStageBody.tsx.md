# dashboard/src/panels/session-cockpit/ChatsStageBody.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## 260731-EFA-L8 Change

The e2e repair fixed a genuine keep-alive defect: a transient `focused ===
undefined` during smart-focus handoff unmounted the PTY layer. The layer now stays
mounted through the handoff and the empty backdrop renders inline; the stage layers
and styles moved to `stageLayers.tsx` / `chatsStageStyles.ts`.

## Purpose

The one **Chats stage body** (260718-CHATS-L4, design §4.1/§12.1): the thin composition seam that
replaced the unconditional controlled-session `PtySurface` body. For a controlled session it defaults
to the structured `ConversationSurface`; it also selects the in-stage history library and the
legacy-raw terminal, and it owns the default-off terminal-diagnostics drawer. It copies NO panel's
state — the composer, interaction bar, queue, header, and status line remain their own authorities and
are rendered by `SessionsView` AROUND this body. For a controlled session the PTY is only a read-only
diagnostic; a legacy-raw session keeps its interactive PTY as the primary body, honestly labeled.

## Code Commentary

### Logic

- **Archetype switch** (L66, L104-L116): `isControlledSession(focused)` (lifecycleCopy) decides. An
  undefined focus renders nothing; a non-controlled (legacy-raw) session renders the interactive
  `PtySurface` as the primary body under the honest label `legacy terminal · structured conversation
  unavailable` (`data-mode="legacy-raw"`, §4.3).
- **Epoch resolution + connect lifecycle** (`EPOCH_RESOLVE_WINDOW_MS`, line 123): `connect` reads the
  bridge epoch from `readSubmissionAuthority` — the LANDED L5 submission authority is REUSED for the
  epoch, not re-discovered, so no second submission/epoch authority is created — then calls
  `connectConversation(sessionId, descriptor.bridgeEpoch)` (the data-layer store orchestration). A
  `useEffect` connects on focus/controlled change and `disconnectConversation`s on cleanup;
  `generationRef` guards against a stale async resolve landing on a newer focus.
- **One bounded auto-retry** (L83-L92, F20): a just-launched chat routinely loses the epoch resolve to
  session startup (`submission-authority` 503), so the first failure schedules ONE 800 ms retry before
  escalating `epochState` to `failed`; fail-loud is preserved — a second failure still renders the
  visible projection-failed banner (`ConversationReconnect phase="projection-failed"`).
- **Harness identity for an eve session** (`harnessOf`, line 87): the guard narrowed
  `session.harness` to `"codex" | "claude" | "pi"` and returned `null` for anything else, so an eve
  session resolved to no harness even though the cockpit was already rendering it; it now accepts
  `"eve"` alongside the other three. This is the dashboard-side counterpart of `HarnessId` gaining
  `eve`, and it is the *whole* dashboard change the eve product-integration leaf needed — no
  eve-specific component, panel or shell was added.
- **Library overlay + diagnostics mutual exclusion** (L34, L55, L525): when the library is open
  (`showLibrary`, controlled harness only) the active surface stays mounted but goes inert behind it
  (`display:none`), and the `TerminalDiagnosticsDrawer` is NOT rendered at all — so the library and the
  drawer can never overlay/z-fight (F8). A successful open closes the library and focuses the new
  session through `onSessionOpened`.

### Invariants And Boundaries

- The structured surface is the controlled-session DEFAULT; the PTY is a read-only diagnostic drawer
  (default-off) for controlled sessions and only the primary body for legacy-raw.
- This body owns composition only. It never holds composer/queue/interaction/header/status authority —
  those are `SessionsView`'s children, unchanged by L4.
- The epoch comes from the reused submission authority, never a new discovery path.
- Fail-loud is preserved: at most one silent auto-retry, then the visible alarm banner; there is never
  a silent PTY fallback for a controlled projection failure.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Thin composition, epoch resolve, bounded auto-retry, library/diagnostics exclusion. [1]
- The reconstructable active-conversation store connect/disconnect orchestration. [2]
- The reused L5 submission authority the epoch comes from. [3]
- The default structured surface, the library surface, the reconnect banner, and the default-off drawer. [4]
- The controlled-session predicate and the legacy-raw PTY body. [5]
- The view that mounts this body and owns the surrounding authorities. [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## Current L5I Maintenance

Controlled chat surfaces now remain mounted per session in a pool bounded by the conversation LRU.
An unfocused surface is `visibility:hidden` and inert, never `display:none`, preserving its scroll
geometry and virtualizer measurements; evicted or terminated projections are removed rather than
resurrected. Warm projection reuse avoids needless epoch resolution, while cold boot resolution
retries only transient failures in a bounded 30-second window and otherwise fails loud. Hidden PTY
layers freeze their last visible box so composer chrome cannot provoke terminal refits.
