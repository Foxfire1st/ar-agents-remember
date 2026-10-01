# dashboard/src/panels/session-cockpit/PtySurface.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## 260731-EFA-L8 Change

The react-hooks remediation memoized `inspectableIds` and pinned the effect
dependency array; keep-alive and renderer-by-measurement behavior is unchanged.

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
- **Two archetypes per pane** cit:(["export function PtySurface"], dashboard/src/panels/session-cockpit/PtySurface.tsx:334-334): `isControlledSession` (lifecycleCopy) switches
  `data-pty-archetype="controlled"|"legacy-raw"`; harvesting `hooks` (onBell/onTitle/OSC 133/9)
  are passed ONLY for legacy raw (`controlled ? undefined : {…}` — L188-L205, R7); the pane
  chrome names the archetype honestly cit:(["paneArchetypeCopy"], dashboard/src/panels/session-cockpit/PtySurface.tsx:16-16).
- **Bell acknowledge-on-focus** cit:(["Focusing a seat acknowledges its bell marker"], dashboard/src/panels/session-cockpit/PtySurface.tsx:371-371): focusing a seat clears its harvested bell marker —
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
- **Zone focus handoff** cit:(["export function PtySurface"], dashboard/src/panels/session-cockpit/PtySurface.tsx:334-334): the `data-kbzone="pty"` root delegates focus to the visible
  pane's terminal host (which delegates into xterm's textarea).

### Invariants And Boundaries

- Fit/keep-alive rules live in Terminal.tsx and must stay byte-compatible for the Chats call
  sites; this file only composes.
- Harvesting hooks must NEVER be wired for controlled panes (the runner line-log carries no
  vendor signals — R7's archetype boundary).
- The renderer constant is a MEASURED decision: flipping it to webgl requires a real-GPU
  datapoint (the bench reproduces one in ~15 s in any real browser).
- The badge slot renders nothing until server truth exists — reserved, never faked.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Renderer record, keep-alive, archetypes, hooks, toggle, slots, focus handoff. [1]
- The wrapped terminal: fit rules, live screenReaderMode, key filter, hooks, cols. [2]
- The archetype predicate + pane copy + accessible name + toggle cost note. [3]
- The harvest store + OSC parsers the legacy-raw hooks feed. [4]
- The reserved-chord matcher the key filter consults. [5]
- The freshness fields the socket/output callbacks write. [6]
- The view mounting this surface + the measured-cols floor chip. [7]
- The measurement harness behind the renderer record. [8]
- The jsdom suite (Terminal mocked out — xterm never enters jsdom). [9]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

The keep-alive owner stays mounted when focus is temporarily absent, retaining visited inspectable panes. Landed panes remain read-only; exited/retired rows render `EndedSessionState`; chrome/keyboard-zone behavior is withheld where no inspectable PTY exists.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

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
