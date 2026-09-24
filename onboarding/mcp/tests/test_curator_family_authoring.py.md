# mcp/tests/test_curator_family_authoring.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_family_authoring.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T07:54+02:00 |
| lastVerifiedCommitHash | `06ed70cfcde7e3860ee5b53435727e7512e4335c` |
| lastVerifiedCommitDate | 2026-09-24T10:53:01+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**The curator's family plane and external-source manifest, driven through the real ingest
(ICR-R28@v2).** The module opens by stating what it is *not* (`:5-8`): nothing here re-protects a
citation round trip — the write half has its own cases (`test_knowledge_curator_ingest.py`) and the
list-driven operation has five more (`test_knowledge_curator_ingest_list.py`), **which this module
imports as its fixture rather than introducing a second one**.

**What it adds is what those cannot reach, and each case measures one of them through the real
operation** — `ingest_curator_list` over a real pair of repositories beside a real contract, with the
public read route reading the stored result back (`:10-27`):

- a family the curator declared is stored as **its own** joint guarantee with exact memberships, and its
  text is not any member's statement;
- one invariant revision can belong to **two** families, and one family to several revisions;
- a **deliberate no-family** outcome is retained with its basis in the revision's recorded conditions,
  while an entry the curator never examined is reported as unexamined and **not** as family-free;
- membership in a family is never **inferred** from a file, a route or a label — the packet's
  non-conforming import;
- a changed guarantee is a **successor** revision that preserves the earlier membership;
- a stored family revision is **examined** — its recorded text is read back and reported — and a
  membership can join it without re-declaring it;
- an external source is retained in a **bounded manifest** named by the record's own origin reference,
  and no source anchor is fabricated for it;
- a membership can be **retired** by the identity of the row this run read.

## Code Commentary

### Logic

**The fixture is shared, not duplicated.** The module imports `AUTHORIZATION`, `CODE_FILE`,
`CODE_SYMBOL`, `GONE_PATH`, `SourcePair`, `entry`, `pair`, `symbol` and `target` from
`test_knowledge_curator_ingest_list`, so the enclosure shape every case drives is the one the
list-driven suite already establishes. Its own helpers are thin: `declared` (`:99-117`) and `membership`
(`:120-134`) build one authored decision, `with_family` (`:137-141`) and `with_sources` (`:144-148`)
attach a plane to an entry, and `source` (`:158-175`) builds one declared external source.
`FAMILY_ALPHA`/`FAMILY_BETA` (`:71-72`), `GUARANTEE_ALPHA`/`GUARANTEE_BETA` (`:73-85`),
`NO_FAMILY_BASIS` (`:86-88`) and the `EXTERNAL_*` constants (`:89-91`) are the authored text the
assertions compare against.

**Every assertion that matters reads the store, not the report.** `database_of` (`:206-209`) reopens
the candidate's sqlite file; `guarantees` (`:242-249`) and `members_of` (`:252-261`) read the
`family_revision` and `family_member` rows; `conditions_of` (`:264-274`) reads the revision's recorded
conditions; `provenance_of` (`:304-315`) reads the written provenance; `family_memberships` (`:318-331`)
reads the endpoint triples; `table_counts` (`:284-301`) counts rows per family table. The public route
is exercised too: `family_view` (`:212-223`) and `invariant_view` (`:226-239`) go through
`open_read_context` and `read_knowledge_view`, so the stored result is also read back the way a product
reader reads it. `ingest` (`:184-197`) drives the real operation, and `committed_revision` (`:334-345`)
and `committed_invariant` (`:348-359`) resolve a report's identity for the entry.

**The cases are grouped by the property each one measures.**

