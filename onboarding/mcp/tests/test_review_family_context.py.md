# mcp/tests/test_review_family_context.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_family_context.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T02:20:00+02:00 |
| lastVerifiedCommitHash | `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` |
| lastVerifiedCommitDate | 2026-09-24T02:30:06+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

**The comparison-bound family context through the production composition (ICR-R31@v1).** These cases
drive the review the dashboard drives — the shipped read over a real leaf enclosure with a real Git
worktree and two real knowledge datasets — and measure the one composition `ICR-R31@v1` adds: the
recorded families the selected subject belongs to on each snapshot, each selected family revision's own
authored guarantee, and that revision's recorded member roster, **including the siblings a reviewer has
to be able to read beside a changed member**.

**Every population is produced by the store's own operations over the shared endpoint fixture** (`:9-13`):
the successor family revision and its memberships are authored through the family and membership owners,
the changed member is an authored successor revision of the sibling invariant, and the datasets the
review reads are the files its own resolution selected. Nothing here builds a review payload, injects a
family context, or reads a database the resolution did not choose.

**It is a separate module by the seam the deliverable already has, and it is a disclosed soft-rail
crossing.** At **1,133 lines** — 946 before this reopen's three walk cases — it is above the 900-line
soft rail and below the 1,200-line hard rail, and the census gained no offender: the offender sets are
byte-identical at base and candidate, 27 whole-tree and 26 over the `mcp` scope at both. Fix round 1
moved the four population cases into `mcp/tests/test_review_family_context_population.py` — importing
this module's enclosure and helpers rather than duplicating them — and the values cases into
`mcp/tests/test_review_family_context_values.py`; the reopen appended the three walk cases below as
**insertions only** (187 lines, nothing removed and nothing renamed), so no case that was here before was
weakened by it. The three modules together are the leaf's case population, and each is registered in
`mcp/tests/test-evidence-lanes.toml`'s `unit-regression` lane.

## Code Commentary

### Logic

**The load-bearing properties, one case each.** The module's own docstring lists them (`:15-25`); the
table below maps each to the case that pins it and the operation the case drives.

| Case | Line | The property it pins |
| --- | --- | --- |
| `test_a_selected_invariant_resolves_both_recorded_families_with_their_own_guarantees` | `:284` | a selected invariant resolves **every** recorded family it belongs to on both snapshots, each with its exact selected family revision, its own stored guarantee text and its recorded roster |
| `test_a_family_that_did_not_move_is_still_composed_at_its_own_revision` | `:321` | an unchanged family still yields a context at its own revision |
| `test_a_successor_family_revision_is_read_from_its_own_rows_not_inherited` | `:342` | a successor that drops a member does **not** inherit the parent's roster, and the dropped membership is still carried on the side that records it |
| `test_a_shared_member_is_one_canonical_revision_referenced_in_two_contexts` | `:384` | one invariant recorded under two families is one canonical revision referenced twice; the unique count does not grow with the repeated membership |
| `test_a_member_change_makes_its_family_context_available_and_concludes_nothing` | `:425` | a changed member makes its family context available and changes nothing about the guarantee |
| `test_a_selection_in_no_recorded_family_is_a_measured_zero` | `:455` | a selection in no recorded family is the measured zero, not an empty collection |
| `test_missing_knowledge_is_the_reviews_refusal_not_an_empty_family_context` | `:473` | missing knowledge is the review's own refusal, never an empty family context |
| `test_a_task_context_review_states_that_it_selected_no_subject` | `:487` | the task-context review states that it selected no subject |
| `test_a_family_only_the_candidate_records_is_a_one_sided_context_with_a_stated_absence` | `:501` | a family only the candidate records is a one-sided context with a stated absence |
| `test_an_ambiguous_family_lineage_names_its_candidates_and_chooses_no_revision` | `:523` | an authored ambiguity names its candidates and chooses no revision |
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
| `test_a_roster_walk_larger_than_one_page_terminates_with_a_page_and_no_failure` | `:1095` | the multi-page boundary: every step is this route's own answer, every earlier page is incomplete with a cursor, and the pages **together** carried exactly `members_total` — which is the claim the continuation control makes to a reader |

**The scenario is built once and shared, and every population comes from the store's own authors.**
`FamilyScenario` (`:116-124`) is the frozen handle the cases read; `scenario` (`:127-131`) is the
module-scoped fixture and `build_family_scenario` (`:134-165`) builds the real enclosure over the shared
endpoint fixture. The authored operations are the store's own: `_author_member_successor` (`:168-189`)
and `_author_family_successor` (`:192-213`) author successor revisions, and `_author_membership`
(`:216-231`) authors one membership row — so a roster no case asked for cannot appear, because the only
way a membership exists is that a case recorded it through the owner.

