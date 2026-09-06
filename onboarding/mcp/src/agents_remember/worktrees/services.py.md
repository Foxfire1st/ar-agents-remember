# mcp/src/agents_remember/worktrees/services.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/services.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Defines the service protocols and process-local binding consumed by worktree lifecycle code. It preserves package layering while application composition supplies provider, memory and citation services, canonical task observation, and an explicit certification continuation boundary.

## Code Commentary

### Logic

`WorktreeServices` carries provider, memory-quality and citation services plus optional `certification_memory_rails` and `certification_continuation` capabilities. `CertificationMemoryRailsPort` returns R11 `RailDefinition` objects for an admitted profile selection. `ProviderSetupRequestSpec` keeps higher-level provider option objects opaque to worktrees.

`MemoryQualityPort.observe_contract_task` returns the shared `CanonicalTaskObservation`; worktree consumers use this port instead of importing the memory observer. `CertificationContinuationPort` separates current memory observation, Gate-5 execution, and finalization. `observe_memory` returns verified `GateFiveSemanticInputs` or explicit absence; absence cannot authorize reuse of an existing memory certificate.

bind_worktree_services assigns the composed bundle, reset_worktree_services clears it for tests/teardown, and worktree_services refuses when no bundle is bound. The getter does not lazily create dependencies. Optional capability fields permit an incomplete bundle to be represented, while consumers refuse when the selected operation requires an absent capability. The default application bundle supplies memory rails but leaves the continuation unbound; defining this protocol does not install a production Gate-5/finalization implementation.

### Conventions

Protocols are the downward dependency boundary. Adapter implementations live above worktrees; module-level binding is explicit process composition.

### Invariants And Boundaries

- Worktrees must not import providers or memory_quality to satisfy a missing service.
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
| Citation and provider lifecycle protocols remain explicit. | `CitationGuardPort`; `ProviderLifecyclePort` | mcp/src/agents_remember/worktrees/services.py:42-48; mcp/src/agents_remember/worktrees/services.py:51-93 |
| Registry population and task/memory observations have distinct service ports. | `CertificationMemoryRailsPort`; `MemoryQualityPort` | mcp/src/agents_remember/worktrees/services.py:96-105; mcp/src/agents_remember/worktrees/services.py:108-125 |
| Current memory authority, Gate 5, and finalization are separate continuation methods. | `CertificationContinuationPort` | mcp/src/agents_remember/worktrees/services.py:128-138 |
| The bundle exposes optional capabilities; provider setup inputs stay opaque. | `WorktreeServices`; `ProviderSetupRequestSpec` | mcp/src/agents_remember/worktrees/services.py:142-147; mcp/src/agents_remember/worktrees/services.py:151-167 |
| Bind the composition-provided services for this process. | "def bind_worktree_services" | mcp/src/agents_remember/worktrees/services.py:181-184 |
| Clear the bound services (tests and process teardown). | "def reset_worktree_services" | mcp/src/agents_remember/worktrees/services.py:187-190 |
| Reading unbound worktree services refuses instead of constructing ambient owners. | "def worktree_services" | mcp/src/agents_remember/worktrees/services.py:193-198 |
| The default application bundle supplies rails but does not bind a continuation. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:197-203 |
| Selected execution observes memory before reuse and refuses an absent continuation. | `execute_selected_closeout` | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:279-332 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## L34 Current Implementation

Prepared-memory certification is an explicit typed service alongside the continuation port. Requests carry the actual physical code view and logical memory pair; returned semantic inputs and original references are revalidated by the current lifecycle owner.

| Finding | Anchor | Source |
| --- | --- | --- |
| `TerminalGuard` owns the corresponding behavior described above. | `TerminalGuard` | `mcp/src/agents_remember/worktrees/services.py:32-42` |
| `CitationGuardPort` owns the corresponding behavior described above. | `CitationGuardPort` | `mcp/src/agents_remember/worktrees/services.py:45-51` |
| `WorktreeServicesUnboundError` owns the corresponding behavior described above. | `WorktreeServicesUnboundError` | `mcp/src/agents_remember/worktrees/services.py:177-178` |
| Bind the composition-provided services for this process. | "def bind_worktree_services" | mcp/src/agents_remember/worktrees/services.py:181-184 |
| `reset_worktree_services` owns the corresponding behavior described above. | `reset_worktree_services` | `mcp/src/agents_remember/worktrees/services.py:187-190` |
| `worktree_services` owns the corresponding behavior described above. | `worktree_services` | `mcp/src/agents_remember/worktrees/services.py:193-198` |

The application composition currently installs `PreparedCloseoutContinuation` and `PreparedMemoryCertificationAdapter` in `application/worktree_services.py`. Missing-port refusal remains part of the service contract; installed binding itself does not certify an execution.

## Update History

### 2026-09-06T17:13:06+00:00 — L34 implementation memory

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

- 2026-09-06T14:55:31+00:00 — Completed source verification against actual commit c69d5171187fa1957025e393270db9f5a864ab14 after rechecking equality with the independently reviewed candidate source. Preserved the curated body, all citations and earlier history; certification remains pending.

- 2026-09-06T13:51:59+00:00 — L33 candidate curation: Added canonical task observation and explicit memory-observation/execution/finalization ports; distinguished the unbound default continuation from installed production composition. Reviewed uncommitted source; prior verification commit/date remain unchanged. This is source documentation, not gate or acceptance evidence.


- 2026-09-05T06:14:14+00:00 — Documented the new rail-population port alongside the preserved layering and explicit-binding invariants.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the worktrees service-port
  surface added by the layering cleanup. Verification metadata pinned until closeout stamps the
  L9 code commit.
