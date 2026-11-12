# mcp/tests/test_review_family_context.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Pins exact family guarantees, memberships and bounded roster continuation in review context.

## Code Commentary

Recorded family revisions supply their own guarantees and memberships; a successor roster is not inherited. Shared members retain canonical revision identity across contexts, and repeated memberships do not inflate the distinct source population. A member change exposes its family context without declaring a guarantee change or an intent verdict.

The suite distinguishes measured no-family, absent knowledge, no selected subject, one-sided families. The former ambiguous-lineage fixture is a removed historical case, not a measured population in this module. Roster truncation preserves owner counts and its continuation; tokens bind their exact walk, final pages carry only their share, and a multi-page walk terminates without loss. The client route assertions exercise the production adapter.

Family/revision/membership inputs are inserted by test-only knowledge_rows_test_support. Those fixtures do not enforce the former canonical family authoring plane. Current guarantees and roster meanings are read from exact supplied rows by the surviving production readers.

### Logic

The family-selection descriptions distinguish missing family records from missing membership of the selected invariant. The latter does not erase a family counterpart or restrict independent authored-head selection. This module’s executable tests are unchanged by L40; the new countercases and revised history expectation live in the population suite.

The multi-page walk assertions count unique `member_id` values across sparse context updates. A member may be represented on content, membership and claim pages, so summing projected rows would overcount a valid walk. The first page must expose remaining primary items; it need not lack a member already represented by content.

**The load-bearing properties, one case each.** The module's own docstring lists them (`:15-25`); the
table below maps each to the case that pins it and the operation the case drives.

| Case | Line | The property it pins |
| --- | --- | --- |
| `test_a_selected_invariant_resolves_both_recorded_families_with_their_own_guarantees` | `:284` | a selected invariant discovers its directly recorded family identities and resolves each independently on both snapshots, with its own selected authored head, guarantee and exact roster |
| `test_a_family_that_did_not_move_is_still_composed_at_its_own_revision` | `:321` | an unchanged family still yields a context at its own revision |
| `test_a_successor_family_revision_is_read_from_its_own_rows_not_inherited` | `:342` | a successor that drops a member does **not** inherit the parent's roster, and the dropped membership is still carried on the side that records it |
| `test_a_shared_member_is_one_canonical_revision_referenced_in_two_contexts` | `:384` | one invariant recorded under two families is one canonical revision referenced twice; the unique count does not grow with the repeated membership |
| `test_a_member_change_makes_its_family_context_available_and_concludes_nothing` | `:425` | a changed member makes its family context available and changes nothing about the guarantee |
| `test_a_selection_in_no_recorded_family_is_a_measured_zero` | `:455` | a selection in no recorded family is the measured zero, not an empty collection |
| `test_missing_knowledge_is_the_reviews_refusal_not_an_empty_family_context` | `:473` | missing knowledge is the review's own refusal, never an empty family context |
| `test_a_task_context_review_states_that_it_selected_no_subject` | `:487` | the task-context review states that it selected no subject |
| `test_a_family_only_the_candidate_records_is_a_one_sided_context_with_a_stated_absence` | `:501` | a family only the candidate records is a one-sided context with a stated absence |
| *Removed historical case:* `test_an_ambiguous_family_lineage_names_its_candidates_and_chooses_no_revision` | historical `:523` | the old multi-head fixture is absent from the current single-revision text population; no executable refusal witness is claimed |
| `test_a_truncated_roster_stays_partial_with_the_owners_counts_and_continuation` | `:593` | a truncated roster stays partial, carrying the owner's own counts and the cursor that reaches the rest |
| `test_the_published_cursor_continues_exactly_the_walk_that_minted_it` | `:631` | the published cursor continues exactly the walk that minted it |
| `test_a_cursor_that_binds_no_walk_is_refused_beside_the_first_pages` | `:676` | a cursor that binds no composed walk is refused while every composed walk's first page stays published |
| `test_naming_the_roster_collection_without_a_cursor_is_refused` | `:717` | naming the roster collection without a cursor earns the collection's own refusal |
| `test_a_token_that_is_not_a_roster_cursor_is_answered_with_the_owner_vocabulary` | `:739` | a token of another format is answered in the owner's own vocabulary |
| `test_the_complete_source_population_does_not_grow_with_a_repeated_membership` | `:760` | the complete source inventory and its unique counts do not grow with repeated memberships |
| `test_the_family_context_reaches_the_client_over_the_real_review_route` | `:878` | the composition reaches the client over the **real** review route, not a constructed payload |

