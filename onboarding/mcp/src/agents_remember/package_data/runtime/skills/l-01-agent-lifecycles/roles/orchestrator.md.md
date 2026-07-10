# l-01-agent-lifecycles/roles/orchestrator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T15:48+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814` |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The spawned backend orchestrator lifecycle: an EVENT LOOP over durable portfolio state, not a
developer-facing conversation. Each turn routes backend events (architect dispatch, manager
handover, worker report, verdict, own finding) into portfolio/orchestration work. Developer-worthy
decisions go to the architect as one-at-a-time decision items over the operator inbox.

## Code Commentary

### Logic

**260707-HFX2-L15 reviewer N7 current-source debt.** The source role still describes supervisor
hosted delivery as an echo-confirmed paste. L15's runtime now grants submitted acceptance only from
the bound harness log; pane capture is retry-safety/failure evidence. This sidecar records that the
role doctrine is stale until a separate canonical skill edit and sync pass lands.

260707-HFX2-L17 aligns orchestrator takeover and manager dispatch with pair-identified task seats.
A hand-opened orchestrator takeover explicitly claims the `orchestrator` role while attaching to
the qualified leaf, then verifies that `(leaf, role)` pair in the catalog/dashboard. Manager
dispatch likewise treats `AR_SPAWN_ROLE=manager` plus the qualified coordination leaf as the
manager's pair claim; the qualified leaf is no longer described as the whole task-seat identity.

260707-HFX2-L5 (doctrine inversion, active vigilance → passive process-and-ack): the dispatch-loop
bullet "monitor turn-report artifacts, nudges, escalation intake" is gone. In its place: "process
and ack the pending signals the L2 supervisor sweep wakes you with — turn-report artifacts,
nudges, escalation intake — before ending your turn; you never watch for these yourself," with an
explicit **watcher ban** (uniform-mechanism ruling 2026-07-07: the supervisor sweep is the one
mechanism, no seat-local polling/monitoring). The **spirit test survives as the one surviving
MODEL-judgment duty** — it is explicitly called out as NOT ported down to a watching duty; the
sentence now reads "apply the spirit test — a model-judgment duty, not a watching one — to
escalated deltas." The Comms Protocol section gains two changes: the "Stdin push" line is reworded
to name the L2 supervisor's injector (HFX2-L3) as the actual delivery mechanism (never this seat's
own initiative), and a new "Idle is safe" bullet states plainly that silence is supervised (the L2
sweep + L4 ladder), so `lifecycle_turn_end_notification` / ending a turn with nothing pending is
correct, not a risk to cover by watching — restating the same watcher ban. Pure doctrine reword;
the underlying sweep/ladder mechanics were already landed by HFX2-L2/L4.

260707-HFX2-L6 adds step 0 to the opening move for developer-declared orchestrator takeovers. If
the developer declares this chat the orchestrator for a named task, the task leaf is the seat: run
the shared Developer-Declared Task-Seat Takeover checklist from `../SKILL.md` before trust
checkpoint/profile work, attaching the current dashboard terminal catalog session to the qualified
leaf key, renaming the session, and verifying the catalog/dashboard row. The same leaf adds the
Delegated Series Authority paragraph: after the developer accepts an orchestration plan, this seat
owns subordinate execution without repeated developer formality, including manager handovers,
direct-work closeout when wearing a build hat, subordinate finalize/cleanup, and master→super
integration. It still stops for final super/PR-carryover, raised human-pinned gates, plan-meaning
changes, red checks outside scope, and quo-vadis truths. This is a doctrine-only correction; the
existing attachment and worktree command paths are unchanged.

260707-HFX2-L7 adds the queue-aware clarification hook to the opening portfolio orientation step.
When a developer or architect clarification arrives while a task is active, the orchestrator applies
Developer Clarification Triage against the same portfolio/queue state it is already reading:
close/current/small additions belong in the active task surface and implementation, future-queue
items go to the durable backlog, and unclear fit becomes one clarification request through the
architect relay.

L13 review follow-up (L13R-1): the knob table's `harness` example is the registry id `claude` (was the non-id `claude-code`); spawn refuses non-registry values, so examples must model valid input.

