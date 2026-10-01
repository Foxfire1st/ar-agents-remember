# mcp/tests/test_review_final_output_receipt.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The final-output receipt driven end to end, against the store's own reopened truth (ICR-R21@v1).** A
comparison generation records what a review *read*; closeout and integration produce what the task
*delivered*. These eleven cases drive that whole operation for real — a live enclosure with two real
datasets and a real captured candidate, the real freeze, the real publication owner at the repository's
declared location, and the real `worktree_closeout_preview_tool` / `worktree_closeout_apply_tool` /
`worktree_integrate_tool` — and then compare every identity the receipt recorded against the store's own
reopened truth: the generation store, the Git objects and the published dataset. **Nothing here is a
prebuilt payload, and no case asserts a value the operation did not produce.**

The load-bearing properties, one case each:

| Property | Case |
| --- | --- |
| the conforming example — the recorded comparison opens the pair the task actually landed | `test_review_receipt_binds_the_delivered_pair_to_the_selected_generation` (`:451`) |
| the integration phase records the refs it landed | `test_integration_receipt_records_the_refs_it_landed` (`:510`) |
| the non-conforming example — the published dataset is not the one the review compared | `test_review_receipt_reports_a_published_dataset_the_review_never_compared` (`:544`) |
| the boundary — a candidate that moves is recorded as `moved`, the prior receipt keeps its bytes, and a successor supersedes it by naming it | `test_a_moved_candidate_is_recorded_as_moved_and_superseded_not_relabelled` (`:572`) |
| a leaf with no generation records no receipt and still closes — the receipt is not a gate | `test_closeout_records_no_receipt_without_a_generation_and_still_closes` (`:617`) |
| receipts are leaf-scoped, one per phase, and the named reclamation owner removes them | `test_final_output_receipts_are_leaf_scoped_and_reclaimed` (`:640`) |
| a location holding something that is not a dataset is `unusable`, never a mismatch | `test_review_receipt_reports_an_unreadable_published_location` (`:676`) |
| the preview's selection sentence never claims a recording the store lacks | `test_preview_selection_sentence_never_claims_a_recording_the_store_lacks` (`:701`) |
| a selected knowledge operand with nothing published is `unmeasured`, never `bound` | `test_a_selected_knowledge_operand_with_nothing_published_is_never_bound` (`:755`) |
| a forged `bound` verdict is refused at read-back | `test_a_forged_coverage_verdict_is_refused_when_read_back` (`:790`) |
| the reopened generation reports what the task delivered, phase by phase | `test_the_reopened_generation_reports_what_the_task_delivered` (`:825`) |

## Code Commentary

### Logic

**The fixture is the product path, and it says so where a shortcut would have been easier.** The module
creates its own two review datasets through the store's own API instead of the shared read-scope
fixture's pair, and the reason is measured rather than stylistic: that fixture invents a random namespace
and records the module's fixed authority home beside it, and while the review route reads under the
namespace, the *publication read-back* consults the authority home — so a dataset bound to another
repository's authority home is another repository's publication, and the store refuses to rebind a
namespace (`apsw.ConstraintError: immutable_revision: a repository namespace cannot be rebound`). The
datasets are therefore created bound to the repository the contract names
(`_seed_review_datasets`, `:113-177`). The two halves differ by `CANDIDATE_ONLY_INVARIANT_ID` (`:107`) on
purpose, "so the two halves are different datasets rather than two spellings of the same one: the
comparison is between them, and 'the published dataset is the reviewed candidate' must be a measurement
rather than a file name".

**Everything downstream of the fixture is a shipped owner.** `_review_closeout_fixture` (`:234-297`)
builds a real enclosure; `_write_review_task_documents` (`:299-371`) writes the real task documents;
`_freeze_review` (`:373-390`) calls the real `freeze_review_comparison`; `_publish_dataset` (`:392-415`)
calls the real publication owners (`freeze_closed_snapshot` + `publish_prepared_snapshot`) at the declared
location; and `_preview` (`:417-427`) / `_closeout` (`:429-449`) call the real MCP tool functions. The
helpers only *address* the operation — they never substitute for it.

**Assertions compare against the store, not against the receipt's own words.** Case 1 (`:451-508`) checks
`delivered_code_commit` against the contract's own `code_commit` **and**
`git rev-parse <commit>^{tree}` **and** the reviewed candidate tree the manifest bound;
`delivered_memory_tree_id` against the memory repository's own object; `published_knowledge_digest`
against `dataset_identity` of the published copy **and** the generation's after-side digest;
`manifest_digest` against `read_generation_refs(...)[-1].manifest_digest`; the receipt file's
`sha256(bytes)` against the reported sha256 with `read_back == matched`; and then re-derives all of it
through `reopen_comparison_generation(...)` and `read_final_output_receipt(...)` so the record is checked
against the store twice. That is the difference between testing the receipt and testing a restatement of
it.

**The three packet examples are cases, not prose.** Case 3 (`:544-570`) is the non-conforming example: the
published dataset is the *baseline* half, `code_match` stays matched while `knowledge_match` differs,
`receipt_state == moved`, and the case asserts the coverage string is **absent** from the statement — it
checks the sentence for the false claim it must not make. Case 4 (`:572-615`) is the boundary: after the
candidate moves, `prepared_is_reviewed_candidate is False` and the state is `moved` with the generation id
unchanged; freezing a successor with `ComparisonFreezeOptions(parent=…)` gives `generation_index + 1` and
a lineage naming the first generation; and **the earlier receipt's sha256 is identical before and
after** while its read-back now names the successor — supersession as a resolved value, not an edit.

