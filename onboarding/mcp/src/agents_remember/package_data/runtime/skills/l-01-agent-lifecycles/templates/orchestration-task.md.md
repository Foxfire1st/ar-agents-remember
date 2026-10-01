# l-01-agent-lifecycles/templates/orchestration-task.md

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Canonical source this bundle copy is sync-propagated from. [1]
- The strategist role that fills this template and chooses either topology. [2]
- The plan-review criteria re-derive effective priority and validate either explicit-graph or graph-less topology. [3]
- The shipped template's derived-wave walk now says nothing serializes a graph-less sprint instead of the removed source-pair-selected exposure walk. [4]

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.

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
