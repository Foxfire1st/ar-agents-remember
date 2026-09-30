# mcp/src/agents_remember/application/knowledge_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T05:58:11+02:00 |
| lastVerifiedCommitHash | `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c` |
| lastVerifiedCommitDate | 2026-09-30T06:21:14+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` step 6 ("an empty database or
exit zero is not a populated foundation") is the process authority this run implements, and it is a
task-tree document rather than a configured domain source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the bootstrap run composition. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the three decisions and of who owns everything else.** | "Three decisions are made here, and only three"; "they are the same operation" | mcp/src/agents_remember/application/knowledge_bootstrap.py:1-38 |
| The published surface: the two result values, the reading, the contents re-export and the run. | `__all__` | mcp/src/agents_remember/application/knowledge_bootstrap.py:86-92 |
| The destination's three states and the contents read's three states as declared vocabularies. | `DestinationState`; `ContentsState` | mcp/src/agents_remember/application/knowledge_bootstrap.py:94-95 |
| Why a run did not begin, and the route that re-observes the condition. | `BootstrapRunRefusal` | mcp/src/agents_remember/application/knowledge_bootstrap.py:98-104 |
| **The pre-run read: the baseline the run forks from and the exact identity its publication may replace.** | `DestinationReading`; "baseline" | mcp/src/agents_remember/application/knowledge_bootstrap.py:107-121 |
| Everything one run measured, grouped so the retained record is assembled from one value. | `_ObservedRun` | mcp/src/agents_remember/application/knowledge_bootstrap.py:124-136 |
| One run's whole result: the admission, the batch, the readback and what remains. | `BootstrapRunResult` | mcp/src/agents_remember/application/knowledge_bootstrap.py:139-154 |
| **The run: two refusals before any write, then the one admitted batch with the explicit-update publication.** | `bootstrap_knowledge`; "staging_belongs_to_another_operation"; "destination_unusable" | mcp/src/agents_remember/application/knowledge_bootstrap.py:157-244 |
| **The fork decision through the ordinary read route's owner.** | `_read_destination`; `resolve_published_intent` | mcp/src/agents_remember/application/knowledge_bootstrap.py:300-330 |
| The snapshot identity one resolved selection carries. | `_identity_of` | mcp/src/agents_remember/application/knowledge_bootstrap.py:333-338 |
| **The read-back that happens only when the run's own report says it published something.** | `_read_back`; `published_identity_read_back` | mcp/src/agents_remember/application/knowledge_bootstrap.py:341-355 |
| **The namespace read from the dataset rather than assumed, because a view read refuses a foreign one.** | `_dataset_namespace` | mcp/src/agents_remember/application/knowledge_bootstrap.py:358-370 |
| One entry's row: the run's outcome and the store's independent answer. | `_entry_progress` | mcp/src/agents_remember/application/knowledge_bootstrap.py:373-381 |
| **Why an entry the report accounts for in no group is `unaccounted`.** | `_outcomes`; "unaccounted" | mcp/src/agents_remember/application/knowledge_bootstrap.py:384-400 |
| The assembly of one entry's row from the run's outcome and the store's answer. | `_one_entry` | mcp/src/agents_remember/application/knowledge_bootstrap.py:403-420 |
| **Where measured absence is kept apart from an unread location, including the refused-publication case.** | `_store_state`; "unmeasured"; "absence_established" | mcp/src/agents_remember/application/knowledge_bootstrap.py:419-464 |
| **The record assembled only from what the run measured, with `remaining` and `unmeasured` as two facts.** | `_progress`; `remaining_basis` | mcp/src/agents_remember/application/knowledge_bootstrap.py:469-499 |
| The destination fields taken from the read-back when there was one, so a disagreement is readable. | `_destination_state`; `_destination_identity` | mcp/src/agents_remember/application/knowledge_bootstrap.py:502-509; mcp/src/agents_remember/application/knowledge_bootstrap.py:512-519 |
| Which read established the destination fields, or that this run published nothing. | `_read_back_state`; `_destination_detail` | mcp/src/agents_remember/application/knowledge_bootstrap.py:522-525; mcp/src/agents_remember/application/knowledge_bootstrap.py:528-533 |
| **The derivation of both lists stated by name, with the unmeasured entries named as such.** | `_remaining_basis`; "UNMEASURED rather than remaining" | mcp/src/agents_remember/application/knowledge_bootstrap.py:536-582 |
| **The one operation both admissions reach, and the selection this run hands it.** | `ingest_curator_list`; `IngestSelection`; `IngestPublication`; `HeldOperation` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1079-1093; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1096-1113; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1116-1243; mcp/src/agents_remember/application/knowledge_curator_ingest.py:468-492 |
| The staging owner whose reader and writer this run uses. | `read_progress`; `write_progress`; `staged_candidate_directory`; `observed_now` | mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:230-233; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:236-239; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:253-323; mcp/src/agents_remember/application/knowledge_bootstrap_staging.py:393-415 |
| **The bounded contents read the remaining list is derived from.** | `dataset_revisions`; `DatasetContents` | mcp/src/agents_remember/application/knowledge_dataset_contents.py:55-100; mcp/src/agents_remember/application/knowledge_dataset_contents.py:103-182 |
| The read route's own publication-readback owner. | `published_identity_read_back`; `DeclaredPublicationLocation`; `PublishedIdentityReadBack` | mcp/src/agents_remember/application/knowledge_publication_route.py:68-80; mcp/src/agents_remember/application/knowledge_publication_route.py:97-112; mcp/src/agents_remember/application/knowledge_publication_route.py:202-250 |
| The resolved published intent, its unavailable form and the selection type. | `resolve_published_intent`; `PublishedIntentUnavailable`; `PublishedIntentSelection` | mcp/src/agents_remember/application/published_intent.py:280-304; mcp/src/agents_remember/application/published_intent.py:228-245; mcp/src/agents_remember/application/published_intent.py:195-210 |
| The identity type the destination reading and the retained record carry. | `SnapshotIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:195-204 |

