# dashboard/src/styles/tokens.css

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The global design-token CSS-var layer — the podracer OKLCH palette (note 08) as `:root` vars. As of
slice 5d this is **all** `tokens.css` holds (it was the ~1,200-line monolith; every component style
moved to co-located Panda).

## Code Commentary

### Logic

`:root { color-scheme: dark; --bg/--bg-panel/--ink/--grid; --amber/--cyan/--alarm/--mint/--dormant;
--font-mono; --glow-strength }`, plus — **260718-CHATS-L5P** — **`--well`** (`#070b0f`, the terminal
"well"): the darker inset the xterm pty pane already used (was a hardcoded `#070b0f` literal in
`panels/Terminal.tsx`). FB7.1/V31 promote it to a token so the STRUCTURED conversation stage
(`ConversationTimeline` viewport + `SessionComposer` editor frame) inherits the SAME well tone as the
legacy-raw pane — the developer's "chat doesn't look like a TUI" identity fix. Mirrored as the Panda
token `colors.well` in `panda.config.ts` (two views of one palette). The TUI-identity spec that derives
this (Toad `main.tcss` + Claude Code / Codex TUIs) lives in the leaf visual-audit `## FB7`. Plus —
260715-FEUI-L1 — **`--muted`** (`oklch(0.7 0.02 250)`,
muted control text): it existed only as a Panda token (`panda.config.ts`) + a hardcoded literal in
`index.css`, and the WebTUI mapping (`webtui.css` → `--foreground1: var(--muted)`) would have
referenced an undefined var — the spike test's declared-token assertion caught it. Plus — 260703-L14
— the six **rank-insignia tier vars** from the
approved V4 sketch: `--gold` `oklch(0.87 0.15 95)` / `--gold-dim` / `--gold-ghost` (the orchestration
tier: chevrons, hairline, row wash) and `--purple` `oklch(0.76 0.14 305)` / `--purple-dim` /
`--purple-ghost` (management). These back `index.css`'s base layer (body/utilities) and a few Panda
`css()` text-shadows that reference `var(--glow-strength)`. `panda.config.ts` mirrors the same palette
as **typed Panda tokens** (the source the component css/recipes resolve — the L14 components consume
the Panda `gold*`/`purple*` tokens, not these vars).

### Invariants And Boundaries

Tokens only — no component/selector rules. Keep in sync with the Panda token palette in
`panda.config.ts` (two views of one palette during the migration).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The Panda token mirror declares the palette under `colors`, including `colors.well`. [1]
- The pty pane consumes the `well` token for its background. [2]
- The session composer consumes the `well` token for its background. [3]
- The structured conversation stage consumes the `well` token for its background. [4]
- WebTUI maps `--foreground1` to `--muted`. [5]
- The WebTUI mapping is token-only and contains no raw color literals. [6]
- The spike assertion that every mapped var is declared here. [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Raises alarm and dormant lightness for the L8 accessibility contrast target while retaining the existing semantic token names and component contracts.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
