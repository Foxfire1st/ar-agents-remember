# l-01-agent-lifecycles/roles/orchestrator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the sprint-bound backend orchestrator lifecycle. The canonical
`skills/l-01-agent-lifecycles/roles/orchestrator.md` owns doctrine; the sync process installs this
exact artifact.

## Code Commentary

### Logic

The orchestrator owns durable portfolio execution behind the architect. It dispatches managers and
system specialists with `dispatch_agent` on canonical master or sprint documents, adopts
architect-ruled plans, processes durable handovers, and decides the one open master handover gate by
master document and kind. It never handles a child occupant id, exact readiness, raw inbox address,
attachment id, or packet-carried gate id. Optional designer/strategist and plan-review reviewer
seats are architect children; leaf/master-exit reviewers are manager children, and super-exit
reviewers are orchestrator children.

### Conventions

The role runs an event loop over durable portfolio state, relays developer decisions to the
architect, and uses proper role seats rather than orchestration-native sub-agents. Edit the canonical
role, then synchronize.

### Invariants And Boundaries

- Seat identity is `(canonical task document, role)` and occupant replacement is plane-owned.
- Structural dispatch and structural gate decision fail closed on missing or ambiguous authority.
- The orchestrator is backend-only and does not become manager, worker, reviewer, curator, or
  developer-facing architect.
- This packaged artifact must remain byte-identical to the canonical role.

### Todos

None recorded.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.


### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

### 260731-EFA-L17 — Quality Altitude Ladder

The orchestrator's quality altitude uses the pinned Dagger graph for Agents Remember acceptance.
Leaf/focused work selects targeted mode; `worktree_integrate` selects full mode exactly once at
master altitude. Both require the explicit task-derived diff base, and host pytest/wrapper runs
are refused rather than accepted or used as fallback. `memory_quality_check` stays a per-leaf
closeout gate; orchestrators do not run a separate full graph per leaf.

## L23 Final Candidate Disposition

The orchestrator observes closeout and integration through canonical task status. Leaf acceptance is
targeted Dagger; master acceptance is one full Dagger graph at master integration altitude, with no
model-managed checklist or fallback runner.

## R39 Generic Quality Altitude

The orchestrator resolves executor, environment, retry, resource, and evidence contracts from
repository memory rather than supplying Agents Remember-specific instructions. Leaf closeout and
master integration remain the only acceptance owners.

## 260815-DAG-L2 Ready-Frontier And Landing Authority

The orchestrator recomputes the ready frontier after every material event and records rationale,
evidence, author, confidence, and supersession before a priority/queue judgment changes selection.
Organizational leaves land directly as released; the last one forms the exact proposed final
candidate and receives the full master check before super moves. Atomic masters hold an exclusive
blocker and land only as a completed block. Integration refs are never repair workbenches; fixes
return to an owning/reopened or new scoped leaf.

## 260815-DAG-L13 Scheduling Default Doctrine

Adoption doctrine now states that a sprint adopted without an `executionGraph` runs the
atomic-sequential default (one master fully integrates before the next starts);
`task_doc.author_execution_graph` bootstraps a graph onto it (first `add_node` batch) and edits
one incrementally afterwards. The `migrate_execution_topology` legacy-cutover reference is gone.

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: synchronized the scheduling-default doctrine —
  graph-less sprints run atomic-sequentially and `author_execution_graph` bootstraps/edits the
  graph; the `migrate_execution_topology` reference is gone. Verification remains closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized ready-frontier judgment records,
  organizational/atomic landing, reviewer lineage, and no-workbench repair routing. Verification
  remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: reconciled the generic orchestrator with
  repository-resolved acceptance and no fallback. Verification remains closeout-owned.
- 2026-08-14T06:32+02:00 — L23 synchronized runtime doctrine: orchestration observes durable
  task-addressed operations and retains the targeted-leaf/full-master Dagger altitude without
  model-managed job ids. Verification remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final curator pass: synchronized Dagger-only acceptance,
  targeted/full altitude, explicit diff-base ownership, and diagnostic-only host execution.
  Verification remains closeout-owned.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: synchronized the
  canonical orchestrator quality-altitude rule with host-managed master memory
  and an optional constrained-environment cap.

