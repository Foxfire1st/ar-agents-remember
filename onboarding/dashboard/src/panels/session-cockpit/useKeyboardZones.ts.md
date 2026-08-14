# dashboard/src/panels/session-cockpit/useKeyboardZones.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/useKeyboardZones.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:42+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## 260731-EFA-L8 Change

The react-hooks remediation pinned the keyboard-zone effect dependencies to
`[active, keymap]`; zone behavior is unchanged.

## Purpose

The **thin React binding over the pure keymap logic** (260715-FEUI-L1 S4): tinykeys at the window,
capture phase, active only while the sessions view is the visible view. Every handler defers to
`data/keymap` for zone resolution and the routing contract — this file owns ONLY the DOM wiring.

## Code Commentary

### Logic

- `active` gates the whole effect (cit:([`active`], dashboard/src/panels/session-cockpit/useKeyboardZones.ts:23-23)): the hidden keep-alive layer never grabs keys;
  `dispatch` rides a ref (cit:([`dispatchRef`], dashboard/src/panels/session-cockpit/useKeyboardZones.ts:27-27)) so rebinding never depends on render identity.
- **Composed handlers** (cit:([`handlers`], dashboard/src/panels/session-cockpit/useKeyboardZones.ts:36-36); cit:([`defaultPrevented`], dashboard/src/panels/session-cockpit/useKeyboardZones.ts:86-94)): one binding string can serve several zones with
  different actions (F6 = chrome region-cycle AND PTY exit-to-chrome), so handlers accumulate per
  chord string and at most one acts per event (`event.defaultPrevented` short-circuits).
- Chrome/composer chords (cit:(["routeKey(zone, event, target) !== \"handle\""], dashboard/src/panels/session-cockpit/useKeyboardZones.ts:51-51)): per event — resolve the zone (`zoneForTarget`), require the
  chord's `zones` list to include it, require `routeKey(...) === "handle"` (the generic printable
  suppression), then preventDefault + stopPropagation + dispatch the command id.
- PTY reserved chords (cit:(["for (const reserved of PTY_RESERVED)"], dashboard/src/panels/session-cockpit/useKeyboardZones.ts:61-61)): only `bound` entries with a `tinykeys` string are installed, the
  zone must be `pty`, and `routeKey` stays the authority (reserved.ts data) — an unbound/removed
  entry can never be intercepted by a stale binding.
- The composer `/` rule (cit:(["slashOpensPalette(target.value"], dashboard/src/panels/session-cockpit/useKeyboardZones.ts:80-80)): `[Shift]+/` (keeps layouts where `/` needs Shift working, e.g.
  German Shift+7), gated by zone = composer + the pure `slashOpensPalette(value, selectionStart)`
  caret test — the deliberate exception to printable suppression.
- `tinykeys(window, map, { ignore: () => false, capture: true })` (cit:(["import { tinykeys, type KeybindingsMap } from \"tinykeys\""], dashboard/src/panels/session-cockpit/useKeyboardZones.ts:7-7)): the **default ignore
  (skip form elements) is disabled** — composer chords MUST fire inside a textarea;
  editable-target suppression is the zone contract's job (printables only, R7).

### Invariants And Boundaries

- No routing decisions here — additions go into `data/keymap` tables, which this hook installs
  mechanically.
- tinykeys v4 ignores synthetic events without `event.code` (its `isKeyboardEvent` guard) — test
  keyDown inits must carry an explicit `code`.
- Window-level + capture-phase is deliberate (chords work regardless of inner focus); the palette
  stops propagation of its own Escape before this layer sees it.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The binding: composed per-chord handlers, zone/route gating, `/` rule, ignore-disabled tinykeys. | `useKeyboardZones` | dashboard/src/panels/session-cockpit/useKeyboardZones.ts:18-97 |
| The zone/routing contract every handler defers to. | `routeKey` | dashboard/src/data/keymap/zones.ts:54-58 |
| The chord tables it installs (`CHROME_CHORDS`, `COMPOSER_CHORDS`). | `CHROME_CHORDS` | dashboard/src/data/keymap/chords.ts:20-81 |
| The reserved set it installs — `PTY_RESERVED` lives in `reserved.ts`, not in `chords.ts`, which is why the old row's second range read out of bounds against the file it named. | `PTY_RESERVED` | dashboard/src/data/keymap/reserved.ts:62-150 |
| The view that supplies `active` + `dispatch`. | `useKeyboardZones` | dashboard/src/panels/session-cockpit/useKeyboardZones.ts:18-97 |
| End-to-end binding coverage (real markers, window tinykeys, preventDefault observation, active=false). | "keyboard zones over the legacy-raw PTY (S4)" | dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx:256-256 |

## FEUI-L8 Reviewed Candidate Delta

Installs the effective binding set rather than static tables and rebinds on signature change. Vim suppresses the cockpit Escape command so the editor owns mode changes; F6 remains active and invariant.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the pinned keyboard-zone deps fix. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T17:52+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 16 citation findings. Converted the
  six Logic line-cite parentheticals — plus the unflagged composed-handlers pair — to cit form against
  the post-rework layout (`active` 31-32, `dispatchRef` 27-28, `handlers`/`defaultPrevented` 36-41/86-94,
  `routeKey` 43-56, `PTY_RESERVED` 58-71, `slashOpensPalette` 73-84, `tinykeys` 95), and re-anchored +
  re-ranged the five Repo-Internal References rows. Scoped recheck clean.
- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived the stale `active` self-citation. L27-L28
  is the `dispatchRef` wiring, not the gate; the `active` guard is the effect's first statement, so the
  bullet now cites L31-L32 for the gate and keeps L27-L28 on the ref clause it actually describes.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4: the tinykeys window binding (capture
  phase, default ignore disabled, composed multi-zone handlers, reserved-set install guarded by
  `routeKey`, the `[Shift]+/` composer rule, `active` keep-alive gating). Verification metadata
  pinned to the task base until closeout stamps the L1 code commit.