## Cross-Repo References

No cross-repository behavior is implemented in this file: it runs one repository's bootstrap against
that repository's own admission. The resolved settings' `crossRepo.allow` is empty, so nothing here
names, reads or writes another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): No content impact: citation-only repair. This card's source is unchanged. Rows citing `mcp/src/agents_remember/application/published_intent.py` were re-pointed to the lines MIK-R05 moved, by the installed fixer or by the exact line shift where it declined (each such row byte-identical to memory HEAD, its anchors checked in the base and the shifted ranges); no claim was reworded.
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R01 moved lines in `application/published_intent.py`, so citation ranges into it were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (each such row was byte-identical to memory HEAD).
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/src/agents_remember/application/knowledge_curator_ingest.py`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T10:50+02:00 — 260921-ICR-L29 curator, **micro-round-2 bytes (documentation only)** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`): **re-read against the
  corrected docstrings; the card and the source agree** — the module docstring now reads "The record is written by any run that was given the commit word", which is exactly what this card's Logic section says; the third decision bullet still describes the run's own three decisions and the carry-forward is stated in the section this leaf added. All ranges were re-derived for the docstring-only line shift. **No verification stamp was advanced.**
- 2026-09-24T10:20+02:00 — 260921-ICR-L29 curator, **fix-round bytes** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`; gate `verify-l29-round2.md`,
  first line `pass-with-findings`): **re-read against the fixed module and rewritten.** Two things this
  card said are no longer true of the code. (a) It said the record is written only by a run that really
  wrote; the fixed `bootstrap_knowledge` writes it whenever the developer gave the commit word
  (`:226-226`), including a run whose batch wrote nothing, because a record left standing is how the owed
  work goes stale when the candidate binding moved. (b) It described `remaining` as derived from this
  run's own list alone. The fix round added `_carried_forward` (`:243-293`): every entry an inherited
  record left owed and this run's list does not mention is carried in with `outcome` `carried` and its
  state **re-derived against this run's own store read**, so a narrowed resume cannot delete the rest of
  the debt and an entry the store has since received stops being owed. `BootstrapRunResult` and the
  retained record both gained the carried set. All line references were re-derived on the 577-line
  candidate (the module was 473 lines when this card was first written). **No verification stamp was
  advanced** — the candidate is uncommitted and the governed closeout owns the real code and memory
  commits.

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): created this one-to-one card for the module
  `ICR-R29@v1` introduced as **the bootstrap run composition**. The stamp basis is the leaf's base
  commit, because the module is untracked there. What a reader must not lose is that this composition
  owns no write: it hands the same `ingest_curator_list` a different admission, so the candidate,
  namespace, identity allocation, first generation, batch, snapshot and publication stay with the shipped
  owners. The second is that the report's claims are **measurements**: a planning run persists nothing, a
  published-not run records the refusal rather than the write half's success, and `remaining` (measured
  absence or no attempt) is never merged with `unmeasured` (a read that could not be completed). No
  verification stamp beyond the leaf's base is advanced: the candidate is uncommitted and the governed
  closeout owns the real commit.
