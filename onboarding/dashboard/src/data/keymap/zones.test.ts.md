# dashboard/src/data/keymap/zones.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/zones.test.ts`        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The contract under test. | `zoneForTarget` | dashboard/src/data/keymap/zones.ts:28-32 |
| The reserved set + verification records the hygiene describe walks. | `BROWSER_FORBIDDEN` | dashboard/src/data/keymap/reserved.ts:153-202 |
| The DOM-level counterpart (real markers, tinykeys, preventDefault observation). | `preventDefault` | dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx:287-287 |

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 6 initial citation findings (3 anchor, 0 prose, 3 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4/S5: the zone-routing contract suite —
  PTY passthrough (incl. bare Esc + harness-owned chords), bound-reserved interception,
  layout-robust code matching, unbound-slot non-interception, five-source verification hygiene,
  R7 printable suppression, and the `/` composer rule. Verification metadata pinned to the task
  base until closeout stamps the L1 code commit.
