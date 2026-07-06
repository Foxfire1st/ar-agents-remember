# l-01-agent-lifecycles/roles/orchestrator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T17:35+02:00 |
| lastVerifiedCommitHash | `bcaa78070f77c76f1c4db0af93786bb193b92523` |
| lastVerifiedCommitDate | 2026-07-06T07:51:05+02:00|

## Purpose

The developer-facing lifecycle, restructured (260703-L8 reopened pass) as an EVENT LOOP over durable portfolio state - not a request-to-close pipeline. Each turn routes the incoming event (developer message, worker report, verdict, own finding) into one of three jobs under one roof: Design (pull the designer hat), Portfolio (streamline + the planner master), Orchestrate (execute the plan). Solo work is the same jobs with hats collapsed. Supersedes the transplanted session-job phase spine the first L8/L9 landing shipped.

## Code Commentary

### Logic

Sync-propagated copy of the canonical skills/l-01-agent-lifecycles/roles/orchestrator.md. Opening move every session (resumption is the common case): trust checkpoint -> lifecycle_start -> PORTFOLIO ORIENTATION (read the task tree: in flight / blocked / awaiting whom; say it back) -> route the event by a four-row condition table (no doc -> D; docs + coherence question -> P; approved series -> O; no code change -> research-only exit, chat is the right medium). THE INVARIANT LADDER: approved task doc -> branch (intent) -> worktree only where something is built; D and P never touch git; chat is never a build route (260628 T7). Job D: run roles/designer.md inline as a hat (egg/hen: a designer cannot sit in a leaf the task does not exist yet); orchestrator bulwark-checks the design planned-vs-planned/past before acceptance; gate = developer accepts. Job P: coherence scan, bulwark, reshape (leaf moves + ORDERED-LIST renumbering: numbers ARE positions, contiguous while unlanded, maps in the decision log, freeze at main-landing); output = the planner master task (coordination leaves as subTasks, DAG + dispatch order in the body); gate = wholesale portfolio review; still no git. Job O: first act = the super-branch INTENT creating a BRANCH only (managers base off it); dispatch loop with AR_SPAWN_ROLE + qualified leaf keys; the FAILED-DELIVERABLE RULE (task_reopen + reshape, never redo siblings); integration duty master->super in a per-edge orchestrator worktree (C-11, the topology's single home with the strict branch stack and two conflict modes); super-exit seam; developer-gated landing tail; self-improvement close. Hat-collapse rule: flat run -> manager hat; session scale -> hands-on build with the worker's discipline and the owner's closeout tail. Spirit test remains this seat only; hand-off protocol (dry-run -> notify-and-stop -> report + junction table) unchanged.

As of the L8 de-harnessing pass the file carries a Sub-Agent Fan-Out capability-doctrine section (any harness that has fan-out: sub-agents write templated durable reports and return compact summaries; AR mutations stay in the main loop; capped by orchestration.concurrency.maxSubAgents; a harness without the ability runs the analyses sequentially) — the content formerly held by the deleted roles/orchestrator.claude-code.md overlay, generalized off the vendor.

As of cycle 4 the orchestrator DECIDES the manager's `master-handover-approval` gate at each master exit (own ambient identity as the attributed decider; policy may require the attached verdict; an undecidable handover escalates to the developer); manager dispatch compiles from templates/manager-brief.md carrying the base-off-current-super fact; the hat-collapse rule notes delegated gates collapse back to the developer when one chair owns both sides; the super-exit reviewer spawn states AR_SPAWN_ROLE=reviewer; finalize wording is honest (statuses via the tool, steps by hand); the dangling Phase cross-reference is fixed.

As of cycle 5: the master-exit decide call is named exactly (gate_decide(gate_id=<packet-carried>, decision, deciding_role=orchestrator) with server-side cross-lifecycle resolution) and integration enforcement stated; a Profile check (takeover) paragraph exists in The Event Loop (the AR-10 pointers now resolve); the fan-out section names the framework backdoor: spawn_agent_session is the harness-independent fan-out (DBMS principle). Cycle 6 makes the enforcement sentence true as-built (`worktree_integrate` refuses while a `master-handover-approval` gate addressed to this master — its `enclosure` — is undecided or policy-invalid), moves the Profile check paragraph AFTER the routing table so strict CommonMark keeps the opening-move list intact, and disambiguates the fan-out fallback: analyses stay sequential-in-loop on a spawnless harness, the framework spawn is for ROLE seats only (an env-less spawned chat would be misrouted as an orchestrator).

As of 260703-L12 the **strategist seat is REAL** (the "(planned seat — leaf L12)" marker is gone): Job P carries the MANDATORY strategist pre-run — before implementation starts on any designed master, `spawn_agent_session` with `AR_SPAWN_ROLE=strategist` and a portfolio brief of refs (never pasted state); the strategist returns the ORCHESTRATION TASK (sprint plan + scope, `templates/orchestration-task.md`), reviewed in the portfolio three-party loop (plan-review catalog) and converged over drawing-board rounds; this seat ADOPTS the draft (reader-not-mutator strategist); re-evaluation rules (in-sprint pre-implementation addition → re-plan; out-of-sprint → next sprint); Job O's entry requires the adopted orchestration task unconditionally (even a single master; the hat-collapse Portfolio bullet now says an orchestrated run never skips the pass — only session-scale hands-on work does). The **super-exit handover is ruled** (2026-07-06, resolves L8-Q9): all leaf→master and master→super integrations are orchestrator-delegated (happy path under the series' standing approval; a raised durable `integration-approval` gate still awaits the developer — human-pinned as-built); the developer reviews ONCE at the fully integrated super branch on the PR/carry-over gate, **visible-behavior-first in a REVIEWABLE ENVIRONMENT** (for agents-remember: the dashboard) with **demo notes ("what changed visibly", per master)**, code second. Round 2 (L12R-6) adds the standing-approval carve-out to the Hand-Off Protocol intro itself: in an orchestrated run, leaf→master and master→super integrations ride the series' standing approval — no per-edge developer hand-off; the table's integration row governs when a hand-off DOES happen (solo runs; a raised durable gate). The Comms escalation swaps "genuinely stumped" for the written QUO-VADIS test (a high-blast-radius truth goes up immediately; presentation-grade never), and the dispatch loop states how a manager-escalated loop (cap hit / non-convergence, round history attached) is re-run at this level's agent set or taken to the developer.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
