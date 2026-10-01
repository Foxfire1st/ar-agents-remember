# dashboard/src/data/keymap/preferences.ts

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
- The defaults are `CHROME_CHORDS`, `COMPOSER_CHORDS` and, since MIK-L33, `REVIEW_CHORDS` (`DEFAULT_BINDINGS`), so
  the reviewer's `review.nextChange`/`review.previousChange` are known commands here: rebindable, validated like the
  others, and resolved for the reviewer through `bindingFor`.
- Supports Emacs and Vim composer profiles. Vim owns Escape for insert/normal transitions; F6 stays
  the invariant way out of the editor.
- Publishes same-tab changes through an external-store subscription and cross-tab changes through
  the browser `storage` event.

## Invariants And Boundaries

Persistence is a user preference, not daemon truth. Invalid entries fall back to defaults with a
visible issue; they never weaken browser safety or the focus-escape invariant.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

No configured Domain Documentation source exists for this file.

### Cross-Repo References

The preference module imports only repository-local keymap definitions and browser/React APIs; no cross-repository implementation governs validation or persistence.

No applicable cross-repository source was found.

### Repo-Internal References

- Static chord definitions. [1]
- Browser/PTY reserved set. [2]
- Global dispatcher consumer. [3]
- Composer and reference UI consumers. [4]
- The default bindings include the reviewer's table (MIK-L33). [5]

## 260718-CHATS-L4 Reviewed Candidate Delta (ariaKeyshortcuts helper)

Added the pure **`ariaKeyshortcuts(chord)`** helper: it renders a validated tinykeys chord as the
WAI-ARIA `aria-keyshortcuts` token (`Control+Shift+Period` → `Control+Shift+.`). The interrupt hook
(`conversation/useConversationControls.ts`) reads `bindingFor(useEffectiveKeymap(), "conversation.stop")?.chord`
and converts it through this helper, so a rebind of the stop chord through the `cockpit.sessions.keymap.v1`
seam keeps the assistive-tech advertisement truthful (F25) — replacing a hardcoded default constant.
Additive to the effective-keymap boundary; verification stays pinned to the FEUI-L8 base until closeout.
