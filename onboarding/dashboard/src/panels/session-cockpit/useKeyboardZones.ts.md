# dashboard/src/panels/session-cockpit/useKeyboardZones.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/useKeyboardZones.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **thin React binding over the pure keymap logic** (260715-FEUI-L1 S4): tinykeys at the window,
capture phase, active only while the sessions view is the visible view. Every handler defers to
`data/keymap` for zone resolution and the routing contract — this file owns ONLY the DOM wiring.

## Code Commentary

### Logic

- `active` gates the whole effect (L27-L28): the hidden keep-alive layer never grabs keys;
  `dispatch` rides a ref so rebinding never depends on render identity.
- **Composed handlers** (L30-L37, L79-L87): one binding string can serve several zones with
  different actions (F6 = chrome region-cycle AND PTY exit-to-chrome), so handlers accumulate per
  chord string and at most one acts per event (`event.defaultPrevented` short-circuits).
- Chrome/composer chords (L39-L49): per event — resolve the zone (`zoneForTarget`), require the
  chord's `zones` list to include it, require `routeKey(...) === "handle"` (the generic printable
  suppression), then preventDefault + stopPropagation + dispatch the command id.
- PTY reserved chords (L54-L64): only `bound` entries with a `tinykeys` string are installed, the
  zone must be `pty`, and `routeKey` stays the authority (reserved.ts data) — an unbound/removed
  entry can never be intercepted by a stale binding.
- The composer `/` rule (L69-L77): `[Shift]+/` (keeps layouts where `/` needs Shift working, e.g.
  German Shift+7), gated by zone = composer + the pure `slashOpensPalette(value, selectionStart)`
  caret test — the deliberate exception to printable suppression.
- `tinykeys(window, map, { ignore: () => false, capture: true })` (L88): the **default ignore
  (skip form elements) is disabled** — composer chords MUST fire inside a textarea;
  editable-target suppression is the zone contract's job (printables only, R7).

### Invariants And Boundaries

- No routing decisions here — additions go into `data/keymap` tables, which this hook installs
  mechanically.
- tinykeys v4 ignores synthetic events without `event.code` (its `isKeyboardEvent` guard) — test
  keyDown inits must carry an explicit `code`.
- Window-level + capture-phase is deliberate (chords work regardless of inner focus); the palette
  stops propagation of its own Escape before this layer sees it.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The binding: composed per-chord handlers, zone/route gating, `/` rule, ignore-disabled tinykeys. | L15-L90 | [useKeyboardZones.ts](useKeyboardZones.ts) |
| The zone/routing contract every handler defers to. | L28-L67 | [../../data/keymap/zones.ts](../../data/keymap/zones.ts) |
| The chord tables and reserved set it installs. | L20-L86; L62-L150 | [../../data/keymap/chords.ts](../../data/keymap/chords.ts) |
| The view that supplies `active` + `dispatch`. | L291-L298 | [SessionsView.tsx](SessionsView.tsx) |
| End-to-end binding coverage (real markers, window tinykeys, preventDefault observation, active=false). | L170-L208 | [SessionsView.test.tsx](SessionsView.test.tsx) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4: the tinykeys window binding (capture
  phase, default ignore disabled, composed multi-zone handlers, reserved-set install guarded by
  `routeKey`, the `[Shift]+/` composer rule, `active` keep-alive gating). Verification metadata
  pinned to the task base until closeout stamps the L1 code commit.
