# mcp/tests/test_knowledge_ingest_failure_windows.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_ingest_failure_windows.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:43:38+00:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047` |
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**Every way a placement can fail without losing the baseline a comparison was opened on** — the
other half of `ICR-R18@v1`'s failure-and-recovery clause, and the regression surface for the two
defects the leaf's verification rounds found. The refused-rerun repair (`260915-KS-L47`) covered one
path; the successful-update path is
[`test_knowledge_ingest_comparison_generation.py`](test_knowledge_ingest_comparison_generation.py.md)'s.
What remains is what a *refused* placement does to a half that already holds the comparison's
original baseline — the state every leaf that ingested before the generation record existed is in —
and what the two legs of one placement do to it when they fail separately.

Nine cases, each driven through the shipped CLI on a real enclosure unless the state is a property of
the half rather than of any invocation:

- an **adopted** half (a dataset placed before generation records existed) is *kept*, not treated as an
  empty slot a later run may fill;
- a **record that disagrees with its bytes**, and a **record path occupied** by something that is not a
  record file, are both named damage — never "this half records no generation";
- **`--rebase-baseline` without `--baseline`** names no generation to begin from and is refused by
  name before the contract or the list is read;
- the **write site's own precondition** — only bytes that read as a dataset of this code — refuses a
  corrupt fork point by name and leaves nothing behind (this case moved here from the ingest-list
  module with the placement owner it measures);
- a **rebase whose record leg fails** leaves the half byte-identical, because the record is durable
  before the bytes it names;
- a **rebase whose dataset leg fails after the record landed** leaves the previous bytes beside a
  record that disagrees with them — the named `damaged` state, and the one window the ordering still
  leaves;
- a leg whose **directory flush fails after its bytes landed** is reported as "did not report success",
  because it has not measured that they are absent — the report's appended read-back, carrying the
  dataset identity actually on disk, is what states what landed.

It registers **no artifact and no contract of its own**: it imports the journey fixtures from the
comparison-generation module and the enclosure builders from the ingest-list fixture module, so its
catalog footprint is one lane row and two `consumer_scope = "exact"` consumer rows on artifacts
`mcp/tests/snapshot_lifecycle_test_support.py` already names.

## Code Commentary

### Logic

**`_adopted_half` is the fixture the failure surface starts from, and it is deliberately *not* a
recorded generation.** (`:80-100`.) It returns the enclosure, the half's dataset path, the fixture
pair, the *published* dataset the half's bytes are a copy of, and that dataset's identity. A half in
this state — no record beside the bytes — is what every leaf that ingested before this record existed
holds, and it is the state an implementation is most likely to get wrong: a dataset with no record is
not an empty slot, it is the dataset this comparison was opened on.

**`_fail_the_directory_flush` is the fault injection that makes the F3 wording measurable.** It makes
the kernel owner's post-rename flush fail for one directory and nothing else, so the failure arrives
*after* the bytes are already on disk: the leg never returned success and the bytes are there anyway.
That is the window the leg wording has to describe honestly, and it is why both leg clauses say "did
not report success" rather than "was not written" / "was not replaced".

**The nine cases and the exact fact each one falsifies.**

