# mcp/tests/test_review_subject_catalogue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_subject_catalogue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T14:38:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61` (this leaf's base, confirmed from the enclosure contract) — the module is new and exists only in the uncommitted candidate |
| lastVerifiedCommitHash | `02957762709c9b515b4ff57f7f13524a7c0dfb8d` |
| lastVerifiedCommitDate | 2026-09-22T16:02:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The complete subject catalogue's case module (`ICR-R09@v1`): **the union, the presence, the
totals, the bounded loading, and the traversal**. Every case drives the production composition —
the catalogue read behind the entries route and the review composition behind the intent route —
over real two-snapshot populations built through the shipped store operations. Nothing here
hand-writes a payload the composition then claims to have produced.

The module docstring states the population rule the cases enforce: populations that differ from
the shared diff fixture are **copies of its datasets extended through the shipped store
operations** — `create_invariant`/`create_revision` for a retired or newly added subject,
`insert_invariant_identity` (a shipped batch operation) for a recorded identity with no authored
content. The bare-identity case is therefore legitimate append-only state (announced but
unauthored), not a corrupt database.

## Code Commentary

### Logic

**The fixture is the shared diff fixture, copied and extended per population.** `fixture` builds
the shared two-snapshot topology through `diff_scope_test_support.build_diff_fixture`; the copy
helpers (`_copy_database`, `_author_extra_invariant`, `_insert_bare_identity`) derive the leaf's
own populations from it rather than introducing a second topology — which is also why this module
is registered as a source-derived consumer of the two exact-scope support rows in
`mcp/tests/evidence-lifecycle.toml` (the Seventeenth deliberate re-pin).

**Ten cases, one distinct user operation each:**

- `test_the_catalogue_unions_both_snapshots_with_labels_and_presence` — the catalogue is the union
  of both snapshots' identity tables with per-row presence, not the candidate side alone.
- `test_the_catalogue_stays_kind_grouped_when_retired_subjects_exist` — the fix-round F1 pin: on a
  fixture **with retired invariants**, the rows are globally kind-grouped (every invariant,
  including the retired one, before every family), and the retired invariant sits after the live
  invariant rather than after the families.
- `test_a_retired_before_only_subject_stays_listed_and_reviewable` — a `before_only` subject is
  listed and opens one-sided (`before_side=present`, `after_side=absent`), which is the
  append-only model the packet requires.
- `test_a_newly_added_after_only_subject_is_listed_beside_the_retired_half` — an `after_only`
  subject is listed beside the retired half rather than replacing it.
- `test_a_family_subject_is_listed_without_an_establishable_statement_side` — a family is listed
  statement-free (families have no statement side to require).
- `test_every_catalogue_row_opens_through_the_normal_review` — the packet's conforming example:
  **every** row opens through the normal task review, which falsifies the "only the first is
  reachable" defect the packet owns.
- `test_a_recorded_but_unselectable_subject_is_listed_and_its_open_carries_the_reason` — the
  failure/recovery boundary: the bare identity stays listed, its open carries the comparison's own
  typed refusal (`comparison_refused` / `selector_absent`) with the reason and next action, and the
  neighbour reviews stay accessible.
- `test_the_entry_route_carries_labelled_totals_for_the_whole_catalogue` — the served entry result
  carries `total_subjects`/`invariant_total`/`family_total` describing the whole catalogue.
- `test_zero_subjects_is_a_valid_catalogue_beside_the_source_inventory` — the packet's boundary:
  an empty catalogue is a valid `entries` result beside a **measured** source inventory, and the
  task-context review stays reachable.
- `test_catalogue_loading_runs_no_comparison` — bounded loading: both `diff_knowledge_scope`
  bindings are monkeypatched to raise, so the entries route answering with the whole catalogue
  proves the read never entered the shipped comparison.

**The route-level cases drive the real adapter through `_entry_route_config`/`_place_pair`** — the
candidate resolution's own config shape with the pair's bytes placed where the resolution derives
them — so the entries route is measured as it is served, not through a direct call to the catalogue
only.

### Conventions

One behavior boundary per module per the test-split rule: this module owns the catalogue's
user-visible behavior and the entries route that serves it; the review composition's one-sided and
revision-selection behavior stays in `test_knowledge_review_one_sided_statements.py` /
`test_knowledge_review_revision_selection.py`, and the dashboard picker's traversal is a vitest
case in `changeSetBar.test.tsx`. Imports go through the public adapter surface
(`list_knowledge_review_entries`, `compose_review`, `resolve_review_candidate`) plus the catalogue
owner's `read_subject_catalogue`; the two support imports (`diff_scope_test_support`,
`read_scope_test_support`) are the exact-scope consumers the evidence lifecycle registers.

