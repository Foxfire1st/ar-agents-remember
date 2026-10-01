# dashboard/src/panels/engine-room/DiagnosticsPanel.tsx

## Governing Overview

[engine-room overview](overview.md)

## Purpose

Renders the diagnostics column for one enclosure pod in slice 5e's Engine Room process map. It presents the server-composed `EngineProcessNode` as read-only facts — phase/health, the four code/memory commit refs with their fact-state honesty, provider-setup progress, completed/failed phases — plus a "Missing observability" notice, action availability, and the contributing source files. Task 11 makes it the Engine Room's secondary gate-response surface: worktree-bound projected gates render compact `GateResponder`; non-gate actions remain display-only affordances. The panel re-derives nothing except one presentation-only `poweringDown` flag (slice 5k F3): during the power-down phases (`cleanup-pending`/`abandoned`) the providers are being torn down, so the diagnostics show "powering down" instead of an "ok" provider line and de-emphasize the now-stale completed-phase lines. That flag is derived from `node.phase` on the frontend because the live runtime is pre-05m and sends no power-down signal of its own.

## Code Commentary

### Logic

Two exports, both presentational (no state, no effects, no mutation).

- `CommitRow({ label, refNode })` formats one `CommitRefNode`. It builds `ref` as `branch @ commit[0:8]` (joined with `·`-style ` @ `, empty parts dropped) and a `flags` string from `exists === false → "absent"`, `dirty → "dirty"`, and `behindSource → "N behind"`. It leads with a `factChip({ factState })` badge showing `refNode.factState`, then `ref || "—"`, then ` (flags)` when any flag is set.
- `DiagnosticsPanel({ node, lifecycleId, gateNode })` is the panel body. It first derives `poweringDown = node.phase === "cleanup-pending" || node.phase === "abandoned"` (slice 5k F3). It then derives `setupLine`: when powering down it joins `"powering down"` and `node.currentPhase`; otherwise it joins `node.setupState`, an optional `heartbeat <fmtWait(heartbeatAgeSeconds)>`, and `node.currentPhase`. It conditionally renders: `node.summary`; always-on Phase (`node.phase`) and Health (`node.health`) rows; an optional Next row (`node.nextAction`); four `CommitRow`s for `codeSource`, `codeWorktree`, and (when present) `memorySource` / `memoryWorktree`; a Provider-setup row when `setupLine` is non-empty; a `phaseLineList` listing `completedPhases` and `failedPhases` (✗, alarm) when either is non-empty — completed lines render as mint `✓` normally but as muted `◦` while `poweringDown` (de-emphasizing the stale, now-torn-down provider/completed-phase lines); a Seed row reading `reroute → reindex fallback` when `node.seedFallback`; an `actionRow` that renders compact `GateResponder` when `lifecycleId` + a worktree-bound `gateNode` are present, otherwise maps `node.actions` to display-only `<Affordance>`; a `missing-facts` notice mapping `node.missingFacts`; and a Sources row joining `node.sourceFiles`.

### Invariants And Boundaries

- Non-gate actions go through `Affordance`, which is `aria-disabled` with no `onClick`/POST. Gate responses
  go through `GateResponder` as chat injections, not local lifecycle mutation.
- Fact honesty is preserved verbatim: the panel never recomputes `factState`; it surfaces the server value through `factChip` and shows `behindSource` as a count (fetch-free), absent/zero meaning current.
- The `poweringDown` flag is a frontend-only presentation decision derived from `node.phase` (no power-down field exists on the pre-05m projection); it only swaps the setup-line text and the completed-phase glyph/colour (`✓` mint → `◦` muted) — it does not drop, recompute, or hide any underlying fact.
- Memory rows are conditional because `memorySource`/`memoryWorktree` are absent on internal/disabled memory modes; optional sections collapse rather than render empty shells.
- `node.actions`, `completedPhases`, `failedPhases`, `missingFacts`, and `sourceFiles` are always arrays; guards use `.length > 0`, so empty collections render nothing.
- `data-testid` hooks (`diagnostics`, `missing-facts`, and `affordance` via the child) are load-bearing for the slice 5e visual/test harness.

## Evidence

### Repo-Internal References

- `CommitRow` formats branch/commit + absent/dirty/behind flags behind a `factChip` [1]
- `DiagnosticsPanel` derives `poweringDown`, builds `setupLine`, renders facts, phases, seed, actions, missing facts, sources [2]
- `poweringDown` flag (`cleanup-pending`/`abandoned`) drives the "powering down" setup line and the muted `◦` completed-phase glyph (5k F3) [3]
- `EngineProcessNode` / `CommitRefNode` / `ProcessFactState` source shapes [4]
- `Affordance` display-only action button (aria-disabled, no POST) [5]
- `GateResponder` compact worktree-gate control. [6]
- `fmtWait` formats `heartbeatAgeSeconds` into s/m/h/d [7]
- `factChip`, `diagPanel`, `diagRow`, `diagKey`, `diagValue`, `missingNotice`, `missingTitle`, `phaseLineList`, `actionRow`, `sectionLabel` recipes [8]

## L23 Source-Lineage Diagnostic

When `node.sourceLineage` is present the panel renders its aggregate state and
uses the server summary as title text. The row is presentation-only: it neither
compares branches nor chooses a recovery, and it disappears for processes with
no applicable lineage projection.
