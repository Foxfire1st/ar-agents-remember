# dashboard/src/panels/FlowTab.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/FlowTab.test.tsx`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-05T16:30+02:00 |
| lastVerifiedCommitHash | `19d76dbd73673ffc72d0ee1b6a868ac2fdf15ad0`       |
| lastVerifiedCommitDate | 2026-07-05T16:23:40+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest + Testing Library coverage for the `FlowTab` design canvas after the 260703-L0 rewrite turned it
from a single hardcoded diagram into a multi-model renderer over the `flowModels.ts` registry. Because
FlowTab is pure and store-free, it is unit-tested directly (no store/backend mocks). The suite pins two
things: the **renderer/nav mechanics** (default model, nav switching + `aria-checked`, `initialModel`
honouring + unknown-id fallback, and a per-model render census that ties DOM node/gate/rundown counts
back to the registry) and the **agreed orchestration invariants** as verbatim on-canvas text, so a prose
edit that drops an invariant from a drawn model fails a test.

## Code Commentary

### Logic

Eight `it` cases under one `describe` (L9), `afterEach(cleanup)` (L7); no mocking — FlowTab has no lazy
xterm or store dependency, so it renders straight into jsdom.

- **default build-job (L10-17)** — a bare `<FlowTab />` reports `data-model="build-job"`, shows the
  build-job title, and still carries the task-26 survivors (`flow-nav` + a `worktree_start --dry-run`
  node).
- **nav switching (L19-28)** — clicking `flow-nav-orchestrator` flips `data-model` to `orchestrator` and
  its `aria-checked` to `"true"` while `flow-nav-build-job` reads `"false"`; a further click to
  `flow-nav-comms` switches again — proving the radiogroup drives the shown model.
- **initialModel + fallback (L30-36)** — `initialModel="manager"` renders the manager model; an unknown
  `initialModel="nope"` falls back to `build-job` (`FLOW_MODELS[0]`).
- **per-model render census (L38-54)** — iterates `FLOW_MODELS` and, for each, asserts `data-model`
  matches and that the DOM counts derived from the registry hold: `flow-gate` count == nodes with
  `rides`, `flow-node` count == non-gate nodes, `flow-rundown` count == `rundown` segments. This is the
  structural guard that the segment renderer draws exactly what each model declares.
- **orchestration invariants (L56-68)** — on `orchestrator`: the master-granular DAG rule
  (`reshape master boundaries — NEVER interleave dispatch`) and exactly **two** `adversarial review seam`
  matches; on `comms`: the escalation ladder text and the **ORCHESTRATOR-ONLY** spirit test; on
  `manager`: `managers don't reshape plans (no bird's-eye)` — i.e. managers escalate, they don't judge.
- **designer (L70-76)** — the designer draws as its own job and names the orchestrator as its adversarial
  reviewer (`ORCHESTRATOR adversarially reviews the design`), plus `ask — never fill silently`.
- **frame (L78-86)** — the frame draws as the thin consistent runtime (`context → job → wrap-up`) with
  the junction where `the JOB's own flow takes over … the frame stays thin`; then switches to build-job
  and asserts it self-identifies as the `Eierlegende Wollmilchsau`.
- **reviewer (L88-94)** — verdicts-are-evidence (`verdicts are evidence, not decisions — a policy may
  REQUIRE a verdict`), the onboarding-vs-code review lens, and the decomposable-blocks outcome
  (`⟁ block? → decomposable fix leaves`).

### Conventions

Pure render/interaction test in the panels suite: it imports both `FLOW_MODELS` (to derive census
expectations from the registry rather than hard-coding counts) and `FlowTab`, and asserts through
`getByTestId` / `getByText` / `getAllByText` on the stable canvas hooks (`flow-tab`, `flow-nav-{id}`,
`flow-node`, `flow-gate`, `flow-rundown`, `data-model`, `aria-checked`). Invariant assertions match the
exact on-canvas prose, so they double as a regression guard on the drawn spec.

### Invariants And Boundaries

- **Registry-driven expectations.** The census case derives counts from `FLOW_MODELS`, so a new model or
  a segment reshape is covered automatically — but a renderer change to the `data-testid` hooks would
  break every case, which is intended (the hooks are the contract).
- **Prose is asserted verbatim.** Several invariant strings are matched literally; editing that copy in
  `flowModels.ts` requires updating the matching assertion here (and vice versa).
- **No store, no network, no xterm.** FlowTab is pure, so the suite mocks nothing; that store-free
  posture is itself part of what these tests protect.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The renderer + nav under test (default model, nav radiogroup, initialModel fallback, segment counts). | L111-L150; L60-L109 | [FlowTab.tsx](FlowTab.tsx) |
| The registry the census derives expectations from and whose invariant prose the suite asserts. | L7-L50; L54-L366; L368 | [flowModels.ts](flowModels.ts) |

As of the 260703-L8 remediation the tests assert the converged canvas: router default + retired models absent from the nav, the ladder and no-chat-builds invariants on the ROUTER drawing, the branch-not-worktree intent and delegated handover decision on the orchestrator, reopen-not-redo on the manager, brief-started/no-machinery worker, hat-framed designer, and the ruled deciders on the reviewer.

## Update History

- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): tests rewritten for the converged canvas (9 tests). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T09:40+02:00 — Created for 260703-L0 (Canvas & playground): 8 vitest cases for the FlowTab
  canvas — default model, nav switching + `aria-checked`, `initialModel` + unknown-id fallback, a
  per-model render census (node/gate/rundown DOM counts vs the registry), and verbatim invariant
  assertions (master-granular DAG rule, the two adversarial seams, orchestrator-only spirit test, manager
  escalation, designer adversarial-review handover, frame junction, Wollmilchsau self-id, reviewer
  evidence-not-decisions + decomposable blocks). Verification metadata pinned until closeout stamps the
  L0 commit.
