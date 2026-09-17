# mcp/src/agents_remember/memory/knowledge/labels.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/labels.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

**Friendly-label edits on the two identity rows, and the concurrency guard they carry.** A display label is the
one field of an identity row that may legitimately change: everything that makes the identity an identity — its
ID, its namespace and, for a revision, its sealed payload — is immutable, so a label edit is not a rewrite of the
subject but a change to how a reader displays it. Because it is the one mutable field, it is also the one place a
stored row can differ from the copy a caller read, which is why **every label edit names the exact row it
expects**.

Both identity rows are shaped the same way (identity columns, a label, an authorship envelope), so the guard, the
update and the result shape live here once for both concepts.

## Code Commentary

### Logic

- Each edit has **two entry points**, and the split is the point:
  - `set_invariant_label` / `set_family_label` are the *operations*: they check scope, take the candidate's
    exclusive lock, run `store.within_immediate` with a `SqliteFailureContext` naming the operation, table and
    record, and return the typed `SetInvariantLabelResult`/`SetFamilyLabelResult`.
  - `apply_invariant_label` / `apply_family_label` are the *in-transaction steps*: they raise a typed refusal for
    the caller to map or roll back, and they return **whether a statement ran**.
- The guard order inside an apply step is what makes it correct: read the row (**unknown identity** refuses),
  compare `expected_row_digest` against the stored `row_digest` (**stale caller** refuses, naming expected and
  observed), and only then compare the requested label with the stored one. A requested label that already
  matches returns `False` **before** the UPDATE, so no statement runs and no receipt entry is claimed.
- The digest the caller names is the same value `get_invariant`/`get_family` expose as `row_digest`, so an
  expectation is carried straight from a read instead of being recomputed by a second rule.
- The result models enforce their own consistency: a `labeled` result must carry the label it stored and no
  refusal; a `refused` result must carry its refusal. `_apply_*_label` therefore constructs only the success
  shape, and the two `_*_label_refusal` helpers only the failure shape.

### Conventions

- The two concepts share one shape deliberately: the guard, the UPDATE and the result construction read
  identically for both, and each function names its own table and operation in the refusal it raises.
- The store exposes `set_invariant_label` as a thin method delegating here
  (`OpenedKnowledgeStore.set_invariant_label`), so a caller holding an opened store does not need a second
  import; the family twin is reached through the application seam's `labels.set_family_label`.
- `__all__` lists exactly the four public names.
- **The batch path shares `apply_*` and does not share the operations.** A batch command calls `apply_*` inside
  the batch's own transaction, and uses `False` to omit a receipt row for an edit that wrote nothing.

### Invariants And Boundaries

- **A label edit is not an identity edit.** Nothing here can change an ID, a namespace, a provenance envelope or
  a revision payload; the UPDATE touches `display_label` only.
- **The row digest is the concurrency guard.** A caller that read a row and lost the race is told
  (`stale_precondition`) rather than obeyed — the stored row is left byte-identical.
- **`False` means "no statement ran".** The return value is a receipt fact, not a success flag: a caller that
  treats `False` as failure would be wrong, and a caller that reports a write for it would overstate the receipt.
- **Both entry points are needed for the guard to be load-bearing.** The batch path carries an independent copy
  of the expectation rule in `batch_preconditions._require_identity`, so a case that only drives the batch would
  stay green with this CAS deleted — which is why the standalone operations have their own module of evidence.
- **Boundary.** This module owns the two label edits and their guard. Who may edit (admission) is the
  application seam's, and when a batch may edit is the precondition module's.

### Todos