- 2026-08-11T19:58+02:00 — Reconciled `orchestrator.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the orchestrator's
  quality altitude ladder paragraph (master-gate-owned full wrapper,
  leaf `--targeted`, per-leaf memory quality, no per-leaf full runs).
  Verification metadata stays pinned until closeout stamps the 260731-EFA-L17
  commit.
- 2026-08-05T22:10+02:00 — 260731-EFA-L16 curator: recorded the No Native Sub-Agents doctrine replacing the Sub-Agent Fan-Out section (developer ruling: orchestration seats use no shadow channel; analyses run in-loop or as dispatched role seats) and the `system/tools.md` naming in delegated-authority checks and the master→super integration packet. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: explicit
  orchestrator takeover now claims and verifies the `orchestrator` role with the qualified leaf;
  manager dispatch now states the environment-role-plus-leaf pair claim. Reconciled the documented
  manager retirement boundary to include curator seats. Verification metadata remains pinned until
  closeout stamps the L17 commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 reviewer N7: recorded the stale echo-confirmed
  supervisor-delivery wording as doctrine debt; no source behavior changed.

- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: replaced the mandatory strategist pre-run
  with architect-proposed/developer-approved Job P, documented the orchestrator-owned task
  author/adopt path after a sanctioned skip, and made independent ready masters parallel by default
  within `maxParallelMasters`. Added the governing-overview backlink. Verification metadata remains
  pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: the package-data orchestrator role
  sidecar now states that `lifecycle_finalize_task` auto-lands completed manager/reviewer seats into
  the landed archive (`autoLandOnFinalize`) rather than auto-retiring them; explicit
  `session_retire` remains the portfolio-wide by-hand cleanup path. Verification metadata pinned
  until closeout stamps the HFX2-L11 commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite, active vigilance → passive
  process-and-ack): "monitor turn-report artifacts" replaced with the
  passive process-and-ack contract + watcher ban (uniform-mechanism ruling 2026-07-07); the spirit
  test is explicitly retained as the one surviving model-judgment (not watching) duty; Comms gains
  a reworded "Stdin push" line naming the L2 injector and a new "Idle is safe" bullet. Doctrine-only
  change set (5 canonical `skills/` files synced to 9 downstream copies, 0 Python); sync-propagated
  bundle copy of the canonical `skills/l-01-agent-lifecycles/roles/orchestrator.md`. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L5 commit.

- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 doctrine refinement: the opening portfolio orientation
  step now applies Developer Clarification Triage to developer/architect clarifications before
  note-only handling. The orchestrator reads the active queue, implements close/current/small
  additions in the active task, records true future queue durably, and asks through the architect
  relay when the fit is unclear. Sync-propagated bundle copy.

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 (seat takeover + delegated series authority):
  opening move gains a task-seat takeover step before the trust checkpoint. A developer-declared
  orchestrator takeover now explicitly opens the named task doc, attaches this dashboard terminal
  catalog session to the qualified leaf key, renames the session, and verifies the catalog/dashboard
  row before continuing. The role also now states that accepted orchestrated-series authority lets
  the orchestrator govern subordinate closeout/finalize/cleanup and master→super integrations
  without repeated developer formality, while final super/PR-carryover, raised human-pinned gates,
  scope shifts, out-of-scope red checks, and quo-vadis decisions remain developer stops.
  Doctrine-only; existing runtime attachment behavior unchanged. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L6 commit.

- 2026-07-08T02:55+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state,
  issue #12): "Integration duty (master → super)" gains step 6 — the orchestrator's portfolio-wide
  `session_retire` authority (any seat, including a completed manager; owner-never-self-retires
  still holds), usable by hand when `lifecycle_finalize_task`'s auto-retire hook (config-gated,
  default ON) misses a stuck/abandoned seat. Knobs `tools` row updated. Sync-propagated bundle
  copy from the canonical `skills/l-01-agent-lifecycles/roles/orchestrator.md`. Verification
  metadata pinned until closeout stamps the HFX-L8 commit.

- 2026-07-08T02:00+02:00 — 260707-HFX-L7 (provider degradation protocol): documented the new
  "## Provider Degradation Alert" section (placed after the opening-move paragraph, before
  Decision-Item Relay) — the four-step dispatch-system-specialist / investigate-first /
  fix-or-stop procedure, the deliberate manager/orchestrator kill-authority asymmetry, the
  system-specialist's report-only mutation boundary, and the critical-failsafe-may-have-already-run
  note. Sync-propagated bundle copy. Verification metadata pinned until closeout stamps the
  HFX-L7 commit.
- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: reframed
  orchestrator.md as a spawned backend lifecycle, never the normal developer-facing seat; design
  and drawing-board questions now emit decision/design items to the architect; developer-worthy
  items use the existing inbox with `decision-item` / `decision-ruling`; super-exit review is
  architect-mediated; and spawned backend hat-collapse is explicitly forbidden. Sync-propagated
  bundle copy. Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): Knobs table gained the three
  free-form escape-hatch rows (launchArgs / sessionCommands / promptKeywords, settings-only, never
  validated) and the knob footer now includes the rolesPerLevel per-level override and the
  harnesses.md manual pointer. Sync-propagated bundle copy. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-06T23:59:06+02:00 — 260703-L14 (visual hierarchy + chat grouping): Job P's Output bullet now
  names the orchestration task's durable form — a `kind:"master"` task doc with a top-level
  `orchestrates` list (the dashboard's hierarchy/insignia source), so setting it is part of
  adoption. Sync-propagated from the canonical skills/ copy.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-1): knob-table harness example fixed to the registry id `claude`. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-6): the Hand-Off Protocol intro carries the orchestrated-run standing-approval carve-out cross-ref (integrations concentrate the developer hand-off at the super PR/carry-over gate; the integration table row governs the hand-off cases that remain). Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): the strategist seat is REAL — Job P's mandatory pre-run + orchestration-task adoption + re-evaluation rules; Job O entry requires the adopted orchestration task; the super-exit handover carries the ruled L8-Q9 resolution (orchestrator-delegated integrations, the developer's single review point at the super PR/carry-over gate, reviewable environment + visible-behavior-first + demo notes); escalation swaps "genuinely stumped" for the quo-vadis test; loop escalations arrive with round history. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T19:10+02:00 - L8 builder cycle 6: enforcement sentence made true (enclosure-addressed integrate refusal), Profile check moved below the routing table, fan-out fallback clarified (role seats only; strategist marked planned) (AR3-1/AR3-4/AR3-6c). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the master-exit decide call is named exactly (gate_decide(gate_id=<packet-carried>, decision, deciding_role=orchestrator) with server-side cross-lifec. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): gained the handover-gate deciding duty + manager-brief dispatch + hat-collapse gate-reversion clause. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: harness overlay deleted; sub-agent doctrine folded in as a capability-conditional section; knob harness row is a preference settings overrides. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:15+02:00 - L8 orchestrator routes rework: restructured as event loop + three jobs + hat-collapse; invariant ladder (task doc -> branch -> worktree) replaces worktree-first ordering; chat-build route removed; reopen-and-reshape + ordered-list renumbering doctrines encoded; body rewritten accordingly. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: orchestrator.md became the full developer-facing lifecycle: absorbed the session-job phase axis + hand-off protocol, gained solo-as-degenerate-portfolio, and is now the topology's single home; body rewritten accordingly. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T13:03+02:00 — 260703-L5 expanded the orchestrator job with its master-to-super
  integration duty: consume the manager handover packet, check the master-exit verdict, integrate from
  a super-sourced orchestrator worktree, run C-09/C-11 merge/carry-over, keep duplicate memory
  single-sided, map the ledger for accumulated master commits, and release the next ready masters only
  after the super code/memory tips are recorded. It also records the 260630-derived gh-route master
  finalize/archive and parallel-master reconcile primitives as sequenced manual backlog until their
  task-doc-tooling leaves land. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-04T11:00+02:00 — Created file-level onboarding for the new `l-02-agent-orchestration` skill's
  orchestrator job (leaf 260703-L1), the portable job the frame houses at the first coordination leaf.
  Captured the seat definition (memory substrate; quality ∝ memory-repo quality), the six-step duties
  spine (seat & profile → portfolio streamlining → plan gate → dependency-ordered dispatch → super-exit
  seam → close with self-improvement proposals), the **orchestrator-only spirit test** (within-spirit →
  act + decision-log; against-spirit → joint decision), the integrity bulwark (planned-vs-planned AND
  planned-vs-past), the two conflict-resolution modes (up-front foundation-master extraction vs post-hoc
  super-branch remediation), the self-improvement loop (proposals only), the sub-agent durable-report
  rule (AR state mutations stay in the main loop), and the knob block. Sync-propagated
  (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-02-agent-orchestration/jobs/orchestrator.md`. Verification metadata pinned until closeout
  stamps the L1 commit.
