# mcp/src/agents_remember/memory_quality/incremental_scope/subresult_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/subresult_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `993953760ef65c4670a40c63a6d6ef0fbcddbe3b`|
| lastVerifiedCommitDate | 2026-09-03T02:13:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Owns bounded, atomic, content-addressed storage for exact CCR-R07 affected-unit results: one
immutable canonical JSON object per SHA-256 address, with no newest-result lookup and an explicit
operation-scoped capacity policy whose reclamation owner is named.

## Code Commentary

### Logic

`SubresultStorePolicy` (`subresult_store.py:22-28`) fixes the operation scope
(`scopeId`), the object/byte capacity bounds, and the `reclamationOwner`.
`ContentAddressedSubresultStore` (`subresult_store.py:31-119`) publishes one validated
`AffectedUnitResult` at `root/sha256/<aa>/<digest>.json` (`exact_path`,
`subresult_store.py:86-92`), refusing a content-address collision whose bytes differ, enforcing
capacity against the policy (`_require_capacity`, `subresult_store.py:94-119`), writing through
`atomic_write_bytes`, and reading back the exact canonical bytes.
`load` (`subresult_store.py:67-84`) validates the stored object and refuses stored bytes that do
not match the requested digest address. Canonical bytes are the compact sorted-key JSON plus a
trailing newline (`_canonical_bytes`, `subresult_store.py:122-126`); reads require regular,
readable files (`_read_regular_file`, `subresult_store.py:129-143`). Refusals are typed
`GateFiveClosureRefusedError` (`_refuse`, `subresult_store.py:146-154`).

### Conventions

The store is a pure content-addressed object store for the reviewed R07 executor; it never scans,
lists newest results, or evicts objects — capacity refusal names the reclamation owner instead.

### Invariants And Boundaries

- Address equality implies byte equality; a collision with different bytes refuses.
- Publication is atomic and read-back verified; a stored object that fails exact schema or digest
  validation refuses.
- Capacity is bounded per operation scope; exceeding it refuses rather than evicting.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for subresult retention.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Required Behavior"; "Exclusions And Forbidden Overreach") requires retaining unchanged
valid memory subresults, reusing exact subresults on an unchanged interrupted closure, and no
newest-result search.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The store publishes and loads exact SHA-256-addressed unit results. | `ContentAddressedSubresultStore`; `publish`; `load` | mcp/src/agents_remember/memory_quality/incremental_scope/subresult_store.py:31-119 |
| Capacity and object-safety boundaries are enforced with typed refusals. | `_require_capacity`; `_read_regular_file` | mcp/src/agents_remember/memory_quality/incremental_scope/subresult_store.py:94-119; mcp/src/agents_remember/memory_quality/incremental_scope/subresult_store.py:129-143 |
| Atomic writes come from the kernel-owned writer. | `atomic_write_bytes` | mcp/src/agents_remember/kernel/atomic_write.py:51-72 |
| Store edges are proven by the focused suites. | `test_r07_subresult_store_is_exact_atomic_bounded_and_has_no_latest_lookup`; `test_r07_subresult_store_refuses_collision_readback_and_wrong_address`; `test_r07_subresult_store_refuses_nonregular_or_unreadable_objects` | mcp/tests/test_memory_incremental_scope_model_edges.py:385-415; mcp/tests/test_memory_incremental_scope_model_edges.py:1102-1137; mcp/tests/test_memory_incremental_scope_model_edges.py:1140-1154 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The store persists inside the coordination memory area, not the code repository. | — | — |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Corrected incoming references and schema ownership against the reviewed candidate; unchanged source retains its genuine verification stamp.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References row as prose.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card for the new content-addressed subresult store; no prior sidecar existed.
