# mcp/tests/test_review_subject_catalogue.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Pins the union, presence, totals, bounded loading and reviewability of a complete subject catalogue.

## Code Commentary

The shared diff fixture is copied and extended for retired, added and bare identities. RowStore and revision constructors come from test-only knowledge_rows_test_support; `_insert_bare_identity` inserts fixture identity rows. It is not a shipped batch insert_invariant_identity operation or proof of production append-only admission.

Production catalogue/entry/review composition checks kind grouping including before-only identities, one-sided statements, family listing without a statement side, every offered row's reviewability and a reason-carrying refusal for an unselectable bare identity. Neighbour reviews remain accessible. Entry totals describe the whole catalogue, an empty catalogue coexists with a measured source inventory, and bounded loading is protected by comparison bindings patched to raise. Browser traversal and relationship/roster paging belong to their separate owners.

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

### Invariants And Boundaries

- **The catalogue's honesty is presence + totals + zero drops**; reason-carrying for an
  unopenable subject lives on the review's own typed refusal (the reused R16 machinery), and the
  case asserts exactly that split.
- **Boundary.** Browser keyboard/focus traversal over the picker and the cockpit takeover are
  R24's; catalogue paging/cursors are R10's; relationship traversal over the complete family
  population is R08's; typed-contract labels are R26's.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_the_catalogue_stays_kind_grouped_when_retired_subjects_exist` supplies the current fixture or assertion described above. [10]
- `test_every_catalogue_row_opens_through_the_normal_review` supplies the current fixture or assertion described above. [11]
- `test_a_recorded_but_unselectable_subject_is_listed_and_its_open_carries_the_reason` supplies the current fixture or assertion described above. [12]
- `test_zero_subjects_is_a_valid_catalogue_beside_the_source_inventory` supplies the current fixture or assertion described above. [13]
- `test_catalogue_loading_runs_no_comparison` supplies the current fixture or assertion described above. [14]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [15]
- RowStore inserts index-shaped fixture rows without the retired production admission plane. [16]

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring, the
shared-fixture population helpers, the route config helpers, and the ten cases.

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is configured for this file.

No relevant domain documentation was found.

- The shared fixture and the population helpers that extend it through test-only constructors (`mcp/tests/test_review_subject_catalogue.py:28-33` fixture imports; `_author_extra_invariant` at 78 and `_insert_bare_identity` at 117); no shipped store operations author populations.
- **The union with labels and presence, and the fix-round F1 pin that the rows stay globally kind-grouped when retired subjects exist.** [18]
- **The retired and added rows: a before-only subject stays listed and opens one-sided; an after-only subject is listed beside the retired half.** [19]
- The statement-free family listing and the packet's conforming example: every row opens through the normal review. [20]
- **The failure/recovery boundary: a recorded but unselectable subject is listed and its open carries the comparison's own reason.** [21]
- The labelled totals on the served entry result, and the zero-subject boundary beside the measured source inventory. [22]
- **The bounded-loading tripwire: both diff bindings rigged, the route answers with the whole catalogue, so loading never compared.** [23]

### Cross-Repo References

No cross-repository behavior is exercised in this file.

No applicable cross-repository source was found.
