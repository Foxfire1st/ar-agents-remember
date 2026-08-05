# dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The terminal diagnostics drawer (design §12.6, §14.1; finding A7). It is CLOSED by default and on a
fresh profile. When closed it is `inert`, removed from the accessibility tree, and height-collapsed —
closing never touches the conversation, draft, queue, interaction, or native process. Vendor output is
FRAMED as diagnostic content (inset container, uppercase label, muted border) so vendor colors can
never read as app chrome; for a controlled session the hosted PTY is read-only.

## Code Commentary

### Logic

- The `<section>` (cit:([`TerminalDiagnosticsDrawer`, "Terminal diagnostics"], dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:77-99)) always carries `aria-label="Terminal diagnostics"`, `data-open`, and — when
  `!open` — `inert` and `aria-hidden` (cit:([`inert`], dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:89-90)) plus the `closed` height-0/border-0 class (cit:([`closed`], dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:19-19)).
- **No PTY when closed:** the body is `open ? (…) : null` (cit:(["open ? (", `PtySurface`], dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:96-96; dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:111-111)), so `PtySurface` mounts ONLY while
  open (R2/R7/§14.1 — a closed drawer holds zero children and no terminal socket).
- Open state renders the header (uppercase `Terminal diagnostics` lockup + the italic caption
  `diagnostic stream · read only · not conversation history` + a `close` button) and the `vendorFrame`
  inset hosting `<PtySurface focused={focused} readOnly />` (cit:([`PtySurface`, `readOnly`], dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:111-111)) — the controlled runner log with
  input disabled.
- The shell sets `transition: "none"` (cit:(["none"], dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:17-17)): keyboard/programmatic toggles never animate (§15.1).

### Invariants And Boundaries

- Default-off, inert-when-closed, and mounts no PTY when closed — the negative-proof the renderer
  suite and the reviewer's live DOM probe assert (R7).
- The drawer is a read-only DIAGNOSTIC, never a fallback message renderer: a projector failure raises
  the fail-loud `ConversationReconnect` banner, never a silent PTY substitution.
- Focus-return on close is owned by the invoker (SessionsView captures a FocusReturnToken on open and
  restores on close — F9); this component only renders the close affordance.
- Vendor output is always framed (A7) so it cannot read as app chrome.

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
| The keep-alive PTY surface hosted read-only inside the frame (its additive `readOnly` prop). | "landed"; "terminal-diagnostics-frame" | dashboard/src/panels/session-cockpit/PtySurface.tsx:225-228; dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx:110-111 |
| The session type the drawer targets. | `OpenSession` | dashboard/src/data/sessions.ts:28-83 |
| The stage body that owns default-off toggling and hides the drawer while the library overlay is up (F8). | "chats-stage-layers"; `TerminalDiagnosticsDrawer`; `setChatsDiagnosticsOpen`; `toggleChatsDiagnostics` | dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:407-413; dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:478-486; dashboard/src/panels/session-cockpit/SessionsView.tsx:287-287; dashboard/src/panels/session-cockpit/SessionsView.tsx:401-413 |
| The view that captures/consumes the diagnostics focus-return token (F9). | `toggleChatsDiagnostics`; `isConnected` | dashboard/src/panels/session-cockpit/SessionsView.tsx:401-413 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-03T09:55+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 11 assigned citation findings (3 missing anchors, 3 malformed sources, and 5 prose citations); final scoped check is clean. Max-reviewer Tier-2 subject-binding addendum replaced declaration-only pointers with the PTY implementation, library/drawer render gate, and diagnostics focus capture/consume ranges.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the terminal diagnostics
  drawer — default-off, inert + aria-hidden + no-PTY-when-closed, the A7 vendor-frame lockup/caption,
  and the read-only controlled PTY via `PtySurface readOnly`. Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