| Property | Cases |
| --- | --- |
| A declared family is its own guarantee with exact memberships | `test_a_declared_family_is_stored_as_its_own_guarantee_with_exact_memberships` (`:367-422`) |
| Membership is never inferred from a file or a route | `test_one_file_and_one_route_are_not_a_family` (`:425-452`) |
| Shared membership across families and revisions | `test_one_revision_can_belong_to_two_families` (`:455-499`) |
| The deliberate no-family outcome versus the unexamined entry | `test_a_deliberate_no_family_outcome_is_retained_while_an_unexamined_entry_is_not` (`:507-547`) |
| A blank basis is refused rather than stored | `test_a_blank_basis_is_refused_instead_of_stored_as_an_unexplained_claim` (`:550-576`) |
| The undeclared key is refused by name | `test_a_membership_that_joins_no_declared_family_is_refused_by_name` (`:579-614`) |
| A stored revision is examined, not re-declared | `test_a_stored_family_revision_is_examined_and_joined_without_being_re_declared` (`:617-668`) |
| A changed guarantee is a successor preserving the earlier membership | `test_a_changed_guarantee_is_a_successor_that_preserves_the_earlier_membership` (`:671-744`) |
| A changed guarantee under one key is refused rather than rewritten | `test_a_changed_guarantee_under_one_key_is_refused_rather_than_rewritten` (`:747-797`) |
| A stored membership can be retired by the identity this run read | `test_a_stored_membership_can_be_retired_by_the_identity_this_run_read` (`:800-843`) |
| A retirement naming no stored membership is refused | `test_a_retirement_that_names_no_stored_membership_is_refused` (`:846-871`) |
| An external source is a manifest reference, never a Git anchor | `test_an_external_source_is_retained_in_a_manifest_and_never_becomes_a_git_anchor` (`:874-935`) |
| A refused entry spends no family identity | `test_a_declaration_whose_entry_is_refused_spends_no_identity` (`:938-972`) |
| **A replayed revision still writes the family plane its entry now authors** | `test_a_replayed_revision_still_writes_the_family_plane_its_entry_now_authors` (`:975-1044`) |
| An exact replay writes nothing and spends no identity | `test_an_exact_replay_writes_nothing_and_spends_no_identity` (`:1047-1085`) |
| A changed no-family basis on a stored revision is refused by name | `test_a_changed_no_family_basis_on_a_stored_revision_is_refused_by_name` (`:1088-1148`) |
| A run that writes nothing retains no manifest and says so | `test_a_run_that_writes_nothing_retains_no_manifest_and_says_so` (`:1151-1191`) |
| An unversioned source is refused | `test_a_source_with_neither_version_nor_retrieval_time_is_refused` (`:1194-1214`) |
| A planning run writes no family row and says so | `test_a_planning_run_writes_no_family_row_and_says_so` (`:1217-1242`) |
| The command line authors the family plane and reports it | `test_the_curator_command_line_authors_the_family_plane_and_reports_it` (`:1245-1320`) |

**The case that exists because a false sentence was reachable is the replayed-revision one**
(`:975-1044`). Its own docstring states what it asserts: step 1 authors an entry with a deliberate
no-family outcome, and step 2 re-runs the **same entry id** with the same targets and a new membership.
It asserts against the dataset rather than against the report's own strings — `table_counts` for the
four family tables, `members_of` for the exact stored revision set, `guarantees` for the stored text,
and the allocation journal's `familyRevisionId` equal to the reported guarantee id — so the case fails
the moment a run can report a family row it did not write. `test_an_exact_replay_writes_nothing_and_spends_no_identity`
(`:1047-1085`) is its deliberate complement, and it is the *non*-discriminating one: on a fully-stored
list both the old and the fixed predicate agree, so it is not presented as proof of the fix.

**The external-source case asserts the absence that matters** (`:874-935`): the manifest file exists at
the declared name with the digest the report names, the stored provenance's origin references name the
hand-off list and the manifest, and **no table holds the URL** — so the source is retained as a
reference and never becomes a repository path with a fabricated blob.

### Conventions

Every case drives the shipped entry points: the real `ingest_curator_list`, the real CLI `main`, the
real `open_read_context`/`read_knowledge_view` read route, and a real pair of repositories beside a real
`ar-series-contract/v1` enclosure. No case asserts a prebuilt payload or reaches into a private helper
to decide whether the operation worked. **Twenty cases, one lane row**: the module is registered in
`test-evidence-lanes.toml` and its consumer rows in `evidence-lifecycle.toml`, which is what makes the
population refuse a module with no lane.

### Invariants And Boundaries

- Assertions read the store; the report is a claim under test, never the oracle.
- The fixture module is imported, not re-created.
- A run that writes nothing retains no manifest and reports no digest.
- A replayed revision contributes its family plane alone; re-issuing its invariant or citations would
  be refused by the batch's own insert-absence preconditions.
- The deliberate no-family outcome travels in the revision's recorded conditions, and an unexamined
  entry is reported as unexamined rather than as family-free.
