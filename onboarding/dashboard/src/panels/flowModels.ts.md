# dashboard/src/panels/flowModels.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/flowModels.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-05T16:30+02:00 |
| lastVerifiedCommitHash | `19d76dbd73673ffc72d0ee1b6a868ac2fdf15ad0`       |
| lastVerifiedCommitDate | 2026-07-05T16:23:40+02:00|
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
only then built. The 8 models encode the **agreed invariants of the agent-orchestration series** in a
human-readable form, so this file is as much a spec record as a UI data file.

## Code Commentary

### Logic

**Types (L7-L50).** `Status = "current" | "proposed"` (L7) drives edge colour (mint vs amber dashed).
The four segment shapes form the `FlowSegment` union (L40): `FlowStart` (L9-14, a labelled entry pill +
optional `next`/`nextStatus` edge), `FlowNode` (L16-27 — `phase`, monospace `tool`, optional `detail`,
optional `rides` = the gate/seam whose notification rides this call, optional `ridesNote` overriding the
default rider line, and the outgoing `next`/`nextStatus` edge), `FlowRundown` (L29-33, a titled card of
`{ line; junction? }` prose lines for non-linear stretches), and `FlowDivider` (L35-38, a caption).
`FlowModel` (L42-50) bundles `id`, `label`, `title`, `takeaway`, and `segments`.

**The 8 models**, in `FLOW_MODELS` order (L368):

1. **`build-job`** (`BUILD_JOB`, L54-95) — the original task-26 model, preserved: `context_packet` →
   `lifecycle_start`, a prose front-half `rundown` (reframe → research → job selection →
   `⟁ task-file-exists?` junction → `task_doc`), a divider, then the linear `worktree_start --dry-run` →
   `lifecycle_end` chain where each gate node `rides` its auto-fired turn-end notification. The takeaway
   now **self-identifies as the "Eierlegende Wollmilchsau"** (one implicit role doing a bit of everything
   minus orchestration) and points at the FRAME model for the decomposition (L64-66).
2. **`frame`** (`FRAME`, L305-332) — the thin **contact points** every job shares: context intake → job
   selection + execution → wrap-up. A `junction` line marks where the housed job's own flow takes over
   (L325); the takeaway frames it as the consistent container that makes jobs composable.
3. **`designer`** (`DESIGNER`, L272-301) — task design as its own registered job (the `tasks/AGENTS.md`
   doctrine: meta-question, reframe-before-execution, evidence-first). It is master-scoped, so
   cross-master/future collisions can slip; that residual risk is owned downstream — **at portfolio
   streamlining the orchestrator doubles as the designer's adversarial reviewer** (L299).
4. **`orchestrator`** (`ORCHESTRATOR`, L99-146) — developer-requested, never self-spawning: profile-fit
   seat, the non-linear **portfolio phase** (streamline before sequencing), the **master-granular
   dependency DAG** rule (`⟁ … reshape master boundaries — NEVER interleave dispatch`, L128), the
   accumulative super integration branch, the dependency-ordered dispatch loop, **both adversarial seams**
   (master-exit L137 and super-exit L140, each `ridesNote`-tagged "seam 1/2 of 2"), wholesale developer
   review, and the grounded self-improvement report at close.
5. **`manager`** (`MANAGER`, L150-184) — one master, the leaf dispatch loop, review-vs-task_doc,
   **delegated attributed leaf gates** (`decidedBy: manager lifecycle · decidedVia: orchestration`, the
   owning agent never self-approves — L177), C-11 leaf→master integration, the master-exit seam, and
   handover to the orchestrator. Managers **escalate plan deltas** rather than judge them ("managers
   don't reshape plans (no bird's-eye)", L170) — no spirit test below the bird's-eye.
6. **`worker`** (`WORKER`, L188-217) — short-lived, one per leaf, onboarded from the context packet +
   task_doc (never a transcript), running the unchanged l-01 build spine; its closeout gate is decided by
   the manager (delegated), and every hand-off leaves a **mandatory turn-report artifact** (L214).
7. **`reviewer`** (`REVIEWER`, L336-366) — spawned at exactly the two seams; three-lens review
   (completion vs task docs · code quality per tools.md · onboarding-vs-code); its **verdict is evidence,
   not a decision** (attaches to the handover gate as judge evidence — L362), and a blocking verdict must
   **decompose into fix leaves** (L363), never prose complaints.
