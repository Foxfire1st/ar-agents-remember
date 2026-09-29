# mcp/src/agents_remember/worktrees/services.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/services.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Defines the service protocols and process-local binding consumed by worktree lifecycle code. It preserves package layering while application composition supplies provider, memory and citation services, canonical task observation, and an explicit certification continuation boundary. Since MIK-R22 it also declares the port through which a memory commit route reaches the mandatory knowledge validator.

## Code Commentary

### Logic

`WorktreeServices` carries provider, memory-quality and citation services plus optional `certification_memory_rails`, `certification_continuation`, `prepared_memory_certification` and `knowledge_validation` capabilities. `CertificationMemoryRailsPort` returns R11 `RailDefinition` objects for an admitted profile selection. `ProviderSetupRequestSpec` keeps higher-level provider option objects opaque to worktrees.

`MemoryQualityPort.observe_contract_task` returns the shared `CanonicalTaskObservation`; worktree consumers use this port instead of importing the memory observer. `CertificationContinuationPort` separates current memory observation, Gate-5 execution, and finalization. `observe_memory` returns verified `GateFiveSemanticInputs` or explicit absence; absence cannot authorize reuse of an existing memory certificate.

`KnowledgeValidationPort.refusal` (MIK-R22 rule 8) takes the memory repository, the exact candidate tree a route is about to commit, its comparison bases (K_B or every merge parent), and the paired code repository and commit, and returns the refusal text naming every violation, or `None`. The worktree layer calls it only through `worktrees/knowledge_validation.memory_commit_refusal`, which first probes the layout marker and refuses a converted commit when the port is unbound.

bind_worktree_services assigns the composed bundle, reset_worktree_services clears it for tests/teardown, and worktree_services refuses when no bundle is bound. The getter does not lazily create dependencies. Optional capability fields permit an incomplete bundle to be represented, while consumers refuse when the selected operation requires an absent capability. The default application bundle (`application/worktree_services.build_default_worktree_services`) binds memory rails, `PreparedCloseoutContinuation`, `PreparedMemoryCertificationAdapter` and, since MIK-R22, `GitKnowledgeValidation` from `memory_quality.knowledge_validator.commit_route`.

### Conventions

Protocols are the downward dependency boundary. Adapter implementations live above worktrees; module-level binding is explicit process composition.

### Invariants And Boundaries

- Worktrees must not import providers or memory_quality to satisfy a missing service. The knowledge validator lives in `memory_quality`, so it is reached only through `KnowledgeValidationPort`.
- An unbound `knowledge_validation` is never a reason to skip validation: the route helper refuses a converted memory commit instead.
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
| Citation and provider lifecycle protocols remain explicit. | `CitationGuardPort`; `ProviderLifecyclePort` | mcp/src/agents_remember/worktrees/services.py:45-51; mcp/src/agents_remember/worktrees/services.py:54-96 |
| The knowledge validator's commit-route port: candidate tree, bases and paired code commit in, refusal text or `None` out. | `KnowledgeValidationPort` | mcp/src/agents_remember/worktrees/services.py:131-147 |
| Registry population and task/memory observations have distinct service ports. | `CertificationMemoryRailsPort`; `MemoryQualityPort` | mcp/src/agents_remember/worktrees/services.py:99-108; mcp/src/agents_remember/worktrees/services.py:111-128 |
| Current memory authority, Gate 5, and finalization are separate continuation methods. | `CertificationContinuationPort` | mcp/src/agents_remember/worktrees/services.py:150-160 |
| The bundle exposes optional capabilities, including `knowledge_validation`; provider setup inputs stay opaque. | `WorktreeServices`; `ProviderSetupRequestSpec` | mcp/src/agents_remember/worktrees/services.py:163-171; mcp/src/agents_remember/worktrees/services.py:174-191 |
| Bind the composition-provided services for this process. | "def bind_worktree_services" | mcp/src/agents_remember/worktrees/services.py:201-201 |
| Clear the bound services (tests and process teardown). | "def reset_worktree_services" | mcp/src/agents_remember/worktrees/services.py:207-207 |
| Reading unbound worktree services refuses instead of constructing ambient owners. | "def worktree_services" | mcp/src/agents_remember/worktrees/services.py:213-213 |
| The default application bundle binds rails, the prepared continuation and certification, and the knowledge validator. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:206-215 |
| The route helper refuses a converted commit when the port is unbound. | `memory_commit_refusal` | mcp/src/agents_remember/worktrees/knowledge_validation.py:57-91 |
| Selected execution observes memory before reuse and refuses an absent continuation. | `execute_selected_closeout` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:344-384 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## L34 Current Implementation

Prepared-memory certification is an explicit typed service alongside the continuation port. Requests carry the actual physical code view and logical memory pair; returned semantic inputs and original references are revalidated by the current lifecycle owner.

| Finding | Anchor | Source |
| --- | --- | --- |
| `TerminalGuard` owns the corresponding behavior described above. | `TerminalGuard` | mcp/src/agents_remember/worktrees/services.py:32-42 |
| `CitationGuardPort` owns the corresponding behavior described above. | `CitationGuardPort` | mcp/src/agents_remember/worktrees/services.py:45-51 |
| `WorktreeServicesUnboundError` owns the corresponding behavior described above. | `WorktreeServicesUnboundError` | mcp/src/agents_remember/worktrees/services.py:197-198 |
| Bind the composition-provided services for this process. | "def bind_worktree_services" | mcp/src/agents_remember/worktrees/services.py:201-201 |
| `reset_worktree_services` owns the corresponding behavior described above. | `reset_worktree_services` | mcp/src/agents_remember/worktrees/services.py:207-210 |
| `worktree_services` owns the corresponding behavior described above. | `worktree_services` | mcp/src/agents_remember/worktrees/services.py:213-218 |

The application composition currently installs `PreparedCloseoutContinuation` and `PreparedMemoryCertificationAdapter` in `application/worktree_services.py`. Missing-port refusal remains part of the service contract; installed binding itself does not certify an execution.

## Update History
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