**The request and read helpers keep every case on the shipped entry point.** `family_request`
(`:237-255`) builds the review request for a given selector; `review` (`:258-264`) calls the production
read; `entry_for` (`:267-272`) selects one family's context from the payload and
`members_of` (`:275-278`) indexes a side's roster by member revision, so the assertions read the
composed value rather than a re-implementation of it. `_author_sibling_family_revisions` (`:566-587`)
builds the ambiguity fixture, `_complete` (`:625-628`) reads a roster page's completeness,
`_author_added_family` (`:793-831`) builds the one-sided case, and `_review_of_unfamiliar_invariant`
(`:834-872`) drives a review whose subject the fixture never authored. The reopen's two helpers keep the
walk on the same shipped entry point: `_author_extra_roster_rows` (`:952-998`) authors further memberships
through the store's own `create_invariant` / `create_revision` / membership owners — each a new invariant
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

The module imports the shipped review read and its request/response values, the store owners it authors
through, the fixture support modules the sibling review cases already use, and FastAPI's test client for
the one route case; the shared fixture is the sibling cases' own rather than a rebuild. `pytestmark`
(`:90`) selects the module's markers once. Module-level constants (`:95-113`) hold the authored labels,
guarantees and statements the cases assert against, so a case's expected bytes are visible at the top of
the file rather than buried in an assertion.

### Invariants And Boundaries

- **Nothing here builds a payload.** Every value asserted is composed by the production read over
  datasets the store's own operations authored.
- **A truncated roster is never asserted as a whole one**, and the owner's own counts are asserted
  beside the cursor rather than restated.
- **The walk cases assert the completed page's own share, never a number the run happens to produce.**
  They pin shape — `0 < carried < members_total` on a completed continued page, the pages together
  equal to `members_total`, the single-page sentence absent from a multi-page walk's final page — because
  how many pages a given roster needs is a property of that run's page budgeting, not of the semantics
  under test. A reader should not read any page count out of this card as a contract.
- **The ambiguity case asserts a refusal to choose**, not a chosen revision: the candidates are
  inspectable and no guarantee is presented as the family's own.
- **The disclosed soft-rail crossing is a disclosure, not a rail breach.** 946 lines is under the 1,200
  hard rail and adds no census offender; the split into the population and values modules is the
  mitigation the leaf applied, and this card records the crossing rather than implying it was avoided.
- **Boundary: L24 owns the rendered tree and L25 the assembled project journeys.** This module proves
  the composition and its transport, not a mounted UI.

### Todos

None recorded.

## Docs References

No configured domain documentation could be consulted for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole body is "No entries
configured yet." — so there is no external or domain source to check and no documentation row is
recorded here.

## Repo-Internal References