- No case fabricates a Git anchor for an external source.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this module protects the repository's own curator
operation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the family-plane cases. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it adds and of the eight properties its cases measure.** | "What this module adds is what those cannot reach"; "a membership can be **retired** by the identity of the row this run read" | mcp/tests/test_curator_family_authoring.py:1-27 |
| **The fixture is imported from the list-driven suite rather than duplicated.** | `AUTHORIZATION`; `CODE_FILE`; `CODE_SYMBOL`; `GONE_PATH`; `SourcePair`; `entry`; `pair`; `symbol`; `target` | mcp/tests/test_curator_family_authoring.py:43-58; mcp/tests/test_knowledge_curator_ingest_list.py:165-179; mcp/tests/test_knowledge_curator_ingest_list.py:182-262; mcp/tests/test_knowledge_curator_ingest_list.py:346-369; mcp/tests/test_knowledge_curator_ingest_list.py:372-375; mcp/tests/test_knowledge_curator_ingest_list.py:384-387 |
| The authored text the assertions compare against. | `FAMILY_ALPHA`; `FAMILY_BETA`; `GUARANTEE_ALPHA`; `NO_FAMILY_BASIS`; `EXTERNAL_URL`; `EXTERNAL_DIGEST`; `EXTERNAL_LOCATION` | mcp/tests/test_curator_family_authoring.py:71-91 |
| The four thin builders: one authored decision, one membership, one attach-a-plane call each for family and sources. | `declared`; `membership`; `with_family`; `with_sources` | mcp/tests/test_curator_family_authoring.py:99-148 |
| The declared-external-source builder and the citation helper. | `source`; `citation` | mcp/tests/test_curator_family_authoring.py:158-181 |
| The real operation driven once per case, and the candidate directory the store is reopened from. | `ingest`; `candidate_of`; `database_of` | mcp/tests/test_curator_family_authoring.py:184-209 |
| **The read-back through the shipped public route rather than a raw query.** | `family_view`; `invariant_view`; `open_read_context`; `read_knowledge_view` | mcp/tests/test_curator_family_authoring.py:212-239; mcp/src/agents_remember/application/knowledge_read.py:103-136; mcp/src/agents_remember/application/knowledge_views.py:86-112 |
| **The store readers every claim is asserted against: guarantees, member sets, recorded conditions, provenance and endpoints.** | `guarantees`; `members_of`; `conditions_of`; `statements_of`; `table_counts`; `provenance_of`; `family_memberships` | mcp/tests/test_curator_family_authoring.py:242-331 |
| The report identities a case resolves before reading the store. | `committed_revision`; `committed_invariant` | mcp/tests/test_curator_family_authoring.py:334-359 |
| **A declared family stored as its own guarantee with exact memberships.** | `test_a_declared_family_is_stored_as_its_own_guarantee_with_exact_memberships` | mcp/tests/test_curator_family_authoring.py:367-422 |
| **Membership is never inferred from a file or a route.** | `test_one_file_and_one_route_are_not_a_family` | mcp/tests/test_curator_family_authoring.py:425-452 |
| **One revision in two families, and one family across revisions.** | `test_one_revision_can_belong_to_two_families` | mcp/tests/test_curator_family_authoring.py:455-499 |
| **The deliberate no-family outcome retained with its basis, while an unexamined entry is reported as unexamined rather than family-free.** | `test_a_deliberate_no_family_outcome_is_retained_while_an_unexamined_entry_is_not` | mcp/tests/test_curator_family_authoring.py:507-547 |
| A blank basis refused instead of stored as an unexplained claim; the undeclared key refused by name. | `test_a_blank_basis_is_refused_instead_of_stored_as_an_unexplained_claim`; `test_a_membership_that_joins_no_declared_family_is_refused_by_name` | mcp/tests/test_curator_family_authoring.py:550-576; mcp/tests/test_curator_family_authoring.py:579-614 |
| **A stored revision examined and joined without being re-declared.** | `test_a_stored_family_revision_is_examined_and_joined_without_being_re_declared` | mcp/tests/test_curator_family_authoring.py:617-668 |
| **A changed guarantee stored as a successor that preserves the earlier membership, and the same key with a changed guarantee refused rather than rewritten.** | `test_a_changed_guarantee_is_a_successor_that_preserves_the_earlier_membership`; `test_a_changed_guarantee_under_one_key_is_refused_rather_than_rewritten` | mcp/tests/test_curator_family_authoring.py:671-744; mcp/tests/test_curator_family_authoring.py:747-797 |
| A stored membership retired by the identity this run read, and a retirement naming no stored membership refused. | `test_a_stored_membership_can_be_retired_by_the_identity_this_run_read`; `test_a_retirement_that_names_no_stored_membership_is_refused` | mcp/tests/test_curator_family_authoring.py:800-843; mcp/tests/test_curator_family_authoring.py:846-871 |
| **The external source retained in a bounded manifest named by the record's own origin reference, with no source anchor fabricated for it.** | `test_an_external_source_is_retained_in_a_manifest_and_never_becomes_a_git_anchor` | mcp/tests/test_curator_family_authoring.py:874-935 |
| A refused entry spends no family identity. | `test_a_declaration_whose_entry_is_refused_spends_no_identity` | mcp/tests/test_curator_family_authoring.py:938-972 |
| **The replayed-revision case, which asserts against the reopened dataset rather than the report's own strings.** | `test_a_replayed_revision_still_writes_the_family_plane_its_entry_now_authors` | mcp/tests/test_curator_family_authoring.py:975-1044 |
| The deliberate complement, which is not the discriminating case because both predicates agree on a fully-stored list. | `test_an_exact_replay_writes_nothing_and_spends_no_identity` | mcp/tests/test_curator_family_authoring.py:1047-1085 |
| A changed no-family basis on an already-stored revision refused by name; a run that writes nothing retaining no manifest and saying so. | `test_a_changed_no_family_basis_on_a_stored_revision_is_refused_by_name`; `test_a_run_that_writes_nothing_retains_no_manifest_and_says_so` | mcp/tests/test_curator_family_authoring.py:1088-1148; mcp/tests/test_curator_family_authoring.py:1151-1191 |
| An unversioned source refused; a planning run writing no family row and saying so. | `test_a_source_with_neither_version_nor_retrieval_time_is_refused`; `test_a_planning_run_writes_no_family_row_and_says_so` | mcp/tests/test_curator_family_authoring.py:1194-1214; mcp/tests/test_curator_family_authoring.py:1217-1242 |
| **The command line authoring the family plane and reporting it, which is the case the F4 guard bites on.** | `test_the_curator_command_line_authors_the_family_plane_and_reports_it` | mcp/tests/test_curator_family_authoring.py:1245-1320 |
| The operation under test and the report type its outcomes are read from. | `ingest_curator_list`; `IngestReport`; `IngestSelection`; `COMMITTED` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1122-1258; mcp/src/agents_remember/application/knowledge_curator_ingest.py:456-538; mcp/src/agents_remember/application/knowledge_curator_ingest.py:215-217 |
| The view request and family view the read-back builds. | `ViewRequest`; `FamilyView`; `InvariantView` | mcp/src/agents_remember/models/knowledge/view.py:1117-1148; mcp/src/agents_remember/models/knowledge/view.py:995-999; mcp/src/agents_remember/models/knowledge/view.py:988-993 |
| The command-line entry point one case drives end to end. | `main` | mcp/src/agents_remember/cli/__main__.py:62-64 |
| The candidate database the store is reopened from. | `candidate_database_path` | mcp/src/agents_remember/models/knowledge/snapshot.py:58-61 |
| The list-driven suite whose fixture this module imports rather than duplicating. | `SourcePair`; `entry`; `pair`; `target`; `symbol` | mcp/tests/test_knowledge_curator_ingest_list.py:165-179; mcp/tests/test_knowledge_curator_ingest_list.py:346-369; mcp/tests/test_knowledge_curator_ingest_list.py:182-262; mcp/tests/test_knowledge_curator_ingest_list.py:372-375; mcp/tests/test_knowledge_curator_ingest_list.py:384-387 |

## Cross-Repo References

No cross-repository behavior is implemented in this module; every case builds its own enclosure and its
own pair of repositories under `tmp_path`, and the resolved settings' `crossRepo.allow` is empty.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): created this one-to-one card for the twenty-case module
  `ICR-R28@v2` introduced for the curator's family plane and external-source manifest. The stamp basis
  is the leaf's base commit, because the module is untracked there. Two things a reader must carry
  away. First, **the fixture is imported, not re-created**: the pair/enclosure shape comes from
  `test_knowledge_curator_ingest_list`, and every case drives the real operation, the real CLI and the
  real public read route while asserting against the **reopened store** rather than the report's own
  strings. Second, the case that matters most is the replayed-revision one
  (`:975`), which exists because a run could report `recorded`/`authored`/`added` over a store holding
  zero family rows: step 1 authors a deliberate no-family outcome and step 2 re-runs the same entry id
  with a new membership, then counts rows in the dataset. Its complement
  (`test_an_exact_replay_writes_nothing_and_spends_no_identity`) is deliberately **not** presented as
  proof of the fix, because both predicates agree on a fully-stored list. No verification stamp beyond
  the leaf's base is advanced: the candidate is uncommitted and the governed closeout owns the real
  commit.
