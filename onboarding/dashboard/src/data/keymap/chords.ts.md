# dashboard/src/data/keymap/chords.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/keymap/chords.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T00:20+02:00                           |
| lastVerifiedCommitHash | `ee955085a2010f62e9ad4d2bdc6aa77975daa5f3`       |
| lastVerifiedCommitDate | 2026-07-17T00:42:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

The **chrome/composer chord tables** (260715-FEUI-L1 S4, design §5.2) — data, not code, so the
tinykeys binding, the `?` keyboard-reference palette page, and the collision tests all read one
source. Zone scoping is per-chord: a chord fires only when the event's zone is listed; every other
zone passes it through.

## Code Commentary

### Logic

- `ZoneChord` (L10-L18): tinykeys `chord` string (`[Shift]` marks an optional modifier — a real
  tinykeys v4 syntax), human `label` for the `?` overlay, target `commandId`, and the `zones`
  list.
- `CHROME_CHORDS` (L20-L71): `Control+K` → `palette.open` (chrome+composer — zone-scoped so it
  NEVER fires over the PTY, where ctrl+k is Codex/Pi kill-line), `Alt+ArrowUp/Down` →
  `session.prev/next` (chrome ONLY — Codex binds alt+Up = edit_queued_message, Pi alt+up =
  dequeue; over a live PTY these always pass through), `Alt+Comma/Period` →
  `effort.decrease/increase` (chrome only — a deliberate convention match with Codex's own
  alt+,/. reasoning-effort chords), `F6`/`Shift+F6` → `focus.nextRegion/prevRegion`
  (chrome+composer), `[Shift]+?` → `keyboard.reference` (chrome; printable — never fires in
  editable targets, and that suppression is GENERIC: `routeKey`'s `isPrintable`/`isEditableTarget`
  contract covers every printable chord; no per-chord flag).
- `COMPOSER_CHORDS` (L73-L86): `Control+Enter` → `composer.submit`, `Escape` →
  `focus.stageHeader` — composer-zone only, so Esc is never touched over the PTY.

### Invariants And Boundaries

- Harness-owned chords stay chrome-only — widening a `zones` list to `pty` would violate the PTY
  passthrough contract; PTY interception belongs exclusively to `reserved.ts`.
- Browser-reserved chords (`BROWSER_FORBIDDEN`) are banned everywhere.
- Review round 2 (finding 3) DELETED the dead `ZoneChord.printable` field: printable suppression
  is enforced generically by `routeKey`, and a per-chord flag could only drift from the real rule.
  Do not reintroduce it.
- Command ids must exist in `data/commands.ts`'s registry — the chord layer dispatches ids, never
  functions.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The two zone-scoped chord tables and the generic-suppression comment on `?`. | L20-L86 | [chords.ts](chords.ts) |
| The binding that installs both tables and enforces the per-chord zone lists. | L39-L49 | [../../panels/session-cockpit/useKeyboardZones.ts](../../panels/session-cockpit/useKeyboardZones.ts) |
| The `?` page renders these tables under the Chrome/Composer group headings. | L179-L194 | [../../panels/session-cockpit/CommandPalette.tsx](../../panels/session-cockpit/CommandPalette.tsx) |
| The command ids these chords dispatch (registered defaults). | L87-L179 | [../commands.ts](../commands.ts) |

## Update History

- 2026-07-17T00:20+02:00 — Created for 260715-FEUI-L1 S4: the chrome/composer chord tables with
  per-chord zone lists (harness-owned Alt chords chrome-only; ctrl+k never over PTY; composer Esc
  → stage header). Review round 2 (finding 3) removed the never-read `printable` field in favor of
  the documented generic `routeKey` suppression. Verification metadata pinned to the task base
  until closeout stamps the L1 code commit.
