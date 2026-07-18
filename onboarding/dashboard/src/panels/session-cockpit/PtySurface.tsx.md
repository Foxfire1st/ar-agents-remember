# dashboard/src/panels/session-cockpit/PtySurface.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/PtySurface.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **PTY stage surface** (260715-FEUI-L6 R1–R3/R7/R8, design §1.4): the session stage's terminal
half, filling L1's pty placeholder WITHOUT moving its zone contract (`data-kbzone="pty"`). Wraps
the EXISTING lazy `Terminal.tsx` in keep-alive layers (Chats' exact `mountedSessionIds` /
display:none / aria-hidden pattern — scrollback and PTY winsize survive focus switches; fit rules
stay in Terminal.tsx UNCHANGED). Carries the measured renderer decision
(**`PTY_RENDERER = "dom"`**, master OQ-B) and the TWO-ARCHETYPE truth: controlled sessions show
the runner's line-log; legacy raw (`unsupported`) sessions host the actual vendor TUI — and ONLY
those panes get byte-stream harvesting hooks.

## Code Commentary

### Logic

- **Renderer decision record** (L24-L34): the comment IS the record — measured on
  `/dev/pty-bench` (headless Chromium, 20 line-log writes/s/pane, 10 s rAF windows): DOM holds a
  locked 60 Hz budget at 1/6/12 concurrent panes (mean ~16.7 ms, zero >33 ms frames); webgl there
  runs on SwiftShader (software GL — the honest caveat) and collapses at 12 panes, but the
  decision does NOT rest on that race: DOM already meets the budget, and `@xterm/addon-webgl`
  allocates one GPU context PER PANE against a browser cap of ~8–16 live contexts — fleet scale
  is where webgl loses by construction. webgl stays a lazy escalation path behind this constant
  (Terminal falls back to DOM on load failure/context loss).
- **Keep-alive layers** (L121-L137): every seat focused in this cockpit joins `mountedIds` and
  stays mounted hidden (`display:none` + `aria-hidden`) while it remains inspectable
  (`running`/`landed` — L106-L108); tombstones PRUNE (a terminated seat's pane and its WS are
  torn down, not hidden forever). Uncapped, like Chats — an LRU cap is where the serialize addon
  plugs in later (worker-report verdict).
- **Two archetypes per pane** (L153-L210): `isControlledSession` (lifecycleCopy) switches
  `data-pty-archetype="controlled"|"legacy-raw"`; harvesting `hooks` (onBell/onTitle/OSC 133/9)
  are passed ONLY for legacy raw (`controlled ? undefined : {…}` — L188-L205, R7); the pane
  chrome names the archetype honestly (`paneArchetypeCopy`, L228-L230).
- **Bell acknowledge-on-focus** (L139-L142): focusing a seat clears its harvested bell marker —
  the marker exists to pull attention here.
- **R8 real-cols wiring** (L144-L149, L183-L185): the VISIBLE pane's `onResizeCols` feeds
  `onVisibleCols` (→ SessionsView's `pane N cols (< 80)` floor chip); reset to `null` on focus
  switch so a fresh fit reports.
- **Freshness writes** (L176-L182): `onSocketState` → `setPtyWs`; `onOutput` → `recordPtyOutput`
  throttled to 1 s/pane (`OUTPUT_STAMP_INTERVAL_MS`).
- **Reserved-chord filter** (L101-L104, L175): `reservedChordFilter` returns false only for
  BOUND reserved chords (`matchReservedChord`), so xterm declines them up to the window tinykeys
  layer; everything else — including the unbound clipboard chords / Firefox Ctrl+Shift+C —
  passes to the harness untouched (R3 defence-in-depth).
- **Screen-reader toggle** (L119, L235-L245, R2): per-pane chrome button, `aria-pressed`, cost
  named in the title (`SCREEN_READER_MODE_NOTE`), persisted via `usePersistedFlag`
  (`cockpit.sessions.screen-reader-mode`); applied LIVE by Terminal's options mutation — never a
  teardown/reconnect.
- **Reserved badge slot** (L66-L68, L231-L234): `data-slot="scrollback-paused-badge"` stays EMPTY
  until the pane-freeze fields land server-side (260710 deferred spec, fix 2) — never faked.
- **Zone focus handoff** (L215-L225): the `data-kbzone="pty"` root delegates focus to the visible
  pane's terminal host (which delegates into xterm's textarea).

### Invariants And Boundaries

- Fit/keep-alive rules live in Terminal.tsx and must stay byte-compatible for the Chats call
  sites; this file only composes.
- Harvesting hooks must NEVER be wired for controlled panes (the runner line-log carries no
  vendor signals — R7's archetype boundary).
- The renderer constant is a MEASURED decision: flipping it to webgl requires a real-GPU
  datapoint (the bench reproduces one in ~15 s in any real browser).
- The badge slot renders nothing until server truth exists — reserved, never faked.

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
| Renderer record, keep-alive, archetypes, hooks, toggle, slots, focus handoff. | L16-L252 | [PtySurface.tsx](PtySurface.tsx) |
| The wrapped terminal: fit rules, live screenReaderMode, key filter, hooks, cols. | L89-L210 | [../Terminal.tsx](../Terminal.tsx) |
| The archetype predicate + pane copy + accessible name + toggle cost note. | L76-L94 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The harvest store + OSC parsers the legacy-raw hooks feed. | L51-L133 | [../../data/ptyHarvest.ts](../../data/ptyHarvest.ts) |
| The reserved-chord matcher the key filter consults. | L193 | [../../data/keymap/reserved.ts](../../data/keymap/reserved.ts) |
| The freshness fields the socket/output callbacks write. | L56-L81 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The view mounting this surface + the measured-cols floor chip. | L606-L630 | [SessionsView.tsx](SessionsView.tsx) |
| The measurement harness behind the renderer record. | — | [../../dev/PtyRenderBench.tsx](../../dev/PtyRenderBench.tsx) |
| The jsdom suite (Terminal mocked out — xterm never enters jsdom). | L15-L153 | [PtySurface.test.tsx](PtySurface.test.tsx) |

## FEUI-L8 Reviewed Candidate Delta

The keep-alive owner stays mounted when focus is temporarily absent, retaining visited inspectable panes. Landed panes remain read-only; exited/retired rows render `EndedSessionState`; chrome/keyboard-zone behavior is withheld where no inspectable PTY exists.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R1–R3/R7/R8: the keep-alive PTY surface
  wrapping the lazy Terminal (Chats' layer pattern, prune on tombstone only), the measured
  `PTY_RENDERER="dom"` decision with the SwiftShader caveat recorded in place, the two-archetype
  switch with legacy-raw-only harvesting hooks, bell acknowledge-on-focus, the reserved
  scrollback-paused badge slot (empty, never faked), the bound-only reserved-chord filter, the
  persisted live screen-reader toggle with its cost named, and the real-cols wiring for the
  ~80-col floor chip. Verification metadata pinned to the leaf base until closeout stamps the L6
  code commit.
