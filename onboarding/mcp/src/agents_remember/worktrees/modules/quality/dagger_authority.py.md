# mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py

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
the exact live consumer in a host-level locked owner registry. Registry writes serialize through the shared kernel file-lock primitive under
POSIX flock; owner liveness uses a process-start fingerprint rather than PID alone so a reused PID
cannot release or suppress another live owner. When the host declaration changes while owners
still run, a typed transition barrier lets old operations finish on their frozen authority while
every fresh admission is refused until the old authority live-owner census reaches zero, at which
point the replacement activates atomically. Terminalization releases only the exact owner; crash
reconciliation drops only stale owner rows and never rewrites an operation primary result. Every
refusal is a typed `DaggerRuntimeAuthorityError` raised before any Dagger command starts.

## Code Commentary

### Logic

`DaggerHostDeclaration` is the sole parsed declaration: connection-only endpoint, absolute reusable layer-store path, pinned engine version and source. `_sha256` supplies sorted compact-JSON digests; the declaration and `DaggerAuthoritySnapshot` render immutable manifests. `DockerEngineInspector` uses connection-only `docker inspect` facts and best-effort version observation; it never provisions an engine or store. Parsing refuses unsupported, malformed, repository-local, provisioning-capable and ambient-conflicting declarations. `authority_environment` pins the admitted endpoint and authority digest.

`AuthorityRegistry` owns `state.json`, `owners.json` and resource path `authority.lock`. Its `exclusive_access` delegates to the kernel's single `exclusive_file_lock` primitive, preserving the existing physical `authority.lock.lock` path. It translates `LockCapabilityError` to `DaggerRuntimeAuthorityError` with finding `runtime-authority-registry-lock-unsafe`. This host policy does not use `StoreOwnership`, does not call the checkout coordinator guard, and does not confer a process execution role.

`admit_dagger_authority` loads/inspects/freezes the declared authority and, when given a registry, enters `_admit_with_registry` under that registry lock. State and owner records are validated before use; `census`, `reconcile_stale` and `live_owners` use process-start liveness, while `activate` and `enter_barrier` implement zero-owner authority transitions. A changed declaration with live owners creates an `awaiting-zero-census` barrier; replacement activation requires the old live census to reach zero.

`DaggerOwner` binds authority digest, operation kind, scope, generation, PID, process fingerprint and start time. `owner_identity` derives the operation owner id; process liveness uses host boot id plus process-start tick rather than PID alone. `register_owner` adds the exact record and `release_owner` releases only its matching live identity. Crash reconciliation removes stale rows without rewriting the operation's primary result.

`reuse_authority_for_continuation` acquires the same registry lock and uses the original frozen snapshot without re-resolving ambient state. It preserves the active authority and transition barrier rules and registers a missing exact continuation owner. `release_dagger_authority` returns immediately for ownerless admission; otherwise it exact-releases under that same lock. `default_registry_root` selects the host-local `.agents-remember/dagger-authority` root unless the dedicated host registry environment setting is configured.

### Conventions

The declaration source is the sole authority; ambient or per-worktree `DAGGER_HOST` values never
merge with the admitted snapshot. Admission, continuation and release hold `AuthorityRegistry.exclusive_access` across their complete registry transactions, and every stored digest is validated 64-hex before use. No module in this file ever
copies or deletes the reusable layer store, retires an engine owned elsewhere, or provisions a
private engine or volume.

### Invariants And Boundaries

- The host registry uses shared kernel exclusion under its own authority policy. It neither grants checkout coordinator access nor declares MCP/test/lifecycle execution to acquire its lock.
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

## Evidence

### Docs References

No external Domain Documentation source is configured. This module implements the repository-owned CCR-R12 host authority contract; the source references below establish its current behavior, without an external documentation claim.

No configured external domain documentation source.

### Repo-Internal References

The declaration, registry and frozen continuation are production owners. The focused test provides coordinator containment and lock composition evidence; the engine inspector double does not prove live engine health.

- Strict declaration, live inspection and immutable authority snapshot. [1]
- Declaration parsing, host location and connection-only endpoint policy. [2]
- Launch environment is bound to the admitted snapshot. [3]
- Host registry transaction entry, domain refusal, census, barriers and exact owner mutations. [4]
- Admission freezes one authority and changes registry state under its lock. [5]
- Continuation and terminal release share the same physical registry lock. [6]
- Process-start liveness and operation-scoped owner identities. [7]
- Host-local registry root configuration. [8]
- One physical lock protocol, actual thread/process exclusion and capability probe. [9]
- Typed lock and authority refusal surfaces. [10]

### Cross-Repo References

The host declaration and owner registry are outside repositories/worktrees, but this file introduces no separate cross-repository implementation dependency. Their repository-owned location and policy are cited above.

No separate cross-repository implementation dependency.
