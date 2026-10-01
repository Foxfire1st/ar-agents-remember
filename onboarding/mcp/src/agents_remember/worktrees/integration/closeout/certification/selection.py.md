# mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Reopens the complete explicitly selected certification graph and selects validated original evidence through the lifecycle journal CAS.

## Code Commentary

### Logic

`_require_selection_binding` checks the exact candidate tree, contract, admission, registry, plans, profile and prior-red disposition. The extraction preserves the immutable graph and retry rules.

`require_selected_certification` follows only named predecessor generations, bounded to 256 with a per-read cache. It verifies operation/contract/task identity, exact stored object kinds and bytes, frozen profile/plan/admission bindings, and distinct candidate-authority digests. Each predecessor must be the immediately preceding archived generation with matching predecessor/successor fingerprints; input terminals must equal that predecessor's selected terminals.

Every terminal reopens its retained original publication and result/certificate references. Inherited terminals use their original frozen run, results are recompiled, nested evidence and full publication authority are checked, and certificate chains remain ordered. Lifecycle admission and every recovery decision are recompiled from the exact retained certificate pool and canonical optional memory inputs. The returned protected-generation set includes current, historical and recursively inherited publications needed by later readback.

`select_certification_state` validates the proposed graph before the live-owner observation and expected-current store CAS. `select_recorded_terminals` preserves exact repeated originals. A different terminal can replace only the final uncertified terminal whose retained decoder explicitly records an interruption; the old terminal is appended to history. A red result is retained as evidence and cannot masquerade as an interrupted green result or authorize an unchanged retry.

### Conventions

`RetainedCertificationBytes` carries canonical original publication or memory-input bytes with SHA-256. Typed references locate immutable store objects; neither mechanism searches a latest pointer or reconstructs original provenance from semantic identity.

### Invariants And Boundaries

- Lost CAS, cancellation, wrong generation/contract, missing or corrupted references, mismatched prefixes and incoherent inherited history refuse selection.
- `require_unchanged_retry_admissible` requires an explicit corrective successor for selected red catalogs.
- Exact same terminal publication is idempotent; replacing a certified result or nonfinal result refuses.
- Terminal history and recovery decisions remain append-only under the journal model/store rules.
- Reuse and pruning protection cover the complete reopened graph, not only the current generation's report pointer.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- Exact object kinds and the loaded graph have typed owners. [1]
- Readback follows bounded explicit generations and validates every original graph binding. [2]
- Inherited terminals and recompiled admissions retain the exact original context. [3]
- Complete terminal chains and every recovery decision are checked against the retained certificate pool. [4]
- Terminal loading reopens original publication bytes and validates full result/certificate authority. [5]
- Memory inputs have exact canonical byte storage and typed readback. [6]
- Only explicit interrupted evidence can be replaced; red retry requires a successor. [7]
- Selection uses a live-owner CAS and preserves terminal history on the permitted replacement. [8]

### Cross-Repo References

No cross-repository implementation or external protocol is owned here.


No separately configured cross-repository source is used for this card.