**The reopen added the walk the delivered continuation control actually drives** (`:949-1133`), one case
per boundary of the corrected completion semantics — these are the bite-proofs for the fix and they
exercise the route rather than the value:

| Case | Line | The property it pins |
| --- | --- | --- |
| `test_a_roster_that_fits_one_page_is_carried_whole_and_says_so` | `:1045` | the single-page boundary: one walk page **is** the roster, it is `complete` with `state == "first_page"`, it publishes no cursor, it carries every recorded row, and its sentence says "all carried here" |
| `test_the_final_page_of_a_long_walk_may_carry_only_its_own_share` | `:1060` | the shape that used to answer a server failure: a walk's FINAL page is `complete` and `state == "continued"`, carries `0 < carried < members_total`, publishes no cursor, and says "completes the read walk" rather than claiming the whole roster |
| `test_a_roster_walk_larger_than_one_page_terminates_with_a_page_and_no_failure` | `:1095` | the multi-page boundary: every step is this route's own answer, every earlier page is incomplete with a cursor, and the pages **together** identify exactly `members_total` unique memberships — which is the claim the continuation control makes to a reader |

**The scenario is built once and shared through test-only text populations.** `FamilyScenario` is the
frozen handle; `scenario` is the module-scoped fixture and `build_family_scenario` builds the enclosure
over shared endpoint support. `rebuild_after_tree` and `extra_families` supply changed/one-sided
populations. The removed member-successor and family-successor helpers are not current authoring
owners. `_author_membership` and the extra-roster helper use test-only row construction, not the
retired canonical production authoring or admission plane.

**The request and read helpers keep every case on the shipped entry point.** `family_request`
(`:237-255`) builds the review request for a given selector; `review` (`:258-264`) calls the production
read; `entry_for` (`:267-272`) selects one family's context from the payload and
`members_of` (`:275-278`) indexes a side's roster by member revision, so the assertions read the
composed value rather than a re-implementation of it. `_complete` reads roster completeness and
`_review_of_unfamiliar_invariant` drives a subject the fixture never authored. The old sibling-family
and added-family author helpers are absent: one-sided populations come from the rebuilt text tree;
the multi-head ambiguity case is retained only as a removal disclosure. The reopen's two helpers keep the
walk on the same shipped entry point: `_author_extra_roster_rows` (`:952-998`) authors further memberships
through test-only invariant/revision/membership row construction — each a new invariant
identity with one revision cited by one membership row — and `_walk_the_route` (`:1001-1042`) follows one
side's walk exactly as the delivered control does, presenting `pageOf=family_members` with the cursor the
previous page published and **no page bound**, with `raise_server_exceptions=False` so an unhandled
failure is visible as the status the browser would receive rather than hidden in a traceback.

**The route case is the leaf's transport proof.** `test_the_family_context_reaches_the_client_over_the_real_review_route`
(`:878-930`) serves the payload through the real application (`_served`, `:933-946`) and asserts the
family context arrives over it, which is what distinguishes this deliverable from a display projection
assembled in the browser. The three walk cases drive that same served application — same fixture, same
route, same absence of an injected payload — one page at a time.

### Conventions

The module imports the shipped review read and its request/response values, test-only row support
and the fixture support modules the sibling review cases already use, and FastAPI's test client for
the one route case; the shared fixture is the sibling cases' own rather than a rebuild. `pytestmark`
(`:90`) selects the module's markers once. Module-level constants (`:95-113`) hold the authored labels,
guarantees and statements the cases assert against, so a case's expected bytes are visible at the top of
the file rather than buried in an assertion.

### Invariants And Boundaries

- **Nothing here builds a payload.** Every value asserted is composed by the production read over
  datasets built by the shared test-only text/row fixture support.
- **A truncated roster is never asserted as a whole one**, and the owner's own counts are asserted
  beside the cursor rather than restated.
- **The walk cases assert the completed page's own share, never a number the run happens to produce.**
  They pin shape — `0 < carried < members_total` on a completed continued page, the pages together
  identify `members_total` unique memberships, the single-page sentence absent from a multi-page walk's final page — because
  how many pages a given roster needs is a property of that run's page budgeting, not of the semantics
  under test. A reader should not read any page count out of this card as a contract.
- **The former ambiguity case is not current coverage.** One text family does not retain two further
  heads; the removed case name must not be advertised as an executed refusal witness.
- **The old 946-line soft-rail disclosure is historical.** It records the original mitigation through
  population/values-module splits, not a current line census or a newly verified hard-rail result.
