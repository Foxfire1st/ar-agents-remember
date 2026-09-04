# mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b` |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

Owns the one host-level shared Dagger runner/layer-store authority (CCR-R12@v4, delivered by
260831-CCR-L12, commit `cfd09381`). One host-global, repository-external declaration selects
exactly one already-running connection-only Dagger endpoint and the exact reusable layer store
mounted at its declared location; every production Dagger launch in the repository crosses this
module admission boundary before any Dagger command starts. Admission strictly parses the
declaration (refusing missing, malformed, unsupported-schema, provisioning-capable,
worktree-local, or ambient-conflicting declarations), inspects the actual live engine and store
mount connection-only (never creating, starting, or provisioning an engine or volume), freezes one
immutable `dagger-runtime-authority/v1` snapshot whose digest binds the operation, and registers
the exact live consumer in a host-level locked owner registry. Registry writes serialize under
POSIX flock; owner liveness uses a process-start fingerprint rather than PID alone so a reused PID
cannot release or suppress another live owner. When the host declaration changes while owners
still run, a typed transition barrier lets old operations finish on their frozen authority while
every fresh admission is refused until the old authority live-owner census reaches zero, at which
point the replacement activates atomically. Terminalization releases only the exact owner; crash
reconciliation drops only stale owner rows and never rewrites an operation primary result. Every
refusal is a typed `DaggerRuntimeAuthorityError` raised before any Dagger command starts.

## Code Commentary

### Logic

Module-level surface (decorator-inclusive ranges):

- `_sha256` (function, lines 71-81) — Deterministic compact sorted-JSON SHA-256 used for every
  authority digest in this module.
- `DaggerHostDeclaration` (class, lines 82-112) — One parsed host declaration: connection-only
  endpoint, absolute layer store path, pinned engine version, and its source; `declaration_digest`
  (lines 92-102) is the digest of the declaration bytes alone and `as_manifest` (lines 103-112)
  renders the persisted shape.
- `InspectedRuntime` (class, lines 113-123) — Live-inspection facts: engine id, running state,
  mounted store destination/source, and the best-effort observed engine version.
- `DaggerAuthoritySnapshot` (class, lines 124-150) — The immutable frozen authority one operation
  may launch against (schema `dagger-runtime-authority/v1`): declaration fields plus inspected
  engine/store facts, `inspected_at`, and the `snapshot_digest` (lines 138-149) bound into
  manifests, fingerprints, and evidence.
- `DaggerOwner` (class, lines 151-164) — One cross-operation live-owner identity: owner id, the
  authority digest, operation kind, scope, generation, PID, process fingerprint, and start time.
- `AdmittedDaggerAuthority` (class, lines 165-178) — The admitted launch context: frozen snapshot,
  parsed declaration, the deterministic launch environment, and the registered owner (optional).
- `AuthorityState` (class, lines 179-189) — Persisted host state: active authority digest plus any
  `awaiting-zero-census` transition barrier.
- `AuthorityBarrier` (class, lines 190-197) — One typed transition barrier with the live-owner
  census.
- `DockerEngineInspector` (class, lines 202-333) — Default production inspector: `docker inspect`
  proves the declared engine container exists and is running, and that the reusable layer store is
  mounted at its declared destination; `_observed_engine_version` is best-effort and never refuses.
- `parse_host_declaration` (function, lines 390-408) — Strictly parses one declaration or raises a
  typed defect; `_require_host_level_root` (lines 409-437) refuses a declaration whose source
  lives inside any repository/worktree root.
- `_endpoint_value` (function, lines 465-489) — Endpoint must use a connection-only scheme
  (`container`/`tcp`/`unix`/`grpc`); provisioning-capable schemes (`docker-container`,
  `docker-image`, `local`, `auto`, `dagger`, `start`) and empty endpoints are refused.
- `authority_snapshot` (function, lines 516-546) — Freezes one immutable snapshot from the
  declaration plus the live inspection, computing the snapshot digest over the full payload.
- `authority_environment` (function, lines 547-568) — The deterministic launch environment:
  refuses an ambient `DAGGER_HOST` that conflicts with the admitted endpoint, then pins
  `DAGGER_HOST` and `AR_DAGGER_RUNTIME_AUTHORITY_DIGEST`.
- `load_host_declaration` (function, lines 569-587) — Loads the sole declaration from the
  `AR_DAGGER_RUNTIME_AUTHORITY` environment source.
- `AuthorityRegistry` (class, lines 588-833) — The host-level locked registry: state/owners files
  plus `authority.lock`; `state`/`_write_state`/`_owners_payload`/`owners`/`_write_owners`
  (lines 605-689) persist typed state and owner records; `census`, `reconcile_stale`,
  `live_owners` (lines 719-752) count live owners and reconcile crash-stale rows; `activate` and
  `enter_barrier` (lines 753-784) implement zero-owner activation and typed barrier entry;
  `register_owner` and `release_owner` (lines 785-833) add and exact-release owner records.
- `process_fingerprint_live`/`_host_process_fingerprint`/`current_process_fingerprint`
  (functions, lines 859-886) — PID-reuse-safe liveness: a digest of the host boot id plus the
  process start tick, never PID alone.
- `owner_identity` (function, lines 908-924) — One operation owner id from operation kind,
  scope, generation, and authority digest.
