# mcp/src/agents_remember/worktrees/integration/organizational_completion.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:59 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `overview.md` |

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


## Docs References

No external Domain Documentation source is configured for this slice. The references below use the current package implementation, rather than a source registry or an assumed external specification.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is configured. | — | — |

## Repo-Internal References

The source separates pair/ancestry proof from task-byte publication. The production caller inspected here is the retained-state classifier; the source definitions do not establish a new automatic landing-to-master-completion edge.

| Finding | Anchor | Source |
| --- | --- | --- |
| The retained completion plan binds the actual code/memory pair and sibling facts. | `organizational_completion_plan` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:123-171 |
| Scope validation pins execution nature, owning master and canonical child. | `_completion_scope` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:174-204 |
| Sibling contracts require exact identities, code ancestry and any external-memory proof. | `_require_landed_sibling`; `_require_sibling_memory_ancestry` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:455-476; mcp/src/agents_remember/worktrees/integration/organizational_completion.py:572-593 |
| External memory must name the same repository and exact accepted/integrated content commit. | `_require_sibling_memory_identity`; `memory_content_commit` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:547-569 |
| The sibling memory commit must descend from its base and reach the completing source base. | `_require_sibling_memory_ancestry` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:572-593 |
| Task-byte preparation binds accepted and intended JSON/Markdown. | `prepare_organizational_master_completion` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:250-301 |
| Publication accepts only the exact journaled before/after task byte states. | `publish_organizational_master_completion`; `OrganizationalCompletionPublicationState` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:304-338; mcp/src/agents_remember/worktrees/integration/organizational_completion.py:50-73 |
| The helper requires Completed status, with a distinct abandonment refusal. | `require_published_organizational_master_completion` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:404-420 |
| The live integration classifier reads retained organizational publication state. | `classify_integration_operation` | mcp/src/agents_remember/worktrees/integration/integration_operation_decision.py:39-81 |

## Cross-Repo References

These helpers can operate on explicitly addressed external-memory Git repositories, but their implementation and authority contracts live in this package. No separate sibling-repository implementation is required to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No distinct cross-repository evidence source is configured for this file. | — | — |

## CCR-R12@v5 Current Completion Boundary

The retained completion definitions use the code/external-memory Git pair and existing ownership. They do not read a durable full-quality or certification marker to approve a normal transaction. Historical completion/certification vocabulary below records prior design context; it does not make cache state or a ledger row authoritative.

## 260821-CLIVE-L2 Current Contract

The current source seams include `OrganizationalCompletionError`, `OrganizationalCompletionPublicationError`, `OrganizationalCompletionPublicationState`. Organizational completion and repair are canonical integration-journal transitions with exact candidate, ref, quality, and cancellation evidence. The queue may schedule a door candidate but does not own failure repair or reopening lifecycle state.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Pair or ownership failures use the completion error family. | `OrganizationalCompletionError` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:30-31 |
| Publication conflicts retain exact expected/observed evidence. | `OrganizationalCompletionPublicationError`; `OrganizationalCompletionPublicationState` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:34-47; mcp/src/agents_remember/worktrees/integration/organizational_completion.py:50-73 |
| Classification distinguishes convergent, published and conflicting task bytes. | `OrganizationalCompletionPublicationState`; `classify_organizational_master_completion` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:341-401 |

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

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:59+00:00 — Current uncommitted candidate: Replaced ledger/mapping authority with the exact sibling code/memory pair and ancestry; distinguished retained historical completion proposals from the current source status/byte checks and refreshed references. Source SHA-256 `47d50a539d4fb0446c80f9790d743c635759bbc88485a5c2dde000a818652806`. Existing committed verification metadata and earlier history are preserved; no new commit or certification is claimed.
- 2026-09-11T23:05:00+00:00: Master abandonment curation: `require_published_organizational_master_completion` now refuses an `abandoned` master with a distinct reason ("abandoned, not completed") instead of the generic not-durably-published message. Added the invariant and its source row. Content change, not a range repoint.
- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: recorded that master completion is now explicitly undecided (the landed-leaf inference was deleted, not replaced), added the two owed checks and their intended `lifecycle_finalize_task_tool` entry point, and recorded that the plan/publication functions here now have zero callers while `classify_organizational_master_completion` remains reachable. Replaced the completion-inference Purpose with the completion-proof ownership, and repointed the sibling door read to `live_closeout_door`. Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `organizational_completion_plan` repointed to mcp/src/agents_remember/worktrees/integration/organizational_completion.py:130-180. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `_completion_scope` repointed to mcp/src/agents_remember/worktrees/integration/organizational_completion.py:183-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `_require_landed_sibling` repointed to mcp/src/agents_remember/worktrees/integration/organizational_completion.py:460-482. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `publish_organizational_master_completion` repointed to mcp/src/agents_remember/worktrees/integration/organizational_completion.py:313-347. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-08-26T14:32+02:00 — Replaced global ledger-key uniqueness with the two required proofs:
  newest mapping for sibling current authority and exact-edge containment for final-history
  preservation. Verification remains closeout-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: moved final-leaf proof from queue collection to claimed doors and canonical sibling contracts. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational direct-super completion proof.
