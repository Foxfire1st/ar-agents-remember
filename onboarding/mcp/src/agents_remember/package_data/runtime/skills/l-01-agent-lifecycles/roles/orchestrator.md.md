# l-01-agent-lifecycles/roles/orchestrator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-05T01:30+02:00 |
| lastVerifiedCommitHash | `277f27a33b35aed8235cbb3c1ae2b5633cc88b22` |
| lastVerifiedCommitDate | 2026-07-05T01:30:08+02:00|

## Purpose

The developer-facing lifecycle - the seat every developer session runs, whether it fixes one typo or orchestrates a portfolio. Absorbs the retired session-job spine as its phase axis (request -> trust-checkpoint -> reframe-research -> decide -> build -> close) and adds Orchestrated Mode, where the build phase becomes dispatch. Solo work is the degenerate portfolio: same lifecycle, hands-on build.

## Code Commentary

### Logic

Sync-propagated copy of the canonical `skills/l-01-agent-lifecycles/roles/orchestrator.md`. Phase axis: trust checkpoint (context_packet facts before trusting memory/providers; approval-gated drift handling), reframe+research (read_ar_files paired reads until the build decision, c-04 strategy routing, lens pick from ../lenses.md, evidence-tied research report, PLAN GATE), decide (research-only exit / session-scale worktree via c-09 with intent hand-off / portfolio-scale -> Orchestrated Mode; openQuestions doctrine), build (same-pass c-05 onboarding, tools.md checks green, freshness watch + early worktree_sync), close (closeout preview/apply with commit gate, integrate + developer-gated push, ledger mapping, finalize incl. task-doc steps; when workers were dispatched, the OWNING SEAT - not the worker - runs the closeout tail). Hand-off protocol: dry-run -> lifecycle_turn_end_notification as last tool call -> report prose -> STOP, with the junction/parked-gate table and the lifecycle_gate fallback. Orchestrated Mode: profile check + takeover spawn; portfolio phase (route-coherence scan, integrity bulwark, reshape proposals, master-granular DAG only); portfolio plan gate; dependency-ordered dispatch (spawn_agent_session(manager) with AR_SPAWN_ROLE env + qualified leaf key); THE TOPOLOGY'S SINGLE HOME (strict branch stack, C-11 at every edge, integration duty master->super in an orchestrator worktree sourced at super, exactly two conflict-resolution modes, the T8/T9 manual backlog); super-exit seam with reviewer verdict as evidenceRefs; close with grounded self-improvement proposals (never automated self-modification). The spirit test lives here and only here.

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
