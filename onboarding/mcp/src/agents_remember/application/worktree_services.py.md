# mcp/src/agents_remember/application/worktree_services.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Builds the default service bundle that lets lower-level worktree operations use provider lifecycle, memory checking, citation guards, Gate-5 rail definitions, the mandatory knowledge validator (with its converted-base converter) and the knowledge crossing without importing those higher-level packages.

## Code Commentary

### Logic

ProviderLifecycleAdapter translates the worktree-owned setup specification into provider-owned requests and delegates setup/status/teardown. MemoryQualityAdapter delegates check-group discovery, drift context and memory checks. CitationGuardAdapter obtains the memory-quality citation cache guard.

CertificationMemoryRailsAdapter delegates the admitted selection id to gate_five_memory_rails. build_default_worktree_services installs this adapter beside the existing three services; the re-exported bind_worktree_services installs the resulting bundle when the MCP/CLI composition calls it.

Since MIK-R22 the default bundle also binds `knowledge_validation=GitKnowledgeValidation()`, imported from `memory_quality.knowledge_validator.commit_route`. It implements `worktrees.services.KnowledgeValidationPort`, so the worktree layer's memory commit routes (today the managed sync's memory merge) can run the validator without importing `memory_quality`.

Since MIK-R24 the validator is bound as `GitKnowledgeValidation(base_converter=GitBaseConverter())`, so a converted merge whose base is unconverted (the far side of a crossing sync) is validated against that base's conversion (rule 7), instead of being refused by rule 6. The bundle also binds `knowledge_crossing=GitKnowledgeCrossing()` (`memory/conversion/crossing_port.py`), which implements `worktrees.services.KnowledgeCrossingPort`: the managed sync plans a crossing sync's structural merge through it (rule 8) without importing `memory.conversion`. Both adapters are inert for a merge in which no tree is converted.

Since MIK-R08 the bundle also binds `knowledge_worklist=LeafWorklistRecompute()` (`application/knowledge_worklist/leaf.py`), which implements `worktrees.services.KnowledgeWorklistPort`: a completed managed sync recomputes and persists the leaf's change-to-knowledge worklist through it (rule 8) without the worktree layer importing the application layer. It returns `None` for a leaf whose two memory sides are unconverted (every production leaf before MIK-R37) and never raises, so the sync result is unchanged for them.

Since MIK-R25 the bundle also binds `review_artifact_cleanup=ReviewArtifactCleanup()` (`application/review_artifact_cleanup.py`), which implements `worktrees.services.ReviewArtifactCleanupPort`: finalization's archive of a root task deletes the task's review refs, its own legacy retained-code refs and its legacy dataset copies through it (rule 5, D17) without the worktree layer importing the application layer. It never raises; a process built without it reports `not-bound`.

Since MIK-R09 the bundle also binds `knowledge_gate=KnowledgeGate()` (`application/knowledge_gate/adapter.py`), which implements `worktrees.services.KnowledgeGatePort`: the closeout validator, direct landing, record landing and master and checkpoint landing reach the mandatory invariant gate through it without the worktree layer importing the application layer. It is the only place the port is bound; a converted route in a process built without it refuses (`GATE_UNBOUND`, rule 5), and an unconverted route never asks it.

- **L37 (review R3-1).** `MemoryQualityAdapter` passes `knowledge_base=context_check_base(code_repository_root,
  context)` into the drift context, so the closeout's memory-quality phases validate a converted working tree
  against `HEAD`'s conversion when `HEAD` is unconverted, through the shared converted-base cache.

### Conventions

Keep imports of providers and memory_quality at this composition boundary. Worktree modules consume protocols from worktrees.services; they do not locate those packages dynamically or construct fallback implementations.

### Invariants And Boundaries

- The bundle wires dependencies; it does not execute a certification gate by being built.
- Supplying Gate-5 rail definitions does not invoke full memory certification or publish coherence.
- Default composition must bind the rail adapter before the Agents Remember certification-record seam requests it.
- Preserve provider teardown and citation-guard ownership while extending the bundle.
- The knowledge validator and the knowledge crossing are bound here and nowhere else. A process without a bound crossing refuses a crossing sync (`crossing sync step 'convert' failed`); it never merges one as plain Git.
- The review-artifact archive hook is bound here and nowhere else (MIK-R25); finalize reads it through the port.
- The knowledge validator is bound here and nowhere else. A process that builds its bundle without it gets a refusal, not a skipped validation, for any converted memory commit.

### Todos

The rail-definition adapter is implemented; the complete R07/R08 production execution path remains a separate integration obligation.

### CCR private preparation boundary

The default application bundle installs `PreparedCloseoutContinuation` and `PreparedMemoryCertificationAdapter` explicitly. This supplies production memory/finalization composition through the existing service ports; binding the adapters neither bypasses certification nor establishes a successful execution.

- The current `build_default_worktree_services` boundary implements the preparation contract above. [1]

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

- Provider translation/delegation [2]
- Memory-rail and memory-quality adapters [3]
- The citation guard delegates terminal namespace protection. [4]
- The default bundle composes the declared worktree services, including the knowledge validator with its base converter and the knowledge crossing. [5]
- The default bundle's MIK-R09 binding: the mandatory gate's port adapter. [6]
- The default bundle's MIK-R08 binding: the worklist recompute port adapter. [7]
- The default bundle's MIK-R25 binding: the review-artifact archive hook. [8]
- The canonical binding owner installs the explicit service bundle. [9]

- The closeout's quality phases get the converted-base port. [10]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.
