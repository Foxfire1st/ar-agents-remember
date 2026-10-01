# dashboard/src/panels/FlowTab.test.tsx

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

The updated fixture path exercises a bound command seat with repository+sprint provenance. This
keeps the flow projection consistent with production named-seat creation and prevents the test
suite from normalizing an unbound global architect as the ordinary case.

Twelve `it` cases under one `describe` (`FlowTab canvas (unified l-01-agent-lifecycles)`),
`afterEach(cleanup)`; no mocking — FlowTab has no lazy xterm or store dependency, so it renders
straight into jsdom.

- **default router** — a bare `<FlowTab />` reports `data-model="router"`, shows the unified-skill
  title, and asserts the retired `build-job`/`frame` models are gone from the nav.
- **nav switching** — clicking `flow-nav-orchestrator` flips `data-model` and `aria-checked`;
  a further click to `flow-nav-comms` switches again — the radiogroup drives the shown model.
- **initialModel + fallback** — `initialModel="manager"` renders the manager model; an unknown id
  falls back to `router` (`FLOW_MODELS[0]`).
- **per-model render census** — iterates `FLOW_MODELS` (9 models since 260707-HFX-L6) and asserts the
  DOM counts derived from the registry hold: `flow-gate` == nodes with `rides`, `flow-node` ==
  non-gate nodes, `flow-rundown` == rundown segments.
- **router invariants** — three conditions/no fourth entry, fail-closed unknown-role/incomplete
  hosted identity, the task-doc → branch → worktree ladder, chat-is-never-a-build-route, and
  developer-facing sessions routing to the sprint-bound architect launcher.
- **architect (HFX-L6)** — the developer-facing owner/drawing-board/decision-relay model, backend
  decision-item relay, and horizontal role expansion.
- **orchestration invariants** — the master-granular DAG rule, the branch-not-worktree intent, the
  backend decide-by-packet-carried-gateId handover; comms ladder through architect + bird's-eye-only
  spirit test for backend orchestrator or architect; manager reopen-not-redo + the enclosure-addressed raise.
- **strategist (260703-L12/HFX-L6)** — the mandatory pre-run gate (`no orchestration task, no
  orchestrated run`), the single-master pass, the cited-edges/blast-radius method line, the
  unplannable-as-scoped junction, and the backend-orchestrator adoption node.
- **three-party-loop invariants (260703-L12)** — manager tier scoring + the 3-full-round cap with
  the non-shrinking-round escalation; comms quo-vadis line; reviewer criteria-catalog binding +
  delta-verify loop-seat reuse; worker builder-resume line; orchestrator strategist pre-run +
  visible-behavior-first reviewable-environment handover.
- **worker** — brief-started, NEVER git commit, owning seat runs closeout → integrate → finalize.
- **designer** — the hat the architect pulls; `ask — never fill silently`.
- **reviewer** — verdicts-are-evidence with `requireReviewerVerdictAtSeams`, the backend
  orchestrator master-exit decider, all four reviewer task-altitude/parent mappings, and
  `⟁ block? → decomposable fix leaves`.

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

## Evidence

### Repo-Internal References

- The renderer + nav under test (default model, nav radiogroup, initialModel fallback, segment counts). [1]
- The registry the census derives expectations from and whose invariant prose the suite asserts. [2]

As of the 260703-L8 remediation the tests asserted the then-converged canvas: router default + retired models absent from the nav, the ladder and no-chat-builds invariants on the ROUTER drawing, the branch-not-worktree intent and delegated handover decision on the coordination event loop, reopen-not-redo on the manager, brief-started/no-machinery worker, hat-framed designer, and the ruled deciders on the reviewer. Cycle 6 pinned the ruled seam channel verbatim: the coordination assertion matched decide-by-packet-carried-gateId, and a manager assertion matched the gateId-rides-the-packet raise line. Cycle 7 adds a manager assertion pinning the raise node's enclosure address (`enclosure="<master task name>" — the exact address integration enforcement matches the gate by`).
