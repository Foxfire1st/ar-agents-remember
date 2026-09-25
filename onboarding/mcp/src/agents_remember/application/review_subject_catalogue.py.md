# mcp/src/agents_remember/application/review_subject_catalogue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_subject_catalogue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T14:35:00+02:00 |
| lastVerifiedCommitHash | `d9e7e6e79ce532d16c689435ae95a63aab430f94` |
| lastVerifiedCommitDate | 2026-09-25T22:40:41+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The Intent Reviewer's subject catalogue (`ICR-R09@v1`): every invariant and family identity the
comparison's before/after pair records, listed with its label and its per-row presence, and **no
subject compared to earn its row**. This module owns the entry half's enumeration, which
[`application/knowledge_review.py`](knowledge_review.py.md) delegates to; the adapter resolves the
candidate, calls `read_subject_catalogue`, fills the labelled totals and assembles — it grows no
enumeration logic of its own. The module is the seam the over-limit adapter's packet
(`ICR-R09@v1` Scope) asked for: the touched responsibility (entry enumeration) moved out of
`knowledge_review.py` (841 → 757 lines) into a purpose-named owner before behavior was added, and
the old per-subject compare-to-earn-a-row mechanism it replaces was private to the adapter, so the
move leaves no alias and no second implementation.

**Why the union is the catalogue and not the comparison.** The old mechanism listed a subject only
when the shipped comparison answered for it — which silently dropped a retired (before-only)
subject entirely and made the list a by-product of per-subject comparisons, so displaying task
source waited on comparing every historical subject first. That was the verified F06 defect this
packet owns: "the API returns multiple entries but only the first is reachable" is its entry-half
shape. The catalogue inverts the source of truth: the two snapshots' **own identity tables** are
the population, read through the store's own `list_invariants`/`list_families` operations (not a
query written here), and the union is offered whatever the comparison would answer. Listing an
identity never runs `diff_knowledge_scope` for it; what one subject's review renders is still the
comparison's own answer when that subject alone is opened.

**Append-only honesty.** The knowledge history is append-only, so a subject the before snapshot
records and the candidate does not is neither gone nor unreviewable: it is `before_only`, keeps
its before snapshot's own recorded label, and opens one-sided (present/absent) exactly as the
`ICR-R06@v1` statement-side contract already renders a removal. Nothing is deleted from history
to shrink the claimed population, and no row is dropped for being unselectable: a recorded but
unselectable subject (e.g. an announced identity with no authored content) opens to the
comparison's own typed refusal, which names the subject and its reason, while the other subjects
and the task-context source review stay accessible.

## Code Commentary

### Logic

