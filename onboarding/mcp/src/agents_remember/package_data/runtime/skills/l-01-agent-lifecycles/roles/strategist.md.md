# l-01-agent-lifecycles/roles/strategist.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `304de8e272fd9128d035b805f317da5f3090865c` |
| lastVerifiedCommitDate | 2026-09-17T12:34:11+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the optional sprint-bound strategist lifecycle. The canonical
`skills/l-01-agent-lifecycles/roles/strategist.md` owns doctrine; the sync process publishes this
exact runtime artifact.

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block. It declares its shared sources
with `**Inherits:**` rather than restating them (`core/authority.md`, `core/invariants.md`,
`core/loop.md`, `core/acceptance.md`, `operations/orientation.md`, `operations/planning.md`); the
planning method, the requirement-compilation precedence, and the loop's review-round rules now live
once in `operations/planning.md` and `core/loop.md`.

Its boundary is unchanged and re-stated structurally: **reader, not mutator** — the strategist reads
the whole in-flight portfolio, proves it coherent, resolves dependency chains, establishes blast
radius and priority, chooses the topology explicitly, and delivers the orchestration-task draft. It
never edits task docs, raises gates, mutates Git, or addresses an orchestrator occupant. This role
file names `roles/manager.md` only to name the seat it hands to, which is its one sanctioned sibling
reference.

## Code Commentary

### Logic

The synchronized caller matrix makes strategist target-only: the architect is its ordinary
plane-hosted caller, while an identity-free launcher may target it only for explicit
developer-declared takeover. Dispatch/tools rows remain structural documentation, not settings
keys.

After developer approval, the architect may dispatch `(sprint document, strategist)` when the
reasoned topology choice or portfolio classification is absent/stale—not merely because a valid
graph-less sprint has no persisted graph. The strategist is read-only: it analyzes portfolio
dependencies, derives one effective priority per candidate, chooses either an evidence-backed
explicit graph or the graph-less atomic-sequential default, and drafts the
orchestration task.
`message_parent` carries clarification or quo-vadis escalation to the architect, the architect rules
the plan, and the orchestrator adopts it. The role never edits task docs, raises gates, mutates Git,
or addresses an orchestrator occupant.

The developer ruling governs that default: nothing serializes a graph-less sprint, because a sprint
with no `executionGraph` declares no dependencies to honour — `atomic-sequential` describes the
sprint's shape (every commanded master executes atomically), not a serialization mechanism, so
independent atomic masters proceed concurrently, no master is held because another is selected, and
no work is retired. Per-contract activation records each canonical contract's own
`reconciling -> active` transition, so masters that share one protected source pair never share that
state and one master's selection never pauses or excludes another; the closeout queue only projects
each contract's own active/reconciling/vacant waiting candidates. Only an explicit graph's
`predecessor-incomplete:` waves gate anything.

### Conventions

Use cited evidence for dependency and coherence claims, preserve the draft/adoption boundary, and
edit only the canonical role before synchronization.

### Invariants And Boundaries

- The strategist remains a sprint-bound reader, not a mutator or orchestrator child.
- Durable artifacts, not runtime identity, carry the result across occupant replacement.
- Planning, classification, priority, dependency, and coherence judgments are mandatory; a
  persisted `executionGraph` is optional.
- This packaged artifact must remain byte-identical to the canonical role.

### Todos

None recorded.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; curation is the exception — the curator always runs the complete memory-quality operation, and closeout and integration carry its completed result as a prerequisite rather than rerunning it. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

