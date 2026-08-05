# dashboard/src/data/ptyHarvest.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/ptyHarvest.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

**Legacy-raw byte-stream harvesting** (260715-FEUI-L6 R7, design §8.1) — CLIENT-SIDE ONLY. A
vendor TUI in a legacy raw (`controlState: "unsupported"`) pane is that pane's only
attention/turn signal, so xterm-observed facts are harvested into this store: `onBell` → a rail
attention marker, OSC 0/2 title changes → row label hints, and — where a vendor emits them (e.g.
Pi) — OSC 133 prompt marks / OSC 9;4 progress → turn-state HINTS. **Hints never enter
`stateGrammar`**: the dot must never lie, so harvested signals render as clearly-labeled hints
beside the grammar, never as states. Controlled panes get NONE of this — harvesting hooks are
wired only for the raw archetype in `PtySurface`.

## Code Commentary

### Logic

- **`PtyHarvest` per session**: `bellPending` (+`lastBellAt`) — bell observed and not
  yet acknowledged; `title` — the vendor TUI's own OSC 0/2 window title, a label HINT, never the
  catalog label; `turnHint` — the last parsed `PtyTurnHint`
  (`prompt | command-running | command-finished | progress[percent] | progress-done`). cit:([`PtyHarvest`], dashboard/src/data/ptyHarvest.ts:21-28) cit:([`PtyTurnHint`], dashboard/src/data/ptyHarvest.ts:13-19)
- **The store**: zustand vanilla, `bySession` keyed by sessionId with the
  copy-on-write `withHarvest` helper. `recordBell` sets the pending marker;
  `acknowledgeBell` clears it — **focusing the seat IS the acknowledgment** (the marker exists to
  pull attention there), and it is a no-op without a pending bell (no state churn, L58-L61);
  `recordTitle`/`recordTurnHint` are per-session and independent; `clear` drops a session's
  harvest. cit:([`ptyHarvestStore`], dashboard/src/data/ptyHarvest.ts:51-73) cit:([`withHarvest`], dashboard/src/data/ptyHarvest.ts:42-49)
- **Pure OSC parsers** (unit-tested; xterm stays out of jsdom):
  - cit:([`parseOsc133`], dashboard/src/data/ptyHarvest.ts:85-91) — FinalTerm shell-integration marks: `A`/`B` → `prompt`,
    `C` → `command-running`, `D[;exit]` → `command-finished`; anything else → null — never a
    fabricated hint.
  - cit:([`parseOsc94`], dashboard/src/data/ptyHarvest.ts:98-110) — ConEmu progress: `4;st;pr` with st 0 → `progress-done`,
    active states → `progress` with the percent clamped to 0–100 (indeterminate st 3 → no
    percent). xterm's handler registration strips the leading `9`, so `data` starts at `4;…`;
    non-progress OSC 9 payloads (e.g. notifications) → null.
  - cit:([`turnHintWord`], dashboard/src/data/ptyHarvest.ts:113-126) — the dim, clearly-hint-labeled words the rail tooltip
    renders (`at prompt`, `command running`, `progress 42%`, …).

### Invariants And Boundaries

- Observe-only: the xterm handlers that feed this store `return false` so sequences still reach
  the terminal untouched; nothing here writes to the PTY.
- Harvested facts are HINTS with explicit labels — they must never feed `stateGrammar` or the
  rail's grammar dot (the reviewer's "dot stays pure grammar" case pins this).
- Wired for the legacy-raw archetype only; controlled panes' truth is the runner line-log.

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
| Store, parsers, and hint vocabulary. | `ptyHarvestStore`, `parseOsc133`, `parseOsc94`, `turnHintWord` | dashboard/src/data/ptyHarvest.ts:51-73; dashboard/src/data/ptyHarvest.ts:85-91; dashboard/src/data/ptyHarvest.ts:98-110; dashboard/src/data/ptyHarvest.ts:113-126 |
| The xterm-side hooks (onBell/onTitleChange/OSC 133/OSC 9), observe-only. | `TerminalStreamHooks` | dashboard/src/panels/Terminal.tsx:107-115 |
| The archetype gate (hooks only when NOT controlled) + acknowledge-on-focus. | `PtySurface` | dashboard/src/panels/session-cockpit/PtySurface.tsx:136-336 |
| The rail consumers: bell attention marker + labeled tooltip hints. | `SessionRail` | dashboard/src/panels/session-cockpit/SessionRail.tsx:487-1102 |
| The grammar this store must never feed. | `seatVisualState` | dashboard/src/data/stateGrammar.ts:101-125 |
| The unit suite: parser matrices, clamps, no-fabrication, bell/ack semantics. | "parseOsc133 (shell-integration marks)", "parseOsc94 (ConEmu progress)", "turnHintWord", "harvest store" | dashboard/src/data/ptyHarvest.test.ts:11-23; dashboard/src/data/ptyHarvest.test.ts:25-37; dashboard/src/data/ptyHarvest.test.ts:39-44; dashboard/src/data/ptyHarvest.test.ts:46-70 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 10 citations (four local prose citations and six repository-internal references); existing parser prose citations were already current.
- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R7: the client-side legacy-raw harvest
  store (bell/ack-on-focus, OSC 0/2 title, turn hints) + the pure OSC 133 / OSC 9;4 parsers and
  the labeled hint words — hints beside the grammar, never grammar states; wired only for the raw
  archetype. Verification metadata pinned to the leaf base until closeout stamps the L6 code
  commit.
