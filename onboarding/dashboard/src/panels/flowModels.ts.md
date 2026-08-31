# dashboard/src/panels/flowModels.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/flowModels.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-31T04:59+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`       |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The **flow-model registry** for the `FlowTab` design canvas (orchestration leaf 260703-L0): the content
side of the canvas split. `FlowTab.tsx` owns the segment renderer + model nav; **this module owns every
drawn lifecycle/interaction as static data**. Each `FlowModel` is one drawable design — a title, a nav
label, a prose takeaway, and an ordered list of `FlowSegment`s (start / node / rundown / divider) — and
the exported `FLOW_MODELS` array is what the nav switches between. Models are **static design artifacts,
no store reads**: the canvas is the surface where a lifecycle is drawn, reviewed with the developer, and
kept in step with the doctrine (visuals ride every doctrine change). The models draw the **converged
`l-01-agent-lifecycles` doctrine** in a human-readable form, so this file is as much a spec record as a
UI data file. Since HFX-L6 the census is **9 models**: the architect model joins as the
developer-facing owner seat between Router and Designer, while the orchestrator model is explicitly a
spawned backend event loop. The strategist remains the spawn-first sprint planner, and the loop doctrine
(tiers · 3-round cap · convergence · quo-vadis · criteria catalogs) rides the manager/worker/reviewer/comms drawings.

## Code Commentary

### Logic

Flow-model command-seat identity now includes the stored repository+sprint provenance carried by
the terminal catalog. That additive identity lets the panel distinguish equal role names in two
concurrent sprints without inferring scope from labels or global role order.

**Types** cit:([`Status`, `FlowSegment`], dashboard/src/panels/flowModels.ts:9-9; dashboard/src/panels/flowModels.ts:42-42): `Status = "current" | "proposed"` drives edge colour (mint vs amber dashed).
The four segment shapes form the `FlowSegment` union (L42): `FlowStart` (a labelled entry pill +
optional `next`/`nextStatus` edge), `FlowNode` (`phase`, monospace `tool`, optional `detail`,
optional `rides` = the gate/seam whose notification rides this call, optional `ridesNote` overriding the
default rider line, and the outgoing `next`/`nextStatus` edge), `FlowRundown` (a titled card of
`{ line; junction? }` prose lines for non-linear stretches), and `FlowDivider` (a caption).
cit:([`FlowModel`], dashboard/src/panels/flowModels.ts:44-52) bundles `id`, `label`, `title`, `takeaway`, and `segments`.

**The 9 models** (HFX-L6 adds the architect), in `FLOW_MODELS` order: ROUTER · ARCHITECT · DESIGNER ·
STRATEGIST · ORCHESTRATOR · MANAGER · WORKER · REVIEWER · COMMS:

1. **`router`** (`ROUTER`, the default) — the unified skill's spine: the three-condition entry
   (valid hosted `AR_SPAWN_ROLE` → identity-free fresh-session role brief → otherwise free-chat
   launcher) with fail-closed unknown-role/incomplete-hosted-identity admission and
   announce-and-wait only for a valid hosted role missing its brief, the architect's owner
   loop (Design · Decision Relay · Spawn/Supervise + research-only exit), and the invariant ladder —
   task doc (approved) → branch (intent) → worktree (only where something is built), with "chat is
   never a build route" as a junction line.
2. **`architect`** (`ARCHITECT`) — the developer-facing owner seat: design/drawing-board work,
   one-at-a-time decision-item relay over the existing inbox, backend role spawning, and durable
   rulings back to backend seats.
3. **`designer`** (`DESIGNER`) — task design as the HAT the architect pulls (the `tasks/AGENTS.md`
   doctrine: meta-question, reframe-before-execution, evidence-first; the reframe-agreement node's phase
   label is `reframe`, the doctrine word). It is master-scoped, so cross-master/future collisions can
   slip; that residual risk is owned downstream — **at portfolio streamlining the backend orchestrator doubles
   as the designer's adversarial reviewer**.