**Two cases exist because a round-1 verifier found a false sentence and an unprotected narrowing.** Case
`:701` drives the real preview twice on one enclosure and puts the store's own reader beside each state —
(a) nothing recorded, so `read_final_output_receipt` returns `not-recorded`; then a real publication, a
real closeout recording generation 1, a candidate move and a real successor generation, so (b) the
preview names index 2 while the stored receipt still names generation 1 with `superseded_by == [2]` and
generation 2 itself reads back `not-recorded`. Both states assert the prospective wording is present and
the past-tense coverage wording is **not**. Case `:755` is the missing narrowing case: a selected
knowledge operand with nothing published is `unmeasured` (never `bound`), code matched,
`knowledge_match == "not-comparable"`, `published_knowledge_state == "not-recorded"`, the unmeasured
clause present and the coverage string absent — and the *integration* result of the same delivery is
`unmeasured` too. Case `:790` writes **canonical** bytes with `state: "bound"` over its own
`knowledge_match: "not-comparable"`, asserts the read-back is `unreadable` with the verdict rule named,
and then restores the genuine bytes to `recorded`/`unmeasured`.

**The reopen is asserted as a channel, not as a flag.** Case `:825` checks the fourth channel's phase
list, the recorded closeout entry's sha256/commit/verdict, and that the *unmeasured* integration phase is
an entry too — so "nothing was recorded" and "no phase was asked about" cannot read the same.

### Conventions

The module's docstring (`:1-23`) states the load-bearing properties one case each, so a reader can map a
failure to a property without reading the cases. Fixtures are `_`-prefixed module helpers rather than
pytest fixtures, because they build one shared enclosure value (`_ReviewCloseout`, `:219-232`) that the
cases address through `_preview`/`_closeout`. The module registers its lane row in
`mcp/tests/test-evidence-lanes.toml` and its three `consumer_scope = "exact"` rows in
`mcp/tests/evidence-lifecycle.toml` (which re-pins `LIFECYCLE_CATALOG_SHA256` in
`test_dependency_ownership_ast_helpers.py`) — the documented procedure for adding a test module, with the
population unchanged at 16 contracts / 66 artifacts. It adds **no** new `# noqa` and no timers, and it
measures 871 lines, inside the 900 soft rail.

### Invariants And Boundaries

- **No case asserts a returned prebuilt payload.** Every identity is compared against the store's own
  answer, and the assert is on the operation's output *and* on the record re-read from disk.
- **The fixture provisions datasets; it never replaces the operation under test.** Resolution,
  comparison, freeze, publication, closeout and integration are the shipped owners.
- **A false coverage sentence is a test failure, not a review note.** Cases `:701` and `:755` assert the
  absence of the coverage string, which is why a reverted sentence fails a case rather than passing
  silently.
- **Boundary: the browser half of A17/A20/A22 is out of scope here** and remains ICR-R25@v1's per
  `notes/05-acceptance-plan.md`; this module evidences the production operation, not a rendered surface.
- **Boundary: no crashed-closeout fixture with a frozen generation.** The "failed/partial transaction"
  clause is evidenced by the no-generation case, the `ok`-gated attachments, and the fact that recording
  happens only after the contract write — stated as a limit in the worker report rather than implied.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The claims on this card are checkable in the module's own docstring and cases. What a reader should
carry: the fixture's dataset setup is a **measured** requirement rather than a preference (the shared
read-scope fixture binds another repository's authority home, which the publication read-back consults);
the assertions compare against the store twice (the operation's own result and the record re-read from
disk); and the newest four cases exist because a verifier reproduced a false sentence and an unprotected
narrowing, so each of them fails if that behaviour is reverted.

- **The module's own map from property to case, and its statement that nothing here is a prebuilt payload.** [1]
- The catalogue rows this module occupies, and the one revision identity both halves must carry for a subject to be selectable at all. [2]
- **The measured reason this module creates its own datasets instead of using the shared read-scope fixture.** [3]
- The one enclosure value the cases address, and the real fixture that builds it. [4]
- The real freeze, the real publication owners, and the real MCP tool calls the cases drive. [5]
- **The conforming case, whose every identity is compared against the contract, the Git objects, the published dataset and the reopened generation.** [6]
- The integration phase records the refs it landed, after the move. [7]
- **The non-conforming case: a published dataset the review never compared reads `moved`, and the coverage string is asserted absent.** [8]
- **The boundary case: the prior receipt's bytes are identical after a successor supersedes it.** [9]
- The no-gate case: no generation, no receipt, and the closeout still reaches a real commit. [10]
- **The boundedness case: one file per phase, leaf-scoped, removed by the named owner.** [11]
- A location holding something that is not a dataset is `unusable`, with the bytes left untouched. [12]
- **The reproduced false sentence: the preview never claims a recording the store lacks, in both states.** [13]
- **The narrowing that was unprotected: a selected knowledge operand with nothing published is `unmeasured`, never `bound`.** [14]
- **The tamper case: canonical bytes carrying a forged `bound` read back `unreadable`.** [15]
- **The consumer case: the reopened generation reports what the task delivered, phase by phase.** [16]
- The lane row and the three exact-scope consumer rows this module is registered in, with the digest re-pin. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The cases build a real enclosure, a real
generation store and a real published dataset inside one repository boundary; the publication read-back
consults that repository's authority home, which is why the fixture is bound to the contract's own
repository rather than to an invented one.

No meaningful cross-repo references found.