When approved, the strategist is spawned by the architect and hands its plan back for ruling and
adoption.

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Lifecycle — Strategist` | skills/l-01-agent-lifecycles/roles/strategist.md:1-16 |
| The role declares the readable order, its inherited sources, and the knob block after the handoff section. | `**Inherits:**`; `## 6 — Completion And Handoff`; `## Knobs, Tool Surface, And Dispatch Authority` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:14-16; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:164-179; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:180-197 |
| The reader-not-mutator boundary the role must preserve. | "**Authority boundary to preserve: reader, not mutator.**" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:43-43 |
| The strategist names `roles/manager.md` only to name the seat it hands to, which is its one sanctioned sibling reference. | `SANCTIONED_SIBLING_REFERENCES` | mcp/tests/test_role_instruction_corpus.py:84-89 |
| The router's role registry still names the strategist row, and the loop doctrine now has its single home in `core/`. | `## The Role Registry`; `# Core — The Three-Party Loop (one home — this file owns the loop doctrine)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:67-86; skills/l-01-agent-lifecycles/core/loop.md:1-1 |
| The orchestrator that adopts the ruled topology or authors the same complete orchestration task after a sanctioned strategist skip. | `# Lifecycle — Orchestrator` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:1-14 |
| The deliverable's template separates mandatory planning from optional persisted graph structure and defines complete graph bootstrap. | `# Orchestration-Task Template` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md:1-215 |
| The plan-review criteria re-derive effective priority and validate either topology choice. | `# Criteria Catalog — Plan Review (the strategist loop)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md:1-140 |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260815-DAG-L14 Doctrine Sync

The strategist adoption payload is updated to the atomic `attach_master` flow and the first-class
sprint seats structure.

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

## 260815-DAG-L2 Evidence-Cited Topology Planning

Initial facts are architect-compiled; runtime-reshape facts arrive from the orchestrator through
the architect. The strategist classifies organizational versus atomic execution, builds the exact
topology choice, and records dependency meaning, blast radius, priority, blockers,
reprioritization, and leaf moves in one canonical Judgment Register. When an explicit
activity-on-node graph is justified, every selected relation cites evidence and its owning judgment
id; otherwise the artifact records the reasoned graph-less atomic-sequential default. In that
default canonical commanded-master order is the stable equal-priority tie-break and nothing
serializes the masters — a graph-less sprint declares no dependencies, so independent masters
proceed concurrently, no master is held because another is selected, and no work is retired — and no
full-integration edge may be fabricated from the activation boundary. Large size alone
never makes a master atomic.

## IAS Graph-Less Activation Choice

The synchronized strategist role keeps dependency planning separate from runtime selection.
Per-contract activation records each canonical contract's own `reconciling -> active` transition and
serializes nothing across masters: masters that share one protected source pair hold independent
records, so one master's selection never pauses, replaces, or excludes another, and the only
activation waiting reason is `atomic-series-reconciling` for that contract's own in-flight
reconciliation. The corrected shipped text says the same at its own `:133-136` — "canonical
commanded-master order is the stable tie-break and nothing serializes the masters". Queue or
selector state cannot veto task authoring or substitute for an evidence-backed relation judgment.

## 260821-DAGQC-L4 Optional Graph And Adoption Sequence

Each schedulable candidate has one effective priority: use its candidate override when present,
otherwise inherit the owning-master default; never combine them or retain duplicate current rows.
The strategist records this judgment input, while the orchestrator compares effective grades
across the portfolio.

A graph-less plan remains fully planned. It classifies every master and records dependency,
priority, coherence, and topology reasoning, then adoption stops after all `attach_master` calls.
If an explicit graph is later chosen, complete every master attachment first and send one
`author_execution_graph` batch with the full node set plus evidence-backed edges. The existing
`add_edge` examples already carried `judgmentId`; no example repair was invented.

## CCR-L42 current candidate

A successor strategy review now carries the sealed issue list, fixed/unfixed dispositions, and subset rule; it cannot perform a new portfolio sweep, add a lens or route, or turn an outside-list observation into a finding. Three rounds remain the ordinary maximum and further work requires developer authorization.

## Update History

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. SOURCE UNCHANGED BY THIS LEAF; card prose falsified by CAPS-R18@v1. Replaced the shared transaction-boundary boilerplate sentence, which presented full memory quality as an explicit request, with the completed-curation rule.
- 2026-09-16T20:45+02:00 — owning-seat merge resolution (source-line convergence): the
  `governingOverview` field and its link were restored to `../../../../../../../overview.md`.
  The 2026-09-16T08:01 metadata repair above dropped one path level — this card sits one directory
  below the skill's `SKILL.md` card, so the target it names (the MCP package overview,
  `onboarding/mcp/overview.md`) needs seven levels up, not five. The five-level value resolved to
  `onboarding/mcp/src/agents_remember/overview.md`, which does not exist, so the card pointed at a
  missing file while its own text claimed the MCP package overview. No content claim changed; only
  the path. Verification metadata is unchanged and stays closeout-owned.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body updated for the corpus consolidation.**
  The canonical strategist role was rewritten (197 lines) into the corpus's readable order and declares
  its inherited sources with `**Inherits:**`. Updated Purpose with the readable order, the inherited
  sources, where the planning method and loop rules now live, and the re-stated **reader, not mutator**
  boundary plus its one sanctioned sibling reference. Repo-Internal References: two citations were
  repointed because their targets moved (`## The Three-Party Loop …` left `SKILL.md` for
  `core/loop.md`; the orchestrator range `:1-619` no longer exists and is now `:1-14`), the canonical
  range was corrected, and the `"nothing serializes the masters"` row was **removed** — the rewritten
  strategist file no longer carries that literal anchor string (the rule is preserved in the role's own
  topology text and in `reference/rulings.md`). **Metadata repair:** `governingOverview` pointed at `../../../../../../../overview.md` (the repository root overview) while its link text said "MCP package overview"; corrected to `../../../../../overview.md`, and the missing blank line between the metadata table and `## Governing Overview` was restored. Verification metadata remains closeout-owned — the source is uncommitted, so no stamp was advanced and no commit hash invented.

