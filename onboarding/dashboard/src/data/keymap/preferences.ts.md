# dashboard/src/data/keymap/preferences.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/keymap/preferences.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

Builds the effective cockpit keymap from immutable defaults, validated user overrides, and the
selected CodeMirror composer profile. It is the sole persistence/subscription boundary for
`cockpit.sessions.keymap.v1`.

## Code Commentary

- Parses a versioned localStorage payload strictly and reports malformed entries rather than
  silently accepting them.
- Rejects browser-reserved chords, printable composer bindings, collisions, and every attempt to
  remove or rebind the invariant F6 `focus.nextRegion` escape.
- Exposes `bindingFor`, command activity, CodeMirror conversion, and a stable effective signature so
  both the global zone dispatcher and mounted editors reconfigure from one source.
- Supports Emacs and Vim composer profiles. Vim owns Escape for insert/normal transitions; F6 stays
  the invariant way out of the editor.
- Publishes same-tab changes through an external-store subscription and cross-tab changes through
  the browser `storage` event.

## Invariants And Boundaries

Persistence is a user preference, not daemon truth. Invalid entries fall back to defaults with a
visible issue; they never weaken browser safety or the focus-escape invariant.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Cross-Repo References

The preference module imports only repository-local keymap definitions and browser/React APIs; no cross-repository implementation governs validation or persistence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Static chord definitions. | `CHROME_CHORDS`, `COMPOSER_CHORDS` | dashboard/src/data/keymap/chords.ts:20-81; dashboard/src/data/keymap/chords.ts:83-104 |
| Browser/PTY reserved set. | `PTY_RESERVED`, `BROWSER_FORBIDDEN` | dashboard/src/data/keymap/reserved.ts:62-150; dashboard/src/data/keymap/reserved.ts:153-202 |
| Global dispatcher consumer. | `useKeyboardZones` | dashboard/src/panels/session-cockpit/useKeyboardZones.ts:18-97 |
| Composer and reference UI consumers. | `SessionComposer`, `CommandPalette` | dashboard/src/panels/SessionComposer.tsx:57-117; dashboard/src/panels/session-cockpit/CommandPalette.tsx:379-449 |

## 260718-CHATS-L4 Reviewed Candidate Delta (ariaKeyshortcuts helper)

Added the pure **`ariaKeyshortcuts(chord)`** helper: it renders a validated tinykeys chord as the
WAI-ARIA `aria-keyshortcuts` token (`Control+Shift+Period` → `Control+Shift+.`). The interrupt hook
(`conversation/useConversationControls.ts`) reads `bindingFor(useEffectiveKeymap(), "conversation.stop")?.chord`
and converts it through this helper, so a rebind of the stop chord through the `cockpit.sessions.keymap.v1`
seam keeps the assistive-tech advertisement truthful (F25) — replacing a hardcoded default constant.
Additive to the effective-keymap boundary; verification stays pinned to the FEUI-L8 base until closeout.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 9 citation findings (4 rows); scoped recheck clean.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 (structured Chats renderer, reviewer FINAL PASS): recorded
  the pure `ariaKeyshortcuts(chord)` helper that renders a validated chord as the WAI-ARIA token, so
  the interrupt control's derived `aria-keyshortcuts` follows a rebind of `conversation.stop` (F25).
  Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-18T07:22+02:00 — Created for FEUI-L8 keymap preferences. Candidate metadata is blank
  because the source is new and uncommitted; closeout owns verification stamping.
