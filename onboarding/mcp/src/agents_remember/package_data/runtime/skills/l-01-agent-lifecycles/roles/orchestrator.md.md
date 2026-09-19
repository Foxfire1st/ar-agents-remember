# l-01-agent-lifecycles/roles/orchestrator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `47570cd827428c171613c8cb01e01f0b1cb26f73` |
| lastVerifiedCommitDate | 2026-09-20T01:58:41+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the sprint-bound backend orchestrator lifecycle. The canonical
`skills/l-01-agent-lifecycles/roles/orchestrator.md` owns doctrine; the sync process installs this
exact artifact.

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block. It declares its shared sources
with `**Inherits:**` rather than restating them: all five shared blocks (`core/authority.md`,
`core/invariants.md`, `core/lifecycle-frame.md`, `core/loop.md`, `core/acceptance.md`) plus
`operations/orientation.md`, `operations/planning.md`, `operations/coordination.md`,
`operations/review.md`, `operations/closeout.md`, and `operations/recovery.md`. **This role file is
the one home of the super-integration-branch topology** — the router now carries only an orientation
diagram and sends the canonical graph, execution-nature classification, ready-frontier recomputation,
landing procedures, conflict routing, and leaf moves here.

## Code Commentary

### Logic

The synchronized caller matrix makes the orchestrator an ordinary plane-hosted caller for direct
manager/system-specialist children and an ambient target only for explicit developer-declared
takeover. Dispatch/tools rows remain structural documentation, not settings keys.
The explicit takeover path converges on the existing canonical sprint seat and does not manually
replace a viable occupant or duplicate its pinned brief.

The orchestrator owns durable portfolio execution behind the architect. It dispatches managers and
system specialists with `dispatch_agent` on canonical master or sprint documents, adopts the
architect-ruled topology choice and its graph only when present, processes durable handovers, and
decides the one open master handover gate by master document and kind. A developer-sanctioned
strategist skip transfers the same complete planning duty to this seat; it does not waive
classification, priority, dependency, coherence, or topology reasoning. It never handles a child
occupant id, exact readiness, raw inbox address, attachment id, or packet-carried gate id. Optional
designer/strategist and plan-review reviewer seats are architect children; leaf/master-exit
reviewers are manager children, and super-exit reviewers are orchestrator children.

The sprint super-exit reviewer generation is stamped with this orchestrator as structural parent,
so its signals and retirement authority cannot be confused with the architect-stamped plan
reviewer that uses the same sprint document and role address at a different time.

### Conventions

The role runs an event loop over durable portfolio state, relays developer decisions to the
architect, and uses proper role seats rather than orchestration-native sub-agents. Edit the canonical
role, then synchronize.

### Invariants And Boundaries

- Seat identity is `(canonical task document, role)` and occupant replacement is plane-owned.
- Structural dispatch and structural gate decision fail closed on missing or ambiguous authority.
- The orchestrator is backend-only and does not become manager, worker, reviewer, curator, or
  developer-facing architect.
- A persisted `executionGraph` is optional; the explicit graph-less choice runs the
  per-contract-activated atomic-sequential default, which describes the sprint's shape — every
  commanded master executes atomically — and serializes nothing across masters, while retaining all
  planning judgments.
- Task-document mutation is upstream of runtime selection; affected queue projections are
  invalidated and rebuilt after planning changes.
- The queue observes activation and owns no lifecycle, commit, or selection evidence.
- This packaged artifact must remain byte-identical to the canonical role.
- The orchestrator is the only home of the super-integration topology; the router deliberately keeps
  an orientation diagram instead of restating it.
- The orchestrator names `roles/strategist.md` and `roles/designer.md` only to dispatch those seats,
  which are this role's sanctioned sibling references.

### Todos