4. **`strategist`** (`STRATEGIST`) — the spawn-first sprint planner: the
   **mandatory pre-run gate** rundown (no orchestration task, no orchestrated run; even a single master
   gets the pass; the re-evaluation junction), the **eight-phase method** rundown (two-sided touch
   surfaces, cgc/grepai edge list, cited doctrine edges, blast-radius register feeding loop-tier
   scoring, coherence sweep, ordering; the unplannable-as-scoped junction), the ORCHESTRATION TASK
   deliver node, the plan-review gate node (the portfolio three-party loop), the drawing-board
   convergence node through the architect, and the reader-not-mutator adoption node.
5. **`orchestrator`** (`ORCHESTRATOR`) — the spawned backend event loop drawn on its biggest run
   (Job O): trust
   checkpoint + portfolio orientation, profile-fit/takeover, the non-linear **portfolio phase**
   (streamline before sequencing, now closing on the STRATEGIST pre-run line → the orchestration
   task), the **master-granular dependency DAG** rule (`⟁ … reshape master
   boundaries — NEVER interleave dispatch`), the super-branch INTENT (a branch, not a worktree), the
   dependency-ordered dispatch loop, the decide-by-packet-carried-gateId handover node, per-edge
   integration worktrees, the super-exit seam, the architect-mediated developer SINGLE review point
   drawn **visible-behavior-first in a reviewable environment (the dashboard) with demo notes**, and
   the grounded self-improvement report at close.
6. **`manager`** (`MANAGER`) — one master, the leaf dispatch loop, review-vs-task_doc with
   `task_reopen`-the-same-leaf, **delegated attributed leaf gates** (`decidedBy: manager lifecycle ·
   decidedVia: orchestration`, the owning agent never self-approves), C-11 leaf→master integration, the
   master-exit seam, and the non-blocking RAISE of `master-handover-approval` (`wait=false`,
   `enclosure="<master task name>"`, the returned gateId riding the packet). Managers **escalate plan
   deltas** rather than judge them ("managers don't reshape plans (no bird's-eye)"); since L12 the
   intake rundown scores each leaf's **loop tier** (direct · builder-verified · full loop, the
   strategist's blast-radius register as input) and carries the 3-full-round cap + convergence
   escalation junction.
7. **`worker`** (`WORKER`) — brief-started (the brief IS the session start), one per leaf: intake →
   orient (paired reads) → build (same-pass onboarding, NEVER git commit) → checks green → the
   **mandatory turn-report artifact**; no lifecycle machinery — closeout/integrate/finalize belong to
   the owning seat; since L12 a loop-position line marks it the loop's BUILDER (fix rounds resume the
   same session; reports append).
8. **`reviewer`** (`REVIEWER`) — one role across four structural seats: leaf route/full-loop under
   its manager, master-exit under its manager, portfolio plan under the architect, and super-exit
   under the orchestrator. Its generation records the exact parent document+role; three-lens review
   (completion vs task docs · code quality per tools.md · onboarding-vs-code); its **verdict is evidence,
   not a decision** (attaches to the handover gate as judge evidence), and a blocking verdict must
   **decompose into fix leaves**, never prose complaints; since L12 the lens rundown binds the
   **criteria catalogs** (five, per review type) and the loop-seat-reuse line (delta-verifies resume
   the same reviewer and close rounds).
9. **`comms`** (`COMMS`) — the channels (inbox = queue · stdin push = delivery · artifacts =
   reporting · chats = walk-in), the nudge loop, the **escalation ladder** (worker → manager →
   orchestrator → architect → developer, no level skipped), the loop cap/convergence line, the
   **quo-vadis junction** (a high-blast-radius truth escalates to the architect relay immediately;
   presentation-grade never), the **bird's-eye-only spirit test** for backend orchestrator or architect, and the single **one-schema
   handover packet** serving master handover / role takeover / worker respawn.

