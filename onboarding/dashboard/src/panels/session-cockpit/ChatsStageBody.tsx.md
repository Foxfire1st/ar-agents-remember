# dashboard/src/panels/session-cockpit/ChatsStageBody.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatsStageBody.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

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
- **Epoch resolution + connect lifecycle** cit:([`EPOCH_RESOLVE_WINDOW_MS`], dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:123-123): `connect` reads the bridge epoch from
  `readSubmissionAuthority` — the LANDED L5 submission authority is REUSED for the epoch, not
  re-discovered, so no second submission/epoch authority is created — then calls
  `connectConversation(sessionId, descriptor.bridgeEpoch)` (the data-layer store orchestration). A
  `useEffect` connects on focus/controlled change and `disconnectConversation`s on cleanup;
  `generationRef` guards against a stale async resolve landing on a newer focus.
- **One bounded auto-retry** (L83-L92, F20): a just-launched chat routinely loses the epoch resolve to
  session startup (`submission-authority` 503), so the first failure schedules ONE 800 ms retry before
  escalating `epochState` to `failed`; fail-loud is preserved — a second failure still renders the
  visible projection-failed banner (`ConversationReconnect phase="projection-failed"`).
- **Library overlay + diagnostics mutual exclusion** cit:(["const ref = useRef<HTMLDivElement>(null);", "<div className={showLibrary ? hiddenBehind : pool} data-testid="], dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:34-34; dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:525-525; dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:55-55);""], dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:34-34; dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:525-525): when the library is open
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
| Thin composition, epoch resolve, bounded auto-retry, library/diagnostics exclusion. | `ChatsStageBody` | dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:147-489 |
| The reconstructable active-conversation store connect/disconnect orchestration. | `connectConversation`; `disconnectConversation` | dashboard/src/data/conversation/store.ts:637-682; dashboard/src/data/conversation/store.ts:684-700 |
| The reused L5 submission authority the epoch comes from. | `readSubmissionAuthority` | dashboard/src/data/submissionLifecycleClient.ts:332-343 |
| The default structured surface, the library surface, the reconnect banner, and the default-off drawer. | `ConversationSurface`; `ConversationLibrarySurface`; `copyFor`; `TerminalDiagnosticsDrawer` | dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx:82-146; dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx:47-66; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:269-341; dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:77-117 |
| The controlled-session predicate and the legacy-raw PTY body. | "legacy raw — the vendor TUI runs in this pane"; `PtySurface` | dashboard/src/panels/session-cockpit/PtySurface.tsx:136-336; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:122-122 |
| The view that mounts this body and owns the surrounding authorities. | `SessionsViewImpl` | dashboard/src/panels/session-cockpit/sessions-view/SessionsView.tsx:15-18 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Current L5I Maintenance

Controlled chat surfaces now remain mounted per session in a pool bounded by the conversation LRU.
An unfocused surface is `visibility:hidden` and inert, never `display:none`, preserving its scroll
geometry and virtualizer measurements; evicted or terminated projections are removed rather than
resurrected. Warm projection reuse avoids needless epoch resolution, while cold boot resolution
retries only transient failures in a bounded 30-second window and otherwise fails loud. Hidden PTY
layers freeze their last visible box so composer chrome cannot provoke terminal refits.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the keep-alive handoff fix and stageLayers/chatsStageStyles extraction. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:45+02:00 — W3-B01 curator: curated 11 Repo-Internal table source citations across 6 rows and 2 prose citations for the stage composition, conversation store, submission authority, surfaces, and view owner. Verification metadata remains unchanged for closeout.

- 2026-07-24T13:17:17Z — Curator: corrected warm/cold projection, bounded keep-alive, scroll-geometry,
  visible-PTY-box, and honest boot-retry invariants; verification fields remain pre-commit.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the one Chats stage body —
  the thin composition that defaults controlled sessions to the structured surface (PTY demoted to a
  default-off read-only diagnostic), reuses the L5 submission authority for the epoch, keeps the library
  and diagnostics from overlaying (F8), and preserves fail-loud with one bounded startup auto-retry
  (F20). Verification is pinned to the leaf base (`0be0099`) because the new source file is uncommitted;
  closeout owns its first source stamp.
