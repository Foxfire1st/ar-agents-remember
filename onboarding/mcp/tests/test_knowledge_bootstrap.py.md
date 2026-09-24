# mcp/tests/test_knowledge_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T10:20+02:00 |
| lastVerifiedCommitHash | `06ed70cfcde7e3860ee5b53435727e7512e4335c` |
| lastVerifiedCommitDate | 2026-09-24T10:53:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The taskless knowledge bootstrap, driven as behaviour: real authority, the one write plane, and
recovery (ICR-R29@v1).** `knowledge-ingest` needs a leaf enclosure contract, so before this leaf the only
way a repository's *knowledge* could be written was by a task that already had a worktree — and the
documented answer for a repository whose first knowledge is being written was to fabricate one. These
cases measure the third option instead: a second **real** admission derived from the MCP settings
document and the ordinary read route's own resolution, driving the *same* operation the leaf path drives.

**Every case is one user operation on a real coordination world** — a real code checkout, a real external
memory repository at `<coordinationRoot>/memory-repos/ar-<repo>`, and a real MCP settings document —
driven through the shipped command line (`agents-remember knowledge-bootstrap`), and **every comparison
is made against something other than the run's own prose**: the location through the read route's own
owner, the identity through a read-back, the stored statements through the mounted read surface
(`knowledge_read_payload(..., view="invariant")`), and the remaining-work manifest read off disk.

**Nineteen cases**, as the user operations, the refusals that guard them, and the four the fix round
added for the retained record. The module's own docstring states the same count — its case list opens
**"Nineteen cases"** — and the sibling re-pin note in `test_dependency_ownership_ast_helpers.py` agrees,
so the code and this card carry one number rather than two.

## Code Commentary

### Logic

**The world builder is the fixture, and it makes "no enclosure was fabricated" measurable**
(`World`, `:99-123`). `world` (`:153-194`) creates the code checkout, the external memory repository and
the settings document; `World.destination` and `World.admitted` (`:111-122`) resolve the two places the
run uses through the production owners rather than through a path the test computed. The assertion that
the world contains **no `series-contract.md` at all** (`:304-304`) is what makes "no enclosure" a
measurement.

**The helpers are the comparisons, and each one reads something other than the run's report.**
`statements` (`:255-266`) and `revisions` (`:267-280`) read the mounted view surface; `progress_record`
(`:281-289`) reads the retained manifest off disk; `cli` (`:247-254`) drives `main()` and returns the exit
code beside the parsed JSON; `argv` (`:232-246`) builds the invocation.

**The ten operations** (`:290-896`):

- `test_a_repository_with_no_leaf_bootstraps_and_publishes_where_readers_look` (`:290`) — asserts
  `admissionProvenance.kind == "repository-bootstrap"` (`:310`), `authoritySource` as
  `<settings>#repositories.<id>` (`:313`), both source revisions, that no contract file exists anywhere
  in the world (`:304`), and that the contents block names this run as their publisher (`:332-335`).
- `test_an_exact_retry_reuses_operation_and_record_identity` (`:344`) — same held revision ids across two
  runs, same revision set in the dataset, `refused == []`.
- `test_existing_knowledge_is_not_overwritten_and_a_semantic_update_gets_its_own_revision` (`:379`) — the
  earlier statement survives verbatim, the dataset holds two revisions, and `destinationBefore.identity`
  equals the identity that was published.
- `test_an_interrupted_bootstrap_resumes_from_retained_identity_bound_progress` (`:425`) — the resumed
  run's allocated revision id equals the first run's.
- `test_a_planning_run_writes_no_batch_no_publication_and_no_progress_record` (`:479`) — the run asserts
  the record does not exist at all (`:502`).
- `test_cleanup_cannot_destroy_unpublised_work_and_removes_published_staging` (`:506`) — the packet's own
  non-conforming example, driven both ways.
- `test_a_moved_source_revision_is_an_explicit_re_observation_condition` (`:573`) — `batchState`
  `not_attempted`, the entry refused with `candidate_binding_changed`, the destination bytes
  byte-identical.
- `test_a_repository_the_settings_do_not_declare_is_refused_by_name` (`:623`).
- `test_the_destination_is_derived_and_no_argument_can_aim_it_elsewhere` (`:654`) — the destination
  equals the owner's own computation, and an argparse inspection finds no `publish_to`/`destination`/
  `expected_destination`.
