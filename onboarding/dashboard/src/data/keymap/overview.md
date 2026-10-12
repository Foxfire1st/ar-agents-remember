# dashboard/src/data/keymap/ — Keyboard Zone Contract Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/data/keymap/`                     |

## Governing Overview

[data overview](../overview.md) — this child owns keyboard contracts while the data overview owns
the surrounding cockpit state and authority boundaries.

## Purpose

`data/keymap/` is the xterm-free keyboard-ownership contract for the canonical Chats cockpit. Its chord tables, routing functions and focus model let consumers share keyboard policy without importing a terminal. The effective-keymap preference layer supplies the cockpit's tinykeys binding, keyboard-reference palette, CodeMirror composer and intent reviewer. The terminal consumes the same reserved-chord matcher.

Four zones own keys: **chrome** is the surrounding shell; **composer** scopes editor commands; **pty** handles only the bound reserved set through this routing contract; **review** scopes the intent reviewer's change traversal. Printable bindings are suppressed on editable targets in the non-PTY zones. The shared-source design is the standing contract; the implementation discrepancies described below must remain visible.

## Hot Path Summary

`resolveKeymap` combines defaults, validated user overrides and the composer profile into one effective map. `zoneForTarget` resolves chrome/composer/pty/review from the nearest `data-kbzone` marker, defaulting to chrome. Consumers check a binding's zone list before calling `routeKey`: PTY events are handled only when `matchReservedChord` matches a bound reservation; other zones pass printable events through on editable targets. The cockpit installs capture-phase tinykeys handlers while active, the reviewer installs its traversal handlers on its own root, and CodeMirror reconfigures its profile and command compartments. The terminal's xterm guard rejects bound reserved chords through the same matcher. `nextRegion` drives the F6 cycle over the available rail, stage and inspector regions.

## Construction

- [`reserved.ts`](reserved.ts.md) defines `PTY_RESERVED`: bound Ctrl+; for the palette, F6 for exit to chrome, and Ctrl+Alt+PageUp/PageDown for session navigation. Selection-aware Ctrl+C and Ctrl+Shift+C remain unbound reservation slots in this table. Each reservation carries a five-source codex/pi/claude/chrome/firefox collision record. `matchReservedChord` skips unbound entries and requires matching modifiers and a matching key or physical code. `BROWSER_FORBIDDEN` supplies the browser-owned chord denylist.
- [`zones.ts`](zones.ts.md) defines zone resolution, printable/editable classification and routing. Textareas, selects, contenteditable targets and writable inputs suppress printable bindings; read-only inputs do not. `slashOpensPalette` expresses the pure line-start caret rule. The cockpit textarea handler uses it; the live CodeMirror handler independently checks the selected document line's start and composition state.
- [`chords.ts`](chords.ts.md) defines `CHROME_CHORDS`, `COMPOSER_CHORDS` and `REVIEW_CHORDS`. Chrome Alt+Up/Down cycles sessions; composer Alt+Up dispatches `composer.popBack`; the PTY routing gate passes those native keys through. The default composer submit chord is Enter, with Shift+Enter installed by the composer for a newline. `conversation.stop` defaults to Control+Shift+Period in chrome and composer, excluding PTY. The reviewer defaults to J for `review.nextChange` and K for `review.previousChange`, both review-only.
- [`focus.ts`](focus.ts.md) defines the rail → stage → inspector cycle and the region, stage-header and PTY-host selectors. The controller filters collapsed rail/inspector regions before calling `nextRegion`; StatusLine is not a cycle region.
- [`preferences.ts`](preferences.ts.md) persists version 1 preferences under `cockpit.sessions.keymap.v1`, combines all three chord tables into defaults, validates overrides, exposes Emacs/Vim composer profiles and produces a signature for consumers. Invalid shapes, malformed or browser-forbidden chords, printable composer overrides, overlapping identical candidate chords and attempts to change the forward F6 command produce issues and restore defaults. The keyboard-reference page displays issues. Public writes notify same-tab subscribers; storage events notify cross-tab subscribers. Helpers convert chords to CodeMirror notation and ARIA shortcut tokens. The interrupt control derives its advertised shortcut from the effective stop binding.
- The active cockpit binding uses `useKeyboardZones`; the palette renders the effective zone groups and the reserved PTY table. `SessionsView` delegates to its controller and body, which own the live wiring and region markers. `SessionComposer` delegates editor construction and reconfiguration to `sessionComposerHooks.ts`, with the composer marker rendered by `sessionComposerParts.tsx`.
- The reviewer binds effective traversal chords with tinykeys on the nearest review root, checks the target's zone and `routeKey`, then moves through changes. `ReviewSurface` carries `data-kbzone="review"`. Its traversal implementation acts directly rather than through the cockpit command registry.
- The PTY surface supplies `reservedChordFilter` to `Terminal`; the filter returns false for a bound reserved match. `terminalSession.ts` invokes that filter from xterm's installed custom key-event handler. It also handles selection-aware copy separately, so the routing gate's passthrough result is not a guarantee that every such key becomes terminal input.
- `zones.test.ts` contains routing, PTY passthrough, reserved-set hygiene and printable-suppression assertions; `focus.test.ts` covers the region cycle; `preferences.test.ts` covers preference validation, profile selection, forward F6 protection, Meta/browser safety and same-/cross-tab notification. These are descriptions of test source, not test-execution results.

