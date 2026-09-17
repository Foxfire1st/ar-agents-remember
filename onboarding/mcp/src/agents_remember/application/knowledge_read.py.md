# mcp/src/agents_remember/application/knowledge_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l07` uncommitted source; base `4eb2b1992f6183fba06e9f31aa664d9a93094c26` |
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The application seam for the selective recorded-scope read (`KS-R07`).** One explicit context, one seed,
one bounded page: it admits a context, delegates selection to `memory.knowledge.read`, and returns the
typed result unchanged. It is the fourth application seam beside `knowledge.py`,
`knowledge_snapshot.py`, `knowledge_merge.py` and `knowledge_export.py`, and like them it decides no
authority and holds no durable state.

## Code Commentary

### Logic

**Three boundaries this module owns, each because getting it wrong is a different kind of wrong:**

1. **The read is read-only, and that is how a refusal persists nothing.** The connection is opened through
   `open_read_only_database`, so the strongest statement available to this operation is a `SELECT`. "A
   refused read left the file byte-identical" is therefore a property of the handle rather than a rollback
   this code has to remember — and `read_row_counts` is the measurement half, reading the real file through
   the same read-only handle so a caller can take counts before and after a refusal and compare.
2. **A baseline read needs no task.** A context with `task_ref=None` is served: this operation never
   resolves a leaf contract, never asks an enclosure owner for one and never fabricates a task to satisfy
   a check. Planning has to be able to read recorded knowledge before a leaf exists.
3. **A continuation is a binding, not a position.** The cursor is verified against the snapshot, the
   context, the selector, the policy and the schema it names **before the file is opened**, and against the
   selected set's manifest and its own position **after** the snapshot is verified and **before** a page is
   built; a cursor that binds something else is refused with **no partial page**. A continuation carries the
   seed forward rather than replacing it: the caller re-sends the selector and the cursor's own
   `seed_digest` is what proves it is the same one.

`read_knowledge_scope(database_path, context, request)` is the entry point and it **never raises for a
caller to catch**. `context` and `request` are the typed models and not `Any`, and the docstring says what
that buys: every input class this operation answers is a field of one of those two, so reaching it with an
arbitrary object is a programming error at the call site rather than a modeled read failure. Inside that
contract, `OSError`, `apsw.Error`, `KnowledgeStorageError`, `SelectionIncomplete` and a malformed cursor
are all named outcomes inside `KnowledgeReadResult`.

The ordered sequence inside one read-only connection (`_select_and_page`):

1. **The declared snapshot is verified** (`_snapshot_identity_refusal`), through **three separate
   comparisons**, each a different fact and each checked before anything is selected: the file must be
   bound to the requested namespace, it must implement the **schema generation** the context declares, and
   it must hold the **declared logical dataset**. The schema comparison is its own statement rather than a
   corollary of the digest: a context that keeps the file's real digest while declaring another generation
   reaches it directly, and **only** it. Each refusal names the comparison that fired, with both
   identities.
2. **The scope is selected** (`select_recorded_scope`, with `anchor_resolver_for(context)` supplying the
   source-resolution seam).
3. **The typed absence is decided** (`_absence_refusal`): a path seed with no recorded claim is
   `registration_absent`; an identity or revision the snapshot does not hold is `selector_absent`; a
   **recorded** identity whose selected revisions carry no memberships and no claims is an empty but real
   selection, served with its zero counts so the caller sees the recorded record rather than a claim that
   nothing exists.
4. **The continuation is checked against the selection** (`_continuation_refusal`): the position must be a
   position *in* that set (`position > len(scope.items)` is `continuation_binding_mismatch` naming the
   selection size and the position), and the manifest must be that set's manifest
   (`_manifest_binding_mismatch`). Both are decided before a page is built, so a hand-edited position is
   refused rather than sliced or handed to a model constraint.
5. **The page is cut** (`page_of_scope`), and a page too small for its next item is turned into
   `page_budget_too_small` with the exact minimum.

**The request-level cursor binding is checked once, before the file is opened, and that placement is a
decision rather than an accident:** a continuation that binds another selection is a defect of the
*request* and not a fact about the bytes, so reporting it as a snapshot problem would send the caller to
re-select a dataset they selected correctly. The scope-dependent half (the manifest) is checked where the
selection it names exists, which is the only point at which it can be checked at all.

