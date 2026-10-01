# dashboard/src/panels/session-cockpit/useKeyboardZones.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The binding: composed per-chord handlers, zone/route gating, `/` rule, ignore-disabled tinykeys. [1]
- The zone/routing contract every handler defers to. [2]
- The chord tables it installs (`CHROME_CHORDS`, `COMPOSER_CHORDS`). [3]
- The reserved set it installs — `PTY_RESERVED` lives in `reserved.ts`, not in `chords.ts`, which is why the old row's second range read out of bounds against the file it named. [4]
- The view that supplies `active` + `dispatch`. [5]
- End-to-end binding coverage (real markers, window tinykeys, preventDefault observation, active=false). [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Installs the effective binding set rather than static tables and rebinds on signature change. Vim suppresses the cockpit Escape command so the editor owns mode changes; F6 remains active and invariant.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
