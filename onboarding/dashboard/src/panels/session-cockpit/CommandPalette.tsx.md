# dashboard/src/panels/session-cockpit/CommandPalette.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/CommandPalette.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-21T05:30+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                   |

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
  query, reset on every open (cit:([`initialQuery`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:392-392) — the palette is transient, never a standing filter).
- `runItem(id)` cit:([`runItem`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:410-419): runs through `registry.run(id, getContext())`; commands without
  `keepsPaletteOpen` close the palette, page-switch commands (keyboard.reference) keep it open
  and clear the query.
- cit:(["const onKeyDown = (event: ReactKeyboardEvent<HTMLDivElement>) =>"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:324-324; dashboard/src/panels/session-cockpit/CommandPalette.tsx:421-421) =>"]"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:324-324): Escape closes (preventDefault + stopPropagation so the window-level
  layer never sees it); Tab/Shift-Tab wrap focus inside the dialog (the modal focus
  trap over the dialog's own enabled inputs/buttons/tabbables); Backspace on an EMPTY query leaves
  a sub-page back to `commands` — the page pattern's back gesture.
- The `keys` page cit:(["Chrome — the shell around the panes"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:260-260) renders three disabled groups from the effective keymap. The Chrome group and the Composer group filter the effective bindings by zone; the Composer group also drops profile-inactive commands, as shown by cit:(["Composer — the editor owns its keys"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:268-268). The old static chord tables are not read here; they only seed the default bindings.
- The PTY reserved set and its unbound slots are rendered under the terminal heading cit:(["Terminal — everything passes through except exactly"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:301-301). The page also carries the composer-profile toggle cit:(["composer-profile-toggle"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:291-291) and keymap validation issues cit:(["keymap-validation"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:297-297). `shouldFilter` is disabled on the keys page cit:([`shouldFilter`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:351-351). The footer hint cit:(["esc closes · backspace returns to commands · Esc is NEVER intercepted over the terminal"], dashboard/src/panels/session-cockpit/CommandPalette.tsx:371-371) states the Esc-is-never-intercepted-over-the-terminal rule.
- cmdk is unstyled; the Panda `box` css styles its `[cmdk-*]` data-attribute parts (cit:([`box`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:31-103)).
- **V1 panel clamp (260718-CHATS-L5P)** (cit:([`box`], dashboard/src/panels/session-cockpit/CommandPalette.tsx:31-103)): the panel `box` is `overflow:hidden` and its
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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pages, run/close semantics, back gesture, and the data-driven keys page. | `CommandPalette` | dashboard/src/panels/session-cockpit/CommandPalette.tsx:379-449 |
| The registry contract (`list`/`run`/`keepsPaletteOpen`). | `CommandRegistry` | dashboard/src/data/commands.ts:47-55 |
| The keys page renders the PTY-reserved terminal entries. | "Terminal — everything passes through except exactly" | dashboard/src/panels/session-cockpit/CommandPalette.tsx:301-301 |
| The view that owns open/page state and the invoker focus-return. | `closePalette` | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:379-379 |
| Palette behavior coverage: open, Esc + focus return, keys page from real tables, suppression, `/` rule. | "opens on ctrl+k from the chrome zone and closes on Escape" | dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx:171-171 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

Each palette open now normalizes and seeds the query passed by the composer slash command. Reopen
replaces stale query state; filtering applies the normalized text to command titles and keywords.
The palette executes registered commands but never interprets a slash line as prompt delivery.

## FEUI-L8 Reviewed Candidate Delta

Consumes the effective keymap for command labels/reference rows and exposes the Emacs/Vim profile plus validation issues. The modal dialog traps Tab focus; action palettes close before focus commands run so invoker restoration cannot overwrite the command's destination.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 15 citation claims; narrowed the keys-page row to PTY-reserved rendering; normalized 1 redundant prose subrange; scoped result 0 findings.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 2 stale self-citations and corrected
  one now-false claim inside them. `onKeyDown` L128-L140 → L195-L224 (the handler also grew the
  modal Tab focus trap at L202-L218, which the FEUI-L8 delta already described but Logic did not
  cite). The `keys` page L177-L206 → L274-L331, and its "Chrome / Composer chord tables
  (`CHROME_CHORDS`/`COMPOSER_CHORDS`)" claim is no longer true: neither constant is imported by
  this file any more — both groups filter `useEffectiveKeymap()`'s `bindings` by zone, and the
  tables survive only as `data/keymap/preferences.DEFAULT_BINDINGS` seeds (verified by grep across
  `dashboard/src`). Added the previously undocumented composer-profile toggle and keymap-validation
  rows the same range covers. NOT fixed (beyond this worklist): the query-reset citation L113-L117
  is now L177-L180, `runItem` L121-L126 is L184-L193, the `box` css L36-L77 is L31-L103 (its
  `[cmdk-*]` parts L52-L102), and the Repo-Internal References row citing `chords.ts` for what the
  keys page renders no longer matches the source it renders from.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the V1 panel clamp — the `box` is
  `overflow:hidden` with `[cmdk-root]`/`[cmdk-list]` as a bounded flex column + interior scroller, so the
  tall keys reference no longer spills its rows/footer onto a transparent background over the live page.
  Page pattern, one-options-source, non-portal focus-return unchanged. Verification pinned to the leaf
  base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented slash-normalized initial-query handling.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S3 (R4): the non-portal cmdk palette with
  the commands/keys page pattern (one options source; the `?` reference rendered from the live
  keymap data), Backspace-on-empty page return, Escape close, and `keepsPaletteOpen` handling.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
