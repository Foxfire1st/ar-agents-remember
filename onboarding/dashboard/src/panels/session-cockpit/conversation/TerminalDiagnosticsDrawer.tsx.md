# dashboard/src/panels/session-cockpit/conversation/TerminalDiagnosticsDrawer.tsx

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The keep-alive PTY surface hosted read-only inside the frame (its additive `readOnly` prop). [1]
- The session type the drawer targets. [2]
- The stage body that owns default-off toggling and hides the drawer while the library overlay is up (F8). [3]
- The view that captures/consumes the diagnostics focus-return token (F9). [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
