# mcp/src/agents_remember/application/knowledge_bootstrap.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**One taskless bootstrap run (ICR-R29@v1): admit, write through the one write plane, read it back,
retain the progress.** This is the composition the requirement is about. It owns no write, no identity,
no namespace and no snapshot: it admits a context, hands the curator's list to the existing ingest
operation as **one** admitted batch, and then reports what the repository actually holds afterwards.
Everything in between — the candidate, the namespace, the identity allocation, the first generation, the
batch, the snapshot and the publication — stays with the shipped owners, which is why a bootstrap and a
leaf's ordinary authoring cannot drift apart: they are the same operation with different admissions.

**Three decisions are made here, and only three.**

- **What this run forks from.** The destination the ordinary read route selects is read *before* anything
  is written, through that route's own owner. A location that holds a dataset is the baseline this run
  forks from and the exact identity its publication may replace; a location that holds nothing is the
  cold start; a location that holds something which is not a dataset of this code is neither, and the run
  refuses by name instead of publishing over it or starting a second store beside it.
- **What is published back.** The publication owner's own result is read back through
  `published_identity_read_back`, so the report says whether the dataset a *reader* will select is the one
  the write reported. Exit status is never that proof.
- **What remains.** The remaining-work manifest is derived from a read of the published dataset through
  the shipped view API, keyed on the identities the candidate's allocation journal holds — never from the
  plan and never from the run's own hopes. A store read that cannot be completed produces a named
  limitation, and an entry whose revision is not in the dataset is `absent` while one whose revision could
  not be looked for at all is `unmeasured`. **Owed work is carried forward, and re-derived rather than
  copied**: every entry an inherited record left owed that this run's own list does not mention is added
  to this run's rows with `outcome` `carried`, its state re-read from the store, so a narrowed resume
  cannot delete the rest of the debt and an entry the dataset has since received stops being owed.

**The record is written by any committed run, and that is wider than "a run that wrote".** A planning
run returns the identical projection and persists nothing, exactly as the ingest itself writes nothing
without the commit word. A **committed** run writes the record even when its batch wrote nothing —
including the case where the run refused before the batch, because every field in the record is a read of
the store and of this run's own outcome, so a run that wrote nothing still has something true to retain
(the owed work it re-derived), and leaving the previous record standing is how a manifest goes stale
exactly when the candidate binding moved. A published-not run — the batch committed but the publication
refused — therefore also writes one, and it says the publication was refused and where the destination
stands instead of borrowing the success of the write half.

## Code Commentary

### Logic

**`bootstrap_knowledge` is the run, and it starts with two refusals before any write** (`:151-231`). The
retained progress is read first: `retention.state == "moved"` returns
`staging_belongs_to_another_operation`, because one staging directory belongs to exactly one bootstrap
operation. Then the destination is read: `before.state == "unusable"` returns `destination_unusable`
stating that nothing was written and the previous dataset is intact. Only then is the list handed to
`ingest_curator_list` with an `IngestSelection` carrying the staged candidate directory, the
authorization reference, `dry_run=not commit`, the baseline the destination read established, and the
`IngestPublication` with `destination_path` and `expected_destination` — the two halves of the explicit
update.

**`_read_destination` is the fork decision, and it is three-valued** (`:234-264`).
`resolve_published_intent` answers `not-recorded` (cold start: no baseline, no expected identity),
`recorded` (the baseline the run forks from **and** the exact identity its publication may replace — both
derived from the same read, so a run cannot fork from one dataset and publish over another), or
`unusable`.

**`_read_back` never reads whatever happens to be there** (`:275-289`). The condition is the run's own
report: a publication the owner refused established nothing about the destination, and a run whose batch
did not commit published nothing at all — in both cases the honest answer is that there is nothing to read
back. Only when the report carries a publication identity is the declared location read back through
`published_identity_read_back`.

**`_dataset_namespace` reads the namespace rather than assuming it** (`:292-304`). A view read refuses a
namespace the dataset is not bound to, so the value must come from a read of the file: the pre-run
destination read, or the identity this run's own publication reported. The docstring is explicit that it
is never the repository's display name, which is not an identity.

**`_store_state` is where measured absence and an unread location are kept apart** (`:357-400`). A held
revision found in `contents.revisions` is `stored`; one that was not found under a read that
*established* absence is `absent`; one that could not be looked for at all is `unmeasured`; an entry with
no creation operation in the journal is `not-attempted`. The docstring names the case that makes this
load-bearing: a refused publication leaves a location holding **no dataset at all**, so the committed
revision is measurably absent and the entry genuinely is outstanding work rather than an unknown.

