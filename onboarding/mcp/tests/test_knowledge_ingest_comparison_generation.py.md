# mcp/tests/test_knowledge_ingest_comparison_generation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_ingest_comparison_generation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T00:34:45Z |
| lastVerifiedCommitHash | `c114deaca13555f3c5121a7f5b803233b6bd866c` |
| lastVerifiedCommitDate | 2026-09-27T02:50:14+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **successful journey of one comparison's before side**, and the production-composition evidence
for `ICR-R18@v1`'s conforming and boundary examples. The defect these cases seal: with **one**
path used for both `--baseline` and `--publish-to`, two successive successful writes each reported
`changed` and published — and the second one re-placed the review's before half from the bytes it
captured, which by then *were* the first run's publication. The comparison then opened on a dataset
that already contained the addition, so the review showed it present on both sides with an empty
delta. The prior refused-rerun repair (`260915-KS-L47`) did not cover the successful-update path, and
capturing the baseline earlier cannot cover it either: the bytes are a different dataset by then, not
a later read of the same one.

**A fourth case, added by `260921-ICR-L34`, protects the second half of the same journey: recording
the comparison.** The three cases above end with the before half correctly placed; a review of that
leaf then has to be *recorded*, and recording retains each half by copying it through the storage
owner, which refuses a dataset opened under a namespace it is not bound to. The namespace was read from
`candidate-receipt.json` **alone** — which a *candidate* half has, because an admission wrote it, and a
**before** half placed from a named `--baseline` never does, because a published dataset is not an
admitted candidate and carries `baseline-generation.json` instead. The read therefore fell back to the
requested repository name while the bytes are bound to a namespace id, and **every leaf on the ordinary
continuity route produced a comparison that could not be frozen** (refused `candidate_dataset_absent`).
`test_the_placed_baseline_is_opened_under_its_own_recorded_namespace` (`:329-370`) drives the real
placed-baseline journey, asserts that the requested repository and the dataset's own namespace differ
(so the case cannot pass vacuously), and then opens the half under `review_namespace` and reads its own
snapshot identity back. It **bites**: reverted in a scratch copy of the module, it fails with
`+ agents-remember`, the exact value that produced the refusal.

Every case drives the **shipped CLI as a real process** on a real enclosure, so nothing here injects a
preconstructed report or a hand-built payload:

- **two successful writes over one shared path** keep the dataset the comparison was opened on, while
  the second write still lands — its publication identity and the entry it committed both move;
- **an exact retry and a refused changed retry** leave that dataset byte-identical, which is the
  packet's own boundary example;
- **a deliberate rebase** begins a new generation whose record names the generation it replaced *and*
  that generation's exact dataset identity, and whose id a reader can recompute from those facts;
- **a placed baseline is opened under its own recorded namespace**, which is what lets the comparison
  the run opened be recorded at all (leaf `260921-ICR-L34`).

This module **owns the journey fixtures**: `_opened_comparison` builds the state every case starts
from, and `test_knowledge_ingest_failure_windows.py` imports `_digest`, `_identity_of` and
`_publish_a_later_line` from here rather than copying them, because the successful journey is what they
were written for. It registers **no artifact and no contract of its own** — its catalog footprint is
one lane row and two `consumer_scope = "exact"` consumer rows on artifacts
`mcp/tests/snapshot_lifecycle_test_support.py` already names.

## Code Commentary

### Logic

**The fixtures build a live leaf whose comparison is *already open*, because that is the state the
defect appears in.** `_opened_comparison` (`:115-147`) composes shipping owners only: `_private_pair`
and `_cycle01_sibling_contract` (both from the ingest-list fixture module) build the enclosure,
`_cycle01_publish_baseline` publishes one real dataset on the repository's line, the fork point is a
`shutil.copyfile` of that publication, and the first CLI run is driven through `_cli_json` over
`_fork_ingest_argv`. The returned tuple is the fixture pair, the shared baseline/publication path, the
enclosure, the candidate directory, the review's before half and the opening run's report — the
comparison is open, the leaf's line has published over the fork point it forked from, and the next run
is handed those published bytes as its baseline.

**`_publish_a_later_line` is the repository's line moving on, driven through the application owner
rather than the CLI.** (`:80-112`.) A CLI run would fill *this* leaf's before half on the way, which
is exactly the state each case has to set up deliberately, so the later publication goes through
`ingest_curator_list` with an `IngestSelection` naming `IngestPublication(destination_path, expected_destination)`
directly, and the case asserts the batch reported `changed` and published an identity before using it.

**The two measurement helpers keep bytes and identity apart on purpose.** `_digest` (`:68-71`) is the
sha256 of a file's bytes — the "did the half move at all" fact — while `_identity_of` (`:74-77`) reads
a dataset's own logical identity through the shipped `dataset_identity`. The cases need both: one
proves the half is byte-identical, the other proves it still *is* the original dataset while the shared
path holds the update.

**The three cases, and the fact each one owns.**