None recorded.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; curation is the exception — the curator always runs the complete memory-quality operation, and closeout and integration carry its completed result as a prerequisite rather than rerunning it. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The synchronized role reads the ruled plan for its requirement-corpus references, the reasoned topology choice, every commanded master's executionNature, and any executionGraph. | `executionNature`; `executionGraph`; "the reasoned topology choice" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:19-21 |
| The orchestration-task template defines one effective priority, graph-less adoption, and the full nodes-plus-evidence-edges bootstrap. | `## Rules`; "## Topology Choice And Canonical executionGraph Adoption Payload" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md:14-72; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md:127-168 |
| Root skills are canonical and the sync script publishes byte-identical package and harness copies. | `SkillTarget`; `TARGETS` | scripts/sync-skills.py:26-29; scripts/sync-skills.py:43-56 |
| The shipped role states that independent ready masters run in parallel up to the configured maximum, and that only an atomic master waits for its explicit graph predecessors. | `maxParallelMasters`; "waits for its explicit graph predecessors" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:111-112 |
| Each release and landing is per execution nature, and the seat releases only the exact first-ready generation the projection admits. | "Release and land per execution nature"; "You release only the exact first-ready generation the projection admits" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:67-68 |
| The shipped role selects from current truth rather than a queue row, and it never mutates an old queue row. | "selecting from current truth rather than a queue row"; "never mutate an old queue row" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:36-36; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:184-185 |
| The shipped topology rule gives only an atomic master an intermediate integration branch off super, and its completed block lands on super once. | "owns an intermediate integration branch"; "its leaves branch from that block, and the completed block lands on super once" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:55-62 |

## Cross-Repo References

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

The orchestrator consumes targeted worker checks and scoped curator checks. Full quality, full tests,
full memory quality, certification, and review remain explicit operations; closeout and integration
do not infer a quality gate or launch those tools automatically.

## 260815-DAG-L14 Doctrine Sync

The seat-row prescription is replaced by the first-class sprint seats structure plus the atomic
`attach_master` adoption flow: sprint seats live on the sprint document (`SprintSeat` rows), and
commanding a master is one validated `task_doc.attach_master` batch (typed `masterRef` row +
membership slug + nature assertion when needed + graph node only when a graph already exists) —
never the three-write manual flow.

## L23 Final Candidate Disposition

The orchestrator observes closeout and integration through canonical task status. The ordinary path
publishes the authorized Git transaction; any explicit quality or review operation remains with its
own lifecycle owner.

## R39 Generic Quality Altitude

The orchestrator resolves executor, environment, retry, resource, and evidence contracts from
repository memory rather than supplying Agents Remember-specific instructions. Leaf closeout and
master integration remain the only acceptance owners.

## 260815-DAG-L2 Ready-Frontier And Landing Authority

The orchestrator recomputes the ready frontier after every material event and records rationale,
evidence, author, confidence, and supersession before a priority/queue judgment changes selection.
Organizational leaves land directly as released; the last one forms the exact proposed final
candidate and receives the full master check before super moves. Atomic masters expose no partial
leaf state to super; the per-contract activation record lets two sprint-commanded atomic masters
that share one protected source pair hold independent records, so activating one never auto-pauses,
replaces, or waits on another, while the separate landing authority serializes protected-ref
movement. Nothing serializes the graph-less sprint itself (developer ruling): a sprint with no
`executionGraph` declares no dependency, so independent atomic masters proceed concurrently and only
explicit graph waves still gate on `predecessor-incomplete:`. Integration refs are never repair
workbenches; fixes return to an owning/reopened or new scoped leaf.

## 260815-DAG-L13 Scheduling Default Doctrine

Adoption doctrine states that a sprint adopted without an `executionGraph` runs the
atomic-sequential default. If the ruled plan
later selects an explicit graph, attach every commanded master first, then bootstrap the graph in
one complete `task_doc.author_execution_graph` batch containing every node and evidence-backed
edge; only an established graph is edited incrementally. The `migrate_execution_topology`
legacy-cutover reference is gone.

## 260815-DAG-L15 Review-Doctrine

Job O gains a review-independence and evidence-type paragraph: this seat never reviews its own
leaf or plan implementation as the "independent" route reviewer (260815-DAG L7/L8/L9 were
orchestrator self-reviews), and never passes a requirement on evidence of the wrong class —
rendering/visibility needs mounted-UI proof, scheduling needs operation-level proof, data-model
needs artifact-level proof. Route reviews come from a distinct reviewer seat; this seat reviews
only at super-exit, through a spawned reviewer.

## 260821-DAGQC-L4 Planning And Scheduling Closure

Every ready candidate resolves to one effective priority before comparison: its candidate-specific
row overrides the owning-master default; otherwise the default is inherited. The orchestrator owns
portfolio-wide comparison of those effective grades, while graph or commanded-master order is only
an equal-grade tie-break. A missing graph is not a stale-plan signal by itself. The signal is a
missing/invalid topology choice, missing execution nature, or materially stale dependency,
classification, or priority model.

