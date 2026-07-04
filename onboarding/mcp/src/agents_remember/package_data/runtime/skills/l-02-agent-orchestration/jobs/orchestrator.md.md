# l-02-agent-orchestration/jobs/orchestrator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-04T13:03+02:00                      |
| lastVerifiedCommitHash | `5ab7550b256fe4cd82514b81f455aa9026c0d7de` |
| lastVerifiedCommitDate | 2026-07-04T13:10:34+02:00|

## Purpose

This file is the portable **orchestrator** job the `l-02-agent-orchestration` frame houses at the
orchestrator seat — role + lens in one file. It is the one job that carries the **spirit test** (and
the test is **orchestrator-only**). The seat owns the portfolio, the master-level dependency DAG,
dependency-ordered manager dispatch, and the accumulative super integration branch, and is the single
point of contact for the developer. It also owns the master-to-super integration duty: consume the
manager handover packet, check the seam verdict, integrate from a super-sourced orchestrator worktree,
carry memory through C-11, map the ledger, and release the next ready masters. This card explains the
seat's flow so an agent onboarding into the orchestrator seat gets the job contract without re-deriving
it from the transcript; the harness specifics live in the `jobs/orchestrator.claude-code.md` overlay.

## Code Commentary

### Logic

This packaged file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-02-agent-orchestration/jobs/orchestrator.md`; the authored skill source owns the wording, and
this is the synced runtime mirror. Drawn as the **ORCHESTRATOR** model on the FlowTab canvas
(`dashboard/src/panels/flowModels.ts`).

**What the seat is.** One per orchestration job; its seat is the **first coordination leaf** of the
series (a `task_doc` subTask leaf, no enclosure at rest). Developer-requested, never self-spawning. Its
analysis substrate is the **memory system** — route indexes, onboarding, `grepai_search`, and the
code-graph (`cgc_*`) tools — and **orchestrator quality ∝ memory-repo quality**: the onboarding system
is the entry gate to big-ticket orchestration and hidden planning-surface collisions should "tingle the
spider web." Its own artifacts are the most important in the system (only it sees the whole picture) and
must survive compaction, termination, and clears.

**Lens.** Opening move is the **portfolio phase** — streamline the requested masters (coherence
*before* sequencing), not dispatch; retrieval leans breadth across the portfolio; decide default is a
**master-granular dependency DAG** and a dispatch order.

The duties spine:

1. **Seat & profile** — take the first coordination leaf; run the frame's profile-fit check first and
   **takeover spawn** the correct profile with a conversation-handover packet before any analysis if
   the session is wrong for the job.
2. **Portfolio phase (streamline before sequencing — non-linear)** — route-coherence scan (route
   indexes · onboarding · `grepai_search` · `cgc_*`; sub-agents write durable
   `templates/impact-analysis.md` reports); the **integrity bulwark** = check planned changes against
   each other **and against the past** (planned-vs-planned AND planned-vs-past — the defense against
   "fixed one thing, broke two others"), which also **adversarially reviews each designer's output**
   (the designer is master-scoped, so cross-master and future-master collisions surface here); reshape
   proposals (leaf **moves** — planning-status only, actually moved with a decision-log entry on each of
   the receiving and losing masters; foundation-master extraction; mixing masters first-or-last);
   **never interleave dispatch** — reshape master boundaries so the DAG is expressible at **master
   granularity**.
3. **Portfolio plan gate** — the streamlining output is a **proposal**; no silent rewrites of
   developer-accepted tasks. One wholesale developer review of the reshaped portfolio + DAG + dispatch
   order; on approval, create the super integration branch (based off main).
4. **Dependency-ordered dispatch loop** — for each **ready** master (its deps integrated into super):
   `spawn_agent_session(manager)` with the manager job + master context packet; monitor + steer (turn
   reports · nudges · escalation intake, applying the spirit test to plan deltas that escalate up);
   receive the master-handover packet (incl. the **master-exit adversarial verdict**); then run the
   integration-duty procedure in an **orchestrator worktree** with super as source. Loop until the DAG
   drains.
5. **Super-exit seam & developer handover** — spawn the **super-exit adversarial reviewer** over the
   whole super branch, attach its verdict, hand super to the developer for a **whole-behavior review**;
   a rejection decomposes into **fix leaves** (reactive dispatch); on approval super → main PR (remote
   merge) + memory carry-over to main + push, per `system/git-workflow.md`.
6. **Close with self-improvement proposals** — propose changes for future tasks grounded in the
   accumulated backdrop; **proposals only, no automated self-modification**; the developer decides.
   `lifecycle_end` records the terminal state.

**The spirit test — this seat only** (developer correction 2026-07-04; not ported to managers/workers):
a change **within the spirit** of what the developer accepted → the orchestrator **acts on its own** and
writes a **decision-log entry** (covers leaf moves against planning-status masters, inserted/appended
fix leaves, mid-series reshaping — the integration branch is the safety net); a necessary change that
goes **against the spirit** → **raise it for a joint decision** with the developer (the
unanticipated-wrench case). Only the orchestrator holds the global view to judge a collision, which is
why the test is confined to this seat.

**Conflict resolution — exactly two modes.** **Up-front (preferred):** an overlap identified during
streamlining → extract the shared logic into its own **foundation master, implemented first** (leaf
moves are the mechanism for pulling shared logic in front of dependents). **Post-hoc:** an overlap only
visible in the returned integration branches → **remediate on the super integration branch worktree**
(code dedup + memory single-siding at merge time; defer the memory write to the strand that integrates
second, ideally keeping memory single-sided so no conflict materializes).

**Integration duty — master to super.** The orchestrator treats each completed master as a higher-level
leaf-to-master edge: consume the manager's handover packet, check the master-exit verdict, open an
orchestrator worktree sourced from the current super branch, merge/replay the master branch into super
with the same C-09/C-11 mechanics, carry memory with C-11, keep duplicate-memory conflicts
single-sided, run memory quality, record the ledger mapping from accumulated master commits to the new
super memory line, then advance the ready set for downstream masters. The final super-to-main edge
keeps the same invariant but lands through the PR-gated main tail in `system/git-workflow.md`.

**Sequenced backlog.** Gh-route master finalize/archive and first-class parallel-master reconcile remain
manual orchestrator duties until the task-doc-tooling leaves
`260703_task-doc-tooling-repair/08_retire-master-series.md` and
`260703_task-doc-tooling-repair/09_parallel-master-reconciliation.md` land.

**Self-improvement loop.** The orchestrator is the first seat where self-improvement is meaningful;
register improvement potential and encountered issues in the durable notes **as you work** and surface
them as grounded, reality-anchored proposals at handover — still proposals, the developer decides.

**Artifact obligations.** Durable notes + reports (the system's most important, kept current as you
work); **sub-agent durable reports** — fan-out sub-agents **write** templated reports
(`templates/impact-analysis.md`, `templates/onboarding-coherency.md`) while **AR state mutations**
(`task_doc`, gates, `spawn_agent_session`, closeout) **stay in the main loop** (design addendum item 5,
the developer overrule of the read-only phrasing; see `jobs/orchestrator.claude-code.md` for the Claude
Code realization); decision-log entries for every spirit-test "act on my own," every leaf move, every
conflict-mode choice; a self-improvement report at close.

### Conventions

Role + lens in one file (borrowed D10). The knob block carries portable defaults (harness `claude-code`;
model `highest-reasoning` — portfolio blast-radius judgment wants the strongest model; effort `high` —
the bird's-eye seat, effort is not the place to economize; tools = full bird's-eye + orchestration:
route indexes · onboarding · `grepai_search` · `cgc_*` · `read_ar_files` · `task_doc` · gates ·
`spawn_agent_session` · worktree/C-11). Settings.json `orchestration.roles.orchestrator` overrides these
(job base < variant < settings). Comms follow the frame's protocol (inbox durable queue · stdin push
delivery · escalation intake), with the orchestrator as the last resolver before the developer.

### Invariants And Boundaries

The seat is developer-requested and never self-spawning. Profile-fit is checked before any analysis;
wrong profile forces a takeover spawn. Streamlining is a proposal — no silent rewrites of
developer-accepted tasks; the portfolio plan gate is one wholesale developer review. The DAG must be
expressible at master granularity — dispatch is never interleaved at leaf-level cross-deps; instead
master boundaries are reshaped. A master is dispatched only when its dependencies are integrated into
super, and downstream masters are released only after the orchestrator records the master-to-super code
tip, memory tip, and ledger mapping. The **spirit test is orchestrator-only** — within-spirit acts get a decision-log entry,
against-spirit changes are raised for a joint decision. Conflict resolution has exactly two modes
(up-front foundation-master extraction vs post-hoc super-branch remediation). Self-improvement is
**proposals only — no automated self-modification**. Sub-agents write durable reports; **AR state
mutations stay in the main loop** (the orchestrator is the only mutator). `spawn_agent_session` is the
L2 spawn tool, **not yet implemented** — treat its references as the contract a dispatch/takeover will
call. The 260630-derived master finalize/archive and parallel-master reconcile primitives are not live
tooling yet; until their task-doc-tooling leaves land, the orchestrator records manual C-09/C-11
operations in durable notes. Continuity lives in the durable notes/reports and `task_doc`, never in the
transcript.

### Todos

No current todo is recorded in this job file.

### Docs References

No external domain documentation applies to this repository-local orchestration job.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The orchestrator job is the payload the `l-02-agent-orchestration` frame houses at the first
coordination leaf; its harness specifics and its integration mechanic live in sibling files.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This job is the payload the frame selects at the orchestrator seat; the frame owns the contact points and the escalation ladder this seat tops. | L1-L23; L146-L149 | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/SKILL.md) |
| The integration-duty procedure consumes the manager handover packet, checks the verdict, integrates from a super-sourced worktree, carries memory, maps the ledger, and releases the next ready masters. | L92-L123 | [jobs/orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.md) |
| The Claude Code overlay realizes the sub-agent fan-out (durable reports; AR mutations stay in the main loop) and never restates these duties. | n/a | [jobs/orchestrator.claude-code.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/jobs/orchestrator.claude-code.md) |
| Master→super and super→main integration is the `c-11-memory-carryover-from-branch` mechanic — the universal integration mechanic at every level. | n/a | [c-11 SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-11-memory-carryover-from-branch/SKILL.md) |
| Fan-out sub-agents write into the report-template library the seat consumes (impact analysis, onboarding coherency). | n/a | [templates/impact-analysis.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-02-agent-orchestration/templates/impact-analysis.md) |

## Cross-Repo References

No sibling repository evidence is needed for this repository-local orchestration job.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

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