**An entry the report lost is `unaccounted`, not given the benefit of a group** (`:318-334`). The report
promises an entry appears in exactly one of `committed`, `rulings` or `refused`; an entry in none of them
is recorded as `unaccounted`, because a list that lost an entry is a different fact from a list that wrote
one.

**The record is assembled only from what the run measured** (`:403-430`), and the destination fields say
which read established them: `_destination_state`/`_destination_identity`/`_destination_detail`
(`:433-464`) prefer the read-back's own answer when there was one, and `_read_back_state` (`:453-456`) is
`not-published` when this run published nothing to read. So a publication whose read-back disagrees with
the writer leaves a record that says so rather than one that repeats the writer's claim.

**`_remaining_basis` states the derivation and the limitation by name** (`:467-501`): the run's own
per-entry outcomes, the candidate's allocation journal, and a read of the published dataset through the
invariant view — with the contents state and detail quoted, and the unmeasured entries named as
`UNMEASURED rather than remaining`.

### Conventions

The module composes the admission, the staging owner, the contents read, the ingest operation, the
publication route and the published-intent resolver. It writes no knowledge record and imports no
database driver.

### Invariants And Boundaries

- The operation is the same `ingest_curator_list` a leaf drives; the only difference is the admission.
- A planning run persists nothing; **any committed run persists a record**, including one whose batch
  wrote nothing, and a published-not run's record says the publication was refused rather than
  borrowing the write half's success.
- A carried entry is re-derived against this run's own store read; the carry is never a copy of the
  inherited state.
- `remaining` is measured absence or no attempt; `unmeasured` is a read that could not be completed. They
  are separate fields.
- The destination is read **before** any write, and the baseline and the expected identity come from that
  one read.
- The read-back is conditional on the run's own report; a refused publication is not read back.
- An entry the report accounts for in no group is `unaccounted`.
- No field of the retained record comes from the plan.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` step 6 ("an empty database or
exit zero is not a populated foundation") is the process authority this run implements, and it is a
task-tree document rather than a configured domain source.

No external documentation is required for the bootstrap run composition.

### Repo-Internal References

- **The module's own statement of the three decisions and of who owns everything else.** [1]
- The published surface: the two result values, the reading, the contents re-export and the run. [2]
- The destination's three states and the contents read's three states as declared vocabularies. [3]
- Why a run did not begin, and the route that re-observes the condition. [4]
- **The pre-run read: the baseline the run forks from and the exact identity its publication may replace.** [5]
- Everything one run measured, grouped so the retained record is assembled from one value. [6]
- One run's whole result: the admission, the batch, the readback and what remains. [7]
- **The run: two refusals before any write, then the one admitted batch with the explicit-update publication.** [8]
- **The fork decision through the ordinary read route's owner.** [9]
- The snapshot identity one resolved selection carries. [10]
- **The read-back that happens only when the run's own report says it published something.** [11]
- **The namespace read from the dataset rather than assumed, because a view read refuses a foreign one.** [12]
- One entry's row: the run's outcome and the store's independent answer. [13]
- **Why an entry the report accounts for in no group is `unaccounted`.** [14]
- The assembly of one entry's row from the run's outcome and the store's answer. [15]
- **Where measured absence is kept apart from an unread location, including the refused-publication case.** [16]
- **The record assembled only from what the run measured, with `remaining` and `unmeasured` as two facts.** [17]
- The destination fields taken from the read-back when there was one, so a disagreement is readable. [18]
- Which read established the destination fields, or that this run published nothing. [19]
- **The derivation of both lists stated by name, with the unmeasured entries named as such.** [20]
- **The one operation both admissions reach, and the selection this run hands it.** [21]
- The staging owner whose reader and writer this run uses. [22]
- **The bounded contents read the remaining list is derived from.** [23]
- The read route's own publication-readback owner. [24]
- The resolved published intent, its unavailable form and the selection type. [25]
- The identity type the destination reading and the retained record carry. [26]

### Cross-Repo References

No cross-repository behavior is implemented in this file: it runs one repository's bootstrap against
that repository's own admission. The resolved settings' `crossRepo.allow` is empty, so nothing here
names, reads or writes another repository.

No meaningful cross-repo references found.