**`open_read_context(database_path, repository_id, …)` is the constructor a caller uses to build a
context.** It opens the file read-only, reads the logical identity the file actually holds, and returns a
context naming **that** exact snapshot — so a caller cannot hand-write the snapshot a read will be
verified against; it can only resolve one, and the read compares that resolution again against the file it
opens. A file bound to another namespace is refused by name.

### The callable surface

```python
from agents_remember.application.knowledge_read import (
    read_knowledge_scope,   # (database_path, context, request) -> KnowledgeReadResult
    open_read_context,      # (database_path, repository_id, *, repository_root=None,
                            #  code_tree_id=None, task_ref=None) -> KnowledgeReadContext
    read_row_counts,        # (database_path) -> dict[str, int]  (the persisted-nothing measurement)
)
```

### Conventions

- **Every failure on the way out is a typed `KnowledgeRefusal` inside the result.** A schema this build
  does not implement, a database bound elsewhere, a missing canonical table and a typed JSON column that
  does not decode all become `snapshot_unavailable` naming the offending comparison; an absent or
  unreadable file becomes `selected_input_unavailable`.
- **The one class that does not reach this boundary is a caller passing an object which is not one of the
  two typed models** — that is a programming error at the call site, and the module says so rather than
  implying a generality its signature does not have.
- `ROW_COUNT_TEMPLATE` is the one statement shape this module runs that changes nothing, and the table
  names come from `schema.CANONICAL_TABLES`, never from a caller.

### Invariants And Boundaries

- **This seam decides no authority.** It does not resolve a task, does not decide whether a candidate is
  admitted, does not publish, and does not carry a semantic verdict. `task_ref` is **carried, not decided**.
- **The read is read-only.** No statement this operation issues can write, and the persisted-nothing
  property is measured rather than promised.
- **A continuation never mixes revisions.** No refusal on the cursor path returns partial items.
- **No tool naming and no advertisement here.** The requirement keeps the public tool name separate from
  the concrete application function, and this module exposes no MCP tool.
- **`read_files.py` is not reused for tree paths.** Its `confine_rel` resolves against a real directory and
  follows a symlink; the read path's confinement is structural (see `read_anchors.py`).
- **Boundary.** This module composes. It owns neither the selection policy (`memory.knowledge.read`), nor
  the observation (`read_anchors.py`), nor the refusal vocabulary (`read_refusals.py`), nor the models
  (`models.knowledge.read`).

### Todos

