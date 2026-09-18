# mcp/src/agents_remember/memory/knowledge/composition_traversal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/composition_traversal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:14+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be`|
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The **read-side successor**: follow declared composition edges from one family revision under one
declared policy version, bounded by that version's declared depth bound, reporting the policy
identity and version it executed under.

**This is a different operation from the retrieval selection, not a flag on it.** The two live on
different axes:

- **Axis A** is the retrieval selection — what one snapshot read selects for a seed, its counts, its
  ordering, the revision groups it forms and the frontier it advertises. **This module does not touch
  it.** The shipped read does not consult the composition table at all, and a case in the boundary
  module asserts that no shipped read path does.
- **Axis B** is the registered review scope: declared edges followed under a versioned traversal
  policy. This module supplies the traversal semantics and the policy checks; the scope itself is
  built by a later leaf.

A card that describes composition edges as being followed **as part of the retrieval selection** is
false. Nothing here widens, reorders or reinterprets the selected set, and the selection policy is
unchanged by this leaf.

## Code Commentary

### Logic

- `follow_composition_scope` — the one traversal. It resolves the declared policy version first
  (through `composition_policies.require_declared_policy`, so an unknown identity and an unknown
  version are refused by name), then walks the declared edges in the declared direction up to the
  declared bound, and returns a `CompositionScope` carrying the reached set, the depth reached, and
  the policy identity and version.
- `TRAVERSAL_OPERATION` — the one operation name this module carries,
  `follow_family_composition`. It is **its own member of the operation vocabulary** because
  following declared edges under a versioned policy is not a retrieval selection; it is not a
  variant of `read_knowledge_scope`.
- `CompositionScope` — the value type. It reports what was reached under which declared policy
  version, so a result is never readable as one produced under another version.

**Four refusals are structural rather than incidental**, and each names the policy identity, its
version and the edge or bound it reached:

1. an **unknown policy identity or version** — never resolved to a default or to the only version
   stored;
2. a policy that **widens a scope this build does not register** — a policy may add scope to a
   *named* scope and nothing else;
3. an edge encountered under a policy that **does not permit following it** — an edge whose own
   declared policy is absent, of another identity, or of another version is not followable, and the
   traversal refuses rather than stepping around it silently;
4. a traversal that would **exceed its declared bound** — refused, never truncated, because a
   truncated traversal reported as a scope would be a false statement about what was reached.

### Conventions

- Widening is **monotone and additive by construction**: the walk only ever *adds* revisions to the
  reached set, in the declared direction, and it never removes, reorders or reinterprets anything a
  caller already held.
- Every modelled failure is a typed `KnowledgeRefusal` carrying the facts above; the caller reads a
  refusal rather than catching an exception.
- The module reads through `compositions` and `families` and never writes: it has no insert, no
  update and no delete.

### Invariants And Boundaries

- **One cycle rule, one walk.** This module contains no cycle check of its own. The composition
  graph is judged by the shipped shared lineage rule, fed by `lineages.composition_edges`; a case
  asserts that **no second cycle walk exists** beside it, and a second rule would make drift possible
  between three graphs instead of two.
- **The traversal is not the retrieval read, and it does not import it.** `family_view.py` never
  imports this module, and this module never touches the selection policy or the advertised frontier.
- **A refused traversal persists nothing.** The application seam opens the database read-only, so
  "a refusal changed nothing" is a fact about the handle rather than a rollback this code remembers.
- **Boundary.** This module follows edges; it does not decide which edges exist
  (`compositions.py`), what a policy is (`composition_policies.py`), or what the Family projection
  reports (`family_view.py`).

### Todos

None recorded. The registered-review-scope construction is a later leaf's; this module supplies the
traversal semantics that construction consumes.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one traversal: policy resolved first, then the bounded declared-direction walk.** | `follow_composition_scope` | mcp/src/agents_remember/memory/knowledge/composition_traversal.py:84-84 |
| **The traversal's own operation member, which is a different operation from the retrieval selection rather than a variant of it.** | `TRAVERSAL_OPERATION` | mcp/src/agents_remember/memory/knowledge/composition_traversal.py:60-60 |
| The result value carrying the reached set, the depth reached and the policy identity and version it executed under. | `CompositionScope` | mcp/src/agents_remember/memory/knowledge/composition_traversal.py:64-83 |
| The third edge source that feeds the shared cycle rule, so this module needs no walk of its own. | `composition_edges` | mcp/src/agents_remember/memory/knowledge/lineages.py:37-37 |
| **The case that proves no second cycle walk or recursive CTE exists beside the shared rule.** | "test_no_second_cycle_implementation_exists_beside_the_shared_rule" | mcp/tests/test_knowledge_family_composition.py:962-962 |
| **The case that proves a traversal under a declared policy reports its version and widens nothing else.** | "test_a_traversal_under_a_declared_policy_reports_its_version_and_widens_nothing_else" | mcp/tests/test_knowledge_family_composition_boundaries.py:288-288 |
| **The case that proves a traversal past its declared bound is refused, not truncated.** | "test_a_traversal_that_would_exceed_its_declared_bound_is_refused_not_truncated" | mcp/tests/test_knowledge_family_composition_boundaries.py:428-428 |
| **The case that proves the shipped read never consults the composition table.** | "test_no_shipped_read_path_consults_the_composition_table" | mcp/tests/test_knowledge_family_composition_boundaries.py:252-252 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-18T10:05+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read the `CompositionScope` claim against the declaration and regenerated its range from the declaration's own extent.** The row cited `:64-64`, the `class` line alone; the declaration runs `:64-83` — through the fields carrying the reached set, the depth reached and the policy identity and version it executed under — and that is the extent the claim's words describe. Wording retained unchanged: it was already true of the construct. This row is one of the three the check keeps reopened, and it stays reopened for a reason no edit can remove: **`CompositionScope` did not exist at `15fe8678` and resolves only in this candidate**, because this leaf created the module. Until closeout stamps a code commit that contains the module, the only revision the checker can compare against necessarily lacks the construct; the working candidate is recorded in `reviewedWorkingCandidate` for exactly that reason. Recorded here so the residual is named rather than hidden.
- 2026-09-18T08:30+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 1 generated projection bullet(s) by hand** — `CompositionScope`, `test_no_second_cycle_implementation_exists_beside_the_shared_rule`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.
- 2026-09-18T06:14+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the declared-policy traversal. It records the content sentence this leaf's remit singles out: the read-side successor is a **different operation** that does **not** touch the retrieval selection — a card that reads composition edges as followed *as part of the retrieval selection* is false — and a case asserts that **no second cycle walk exists** beside the shipped shared rule. It records the four structural refusals (unknown policy, unregistered widened scope, a not-permitted edge, an exceeded bound), that an exceeded bound is refused rather than truncated, and that widening is monotone and additive by construction. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp. **This card also records the claim's own re-read:** the `CompositionScope` claim was verified against the declaration on this candidate — the construct did not exist at the base commit, because this leaf created it — so the claim's evidence is the working tree rather than a reopened range, and the verification stamp stays closeout-owned.