- **Boundary: L24 owns the rendered tree and L25 the assembled project journeys.** This module proves
  the composition and its transport, not a mounted UI.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References


- `test_a_successor_family_revision_is_read_from_its_own_rows_not_inherited` supplies the current fixture or assertion described above. [42]


- `test_a_shared_member_is_one_canonical_revision_referenced_in_two_contexts` supplies the current fixture or assertion described above. [43]

- `test_missing_knowledge_is_the_reviews_refusal_not_an_empty_family_context` supplies the current fixture or assertion described above. [44]
- `test_the_published_cursor_continues_exactly_the_walk_that_minted_it` supplies the current fixture or assertion described above. [45]

- `test_a_roster_walk_larger_than_one_page_terminates_with_a_page_and_no_failure` supplies the current fixture or assertion described above. [46]


- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [47]


- RowStore writes text-tree fixture rows without the retired production admission plane. [48]


Every claim on this card is checkable in the module's own cases and in the owners they drive. The three
details a reader should carry: **test-only text/row construction supplies the shared endpoint
populations**, while the production read composes the payload from the side the resolution selected;
**the former multi-head ambiguity fixture is removed and supplies no current execution evidence**;
and **the route case serves the real application**, which is what proves the context reaches the client
over the shipped transport rather than being assembled in the browser.

### Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.


- **The leaf's load-bearing properties, one case each, and the fact that nothing here builds a review payload.** [49]


- The frozen scenario handle the cases read. [50]


- The module-scoped scenario fixture. [51]


- **The real leaf enclosure built over the shared endpoint fixture, with two real knowledge datasets.** [52]

The former member-successor author helper is removed; current changed populations are rebuilt as text trees.
The former family-successor author helper is removed; its name is not current production-admission evidence.

- **One membership row built by the test-only fixture helper, not the retired canonical authoring plane.** [55]

- The review request built for a given selector. [56]
- The production read the cases drive. [57]
- The one family context selected out of the payload. [58]
- A side's roster indexed by member revision. [59]
- **A selected invariant resolving every recorded family it belongs to, each with its own guarantee text.** [60]

- An unchanged family still composed at its own revision. [61]


- **A successor revision read from its own rows, with the dropped membership still carried on the side that records it.** [62]


- **One canonical revision referenced in two contexts, with the unique count not growing.** [63]


- **A member change making its family context available and concluding nothing about the guarantee.** [64]

- A selection in no recorded family as the measured zero. [65]
- Missing knowledge as the review's own refusal rather than an empty family context. [66]
- The task-context review stating that it selected no subject. [67]

- A family only the candidate records as a one-sided context with a stated absence. [68]

The old authored-ambiguity refusal case is removed from this population; no current witness is claimed.
The old sibling-family revision builder is removed with that ambiguity fixture.

- **A truncated roster staying partial with the owner's counts and the cursor that reaches the rest.** [71]

- The roster page's completeness as the case reads it. [72]
- **The published cursor continuing exactly the walk that minted it.** [73]
- **A cursor that binds no composed walk refused beside every first page.** [74]
- Naming the roster collection without a cursor earning the collection's own refusal. [75]
- A token of another format answered in the owner's own vocabulary. [76]

- **The complete source inventory and its unique counts not growing with a repeated membership.** [77]


- The one-sided family fixture. [78]


- The review of a subject the fixture never authored. [79]

- **The context reaching the client over the real review route, which is what makes this a transport proof.** [80]
- The real application the route case serves. [81]

- **Further memberships built through test-only row construction, so a roster needs more than one page of the production read walk.** [82]

- **One side's roster walk followed exactly as the delivered continuation control drives it, with the previous page's cursor and no page bound.** [83]
- **The single-page boundary: one page is the roster, complete, cursored nowhere, carrying every row and saying so.** [84]

- **The page the pre-correction guard refused: a completed FINAL page carrying only its own share, which used to answer a server failure.** [85]


- **The multi-page boundary: every step is this route's own answer and the pages together carried exactly the owner's total.** [86]


- **The production read these cases drive, which composes the context and carries it on the payload.** [87]


- The population cases this module's fixtures are shared with. [88]

- The values cases that pin the construction rules of the same deliverable. [89]

### Cross-Repo References

No cross-repository behavior is exercised by these cases. The enclosure, the two knowledge datasets, the
code trees and the served application all belong to this repository's own fixture support and to the
leaf enclosure the resolution selected. No remote, credential, network or external system is involved, so
no cross-repo reference row is recorded.
