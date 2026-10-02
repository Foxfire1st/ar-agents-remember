# mcp/src/agents_remember/worktrees/services.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Defines the service protocols and process-local binding consumed by worktree lifecycle code. It preserves package layering while application composition supplies provider, memory and citation services, canonical task observation, and an explicit certification continuation boundary. Since MIK-R22 it also declares the port through which a memory commit route reaches the mandatory knowledge validator, and since MIK-R24 the port through which the managed sync plans a crossing sync's structural merge. Since MIK-R09 (leaf 260928-MIK-L09) it declares `KnowledgeGatePort`, through which every route that commits or lands memory reaches the mandatory invariant gate.

## Code Commentary

### Logic

`WorktreeServices` carries provider, memory-quality and citation services plus optional `certification_memory_rails`, `certification_continuation`, `prepared_memory_certification`, `knowledge_validation`, (since MIK-R24) `knowledge_crossing`, (since MIK-R08) `knowledge_worklist`, (since MIK-R25) `review_artifact_cleanup` and (since MIK-R09) `knowledge_gate` capabilities. `CertificationMemoryRailsPort` returns R11 `RailDefinition` objects for an admitted profile selection. `ProviderSetupRequestSpec` keeps higher-level provider option objects opaque to worktrees.

`MemoryQualityPort.observe_contract_task` returns the shared `CanonicalTaskObservation`; worktree consumers use this port instead of importing the memory observer. `CertificationContinuationPort` separates current memory observation, Gate-5 execution, and finalization. `observe_memory` returns verified `GateFiveSemanticInputs` or explicit absence; absence cannot authorize reuse of an existing memory certificate.

`KnowledgeValidationPort.refusal` (MIK-R22 rule 8) takes the memory repository, the exact candidate tree a route is about to commit, its comparison bases (K_B or every merge parent), and the paired code repository and commit, and returns the refusal text naming every violation, or `None`. The worktree layer calls it only through `worktrees/knowledge_validation.memory_commit_refusal`, which first probes the layout marker and refuses a converted commit when the port is unbound.

Since MIK-R09, `KnowledgeValidationPort.leaf_refusal(...)` judges a commit that publishes a leaf (closeout, direct landing, a leaf's recorded landing): the leaf's own history file is re-anchor-checked whatever its `closed` flag (review R1 F1), unless it is closed in a base or in a frozen commit; `memory_commit_refusal` chooses it when `leaf_publication` is set. Since L37 it takes a `LeafPublication(candidate_tree, bases, frozen=())` in place of the tree and the bases. `frozen` are the commits the candidate sits on when they are not bases: a history file closed there was closed by an earlier closeout of the same leaf that was not integrated, and stays frozen (decision record DEC-0AEQ28). `LandingGateRequest.frozen` carries the same commits for a recorded landing; the caller names them only for the memory commit the leaf's contract records as its completed closeout.

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

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The protocols establish the downward dependency boundary; the application supplies adapters and the selected executor requires the continuation. Protocol definitions do not themselves prove execution or provide a missing implementation.

- Citation and provider lifecycle protocols remain explicit. [1]

- The knowledge validator's commit-route port: candidate tree, bases and paired code commit in, refusal text or `None` out; since MIK-R09 a `leaf_refusal` twin that takes a `LeafPublication`. [2]

- The mandatory gate's port, its landing request and the direct-landing verdict (MIK-R09). [3]

- The crossing sync's port, its request and plan view, and the step failure it raises. [4]
- The worklist recompute port and the bundle field that carries it. [5]
- The archive hook's request and port (MIK-R25 rule 5): one archived task, its directory name and its two repositories in; the cleanup report out, never raising. [6]
- Registry population and task/memory observations have distinct service ports. [7]
- Current memory authority, Gate 5, and finalization are separate continuation methods. [8]
- The bundle exposes optional capabilities, including `knowledge_validation`, `knowledge_crossing`, `knowledge_worklist`, (since MIK-R25) `review_artifact_cleanup` and (since MIK-R09) `knowledge_gate`; provider setup inputs stay opaque. [9]
- Bind the composition-provided services for this process. [10]
- Clear the bound services (tests and process teardown). [11]
- Reading unbound worktree services refuses instead of constructing ambient owners. [12]
- The default application bundle binds rails, the prepared continuation and certification, the knowledge validator with its base converter, and the knowledge crossing. [13]

- The route helper refuses a converted commit when the port is unbound. [14]

- Selected execution, which since MIK-R09 first refuses the prepared path on converted memory, observes memory before reuse and refuses an absent continuation. [15]

- The memory trees of a commit that publishes a leaf, with the commits whose closed files stay frozen. [22]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.

## L34 Current Implementation

Prepared-memory certification is an explicit typed service alongside the continuation port. Requests carry the actual physical code view and logical memory pair; returned semantic inputs and original references are revalidated by the current lifecycle owner.

- `TerminalGuard` owns the corresponding behavior described above. [16]
- `CitationGuardPort` owns the corresponding behavior described above. [17]
- `WorktreeServicesUnboundError` owns the corresponding behavior described above. [18]
- Bind the composition-provided services for this process. [19]
- `reset_worktree_services` owns the corresponding behavior described above. [20]
- `worktree_services` owns the corresponding behavior described above. [21]

The application composition currently installs `PreparedCloseoutContinuation` and `PreparedMemoryCertificationAdapter` in `application/worktree_services.py`. Missing-port refusal remains part of the service contract; installed binding itself does not certify an execution.