Sync-propagated copy of the canonical skills/l-01-agent-lifecycles/roles/orchestrator.md. HFX-L6
reframes this file as a spawned backend seat. Opening move every session (resumption is the common
case): trust checkpoint -> lifecycle_start -> PORTFOLIO ORIENTATION (read the task tree: in flight /
blocked / awaiting whom; say it back) -> route backend events from the architect, managers, workers,
reviewers, or the orchestrator's own findings. The invariant ladder still holds: approved task doc
-> branch intent -> worktree only where something is built; chat is never a build route. Design and
drawing-board items go to the architect. Job P performs coherence scan, bulwark, and—only after
developer approval of the architect's propose-first question—a strategist pass. Job O always
requires an adopted orchestration task: it adopts the approved strategist draft, or after a
developer-sanctioned skip this seat authors and adopts the task from the ruled plan and records the
source in the decision log. Job O executes approved backend plans: super-branch intent,
dependency-ordered dispatch with independent ready masters parallel by default up to
`orchestration.concurrency.maxParallelMasters`, failed-deliverable reopen/reshape, C-11
master->super integration duty, super-exit seam, architect-mediated developer landing tail, and
self-improvement close. Backend operational handoffs still use durable gates and inbox surfaces.
Hat-collapse is forbidden for spawned backend orchestrator sessions.

As of the L8 de-harnessing pass the file carries a Sub-Agent Fan-Out capability-doctrine section (any harness that has fan-out: sub-agents write templated durable reports and return compact summaries; AR mutations stay in the main loop; capped by orchestration.concurrency.maxSubAgents; a harness without the ability runs the analyses sequentially) — the content formerly held by the deleted roles/orchestrator.claude-code.md overlay, generalized off the vendor.

As of cycle 4 the orchestrator DECIDES the manager's `master-handover-approval` gate at each master exit (own ambient identity as the attributed decider; policy may require the attached verdict; an undecidable handover escalates to the developer); manager dispatch compiles from templates/manager-brief.md carrying the base-off-current-super fact; the hat-collapse rule notes delegated gates collapse back to the developer when one chair owns both sides; the super-exit reviewer spawn states AR_SPAWN_ROLE=reviewer; finalize wording is honest (statuses via the tool, steps by hand); the dangling Phase cross-reference is fixed.

As of cycle 5: the master-exit decide call is named exactly (gate_decide(gate_id=<packet-carried>, decision, deciding_role=orchestrator) with server-side cross-lifecycle resolution) and integration enforcement stated; a Profile check (takeover) paragraph exists in The Event Loop (the AR-10 pointers now resolve); the fan-out section names the framework backdoor: spawn_agent_session is the harness-independent fan-out (DBMS principle). Cycle 6 makes the enforcement sentence true as-built (`worktree_integrate` refuses while a `master-handover-approval` gate addressed to this master — its `enclosure` — is undecided or policy-invalid), moves the Profile check paragraph AFTER the routing table so strict CommonMark keeps the opening-move list intact, and disambiguates the fan-out fallback: analyses stay sequential-in-loop on a spawnless harness, the framework spawn is for ROLE seats only (an env-less spawned chat would be misrouted as an orchestrator).

As of 260703-L12 the **strategist seat is real** and returns an orchestration-task draft when
dispatched. HFX3 supersedes the old mandatory-pre-run rule: the architect proposes Job P and the
developer decides; a sanctioned skip routes directly to this seat's author-and-adopt path, so Job O
never deadlocks. The dependency graph, not habit, decides sequencing: independent ready masters run
in parallel within `maxParallelMasters`; serial execution must name a gate, shared-file one-writer
dependency, or explicit ruling. The super-exit handover remains orchestrator-delegated under standing
series authority, with human-pinned gates and the final visible-behavior-first super review preserved.

