# dashboard/src/styles/tokens.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/styles/tokens.css`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-21T05:30+02:00                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The Panda token mirror declares the palette under `colors`, including `colors.well`. | `colors`; "well: { value:" | dashboard/panda.config.ts:30-30; dashboard/panda.config.ts:36-36 |
| The pty pane consumes the `well` token for its background. | "background: \"well\"" | dashboard/src/panels/Terminal.tsx:27-27 |
| The session composer consumes the `well` token for its background. | "background: \"well\"" | dashboard/src/panels/sessionComposerStyles.ts:13-13 |
| The structured conversation stage consumes the `well` token for its background. | "background: \"well\"" | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/styles.ts:12-12 |
| WebTUI maps `--foreground1` to `--muted`. | "--foreground1" | dashboard/src/styles/webtui.css:28-28 |
| The WebTUI mapping is token-only and contains no raw color literals. | "[data-view=\"sessions\"] { --background0: var(--bg); --background1: var(--bg-panel); --background2: var(--grid); --background3: color-mix(in oklch, var(--grid) 55%, var(--muted)); --foreground0: var(--ink); --foreground1: var(--muted); --foreground2: color-mix(in oklch, var(--muted) 60%, var(--bg-panel)); --box-border-color: var(--grid); --font-family: var(--font-mono); --font-size: 14px; --line-height: 1.3; }" | dashboard/src/styles/webtui.css:22-34 |
| The spike assertion that every mapped var is declared here. | "references only existing token vars — no raw color literals (no second color system)" | dashboard/src/test/webtuiSpike.test.ts:117-128 |

## FEUI-L8 Reviewed Candidate Delta

Raises alarm and dormant lightness for the L8 accessibility contrast target while retaining the existing semantic token names and component contracts.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: resolved the CSS anchor ambiguity with a source-exact whole-rule quote, regenerated the complete mapping extent with the locked fixer, and inspected it against the approved claim; no semantic claim changes.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: selected the complete sessions token-mapping rule as the whole-claim anchor and returned its binding to provisional fixer input.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: repaired the `well` mirror/consumer bindings and separated the proven `--foreground1` mapping from the broader token-only WebTUI claim; new bindings remain provisional.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: added the `--well` (`#070b0f`) terminal-well token
  — the xterm pty inset promoted from a Terminal.tsx literal (FB7.1/V31) so the structured conversation
  stage + composer inherit the same well tone; mirrored as Panda `colors.well`. Two-views-of-one-palette
  rule unchanged. TUI-identity spec home is the leaf visual-audit `## FB7`. Verification pinned to the
  leaf base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T00:25+02:00 — 260715-FEUI-L1 S1: added `--muted` (`oklch(0.7 0.02 250)`), mirroring
  panda.config's `muted` token — the WebTUI mapping references it and the spike test's
  declared-token assertion caught that it existed only as a Panda token + a hardcoded literal.
  Two-views-of-one-palette rule unchanged. Verification metadata pinned to the task base until
  closeout stamps the L1 code commit.
- 2026-07-06T23:57:18+02:00 — 260703-L14 (visual hierarchy + chat grouping): added the six rank-insignia
  tier vars (`--gold`/`--gold-dim`/`--gold-ghost`, `--purple`/`--purple-dim`/`--purple-ghost` — the
  V4 sketch's OKLCH values), mirrored as typed Panda tokens in `panda.config.ts` (two views of one
  palette, unchanged rule). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-15T17:00 — Created for slice 5d: `tokens.css` reduced to the `:root` design tokens (the
  1.2k-line monolith retired into co-located Panda). Verification metadata pinned until closeout
  stamps the 5d code commit.