### Invariants And Boundaries

- **No case trusts a constructed payload.** Populations are built through the shipped store
  operations and served results are read back through the production composition.
- **The catalogue's honesty is presence + totals + zero drops**; reason-carrying for an
  unopenable subject lives on the review's own typed refusal (the reused R16 machinery), and the
  case asserts exactly that split.
- **Boundary.** Browser keyboard/focus traversal over the picker and the cockpit takeover are
  R24's; catalogue paging/cursors are R10's; relationship traversal over the complete family
  population is R08's; typed-contract labels are R26's.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
shared-fixture population helpers, the route config helpers, and the ten cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it measures and how its populations are built. | `create_invariant`; `create_revision` | mcp/tests/test_review_subject_catalogue.py:1-7 |
| The shared fixture and the population helpers that extend it through shipped store operations. | `fixture`; `resolution_for`; `_copy_database`; `_author_extra_invariant`; `_insert_bare_identity` | mcp/tests/test_review_subject_catalogue.py:47-58; mcp/tests/test_review_subject_catalogue.py:54-69; mcp/tests/test_review_subject_catalogue.py:71-77; mcp/tests/test_review_subject_catalogue.py:79-116; mcp/tests/test_review_subject_catalogue.py:118-133 |
| The route-level helpers that drive the entries route as it is served. | `_entry_route_config`; `_place_pair`; `ENTRY_MASTER`; `ENTRY_LEAF` | mcp/tests/test_review_subject_catalogue.py:155-217; mcp/tests/test_review_subject_catalogue.py:219-230; mcp/tests/test_review_subject_catalogue.py:151-152 |
| **The union with labels and presence, and the fix-round F1 pin that the rows stay globally kind-grouped when retired subjects exist.** | `test_the_catalogue_unions_both_snapshots_with_labels_and_presence`; `test_the_catalogue_stays_kind_grouped_when_retired_subjects_exist` | mcp/tests/test_review_subject_catalogue.py:232-250; mcp/tests/test_review_subject_catalogue.py:252-283 |
| **The retired and added rows: a before-only subject stays listed and opens one-sided; an after-only subject is listed beside the retired half.** | `test_a_retired_before_only_subject_stays_listed_and_reviewable`; `test_a_newly_added_after_only_subject_is_listed_beside_the_retired_half` | mcp/tests/test_review_subject_catalogue.py:285-309; mcp/tests/test_review_subject_catalogue.py:311-332 |
| The statement-free family listing and the packet's conforming example: every row opens through the normal review. | `test_a_family_subject_is_listed_without_an_establishable_statement_side`; `test_every_catalogue_row_opens_through_the_normal_review` | mcp/tests/test_review_subject_catalogue.py:334-358; mcp/tests/test_review_subject_catalogue.py:360-386 |
| **The failure/recovery boundary: a recorded but unselectable subject is listed and its open carries the comparison's own reason.** | `test_a_recorded_but_unselectable_subject_is_listed_and_its_open_carries_the_reason` | mcp/tests/test_review_subject_catalogue.py:388-430 |
| The labelled totals on the served entry result, and the zero-subject boundary beside the measured source inventory. | `test_the_entry_route_carries_labelled_totals_for_the_whole_catalogue`; `test_zero_subjects_is_a_valid_catalogue_beside_the_source_inventory` | mcp/tests/test_review_subject_catalogue.py:432-459; mcp/tests/test_review_subject_catalogue.py:461-509 |
| **The bounded-loading tripwire: both diff bindings rigged, the route answers with the whole catalogue, so loading never compared.** | `test_catalogue_loading_runs_no_comparison`; `monkeypatch.setattr` | mcp/tests/test_review_subject_catalogue.py:511-545; mcp/tests/test_review_subject_catalogue.py:525-533 |

## Cross-Repo References

No cross-repository behavior is exercised in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-22T14:38:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`): **created.** The module is new in this leaf and this is its one-to-one card. It records the ten-case catalogue suite: union with labels and presence, the fix-round F1 kind-grouping pin, the retired/added one-sided openings, the statement-free family, the whole-row traversal, the unselectable subject's carried reason, the labelled totals, the zero-subject boundary, and the no-comparison tripwire. It also records the module's evidence-lifecycle registration: as a source-derived consumer of the two exact-scope support rows (`diff_scope_test_support.py`, `read_scope_test_support.py`) in `mcp/tests/evidence-lifecycle.toml`, plus its own unit-regression lane row in `mcp/tests/test-evidence-lanes.toml`. **Stamp accounting:** the verification pair names this leaf's base — the production line `f141d164265e926be9249acf6ae680ccf9ffae61`, the last real commit the reading was taken against — because the module exists only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
