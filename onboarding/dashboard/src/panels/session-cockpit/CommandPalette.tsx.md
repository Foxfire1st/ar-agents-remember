# dashboard/src/panels/session-cockpit/CommandPalette.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/CommandPalette.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
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
  query, reset on every open (L113-L117 — the palette is transient, never a standing filter).
- `runItem(id)` (L121-L126): runs through `registry.run(id, getContext())`; commands without
  `keepsPaletteOpen` close the palette, page-switch commands (keyboard.reference) keep it open
  and clear the query.
- `onKeyDown` (L128-L140): Escape closes (preventDefault + stopPropagation so the window-level
  layer never sees it); Backspace on an EMPTY query leaves a sub-page back to `commands` — the
  page pattern's back gesture.
- The `keys` page (L177-L206) renders three disabled groups straight from the data: Chrome /
  Composer chord tables (`CHROME_CHORDS`/`COMPOSER_CHORDS`) and the PTY reserved set
  (`PTY_RESERVED`, unbound slots labeled "(reserved, unbound)") under the heading "Terminal —
  everything passes through except exactly". `shouldFilter` is disabled on the keys page. The
  footer hint states the Esc-is-never-intercepted-over-the-terminal rule.
- cmdk is unstyled; the Panda `box` css styles its `[cmdk-*]` data-attribute parts (L36-L77).

### Invariants And Boundaries

- One options source: the commands page maps `registry.list(getContext())` — never a hardcoded
  command list; the keys page maps the keymap data — never copied chord strings.
- Non-portal is load-bearing (WebTUI scope + local focus). Do not lift the overlay out of the
  view root.
- Focus-return ownership sits in the VIEW (`closePalette` + the invoker ref kept across page
  switches); this component only reports close.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Pages, run/close semantics, back gesture, and the data-driven keys page. | L98-L218 | [CommandPalette.tsx](CommandPalette.tsx) |
| The registry contract (`list`/`run`/`keepsPaletteOpen`). | L33-L80 | [../../data/commands.ts](../../data/commands.ts) |
| The chord tables + reserved set the keys page renders. | L20-L86; L62-L150 | [../../data/keymap/chords.ts](../../data/keymap/chords.ts) |
| The view that owns open/page state and the invoker focus-return. | L235-L251; L496-L503 | [SessionsView.tsx](SessionsView.tsx) |
| Palette behavior coverage: open, Esc + focus return, keys page from real tables, suppression, `/` rule. | L112-L175 | [SessionsView.test.tsx](SessionsView.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
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

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented slash-normalized initial-query handling.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S3 (R4): the non-portal cmdk palette with
  the commands/keys page pattern (one options source; the `?` reference rendered from the live
  keymap data), Backspace-on-empty page return, Escape close, and `keepsPaletteOpen` handling.
  Verification metadata pinned to the task base until closeout stamps the L1 code commit.