### Conventions

Plain TypeScript data module — no React, no styling, no store. Each model is a `const` typed as
`FlowModel`, and cit:([`FLOW_MODELS`], dashboard/src/panels/flowModels.ts:451-451) is the ordered export the nav renders; `FLOW_MODELS[0]`
(`ROUTER`) is FlowTab's default/fallback, so ordering is load-bearing for the default view. Prose
carries the series' typographic conventions (`⟁` for a junction/decision, `⊘` for a gate/seam rider,
`·` separators, mint/amber via `nextStatus`). A gate/seam node sets `rides`; when it needs a bespoke
rider line (a seam, a delegated gate, judge evidence, a reframe) it also sets `ridesNote`, overriding
FlowTab's default auto-fire notification text.

### Invariants And Boundaries

- **Content-only, static, no store reads.** Everything here is authored design data; the module imports
  nothing and reads no runtime state. Reshaping a drawn lifecycle happens here, not in the renderer.
- **The registry is a spec record.** The models encode the converged doctrine's agreed invariants (the
  router three-condition entry with no fourth; the task-doc → branch → worktree ladder with no chat
  builds; architect as the developer-facing owner seat; the bird's-eye-only spirit test for backend orchestrator or architect; the
  worker → manager → orchestrator → architect → developer escalation
  ladder; exactly two adversarial seams; the master-granular DAG / never-interleave-dispatch rule;
  delegated attributed gates where the owning agent never self-approves;
  verdicts-are-evidence-not-decisions; mandatory turn-report artifacts; one handover-packet schema;
  and — since 260703-L12 — the strategist's mandatory pre-run, the loop tiers with the 3-full-round
  cap and convergence rule, the quo-vadis criterion, and the criteria-catalog binding).
  Changing that prose changes the spec — `FlowTab.test.tsx` asserts several of these strings verbatim,
  so edits must stay in sync with the tests.
