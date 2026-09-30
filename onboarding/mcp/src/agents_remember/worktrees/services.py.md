# mcp/src/agents_remember/worktrees/services.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/services.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Defines the service protocols and process-local binding consumed by worktree lifecycle code. It preserves package layering while application composition supplies provider, memory and citation services, canonical task observation, and an explicit certification continuation boundary. Since MIK-R22 it also declares the port through which a memory commit route reaches the mandatory knowledge validator, and since MIK-R24 the port through which the managed sync plans a crossing sync's structural merge. Since MIK-R09 (leaf 260928-MIK-L09) it declares `KnowledgeGatePort`, through which every route that commits or lands memory reaches the mandatory invariant gate.

## Code Commentary

### Logic

`WorktreeServices` carries provider, memory-quality and citation services plus optional `certification_memory_rails`, `certification_continuation`, `prepared_memory_certification`, `knowledge_validation`, (since MIK-R24) `knowledge_crossing`, (since MIK-R08) `knowledge_worklist`, (since MIK-R25) `review_artifact_cleanup` and (since MIK-R09) `knowledge_gate` capabilities. `CertificationMemoryRailsPort` returns R11 `RailDefinition` objects for an admitted profile selection. `ProviderSetupRequestSpec` keeps higher-level provider option objects opaque to worktrees.

`MemoryQualityPort.observe_contract_task` returns the shared `CanonicalTaskObservation`; worktree consumers use this port instead of importing the memory observer. `CertificationContinuationPort` separates current memory observation, Gate-5 execution, and finalization. `observe_memory` returns verified `GateFiveSemanticInputs` or explicit absence; absence cannot authorize reuse of an existing memory certificate.

`KnowledgeValidationPort.refusal` (MIK-R22 rule 8) takes the memory repository, the exact candidate tree a route is about to commit, its comparison bases (K_B or every merge parent), and the paired code repository and commit, and returns the refusal text naming every violation, or `None`. The worktree layer calls it only through `worktrees/knowledge_validation.memory_commit_refusal`, which first probes the layout marker and refuses a converted commit when the port is unbound.

