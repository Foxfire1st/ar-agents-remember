# dashboard/src/dev/PtyRenderBench.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/PtyRenderBench.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-31T16:10+02:00                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The **PTY renderer measurement harness** (260715-FEUI-L6 S1, master OQ-B): `/dev/pty-bench`
mounts N concurrent REAL `Terminal` panes — the exact component the cockpit mounts, fit addon and
all — fed a synthetic runner line-log through the dev mock socket, and measures
`requestAnimationFrame` deltas. This is the in-repo, re-derivable source of the numbers behind
the `PTY_RENDERER = "dom"` decision (recorded in `PtySurface.tsx` and the L6 worker report): DOM
held a locked 60 Hz budget at 12 concurrent panes; webgl (software GL in headless) degraded and
additionally costs one GPU context per pane against the browser's live-context cap. The same page
runs the `@xterm/addon-serialize` reattach evaluation (`?probe=serialize&lines=5000`: a
5000-line buffer → ~234 KB serialized in ~27 ms, restored by `write()` in ~23 ms — cheap enough
to adopt, deliberately NOT enabled in product code).

## Code Commentary

### The Probe Shapes Are No Longer Declared Here

260731-EFA-L2 moved the file-local `FrameStats` and `SerializeProbe` interfaces and the
`declare global { interface Window { … } }` block out to
[`benchProbes.ts`](benchProbes.ts), where they are `PtyFrameStats` and `PtySerializeProbe`.
This file now imports them as types and declares no globals of its own.

The reason is a project boundary, not tidiness: `perf/cockpit.perf.spec.ts` reads
`window.__ptyBench` from the **driver** tsconfig project (`tsconfig.driver.json`), which
does not include the app's module graph. With the augmentation living in a `.tsx` the driver
never compiles, the driver read `any` or hand-copied the fields. `benchProbes.ts` has no
imports so the driver project can name it directly.

**Nothing measured changed.** Every number, query parameter, probe and surface below is as
it was; the line citations were re-anchored (the extraction removed ~28 lines from the top of
the file).

### Logic

- **Query-parameterized run** cit:([`PtyRenderBench`], dashboard/src/dev/PtyRenderBench.tsx:83-164): `?panes=` (default 12), `?renderer=dom|webgl`,
  `?rate=` lines/s/pane (default 20), `?seconds=` measurement window (default 10), `?settle=`
  pre-measure settle (default 3), `?probe=serialize&lines=N` for the serialize path.
- **`measureFrames`** cit:([`measureFrames`], dashboard/src/dev/PtyRenderBench.tsx:18-41): rAF-delta collection over the window → `frames`, `meanMs`,
  `p95Ms`, `maxMs`, and `longFrames` (> 33.4 ms — two 60 Hz budgets, the visible-jank count).
  Its return type is `Omit<PtyFrameStats, …>` against the shared declaration.
- **`runSerializeProbe`** cit:([`runSerializeProbe`], dashboard/src/dev/PtyRenderBench.tsx:43-81): lazily imports `@xterm/xterm` + `@xterm/addon-serialize`,
  fills an off-screen raw xterm with `lines` buffer lines from `RUNNER_LINE_LOG_STREAM`, times
  ONE `serialize()` pass and one restore-`write()` into a fresh terminal (the reattach path),
  returns `{bufferLines, serializedBytes, serializeMs, restoreMs}`.
- **Results surface** (L100-L123, L135-L137): stats land on `window.__ptyBench`
  (`{done, stats?|serialize?|error?}`) for the driver's `waitForFunction`, AND render into
  `data-testid="pty-bench-results"` for scraping; per-pane REAL column counts land on
  `window.__ptyBenchCols` via each pane's cit:([`onResizeCols`], dashboard/src/dev/PtyRenderBench.tsx:153-154) — the R8 ~80-col floor
  verification reads these.
- **The constrained grid** cit:(["repeat(4, minmax(0, 1fr))"], dashboard/src/dev/PtyRenderBench.tsx:138-160): `repeat(4, minmax(0, 1fr))` — `minmax(0,…)` is
  deliberate: xterm's canvas must never inflate a track to min-content, so panes get REALLY
  squeezed (the bug fixed during the L6 run; also exactly what the floor verification needs).
  Each 220px-tall cell mounts `<Terminal sessionId="bench-N" renderer={…}>` under a
  `TerminalSocketContext.Provider` carrying `benchLineLogSocketFactory(rate)`.