| Case | Range | What it pins |
| --- | --- | --- |
| `test_a_half_that_records_no_generation_keeps_its_baseline_as_the_original` | `:122-166` | An adopted half is the comparison's baseline, not an empty slot: a differing baseline places nothing, names the unrecorded state and the rebase action, and reports the half's derived generation id. |
| `test_a_recorded_generation_that_disagrees_with_its_bytes_is_named_not_trusted` | `:169-224` | A record that does not match its bytes is damage, nothing is placed over it — not even by an explicit `rebase=True` — and the state is a property of the half, so both halves of the answer are measured without a CLI run. |
| `test_a_rebase_without_a_baseline_is_refused_before_anything_is_read` | `:227-260` | The action without the dataset states nothing to transition from; exit 2, by name, demonstrated by an absent contract path. |
| `test_the_write_site_publishes_only_bytes_that_read_as_a_dataset` | `:263-318` | The write site's own precondition: non-dataset bytes refused by name with nothing left behind, and a real dataset published with the record that names its generation, then kept as it is by the run that follows. Moved here from `test_knowledge_curator_ingest_list.py` with the owner it measures. |
| `test_a_rebase_whose_record_leg_fails_leaves_the_original_baseline_in_place` | `:321-395` | **Verification F1.** The record is durable before the bytes it names, so a blocked record cannot lose the original: the run reports the record leg and claims no generation; the half still holds the pre-rebase bytes byte-for-byte with the original identity; no record appeared; and a following run handed the true original reports it as the standing baseline (`present:`) instead of being told the replacement is it. |
| `test_a_rebase_whose_dataset_leg_fails_names_the_damage_it_left` | `:398-476` | The one window a record-first rebase can leave: the previous bytes beside a foreign record, named as damage, never the replacement with no record. The dataset leg is made to fail at the kernel write every placement goes through and only for the half's dataset path, so the run's own commit and publication still land and the case measures the placement leg and nothing else. |
| `test_an_obstructed_generation_record_path_is_damage_and_not_an_absent_record` | `:479-525` | **Verification C2.** A directory left where the record belongs must not read as "this half records no generation" — that reading adopts whatever bytes are beside it and lets the obstruction stay invisible. Both the reader and the CLI answer are measured. |
| `test_a_record_leg_whose_flush_fails_reports_no_success_and_the_read_back_says_what_landed` | `:528-585` | **Verification F3.** A clause reading "was not written" would contradict the read-back beside it — the half reads `damaged` precisely *because* the record landed and names bytes the dataset does not hold — so the leg says only what it measured and the read-back carries the outcome. |
| `test_a_dataset_leg_whose_flush_fails_reports_no_success_while_the_bytes_are_present` | `:588-631` | **Verification F3.** Same window, the other leg, from an *empty* half: the bytes are on disk, so "was not replaced" would be false; the read-back reports the half as `adopted` and names the identity it now holds. |

**The failure orders are the module's real subject.** A rebase runs its record leg first and a first
placement runs its dataset leg first, and the cases exist to prove that each order leaves only the
window it is supposed to leave. The two assertions in the F3 cases are deliberately the *negation* of
the old wording — the case fails if the report claims the bytes are absent — because the defect was a
line that named a byte outcome it had never measured.

### Conventions

A `pytest.mark.evidence_unit` ordinary unit-regression module whose lane row lives in
`mcp/tests/test-evidence-lanes.toml` under `unit-regression`. It imports downward into
`application.knowledge_baseline_generation` and `cli.__main__`, and sideways into
`test_knowledge_ingest_comparison_generation` (the journey fixtures), the ingest-list fixture module
and `snapshot_lifecycle_test_support` (`build_case`, `create` — the shipped builders for a real
dataset). It introduces no third support module. Its name deliberately avoids the governance policy's
task-shaped-proof token, so it needs no pinned lifecycle-catalog artifact row.

### Invariants And Boundaries

- **No window may leave a half reading `adopted` over bytes that are not the captured baseline.** That
  single invariant is what the five windows and the two F3 cases together assert.
- **A failure line states what it measured.** The leg names itself; the appended read-back names the
  state and the dataset identity actually on disk; neither claims the other's fact.
- **Fault injection is at the shipped boundary.** `_fail_the_directory_flush` patches the kernel
  owner's flush, and the dataset-leg case makes the kernel write fail only for the half's dataset
  path, so the run's own commit and publication still land.
- **Boundary.** This module owns the failure surface only; the successful path and its fixtures belong
  to the comparison-generation module, and the review's own behaviour on a rebased pair belongs to the
  review leaves.

### Todos