Since MIK-R09, `KnowledgeValidationPort.leaf_refusal(...)` takes the same arguments for a commit that publishes a leaf (closeout, direct landing, a leaf's recorded landing): the leaf's own history file is re-anchor-checked whatever its `closed` flag (review R1 F1); `memory_commit_refusal(..., leaf_publication=True)` chooses it.

**`KnowledgeGatePort` (MIK-R09).** Bound by the composition layer (`application/knowledge_gate/adapter.KnowledgeGate`); each method recomputes from the exact trees it is given, trusts nothing persisted, and returns the refusal naming every finding, or `None`:
- `leaf_refusal(contract, *, code_tree, memory_tree, parent_memory_tip)`: the gate over a leaf's exact closeout candidate (the closeout validator);
- `direct_verdict(contract, *, code_commit, memory_tree) -> DirectGateVerdict(applies, owner, refusal)`: direct landing's verdict and the leaf whose history file it closes;
- `landing_refusal(LandingGateRequest)`: a landing's closed-history and net-staleness checks. `LandingGateRequest` names the landed memory commit and its `memory_bases` (the parent line's memory tip for a master or checkpoint landing, the task's memory base or the commit's parents for a recorded landing), the code repository and commit, `code_base` (the parent line's code tip whose merge base with the code commit starts the master's net diff; `None`: no staleness check) and `leaf_owner` (a leaf's recorded landing: its history file must be closed).

The worktree layer reaches it only through `worktrees/knowledge_gate.py`, whose marker probes decide applicability first.

`KnowledgeCrossingPort.plan(request)` (MIK-R24 rule 8) runs steps 1-4 of a crossing sync over three memory commits. The `CrossingRequest` names the memory repository, the (merge base, own, incoming) commits, the paired code repository and commit, and who performs the sync (`owner_kind` `leaf` or `master`, with `owner_id`). It returns a `CrossingPlanView`: `files` maps every `knowledge/` and `onboarding/` path of the merged tree to its bytes (`None` = absent), `conflicts` are `(path, item, reason)` triples for the curator, `conflict_versions` holds the converted base, own and incoming bytes of each conflicted path, and `report` is the crossing report. A failing step raises `CrossingStepFailed`, whose message names the step; nothing has been written by then. The adapter (`memory/conversion/crossing_port.GitKnowledgeCrossing`) lives above this layer, and the worktree layer calls the port only through `worktrees/knowledge_crossing.crossing_plan`.

`KnowledgeWorklistPort.recompute(contract)` (MIK-R08 rule 8) recomputes and persists a leaf's change-to-knowledge worklist and returns its compact summary, or `None` where no worklist applies (both memory sides unconverted, or not a leaf). It never raises: an unanticipated failure is persisted as the `incomplete` worklist naming the run. The adapter (`application/knowledge_worklist/leaf.LeafWorklistRecompute`) lives above this layer; the worktree layer calls the port only from `sync_transaction_recovery.recompute_knowledge_worklist`, after a managed sync completed.

`ReviewArtifactCleanupPort.cleanup(request)` (MIK-R25 rule 5, D17) deletes an archived task's review artifacts and returns the cleanup report the finalizer carries as `taskArchive.reviewArtifacts`. The `ReviewArtifactCleanupRequest` names the task root as it is now (the archive location once archived), `task_name` (the task directory name, which alone names the review-ref namespace, ruling 2026-09-30T02:32:42 (a)), the code and memory repositories the series contract names (`None` for one the task does not have), and `dry_run`. It never raises for one artifact it could not delete; that artifact is listed under `failures`. The adapter (`application/review_artifact_cleanup.ReviewArtifactCleanup`) lives above this layer; the worktree layer calls the port only from `modules/finalize._with_review_artifact_cleanup`.

bind_worktree_services assigns the composed bundle, reset_worktree_services clears it for tests/teardown, and worktree_services refuses when no bundle is bound. The getter does not lazily create dependencies. Optional capability fields permit an incomplete bundle to be represented, while consumers refuse when the selected operation requires an absent capability. The default application bundle (`application/worktree_services.build_default_worktree_services`) binds memory rails, `PreparedCloseoutContinuation`, `PreparedMemoryCertificationAdapter` and, since MIK-R22, `GitKnowledgeValidation` from `memory_quality.knowledge_validator.commit_route`.

### Conventions

Protocols are the downward dependency boundary. Adapter implementations live above worktrees; module-level binding is explicit process composition.

### Invariants And Boundaries

- Worktrees must not import providers or memory_quality to satisfy a missing service. The knowledge validator lives in `memory_quality`, so it is reached only through `KnowledgeValidationPort`.
- An unbound `knowledge_validation` is never a reason to skip validation: the route helper refuses a converted memory commit instead.
- An unbound `knowledge_crossing` is never a reason to merge a crossing sync as plain Git: `crossing_plan` refuses with the `convert` step named.
- An unbound `knowledge_gate` is never a reason to commit or land converted memory ungated: the route helpers in `worktrees/knowledge_gate.py` refuse (`GATE_UNBOUND`, MIK-R09 rule 5); unconverted memory never asks it.
- An unbound `knowledge_worklist` only means no worklist is recomputed: the completed sync's result is exactly what it was, and the recompute can never fail a completed sync.
- An unbound service bundle is an error, not a signal to invent a default.
- Rail population is data authority; `CertificationMemoryRailsPort` does not run Gate 5.
- Memory reuse requires a current observation from the bound continuation. A missing continuation cannot complete selected closeout.
- The protocol returns a handoff result; it does not select certificates, invent memory evidence, or finalize by default.
- The citation terminal guard retains its publication/rollback callback boundary.

### Todos

Keep absent rail or continuation capabilities visible at their requiring consumers. Production continuation composition remains separate work from this protocol definition.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The protocols establish the downward dependency boundary; the application supplies adapters and the selected executor requires the continuation. Protocol definitions do not themselves prove execution or provide a missing implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Citation and provider lifecycle protocols remain explicit. | `CitationGuardPort`; `ProviderLifecyclePort` | mcp/src/agents_remember/worktrees/services.py:47-53; mcp/src/agents_remember/worktrees/services.py:56-98 |
| The knowledge validator's commit-route port: candidate tree, bases and paired code commit in, refusal text or `None` out; since MIK-R09 a `leaf_refusal` twin for a leaf publication. | `KnowledgeValidationPort`; "The same, for a commit that publishes a leaf" | mcp/src/agents_remember/worktrees/services.py:133-162 |
| The mandatory gate's port, its landing request and the direct-landing verdict (MIK-R09). | `LandingGateRequest`; `DirectGateVerdict`; `KnowledgeGatePort` | mcp/src/agents_remember/worktrees/services.py:214-263 |
| The crossing sync's port, its request and plan view, and the step failure it raises. | `KnowledgeCrossingPort`; `CrossingRequest`; `CrossingPlanView`; `CrossingStepFailed` | mcp/src/agents_remember/worktrees/services.py:165-177; mcp/src/agents_remember/worktrees/services.py:184-194; mcp/src/agents_remember/worktrees/services.py:197-200; mcp/src/agents_remember/worktrees/services.py:180-181 |
| The worklist recompute port and the bundle field that carries it. | `KnowledgeWorklistPort`; `knowledge_worklist` | mcp/src/agents_remember/worktrees/services.py:203-211; mcp/src/agents_remember/worktrees/services.py:315-315 |
| The archive hook's request and port (MIK-R25 rule 5): one archived task, its directory name and its two repositories in; the cleanup report out, never raising. | `ReviewArtifactCleanupRequest`; `ReviewArtifactCleanupPort` | mcp/src/agents_remember/worktrees/services.py:266-279; mcp/src/agents_remember/worktrees/services.py:282-289 |
| Registry population and task/memory observations have distinct service ports. | `CertificationMemoryRailsPort`; `MemoryQualityPort` | mcp/src/agents_remember/worktrees/services.py:101-110; mcp/src/agents_remember/worktrees/services.py:113-130 |
| Current memory authority, Gate 5, and finalization are separate continuation methods. | `CertificationContinuationPort` | mcp/src/agents_remember/worktrees/services.py:292-302 |
| The bundle exposes optional capabilities, including `knowledge_validation`, `knowledge_crossing`, `knowledge_worklist`, (since MIK-R25) `review_artifact_cleanup` and (since MIK-R09) `knowledge_gate`; provider setup inputs stay opaque. | `WorktreeServices`; `ProviderSetupRequestSpec` | mcp/src/agents_remember/worktrees/services.py:305-317; mcp/src/agents_remember/worktrees/services.py:320-337 |
| Bind the composition-provided services for this process. | "def bind_worktree_services" | mcp/src/agents_remember/worktrees/services.py:347-347 |
| Clear the bound services (tests and process teardown). | "def reset_worktree_services" | mcp/src/agents_remember/worktrees/services.py:353-353 |
| Reading unbound worktree services refuses instead of constructing ambient owners. | "def worktree_services" | mcp/src/agents_remember/worktrees/services.py:359-359 |
| The default application bundle binds rails, the prepared continuation and certification, the knowledge validator with its base converter, and the knowledge crossing. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:211-224 |
| The route helper refuses a converted commit when the port is unbound. | `memory_commit_refusal` | mcp/src/agents_remember/worktrees/knowledge_validation.py:64-104 |
| Selected execution, which since MIK-R09 first refuses the prepared path on converted memory, observes memory before reuse and refuses an absent continuation. | "def execute_selected_closeout(" | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:348-391 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## L34 Current Implementation

Prepared-memory certification is an explicit typed service alongside the continuation port. Requests carry the actual physical code view and logical memory pair; returned semantic inputs and original references are revalidated by the current lifecycle owner.

| Finding | Anchor | Source |
| --- | --- | --- |
| `TerminalGuard` owns the corresponding behavior described above. | `TerminalGuard` | mcp/src/agents_remember/worktrees/services.py:34-44 |
| `CitationGuardPort` owns the corresponding behavior described above. | `CitationGuardPort` | mcp/src/agents_remember/worktrees/services.py:47-53 |
| `WorktreeServicesUnboundError` owns the corresponding behavior described above. | `WorktreeServicesUnboundError` | mcp/src/agents_remember/worktrees/services.py:343-344 |
| Bind the composition-provided services for this process. | "def bind_worktree_services" | mcp/src/agents_remember/worktrees/services.py:347-347 |
| `reset_worktree_services` owns the corresponding behavior described above. | `reset_worktree_services` | mcp/src/agents_remember/worktrees/services.py:353-356 |
| `worktree_services` owns the corresponding behavior described above. | `worktree_services` | mcp/src/agents_remember/worktrees/services.py:359-364 |

The application composition currently installs `PreparedCloseoutContinuation` and `PreparedMemoryCertificationAdapter` in `application/worktree_services.py`. Missing-port refusal remains part of the service contract; installed binding itself does not certify an execution.

## Update History
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** Purpose and Logic record the new `KnowledgeGatePort` (with `LandingGateRequest` and `DirectGateVerdict`), `KnowledgeValidationPort.leaf_refusal` (review R1 F1) and the bundle's `knowledge_gate` field; an Invariants bullet records that an unbound gate refuses converted memory (`GATE_UNBOUND`). One row added and the validator-port row extended. **Reopened claims reworded:** the `WorktreeServices` bundle row (it now names `knowledge_gate`, re-measured `305-317`) and the `execute_selected_closeout` row (the prepared path refuses first on converted memory). The port rows the installed fixer declined were re-pointed by the exact base-to-staged line shift; the fixer re-pointed the rest (its bullets are kept, since those claims were not reworded). **Re-anchored:** claims bind by anchor text and a committed generated bullet names the old anchor, so the reworded `execute_selected_closeout` row was re-anchored on line-exact quotes ("def execute_selected_closeout("); no committed history line was edited.
- 2026-09-30T18:02:22+00:00: Generated citation repair: `ReviewArtifactCleanupRequest`; `ReviewArtifactCleanupPort` repointed to mcp/src/agents_remember/worktrees/services.py:266-279; mcp/src/agents_remember/worktrees/services.py:282-289. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:02:22+00:00: Generated citation repair: `CertificationContinuationPort` repointed to mcp/src/agents_remember/worktrees/services.py:292-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:02:22+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:347-347. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:02:22+00:00: Generated citation repair: "def reset_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:353-353. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:02:22+00:00: Generated citation repair: "def worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:359-359. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:02:22+00:00: Generated citation repair: `WorktreeServicesUnboundError` repointed to mcp/src/agents_remember/worktrees/services.py:343-344. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:02:22+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:347-347. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:02:22+00:00: Generated citation repair: `reset_worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:353-356. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:02:22+00:00: Generated citation repair: `worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:359-364. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): **body updated for MIK-R25.** Logic gains `ReviewArtifactCleanupRequest`, `ReviewArtifactCleanupPort` and the `review_artifact_cleanup` bundle field, with one row. **The `WorktreeServices` row (its construct changed) was re-read, reworded to name the new field, and re-measured** to the class's current extent (`239-250`), dropping a stale first range that no longer held it. The other rows were projected by the installed fixer. No verification stamp was advanced.
- 2026-09-30T01:49:50+00:00: Generated citation repair: `CertificationContinuationPort` repointed to mcp/src/agents_remember/worktrees/services.py:226-236. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:49:50+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:49:50+00:00: Generated citation repair: "def reset_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:286-286. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:49:50+00:00: Generated citation repair: "def worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:292-292. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:49:50+00:00: Generated citation repair: `WorktreeServicesUnboundError` repointed to mcp/src/agents_remember/worktrees/services.py:276-277. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:49:50+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:49:50+00:00: Generated citation repair: `reset_worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:286-289. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:49:50+00:00: Generated citation repair: `worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:292-297. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:45:29+00:00: Generated citation repair: `CertificationContinuationPort` repointed to mcp/src/agents_remember/worktrees/services.py:200-210. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:45:29+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:45:29+00:00: Generated citation repair: "def reset_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:259-259. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:45:29+00:00: Generated citation repair: "def worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:45:29+00:00: Generated citation repair: `WorktreeServicesUnboundError` repointed to mcp/src/agents_remember/worktrees/services.py:249-250. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:45:29+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:45:29+00:00: Generated citation repair: `reset_worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:259-262. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T15:45:29+00:00: Generated citation repair: `worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:265-270. No content impact: mechanical anchor-range projection bound to citation source snapshot e0edc40115a57d64eee749407e3bb64382ff6c5a6884c16ce3f8938fb89031a7; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): **body updated for MIK-R08.** Logic names the new optional `knowledge_worklist` field and describes `KnowledgeWorklistPort.recompute` (summary or `None`, never raises, adapter above this layer, called only after a completed managed sync); Invariants records that an unbound port only means no recompute. A row cites the port and the bundle field.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Body update: the knowledge crossing port (MIK-R24 rule 8).** Documented `KnowledgeCrossingPort`, `CrossingRequest`, `CrossingPlanView`, `CrossingStepFailed` and the `knowledge_crossing` bundle field in Purpose, Logic, an invariant and a new row. The reopened `WorktreeServices` row was reworded to name the new field and re-measured (`202-211`) by hand. The composition row names the base converter and the crossing.
- 2026-09-29T12:05:58+00:00: Generated citation repair: `CertificationContinuationPort` repointed to mcp/src/agents_remember/worktrees/services.py:189-199. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T12:05:58+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:241-241. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T12:05:58+00:00: Generated citation repair: "def reset_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:247-247. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T12:05:58+00:00: Generated citation repair: "def worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T12:05:58+00:00: Generated citation repair: `WorktreeServicesUnboundError` repointed to mcp/src/agents_remember/worktrees/services.py:237-238. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T12:05:58+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:241-241. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T12:05:58+00:00: Generated citation repair: `reset_worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:247-250. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T12:05:58+00:00: Generated citation repair: `worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:253-258. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): documented MIK-R22's `KnowledgeValidationPort` and the optional `WorktreeServices.knowledge_validation` field, the layering reason the validator is reached only through the port, and the refusal of a converted commit when it is unbound. Corrected the default-bundle claim, which still said the continuation was unbound, and re-measured the `WorktreeServices`/`ProviderSetupRequestSpec` rows. I folded the same-pass generated repair bullet for `build_default_worktree_services` into this entry, because that claim's text changed. The verification stamp is unchanged; closeout owns it.
- 2026-09-29T05:01:31+00:00: Generated citation repair: `CertificationContinuationPort` repointed to mcp/src/agents_remember/worktrees/services.py:150-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:01:31+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:01:31+00:00: Generated citation repair: "def reset_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:01:31+00:00: Generated citation repair: "def worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:01:31+00:00: Generated citation repair: `WorktreeServicesUnboundError` repointed to mcp/src/agents_remember/worktrees/services.py:197-198. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:01:31+00:00: Generated citation repair: "def bind_worktree_services" repointed to mcp/src/agents_remember/worktrees/services.py:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:01:31+00:00: Generated citation repair: `reset_worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:207-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:01:31+00:00: Generated citation repair: `worktree_services` repointed to mcp/src/agents_remember/worktrees/services.py:213-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `execute_selected_closeout` repointed to mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:344-384. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

### 2026-09-06T17:13:06+00:00 — L34 implementation memory

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

- 2026-09-06T14:55:31+00:00 — Completed source verification against actual commit c69d5171187fa1957025e393270db9f5a864ab14 after rechecking equality with the independently reviewed candidate source. Preserved the curated body, all citations and earlier history; certification remains pending.

- 2026-09-06T13:51:59+00:00 — L33 candidate curation: Added canonical task observation and explicit memory-observation/execution/finalization ports; distinguished the unbound default continuation from installed production composition. Reviewed uncommitted source; prior verification commit/date remain unchanged. This is source documentation, not gate or acceptance evidence.


- 2026-09-05T06:14:14+00:00 — Documented the new rail-population port alongside the preserved layering and explicit-binding invariants.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the worktrees service-port
  surface added by the layering cleanup. Verification metadata pinned until closeout stamps the
  L9 code commit.
