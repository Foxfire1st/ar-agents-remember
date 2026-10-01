# dashboard/src/data/ptyHarvest.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Store, parsers, and hint vocabulary. [1]
- The xterm-side hooks (onBell/onTitleChange/OSC 133/OSC 9), observe-only. [2]
- The archetype gate (hooks only when NOT controlled) + acknowledge-on-focus. [3]
- The rail consumers: bell attention marker + labeled tooltip hints. [4]
- The grammar this store must never feed. [5]
- The unit suite: parser matrices, clamps, no-fabrication, bell/ack semantics. [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
