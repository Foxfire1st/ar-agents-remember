# dashboard/src/data/keymap/preferences.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/keymap/preferences.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate |  2026-07-18T07:47:42+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Cross-Repo References

The preference module imports only repository-local keymap definitions and browser/React APIs; no cross-repository implementation governs validation or persistence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Static chord definitions. | [chords.ts](chords.ts) |
| Browser/PTY reserved set. | [reserved.ts](reserved.ts) |
| Global dispatcher consumer. | [useKeyboardZones.ts](../../panels/session-cockpit/useKeyboardZones.ts) |
| Composer and reference UI consumers. | [SessionComposer.tsx](../../panels/SessionComposer.tsx) · [CommandPalette.tsx](../../panels/session-cockpit/CommandPalette.tsx) |

## Update History

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 keymap preferences. Candidate metadata is blank
  because the source is new and uncommitted; closeout owns verification stamping.
