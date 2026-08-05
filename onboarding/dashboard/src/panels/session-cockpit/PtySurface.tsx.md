# dashboard/src/panels/session-cockpit/PtySurface.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/PtySurface.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d`       |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
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

- **Renderer decision record** cit:(["export const PTY_RENDERER"], dashboard/src/panels/session-cockpit/PtySurface.tsx:39-39): the comment IS the record — measured on
  `/dev/pty-bench` (headless Chromium, 20 line-log writes/s/pane, 10 s rAF windows): DOM holds a
  locked 60 Hz budget at 1/6/12 concurrent panes (mean ~16.7 ms, zero >33 ms frames); webgl there
  runs on SwiftShader (software GL — the honest caveat) and collapses at 12 panes, but the
  decision does NOT rest on that race: DOM already meets the budget, and `@xterm/addon-webgl`
  allocates one GPU context PER PANE against a browser cap of ~8–16 live contexts — fleet scale
  is where webgl loses by construction. webgl stays a lazy escalation path behind this constant
  (Terminal falls back to DOM on load failure/context loss).
- **Keep-alive layers** cit:(["function reservedChordFilter"], dashboard/src/panels/session-cockpit/PtySurface.tsx:128-128): every seat focused in this cockpit joins `mountedIds` and
  stays mounted hidden (`display:none` + `aria-hidden`) while it remains inspectable
  (`running`/`landed` — L106-L108); tombstones PRUNE (a terminated seat's pane and its WS are
  torn down, not hidden forever). Uncapped, like Chats — an LRU cap is where the serialize addon
  plugs in later (worker-report verdict).
- **Two archetypes per pane** cit:(["export function PtySurface"], dashboard/src/panels/session-cockpit/PtySurface.tsx:136-136): `isControlledSession` (lifecycleCopy) switches
  `data-pty-archetype="controlled"|"legacy-raw"`; harvesting `hooks` (onBell/onTitle/OSC 133/9)
  are passed ONLY for legacy raw (`controlled ? undefined : {…}` — L188-L205, R7); the pane
  chrome names the archetype honestly cit:([`paneArchetypeCopy`], dashboard/src/panels/session-cockpit/PtySurface.tsx:305-305).
- **Bell acknowledge-on-focus** cit:(["Focusing a seat acknowledges its bell marker"], dashboard/src/panels/session-cockpit/PtySurface.tsx:195-195): focusing a seat clears its harvested bell marker —
  the marker exists to pull attention here.
- **R8 real-cols wiring** (L144-L149, L183-L185): the VISIBLE pane's `onResizeCols` feeds
  `onVisibleCols` (→ SessionsView's `pane N cols (< 80)` floor chip); reset to `null` on focus
  switch so a fresh fit reports.
- **Freshness writes** cit:([`lastOutputAt`], dashboard/src/panels/session-cockpit/PtySurface.tsx:42-42): `onSocketState` → `setPtyWs`; `onOutput` → `recordPtyOutput`
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
- **Zone focus handoff** cit:(["export function PtySurface"], dashboard/src/panels/session-cockpit/PtySurface.tsx:136-136): the `data-kbzone="pty"` root delegates focus to the visible
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Renderer record, keep-alive, archetypes, hooks, toggle, slots, focus handoff. | "export function PtySurface" | dashboard/src/panels/session-cockpit/PtySurface.tsx:136-136 |
| The wrapped terminal: fit rules, live screenReaderMode, key filter, hooks, cols. | "export function Terminal" | dashboard/src/panels/Terminal.tsx:117-117 |
| The archetype predicate + pane copy + accessible name + toggle cost note. | "export function cleanupOutcomeCopy" | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:40-40 |
| The harvest store + OSC parsers the legacy-raw hooks feed. | "export interface PtyHarvest" | dashboard/src/data/ptyHarvest.ts:21-21 |
| The reserved-chord matcher the key filter consults. | "export const PTY_RESERVED" | dashboard/src/data/keymap/reserved.ts:62-62 |
| The freshness fields the socket/output callbacks write. | "export type EvidenceTier" | dashboard/src/data/sessionCockpitStore.ts:18-18 |
| The view mounting this surface + the measured-cols floor chip. | "export const SessionsView" | dashboard/src/panels/session-cockpit/SessionsView.tsx:1336-1336 |
| The measurement harness behind the renderer record. | "export function PtyRenderBench" | dashboard/src/dev/PtyRenderBench.tsx:83-83 |
| The jsdom suite (Terminal mocked out — xterm never enters jsdom). | "controlled panes are labeled as the runner line-log and get NO harvesting hooks" | dashboard/src/panels/session-cockpit/PtySurface.test.tsx:54-69 |

## FEUI-L8 Reviewed Candidate Delta

The keep-alive owner stays mounted when focus is temporarily absent, retaining visited inspectable panes. Landed panes remain read-only; exited/retired rows render `EndedSessionState`; chrome/keyboard-zone behavior is withheld where no inspectable PTY exists.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## 260718-CHATS-L4 Reviewed Candidate Delta

An optional `readOnly` prop (default `false`) is added so the L4 terminal-diagnostics drawer can host
the controlled runner line-log input-disabled (design §12.6): when true the surface renders the same
keep-alive pane but declines keystrokes. The legacy-raw and landed call sites are unchanged (default
`false`). Note the broader L4 composition change this prop serves: for a CONTROLLED seat this surface is
no longer the primary stage body — `ChatsStageBody` makes it a default-off, read-only diagnostics drawer
(the `TerminalDiagnosticsDrawer`), while a legacy-raw seat keeps its interactive PTY as the primary body.

The reviewed candidate is uncommitted; existing verification hash/date remain pinned; closeout owns
commit stamping.

## Current L5I Maintenance

The PTY pane no longer reserves a standing chrome bar for archetype text or an empty badge slot.
Archetype context remains available through the inspector and the screen-reader toggle tooltip,
which now floats inside the pane. A hidden layer has no keyboard zone or ended-state focus target,
so focus routing reaches only the currently visible terminal surface.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the superseded `(L…)`
  prose citations and the `n/a` rows with exact anchors and fixer-generated ranges; exact
  non-fixing check returns zero findings.

- 2026-07-24T13:17:17Z — Curator: corrected PTY declutter, retained archetype disclosure, and
  hidden-layer focus invariants; verification fields remain pre-commit.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: recorded the optional `readOnly` prop (default
  false) that lets the terminal-diagnostics drawer host the controlled runner PTY input-disabled
  (§12.6), and noted that for a controlled seat this surface is now a default-off read-only diagnostic
  rather than the primary stage body. Verification metadata remains pinned to the leaf base until
  closeout stamps the L4 commit.
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