None recorded. The CLI's lack of a lock between two concurrent ingests is a known, deliberately
unfixed condition recorded with the production module rather than here; the failure mode is bounded
because a record-first rebase cannot leave replacement bytes with no record, so an interleaving ends in
one of the named readings rather than a silent swap.

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
| The module's own statement of the two failure halves it measures, the five windows, and where the successful path lives. | "Five windows are measured"; "an **adopted** half" | mcp/tests/test_knowledge_ingest_failure_windows.py:1-29 |
| **The fixture the whole failure surface starts from: a half placed before generation records existed, with the published dataset it is a copy of.** | `_adopted_half` | mcp/tests/test_knowledge_ingest_failure_windows.py:80-100 |
| **The fault injection that makes a leg fail after its bytes landed: the kernel owner's post-rename flush, for one directory and nothing else.** | `_fail_the_directory_flush` | mcp/tests/test_knowledge_ingest_failure_windows.py:103-119 |
| **An adopted half is the comparison's baseline, never an empty slot a later run may fill.** | `test_a_half_that_records_no_generation_keeps_its_baseline_as_the_original` | mcp/tests/test_knowledge_ingest_failure_windows.py:122-166 |
| **A record that disagrees with its bytes is named damage, and nothing is placed over it — not even by an explicit rebase.** | `test_a_recorded_generation_that_disagrees_with_its_bytes_is_named_not_trusted` | mcp/tests/test_knowledge_ingest_failure_windows.py:169-224 |
| **The invocation refusal: the rebase action without the dataset it rebases onto.** | `test_a_rebase_without_a_baseline_is_refused_before_anything_is_read` | mcp/tests/test_knowledge_ingest_failure_windows.py:227-260 |
| **The write site's own precondition, moved here with the owner it measures.** | `test_the_write_site_publishes_only_bytes_that_read_as_a_dataset` | mcp/tests/test_knowledge_ingest_failure_windows.py:263-318 |
| **Verification F1: a blocked record leg cannot lose the original, and a following run still reports the true original as the standing baseline.** | `test_a_rebase_whose_record_leg_fails_leaves_the_original_baseline_in_place` | mcp/tests/test_knowledge_ingest_failure_windows.py:321-395 |
| **The one window a record-first rebase can leave: the previous bytes beside a record that disagrees with them.** | `test_a_rebase_whose_dataset_leg_fails_names_the_damage_it_left` | mcp/tests/test_knowledge_ingest_failure_windows.py:398-476 |
| **Verification C2: an obstructed record path is damage, never an absent record.** | `test_an_obstructed_generation_record_path_is_damage_and_not_an_absent_record` | mcp/tests/test_knowledge_ingest_failure_windows.py:479-525 |
| **Verification F3, record leg: the clause says only "did not report success" and the read-back names what landed.** | `test_a_record_leg_whose_flush_fails_reports_no_success_and_the_read_back_says_what_landed` | mcp/tests/test_knowledge_ingest_failure_windows.py:528-585 |
| **Verification F3, dataset leg: the bytes are on disk, so "was not replaced" would be a claim the caller never measured.** | `test_a_dataset_leg_whose_flush_fails_reports_no_success_while_the_bytes_are_present` | mcp/tests/test_knowledge_ingest_failure_windows.py:588-631 |
| **The production reader and the two publication legs these cases drive to failure.** | `read_standing_generation`; `_publish_generation`; `_publish_dataset_leg`; `_publish_record_leg`; `_failed_placement` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:354-373; mcp/src/agents_remember/application/knowledge_baseline_generation.py:660-696; mcp/src/agents_remember/application/knowledge_baseline_generation.py:699-712; mcp/src/agents_remember/application/knowledge_baseline_generation.py:715-738; mcp/src/agents_remember/application/knowledge_baseline_generation.py:741-760 |
| The production entry points and values the direct cases use instead of the CLI: the placement decision, the first placement, the bytes-read-as-dataset read, the record writer and the derived id. | `fill_admitted_before_half`; `place_original_baseline`; `read_admitted_baseline`; `write_baseline_generation`; `generation_identity`; `BaselineRun`; `CapturedBaseline`; `BaselineGeneration`; `baseline_generation_path`; `BASELINE_GENERATION_NAME` | mcp/src/agents_remember/application/knowledge_baseline_generation.py:163-175; mcp/src/agents_remember/application/knowledge_baseline_generation.py:178-189; mcp/src/agents_remember/application/knowledge_baseline_generation.py:464-500; mcp/src/agents_remember/application/knowledge_baseline_generation.py:579-612; mcp/src/agents_remember/application/knowledge_baseline_generation.py:519-531; mcp/src/agents_remember/application/knowledge_baseline_generation.py:108-160; mcp/src/agents_remember/application/knowledge_baseline_generation.py:91-91; mcp/src/agents_remember/application/knowledge_baseline_generation.py:266-269; mcp/src/agents_remember/application/knowledge_baseline_generation.py:272-282; mcp/src/agents_remember/application/knowledge_baseline_generation.py:319-348 |
| The kernel write the dataset leg fails at, and the flush the fault injection patches. | `atomic_write_bytes` | mcp/src/agents_remember/kernel/atomic_write.py:53-72 |
| The CLI entry point every CLI-driven case runs. | `main` | mcp/src/agents_remember/cli/__main__.py:88-90 |
| The shipped builders for a real dataset the write-site case publishes. | `build_case`; `create` | mcp/tests/snapshot_lifecycle_test_support.py:178-205; mcp/tests/snapshot_lifecycle_test_support.py:208-211 |
| The journey fixtures this module imports rather than copies. | `_digest`; `_identity_of`; `_publish_a_later_line` | mcp/tests/test_knowledge_ingest_comparison_generation.py:71-74; mcp/tests/test_knowledge_ingest_comparison_generation.py:77-80; mcp/tests/test_knowledge_ingest_comparison_generation.py:83-115 |
| The enclosure and CLI fixture helpers this module imports from the ingest-list module. | `SourcePair`; `_private_pair`; `_cycle01_sibling_contract`; `_cycle01_publish_baseline`; `_fork_ingest_argv`; `_review_before_half`; `_one_entry_list`; `_cli_json` | mcp/tests/test_knowledge_curator_ingest_list.py:165-179; mcp/tests/test_knowledge_curator_ingest_list.py:1725-1735; mcp/tests/test_knowledge_curator_ingest_list.py:3129-3143; mcp/tests/test_knowledge_curator_ingest_list.py:3146-3169; mcp/tests/test_knowledge_curator_ingest_list.py:1763-1791; mcp/tests/test_knowledge_curator_ingest_list.py:1669-1682; mcp/tests/test_knowledge_curator_ingest_list.py:1702-1722; mcp/tests/test_knowledge_curator_ingest_list.py:1661-1666 |
| The note left where the moved write-site case stood, and the case's own statement of the precondition it measures. The note's own text names `test_knowledge_ingest_comparison_generation.py` as the destination, but the case actually lives **here** — the failure surface was extracted out of that module after the note was written, and the case travelled with it. Recorded here as the fact, with the note's stale destination named rather than silently reconciled. | "The write site's own precondition"; "the write site's own precondition" | mcp/tests/test_knowledge_curator_ingest_list.py:2404-2412; mcp/tests/test_knowledge_ingest_failure_windows.py:263-318 |
| The note left where the moved write-site case stood. Its own text names `test_knowledge_ingest_comparison_generation.py` as the destination, but the case actually lives **here** — the failure surface was extracted out of that module after the note was written, and the case travelled with it. Recorded here as the fact, with the note's stale destination named rather than silently reconciled. | "the write site's own precondition" | mcp/tests/test_knowledge_ingest_failure_windows.py:263-318 |
| The dataset name the write-site case asserts against. | `CANDIDATE_DATABASE_NAME` | mcp/src/agents_remember/models/knowledge/snapshot.py:52-52 |
| The lane row that makes these cases ordinary unit-regression evidence. | "unit-regression"; "mcp/tests/test_knowledge_ingest_failure_windows.py" | mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:104-104 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every enclosure and dataset it builds is
local to one temporary coordination root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): No content impact: citation-only re-measure. This card cites `mcp/tests/test-evidence-lanes.toml`, where MIK-R22's two `unit-regression` rows (`:99-100`) moved every later row down two lines, and `cli/__main__.py`, where the `knowledge-validate` subparser moved `main` down six lines. Ranges were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact line shift, and a per-document check then reported 0 findings. The claims were re-read and are unchanged. No verification stamp was advanced.
- 2026-09-29T05:02:20+00:00: Generated citation repair: `main` repointed to mcp/src/agents_remember/cli/__main__.py:88-90. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta): No content impact: MIK-R07 inserts one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:98`, so this card's rows citing lane lines below it were re-pointed one line down (by the installed anchor-range projection or, where it declined a multi-anchor row, by an exact one-line shift confirmed by every anchor resolving in the current file). Claim wording unchanged. No stamp advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: the lane-row citation re-measured after MIK-R21's two-line insertion into `test-evidence-lanes.toml`. Claim meaning unchanged; no stamp advanced.
- 2026-09-29T02:54:57+00:00: Generated citation repair: `main` repointed to mcp/src/agents_remember/cli/__main__.py:81-83. No content impact: mechanical anchor-range projection bound to citation source snapshot 2eb2ea9eedcea065d08ac926c00a066bf53846ee3aa35f06aeeb6a9d076a86de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`, `mcp/tests/test_knowledge_curator_ingest_list.py`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 1 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `main` repointed to mcp/src/agents_remember/cli/__main__.py:73-75. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair of a pre-existing defect this leaf did not cause.** This file is not a changed source file, and neither is `mcp/tests/test_knowledge_curator_ingest_list.py`: the row below cited that module's `:2404-2409` for the literal `"the write site's own precondition"`, which does not occur there — the note spells it `"The write site's own precondition"`, and the lowercase form the row quoted is the moved case's own docstring sentence at `mcp/tests/test_knowledge_ingest_failure_windows.py:266`. The row was re-read against the candidate and now cites both: the note's own line for the capitalised literal it actually holds, and this module's case extent `:263-318` for the lowercase one. No claim was re-worded beyond naming what each range holds, no anchor was dropped, and **no verification stamp was advanced** — the recorded stamp is kept, because the candidate is uncommitted and closeout owns the real commit.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **citation repair only, forced by this leaf's own moves in the files this card cites.** The source file this card documents did **not** change; the ranges that moved belong to the leaf's other edits — this leaf appended one row to `mcp/tests/test-evidence-lanes.toml` at `:89`, so this module's own `unit-regression` row moved `:126` → `:88` in that manifest. Each row was re-read against the construct it names and its range re-derived from that construct's own extent in the moved file rather than shifted by a remembered delta. No claim was re-worded, no anchor was renamed and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.

