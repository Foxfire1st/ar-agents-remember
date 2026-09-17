# l-01-agent-lifecycles/templates/orchestration-task.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-26T08:45+02:00 |
| lastVerifiedCommitHash | `304de8e272fd9128d035b805f317da5f3090865c` |
| lastVerifiedCommitDate | 2026-09-17T12:34:11+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the orchestration-task template. The canonical template owns the sprint
plan shape; the sync process publishes this exact artifact.

## Code Commentary

### Logic

After developer approval, the sprint-bound strategist drafts the plan for the architect; after a
developer-sanctioned strategist skip, the orchestrator authors the same complete artifact. The
architect rules it and the orchestrator adopts the accepted plan into durable execution form. The
artifact carries cited scope, dependency, blast-radius, effective-priority, risk, topology, and
reevaluation evidence rather than an agent id. Planning is mandatory, while persisted
`executionGraph` structure is optional.

### Conventions

Plans show their evidence per edge and remain drafts until architect ruling and orchestrator
adoption. Edit the canonical template, then synchronize.

### Invariants And Boundaries

- The strategist is a reader and does not mutate task documents.
- Durable plan evidence survives seat-occupant replacement.
- Each candidate has one effective priority: candidate override when present, otherwise the
  owning-master default; the two grades are never combined.
- A graph-less atomic-sequential topology is valid: canonical order is an equal-priority tie-break,
  while per-contract activation lets sibling masters that share one protected source pair proceed
  independently and serializes nothing, because a graph-less sprint declares no dependencies. First
  graph
  adoption occurs only after every master attachment and uses one complete nodes-plus-evidence-edges
  batch.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.


## CCR-R12@v5 Handoff Boundary

This template records the exact checks and their failed or not-run status as handoff evidence, together with the curator's complete memory-quality result. Closeout and integration consume the prepared code, memory-content, and ledger transaction and carry that completed curation as a prerequisite; full code quality, full tests, certification, and review are explicit requests rather than automatic template gates.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Orchestration-Task Template` | skills/l-01-agent-lifecycles/templates/orchestration-task.md:1-215 |
| The strategist role that fills this template and chooses either topology. | `# Lifecycle — Strategist`; `## 3 — Normal Workflow` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:1-16; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:68-135 |
| The plan-review criteria re-derive effective priority and validate either explicit-graph or graph-less topology. | `# Criteria Catalog — Plan Review (the strategist loop)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md:1-140 |
| The shipped template's derived-wave walk now says nothing serializes a graph-less sprint instead of the removed source-pair-selected exposure walk. | "nothing serializes a graph-less" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md:172-174 |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260815-DAG-L14 Doctrine Sync

The orchestration task template documents the atomic `attach_master` adoption flow and the
first-class sprint seats structure.

## L23 Final Candidate Disposition

Orchestration task packets identify review routes, candidate-bound evidence, and the targeted/full
Dagger altitude. Durable operation observation remains task-addressed and excludes worker/job ids.

## 260815-DAG-L2 Executable Plan Shape

The artifact separates a Mechanical Fact Inventory from one canonical Judgment Register. The
nature, relation, blast-radius, priority, blocker, and leaf-move sections are projections that cite
their owning judgment rows. When present, `executionGraph` carries exact `TaskDocumentRef` nodes
and evidence-backed predecessor edges; deterministic waves and blocker positions are derived
rather than persisted. Without it, the reasoned atomic-sequential default uses canonical
commanded-master order only as an equal-priority tie-break and serializes nothing — a graph-less
sprint declares no dependencies, so independent atomic masters proceed concurrently and no master is
held because another is selected — while per-contract activation records each contract's own
`reconciling -> active` transition and the queue only projects each contract's own
active/reconciling/vacant waiting candidates. Runtime
reprioritization records rationale, evidence, author, confidence,
and supersession before queue selection changes.

## 260815-DAG-L13 Scheduling Default Doctrine

The template's adoption rule treats a sprint adopted without an `executionGraph` as running the
atomic-sequential default. All master attachments complete before the first explicit graph is
published in one full `task_doc.author_execution_graph` nodes-plus-evidence-edges batch; later calls
edit the established graph. Graph authoring is never a runtime fallback or ceremonial empty
topology. The `migrate_execution_topology` legacy-cutover reference is gone.

## 260815-DAG Master Full-Gate Repair

Restored the template heading to `## Canonical executionGraph Adoption Payload` (the `executionGraph` qualifier phrase restored); all 9 generated copy trees are byte-identical via `scripts/sync-skills.py`.

## 260821-DAGQC-L4 Effective Priority And Topology Choice

The Priority Register distinguishes candidate-specific rows from owning-master defaults. Resolution
is deterministic: use the candidate row when it exists, otherwise inherit the master row; never
combine both, and reject duplicate current rows for one subject. The orchestrator retains
portfolio-wide comparison of the resulting effective grades.

The topology section now makes `explicit executionGraph` and `graph-less atomic-sequential default`
peer ruled choices. A strategist skip changes the author, not the artifact's full reasoning duty.
For graph-less adoption, attach every master and stop. To choose a graph from that state, complete
all attachments and publish every node plus all evidence-backed edges in one batch. The shown
`add_edge` example already had `judgmentId`; no code or documentation fix was fabricated.

## IAS Graph-Less Walk Correction

The generated template now asks the plan to record canonical tie-break order plus per-contract
activation as the implementation-exposure boundary, where each canonical series contract owns its
own record and the only waiting reason is `atomic-series-reconciling` for that contract's own
in-flight reconciliation. A plan therefore may not treat a foreign master as a pause or a blocker,
so graph absence cannot be misread as full-integration dependency.

