# dashboard/src/data/keymap/chords.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/chords.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`       |
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview      | `overview.md`                                    |

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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two zone-scoped chord tables and the generic-suppression comment on `?`. | `CHROME_CHORDS`; `COMPOSER_CHORDS` | dashboard/src/data/keymap/chords.ts:20-81; dashboard/src/data/keymap/chords.ts:83-104 |
| The binding that installs both tables and enforces the per-chord zone lists. | `useKeyboardZones` | dashboard/src/panels/session-cockpit/useKeyboardZones.ts:18-97 |
| The `?` page renders these tables under the Chrome/Composer group headings. | "Chrome — the shell around the panes"; "Composer — the editor owns its keys" | dashboard/src/panels/session-cockpit/CommandPalette.tsx:260-260; dashboard/src/panels/session-cockpit/CommandPalette.tsx:268-268 |
| The command ids these chords dispatch (registered defaults). | "palette.open"; "keyboard.reference" | dashboard/src/data/commands.ts:90-90; dashboard/src/data/commands.ts:97-97 |
| The reviewer's `j`/`k` table, `review` zone only (MIK-L33). | `REVIEW_CHORDS`; "review.nextChange" | dashboard/src/data/keymap/chords.ts:106-122 |
| The reviewer binds them itself on its zone from the effective keymap. | `useChangeTraversal`; "const binding = bindingFor(keymap, commandId);" | dashboard/src/panels/review/changeTraversal.ts:119-164 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

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

## Update History

- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-R33 rule 7:** `REVIEW_CHORDS` (`J`/`K` → `review.nextChange`/`review.previousChange`, `review` zone only, rebindable, listed on the `?` page). Purpose, Logic and Invariants updated; the rule that chord ids are registered commands now names its exception (the reviewer binds its two chords itself; no `data/commands.ts` entry), recorded as a Todo for the keymap owner. Two rows added.
- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 4 repo-internal citation rows and preserved verification metadata.

- 2026-07-24T13:17:50Z — Updated the default composer submit chord to Enter. Verification hash/date
  remain pinned to the pre-commit source stamp.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 (structured Chats renderer, reviewer FINAL PASS): recorded
  the new `conversation.stop` chord (`Control+Shift+Period`, chrome+composer, pty-excluded,
  collision-audited) replacing the stale `turn.stop` (F2); the effective assignment drives the
  derived `aria-keyshortcuts` (F25). Verification metadata remains pinned to the leaf base until
  closeout.
- 2026-07-17T21:39+02:00 — FEUI-L5: recorded the composer/chrome Alt+Up ownership split.

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4: the chrome/composer chord tables with
  per-chord zone lists (harness-owned Alt chords chrome-only; ctrl+k never over PTY; composer Esc
  → stage header). Review round 2 (finding 3) removed the never-read `printable` field in favor of
  the documented generic `routeKey` suppression. Verification metadata pinned to the task base
  until closeout stamps the L1 code commit.