## Invariants And Boundaries

- **One PTY reservation authority:** the palette renders `PTY_RESERVED`, the cockpit binds its bound entries, and the installed terminal guard consumes `matchReservedChord`. Consumers must not fork the reserved list.
- **No bare-Escape claim by the PTY routing gate:** Escape and modified Escape pass through. The collision comments record Codex's Escape interrupt and Claude Code's Escape Escape rewind; the tests assert local passthrough behavior.
- **A collision replaces the chord, not the rule.** The recorded audit replaced Ctrl+Alt+[/] with Ctrl+Alt+PageUp/PageDown because Pi used Ctrl+Alt+] and Ctrl+Alt+['s recorded terminal encoding was Escape Escape. The source records the replacement's distinct CSI encodings and no audited harness binding. These are recorded audit findings, not a fresh verification of current vendor/browser behavior.
- The standing intent is that every bound chord is fully clear across all five audit sources, with collisions only on unbound reserved slots. The current records and tests establish that census for PTY reservations, not every effective chrome, composer or review override; that implementation coverage limit does not withdraw the wider intent. Ctrl+Shift+C's unbound slot records the Firefox collision.
- **Alt+Up ownership stays zone-specific:** composer pop-back, chrome session navigation and PTY passthrough must remain distinct.
- **Forward F6 remains the fixed focus escape:** preferences protect `focus.nextRegion`, and Vim suppresses the composer stage-header Escape binding while leaving F6 active. The implementation does not make `focus.prevRegion` equally immutable: a valid nonprintable override can replace Shift+F6.
- The core routing and focus modules remain pure/DOM-light. `preferences.ts` is the intentional React/browser boundary for localStorage and external-store subscriptions; no module in this directory imports xterm. Thus the original intent of terminal-independent routing is preserved, but the whole directory is not exclusively pure functions and data.
- The shared-source intent still has visible discrepancies: the live CodeMirror slash handler reproduces the line-start predicate instead of calling `slashOpensPalette`; review commands have no entry in `registerDefaultCommands`, although the original card records a standing expectation that dispatched chord commands have registry entries; and `zones.ts` still introduces its four-zone list with the comment “Three zones:”. The reviewer has its own direct binding, so registry absence must not be described as proof that traversal is unavailable.
- References to FEUI-L6 in reservation comments describe original ownership and intent. The installed terminal guard and separate selection-copy behavior are present in source; those comments do not establish a current leaf lifecycle status.

## Evidence

- The reviewer's zone and chords. [1]
- The reviewer's own binding on its zone. [2]
- The effective-keymap preference and validation boundary. [3]
- The thin React binding that installs the effective tables via tinykeys. [4]
- The `?` reference/profile page that renders the same effective map. [5]
- The command ids the chord tables dispatch into. [6]
- The cockpit wrapper delegates the DOM carrying the region markers to its body. [7]
- The live CodeMirror surface consumes profile and chord reconfiguration through its hooks. [8]
- Reserved PTY chords, recorded collision audit and bound-only matching. [9]
- Four-zone routing, editable classification and the pure slash predicate. [10]
- Default zone-scoped chords and forward F6 preference protection. [11]
- Preference subscriptions, conversions and profile activation. [12]
- Focus cycle and collapsed-region filtering. [13]
- Source assertions for routing, focus and preference contracts. [14]
- Effective review traversal wiring and its root marker. [15]
- Installed terminal guard consumes the reserved matcher; selection-aware copy is separate. [16]
- Composer marker, effective stop shortcut and interruptible stop-command registration. [17]
- Palette renders effective reviewer bindings, profiles, issues and PTY reservations. [18]
- Default command registry contains no review traversal entries. [19]
