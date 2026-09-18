# mcp/src/agents_remember/application/knowledge_facets.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_facets.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T00:25+02:00 |
| lastVerifiedCommitHash | `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l11` uncommitted source; base `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The application seam for the facet-specific selection: one context, one seed, one complete page.**
`read_facet_scope` is the narrow API a caller uses to read the authored-judgment aggregate, and it is the
route's **sixth** composition seam beside `knowledge.py`, `knowledge_snapshot.py`, `knowledge_merge.py`,
`knowledge_export.py` and `knowledge_read.py`. Like its five siblings it decides no authority and holds no
durable state: it verifies the declared snapshot against the file it opened, delegates the selection to
`memory.knowledge.facet_read`, and returns the typed result unchanged.

The module exists because the facet aggregate is a **different selection** from `KS-R07@v1`'s recorded-scope
selection. Reading facets does not extend that selection's seeds, its item kinds, its counts or its policy
name; it declares its own policy (`authored-judgment-facets/v1`) and reuses the *shape* of a read — context,
result, snapshot — without sharing a code path. That non-overlap is what makes a shipped seed's serialized
page byte-identical across this leaf, and the module says so in its own docstring rather than leaving it to
be inferred from the diff.

## Code Commentary

### Logic

- **The read is read-only, and that is how "a refused read persisted nothing" is structural.** The
  connection is opened through the shipped `open_read_only_database`, so the strongest statement this
  operation can issue is a `SELECT`. The property is a fact about the handle rather than a rollback the
  code has to remember, and `facet_read.select_facet_scope` is written against that same handle.
- **The declared snapshot is verified before anything is selected, in three separate comparisons.** The
  file must be bound to the requested repository namespace (`bound_repository`), must implement the schema
  generation the context declares (`inspect_schema`), and must hold the declared logical dataset
  (`logical_digest`). Each disagreement returns `snapshot_unavailable` with the expected and observed
  values as facts, so a context describing another dataset is refused by name instead of being answered
  from whatever bytes the path happens to hold.
- **Absence and emptiness are two different answers.** A seed naming nothing recorded is
  `selector_absent` — the caller asked for a record the snapshot does not hold. A *recorded* facet record
  with no attachments and no supersession edges is **not** an absence: `_absence_refusal` consults
  `selection.seed_recorded` and returns `None`, so the page is served with the counts it really has and
  the caller sees the record rather than a claim that nothing exists.
- **The selection is complete or it refuses.** `FacetSelectionIncomplete` is caught here and converted into
  the shipped `selection_incomplete` refusal carrying the item count and the bound it reached. There is no
  cursor and no continuation contract, so a caller never receives a page it could read as the whole
  aggregate when it is not.
- **The result is built in one place per outcome.** `_read_inside_snapshot` builds the served result
  (`state="page"`, snapshot from `snapshot_of_context`, the seed digest, the selection's
  `manifest_digest`, the declared `FACET_SELECTION_POLICY_VERSION` and `_page`); `_refused` builds the
  refused result, which carries the same snapshot, context digest and seed digest but `page=None`.
- **Three failure families reach the same fallback for three different reasons.** A raised
  `KnowledgeStorageError` (an unimplemented schema, a namespace bound elsewhere, a missing canonical
  table, a typed-JSON column that does not decode), an `apsw.Error`, and an `OSError` on the path each
  become a typed refusal here rather than an exception out of the application layer — the first two
  through `_unusable_snapshot`, the last through `selected_input_unavailable_refusal`, which is also what
  an absent or non-file path earns.

### Conventions

- **One operation name, carried into every refusal.** `_OPERATION` is the single literal
  `"read_facet_scope"`, and it is passed to each refusal factory, so the operation a caller is told about
  is the operation it called.
- **The context model is shared, not copied.** `context` is the *same* `KnowledgeReadContext` the
  recorded-scope read uses — one definition of "which snapshot am I reading" rather than two — and the
  snapshot, context digest and seed digest are produced by the shipped helpers (`snapshot_of_context`,
  `read_context_digest`, `facet_seed_digest`) rather than re-derived.
- **The connection is always closed.** `_read_inside_snapshot` closes in a `finally`, so a refusal inside
  the selection cannot leak a handle.
- **The declared policy version travels on every result**, served or refused, so a caller can tell which
  selection produced a page from the page itself.

### Invariants And Boundaries

- **The shipped selection does not move.** This operation does not call `read_knowledge_scope`, does not
  share its policy name with it, and does not appear in its response; a shipped seed's page is unchanged
  because no code path is shared, not because a guard prevents an addition.
- **The seed is not a filter.** A `FacetReadRequest` carries exactly one seed, and the seed is either an
  exact record identity or an exact statement revision. Nothing here narrows a selection by a label, a
  path, a display version or a time.
- **Boundary.** This module owns the read path only: it does not author a facet (that is the write path in
  `memory/knowledge/facets.py`, reached through `application/knowledge.py`), does not declare the
  selection's items or counts (`models/knowledge/facet_read.py` does), and does not decide which schema
  generation a dataset is (`memory/knowledge/schema_generations.py` does).
- **Recorded detail rather than a defect claim.** The module docstring calls itself the **fifth**
  application seam while naming five seams before it; the route's own running count (and the L7 section's
  "fifth" for `knowledge_read.py`) makes this the sixth. The sentence is left as written and the position
  is recorded here, because a reader counting seams from either number should see which one this is.
- **Not admissible, recorded so it is not re-proposed:** adding a `has_more`/cursor pair to this
  selection. The declared contract is complete-or-refused, and a continuation surface would be a second
  declared policy the requirement did not ask for.

### Todos

None recorded. `FacetReadRequest` carries one seed today; a later leaf that needs a second question asks
for a second seed kind rather than widening this request with optional filters.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one entry point, its three refusal families and the operation name every refusal carries. | `read_facet_scope` | mcp/src/agents_remember/application/knowledge_facets.py:71-121 |
| The read-only handle, the delegate call and the served result, closed in a `finally`. | `_read_inside_snapshot`; "def select_facet_scope(" | mcp/src/agents_remember/application/knowledge_facets.py:124-154; mcp/src/agents_remember/memory/knowledge/facet_read.py:109-129 |
| **The absence-versus-emptiness split, and why a recorded record with no attachments is a page.** | `_absence_refusal`; `seed_recorded` | mcp/src/agents_remember/application/knowledge_facets.py:163-188 |
| **The three snapshot comparisons run before any selection, each naming expected and observed.** | `_snapshot_identity_refusal` | mcp/src/agents_remember/application/knowledge_facets.py:191-224 |
| The fallback that refuses a file which is not the selected snapshot, naming both identities. | `_unusable_snapshot` | mcp/src/agents_remember/application/knowledge_facets.py:227-241 |
| The refused result, which carries the snapshot and digests but no page. | `_refused` | mcp/src/agents_remember/application/knowledge_facets.py:244-256 |
| The declared policy name and the one operation name the module publishes. | "FACET_SELECTION_POLICY_VERSION ="; "def read_facet_scope(" | mcp/src/agents_remember/models/knowledge/facet_read.py:56-56; mcp/src/agents_remember/application/knowledge_facets.py:71-121 |
| The selection this seam delegates to: one query, one complete aggregate, the bound it raises past. | `FacetSelectionQuery`; `select_facet_scope`; `FacetSelectionIncomplete` | mcp/src/agents_remember/memory/knowledge/facet_read.py:85-91; mcp/src/agents_remember/memory/knowledge/facet_read.py:109-129; mcp/src/agents_remember/memory/knowledge/facet_read.py:68-82 |
| The shared read context the facet read reuses, and the shipped helpers that produce the result's snapshot and digests. | `KnowledgeReadContext`; `snapshot_of_context`; `read_context_digest` | mcp/src/agents_remember/models/knowledge/read.py:216-263; mcp/src/agents_remember/models/knowledge/read.py:540-560 |
| The seed digest and the seed union the request carries. | `facet_seed_digest`; `FacetReadSeed` | mcp/src/agents_remember/models/knowledge/facet_read.py:188-191; mcp/src/agents_remember/models/knowledge/facet_read.py:182-185 |
| The refusal helpers this seam reports through, including the absence the read owns. | `selector_absent_refusal`; `selection_incomplete_refusal`; `snapshot_unavailable_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:35-63; mcp/src/agents_remember/memory/knowledge/read_refusals.py:169-186; mcp/src/agents_remember/memory/knowledge/read_refusals.py:142-168 |
| The read-only open this seam is built on, and the refusal an absent path earns. | `open_read_only_database`; `selected_input_unavailable_refusal` | mcp/src/agents_remember/memory/knowledge/connection.py:52-65; mcp/src/agents_remember/memory/knowledge/refusals.py:882-902 |
| **The cases that hold the seam's own boundaries: its own-policy page, the byte-identical shipped page, and the incompleteness refusal.** | "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy"; "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" | mcp/tests/test_knowledge_facets.py:1053-1068; mcp/tests/test_knowledge_facets.py:1104-1119; mcp/tests/test_knowledge_facets.py:1068-1068 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T00:25+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): created this one-to-one card for the route's sixth composition seam. It records the read-only handle as the structural reason "a refused facet read persisted nothing" holds, the **three** snapshot comparisons (namespace, schema generation, logical dataset) that run before any selection, the **absence-versus-emptiness** split where a recorded facet record with no attachments is served as a real page rather than reported as `selector_absent`, the complete-or-refused selection with no cursor, the one operation name every refusal carries, the shared `KnowledgeReadContext` and shipped digest helpers rather than second definitions, and the non-overlap with `KS-R07@v1`'s selection that makes a shipped seed's page byte-identical. It also records, as a position rather than a defect claim, that the module docstring counts itself the **fifth** seam while naming five predecessors. Verification metadata stays at the last real commit: the code commit does not exist yet and closeout owns that stamp.