- 2026-09-13T15:02:41+02:00 — 260831-LOCR-L36 round 2 shipped-text correction (real body update for
  this changed source): removed the stale source-pair-selected/source-pair-activation prose from the
  Logic paragraph, the 260815-DAG-L2 topology paragraph ("selecting another master may logically
  pause the former"), and the IAS Graph-Less Activation Choice section, and replaced it with the
  developer ruling — nothing serializes a graph-less sprint, `atomic-sequential` describes sprint
  shape (every commanded master executes atomically) rather than a serialization mechanism,
  independent masters proceed concurrently, per-contract activation records each contract's own
  `reconciling -> active` transition so masters sharing one code/memory source pair never share that
  state, the queue only projects each contract's own active/reconciling/vacant waiting candidates,
  and only explicit `executionGraph` waves gate on `predecessor-incomplete:`. Added the corrected
  shipped citation at `strategist.md:133-136` ("nothing serializes the masters") and re-grepped every
  other range: canonical `strategist.md:1-263`, `l-01 SKILL.md:119-136` and `:218-421`,
  `orchestrator.md:1-619`, `orchestration-task.md:1-215`, `plan-review.md:1-140`. Source
  documentation only; verification metadata remains closeout-owned and no acceptance or test claim
  is made.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: A successor strategy review now carries the sealed issue list, fixed/unfixed dispositions, and subset rule; it cannot perform a new portfolio sweep, add a lens or route, or turn an outside-list observation into a finding. Three rounds remain the ordinary maximum and further work requires developer authorization.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 synchronized architect-owned strategist dispatch,
  explicit ambient takeover, and fixed structural-row ownership. Verification remains
  closeout-owned.

- 2026-08-26T08:45+02:00 — Restored the canonical Docs reference section for this changed
  synchronized strategist-role card.

- 2026-08-26T05:20+02:00 — Reconciled the generated strategist role with graph-less source-pair
  activation and pause-without-retirement semantics. Verification remains post-Dagger-owned.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: removed graph absence as a strategist trigger,
  recorded effective-priority override/default semantics, preserved graph-less planning, and made
  first graph adoption one complete nodes-plus-edges batch. Canonical/generated sync is complete;
  Dagger acceptance remains closeout-owned and pending.

- 2026-08-20T05:10+02:00 — 260815-DAG-L14: adoption payload updated to the atomic
  `attach_master` flow and seats structure. Verified at code commit 2f494982.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized fact/judgment separation, graph-edge
  traceability, and dependency/risk-driven master classification. Verification remains
  closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `strategist.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 6 citation anchors across 5 reference claims; scoped recheck clean (0 findings).

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: superseded mandatory-precondition wording
  with architect-proposed, developer-approved dispatch; preserved reader-not-mutator and the
  unconditional artifact duty of an already-running strategist; recorded the orchestrator-owned
  sanctioned-skip path and added the governing-overview backlink. Verification metadata remains
  pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added
  role-seat immutability; clarified that drawing-board feedback and quo-vadis contradictions go
  through the architect relay while the strategist remains the reader-not-mutator portfolio
  planner for backend orchestration. Sync-propagated bundle copy. Verification metadata pinned
  until closeout stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): Knobs table gained the three
  free-form escape-hatch rows (launchArgs / sessionCommands / promptKeywords, settings-only, never
  validated) and the knob footer now includes the rolesPerLevel per-level override and the
  harnesses.md manual pointer. Sync-propagated bundle copy. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-1): knob-table harness example fixed to the registry id `claude`. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-8): duty 6 aligned with the Tool Surface — the orchestration-task artifact write is unconditional; inbox posting is the when-wired delivery channel, the final playback message the fallback. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `roles/strategist.md` (leaf 260703-L12): the spawn-first sprint planner, mandatory precondition for any orchestrated run; the eight-phase method with two-sided touch surfaces and evidence-cited edges; reader-not-mutator boundary; drawing-board rounds with the 3-full-round cap. Verification metadata pinned until closeout stamps the L12 commit.
