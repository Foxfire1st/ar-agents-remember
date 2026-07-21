# dashboard/src/panels/session-cockpit/conversation-library/ — In-Stage History Browser Overview

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| repository             | agents-remember                                                     |
| sourceRoute            | `dashboard/src/panels/session-cockpit/conversation-library/`        |
| doc_type               | `route-local-overview`                                              |
| lastUpdated            | 2026-07-21T05:30+02:00                                              |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34`                         |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
| governingOverview      | `../overview.md`                                                    |

## Governing Overview

[session-cockpit overview](../overview.md) — this child owns the in-stage previous-conversation browser
while the session-cockpit overview owns the one-roof Chats composition. Its data authority is the
reconstructable [data/conversation-library](../../../data/conversation-library/overview.md) projection;
the sibling live renderer is [conversation/](../conversation/overview.md).

## Purpose

`session-cockpit/conversation-library/` is the **in-stage previous-conversation library** (260718-CHATS-L4,
design §4.4, §12.1). It renders each harness's normalized native history inside the same Chats stage,
previews a selected conversation READ-ONLY in the same block grammar, and owns the **sole exact-open
resume action**. Opening focuses a new live rail row ONLY on exact `opened` catalog proof; every other
outcome leaves the operator's current draft, focus, and scroll intact (R4). It holds only a
reconstructable projection of the library API — no durable browser index — and never marks a history row
active.

## Route Model

- `ConversationLibrarySurface.tsx` — the in-stage browser shell: heading focus on open, responsive
  columns, and the §4.4 return paths (Back button, Escape-in-stage → `onBack`, palette Back-to-current-chat)
  all consuming the same focus-return token. **Layout idiom (F23/L4.R5):** the `columns` flex container is
  `nowrap` (NOT wrap) with `min-height:0` columns each handing overflow to its own interior scroller, and
  `@container (max-width:56rem)` owns stacking with `container-type:inline-size` (F22). A wrapping flex
  container would size each line to content, defeat the `overflow:hidden` height clip, and leave the sole
  resume action and the paging affordance pointer-unreachable — the regression F23 fixed. **V10 threshold
  raise (260718-CHATS-L5P):** the stack breakpoint moved `640px → 56rem` — the 16rem list + 20rem preview
  crush below ~56rem of surface (the list falls to a ~180px sliver, preview prose splits mid-word), so the
  surface stacks to one column BEFORE that (the 900px window with the rail collapsed, and the ~1000px
  sweep). Sibling `MarkdownBlock` prose wraps whole-word (`break-word`) with inline code `nowrap` (V10),
  effective only under the app-root `word-break: normal` override (RV-1). The `nowrap`/container-query
  idiom itself is unchanged.
- `ConversationLibraryList.tsx` — the native list: boundary-truncated title carrying the full value in
  `title` (A5), humanized age (`humanizeAge`), a completeness badge, and `Load more` paging.
- `ConversationHistoryPreview.tsx` — the read-only preview in the SAME block grammar, labeled
  `history preview · not active`; its partial note prints the reason from the capability that is ACTUALLY
  unsupported (F13), never a supported-state reason.
- `OpenConversationAction.tsx` — the SOLE resume action: a caller-stable `requestId`; focus moves to a
  new rail row ONLY on `phase="opened" && outcome="opened"` catalog proof; every other outcome
  (`unsupported`/`stale-identity`/`timeout-unknown`/`launch-failed`/`identity-mismatch`/`request-conflict`)
  is surfaced without focusing. `dispatching` (set from dispatch) blocks a double-open (the L2.3 TOCTOU
  window); poll exhaustion switches to an honest "outcome unknown — reconcile" re-drive under the SAME
  requestId (F6).

## Invariants And Boundaries

- **Read-only history; focus only on exact opened proof (R4).** The preview carries no composer or
  controls; the library store never marks a row active; a successful open focuses the new session only
  after the catalog reports `opened`, and every other outcome leaves draft/focus/scroll intact.
- **One reconstructable projection, no durable index (R1).** The surface reads the
  `data/conversation-library` store; reload rebuilds from the list/read APIs. It invents no second
  history database.
- **One exact-open authority.** `OpenConversationAction` is the sole resume path; a lost response
  reconciles under the same `requestId` (invariant 27); a double-click cannot dispatch two opens.
- **In-stage, never overlapping the diagnostics drawer.** While the library overlay is up, `ChatsStageBody`
  does not render the diagnostics drawer, so the two surfaces can never overlay (F8); the live surface
  stays mounted but inert behind the library.
- **Height containment via single-line flex + container queries (L4.R5).** See the layout idiom above —
  wrapping flex is forbidden here; each column scrolls independently.

## Hot Path Summary

1. `ChatsStageBody` mounts `ConversationLibrarySurface` when the browse-history stage mode is on for a
   controlled harness session; the surface reads the `data/conversation-library` store.
2. `ConversationLibraryList` renders the native rows (truncated title + full value, humanized age,
   completeness); selecting one previews it read-only in the same grammar (`ConversationHistoryPreview`).
3. `OpenConversationAction` dispatches an exact open under a stable `requestId`; on `opened` catalog proof
   it hands the new `arSessionId` up to focus a live rail row; any other outcome is surfaced in place.
4. Back / Escape / palette-return restore focus through the shared focus-return token.

## Child Route Onboarding Map

No deeper child route exists below `conversation-library/`; each source has a one-to-one file card and
this overview is their governing pillar.

## File Onboarding Map

| Responsibility | File onboarding |
| --- | --- |
| In-stage browser shell + return paths + layout | [ConversationLibrarySurface.tsx](ConversationLibrarySurface.tsx.md) |
| Native history list | [ConversationLibraryList.tsx](ConversationLibraryList.tsx.md) |
| Read-only preview | [ConversationHistoryPreview.tsx](ConversationHistoryPreview.tsx.md) |
| Sole exact-open resume action | [OpenConversationAction.tsx](OpenConversationAction.tsx.md) |

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This route relies on its direct agents-remember source/tests and the reviewed L4
task/worker/verdict evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for the in-stage history browser. | `system/sources.md` checked | — |

## Cross-Repo References

The browser composes repository-local components over this package's own library contract; no
cross-repository implementation source governs it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The reconstructable library projection this browser reads. | [data/conversation-library overview](../../../data/conversation-library/overview.md) |
| The one-roof composition that mounts this browser in-stage. | [session-cockpit overview](../overview.md) |
| The live renderer whose block grammar the read-only preview reuses. | [conversation overview](../conversation/overview.md) |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: minimal body update for the V10 responsive fix —
  the Route Model's stale `@container (max-width:640px)` stacking threshold is corrected to `56rem` (the
  two columns crush below ~56rem, so the surface stacks earlier), and the sibling `MarkdownBlock`
  whole-word/inline-code-nowrap wrap policy (dependent on the RV-1 root override) is noted. The
  `nowrap` + container-query height-containment idiom (F22/F23/L4.R5) is unchanged; no data/authority/
  focus behavior changed. Verification pinned to the leaf base (`352d5cd`) until closeout stamps the
  candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the governing pillar for the in-stage
  previous-conversation browser — the read-only preview in the shared block grammar, the sole exact-open
  resume action with focus-only-on-opened-proof (R4) and same-requestId reconcile, the §4.4 return paths
  on one focus-return token, and the single-line-flex + container-query height-containment idiom that the
  F23 regression fix established (L4.R5). Verification is pinned to the leaf base (`0be0099`) because the
  new source route is uncommitted; closeout owns its first source stamp.
