# l-01-agent-lifecycles/templates/orchestration-task.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/orchestration-task.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the orchestration-task template. The canonical template owns the sprint
plan shape; the sync process publishes this exact artifact.

## Code Commentary

### Logic

After developer approval, the sprint-bound strategist drafts the plan for the architect. The
architect rules it and the orchestrator adopts the accepted plan into durable execution form. The
strategist seat is identified by sprint task document plus role, and the artifact carries cited
scope, dependency, blast-radius, ordering, risk, and reevaluation evidence rather than an agent id.

### Conventions

Plans show their evidence per edge and remain drafts until architect ruling and orchestrator
adoption. Edit the canonical template, then synchronize.

### Invariants And Boundaries

- The strategist is a reader and does not mutate task documents.
- Durable plan evidence survives seat-occupant replacement.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Orchestration-Task Template` | skills/l-01-agent-lifecycles/templates/orchestration-task.md:1-145 |
| The strategist role that fills this template as method phase 8. | `# Lifecycle — Strategist` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/strategist.md:1-204 |
| The plan-review criteria catalog the reviewer runs against a filled orchestration task. | `# Criteria Catalog — Plan Review (the strategist loop)` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/plan-review.md:1-84 |

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

The artifact now separates a Mechanical Fact Inventory from one canonical Judgment Register. The
nature, relation, blast-radius, priority, blocker, and leaf-move sections are projections that cite
their owning judgment rows. `executionGraph` carries exact `TaskDocumentRef` nodes and evidence-
backed predecessor edges; deterministic waves and blocker positions are derived rather than
persisted. Runtime reprioritization records rationale, evidence, author, confidence, and
supersession before queue selection changes.

## 260815-DAG-L13 Scheduling Default Doctrine

The template's adoption rule now treats a sprint adopted without an `executionGraph` as running the
atomic-sequential default; `task_doc.author_execution_graph` bootstraps or edits the graph and is
never a runtime fallback. The `migrate_execution_topology` legacy-cutover reference is gone.

## 260815-DAG Master Full-Gate Repair

Restored the template heading to `## Canonical executionGraph Adoption Payload` (the `executionGraph` qualifier phrase restored); all 9 generated copy trees are byte-identical via `scripts/sync-skills.py`.

## Update History

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