- `test_a_repository_without_a_leaf_writes_its_only_candidate_under_the_staging_root` (`:678`) — the
  working candidate is inside the context's own temp root, and `REVIEW_CANDIDATE_RELATIVE_ROOT` is
  asserted **absent** from the world (`:692-692`, read through `.as_posix()`).
- `test_memory_init_names_the_knowledge_foundation_and_what_is_there_now` (`:701`).
- `test_an_unusable_destination_refuses_instead_of_publishing_over_it` (`:735`).
- `test_a_partial_run_names_the_refused_entry_as_remaining_and_publishes_only_what_committed` (`:757`) —
  the contents block reports `state "absent"` with `publishedByThisRun` **false** (`:823-825`).
- `test_cleanup_removes_a_staging_that_holds_no_authored_row` (`:798`) — a **measured** zero rather than
  an assumption of emptiness.
- `test_a_refused_publication_is_not_success_and_names_the_work_as_remaining` (`:847`) — the memory line
  is made unwritable, the batch commits, the publication is refused, and the entry is named remaining
  against a location measured to hold no dataset, with `publishedByThisRun` false on the contents block
  (`:878-879`).

**The four cases the fix round added, and the behaviour each one pins** (`:897-1049`):

- `test_a_retained_record_for_another_operation_refuses_before_anything_is_written` (`:897`) — the
  retained record is rewritten to name another scope, and the run must refuse with exit **2** and the code
  `staging_belongs_to_another_operation` naming **both** scopes, leaving the destination's bytes
  identical. This is the case that fails when the ownership guard is removed.
- `test_a_narrowed_resume_keeps_the_owed_entry_named_on_disk` (`:929`) — run one carries a committed and a
  refused entry, so the record names the refused one as owed; run two hands over **only** the committed
  entry and replays. The record it writes must still name the owed entry, carried with
  `carried == ["E-BAD"]` (`:958-958`) rather than deleted by the narrower list.
- `test_a_run_that_commits_nothing_still_refreshes_the_manifest` (`:967`) — a committed run whose batch
  wrote nothing writes the record anyway, so the previous record cannot stand stale exactly when the
  candidate binding moved.
- `test_a_carried_entry_the_repository_has_since_received_is_no_longer_owed` (`:1004`) — a carried entry
  is **re-derived against this run's own store read**, so once the dataset holds its revision it stops
  being owed; the carry is a re-observation, never a copy.

### Conventions

Cases carry `pytest.mark.evidence_unit` and are driven through the shipped `main()` rather than through a
private function, so the surface under test is the one an operator has. No case reads a private helper of
the modules it covers.

### Invariants And Boundaries

- Every comparison is against something other than the run's own prose.
- The bootstrap world contains no contract file; "no enclosure was fabricated" is asserted, not assumed.
- A measured absence (`absent`) and an unread location (`unmeasured`) are asserted as separate lists.
- The destination is compared against the read route's own owner, and the argument surface is inspected
  for a way to aim it.
- Cleanup is driven in both directions: it must refuse while the work is unpublished and remove once it
  is published.
- The retained record's carry-forward is pinned in all three of its states: kept when owed, refreshed by a
  run that committed nothing, and dropped once the store holds the revision.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the bootstrap case module. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the third option, the real world, and that comparisons are not made against the run's prose.** | "a second **real** admission"; "the run's own prose" | mcp/tests/test_knowledge_bootstrap.py:1-45 |