- **Segment prose speaks the l-01 vocabulary.** Phase labels and rundown lines use the role files' own
  words (the worker's `orient`, the designer's `reframe`, the frame's `request → trust-checkpoint →
  reframe-research → decide → build → close` axis); the retired FRAME/BUILD-JOB models and the
  contact-point vocabulary died with the l-01/l-02 convergence and must not reappear here.
- **`FlowSegment` is the contract with the renderer.** Adding a segment kind means updating both this
  union and FlowTab's `Segment` switch; keep them in lockstep.

## Docs References

| Source | Relevance |
| --- | --- |

No relevant documentation found after checking live sources; the design record backing these models is
same-repository (see Repo-Internal References).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The renderer + nav that consume this registry (segment switch, gate rider default, model fallback). | "Flow model" | dashboard/src/panels/FlowTab.tsx:119-119 |
| The coverage that asserts the render census + several invariant strings on these models. | "renders every registered model without crashing" | dashboard/src/panels/FlowTab.test.tsx:39-55 |
| `lifecycle_start`, which emits the orchestrator lifecycle's front-half prose rundown. | `lifecycle_start_payload` | mcp/src/agents_remember/mcp/tools/lifecycle.py:20-21 |

As of the 260703-L8 remediation the registry drew the then-converged doctrine: a ROUTER model (three conditions, edge cases, the D·P·O event loop, the task-doc→branch→worktree ladder) replaced the retired FRAME and BUILD-JOB models; the worker model was brief-started with no lifecycle machinery; the manager raised master-handover-approval; the orchestrator model drew the event loop with the super-branch INTENT as a branch-only act; and the comms takeaway scoped the spirit test to the bird's-eye coordination rung. Cycle 6 aligned the two seam nodes with the ruled channel: the manager's handover node draws the non-blocking raise (`wait=false`) with the returned gateId riding the packet, and the backend orchestrator's handover node draws the decide-by-packet-carried-gateId — a canvas-onboarded manager no longer reproduces the blocking raise. Cycle 7 completes the raise node's address (AR4-4): its detail now names `enclosure="<master task name>"` as the exact address integration enforcement matches the gate by, so a canvas-onboarded manager raises an addressed (matchable) gate instead of an unaddressed one.

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: replaced the drawn
  unknown-role fallthrough with fail-closed hosted admission and expanded reviewer from two prose
  seams to four explicit task-altitude/parent addresses. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `flowModels.ts` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded sprint provenance as part of command-seat flow
  identity. Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the superseded Types
  prose citation and the `n/a` table rows with exact anchors; deleted the unresolvable
  design-doc rows (task-provenance sources outside the code/memory roots) and the removed
  `next_step.py` row; exact non-fixing check returns zero findings.

- 2026-07-07T21:17+02:00 — 260707-HFX-L6 review remediation: the FlowTab registry now has
  a 9-model census with an ARCHITECT model between Router and Designer; the Router model routes
  developer-facing sessions to architect; Designer is the architect hat; Orchestrator is a spawned
  backend loop; Comms shows worker -> manager -> orchestrator -> architect -> developer; and
  super/developer review wording is architect-mediated. Verification metadata pinned until closeout
  stamps the HFX-L6 commit.

- 2026-07-06T15:40+02:00 — 260703-L12 (three-party loops): the census becomes 8 — the STRATEGIST model (L105-149: mandatory pre-run gate, eight-phase method with two-sided surfaces and cited edges, orchestration-task deliver node, plan-review loop gate, drawing-board convergence, reader-not-mutator adoption) joins between DESIGNER and ORCHESTRATOR; loop ride-along lines land on the manager (tier scoring + cap/convergence junction), worker (builder resume), reviewer (criteria catalogs + delta-verify reuse), comms (cap/convergence + quo-vadis junction), and orchestrator (strategist pre-run line, orchestration-task gate detail, visible-behavior-first single review point); `FLOW_MODELS` moved to L400. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T13:35+02:00 — 260703-L10 round 2 (L10R-3): the References row's leftover "8 models" became the 7-model census (and its parenthetical drops the dead frame-doctrine item) — the last pre-convergence count in this sidecar, missed by the round-1 body de-stale. No source change. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T12:05+02:00 — 260703-L10 (one-vocabulary sweep, S2 verification): the canvas was verified against the converged `l-01-agent-lifecycles` doctrine — the ROUTER/role/COMMS structure, seam channel, and invariant strings were already current from L8; the one residual vocabulary drift fixed is the designer model's reframe-agreement node phase label, `"frame"` → `"reframe"` (the doctrine word in `roles/designer.md`). Sidecar body de-staled from the pre-convergence 8-model census (build-job/frame, BUILD_JOB default) to the shipped 7-model registry with ROUTER as `FLOW_MODELS[0]`. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: manager RAISE node detail now names the enclosure address (`enclosure="<master task name>"`, AR4-4). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: seam nodes updated — manager RAISE node carries wait=false + gateId-in-packet, orchestrator decide node carries decide-by-packet-carried-id (AR3-6a). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): canvas redrawn to the converged doctrine (visuals ride every doctrine change from now on). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T09:40+02:00 — Created for 260703-L0 (Canvas & playground): the flow-model registry for the
  FlowTab canvas — the segment/model types (`Status`, `FlowStart`, `FlowNode` incl. `rides`/`ridesNote`,
  `FlowRundown`, `FlowDivider`, `FlowSegment`, `FlowModel`) plus 8 static models (build-job with the
  task-26 chain preserved and the Wollmilchsau self-id added; frame; designer; orchestrator; manager;
  worker; reviewer; comms). The models encode the agent-orchestration series' agreed invariants and back
  the extracted content that FlowTab used to hold inline. Verification metadata pinned until closeout
  stamps the L0 commit.
