# dashboard/src/panels/engine-room/DiagnosticsPanel.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/DiagnosticsPanel.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-23T13:45+02:00                           |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`       |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `CommitRow` formats branch/commit + absent/dirty/behind flags behind a `factChip` | `CommitRow` | dashboard/src/panels/engine-room/DiagnosticsPanel.tsx:19-38 |
| `DiagnosticsPanel` derives `poweringDown`, builds `setupLine`, renders facts, phases, seed, actions, missing facts, sources | `DiagnosticsPanel` | dashboard/src/panels/engine-room/DiagnosticsPanel.tsx:40-146 |
| `poweringDown` flag (`cleanup-pending`/`abandoned`) drives the "powering down" setup line and the muted `◦` completed-phase glyph (5k F3) | "const poweringDown = node.phase" | dashboard/src/panels/engine-room/DiagnosticsPanel.tsx:52-52 |
| `EngineProcessNode` / `CommitRefNode` / `ProcessFactState` source shapes | `EngineProcessNode`, `CommitRefNode`, `ProcessFactState` | dashboard/src/types/projection.ts:41-41; dashboard/src/types/projection.ts:111-119; dashboard/src/types/projection.ts:162-202 |
| `Affordance` display-only action button (aria-disabled, no POST) | `Affordance` | dashboard/src/grammar/Affordance.tsx:27-42 |
| `GateResponder` compact worktree-gate control. | `GateResponder` | dashboard/src/panels/GateResponder.tsx:720-780 |
| `fmtWait` formats `heartbeatAgeSeconds` into s/m/h/d | `fmtWait` | dashboard/src/data/selectors.ts:108-114 |
| `factChip`, `diagPanel`, `diagRow`, `diagKey`, `diagValue`, `missingNotice`, `missingTitle`, `phaseLineList`, `actionRow`, `sectionLabel` recipes | `factChip`, `diagPanel`, `diagRow`, `diagKey`, `diagValue`, `missingNotice`, `missingTitle`, `phaseLineList`, `actionRow`, `sectionLabel` | dashboard/src/panels/engine-room/layout.styles.ts:526-526; dashboard/src/panels/engine-room/layout.styles.ts:260-260; dashboard/src/panels/engine-room/layout.styles.ts:536-536; dashboard/src/panels/engine-room/layout.styles.ts:543-543; dashboard/src/panels/engine-room/layout.styles.ts:544-544; dashboard/src/panels/engine-room/layout.styles.ts:546-546; dashboard/src/panels/engine-room/layout.styles.ts:556-556; dashboard/src/panels/engine-room/layout.styles.ts:563-563; dashboard/src/panels/engine-room/layout.styles.ts:579-579; dashboard/src/panels/EngineRoom.tsx:39-39 |

## L23 Source-Lineage Diagnostic

When `node.sourceLineage` is present the panel renders its aggregate state and
uses the server summary as title text. The row is presentation-only: it neither
compares branches nor chooses a recovery, and it disappears for processes with
no applicable lineage projection.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented the optional read-only lineage diagnostic row; verification remains closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 6 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-06-23T13:45+02:00 — Task 11: added `lifecycleId`/`gateNode` props. Worktree-bound projected
  gates render compact `GateResponder` in the action row; ordinary action availability still renders
  through display-only `Affordance`. Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-21T23:35 — Slice 5k F3: documented the frontend-derived `poweringDown` flag (`node.phase ∈ {cleanup-pending, abandoned}`). During power-down the setup line reads "powering down · <phase>" instead of the provider/heartbeat line, and completed-phase lines de-emphasize from mint `✓` to muted `◦`. Derived on the frontend because the pre-05m runtime sends no power-down signal; presentation-only (no fact recompute). Added the flag reference row and refreshed the panel-body line range.
- 2026-06-15T19:35 — Created for slice 5e: facts + missing observability + display-only Affordance actions + source files. Verification metadata pinned until closeout stamps the 5e code commit.