- `test_a_second_successful_ingest_over_one_path_keeps_the_original_baseline` (`:150-206`) measures
  four facts and the fourth is the defect: the second write lands (its entry commits and the published
  identity moves), the before half is byte-identical to the fork point, its dataset identity is still
  the original baseline's while the shared path holds the update, and the report says which generation
  stands there and how a deliberate rebase would replace it. This is the packet's non-conforming
  example read as a regression: it fails on the base implementation.
- `test_an_exact_retry_and_a_refused_changed_retry_keep_the_original_baseline` (`:209-257`) drives the
  two retries the packet names as its boundary example: the exact retry repeats an operation that
  already committed, so it writes no new row and must restate nothing; the changed retry wears the same
  entry id with a different statement and is correctly refused as a conflict
  (`allocation_content_conflict`) — and a refusal must not become a second way to move the before side
  either.
- `test_a_deliberate_rebase_begins_a_recorded_generation_with_explicit_lineage` (`:260-323`) measures
  the one act that *may* replace a standing baseline: the report names both generations, the half holds
  the new baseline's bytes, the record's lineage is the old generation's id **and** its dataset
  identity, and the record's own id is the one its recorded facts derive via `generation_identity`.

**Every way a placement *fails* is measured beside this module**, not here:
`test_knowledge_ingest_failure_windows.py` owns the adopted half, the damaged record, the obstructed
record path, the two separately-failing legs, the two post-rename flush windows, the rebase-flag
refusal and the write-site precondition. The split is an extraction, not a subject boundary: the F3
cases pushed this module to 901 lines — one over the repository's 900-line soft rail — and the
repository's rule is to clear that by extraction rather than growth.

### Conventions

The module is a `pytest.mark.evidence_unit` ordinary unit-regression module (its lane row lives in
`mcp/tests/test-evidence-lanes.toml` under `unit-regression`). It imports downward into
`application.knowledge_baseline_generation` and `application.knowledge_curator_ingest`, and sideways
into the ingest-list fixture module and `snapshot_lifecycle_test_support`; it introduces no third
support module. Its name deliberately avoids the governance policy's task-shaped-proof token, so it
needs no pinned lifecycle-catalog artifact row for what is a plain unit module.

### Invariants And Boundaries

- **The CLI is the surface under test.** Every case runs the shipped entry point as its own process;
  no case asserts a returned prebuilt payload in place of the production composition.
- **The shared path is the point.** `--baseline` and `--publish-to` name one path in runs 1–4, because
  that path *is* the leaf's line.
- **The half is measured in bytes *and* in identity.** A byte-identical half whose identity had
  changed would still be the wrong before side, and vice versa.