- `default_registry_root` (function, lines 925-932) — `~/.agents-remember/dagger-authority`
  unless `AR_DAGGER_AUTHORITY_ROOT` is configured.
- `admit_dagger_authority` (function, lines 933-989) — The public admission entry: loads and
  inspects the declaration, freezes the snapshot, builds the launch environment, and (with a
  registry) registers the live owner under `_admit_with_registry` (lines 990-1030).
- `_raise_transition_barrier` (function, lines 1031-1059) — The typed refusal when the declaration
  changed while live owners still use the old authority.
- `reuse_authority_for_continuation` (function, lines 1060-1114) — Retry/recovery/lifecycle
  continuation on the frozen snapshot: never re-resolves ambient state, never silently binds a
  different engine or store, and stays behind the typed barrier when other owners are live.
- `release_dagger_authority` (function, lines 1115-1132) — Terminalizes one owner, releasing only
  the exact registered owner record.

### Conventions

The declaration source is the sole authority; ambient or per-worktree `DAGGER_HOST` values never
merge with the admitted snapshot. All registry mutations run inside `exclusive_access` on the
registry lock, and every stored digest is validated 64-hex before use. No module in this file ever
copies or deletes the reusable layer store, retires an engine owned elsewhere, or provisions a
private engine or volume.

### Invariants And Boundaries

- One host-level declaration outside every repository and worktree selects one already-running,
  connection-only engine and the exact reusable store; the registry never holds the declaration
  itself.
- Admission happens before any Dagger command starts, and inspection is connection-only: a
  provisioning-capable endpoint, missing store mount, non-running engine, or ambiguous liveness is
  a typed refusal, never a fallback to ambient state.
- The frozen snapshot digest participates in operation fingerprints, sandbox manifests, published
  quality manifests, and recovery equality; a changed declaration with live owners creates a typed
  transition barrier and never serves two authorities concurrently.
- Owner release requires the exact owner record and matching process liveness; stale rows are
  reconciled only by crash reconciliation, which never rewrites an operation result.
- All refusals raise `DaggerRuntimeAuthorityError` (status
  `dagger-runtime-authority-invalid`) before any command is launched.

### Todos

None.

## Docs References

CCR-R12@v4 (260831-CCR-L12 implementation-readiness analysis, 260903-CCR-L12-implementation-readiness)
requires one host-level declaration outside every repository/worktree selecting exactly one
already-running connection-only Dagger endpoint and the exact reusable layer-store identity, a
trusted host launch boundary for every production Dagger execution, pre-admission engine/container
and store verification with a frozen immutable authority snapshot bound into the operation
fingerprint, and a locked host-level registry covering repositories, worktrees, operation kinds,
and generations with process-start liveness, typed transition barriers, and crash reconciliation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission verifies the actual engine/container and the exact store at `/var/lib/dagger` before freezing a safe immutable snapshot. | `admit_dagger_authority`; `DockerEngineInspector` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:933-989; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:202-333 |
| The frozen snapshot/digest binds into the operation fingerprint, manifest, and retry/recovery equality, never re-resolving ambient state. | `authority_snapshot`; `reuse_authority_for_continuation` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:516-546; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:1060-1114 |
| A declaration change while old owners remain creates a typed transition barrier; the replacement activates only after a locked zero-owner census. | `AuthorityRegistry.enter_barrier`; `_admit_with_registry` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:766-784; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:990-1030 |
| Owner liveness uses a process-start fingerprint rather than PID alone; terminalization releases only the exact owner. | `process_fingerprint_live`; `release_dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:859-864; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:1115-1132 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the strict host-declaration model with declaration digest and manifest rendering. | `DaggerHostDeclaration`; `declaration_digest` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:82-112; mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:92-102 |
| Defines the immutable frozen authority snapshot consumed by every admitted launch. | `DaggerAuthoritySnapshot` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:124-150 |
| Defines the host-level locked owner registry with census, barrier, activation, and exact release. | `AuthorityRegistry` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:588-833 |
| Defines the public admission entry that loads/inspects/freezes and registers the live owner. | `admit_dagger_authority` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:933-989 |
| Defines the continuation entry that reuses a frozen snapshot for retry/recovery without ambient re-resolution. | `reuse_authority_for_continuation` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:1060-1114 |
| The clean executor crosses this boundary for every profile-declared Dagger launch and releases its exact owner on terminalization. | `run_clean_quality`; `_quality_owner` | mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:140-229; mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py:849-873 |
| The typed refusal surface shared by every authority defect. | `DaggerRuntimeAuthorityError` | mcp/src/agents_remember/errors.py:52-65 |

## Cross-Repo References

No cross-repository implementation dependency governs this authority; the declaration source and
registry live host-level and outside every repository and worktree.

| Finding | Anchor | Source |
| --- | --- | --- |
| The default registry root is host-local (`~/.agents-remember/dagger-authority`) unless `AR_DAGGER_AUTHORITY_ROOT` is set. | `default_registry_root` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:925-932 |

## Update History

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass: created this file-level
  onboarding card for the new host-level shared Dagger authority layer (CCR-R12@v4) delivered in
  code commit cfd09381; anchors and ranges derived from the current worktree source and pinned to
  that commit.
