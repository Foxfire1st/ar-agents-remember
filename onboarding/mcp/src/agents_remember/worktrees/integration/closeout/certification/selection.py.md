# mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:58:25+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Reopens the complete explicitly selected certification graph and selects validated original evidence through the lifecycle journal CAS.

## Code Commentary

### Logic

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

## Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolved registry supplies no applicable external Domain Documentation source for this card. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact object kinds and the loaded graph have typed owners. | `load_typed`; `LoadedCertificationSelection` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:72-80; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:84-91 |
| Readback follows bounded explicit generations and validates every original graph binding. | `require_selected_certification`; `_load_selection`; `_load_predecessor` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:105-109; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:112-195; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:198-228 |
| Inherited terminals and recompiled admissions retain the exact original context. | `_require_inherited_terminals`; `_recompile_admission` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:241-256; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:259-296 |
| Complete terminal chains and every recovery decision are checked against the retained certificate pool. | `_require_terminal_chain`; `_require_recovery_history` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:299-309; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:312-337 |
| Terminal loading reopens original publication bytes and validates full result/certificate authority. | `load_selected_terminal`; `terminal_selection` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:340-382; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:385-400 |
| Memory inputs have exact canonical byte storage and typed readback. | `recovery_memory_inputs`; `retain_memory_inputs` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:403-413; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:416-423 |
| Only explicit interrupted evidence can be replaced; red retry requires a successor. | `_require_interrupted_terminal`; `require_unchanged_retry_admissible` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:426-442; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:94-102 |
| Selection uses a live-owner CAS and preserves terminal history on the permitted replacement. | `select_certification_state`; `select_recorded_terminals` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:445-463; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:466-499 |

## Cross-Repo References

No cross-repository implementation or external protocol is owned here.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separately configured cross-repository source is used for this card. | — | — |
## Update History

- 2026-09-06T14:58:25+00:00 — Created after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Records current implementation and remaining composition boundaries; source verification is not gate execution, delivery or acceptance.