8. **`comms`** (`COMMS`, L221-268) — the channels (inbox = queue · stdin push = delivery · artifacts =
   reporting · chats = walk-in), the nudge loop, the **escalation ladder** (worker → manager →
   orchestrator → developer, no level skipped), the **orchestrator-only spirit test** (L262-264), and the
   single **one-schema handover packet** serving master handover / role takeover / worker respawn (L266).

### Conventions

Plain TypeScript data module — no React, no styling, no store. Each model is a `const` typed as
`FlowModel`, and `FLOW_MODELS` (L368) is the ordered export the nav renders; `FLOW_MODELS[0]`
(`BUILD_JOB`) is FlowTab's default/fallback, so ordering is load-bearing for the default view. Prose
carries the series' typographic conventions (`⟁` for a junction/decision, `⊘` for a gate/seam rider,
`·` separators, mint/amber via `nextStatus`). A gate/seam node sets `rides`; when it needs a bespoke
rider line (a seam, a delegated gate, judge evidence, a reframe) it also sets `ridesNote`, overriding
FlowTab's default auto-fire notification text.

### Invariants And Boundaries

- **Content-only, static, no store reads.** Everything here is authored design data; the module imports
  nothing and reads no runtime state. Reshaping a drawn lifecycle happens here, not in the renderer.
- **The registry is a spec record.** The models encode the series' agreed invariants (orchestrator-only
  spirit test; the worker → manager → orchestrator → developer escalation ladder; exactly two adversarial
  seams; the master-granular DAG / never-interleave-dispatch rule; delegated attributed gates where the
  owning agent never self-approves; verdicts-are-evidence-not-decisions; mandatory turn-report artifacts;
  one handover-packet schema). Changing that prose changes the spec — `FlowTab.test.tsx` asserts several
  of these strings verbatim, so edits must stay in sync with the tests.
- **build-job stays the task-26 spec.** Its chain (front-half prose rundown + linear gate chain) remains
  the human-readable mirror of `next_step.py`; only its takeaway was extended (the Wollmilchsau self-id +
  FRAME pointer).
- **`FlowSegment` is the contract with the renderer.** Adding a segment kind means updating both this
  union and FlowTab's `Segment` switch; keep them in lockstep.

## Docs References

| Source | Relevance |
| --- | --- |

No relevant documentation found after checking live sources; the design record backing these models is
same-repository (see Repo-Internal References).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The renderer + nav that consume this registry (segment switch, gate rider default, model fallback). | L57-L58; L81-L133 | [FlowTab.tsx](FlowTab.tsx) |
| The coverage that asserts the render census + several invariant strings on these models. | L38-L94 | [FlowTab.test.tsx](FlowTab.test.tsx) |
| The next-step engine the `build-job` model is the human-readable spec for. | — | [tools/next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |
| `lifecycle_start`, which emits the build-job front-half prose rundown. | — | [tools/lifecycle.py](agents-remember/mcp/src/agents_remember/mcp/tools/lifecycle.py) |
| The orchestration series design record these 8 models encode (roles, seams, DAG topology, gate delegation, spirit test, frame doctrine). | — | [design-agent-orchestration.md](agents-remember/tasks/agents-remember/260703_agent-orchestration/notes/design-agent-orchestration.md) |

As of the 260703-L8 remediation the registry draws the CONVERGED doctrine: a ROUTER model (three conditions, edge cases, the D·P·O event loop, the task-doc→branch→worktree ladder) replaces the retired FRAME and BUILD-JOB models; the worker model is brief-started with no lifecycle machinery; the manager raises master-handover-approval (the orchestrator decides); the orchestrator model draws the event loop with the super-branch INTENT as a branch-only act; the comms takeaway scopes the spirit test to the orchestrator rung. FLOW_MODELS = [ROUTER, DESIGNER, ORCHESTRATOR, MANAGER, WORKER, REVIEWER, COMMS].

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): canvas redrawn to the converged doctrine (visuals ride every doctrine change from now on). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T09:40+02:00 — Created for 260703-L0 (Canvas & playground): the flow-model registry for the
  FlowTab canvas — the segment/model types (`Status`, `FlowStart`, `FlowNode` incl. `rides`/`ridesNote`,
  `FlowRundown`, `FlowDivider`, `FlowSegment`, `FlowModel`) plus 8 static models (build-job with the
  task-26 chain preserved and the Wollmilchsau self-id added; frame; designer; orchestrator; manager;
  worker; reviewer; comms). The models encode the agent-orchestration series' agreed invariants and back
  the extracted content that FlowTab used to hold inline. Verification metadata pinned until closeout
  stamps the L0 commit.