| **The world the cases run in, with the destination and the admission resolved through the production owners.** | `World`; `destination`; `admitted` | mcp/tests/test_knowledge_bootstrap.py:99-122 |
| The Git and filesystem helpers the world is built with. | `_git`; `_write`; `_commit` | mcp/tests/test_knowledge_bootstrap.py:124-152 |
| **The fixture: a real code checkout, a real external memory repository and a real settings document.** | `world` | mcp/tests/test_knowledge_bootstrap.py:153-194 |
| The hand-off entry and list builders. | `entry`; `hand_off` | mcp/tests/test_knowledge_bootstrap.py:195-233 |
| The invocation builder and the driver that returns the exit code beside the parsed JSON. | `argv`; `cli` | mcp/tests/test_knowledge_bootstrap.py:232-254 |
| **The readbacks: statements and revisions from the mounted view surface, and the manifest read off disk.** | `statements`; `revisions`; `progress_record` | mcp/tests/test_knowledge_bootstrap.py:255-289 |
| **The bootstrapped admission's own provenance, authority and both source revisions, with no contract file in the world and the contents block naming this run as publisher.** | `test_a_repository_with_no_leaf_bootstraps_and_publishes_where_readers_look`; "repository-bootstrap"; `destinationContents` | mcp/tests/test_knowledge_bootstrap.py:290-343 |
| **An exact retry reusing operation and record identity without a duplicate row.** | `test_an_exact_retry_reuses_operation_and_record_identity` | mcp/tests/test_knowledge_bootstrap.py:344-378 |
| **Existing knowledge not overwritten, and a semantic update getting its own revision.** | `test_existing_knowledge_is_not_overwritten_and_a_semantic_update_gets_its_own_revision` | mcp/tests/test_knowledge_bootstrap.py:379-424 |
| **A resume keeping the identity the earlier run was allocated.** | `test_an_interrupted_bootstrap_resumes_from_retained_identity_bound_progress` | mcp/tests/test_knowledge_bootstrap.py:425-478 |
| **A planning run writing no batch, no publication and no progress record at all.** | `test_a_planning_run_writes_no_batch_no_publication_and_no_progress_record`; `BOOTSTRAP_PROGRESS_NAME` | mcp/tests/test_knowledge_bootstrap.py:479-509 |
| **The packet's non-conforming example driven both ways: cleanup refuses unpublished work and removes published staging.** | `test_cleanup_cannot_destroy_unpublised_work_and_removes_published_staging` | mcp/tests/test_knowledge_bootstrap.py:506-572 |
| **A moved source revision as an explicit re-observation condition, leaving the destination byte-identical.** | `test_a_moved_source_revision_is_an_explicit_re_observation_condition`; "candidate_binding_changed" | mcp/tests/test_knowledge_bootstrap.py:573-622 |
| An undeclared repository refused by name. | `test_a_repository_the_settings_do_not_declare_is_refused_by_name` | mcp/tests/test_knowledge_bootstrap.py:623-653 |
| **The destination derived rather than accepted, with the argument surface inspected for a way to aim it.** | `test_the_destination_is_derived_and_no_argument_can_aim_it_elsewhere`; "expected_destination" | mcp/tests/test_knowledge_bootstrap.py:654-682 |
| **The candidate's only home is the bootstrap's own staging root, and the leaf review-candidate root is absent.** | `test_a_repository_without_a_leaf_writes_its_only_candidate_under_the_staging_root`; `REVIEW_CANDIDATE_RELATIVE_ROOT` | mcp/tests/test_knowledge_bootstrap.py:678-700 |
| The memory initializer naming the knowledge foundation and its measured state. | `test_memory_init_names_the_knowledge_foundation_and_what_is_there_now` | mcp/tests/test_knowledge_bootstrap.py:701-734 |
| An unusable destination refused instead of published over. | `test_an_unusable_destination_refuses_instead_of_publishing_over_it` | mcp/tests/test_knowledge_bootstrap.py:735-756 |
| **A partial run naming the refused entry as remaining and publishing exactly what committed.** | `test_a_partial_run_names_the_refused_entry_as_remaining_and_publishes_only_what_committed` | mcp/tests/test_knowledge_bootstrap.py:757-797 |
| **Cleanup removing a staging that holds a measured zero rather than an assumed emptiness.** | `test_cleanup_removes_a_staging_that_holds_no_authored_row` | mcp/tests/test_knowledge_bootstrap.py:798-846 |
| **A refused publication is not success: the entry is named remaining against a location measured to hold no dataset, and the contents block says this run published nothing.** | `test_a_refused_publication_is_not_success_and_names_the_work_as_remaining`; `publishedByThisRun` | mcp/tests/test_knowledge_bootstrap.py:847-896 |
| **The case that makes the staging-ownership guard bite: another scope's retained record refuses by name, exit 2, destination untouched.** | `test_a_retained_record_for_another_operation_refuses_before_anything_is_written`; "staging_belongs_to_another_operation" | mcp/tests/test_knowledge_bootstrap.py:897-930 |
| **The narrowed resume that must not delete the rest of the debt, asserted on the record read off disk.** | `test_a_narrowed_resume_keeps_the_owed_entry_named_on_disk`; "carried" | mcp/tests/test_knowledge_bootstrap.py:929-966 |
| **A committed run that wrote nothing still refreshes the manifest rather than leaving the previous record standing.** | `test_a_run_that_commits_nothing_still_refreshes_the_manifest` | mcp/tests/test_knowledge_bootstrap.py:967-1003 |
| **A carried entry re-derived against this run's own store read, so it stops being owed once the dataset holds it.** | `test_a_carried_entry_the_repository_has_since_received_is_no_longer_owed` | mcp/tests/test_knowledge_bootstrap.py:1004-1049 |
| **The admission the cases exercise through the shipped command line.** | `admit_bootstrap_context`; `AdmittedKnowledgeBootstrap` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:175-214; mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:132-151 |
| **The run composition whose per-entry rows, carried set and remaining list the cases assert.** | `bootstrap_knowledge`; `BootstrapRunResult`; `_carried_forward` | mcp/src/agents_remember/application/knowledge_bootstrap.py:153-240; mcp/src/agents_remember/application/knowledge_bootstrap.py:136-151; mcp/src/agents_remember/application/knowledge_bootstrap.py:243-293 |
| The cleanup owner whose two measured facts the cleanup cases drive. | `discard_bootstrap_staging` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:416-479 |
| The record name the cases read off disk, and the reader that reconstructs it. | `BOOTSTRAP_PROGRESS_NAME`; `read_progress` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:72-73; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:73-321 |
| The read surface the stored statements are read back through. | `knowledge_read_payload` | mcp/src/agents_remember/mcp/tools/knowledge.py:283-283 |
| The leaf review-candidate root name this module asserts is absent from a bootstrap world. | `REVIEW_CANDIDATE_RELATIVE_ROOT` | mcp/src/agents_remember/application/knowledge_review.py:203-203 |

