# dashboard/src/panels/session-cockpit/conversation/primitives.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The shared conversation-item primitives that enforce the ruled cross-item behaviors ONCE so every
block reads as one grammar (design §12.2, §14.2) and matches the cockpit house style (bare color
tokens, inline amber focus ring, lowercase interpunct chips — A8). No new palette or recipe is
introduced.

## Code Commentary

### Logic

- cit:([`ClampButton`], dashboard/src/panels/session-cockpit/conversation/primitives.tsx:38-68): the ONLY expand/collapse control for a clamped message/tool/diff. It is a real
  `<button>` with `aria-expanded`/`aria-controls`, and it shows an exact `show more (+N lines)` ONLY
  when a logical source-line count is known (`hiddenLines > 0`); otherwise plain `show more`/`show
  less`. `noun` defaults to `lines`. **FB7.4/A8/V12 (260718-CHATS-L5P):** the labels are now LOWERCASE
  (`show more`/`show less`, was `Show …`) and the control is a de-boxed underline text affordance
  (`clampButton`, L16-L31, dropped the border/padding chip for `textDecoration: underline` +
  `whiteSpace: nowrap`) — it never wraps its own label and matches the well's chip grammar.
- cit:([`sourceLineCount`], dashboard/src/panels/session-cockpit/conversation/primitives.tsx:71-74): counts logical source lines (`split("\n").length`) — the honest basis for
  an exact clamp count, never visual wrapping/pixels.
- `SourceBadge` / `sourceBadgeLabel` (L92/L108): a terse source/lane badge shown ONLY when origin
  changes interpretation (§13) — `agent bus` (agent-bus lane / durable-inbox source), `native replay`,
  `native history`, `input source unavailable` (unknown-input lane), `terminal`; ordinary
  operator/harness content is UNBADGED (returns `null`).
- `CapabilityReason` (L130, R11 — 260718-CHATS-L5P): a short honest CUE, no longer the reason wall. The
  VISIBLE text is the one-word capability state (`partial`/`unavailable`/`unverified`, or `<label>
  <state>` when an optional `label` disambiguates which capability, e.g. `history partial`); the exact
  server `reason` moves entirely into the hover `title` (dotted-underline `cue` recipe, `cursor: help`).
  It returns `null` when `state === "supported"`. The progressive disclosure is unit-pinned by
  `primitives.test.tsx` (visible = state word; `title` = full reason incl. optional `label:` prefix;
  supported = nothing). This replaced the prior always-visible `state: reason` paragraph, which was an
  implementation-jargon wall above every codex conversation (A3).
- cit:([`useClampIds`], dashboard/src/panels/session-cockpit/conversation/primitives.tsx:161-164): a stable `useId`-based `{buttonId, regionId}` pair binding a clamp button to
  its controlled region.

### Invariants And Boundaries

- An exact `+N lines` count is emitted only from a known logical source-line delta; a clamp with an
  unknown count degrades to plain `show more` rather than lying (F12/§14.2).
- A badge appears only when the source changes how the content should be read; the common case is
  deliberately unbadged (no chip noise).
- `CapabilityReason` shows only the one-word state as the visible cue and carries the SERVER's exact
  reason in the `title` — it never fabricates or paraphrases capability copy, and never renders the
  reason as always-visible chrome (R11).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The lane/source/capability types these primitives narrow over. [1]
- The clamp/badge consumer in the message grammar. [2]
- The clamp/badge consumer in the tool grammar. [3]
- The clamp/badge consumer in the diff grammar. [4]
- The surface that renders CapabilityReason cues (labeled `history`/`live`) for history/live completeness. [5]
- The renderer suite asserting the real clamp button + source badge. [6]
- The R11 progressive-disclosure cue unit pins (visible state word, full reason in `title`, supported = nothing). [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
