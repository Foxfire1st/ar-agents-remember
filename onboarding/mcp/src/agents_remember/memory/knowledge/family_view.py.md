# mcp/src/agents_remember/memory/knowledge/family_view.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/family_view.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:16+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be`|
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The **Family projection**: what one family revision's recorded composition, owning route and
explanatory context *are*, reported from the canonical rows.

**It reports and never traverses.** The projection has no reached set, follows no edge, and fills no
gap. A missing composition link, a missing owning route and a missing explanatory context are all
reported as **absent**; nothing here infers a relationship from a display label, a folder or path
ancestry, a prefix, a symbol, a shared member, a shared anchor or a prose sentence. A revision whose
members all live under one route's path and which records no owning route is reported
**ungoverned**, not governed by that route.

## Code Commentary

### Logic

- `family_revision_view` — the one entry point. It reads the stored links, the recorded owning route
  (or the explicit ungoverned state) and the authored context, and returns them with their
  provenance.
- `FamilyRevisionView` — the value. Each link carries its **direction** and the **policy version it
  was declared under**, because a link reported without that version would be unreadable against
  another version of the same policy.
- The three reads it uses are the projection's own lookups in `read_queries.py`
  (`fetch_composition_rows`, `fetch_owning_routes_for_revisions`, `fetch_contexts_for_revisions`),
  ordered through the order-column registrations that module declares. The projection holds no
  statement of its own.

### Conventions

- **Derived output, not a second authority.** The view is regenerable at will from the canonical rows
  and writes nothing; every statement it runs is a `SELECT` on the caller's connection. Reading it
  twice changes nothing.
- **Only stored facts, and absences are stated.** There is no computed set of "related families"
  presented as a recorded relationship.
- The one value that could be mistaken for a traversal's result — the declared depth bound — travels
  as *the policy's declared bound*, labelled as a declaration, beside the links it declares.

### Invariants And Boundaries

- **The projection does not traverse.** It carries no reachable set and it never imports
  `composition_traversal.py`; a case asserts both.
- **The composition table is deliberately not consulted for selection anywhere.** The selected set,
  the counts, the ordering, the revision groups, the advertised frontier and the manifest digest are
  unchanged by this leaf, and the retrieval read does not import this module.
- **The projection is not an authority.** It decides no relationship, mints no identity and records
  no status; it presents what is stored.
- **Boundary.** Reading the stored rows is `compositions.py`; walking declared edges under a policy is
  `composition_traversal.py`. This module only presents.

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
| **The one projection entry point, which reports the stored links, the route or the explicit ungoverned state, and the recorded context.** | `family_revision_view` | mcp/src/agents_remember/memory/knowledge/family_view.py:107-107 |
| The projection's value, whose links carry their direction and the policy version they were declared under. | `FamilyRevisionView` | mcp/src/agents_remember/memory/knowledge/family_view.py:83-106 |
| The ungoverned state's own read, which never fills the gap. | `owning_route_of_family_revision` | mcp/src/agents_remember/memory/knowledge/compositions.py:392-392 |
| **The case that drives the projection through the read-only application seam and asserts the recorded link is reported with its policy version.** | "test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection" | mcp/tests/test_knowledge_family_composition_boundaries.py:617-617 |
| **The same case's second half: a family revision this namespace does not hold is a typed refusal, and the file is byte-identical afterwards.** | "test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection" | mcp/tests/test_knowledge_family_composition_boundaries.py:617-617 |
| **The case that proves a composition graph leaves the shipped selection exactly as it was.** | "test_a_composition_graph_leaves_the_shipped_selection_exactly_as_it_was" | mcp/tests/test_knowledge_family_composition_boundaries.py:219-219 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-18T10:05+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read the `FamilyRevisionView` claim against the declaration and regenerated its range from the declaration's own extent.** The row cited `:83-83`, the `class` line alone; the declaration runs `:83-106` — through the fields whose links carry their direction and the policy version they were declared under — and that is the extent the claim's words describe. Wording retained unchanged: it was already true of the construct. This row is one of the three the check keeps reopened, and it stays reopened for a reason no edit can remove: **`FamilyRevisionView` did not exist at `15fe8678` and resolves only in this candidate**, because this leaf created the module. Until closeout stamps a code commit that contains the module, the only revision the checker can compare against necessarily lacks the construct; the working candidate is recorded in `reviewedWorkingCandidate` for exactly that reason. Recorded here so the residual is named rather than hidden.

- 2026-09-18T06:16+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the Family projection. It records the content sentence this leaf's remit fixes: **the projection reports and never traverses** — a missing link, route or context is reported as absent, the ungoverned state is explicit, and no relationship is inferred from a label, a path, a prefix, a shared member or prose. It records that a reported link carries the policy version it was declared under, that the view is derived output rather than a second authority, and that the composition table is not consulted for selection anywhere. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp. **This card also records the claim's own re-read:** the `FamilyRevisionView` claim was verified against the declaration on this candidate — the construct did not exist at the base commit, because this leaf created it — so the claim's evidence is the working tree rather than a reopened range, and the verification stamp stays closeout-owned.