## Cross-Repo References

No cross-repository behavior is exercised: every case builds its own single-repository coordination world
under a temporary root. The resolved settings' `crossRepo.allow` is empty, so nothing here names, reads
or writes another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T10:50+02:00 — 260921-ICR-L29 curator, **micro-round-2 bytes (documentation only)** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`): **re-read against the
  corrected docstring; the card and the source now agree, and the card's own note that they did not is
  retired.** The module docstring's case list now reads "Nineteen cases" and names the added operations,
  matching this card and the sibling re-pin note. All case ranges were re-derived for the docstring-only
  line shift; the nineteen case boundaries, the four carry-forward/ownership cases and the
  `destinationContents`/`publishedByThisRun` assertions are unchanged in kind. **No verification stamp was
  advanced.**

- 2026-09-24T10:20+02:00 — 260921-ICR-L29 curator, **fix-round bytes** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`; gate `verify-l29-round2.md`,
  first line `pass-with-findings`): **re-read against the fixed module and rewritten, not merely
  re-anchored.** The fix round grew this module 861 → **1050** lines and its case population 15 →
  **nineteen**, so every case range on this card was re-derived and four new cases were documented:
  `:897` (the staging-ownership refusal, the case that fails when that guard is removed), `:929` (a
  narrowed resume that must still name the owed entry), `:967` (a committed run that wrote nothing still
  refreshes the record) and `:1004` (a carried entry re-derived against this run's own store read). The
  contents assertions were updated with the F7 rename (`destinationContents`, `publishedByThisRun`), and
  the candidate-root assertion now names the `.as_posix()` call the F1 pyright fix introduced. **Two
  corrections of this card's own earlier draft:** it said "fifteen cases", and it did not know about the
  carry-forward at all. The module's own docstring then still said "Fifteen cases"; **that sentence was
  corrected by the micro round that followed**, and this card's Purpose now records that the docstring and
  the card agree on nineteen. **No
  verification stamp was advanced** — the candidate is uncommitted and the governed closeout owns the
  real code and memory commits.
- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): created this one-to-one card for the case module
  `ICR-R29@v1` introduced. The stamp basis is the leaf's base commit, because the module is untracked
  there. What a reader must not lose is that the cases measure the **third option** — a second real
  admission driving the same operation — and that each comparison is made against something other than
  the run's own prose (the read route's own destination owner, a read-back identity, the mounted view
  surface, and the manifest on disk). No verification stamp beyond the leaf's base is advanced: the
  candidate is uncommitted and the governed closeout owns the real commit.
