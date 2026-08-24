# l-01-agent-lifecycles/templates/orchestration-task.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-24T13:51:26+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
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
- A graph-less atomic-sequential topology is valid. First graph adoption occurs only after every
  master attachment and uses one complete nodes-plus-evidence-edges batch.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Orchestration-Task Template` | skills/l-01-agent-lifecycles/templates/orchestration-task.md:1-198 |
| The strategist role that fills this template as method phase 8 and chooses either topology. | `# Lifecycle — Strategist` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:1-247 |
| The plan-review criteria re-derive effective priority and validate either explicit-graph or graph-less topology. | `# Criteria Catalog — Plan Review (the strategist loop)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md:1-134 |

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
commanded-master order. Runtime reprioritization records rationale, evidence, author, confidence,
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

## Update History

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
