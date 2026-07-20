# dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
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

- The `<section>` (L87) always carries `aria-label="Terminal diagnostics"`, `data-open`, and — when
  `!open` — `inert` and `aria-hidden` (L90-L92) plus the `closed` height-0/border-0 class (L19).
- **No PTY when closed:** the body is `open ? (…) : null` (L96), so `PtySurface` mounts ONLY while
  open (R2/R7/§14.1 — a closed drawer holds zero children and no terminal socket).
- Open state renders the header (uppercase `Terminal diagnostics` lockup + the italic caption
  `diagnostic stream · read only · not conversation history` + a `close` button) and the `vendorFrame`
  inset hosting `<PtySurface focused={focused} readOnly />` (L111) — the controlled runner log with
  input disabled.
- The shell sets `transition: "none"` (L17): keyboard/programmatic toggles never animate (§15.1).

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The keep-alive PTY surface hosted read-only inside the frame (its additive `readOnly` prop). | L10, L111 | [../PtySurface.tsx](../PtySurface.tsx) |
| The session type the drawer targets. | L9 | [../../../data/sessions.ts](../../../data/sessions.ts) |
| The stage body that owns default-off toggling and hides the drawer while the library overlay is up (F8). | — | [../ChatsStageBody.tsx](../ChatsStageBody.tsx) |
| The view that captures/consumes the diagnostics focus-return token (F9). | — | [../SessionsView.tsx](../SessionsView.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the terminal diagnostics
  drawer — default-off, inert + aria-hidden + no-PTY-when-closed, the A7 vendor-frame lockup/caption,
  and the read-only controlled PTY via `PtySurface readOnly`. Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
