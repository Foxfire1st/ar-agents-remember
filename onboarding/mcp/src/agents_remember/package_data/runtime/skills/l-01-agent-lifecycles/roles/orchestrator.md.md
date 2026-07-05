# l-01-agent-lifecycles/roles/orchestrator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T04:40+02:00 |
| lastVerifiedCommitHash | `314d21a8917decf942b302413e0cd31e8befec33` |
| lastVerifiedCommitDate | 2026-07-05T04:29:52+02:00|

## Purpose

The developer-facing lifecycle, restructured (260703-L8 reopened pass) as an EVENT LOOP over durable portfolio state - not a request-to-close pipeline. Each turn routes the incoming event (developer message, worker report, verdict, own finding) into one of three jobs under one roof: Design (pull the designer hat), Portfolio (streamline + the planner master), Orchestrate (execute the plan). Solo work is the same jobs with hats collapsed. Supersedes the transplanted session-job phase spine the first L8/L9 landing shipped.

## Code Commentary

### Logic

Sync-propagated copy of the canonical skills/l-01-agent-lifecycles/roles/orchestrator.md. Opening move every session (resumption is the common case): trust checkpoint -> lifecycle_start -> PORTFOLIO ORIENTATION (read the task tree: in flight / blocked / awaiting whom; say it back) -> route the event by a four-row condition table (no doc -> D; docs + coherence question -> P; approved series -> O; no code change -> research-only exit, chat is the right medium). THE INVARIANT LADDER: approved task doc -> branch (intent) -> worktree only where something is built; D and P never touch git; chat is never a build route (260628 T7). Job D: run roles/designer.md inline as a hat (egg/hen: a designer cannot sit in a leaf the task does not exist yet); orchestrator bulwark-checks the design planned-vs-planned/past before acceptance; gate = developer accepts. Job P: coherence scan, bulwark, reshape (leaf moves + ORDERED-LIST renumbering: numbers ARE positions, contiguous while unlanded, maps in the decision log, freeze at main-landing); output = the planner master task (coordination leaves as subTasks, DAG + dispatch order in the body); gate = wholesale portfolio review; still no git. Job O: first act = the super-branch INTENT creating a BRANCH only (managers base off it); dispatch loop with AR_SPAWN_ROLE + qualified leaf keys; the FAILED-DELIVERABLE RULE (task_reopen + reshape, never redo siblings); integration duty master->super in a per-edge orchestrator worktree (C-11, the topology's single home with the strict branch stack and two conflict modes); super-exit seam; developer-gated landing tail; self-improvement close. Hat-collapse rule: flat run -> manager hat; session scale -> hands-on build with the worker's discipline and the owner's closeout tail. Spirit test remains this seat only; hand-off protocol (dry-run -> notify-and-stop -> report + junction table) unchanged.

As of the L8 de-harnessing pass the file carries a Sub-Agent Fan-Out capability-doctrine section (any harness that has fan-out: sub-agents write templated durable reports and return compact summaries; AR mutations stay in the main loop; capped by orchestration.concurrency.maxSubAgents; a harness without the ability runs the analyses sequentially) — the content formerly held by the deleted roles/orchestrator.claude-code.md overlay, generalized off the vendor.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
