# dashboard/src/data/ptyHarvest.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/ptyHarvest.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

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

- **`PtyHarvest` per session** (L21-L28): `bellPending` (+`lastBellAt`) — bell observed and not
  yet acknowledged; `title` — the vendor TUI's own OSC 0/2 window title, a label HINT, never the
  catalog label; `turnHint` — the last parsed `PtyTurnHint`
  (`prompt | command-running | command-finished | progress[percent] | progress-done`, L13-L19).
- **The store** (L51-L73): zustand vanilla, `bySession` keyed by sessionId with the
  copy-on-write `withHarvest` helper (L42-L49). `recordBell` sets the pending marker;
  `acknowledgeBell` clears it — **focusing the seat IS the acknowledgment** (the marker exists to
  pull attention there), and it is a no-op without a pending bell (no state churn, L58-L61);
  `recordTitle`/`recordTurnHint` are per-session and independent; `clear` drops a session's
  harvest.
- **Pure OSC parsers** (unit-tested; xterm stays out of jsdom):
  - `parseOsc133(data, at)` (L85-L91) — FinalTerm shell-integration marks: `A`/`B` → `prompt`,
    `C` → `command-running`, `D[;exit]` → `command-finished`; anything else → null — never a
    fabricated hint.
  - `parseOsc94(data, at)` (L98-L110) — ConEmu progress: `4;st;pr` with st 0 → `progress-done`,
    active states → `progress` with the percent clamped to 0–100 (indeterminate st 3 → no
    percent). xterm's handler registration strips the leading `9`, so `data` starts at `4;…`;
    non-progress OSC 9 payloads (e.g. notifications) → null.
  - `turnHintWord(hint)` (L113-L126) — the dim, clearly-hint-labeled words the rail tooltip
    renders (`at prompt`, `command running`, `progress 42%`, …).

### Invariants And Boundaries

- Observe-only: the xterm handlers that feed this store `return false` so sequences still reach
  the terminal untouched; nothing here writes to the PTY.
- Harvested facts are HINTS with explicit labels — they must never feed `stateGrammar` or the
  rail's grammar dot (the reviewer's "dot stays pure grammar" case pins this).
- Wired for the legacy-raw archetype only; controlled panes' truth is the runner line-log.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Store, parsers, and hint vocabulary. | L13-L126 | [ptyHarvest.ts](ptyHarvest.ts) |
| The xterm-side hooks (onBell/onTitleChange/OSC 133/OSC 9), observe-only. | L178-L189 | [../panels/Terminal.tsx](../panels/Terminal.tsx) |
| The archetype gate (hooks only when NOT controlled) + acknowledge-on-focus. | L141; L186-L208 | [../panels/session-cockpit/PtySurface.tsx](../panels/session-cockpit/PtySurface.tsx) |
| The rail consumers: bell attention marker + labeled tooltip hints. | L389; L450-L467 | [../panels/session-cockpit/SessionRail.tsx](../panels/session-cockpit/SessionRail.tsx) |
| The grammar this store must never feed. | — | [stateGrammar.ts](stateGrammar.ts) |
| The unit suite: parser matrices, clamps, no-fabrication, bell/ack semantics. | L11-L70 | [ptyHarvest.test.ts](ptyHarvest.test.ts) |

## Update History

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R7: the client-side legacy-raw harvest
  store (bell/ack-on-focus, OSC 0/2 title, turn hints) + the pure OSC 133 / OSC 9;4 parsers and
  the labeled hint words — hints beside the grammar, never grammar states; wired only for the raw
  archetype. Verification metadata pinned to the leaf base until closeout stamps the L6 code
  commit.
