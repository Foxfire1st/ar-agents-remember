# dashboard/src/styles/tokens.css

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/styles/tokens.css`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-21T05:30+02:00                           |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34`       |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Panda token mirror of this palette (incl. `colors.well`). | L30-L46 | [panda.config.ts](agents-remember/dashboard/panda.config.ts) |
| The pty pane + structured stage that consume `well` (parity is the FB7.1 acceptance test). | — | [../panels/Terminal.tsx](../panels/Terminal.tsx.md) · [../panels/session-cockpit/conversation/ConversationTimeline.tsx](../panels/session-cockpit/conversation/ConversationTimeline.tsx.md) · [../panels/SessionComposer.tsx](../panels/SessionComposer.tsx.md) |
| The WebTUI mapping that consumes these vars (incl. `--muted`) — no raw literals allowed there. | L17-L34 | [webtui.css](webtui.css) |
| The spike assertion that every mapped var is declared here. | L117-L128 | [../test/webtuiSpike.test.ts](../test/webtuiSpike.test.ts) |

## FEUI-L8 Reviewed Candidate Delta

Raises alarm and dormant lightness for the L8 accessibility contrast target while retaining the existing semantic token names and component contracts.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
