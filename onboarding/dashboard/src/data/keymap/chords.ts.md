# dashboard/src/data/keymap/chords.ts

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The **chrome/composer chord tables**, and since MIK-L33 the intent reviewer's (`REVIEW_CHORDS`) (260715-FEUI-L1 S4, design §5.2) — data, not code, so the
tinykeys binding, the `?` keyboard-reference palette page, and the collision tests all read one
source. Zone scoping is per-chord: a chord fires only when the event's zone is listed; every other
zone passes it through.

## Code Commentary

### Logic

- cit:([`ZoneChord`], dashboard/src/data/keymap/chords.ts:10-18): tinykeys `chord` string (`[Shift]` marks an optional modifier — a real
  tinykeys v4 syntax), human `label` for the `?` overlay, target `commandId`, and the `zones`
  list.
- cit:([`CHROME_CHORDS`], dashboard/src/data/keymap/chords.ts:20-81): `Control+K` → `palette.open` (chrome+composer — zone-scoped so it
  NEVER fires over the PTY, where ctrl+k is Codex/Pi kill-line), `Alt+ArrowUp/Down` →
  `session.prev/next` (chrome ONLY — Codex binds alt+Up = edit_queued_message, Pi alt+up =
  dequeue; over a live PTY these always pass through), `Alt+Comma/Period` →
  `effort.decrease/increase` (chrome only — a deliberate convention match with Codex's own
  alt+,/. reasoning-effort chords), `F6`/`Shift+F6` → `focus.nextRegion/prevRegion`
  (chrome+composer), `[Shift]+?` → `keyboard.reference` (chrome; printable — never fires in
  editable targets, and that suppression is GENERIC: `routeKey`'s `isPrintable`/`isEditableTarget`
  contract covers every printable chord; no per-chord flag).
- cit:([`COMPOSER_CHORDS`], dashboard/src/data/keymap/chords.ts:83-104): `Control+Enter` → `composer.submit`, `Escape` →
  `focus.stageHeader` — composer-zone only, so Esc is never touched over the PTY.
- **`REVIEW_CHORDS` (MIK-L33, MIK-R33 adopting ICR-R32 rule 7):** `J` → `review.nextChange` and `K` →
  `review.previousChange` (labels `j`, `k`), both in the `review` zone only. They are printable, so the generic
  `routeKey` suppression keeps them inert in inputs, textareas and contenteditable regions, and the `review` zone is
  never the PTY zone. They join `DEFAULT_BINDINGS` in `preferences.ts`, so they can be rebound through the
  `cockpit.sessions.keymap.v1` preference and are listed on the `?` page's "Intent reviewer" group.

### Invariants And Boundaries

- Harness-owned chords stay chrome-only — widening a `zones` list to `pty` would violate the PTY
  passthrough contract; PTY interception belongs exclusively to `reserved.ts`.
- Browser-reserved chords (`BROWSER_FORBIDDEN`) are banned everywhere.
- Review round 2 (finding 3) DELETED the dead `ZoneChord.printable` field: printable suppression
  is enforced generically by `routeKey`, and a per-chord flag could only drift from the real rule.
  Do not reintroduce it.
- Command ids must exist in `data/commands.ts`'s registry — the chord layer dispatches ids, never
  functions. **Exception since MIK-L33:** `review.nextChange` and `review.previousChange` have no registry entry;
  the reviewer binds them itself on its own zone from the effective keymap (`panels/review/changeTraversal.ts`
  `useChangeTraversal`), and the registry's `run` answers `false` for an id it does not hold.

### 2026-07-24 Curator Delta

Harness-chat composition now uses plain Enter for submit; Shift+Enter remains the editor newline
binding at the same precedence. The chord table remains the single source shared by the key router and
keyboard-reference surfaces.

### Todos

- **MIK-L33 observation for the keymap owner:** the two review chords are dispatched outside the command registry
  (see the invariant above). If the rule that every chord's id is a registered command should hold without
  exception, the reviewer's traversal needs registry entries; nothing asserts it today.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The two zone-scoped chord tables and the generic-suppression comment on `?`. [1]
- The binding that installs both tables and enforces the per-chord zone lists. [2]
- The `?` page renders these tables under the Chrome/Composer group headings. [3]
- The command ids these chords dispatch (registered defaults). [4]
- The reviewer's `j`/`k` table, `review` zone only (MIK-L33). [5]
- The reviewer binds them itself on its zone from the effective keymap. [6]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

Alt+Up is now zone-sensitive: the composer owns authoritative pop-back, while chrome retains
`session.prev`. The keymap records both bindings explicitly so global navigation cannot intercept a
withdrawal gesture inside CodeMirror and the composer cannot steal the chord outside its zone.

## 260718-CHATS-L4 Reviewed Candidate Delta (conversation.stop chord)

The chord table gained the real **`conversation.stop`** interrupt chord — `Control+Shift+Period`,
scoped to the chrome+composer zones and excluded from the raw-PTY zone (interception there routes only
through `reserved.ts`) — replacing the stale L6 `turn.stop` registration (finding F2). It is the sole
`Control+Shift` entry, so it is collision-clear; the `preferences.ts` validation makes it rebindable
through the documented `cockpit.sessions.keymap.v1` seam, and the enabled control advertises the
EFFECTIVE assignment via `preferences.ts`'s `ariaKeyshortcuts` (never a phantom — F25). The chord
dispatches the id only when the palette `when`-gate reports the turn is interruptible. Additive to the
zone-scoping contract; the reviewed L4 candidate is uncommitted, verification stays pinned to the
FEUI-L1 base until closeout.