**`read_subject_catalogue` is the one entry point, and it reads both sides under one namespace.**
The namespace is read once through `review_namespace` (the resolution module's), which takes it from
the record standing beside each dataset — the candidate's admission receipt when there is one,
otherwise the before half's own `baseline-generation.json` — and both the before and the after store
are opened under it, so one catalogue read cannot offer its subjects under two different namespaces:
the recorded one is what the catalogue and the review an entry opens both use. Each side is read
through `_side_identities` and closed before returning (one `open_existing_knowledge_store` per side,
each in its own `try/finally`), and the two identity tuples are merged by `_union`.

**`_side_identities` reads each snapshot through the store's own two list operations.** The
identities offered are the ones the namespace records and not the ones a second reader of the same
tables believes it finds. Each recorded identity travels as `(kind, id, label)` with the label
carried beside the side it was read from, so the union can prefer the live side's wording without
mixing two snapshots' spellings into one string.

**`_union` is kind-grouped globally, whatever each snapshot holds.** The outer loop is the subject
kind — both sides' invariants first, then both sides' families — so the catalogue's
"invariants before families" guarantee holds **including retired rows**: a retired invariant sorts
with the invariants rather than after the live families. Within a kind the candidate side orders
first (it is the live side a reader extends) and the before side's retired rows follow in the
before snapshot's own order. The after side's label wins when both sides record the identity,
because the candidate is the side a reader acts on; a retired subject keeps its before snapshot's
own wording rather than receiving a label nothing recorded. This kind-grouping was the F1 finding
of this leaf's verification round — the first cut emitted after-side rows then before-side rows,
which interleaved retired invariants after live families — and it is now pinned by a test with
retired invariants in the fixture (`test_the_catalogue_stays_kind_grouped_when_retired_subjects_exist`).

**`_after_kind_rows` / `_before_only_kind_rows` state presence per row.** A candidate row is
`both` when the before side records the same `(kind, id)` key and `after_only` otherwise; a
before-side row is listed only when the candidate does not record it, and is always
`before_only`. Presence is the catalogue's selection state — which snapshot selections reach the
row — and it is the vocabulary the dashboard picker renders to mark retired rows.

### Conventions

The module imports the shipped vocabulary and resolution names and re-declares nothing:
`ReviewCandidateResolution`/`review_namespace` come from
[`application/review_candidate_resolution.py`](review_candidate_resolution.py.md), the store opener
from `memory/knowledge/store.py`, and `ReviewEntry`/`ReviewSubjectKind` from
[`models/knowledge/review.py`](../models/knowledge/review.py.md). `__all__` publishes exactly one
name — `read_subject_catalogue` — and the adapter imports it for use, not for re-export: the
per-subject helpers it replaces (`_reviewable_entries`, `_recorded_identities`,
`_selected_item_count`) were private to the adapter, so no importer had to learn a new home and no
alias is left. The private type `_RecordedIdentity` travels as one tuple so a label cannot be
separated from the side it was read from. No diff import exists in the module (verified by the
served route's tripwire case) and the module writes nothing: it opens both stores read-only and
closes them before returning.

### Invariants And Boundaries

- **The population is the union of the two snapshots' own identity tables, and nothing else.** No
  HEAD/current-knowledge fallback, no browser-supplied candidate, no ranking, no filter: a recorded
  identity is listed, and an identity neither snapshot records is not.
- **Listing never compares.** The module has no diff import; the served route is tripwired so both
  `diff_knowledge_scope` bindings fail the case if the catalogue read reaches the comparison —
  bounded catalogue loading at two measured population sizes (`diff_calls=0` at 12 and 87 rows).
- **No silent drops.** Every recorded identity is listed with its presence; an unselectable
  subject's reason is carried by the review's own typed refusal when it is opened, not by shrinking
  the catalogue.
- **Kind-grouped globally, retired rows included.** Invariants (live then retired) precede
  families; the guarantee is stated in the docstrings and pinned by a test.
- **One namespace, read from the candidate's own receipt.** Both sides are listed under the
  recorded namespace, so the catalogue and the review an entry opens cannot disagree about which
  datasets are compared.
- **Zero subjects is an empty catalogue, not an invitation.** The empty union is a valid `entries`
  result with zero totals beside the measured source inventory; the task-context review stays
  reachable beside it.
- **Boundaries.** Catalogue paging/cursors are R10's (the totals validator deliberately uses `>=`
  so a page stays valid); cockpit/browser/keyboard journeys over the picker are R24's; relationship
  traversal over the now-complete family population is R08's; typed-contract labels are R26's.
  The family rows are listed statement-free — families have no statement side to require — and an
  opened family states its sides as unresolved with their reasons through the reused
  `ICR-R06@v1` `side_content`, not a reimplementation.

### Todos

None recorded. The R08/R09 routed debt (a family subject's `unresolved` statement side and its
reason-carrying) is recorded as a boundary above and lives on the review's refusal/statement
machinery, not on this module.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and
four functions, the resolution and store operations it reads through, the model vocabulary it fills,
the adapter that delegates to it, and the ten-case module that measures it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the contract: both snapshots, no comparison, no silent drops, zero subjects an empty catalogue.** | `read_subject_catalogue` | mcp/src/agents_remember/application/review_subject_catalogue.py:1-22; mcp/src/agents_remember/application/review_subject_catalogue.py:47-69 |
| The published surface: one name. | `__all__` | mcp/src/agents_remember/application/review_subject_catalogue.py:39-39 |
| The one entry point: both stores opened under the record-beside-the-bytes namespace, each read and closed, then merged. | `read_subject_catalogue`; `review_namespace`; `open_existing_knowledge_store` | mcp/src/agents_remember/application/review_subject_catalogue.py:47-69; mcp/src/agents_remember/application/review_candidate_resolution.py:351-399; mcp/src/agents_remember/memory/knowledge/store.py:181-197 |
| The per-side read through the store's own two list operations, with each label travelling beside its side. | `_side_identities`; `list_invariants`; `list_families` | mcp/src/agents_remember/application/review_subject_catalogue.py:72-87; mcp/src/agents_remember/memory/knowledge/store.py:181-197; mcp/src/agents_remember/memory/knowledge/store.py:199-214 |
| **The globally kind-grouped union: the outer loop is the subject kind, the after label wins on overlap, and retired rows keep the before snapshot's own wording.** | `_union` | mcp/src/agents_remember/application/review_subject_catalogue.py:90-112 |
| The candidate's rows of one kind with the presence both snapshots give them, and the baseline's retired rows of one kind in the before snapshot's own order. | `_after_kind_rows`; `_before_only_kind_rows` | mcp/src/agents_remember/application/review_subject_catalogue.py:115-131; mcp/src/agents_remember/application/review_subject_catalogue.py:134-150 |
| The vocabulary the rows fill: presence per entry and the entry list's labelled totals with their agreement validators. | `ReviewEntry`; `ReviewSubjectPresence`; `ReviewEntryListResult` | mcp/src/agents_remember/models/knowledge/review.py:196-1164; mcp/src/agents_remember/models/knowledge/review.py:99-99; mcp/src/agents_remember/models/knowledge/review.py:73-73 |
| The adapter that delegates: the entry half resolves, calls this module, fills the totals and assembles — no enumeration logic of its own. | `list_knowledge_review_entries` | mcp/src/agents_remember/application/knowledge_review.py:199-276 |
| **The ten cases that measure the catalogue: the union, the kind grouping with retired subjects, the retired and added rows, the statement-free family, the whole-row traversal, the unselectable subject's reason, the totals, the zero-subject boundary, and the no-comparison tripwire.** | `test_the_catalogue_unions_both_snapshots_with_labels_and_presence`; `test_the_catalogue_stays_kind_grouped_when_retired_subjects_exist`; `test_a_retired_before_only_subject_stays_listed_and_reviewable`; `test_a_newly_added_after_only_subject_is_listed_beside_the_retired_half`; `test_a_family_subject_is_listed_without_an_establishable_statement_side`; `test_every_catalogue_row_opens_through_the_normal_review`; `test_a_recorded_but_unselectable_subject_is_listed_and_its_open_carries_the_reason`; `test_the_entry_route_carries_labelled_totals_for_the_whole_catalogue`; `test_zero_subjects_is_a_valid_catalogue_beside_the_source_inventory`; `test_catalogue_loading_runs_no_comparison` | mcp/tests/test_review_subject_catalogue.py:232-250; mcp/tests/test_review_subject_catalogue.py:252-283; mcp/tests/test_review_subject_catalogue.py:285-309; mcp/tests/test_review_subject_catalogue.py:311-332; mcp/tests/test_review_subject_catalogue.py:334-358; mcp/tests/test_review_subject_catalogue.py:360-386; mcp/tests/test_review_subject_catalogue.py:388-430; mcp/tests/test_review_subject_catalogue.py:432-459; mcp/tests/test_review_subject_catalogue.py:461-509; mcp/tests/test_review_subject_catalogue.py:511-545 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The catalogue reads the two datasets the
server resolved and names one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T14:35:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`): **created.** The module is new in this leaf and this is its one-to-one card. It records the catalogue contract the packet (`ICR-R09@v1`) states: the union of both snapshots' own identity tables as the population, per-row presence (`before_only`/`after_only`/`both`) as the selection state, labelled totals on the entry list, no comparison run to earn a row, no silent drops, and zero subjects as a valid catalogue beside the task-context source review. It also records the seam: the entry enumeration moved out of the over-limit `knowledge_review.py` adapter (841 → 757 lines) before behavior was added, the replaced per-subject compare-to-earn-a-row helpers were private to the adapter so no alias is left, and the fix-round F1 ordering correction (globally kind-grouped rows, retired invariants still inside the invariant group) is stated in the docstrings and pinned by a test. **Stamp accounting:** the verification pair names this leaf's base — the production line `f141d164265e926be9249acf6ae680ccf9ffae61`, the last real commit the reading was taken against — because the module exists only in this leaf's uncommitted candidate; what was actually read is this leaf's uncommitted working tree. Closeout owns the stamp once the code commit exists.