Every claim on this card is checkable in the module's own cases and in the owners they drive. The three
details a reader should carry: **every population is authored through the store's own operations over
the shared endpoint fixture**, so no case injects a payload or reads a database the resolution did not
choose; **the ambiguity case asserts that no revision was chosen** while the candidates stay inspectable;
and **the route case serves the real application**, which is what proves the context reaches the client
over the shipped transport rather than being assembled in the browser.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The leaf's load-bearing properties, one case each, and the fact that nothing here builds a review payload.** | "Every population is produced by the store's own operations over the shared endpoint fixture" | mcp/tests/test_review_family_context.py:1-34 |
| The frozen scenario handle the cases read. | `FamilyScenario` | mcp/tests/test_review_family_context.py:116-124 |
| The module-scoped scenario fixture. | `scenario` | mcp/tests/test_review_family_context.py:127-131 |
| **The real leaf enclosure built over the shared endpoint fixture, with two real knowledge datasets.** | `build_family_scenario` | mcp/tests/test_review_family_context.py:134-165 |
| The authored successor revision of a member invariant. | `_author_member_successor` | mcp/tests/test_review_family_context.py:168-189 |
| The authored successor family revision. | `_author_family_successor` | mcp/tests/test_review_family_context.py:192-213 |
| **One membership row authored through the membership owner, so a membership exists only because a case recorded it.** | `_author_membership` | mcp/tests/test_review_family_context.py:216-231 |
| The review request built for a given selector. | `family_request` | mcp/tests/test_review_family_context.py:237-255 |
| The production read the cases drive. | `review` | mcp/tests/test_review_family_context.py:258-264 |
| The one family context selected out of the payload. | `entry_for` | mcp/tests/test_review_family_context.py:267-272 |
| A side's roster indexed by member revision. | `members_of` | mcp/tests/test_review_family_context.py:275-278 |
| **A selected invariant resolving every recorded family it belongs to, each with its own guarantee text.** | `test_a_selected_invariant_resolves_both_recorded_families_with_their_own_guarantees` | mcp/tests/test_review_family_context.py:284-318 |
| An unchanged family still composed at its own revision. | `test_a_family_that_did_not_move_is_still_composed_at_its_own_revision` | mcp/tests/test_review_family_context.py:321-336 |
| **A successor revision read from its own rows, with the dropped membership still carried on the side that records it.** | `test_a_successor_family_revision_is_read_from_its_own_rows_not_inherited` | mcp/tests/test_review_family_context.py:342-381 |
| **One canonical revision referenced in two contexts, with the unique count not growing.** | `test_a_shared_member_is_one_canonical_revision_referenced_in_two_contexts` | mcp/tests/test_review_family_context.py:384-422 |
| **A member change making its family context available and concluding nothing about the guarantee.** | `test_a_member_change_makes_its_family_context_available_and_concludes_nothing` | mcp/tests/test_review_family_context.py:425-449 |
| A selection in no recorded family as the measured zero. | `test_a_selection_in_no_recorded_family_is_a_measured_zero` | mcp/tests/test_review_family_context.py:455-470 |
| Missing knowledge as the review's own refusal rather than an empty family context. | `test_missing_knowledge_is_the_reviews_refusal_not_an_empty_family_context` | mcp/tests/test_review_family_context.py:473-484 |
| The task-context review stating that it selected no subject. | `test_a_task_context_review_states_that_it_selected_no_subject` | mcp/tests/test_review_family_context.py:487-498 |
| A family only the candidate records as a one-sided context with a stated absence. | `test_a_family_only_the_candidate_records_is_a_one_sided_context_with_a_stated_absence` | mcp/tests/test_review_family_context.py:501-520 |
| **An authored ambiguity naming its candidates and choosing no revision.** | `test_an_ambiguous_family_lineage_names_its_candidates_and_chooses_no_revision` | mcp/tests/test_review_family_context.py:523-563 |
| The sibling family revisions that build the ambiguity fixture. | `_author_sibling_family_revisions` | mcp/tests/test_review_family_context.py:566-587 |
| **A truncated roster staying partial with the owner's counts and the cursor that reaches the rest.** | `test_a_truncated_roster_stays_partial_with_the_owners_counts_and_continuation` | mcp/tests/test_review_family_context.py:593-622 |
| The roster page's completeness as the case reads it. | `_complete` | mcp/tests/test_review_family_context.py:625-628 |
| **The published cursor continuing exactly the walk that minted it.** | `test_the_published_cursor_continues_exactly_the_walk_that_minted_it` | mcp/tests/test_review_family_context.py:631-673 |
| **A cursor that binds no composed walk refused beside every first page.** | `test_a_cursor_that_binds_no_walk_is_refused_beside_the_first_pages` | mcp/tests/test_review_family_context.py:676-714 |
| Naming the roster collection without a cursor earning the collection's own refusal. | `test_naming_the_roster_collection_without_a_cursor_is_refused` | mcp/tests/test_review_family_context.py:717-736 |
| A token of another format answered in the owner's own vocabulary. | `test_a_token_that_is_not_a_roster_cursor_is_answered_with_the_owner_vocabulary` | mcp/tests/test_review_family_context.py:739-754 |
| **The complete source inventory and its unique counts not growing with a repeated membership.** | `test_the_complete_source_population_does_not_grow_with_a_repeated_membership` | mcp/tests/test_review_family_context.py:760-790 |
| The one-sided family fixture. | `_author_added_family` | mcp/tests/test_review_family_context.py:793-831 |
| The review of a subject the fixture never authored. | `_review_of_unfamiliar_invariant` | mcp/tests/test_review_family_context.py:834-872 |
| **The context reaching the client over the real review route, which is what makes this a transport proof.** | `test_the_family_context_reaches_the_client_over_the_real_review_route` | mcp/tests/test_review_family_context.py:878-930 |
| The real application the route case serves. | `_served` | mcp/tests/test_review_family_context.py:933-946 |
| **Further memberships authored through the store's own operations, so a roster needs more than one page of the read walk.** | `_author_extra_roster_rows` | mcp/tests/test_review_family_context.py:952-998 |
| **One side's roster walk followed exactly as the delivered continuation control drives it, with the previous page's cursor and no page bound.** | `_walk_the_route` | mcp/tests/test_review_family_context.py:1001-1042 |
| **The single-page boundary: one page is the roster, complete, cursored nowhere, carrying every row and saying so.** | `test_a_roster_that_fits_one_page_is_carried_whole_and_says_so` | mcp/tests/test_review_family_context.py:1045-1057 |
| **The page the pre-correction guard refused: a completed FINAL page carrying only its own share, which used to answer a server failure.** | `test_the_final_page_of_a_long_walk_may_carry_only_its_own_share` | mcp/tests/test_review_family_context.py:1060-1092 |
| **The multi-page boundary: every step is this route's own answer and the pages together carried exactly the owner's total.** | `test_a_roster_walk_larger_than_one_page_terminates_with_a_page_and_no_failure` | mcp/tests/test_review_family_context.py:1095-1133 |
| **The production read these cases drive, which composes the context and carries it on the payload.** | `compose_review` | mcp/src/agents_remember/application/knowledge_review.py:371-611 |
| The population cases this module's fixtures are shared with. | `test_the_canonical_memberless_successor_shape_is_an_ambiguity` | mcp/tests/test_review_family_context_population.py:94-139 |
| The values cases that pin the construction rules of the same deliverable. | `test_a_context_whose_counts_do_not_describe_its_roster_is_refused` | mcp/tests/test_review_family_context_values.py:29-47 |

