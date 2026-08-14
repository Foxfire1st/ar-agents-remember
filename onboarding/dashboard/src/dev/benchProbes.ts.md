# dashboard/src/dev/benchProbes.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/benchProbes.ts`               |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-31T16:10+02:00                           |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038`       |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **browser-side bench contract**, declared once for both sides that use it.

`/dev/bench` and `/dev/pty-bench` install probes on `window` so the Playwright drivers can
read what the app actually did. That makes those globals an interface between **two
TypeScript projects**: the app installs them (`cockpitScenarios.ts`, `PtyRenderBench.tsx`),
the drivers in `e2e/`, `e2e-chats/`, `e2e-production/` and `perf/` read them. Declaring the
shapes in either project alone leaves the other reading `any` or hand-copying the fields,
which is how the two halves drift.

This module is type-only. It emits nothing and has **no imports at all** — deliberately, so
that `tsconfig.driver.json` can name it directly and the driver program gains the `Window`
augmentation without pulling the app's module graph in behind it.

## Code Commentary

### What It Declares

| Export | Consumer |
| --- | --- |
| `CockpitBenchRequest` | one request the bench fetch stub intercepted, in issue order |
| `CockpitResetAudit` | the cockpit state a scenario reset must restore, captured for comparison |
| `CockpitBenchTransition` | `"launch-failures" \| "set-turn-ended" \| "defer-next-open" \| "release-open"` — the steps a driver can drive a scenario through mid-test |
| `CockpitBenchProbe` | the `window.__cockpitBench` object: counts, request log, launched ids, `snapshot()`, `advance()` |
| `PtyFrameStats` | one rAF measurement run, including `longFrames` (> 33.4 ms, two 60 Hz budgets — the visible-jank count) |
| `PtySerializeProbe` | the `@xterm/addon-serialize` reattach measurement |
| `PtyBenchProbe` | the `window.__ptyBench` object: `{done, stats?, serialize?, error?}` |

The single `declare global { interface Window { … } }` block augments `window` with
`__cockpitBench`, `__cockpitBenchResetAudit`, `__ptyBench` and `__ptyBenchCols` (per-pane
REAL column counts, read by the ~80-col floor verification).

### Where The Declarations Came From

All of it moved here in 260731-EFA-L2; none of it is new behaviour. `CockpitBenchProbe`,
`CockpitBenchTransition`, `CockpitBenchRequest`, `CockpitResetAudit` and the
`__cockpitBench`/`__cockpitBenchResetAudit` augmentation were exported from
`cockpitScenarios.ts`; `FrameStats`, `SerializeProbe` and the `__ptyBench`/`__ptyBenchCols`
augmentation were **file-local** to `PtyRenderBench.tsx` (the two interfaces are now named
`PtyFrameStats` and `PtySerializeProbe`). Both files now import the types from here, and
neither declares a `Window` augmentation any more.

`dashboard/tsconfig.driver.json` lists `"src/dev/benchProbes.ts"` as its only `src/` entry,
alongside the four Playwright config files and the four driver directories.

## Invariants And Boundaries

- **Type-only, and import-free on purpose.** Adding an import here pulls the app's module
  graph into the driver TypeScript project, which is the exact coupling the split avoids.
- This is a contract between two tsconfig projects. A field added on the app side without
  adding it here leaves the drivers reading a stale shape; a field removed here breaks the
  app side at compile time, which is the intended direction.
- DEV-only. `/dev/*` is lazy-loaded and statically dropped from the production bundle; these
  globals do not exist in a shipped build.
- The `Window` augmentation must stay in exactly one file. Two augmentations of the same
  property in one program is the drift this module was created to end.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `cockpitScenarios.ts` imports `CockpitBenchProbe` + `CockpitResetAudit` from this type-only module. | "./benchProbes" | dashboard/src/dev/cockpitScenarios.ts:33-33 |
| `cockpitScenarios.ts` installs the `window.__cockpitBench` probe used by the browser drivers. | "window.__cockpitBench =" | dashboard/src/dev/cockpitScenarios.ts:780-780 |
| `cockpitScenarios.ts` installs the `__cockpitBenchResetAudit` reset-audit surface. | `__cockpitBenchResetAudit` | dashboard/src/dev/cockpitScenarios.ts:293-293 |
| `PtyRenderBench.tsx` imports `PtyFrameStats` + `PtySerializeProbe` from this type-only module. | "./benchProbes" | dashboard/src/dev/PtyRenderBench.tsx:7-7 |
| `PtyRenderBench.tsx` installs the initial `window.__ptyBench` probe state. | "window.__ptyBench = { done: false" | dashboard/src/dev/PtyRenderBench.tsx:100-100 |
| `PtyRenderBench.tsx` installs the real-column-count `__ptyBenchCols` surface. | `__ptyBenchCols` | dashboard/src/dev/PtyRenderBench.tsx:154-154 |
| The driver TypeScript project includes this file. | "src/dev/benchProbes.ts" | dashboard/tsconfig.driver.json:21-21 |

## Update History

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: applied reviewer verdict D1-D25 deterministic whole-claim repairs; corrected operative source ranges and focused assertions, removed the false Pi gate-field claim, and rechecked this card through the locked exact-document fixer/check.

- 2026-07-31T16:10+02:00 — Created for 260731-EFA-L2. The probe interfaces and the single
  `Window` augmentation were extracted here from `cockpitScenarios.ts` and
  `PtyRenderBench.tsx` so the app and the Playwright driver tsconfig project read one
  declaration instead of two (or one plus `any`). No runtime behaviour moved. Verification
  metadata is pinned to the leaf's reformat commit until closeout stamps the code commit.