- **Boundary.** This module owns the successful path and its fixtures only; the failure surface, the
  review's own rendering of a rebased pair, and any retention contract for the superseded dataset's
  bytes belong to other modules and other leaves.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` in the memory
layer reads "No entries configured yet", so it carries no `Domain Documentation` category). The
statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Ranges are the exact construct extents in this candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the defect, the three successful-path facts it measures, and where the failure surface lives. | "The defect these cases seal (ICR-R18, A21)"; "two successful writes over one shared path" | mcp/tests/test_knowledge_ingest_comparison_generation.py:1-26 |
| The shared-path journey fixture every case starts from, built from shipping owners only. | `_opened_comparison` | mcp/tests/test_knowledge_ingest_comparison_generation.py:118-150 |
| **The repository's line moving on, driven through the application owner because a CLI run would fill this leaf's half on the way.** | `_publish_a_later_line` | mcp/tests/test_knowledge_ingest_comparison_generation.py:83-115 |
| The two measurement helpers: the bytes at a path, and the dataset's own logical identity. | `_digest`; `_identity_of` | mcp/tests/test_knowledge_ingest_comparison_generation.py:71-74; mcp/tests/test_knowledge_ingest_comparison_generation.py:77-80 |
| **The packet's non-conforming example as a regression: the second successful write lands while the before half stays byte-identical to the fork point and still holds the original identity.** | `test_a_second_successful_ingest_over_one_path_keeps_the_original_baseline` | mcp/tests/test_knowledge_ingest_comparison_generation.py:153-209 |
| **The packet's boundary example: an exact retry restates nothing and a refused changed retry is not a second way to move the before side.** | `test_an_exact_retry_and_a_refused_changed_retry_keep_the_original_baseline` | mcp/tests/test_knowledge_ingest_comparison_generation.py:212-260 |
| **The one act allowed to replace a standing baseline, measured as lineage by id and by exact dataset identity, plus an id the reader can recompute.** | `test_a_deliberate_rebase_begins_a_recorded_generation_with_explicit_lineage` | mcp/tests/test_knowledge_ingest_comparison_generation.py:263-326 |
| **The case `260921-ICR-L34` added: the half a `--baseline` run placed is opened under the namespace its own `baseline-generation.json` names, which is what makes the comparison recordable at all — and it bites when the receipt-only read is restored.** | `test_the_placed_baseline_is_opened_under_its_own_recorded_namespace`; `review_namespace`; `read_baseline_generation`; `open_read_only_store` | mcp/tests/test_knowledge_ingest_comparison_generation.py:329-370 |
| The generation id the rebase case recomputes and the record reader it compares against. | `generation_identity`; `read_baseline_generation` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:319-348; mcp/src/agents_remember/application/knowledge_baseline_generation.py:285-316 |
| The publication owner and selection this module drives the later line through. | `ingest_curator_list`; `IngestSelection`; `IngestPublication` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1074-1088; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1091-1108; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1111-1235; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1015-1031; mcp/src/agents_remember/application/knowledge_curator_ingest.py:998-1011 |
| The shipped reader the identity helper uses. | `dataset_identity` | mcp/src/agents_remember/memory/knowledge/logical.py:153-175 |
| The identity value the identity helper answers with. | `SnapshotIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:195-204 |
| **The journey fixtures this module owns and the failure-window module imports rather than copies.** | `_digest`; `_identity_of`; `_publish_a_later_line` | mcp/tests/test_knowledge_ingest_failure_windows.py:71-75; mcp/tests/test_knowledge_ingest_failure_windows.py:80-119 |
| The ingest-list fixture module every one of these cases builds its enclosure from. | `SourcePair`; `_private_pair`; `_cycle01_sibling_contract`; `_cycle01_publish_baseline`; `_fork_ingest_argv`; `_review_before_half`; `_one_entry_list`; `_cli_json` | mcp/tests/test_knowledge_curator_ingest_list.py:165-179; mcp/tests/test_knowledge_curator_ingest_list.py:1723-1733; mcp/tests/test_knowledge_curator_ingest_list.py:3127-3141; mcp/tests/test_knowledge_curator_ingest_list.py:3144-3167; mcp/tests/test_knowledge_curator_ingest_list.py:1761-1789; mcp/tests/test_knowledge_curator_ingest_list.py:1667-1680; mcp/tests/test_knowledge_curator_ingest_list.py:1700-1720; mcp/tests/test_knowledge_curator_ingest_list.py:1659-1664 |
| The lane row that makes these cases ordinary unit-regression evidence, and the run budget they are counted against. | "unit-regression"; "mcp/tests/test_knowledge_ingest_comparison_generation.py" | mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:95-95 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every enclosure, dataset and publication it
builds is local to one temporary coordination root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-25T22:30:00+02:00 — 260921-ICR-L34 curator (leaf `260921-ICR-L34`, uncommitted change set on `ar/260921-icr-l34-ar`, code base `a9a1a41bba535803421470bd17d858657177cb5f` plus the working-tree delta): **body update — the module gains a fourth case, and it protects the second half of the journey these three measure.** `test_the_placed_baseline_is_opened_under_its_own_recorded_namespace` (`:329-370`) drives the real placed-baseline journey and asserts that the requested repository and the dataset's own namespace differ before it opens the half under `review_namespace` and reads its snapshot identity back; the defect it seals is that the namespace was read from `candidate-receipt.json` alone, which a before half placed from a named `--baseline` never has — so every leaf on the ordinary continuity route produced a comparison that could not be frozen, refused `candidate_dataset_absent`, invisibly (the fixtures hand-assemble their pairs and the first-generation path leaves a receipt). This **is** the body update the external-memory refresh asks for, not a metadata refresh: the Purpose now states the fourth fact and its consequence, the case list gained its fourth bullet, and a reference row carries the case and the owners it names. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **citation repair only, forced by this leaf's own moves in the files this card cites.** The source file this card documents did **not** change; the ranges that moved belong to the leaf's other edits — this leaf appended one row to `mcp/tests/test-evidence-lanes.toml` at `:89`, so this module's own `unit-regression` row moved `:125` → `:87` in that manifest. Each row was re-read against the construct it names and its range re-derived from that construct's own extent in the moved file rather than shifted by a remembered delta. No claim was re-worded, no anchor was renamed and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.

- 2026-09-21T15:35+02:00 — 260921-ICR-L18 curator (uncommitted change set on `ar/260921-icr-l18`, code base `0fca5c69766aa95eebe950c19fbcdc83864ec35a`): created this one-to-one card for the new module, which is the production-composition evidence for `ICR-R18@v1`'s conforming and boundary examples. The card records the defect the cases seal (one path named for both `--baseline` and `--publish-to`, so the second successful write re-placed the half from what by then *were* the first run's published bytes), the state the shared fixture sets up, the two measurement helpers' deliberate split between bytes and identity, and the fact each of the three cases owns. It also records the two things a reader would otherwise have to infer: this module **owns the journey fixtures** that the failure-window module imports rather than copies, and it registers **no artifact and no contract of its own** — one lane row plus two consumer rows on artifacts the existing support module already names. The failure surface is documented as living beside this module, and the split is recorded as an extraction forced by the repository's 900-line soft rail rather than as a subject boundary. **Verification metadata:** the card names the production line it was read against — `0fca5c69766aa95eebe950c19fbcdc83864ec35a`, this leaf's base — because every construct it cites exists only in this leaf's uncommitted candidate. The governed closeout's own metadata refresh re-stamps it against the code commit its transaction creates.