Graph-less adoption attaches all masters and stops, selecting atomic-sequential execution. Explicit
graph adoption from that state attaches all masters first and then publishes one complete
nodes-plus-evidence-edges batch. No fake graph, partial bootstrap, runtime fallback, or mandatory-
graph compatibility path exists.

## IAS Per-Contract Activation, Queue, And Conflict Boundary

Before atomic implementation exposure, manager/worker dispatch activates the requested canonical
contract as `reconciling`, source-syncs that contract's two protected branches, and publishes
`active` only when both bases are current. The activation record is keyed by the series contract,
not the protected source pair, so two atomic masters commanded by one sprint and sharing that pair
hold independent records: activating one never auto-pauses, replaces, or blocks the other, and the
only activation waiting reason is `atomic-series-reconciling` for the contract's own in-flight
reconciliation. Reviewer/curator inspection does not activate a contract, and nonterminal sibling
contracts keep their chats, processes, worktrees, contracts, and claimed journals untouched.

Task authoring never waits for activation or queue permission. The queue is a disposable observer
of active/reconciling/vacant waiting facts. Malformed activation state fails closed only for
affected runtime admission/projection and is archived/replaced by a selecting operation; no
contract-presence fallback exists. Technically derivable retained conflicts are resolved through
the advertised continue/cancel operation; only genuine semantic ambiguity returns to the architect.

**Shipped text corrected (260831-LOCR-L36 round 2).** The mirrored runtime role this card
describes — `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md` —
now carries the corrected doctrine in its own text: the graph-less adoption paragraph at `:264-267`
says "canonical commanded order is the stable tie-break, and nothing serializes its masters — a
graph-less sprint declares no dependencies, so independent masters proceed concurrently, no master is
held because another is selected, and none is retired"; the execution-loop paragraph at `:345-347`
says "Per-contract activation records each master's own `reconciling -> active` transition and
serializes nothing across masters", with only the landing lane separately serializing conflicting
protected-ref movement, and that "Queue rows only project each contract's own active/reconciling
waiting facts" (`:350-351`); atomic step 4 at `:409-413` requires "the master's own contract
activation to be `active`" and records that "an unfinished master retains its branch and journals";
and the topology diagram at `:454-456` shows each atomic master on its own branch with one landing
into super. The
earlier shipped-source debt note is therefore removed — a repo-wide grep for `source-pair-scoped`,
`source-pair-selected`, the "logically pauses the former master" admission, one-selected-master-at-a-time
and source-pair activation wording returns 0 hits in the code worktree.

## Update History
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `orchestrator.md.md:108` ("selecting from current truth rather than a queue row", "never mutate an old queue row").
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "atomic master B branch" repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:269-269. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Replaced the CCR-R12@v5 transaction-boundary boilerplate sentence, which still presented full memory quality as an explicit request, and updated the role's own curation sentences to the complete-handoff rule.
- 2026-09-16T20:45+02:00 — owning-seat merge resolution (source-line convergence): the
  `governingOverview` field and its link were restored to `../../../../../../../overview.md`.
  The 2026-09-16T08:01 metadata repair above dropped one path level — this card sits one directory
  below the skill's `SKILL.md` card, so the target it names (the MCP package overview,
  `onboarding/mcp/overview.md`) needs seven levels up, not five. The five-level value resolved to
  `onboarding/mcp/src/agents_remember/overview.md`, which does not exist, so the card pointed at a
  missing file while its own text claimed the MCP package overview. No content claim changed; only
  the path. Verification metadata is unchanged and stays closeout-owned.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: Repaired citations this leaf falsified: the canonical lifecycle corpus was consolidated (the router shrank 620 → 179 lines; all nine role files and several templates were rewritten), so the cited anchors and ranges no longer resolved. No behavioral claim changed — the cited rule was re-pointed at its current home. Verification metadata remains closeout-owned. The `Job P — Portfolio (streamline + plan)` / `Job O — Orchestrate (execute the plan)` row now cites the real (bold-lead, not `##`) anchors at `:102-163` and `:164-306`; the previous `:278-506` exceeded the rewritten file's 459 lines.


- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body updated for the corpus consolidation.** The
  canonical orchestrator role was rewritten (457 lines) into the corpus's readable order and declares
  its eleven inherited sources with `**Inherits:**`. Updated Purpose to record the readable order, the
  inherited sources, and the load-bearing consequence of the consolidation for this file: the
  super-integration-branch topology now has exactly one home here, while the router keeps only an
  orientation diagram. Added two Invariants: that the router deliberately does not restate the
  topology, and that this role's two sibling references (`roles/strategist.md`, `roles/designer.md`)
  are sanctioned dispatch references only. **Metadata repair:** `governingOverview` pointed at
  `../../../../../../../overview.md` (the repository root overview) while its link text said "MCP
  package overview"; corrected to `../../../../../overview.md`, and the missing blank line between the
  metadata table and `## Governing Overview` was restored. Verification metadata remains
  closeout-owned — the source is uncommitted, so no stamp was advanced and no commit hash invented.

- 2026-09-13T15:02:41+02:00 — 260831-LOCR-L36 round 2 shipped-text correction: removed the
  shipped-source debt row and debt paragraph and replaced them with the corrected shipped ranges —
  the role's graph-less paragraph now says "nothing serializes its masters" `:264-267`, per-contract
  activation "serializes nothing across masters" `:345-347`, queue rows "only project each contract's
  own active/reconciling waiting facts" `:350-351`, atomic step 4 requires the master's own contract
  activation `:409-413`, and the topology diagram shows one landing per atomic master `:454-456`.
  Body prose now states the developer ruling (nothing serializes a graph-less sprint;
  `atomic-sequential` is sprint shape, not a scheduling mechanism; independent atomic masters proceed
  concurrently; per-contract activation records each contract's own `reconciling -> active`; only
  explicit `executionGraph` waves gate on `predecessor-incomplete:`), and the Job P/Job O and
  template `## Rules` ranges were re-grepped and repointed to `:183-277`/`:278-506` and `:14-72`.
  Source documentation only; verification metadata remains closeout-owned and no acceptance or test
  claim is made.
- 2026-09-13T14:24:00+02:00 — 260831-LOCR-L36 activation re-keying: rewrote this card's activation
  boundary from source-pair selection with an auto-paused former master to the per-contract
  activation record — each series contract owns its record, the only waiting reason is
  `atomic-series-reconciling`, and a foreign master is never a reason to wait or pause — and
  recorded the shipped-source debt that the frozen mirrored orchestrator role still states the
  removed per-source-pair rule at `:264-265`, `:321-324`, `:344`, `:348`, and `:407-411`, flagged
  for a future code leaf. That debt observation is superseded by the 260831-LOCR-L36 round-2 entry
  above: the shipped text is corrected and the debt note is removed. Source documentation only; verification metadata remains closeout-owned
  and no acceptance or test claim is made.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: recorded the baseline/fix-verification review packet, atomic-child master-review boundary, and explicit three-round/developer-authorization rule in the synchronized runtime role card.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: synchronized the
  orchestrator-stamped super reviewer and its separation from the architect plan reviewer.
  Verification remains closeout-owned.

- 2026-08-30T12:57+02:00 — 260821-ARSPAWN-L3 review correction: synchronized idempotent
  canonical-seat convergence for an explicit orchestrator takeover. Verification remains
  closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 synchronized the orchestrator's plane caller,
  explicit ambient-takeover target, and fixed structural-row boundary. Verification remains
  closeout-owned.

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference headings for this changed
  synchronized orchestrator-role card.

- 2026-08-26T05:20+02:00 — Reconciled the generated orchestrator role with exact source-pair
  selection, pause preservation, separate landing authority, task-authoring primacy, disposable
  queue observation, and agent-owned resumable conflicts. Verification remains closeout-owned.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: made strategist-skip reasoning complete, graph
  persistence and attachment-node creation conditional, priority override/default resolution
  explicit, and first graph adoption one complete nodes-plus-edges batch. Canonical/generated sync
  is complete; Dagger acceptance remains closeout-owned and pending.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: Job O now states review independence — never review
  your own leaf/plan as the independent route reviewer, and match requirement verdicts to their
  evidence class. Verified at code commit de3a0fd9.

- 2026-08-20T05:08+02:00 — 260815-DAG-L14: the seat-row prescription is superseded by the sprint
  seats structure and the atomic `attach_master` adoption flow (canonical + generated copies kept
  identical by `scripts/sync-skills.py`). Verified at code commit 2f494982.


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