### Invariants And Boundaries

- DEV-only — `/dev/*` is lazy-loaded and statically dropped from the production bundle.
- The panes must stay the REAL `Terminal` component: the measurement's whole value is that it
  exercises the shipped fit/renderer path, not a lookalike.
- **`window.__ptyBench` and `window.__ptyBenchCols` are declared in `benchProbes.ts`, not
  here.** Re-adding a local `declare global` for either would give the app and the driver
  project two declarations of one property, which is the drift the extraction removed.
- **Driver relationship:** the sweep is driven by `dashboard/e2e/ptyRenderBench.mjs` — a plain
  node script (NOT a Playwright spec; never collected by `npm run e2e`) that walks the six
  (renderer × panes) cells at 1600×1000 headless Chromium plus the serialize probe. The driver
  header carries the recorded caveat: headless Chromium renders WebGL through **SwiftShader
  (software GL)** — the webgl rows measure software GL; the DOM rows are hardware-honest, and the
  decision logic leans on DOM adequacy + the per-pane WebGL context budget, never on beating
  software GL. (The e2e driver has no card of its own — `dashboard/e2e/` is outside the
  onboarding convention — so this card is its documentation anchor.) Reproduce:
  `npm run dev` then `node e2e/ptyRenderBench.mjs`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Query params, rAF measurement, serialize probe, `__ptyBench`/`__ptyBenchCols` installation, the minmax grid. | `measureFrames` | dashboard/src/dev/PtyRenderBench.tsx:18-41; dashboard/src/dev/PtyRenderBench.tsx:43-81; dashboard/src/dev/PtyRenderBench.tsx:84-91; dashboard/src/dev/PtyRenderBench.tsx:100-123; dashboard/src/dev/PtyRenderBench.tsx:138-160 |
| The shared declaration of `PtyFrameStats`, `PtySerializeProbe` and the `Window` augmentation this file installs into. | `PtyFrameStats` | dashboard/src/dev/benchProbes.ts:57-90 |
| The line-log content + configurable-rate mock socket factory the panes consume. | `benchLineLogSocketFactory` | dashboard/src/dev/lineLogFixture.ts:22-22; dashboard/src/dev/lineLogFixture.ts:89-90 |
| The real pane component under measurement (renderer prop, `onResizeCols`). | `onResizeCols` | dashboard/src/panels/Terminal.tsx:61-61 |
| The decision record the numbers feed (`PTY_RENDERER = "dom"` + measured summary). | `PTY_RENDERER` | dashboard/src/panels/session-cockpit/PtySurface.tsx:39-39 |
| The `/dev/pty-bench` route mount. | `PtyRenderBench` | dashboard/src/dev/DevApp.tsx:15-15 |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: converted the 4 superseded prose
  citations to cit form (query params `PtyRenderBench`, `measureFrames` 18-41, `runSerializeProbe`
  43-81, the minmax grid 138-160) and normalized the 6 reference rows with anchors. Zero findings
  remain.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2: the `FrameStats`/`SerializeProbe` interfaces and the
  `Window` augmentation for `__ptyBench`/`__ptyBenchCols` moved out to `benchProbes.ts` (as
  `PtyFrameStats`/`PtySerializeProbe`) so the Playwright driver tsconfig project reads one
  declaration instead of `any`. No measurement, query parameter or probe changed; line
  citations re-anchored after the ~28-line extraction. Verification metadata is pinned to the
  leaf's reformat commit until closeout stamps the code commit.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 S1 (master OQ-B): the renderer measurement
  harness — N real Terminal panes on a mock line-log firehose, rAF-delta stats on
  `window.__ptyBench`, per-pane real cols on `window.__ptyBenchCols` (R8), the minmax(0,1fr)
  squeeze grid, and the serialize reattach probe; driven by the un-carded
  `dashboard/e2e/ptyRenderBench.mjs` node script (SwiftShader caveat recorded there and here).
  Verification metadata pinned to the leaf base until closeout stamps the L6 code commit.
