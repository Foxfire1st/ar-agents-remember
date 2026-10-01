# mcp/tests/test_knowledge_ingest_failure_windows.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` in the memory
layer reads "No entries configured yet", so it carries no `Domain Documentation` category). The
statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Ranges are the exact construct extents in this candidate.

- The module's own statement of the two failure halves it measures, the five windows, and where the successful path lives. [1]
- **The fixture the whole failure surface starts from: a half placed before generation records existed, with the published dataset it is a copy of.** [2]
- **The fault injection that makes a leg fail after its bytes landed: the kernel owner's post-rename flush, for one directory and nothing else.** [3]
- **An adopted half is the comparison's baseline, never an empty slot a later run may fill.** [4]
- **A record that disagrees with its bytes is named damage, and nothing is placed over it — not even by an explicit rebase.** [5]
- **The invocation refusal: the rebase action without the dataset it rebases onto.** [6]
- **The write site's own precondition, moved here with the owner it measures.** [7]
- **Verification F1: a blocked record leg cannot lose the original, and a following run still reports the true original as the standing baseline.** [8]
- **The one window a record-first rebase can leave: the previous bytes beside a record that disagrees with them.** [9]
- **Verification C2: an obstructed record path is damage, never an absent record.** [10]
- **Verification F3, record leg: the clause says only "did not report success" and the read-back names what landed.** [11]
- **Verification F3, dataset leg: the bytes are on disk, so "was not replaced" would be a claim the caller never measured.** [12]
- **The production reader and the two publication legs these cases drive to failure.** [13]
- The production entry points and values the direct cases use instead of the CLI: the placement decision, the first placement, the bytes-read-as-dataset read, the record writer and the derived id. [14]
- The kernel write the dataset leg fails at, and the flush the fault injection patches. [15]
- The CLI entry point every CLI-driven case runs. [16]
- The shipped builders for a real dataset the write-site case publishes. [17]
- The journey fixtures this module imports rather than copies. [18]
- The enclosure and CLI fixture helpers this module imports from the ingest-list module. [19]
- The note left where the moved write-site case stood, and the case's own statement of the precondition it measures. The note's own text names `test_knowledge_ingest_comparison_generation.py` as the destination, but the case actually lives **here** — the failure surface was extracted out of that module after the note was written, and the case travelled with it. Recorded here as the fact, with the note's stale destination named rather than silently reconciled. [20]
- The note left where the moved write-site case stood. Its own text names `test_knowledge_ingest_comparison_generation.py` as the destination, but the case actually lives **here** — the failure surface was extracted out of that module after the note was written, and the case travelled with it. Recorded here as the fact, with the note's stale destination named rather than silently reconciled. [21]
- The dataset name the write-site case asserts against. [22]
- The lane row that makes these cases ordinary unit-regression evidence. [23]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every enclosure and dataset it builds is
local to one temporary coordination root.

No meaningful cross-repo references found.