As of 260703-L14 the Job P Output bullet states the orchestration task's DURABLE FORM: a
`kind:"master"` task doc carrying a top-level `orchestrates` list naming the master tasks it
commands — the dashboard derives the orchestration > master > leaf hierarchy (and the rank
insignia) from that field, so setting it is part of adoption. This onboarded package_data copy is
the mirror of the canonical `skills/l-01-agent-lifecycles/roles/orchestrator.md`; the other
sync-propagated harness-dir copies (`.claude/`, `.codex/`, …) are generated and not
onboarding-covered.

**260707-HFX-L7 (provider degradation protocol)** adds a new "## Provider Degradation Alert"
section, placed right after the trust-checkpoint/hand-off paragraph that closes the opening-move
description and before the "Decision-Item Relay To The Architect" section. On a `degradation-alert`
inbox row the orchestrator keeps portfolio attention on OBSERVATION AND DELEGATION — it must never
become the fixer itself, echoing the file's core framing (an event loop over durable state, never a
hands-on builder). The section is a four-step procedure: (1) dispatch the new `system-specialist`
role via `spawn_agent_session` with `env={"AR_SPAWN_ROLE": "system-specialist"}`, the degradation
event id/payload, current metrics and provider log paths, and a report path under the active
master's `notes/reports/` (or an orchestrator-designated folder when no master owns the incident);
(2) require the specialist to investigate and write the report BEFORE any remediation — this is
the same investigate-first discipline `roles/system-specialist.md` itself carries; (3) read the
report and, only if it says the issue is fixable in session, send the specialist exactly ONE
explicit fix order; (4) otherwise — not fixable, or critical pressure continues — stop providers
through the always-legal teardown path (`provider_watchers stop` / provider teardown) before they
take the system down, noting that a critical detector event may already have executed the
automated failsafe stop (`providers/degradation.py`'s critical-threshold behavior), in which case
the orchestrator verifies and records what happened rather than re-issuing a redundant stop. The
section closes three composition points: managers receiving the same alert only stop STARTING
providers and have no kill authority (the asymmetry with this seat's step 4 is deliberate — kill
authority is exclusively the orchestrator's escalation path); the system-specialist seat never
mutates task docs, lifecycle state, or memory beyond its report (so this dispatch is safe under
the orchestrator's existing decision-item-relay and gate-decision machinery — the specialist
cannot make an irreversible AR-state change on its own); and the whole protocol is scoped
providers-only this iteration, with Sentry/system-monitoring integration recorded as a future
detection source, not part of this role's response procedure.


### 260707-HFX2-L11 Seat Cleanup Addition

Issue #12's authority split still names the orchestrator's PORTFOLIO-WIDE retire authority, but
normal successful master→super finalization no longer terminates chats. `lifecycle_finalize_task`
marks the finalizing master's manager + master-level reviewer seats `status:"landed"` at the
finalize edge (config-gated `retirement.autoLandOnFinalize`, default ON), putting them in the
dashboard's collapsed landed archive for inspection until explicit archive cleanup. The by-hand
`session_retire(actor_session_id=<own session>, session_id=<the seat>, reason=...)` path remains for
stuck/abandoned seats and for exceptional cleanup; unlike the manager (scoped to its own master's
worker/reviewer/curator seats), the orchestrator may retire any seat in the portfolio.
Owner-never-self-retires still holds unconditionally: the orchestrator can never retire its own seat, mirroring the
same server-side policy (`serving/retire_policy.py::check_retire_authority`) the manager's cleanup
duty relies on. The Knobs table's `tools` row includes `session_retire` (any seat, portfolio-wide)
alongside the existing `spawn_agent_session` entry for explicit by-hand cases.

### L16 Knob Additions

260703-L16: the Knobs table gains the three FREE-FORM rows (`launchArgs` — verbatim harness argv;
`sessionCommands` — lines pasted + submitted into the fresh session before the brief;
`promptKeywords` — prepended as the first line of the dispatch brief paste; all settings-only,
never validated, recorded in spawn provenance), and the knob footer now names the per-level
override (`orchestration.rolesPerLevel.<level>.<role>`; role-file defaults < settings < level
override) plus the `docs/reference/harnesses.md` spawn-knobs manual.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
  process-and-ack): "monitor turn-report artifacts, nudges, escalation intake" replaced with the
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