**Shipped text corrected (260831-LOCR-L36 round 2).** The mirrored runtime template this card
describes —
`mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md` —
now states the corrected rule in its own text at `:172-174`: the graph-less default is "canonical
commanded-master tie-break; nothing serializes a graph-less sprint — it declares no dependencies, so
independent atomic masters proceed concurrently and no master is held because another is selected".
The graph-less choice therefore describes sprint shape (every commanded master executes atomically),
not a scheduling mechanism; only an explicit `executionGraph`'s `predecessor-incomplete:` waves gate
(developer ruling). The earlier shipped-source debt note is therefore removed — a repo-wide grep for
`source-pair-scoped`, `source-pair-selected`, the "logically pauses the former master" admission,
one-selected-master-at-a-time and source-pair activation wording returns 0 hits in the code worktree.

## CCR-L42 current candidate

The orchestration task template now specifies baseline sealing, fix-verification subset checks, review-mode fields, explicit developer authorization at the three-round limit, and task-document review lifecycle operations.

## Update History

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. SOURCE UNCHANGED BY THIS LEAF; card prose falsified by CAPS-R18@v1. Replaced the shared handoff-evidence boilerplate sentence with the completed-curation rule.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: Repaired citations this leaf falsified: the canonical lifecycle corpus was consolidated (the router shrank 620 → 179 lines; all nine role files and several templates were rewritten), so the cited anchors and ranges no longer resolved. No behavioral claim changed — the cited rule was re-pointed at its current home. Verification metadata remains closeout-owned. The strategist row now cites the rewritten file's real head range (`:1-16`, was `:1-263` against a 197-line file).

- 2026-09-13T15:02:41+02:00 — 260831-LOCR-L36 round 2 shipped-text correction: removed the
  shipped-source debt row and debt paragraph and replaced them with the corrected shipped range —
  the template's derived-wave walk now reads "nothing serializes a graph-less sprint — it declares no
  dependencies, so independent atomic masters proceed concurrently and no master is held because
  another is selected" at `:172-174`. Body prose now states the developer ruling (nothing serializes
  a graph-less sprint; `atomic-sequential` is sprint shape, not a serialization mechanism;
  per-contract activation records each contract's own `reconciling -> active` and the queue projects
  only each contract's own active/reconciling/vacant waiting candidates; only explicit
  `executionGraph` waves gate on `predecessor-incomplete:`), and every other range was re-grepped and
  repointed to canonical `orchestration-task.md:1-215`, `strategist.md:1-263`, and
  `plan-review.md:1-140`. Source documentation only; verification metadata remains closeout-owned and
  no acceptance or test claim is made.
- 2026-09-13T14:24:00+02:00 — 260831-LOCR-L36 activation re-keying: rewrote this card's graph-less
  walk from one source-pair-selected implementation exposure with pause/resume to the per-contract
  activation record — a sibling master sharing the protected source pair is never paused or blocked,
  and the only waiting reason is `atomic-series-reconciling` — and recorded the shipped-source debt
  that the frozen mirrored template still shows the removed source-pair-selected walk at its own
  `:172-173`, flagged for a future code leaf. That debt observation is superseded by the
  260831-LOCR-L36 round-2 entry above: the shipped text is corrected and the debt note is removed.
  Source documentation only; verification metadata
  remains closeout-owned and no acceptance or test claim is made.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: The orchestration task template now specifies baseline sealing, fix-verification subset checks, review-mode fields, explicit developer authorization at the three-round limit, and task-document review lifecycle operations.

- 2026-08-26T08:45+02:00 — Restored the canonical Docs reference section for this changed
  synchronized orchestration-task template card.

- 2026-08-26T05:20+02:00 — Reconciled the generated graph-less walk with source-pair selection,
  pause/resume preservation, and dependency separation. Final ranges remain post-Dagger-owned.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: recorded one effective candidate priority,
  optional explicit graph structure, complete strategist-skip reasoning, and the all-attachments
  then one-full-graph-bootstrap sequence. Canonical/generated sync is complete; Dagger acceptance
  remains closeout-owned and pending.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: restored the `executionGraph` qualifier in the canonical adoption-payload heading; copies re-synced. Verified at code commit e5cb139f.


- 2026-08-20T05:10+02:00 — 260815-DAG-L14: template updated to the atomic
  `attach_master` flow and seats structure. Verified at code commit 2f494982.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: synchronized the scheduling-default doctrine —
  adoption without a graph runs atomic-sequentially and `author_execution_graph` owns bootstrap
  and edits; the `migrate_execution_topology` reference is gone. Verification remains
  closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized explicit fact/judgment authority,
  graph-edge traceability, derived waves, and auditable runtime reprioritization. Verification
  remains closeout-owned.
- 2026-08-14T06:34+02:00 — L23 synchronized runtime template: orchestration tasks record
  candidate-bound route review and Dagger altitude without exposing private operation identity.

- 2026-08-11T19:58+02:00 — Reconciled `orchestration-task.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 6 citation findings (3 rows); scoped recheck clean.

- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: replaced the mandatory-strategist premise
  with the two valid authorship paths—approved strategist draft or orchestrator-authored task after
  a sanctioned skip—and preserved adoption plus shown-work requirements. Added the governing
  overview backlink. Verification metadata remains pinned until closeout stamps the eventual
  two-parent code commit.

- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `templates/orchestration-task.md` (leaf 260703-L12): the tenth template — the strategist's sprint plan with mandatory shown work (evidence-cited edges incl. declaration cross-references, derivation-named blast radii, from→to leaf moves, honest unplannable-as-scoped findings). Verification metadata pinned until closeout stamps the L12 commit.
