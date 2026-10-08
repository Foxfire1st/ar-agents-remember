# l-01-agent-lifecycles/templates/manager-brief.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Packaged runtime copy of the complete manager dispatch brief. The canonical
`skills/l-01-agent-lifecycles/templates/manager-brief.md` owns the packet; the sync process installs
this exact artifact.

## Code Commentary

### Logic

The synchronized manager brief distinguishes the next review-handoff attempt from internal
protocol events and requires a lightweight content-addressed record and non-gating summary.

The orchestrator calls `dispatch_agent` with the canonical master document, role `manager`, and this
complete brief. The manager dispatches worker/reviewer/curator children on canonical leaf or review
documents, never handles their occupant ids, and closes a leaf only after builder code, reviewer
verdict, and curator coherence exist. Master handover raises the structural gate from ambient master
identity; the orchestrator later decides the one matching open gate by master document and kind.

### Conventions

Fill every placeholder, retain the current-super branch anchor, include existing/ruled/current
memory intent inputs for the curator, and synchronize only from the canonical template.

### Invariants And Boundaries

- The brief addresses `(master document, manager)`, not a qualified leaf key or runtime id.
- Child retirement uses `retire_child` by leaf document and role.
- Gate authority and initial brief delivery remain control-plane-owned.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.


## CCR-R12@v5 Handoff Boundary

This template records the exact checks and their failed or not-run status as handoff evidence, together with the curator's complete memory-quality result. Closeout and integration consume the prepared code, memory-content, and ledger transaction and carry that completed curation as a prerequisite; full code quality, full tests, certification, and review are explicit requests rather than automatic template gates.

## Evidence

### Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

No meaningful cross-repo references found.

#### 260731-EFA-L17 — Quality Altitude Ladder

The manager brief now assigns Agents Remember acceptance to the pinned Dagger graph. Leaf and
focused gates select targeted mode; `worktree_integrate` selects full mode once at master
altitude. Both use the task-derived explicit diff base. Host pytest is refused; Candidate A's
direct wrapper has been deleted rather than retained as an acceptance or fallback route.
`memory_quality_check` remains a
per-leaf closeout gate, and omitted required proof refuses the gate.

## L23 Final Candidate Disposition

The manager brief makes route partitioning, exact candidate identity, same-reviewer delta checks,
and the final pre-curator lineage proof explicit deliverables rather than conversational memory.

## R39 Generic Manager Brief Contract

The manager brief requires repository memory to supply executor, environment, arguments, resource
policy, retry rules, and evidence. It preserves one leaf-closeout acceptance and one
master-integration full acceptance, with no leaf-integration rerun or fallback.

## 260815-DAG-L2 Dispatch And Exit Contract

The brief now carries execution nature, graph reference, nature-appropriate parent edge, and the
manager's fact-only closeout-ready report. Organizational exit review is explicitly scoped to the
exact proposed final super candidate containing prior landed contributions plus the proposed final
leaf. Build concurrency never grants landing order; only orchestrator release does.

## 260815-DAG-L15 Review-Doctrine

The route-review paragraph now states that the reviewer seat must be distinct from the leaf's
builder seat, and every requirement verdict must cite evidence of the requirement's class —
rendering → mounted-UI proof, scheduling → operation-level proof, data model → artifact-level
proof.

## 260821-CLIVE Brief Contract

The brief now requires the manager to declare a complete waiting closeout-door generation rather
than send an informal queue-readiness row, and to wait for orchestrator release of the current
first-ready generation. It explicitly keeps task edits live, requires inspection/relay of
`projectionEffects`, and routes changed waiting evidence through door provenance/disposition.
Post-claim lifecycle, worker, commit, and recovery evidence is read only from the enclosure-root
journal via status and advertised controls; projection invalidation is never a lifecycle loss.

## M38 Manager-Brief Projection

The manager brief now requires compilation of the exact stable requirement set, validation of one
complete worker envelope per ID, and dispatch of the same set for independent reviewer
adjudication. It forbids aggregate completion and keeps the durable-evidence hold point separate.
This installed artifact is a synchronized projection only.
The exact set includes the approved version-addressed packet and its durable corpus ruling for
every row; an unapproved or mismatched row invalidates dispatch.

## M40-M45 Manager-Brief Projection

The installed manager brief carries exact attempt dispatch/adjudication, failure/revision routing,
bounded invalidation, and rebuildable non-gating master-summary obligations from the canonical
template.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.

## CCR-L42 current candidate

The manager brief now carries review mode, the sealed baseline, the preceding result, and exact outstanding IDs. Fix-verification checks only those IDs, uses the begin/record review task-document operations, and does not add routes or rediscover the scope.

## MIK-R95 Shared Start Preparation

The dispatched Manager briefing now sends each leaf role through `role_start` as the operation that prepares its admitted environment: no separate `worktree_status`/`worktree_start` call precedes it. If a start reports moved source, the manager follows the contract-addressed `worktree_sync` recovery the start names and re-reads status, without inferring a source branch or carrying a prior super tip forward. The bundled runtime copy and the source skill template are byte-identical.
