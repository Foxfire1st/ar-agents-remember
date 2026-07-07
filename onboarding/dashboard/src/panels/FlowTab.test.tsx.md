# dashboard/src/panels/FlowTab.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/FlowTab.test.tsx`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T15:40+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
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

Eleven `it` cases under one `describe` (`FlowTab canvas (unified l-01-agent-lifecycles)`),
`afterEach(cleanup)`; no mocking — FlowTab has no lazy xterm or store dependency, so it renders
straight into jsdom.

- **default router** — a bare `<FlowTab />` reports `data-model="router"`, shows the unified-skill
  title, and asserts the retired `build-job`/`frame` models are gone from the nav.
- **nav switching** — clicking `flow-nav-orchestrator` flips `data-model` and `aria-checked`;
  a further click to `flow-nav-comms` switches again — the radiogroup drives the shown model.
- **initialModel + fallback** — `initialModel="manager"` renders the manager model; an unknown id
  falls back to `router` (`FLOW_MODELS[0]`).
- **per-model render census** — iterates `FLOW_MODELS` (8 models since 260703-L12) and asserts the
  DOM counts derived from the registry hold: `flow-gate` == nodes with `rides`, `flow-node` ==
  non-gate nodes, `flow-rundown` == rundown segments.
- **router invariants** — three conditions/no fourth entry, the task-doc → branch → worktree
  ladder, and chat-is-never-a-build-route.
- **orchestration invariants** — the master-granular DAG rule, the branch-not-worktree intent, the
  decide-by-packet-carried-gateId handover; comms ladder + ORCHESTRATOR-ONLY spirit test; manager
  reopen-not-redo + the enclosure-addressed raise.
- **strategist (260703-L12)** — the mandatory pre-run gate (`no orchestration task, no
  orchestrated run`), the single-master pass, the cited-edges/blast-radius method line, the
  unplannable-as-scoped junction, and the reader-not-mutator adoption node.
- **three-party-loop invariants (260703-L12)** — manager tier scoring + the 3-full-round cap with
  the non-shrinking-round escalation; comms quo-vadis line; reviewer criteria-catalog binding +
  delta-verify loop-seat reuse; worker builder-resume line; orchestrator strategist pre-run +
  visible-behavior-first reviewable-environment handover.
- **worker** — brief-started, NEVER git commit, owning seat runs closeout → integrate → finalize.
- **designer** — the hat the orchestrator pulls; `ask — never fill silently`.
- **reviewer** — verdicts-are-evidence with `requireReviewerVerdictAtSeams`, the ruled deciders,
  and `⟁ block? → decomposable fix leaves`.

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

As of the 260703-L8 remediation the tests assert the converged canvas: router default + retired models absent from the nav, the ladder and no-chat-builds invariants on the ROUTER drawing, the branch-not-worktree intent and delegated handover decision on the orchestrator, reopen-not-redo on the manager, brief-started/no-machinery worker, hat-framed designer, and the ruled deciders on the reviewer. Cycle 6 pins the ruled seam channel verbatim: the orchestrator assertion now matches `the ORCHESTRATOR decides by the packet-carried gateId`, and a manager assertion matches the gateId-rides-the-packet raise line. Cycle 7 adds a manager assertion pinning the raise node's enclosure address (`enclosure="<master task name>" — the exact address integration enforcement matches the gate by`).

## Update History

- 2026-07-06T15:40+02:00 — 260703-L12 (three-party loops): two new cases — the strategist model (mandatory pre-run gate, cited-edges method, unplannable-as-scoped junction, reader-not-mutator adoption) and the cross-model loop invariants (tier scoring, 3-full-round cap, quo-vadis, criteria-catalog binding, builder/reviewer resume, strategist pre-run + reviewable-environment handover) — 11 tests total; the Logic body was de-staled from the pre-convergence build-job/frame census to the current suite. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: new assertion pins the manager raise node's enclosure address (AR4-4). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: seam-channel assertions updated to the wait=false raise + decide-by-packet-carried-gateId prose (AR3-6a). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): tests rewritten for the converged canvas (9 tests). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T09:40+02:00 — Created for 260703-L0 (Canvas & playground): 8 vitest cases for the FlowTab
  canvas — default model, nav switching + `aria-checked`, `initialModel` + unknown-id fallback, a
  per-model render census (node/gate/rundown DOM counts vs the registry), and verbatim invariant
  assertions (master-granular DAG rule, the two adversarial seams, orchestrator-only spirit test, manager
  escalation, designer adversarial-review handover, frame junction, Wollmilchsau self-id, reviewer
  evidence-not-decisions + decomposable blocks). Verification metadata pinned until closeout stamps the
  L0 commit.
