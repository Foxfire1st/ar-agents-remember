# mcp/src/agents_remember/worktrees/integration/organizational_completion.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Definitions for branchless organizational-master completion proof and exact task-publication bytes. In the inspected production tree the plan/publication entry points remain uncalled; the live consumer is the integration decision classifier for a retained publication intent. This candidate changes the commit-pair proof, not master-completion policy or reachability.

## Historical Design Note: Master Completion After The Door Cut

The following account records the earlier design discussion and its proposed checks. It is preserved as history, not as a new review/approval prerequisite for the current transaction. Current source behavior is described under Code Commentary.

A leaf integrating reports a fact: integrated, checks passed. It may never imply its master is done.
`publish_organizational_master_completion` had exactly one live effect — writing the master task
document to `Completed` by inference from a landed leaf. That inference was deleted by commit
`fad9808e` and deliberately **not** re-expressed: a door-less leaf now yields a genuine absence, not a
reconstructed completion plan.

The current truthful state is that **completing a master is a decision that is not reachable in code
today**. Two checks are owed and neither is built:

- a reviewer **report must exist** — existence only; it is never read, parsed, hashed or graded;
- an **approval must be recorded**, widened from `tasks/route_review.py`'s `developerApproval` into
  one `{approver role/altitude, tentative | final}` concept, so an orchestrator may approve
  tentatively and the developer's sprint-handover approval is final.

The intended entry point is `application/worktree_tools.py::lifecycle_finalize_task_tool`, gated on
both checks. Master completion is never a side effect of a landing.

**What is still reachable here.** `organizational_completion_plan`,
`prepare_organizational_master_completion`, `publish_organizational_master_completion` and
`require_published_organizational_master_completion` all have zero callers and zero test references
after the cut; they are retained as the named site of this gap, not as live inference. Only
`classify_organizational_master_completion` is still reached — called from
`integration_operation_decision.py` to classify a retained
`publication.organizationalCompletion`.

## Code Commentary

### Logic

`organizational_completion_plan` resolves the canonical sprint/master/leaf topology, requires organizational execution, and binds the exact claimed final-leaf door. Each confined sibling contract must prove its own claimed door, repository identity, exact landed code and memory commits, and ancestry from its recorded base into the completing leaf's source base. The fingerprint binds the master semantic digest, sibling facts, and the actual two-output pair.

Memory proof no longer parses a sibling or final memory.md, chooses a cache row, or requires a mapping for the code commit. Its actual integrated memory-content commit must equal the sibling's accepted memory commit and be reachable on the source line. The live sibling door still comes from `live_closeout_door`.

Task-byte preparation binds accepted/intended JSON and Markdown. Publication classifies those exact byte states and rejects a third state; it does not itself move Git refs. `require_published_organizational_master_completion` checks Completed status and distinguishes abandonment; it does not inspect a certification marker. No automatic master completion is introduced by these retained definitions.

### Conventions

Use canonical task-document and contract identities. Logical task parentage and Git integration parentage are distinct; cache display rows are neither. Existing committed metadata and earlier design records remain intact.

### Invariants And Boundaries

- Task parentage (logical master) and Git parentage (sprint super) remain separate.
- Symlinked or escaping sibling contracts, foreign repositories, mismatched accepted/integrated commits, and unrelated code or memory ancestry refuse.
- The accepted pair has code and memory-content commits only; cache bytes, rows, or absent attribution cannot replace or veto that Git proof.
- Exact accepted/intended task bytes govern publication, with conflicting third states reported for decision.
- Abandoned is terminal but is not a published completion; the status helper requires Completed and reports abandonment distinctly.

### Todos

No additional source-local TODO is introduced by this pair-proof maintenance. The earlier reachability/design discussion remains explicitly historical above.


## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

No external domain source is configured.

### Repo-Internal References

The source separates pair/ancestry proof from task-byte publication. The production caller inspected here is the retained-state classifier; the source definitions do not establish a new automatic landing-to-master-completion edge.

- The retained completion plan binds the actual code/memory pair and sibling facts. [1]
- Scope validation pins execution nature, owning master and canonical child. [2]
- Sibling contracts require exact identities, code ancestry and any external-memory proof. [3]
- External memory must name the same repository and exact accepted/integrated content commit. [4]
- The sibling memory commit must descend from its base and reach the completing source base. [5]
- Task-byte preparation binds accepted and intended JSON/Markdown. [6]
- Publication accepts only the exact journaled before/after task byte states. [7]
- The helper requires Completed status, with a distinct abandonment refusal. [8]
- The live integration classifier reads retained organizational publication state. [9]

### Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

No distinct cross-repository evidence source is configured for this file.

## CCR-R12@v5 Current Completion Boundary

The retained completion definitions use the code/external-memory Git pair and existing ownership. They do not read a durable full-quality or certification marker to approve a normal transaction. Historical completion/certification vocabulary below records prior design context; it does not make cache state or a ledger row authoritative.

## 260821-CLIVE-L2 Current Contract

The current source seams include `OrganizationalCompletionError`, `OrganizationalCompletionPublicationError`, `OrganizationalCompletionPublicationState`. Organizational completion and repair are canonical integration-journal transitions with exact candidate, ref, quality, and cancellation evidence. The queue may schedule a door candidate but does not own failure repair or reopening lifecycle state.

### Reconciled Source Evidence

- Pair or ownership failures use the completion error family. [10]
- Publication conflicts retain exact expected/observed evidence. [11]
- Classification distinguishes convergent, published and conflicting task bytes. [12]

## 260821-CLIVE Door-Based Completion Proof

Final-leaf proof is driven by the exact claimed `CloseoutDoorGeneration` and canonical sibling
contracts. The door itself embeds candidate, master, and sprint binding; sibling-landed checks
require their own exact claimed doors, now read through `live_closeout_door` rather than from a
contract field. Absence of a queue row, candidate collection, or mutable
blocker state is never organizational-completion evidence. Since commit `fad9808e` this proof is not
reached from the integration path at all; see "Historical Design Note: Master Completion After The Door Cut" above.


## PDLS Reconciliation

Sibling completion proof now separates code ancestry, memory identity/ancestry, confined path, and exact task-byte validation into explicit fail-closed helpers.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