None recorded. One carried observation belongs to the owning seat: this seam is the boundary the leaf's
`page_budget_too_small` / `continuation_binding_mismatch` / absence codes are asserted through, and the
**non-zero-exit** producer of `recorded_object_unavailable` is disclosed as an unasserted defensive branch
rather than coverage (L9 ledger **A6**).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The constructor that resolves a context from the identity the file actually holds, so a caller cannot hand-write the snapshot a read is verified against.** | `open_read_context` | mcp/src/agents_remember/application/knowledge_read.py:103-136 |
| **The entry point, its typed parameters and the never-raises contract inside them.** | `read_knowledge_scope` | mcp/src/agents_remember/application/knowledge_read.py:139-192 |
| **The read-only handle, the request-level cursor check before the file is opened, and the close.** | `_read_inside_snapshot` | mcp/src/agents_remember/application/knowledge_read.py:195-225 |
| **The ordered sequence: verify the snapshot, select, decide absence, check the continuation, page, refuse a too-small budget.** | `_select_and_page` | mcp/src/agents_remember/application/knowledge_read.py:228-271 |
| **The three separate snapshot comparisons — namespace, schema generation, logical dataset — each naming the comparison that fired.** | `_snapshot_identity_refusal` | mcp/src/agents_remember/application/knowledge_read.py:274-313 |
| **The scope-dependent half of the cursor binding: a position past the end is typed, and the manifest must be this selection's.** | `_continuation_refusal`; `_manifest_binding_mismatch` | mcp/src/agents_remember/application/knowledge_read.py:316-337; mcp/src/agents_remember/application/knowledge_read.py:496-516 |
| **The request-level cursor bindings, checked once before the file is opened.** | `_cursor_mismatch` | mcp/src/agents_remember/application/knowledge_read.py:468-493 |
| **The two absence codes, and the recorded-but-empty selection that is served rather than refused.** | `_absence_refusal`; `_invariant_identity_is_recorded`; `_family_identity_is_recorded` | mcp/src/agents_remember/application/knowledge_read.py:357-389; mcp/src/agents_remember/application/knowledge_read.py:392-414; mcp/src/agents_remember/application/knowledge_read.py:417-439 |
| **The persisted-nothing measurement, read through the same read-only handle the operation uses.** | `read_row_counts`; `ROW_COUNT_TEMPLATE` | mcp/src/agents_remember/application/knowledge_read.py:587-602; mcp/src/agents_remember/application/knowledge_read.py:98-100 |
| The result assembly for a page and for a refusal, and the unusable-snapshot rendering. | `_page_result`; `_refused`; `_unusable_snapshot`; `_small_budget_refusal` | mcp/src/agents_remember/application/knowledge_read.py:446-465; mcp/src/agents_remember/application/knowledge_read.py:576-584; mcp/src/agents_remember/application/knowledge_read.py:556-573; mcp/src/agents_remember/application/knowledge_read.py:340-354 |
| **The nodes that measure the binding refusals, each with its own positive control.** | "test_a_continuation_presented_with_another_selector_refuses_and_returns_no_partial_page"; "test_a_continuation_presented_under_another_context_or_policy_refuses"; "test_a_continuation_that_binds_another_manifest_is_refused_and_its_own_is_verified"; "test_a_continuation_naming_a_position_past_the_selection_refuses_rather_than_escaping"; "test_a_continuation_against_its_own_snapshot_continues_the_same_manifest" | mcp/tests/test_knowledge_read_boundaries.py:576-604; mcp/tests/test_knowledge_read_boundaries.py:605-663; mcp/tests/test_knowledge_read_boundaries.py:664-724; mcp/tests/test_knowledge_read_boundaries.py:725-762; mcp/tests/test_knowledge_read_boundaries.py:859-892 |
| **The task-free baseline read node, the snapshot/namespace/schema refusal nodes and the absent-database node.** | "test_a_baseline_read_serves_a_task_free_context_and_reaches_the_whole_selected_scope"; "test_a_context_naming_another_namespace_refuses_and_names_both_identities"; "test_a_context_whose_logical_digest_is_not_the_files_is_refused"; "test_a_context_declaring_another_schema_generation_is_refused_before_a_page_is_built"; "test_an_absent_database_refuses_as_an_unavailable_input_rather_than_as_empty_knowledge" | mcp/tests/test_knowledge_read_boundaries.py:465-497; mcp/tests/test_knowledge_read_boundaries.py:498-527; mcp/tests/test_knowledge_read_boundaries.py:528-553; mcp/tests/test_knowledge_read_boundaries.py:763-826; mcp/tests/test_knowledge_read_boundaries.py:554-575 |
| The read-only connection the seam opens. | `open_read_only_database` | mcp/src/agents_remember/memory/knowledge/connection.py:52-63 |
| The schema identity the seam inspects before it selects anything. | `inspect_schema` | mcp/src/agents_remember/memory/knowledge/connection.py:106-122 |
| The existing reader whose confinement helper must **not** be reused for tree paths. | `confine_rel` | mcp/src/agents_remember/kernel/sidecar_pairing.py:37-58 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The read is addressed at one database and one
code tree inside one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-16T23:50+02:00 — 260915-KS-L07 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the read's application seam. It records the **three boundaries the module owns** — the read-only handle that makes "a refused read persisted nothing" structural (measured, not promised, by `read_row_counts`), the task-free baseline read that never fabricates a leaf, and the cursor as a **binding** rather than a position — plus the ordered sequence and the placement decision behind it: the request-level bindings are checked **before the file is opened** (a cursor binding another selection is a defect of the request, not a fact about the bytes) while the manifest and position bindings are checked **where the selection exists**. It records the three separate snapshot comparisons (namespace, schema generation, logical dataset) where the schema check is its own statement rather than a corollary of the digest, the two absence codes with the recorded-but-empty selection served rather than refused, and the never-raises contract *inside* the typed-parameter contract. It also carries the forward rule that `read_files.py`'s `confine_rel` must not be reused for tree paths because it follows a symlink. Verification metadata remains empty until closeout stamps the code commit.
