# mcp/src/agents_remember/application/knowledge_composition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_composition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:20+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be`|
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The fifth read-only application seam**, beside `knowledge_read`, `knowledge_snapshot`,
`knowledge_merge` and `knowledge_export`. It admits a dataset path and a repository namespace, opens
the database **read-only**, and delegates to the two memory modules that own the acts:

- `follow_family_composition` — the declared-policy traversal, under one declared policy version,
  bounded by that version's declared depth bound;
- `family_view` — the Family projection, which reports the recorded links, the canonical owning route
  or the explicit ungoverned state, and the authored explanatory context.

**The traversal is a read, not a write, and it is not the retrieval read.** Following composition
edges is a different operation from `read_knowledge_scope`: this seam does not touch that function,
its selection policy or its advertised frontier. A caller that wants the recorded-scope selection
asks for that operation; a caller that wants declared composition edges followed asks for this one.

## Code Commentary

### Logic

- `follow_family_composition` — resolves the policy version, walks the declared edges and returns a
  `CompositionTraversalResult`. A traversal that cannot be reported as a **complete** scope — an
  unknown policy, a not-permitted edge, a step past the declared bound — returns the refusal rather
  than a truncated scope, because a truncated traversal reported as a scope would be a false
  statement about what was reached.
- `family_view` — returns a `FamilyViewResult` whose state is `reported` or `refused`. A family
  revision this namespace does not hold is **refused rather than reported empty**: an empty report
  would be indistinguishable from a revision that genuinely records nothing.
- `open_read_only_store` — the one open path. The connection is the shipped
  `open_read_only_database` handle, whose strongest available statement is a `SELECT`, and the schema
  is validated against the generation **the file declares**, exactly as every other open path does.
- `_as_refusal` — converts a modelled `KnowledgeRefused` into its typed refusal and lets anything
  else propagate, so a defect is never reported as an expected state.

### Conventions

- Every function opens through `open_read_only_store` inside a `with` block, so no read leaves a
  connection open and no caller can reach a writable handle by accident.
- **Every modelled failure is a typed refusal, not an exception**: an unknown policy identity or
  version, a not-permitted edge, a step past the declared bound and a family revision this namespace
  does not hold are all returned as `KnowledgeRefusal` values inside the result.
- `__all__` publishes the two operations and their two value types; nothing else in the module is
  part of the seam's surface.

### Invariants And Boundaries

- **Read-only, so a refusal persists nothing.** "A refused traversal changed nothing" is a property
  of the handle rather than a rollback this code remembers, and the boundary case asserts the file's
  bytes are identical before and after a refusal.
- **Two axes stay separate.** Axis A is the retrieval selection; axis B is the registered review
  scope. Conflating them is the defect this seam exists to prevent, and the case states the boundary
  as one measurement: running the traversal moves nothing about what the retrieval read selects.
- **The seam owns no semantics.** It carries values; the traversal and the projection own the rules.
- **Boundary.** Writing an edge, a policy, a route or a context is the candidate batch's path through
  `memory/knowledge/compositions.py`; this module is read-only and has no write path at all.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The read-only open path, whose handle is the shipped `open_read_only_database` connection and whose schema is the one the file declares.** | `open_read_only_store` | mcp/src/agents_remember/application/knowledge_composition.py:136-136 |
| **The traversal seam: it carries `follow_family_composition` as its own operation and returns a refusal rather than a truncated scope.** | `follow_family_composition` | mcp/src/agents_remember/application/knowledge_composition.py:83-83 |
| **The projection seam: a family revision this namespace does not hold is refused, not reported empty.** | `family_view` | mcp/src/agents_remember/application/knowledge_composition.py:115-115 |
| The traversal result type carrying the state, the seed and the refusal or the scope. | `CompositionTraversalResult` | mcp/src/agents_remember/application/knowledge_composition.py:60-72 |
| The published seam surface: two operations and their two value types. | `__all__` | mcp/src/agents_remember/application/knowledge_composition.py:49-49 |
| **The case that asserts the seam is read-only, carries its own operation, and moves no selection.** | "test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection" | mcp/tests/test_knowledge_family_composition_boundaries.py:617-617 |
| The case that proves the shipped read never consults the composition table, which is the other half of the axis separation. | "test_no_shipped_read_path_consults_the_composition_table" | mcp/tests/test_knowledge_family_composition_boundaries.py:252-252 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-18T10:05+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read the `CompositionTraversalResult` claim against the declaration and regenerated its range from the declaration's own extent.** The row cited `:60-60`, the `class` line alone; the declaration runs `:60-72` — `class CompositionTraversalResult:` through the fields it carries (the state, the seed, and the refusal or the scope) up to the next top-level statement — and that is the extent the claim's words describe. The claim's wording is retained unchanged: it was already true of the construct, and the range now shows the whole of what it names. This row is one of the three the check keeps reopened, and it stays reopened for a reason no edit can remove: **`CompositionTraversalResult` did not exist at `15fe8678` and resolves only in this candidate**, because this leaf created the module. Until closeout stamps a code commit that contains the module, the only revision the checker can compare against necessarily lacks the construct; the working candidate is recorded in `reviewedWorkingCandidate` for exactly that reason. Recorded here so the residual is named rather than hidden.

- 2026-09-18T06:20+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the fifth read-only application seam. It records the sentence this leaf's remit fixes: **`follow_family_composition` is a read operation, not a write** — the traversal follows declared composition edges under a declared policy version and touches no retrieval selection, so a card that reads composition edges as followed *as part of the retrieval selection* is false. It records that the handle is read-only (so a refusal persists nothing and "changed nothing" is a property of the handle), that a missing family revision is refused rather than reported empty, that every modelled failure is a typed refusal rather than an exception, and that the seam owns no semantics. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp. **This card also records the claim's own re-read:** the `CompositionTraversalResult` claim was verified against the declaration on this candidate — the construct did not exist at the base commit, because this leaf created it — so the claim's evidence is the working tree rather than a reopened range, and the verification stamp stays closeout-owned.