- 2026-09-21T15:35+02:00 — 260921-ICR-L18 curator (uncommitted change set on `ar/260921-icr-l18`, code base `0fca5c69766aa95eebe950c19fbcdc83864ec35a`): created this one-to-one card for the new module, which is the failure-and-recovery evidence for `ICR-R18@v1`. The card records the two failure halves the module's own docstring separates, the fixture the whole surface starts from (an adopted half, deliberately *not* a recorded generation), the fault injection that makes a leg fail after its bytes already landed, and a per-case table of the exact fact each of the nine cases falsifies — including the three verification rounds this leaf's own verification produced: F1 (the record-first ordering), C2 (the obstructed record path reading as damage rather than absence) and F3 (a leg clause that must say only "did not report success", pinned by the two flush cases). It records that the write-site precondition case **moved here** from the ingest-list module with the owner it measures, and that the module registers **no artifact and no contract of its own** — one lane row plus two consumer rows on artifacts the existing support module already names. It also records why the split from the comparison-generation module happened: the F3 cases pushed that module one line over the repository's 900-line soft rail, and the repository's rule is to clear that by extraction. **One code-side inaccuracy is recorded here rather than silently reconciled:** the note left where the moved case stood (`test_knowledge_curator_ingest_list.py:2404-2409`) names `test_knowledge_ingest_comparison_generation.py` as that case's destination, but the case actually lives in this module — the failure surface was extracted out of the comparison module after the note was written, and the case travelled with it. The comment text is code and not this seat's to edit; it is reported to the owning seat instead. **Verification metadata:** the card names the production line it was read against — `0fca5c69766aa95eebe950c19fbcdc83864ec35a`, this leaf's base — because every construct it cites exists only in this leaf's uncommitted candidate. The governed closeout's own metadata refresh re-stamps it against the code commit its transaction creates.
