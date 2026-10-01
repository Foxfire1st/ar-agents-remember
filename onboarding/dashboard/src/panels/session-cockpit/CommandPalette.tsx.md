# dashboard/src/panels/session-cockpit/CommandPalette.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **cmdk command palette** (260715-FEUI-L1 S3, R4) with the palette-page pattern established:
page `commands` lists the live registry (the one options source); page `keys` renders the SAME
chord/reserved-set data the tinykeys layer binds (`data/keymap`), so the `?` keyboard reference
can never drift from the real bindings. Deliberately **NOT a portal**: the overlay stays inside
the sessions-view root so the `[data-view="sessions"]` WebTUI scope covers it and focus return
stays local (R7 — the view's `closePalette` hands focus back to the invoker).

## Code Commentary

### Logic

- Controlled by the view: `open`/`page` state, `onClose`, `onPage`; the component holds only the
  query, reset on every open (cit:([`initialQuery`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:400-400) — the palette is transient, never a standing filter).
- `runItem(id)` cit:([`runItem`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:418-427): runs through `registry.run(id, getContext())`; commands without
  `keepsPaletteOpen` close the palette, page-switch commands (keyboard.reference) keep it open
  and clear the query.
- cit:(["const onKeyDown = (event: ReactKeyboardEvent<HTMLDivElement>) =>"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:429-429): Escape closes (preventDefault + stopPropagation so the window-level
  layer never sees it); Tab/Shift-Tab wrap focus inside the dialog (the modal focus
  trap over the dialog's own enabled inputs/buttons/tabbables); Backspace on an EMPTY query leaves
  a sub-page back to `commands` — the page pattern's back gesture.
- The `keys` page cit:(["Chrome — the shell around the panes"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:260-260) renders four disabled groups from the effective keymap (three before MIK-L33). The Chrome group and the Composer group filter the effective bindings by zone; the Composer group also drops profile-inactive commands, as shown by cit:(["Composer — the editor owns its keys"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:268-268). The old static chord tables are not read here; they only seed the default bindings. **Since MIK-L33** (MIK-R33 rule 7) a group headed "Intent reviewer — while focus is inside it" lists the effective bindings whose zones include `review` (`review.nextChange` `j`, `review.previousChange` `k`), between the keymap issues and the terminal group, so a rebinding shows here too. The `?` page lives in the sessions view's palette, which is not reachable while the reviewer takeover is open (pre-existing; review R1 F9, left as ruled 2026-09-30T17:47:43).
- The PTY reserved set and its unbound slots are rendered under the terminal heading cit:(["Terminal — everything passes through except exactly"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:309-309). The page also carries the composer-profile toggle cit:(["composer-profile-toggle"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:291-291) and keymap validation issues cit:(["keymap-validation"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:297-297). `shouldFilter` is disabled on the keys page cit:([`shouldFilter`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:359-359). The footer hint cit:(["esc closes · backspace returns to commands · Esc is NEVER intercepted over the terminal"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:379-379) states the Esc-is-never-intercepted-over-the-terminal rule.
- cmdk is unstyled; the Panda `box` css styles its `[cmdk-*]` data-attribute parts (cit:([`box`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:38-110)).
- **V1 panel clamp (260718-CHATS-L5P)** (cit:([`box`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:38-110)): the panel `box` is `overflow:hidden` and its
  `[cmdk-root]` is a bounded flex column (`flex:1; minHeight:0; overflow:hidden`) with the
  `[cmdk-list]` as the sole interior scroller (`flex:1; minHeight:0; overflow:auto`). The keys reference
  is taller than the `maxHeight:70%` panel; without this clamp its list rows + footer spilled onto a
  TRANSPARENT background over the live composer/StatusLine (help text superimposed on page text). Now the
  list scrolls INSIDE the panel and the footer stays on the panel background.

### Invariants And Boundaries

- One options source: the commands page maps `registry.list(getContext())` — never a hardcoded
  command list; the keys page maps the keymap data — never copied chord strings.
- Non-portal is load-bearing (WebTUI scope + local focus). Do not lift the overlay out of the
  view root.
- Focus-return ownership sits in the VIEW (`closePalette` + the invoker ref kept across page
  switches); this component only reports close.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- Pages, run/close semantics, back gesture, and the data-driven keys page. [1]
- The registry contract (`list`/`run`/`keepsPaletteOpen`). [2]
- The keys page renders the PTY-reserved terminal entries. [3]
- The view that owns open/page state and the invoker focus-return. [4]
- Palette behavior coverage: open, Esc + focus return, keys page from real tables, suppression, `/` rule. [5]
- The reviewer's group on the keys page, from the effective bindings (MIK-L33). [6]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

Each palette open now normalizes and seeds the query passed by the composer slash command. Reopen
replaces stale query state; filtering applies the normalized text to command titles and keywords.
The palette executes registered commands but never interprets a slash line as prompt delivery.

## FEUI-L8 Reviewed Candidate Delta

Consumes the effective keymap for command labels/reference rows and exposes the Emacs/Vim profile plus validation issues. The modal dialog traps Tab focus; action palettes close before focus commands run so invoker restoration cannot overwrite the command's destination.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
