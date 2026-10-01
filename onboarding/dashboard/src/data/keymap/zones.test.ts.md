# dashboard/src/data/keymap/zones.test.ts

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The keyboard-zone routing contract suite (260715-FEUI-L1 S4/S5, 12 cases). The PTY pass-through
invariants are the load-bearing ones: a hosted harness must receive EVERY key except exactly the
bound reserved set, and bare Esc is never claimed over a live PTY (Claude Code owns Esc Esc).

## Code Commentary

### Logic

Pure-object fixtures (`key`/`el` factories over `KeyEventLike`/`ZoneElementLike`) — no DOM events.
The describes pin, in order:

- **zoneForTarget** — pty/composer containers resolve; bogus/absent markers default to chrome.
- **PTY passthrough** — bare Esc and Esc chords pass; harness-owned chords pass (Codex alt+↑ /
  alt+, / alt+. · Pi ctrl+alt+] · ctrl+c interrupt · ctrl+k · plain keys); exactly the four bound
  reserved chords handle; `ctrl+;` also matches by physical `code` (layout robustness — `ö` with
  `code: Semicolon`); the unbound clipboard reservations are never intercepted and are exactly
  `clipboard.copySelection` + `clipboard.copy`.
- **Reserved-set hygiene (R5/R6)** — no reserved chord claims a bare-Esc sequence or a
  `BROWSER_FORBIDDEN` chord; every reserved chord carries a full five-source verification record
  (chrome/claude/codex/firefox/pi); every BOUND chord is verified fully clear, and the recorded
  Firefox DevTools collision lives only on the unbound `ctrl+shift+c` slot.
- **Printable suppression (R7)** — printables never fire as bindings in editable targets;
  non-printable chords (ctrl+enter, F6) still handle there; printables handle on non-editable
  targets — plus the `isEditableTarget`/`isPrintable` primitives.
- **The composer `/` rule** — palette opens only at position 0 or after a newline.

### Invariants And Boundaries

The hygiene describe is the durable R6 regression net: adding a reserved chord without a complete
five-source record, with a collision while bound, with a bare-Esc claim, or colliding with the
browser-forbidden list fails here. Test-only; jsdom-free (pure logic).

## Evidence

### Repo-Internal References

- The contract under test. [1]
- The reserved set + verification records the hygiene describe walks. [2]
- The DOM-level counterpart (real markers, tinykeys, preventDefault observation). [3]