None recorded for this slice. The two label edits are the only identity edits the store exposes by design; a
future editable identity field would need its own guard here rather than widening the UPDATE.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The invariant label operation: scope, lock, one transaction, typed result. | `set_invariant_label` | mcp/src/agents_remember/memory/knowledge/labels.py:40-59 |
| The in-transaction step: unknown identity, stale digest, then the no-op return before the UPDATE. | `apply_invariant_label` | mcp/src/agents_remember/memory/knowledge/labels.py:62-99 |
| The family twins, shaped identically. | `set_family_label`; `apply_family_label` | mcp/src/agents_remember/memory/knowledge/labels.py:102-121; mcp/src/agents_remember/memory/knowledge/labels.py:124-156 |
| The two result constructors, each producing only the shape its model permits. | `_apply_invariant_label`; `_apply_family_label`; `_invariant_label_refusal`; `_family_label_refusal` | mcp/src/agents_remember/memory/knowledge/labels.py:159-216 |
| The result models and their consistency validators. | `SetInvariantLabelResult`; `SetFamilyLabelResult` | mcp/src/agents_remember/models/knowledge/result.py:511-531; mcp/src/agents_remember/models/knowledge/result.py:534-554 |
| The request models, each naming the row the caller read. | `SetInvariantLabelRequest`; `SetFamilyLabelRequest` | mcp/src/agents_remember/models/knowledge/result.py:306-317; mcp/src/agents_remember/models/knowledge/result.py:320-326 |
| The stale-caller refusal wording, shared with the removals. | `stale_expected_row_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:531-551 |
| The batch command that shares these apply steps and omits a receipt row when nothing was written. | `_set_invariant_label`; `_set_family_label` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:474-510 |
| The batch's own copy of the expectation rule, which is why the standalone path needs its own evidence. | `_require_identity` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:311-348 |
| The standalone operations' entry points in the composition seam. | `set_knowledge_invariant_label`; `set_knowledge_family_label` | mcp/src/agents_remember/application/knowledge.py:224-250 |
| The store method that delegates here. | `set_invariant_label` | mcp/src/agents_remember/memory/knowledge/store.py:291-294 |
| The six nodes that drive the standalone entry points, including the stale-expectation case the batch path cannot cover. | "test_a_stale_invariant_label_expectation_refuses_and_leaves_the_row_identical"; "test_a_stale_family_label_expectation_refuses_and_leaves_the_row_identical" | mcp/tests/test_knowledge_label_operations.py:94-140; mcp/tests/test_knowledge_label_operations.py:205-244 |
| The node that pins the no-op label edit inside a mixed batch. | "test_a_no_op_label_edit_inside_a_mixed_batch_is_not_reported_as_a_write" | mcp/tests/test_candidate_batch_transaction.py:799-845 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T07:33:51+00:00: Generated citation repair: `SetInvariantLabelResult`; `SetFamilyLabelResult` repointed to mcp/src/agents_remember/models/knowledge/result.py:511-531; mcp/src/agents_remember/models/knowledge/result.py:534-554. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `SetInvariantLabelRequest`; `SetFamilyLabelRequest` repointed to mcp/src/agents_remember/models/knowledge/result.py:306-317; mcp/src/agents_remember/models/knowledge/result.py:320-326. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/src/agents_remember/models/knowledge/result.py:306 to the row 97 of this card as the citation for `SetInvariantLabelRequest`: no cited file carried the construct, and the checker named line(s) [306] in this file as its live location; added mcp/src/agents_remember/models/knowledge/result.py:511 to the row 96 of this card as the citation for `SetInvariantLabelResult`: no cited file carried the construct, and the checker named line(s) [511, 522] in this file as its live location
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `SetInvariantLabelRequest` in the row 97 of this card from mcp/src/agents_remember/models/knowledge/result.py:320-321 to mcp/src/agents_remember/models/knowledge/result.py:306-307, the extent of the construct the claim is about (the checker named line(s) [306] as its live location); re-pointed `SetInvariantLabelResult` in the row 96 of this card from mcp/src/agents_remember/models/knowledge/result.py:534-535 to mcp/src/agents_remember/models/knowledge/result.py:511-512, the extent of the construct the claim is about (the checker named line(s) [511, 522] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `SetFamilyLabelRequest` in the row 97 of this card from mcp/src/agents_remember/models/knowledge/result.py:306-307 to mcp/src/agents_remember/models/knowledge/result.py:320-321, the extent of the construct the claim is about (the checker named line(s) [320] as its live location); re-pointed `SetFamilyLabelResult` in the row 96 of this card from mcp/src/agents_remember/models/knowledge/result.py:511-512 to mcp/src/agents_remember/models/knowledge/result.py:534-535, the extent of the construct the claim is about (the checker named line(s) [534, 545] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/models/knowledge/result.py:320-321 in the row 97 of this card; the repetition added no pooled evidence; kept one copy of the repeated citation mcp/src/agents_remember/models/knowledge/result.py:534-535 in the row 96 of this card; the repetition added no pooled evidence
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the two friendly-label edits. It records the operation/apply split and why both entry points are needed, the guard order (unknown identity, stale digest, no-op before the UPDATE), the `False`-means-no-statement rule the batch receipt depends on, and the recorded reason the standalone path needs its own evidence module: the batch carries an independent copy of the expectation rule, so a batch-only case would stay green with this guard deleted. Verification metadata remains empty until closeout stamps the code commit.