## Cross-Repo References

No cross-repository behavior is exercised by these cases. The enclosure, the two knowledge datasets, the
code trees and the served application all belong to this repository's own fixture support and to the
leaf enclosure the resolution selected. No remote, credential, network or external system is involved, so
no cross-repo reference row is recorded.

## Update History

- 2026-09-24T02:20:00+02:00 — 260921-ICR-L31 curator, **reopened enclosure** (`260921-icr-l31b`, same base `fdf3e4b6cfe73040d35cbfd4d8b93fd55369e499`): **this card gained the three walk cases the reopen appended, and its line-count disclosure was corrected.** The reopen's subject is a completion-semantics defect in `ReviewFamilyRevisionContext`, and these cases are its bite-proofs at the route: `test_a_roster_that_fits_one_page_is_carried_whole_and_says_so` (`:1045-1057`), `test_the_final_page_of_a_long_walk_may_carry_only_its_own_share` (`:1060-1092`) and `test_a_roster_walk_larger_than_one_page_terminates_with_a_page_and_no_failure` (`:1095-1133`), with the two helpers they need (`_author_extra_roster_rows` `:952-998`, `_walk_the_route` `:1001-1042`). The module is **946 → 1,133 lines**: still above the 900-line soft rail and below the 1,200-line hard rail, and the census offender sets are byte-identical at base and candidate, so the disclosed crossing did not become a breach. The appended block is **insertions only**, so every citation this card already carried still holds and none was re-anchored. What the card asserts about the new cases is deliberately **shape rather than arithmetic**: how many pages a roster needs is a property of that run's page budgeting (the read walk is bounded over its item population and its byte ceiling, not over rows), so no page count or per-page row count is recorded here as a contract — the cases assert the completed page's own share strictly between zero and the owner's total, the pages summing to that total, and the single-page sentence staying off a multi-page walk's final page. **Stamp accounting: no verification stamp was advanced** — the candidate is uncommitted and the governed closeout owns the real code and memory commits, so the header still names the leaf's base `fdf3e4b6` plus the working-tree delta.

- 2026-09-23T22:10:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): created this one-to-one card for the case module `ICR-R31@v1` introduced as the production-entry measurement of the comparison-bound family context. The stamp basis is honest rather than convenient: the module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf's base commit, and the verified basis is the working-tree delta on top of it — no commit contains what a stamp would otherwise claim to have verified. The card records the two things a reader should not have to rediscover: **every population is authored through the store's own operations over the shared endpoint fixture**, so no case builds a review payload, injects a context or reads a database the resolution did not choose; and **the module is a disclosed soft-rail crossing** at 946 lines — under the 1,200 hard rail, adding no census offender — with the population and values cases split into two sibling modules rather than growing this one. Fix round 1 added the sibling population module after round-1 verification falsified the composition's revision population; this module's own cases were not weakened by that fix, and the split is by seam rather than by line count.
