# mcp/tests/test_read_anchor_memo.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The executable pin for the anchor-observation memo (`260921-ICR-L56`, ICR-R24@v3): the process-lifetime
tables in [`read_anchor_memo.py`](../src/agents_remember/memory/knowledge/read_anchor_memo.py.md) and the
owner that fills them, [`read_anchors.py`](../src/agents_remember/memory/knowledge/read_anchors.py.md).
The repository cases use real Git to compare answers and reads, exercise transient failures and
availability changes, and check isolation. A separate in-memory case checks the eviction bound.

## Code Commentary

The byte memo case charges both the key and the value, evicts by least recent use and skips oversized entries. The request ownership case shares owners with a joined thread, isolates concurrent scopes and checks that copied scope state is clear at exit.

### Logic

- **Fixtures.** `tree` writes one parsed module (a constant, a class with a method, a function) and one
  text file as a real tree object; `git_calls` and `parses` spy on the owner's `run_git` and on
  `extents.definitions` while delegating to the real ones; the autouse `_forgotten` empties all three
  tables before and after every case. `_claims` builds the case’s observed outcomes (symbols, a
  qualified name, an invented name, a file, an in-range and a past-the-end line range, an absent path and
  a mismatched blob); `_observe` builds a fresh `_TreeAnchorResolver` per pass;
  `_unremembered` empties the tables before each observation to reproduce the path before the memo.
- **Same answers, one read per object.** A remembered pass equals the unremembered one; a repeat pass runs
  only the per-resolver `--no-replace-objects rev-parse --verify --quiet <tree>^{tree}` probe; the first pass runs one `ls-tree` per distinct path (the
  absent one too), one blob read per distinct blob and one parse.
- **Failures are asked again.** A runner that fails each Git question once shows the probe, the lookup
  and the blob read each asked again and only the success remembered.
- **Abbreviations are never remembered**, and `is_complete_object_id` refuses an abbreviation, `HEAD`,
  upper case and a trailing newline.
- **The bound.** Weight, not count, bounds the table; a read refreshes recency; an oversized value is
  refused; an overwrite replaces its weight; a remembered empty answer is a hit; at 100 and 20,000
  inserts only the newest entries remain. Eight threads with a shortened switch interval all get the
  serial answer. In that concurrent case a separate weighted memo stays within its bound.
- **Availability is never remembered** (the review L56-R1-F1 regression, parametrised `pruned` /
  `revoked`): after warming the memo in the repository and in an alternates borrower, the tree is released
  and pruned or the alternate revoked, and a fresh resolver must report `recorded_object_unavailable` for
  every anchor with no ranges.
- **No cross-repository or cross-grammar reuse** (review L56-R1-F2): an empty neighbour observed without a
  resolver fails its lookup instead of receiving the first repository's entry; a blobless neighbour
  holding only the trees preserves exact_recorded_blob for the range with no resolved ranges, and reports unsupported_locator for the symbol rather than answering from the first repository's
  lines; one blob at `a.py` and `a.ts` resolves `x` only under Python and `g` only under TypeScript, in
  either order.

### Conventions

Registered in the `unit-regression` lane of `test-evidence-lanes.toml` (an unregistered test file is
refused by the lane gate). The fixture’s `_git` helper supplies `GIT_CONFIG_NOSYSTEM=1` and uses
the fixture repository as `HOME`. The observation spies delegate to the production Git and parser
runners. `_claim` gives every claim a fresh uuid `anchor_id`, so cases that build claims
separately compare resolutions and ranges rather than whole observations (worker event E2). Eight test
functions, one parametrised twice, make the nine cases.

### Invariants And Boundaries

The repository cases drive the shipped owner and the real Git binary. The counting spies delegate and the transient-failure case injects the first failure for each Git operation before delegating the successful calls.

The earlier card at memory snapshot `81cfe4a8` recorded this review evidence:

> The availability and isolation cases fail on the first attempt's code
> (A1, which remembered positive tree probes), and the reviewer's mutants R2–R4 are killed by this module
> alone (review R2).

This is retained A1/review-R2 context, not a new execution or mutation result for the current candidate.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this test module.

No relevant domain documentation was found.

### Repo-Internal References


### Cross-Repo References

The tests exercise cache isolation between temporary repositories, including an alternates borrower and empty or blobless neighbours; they establish no external managed-repository protocol.

No meaningful cross-repo references found.

### Repo-Internal References (continued)

- The real repository, the Git and parser spies, and the per-case emptied tables. [1]
- The fixture builds symbol, file, range, absent-path and blob-mismatch cases. Each pass creates a fresh resolver. The baseline clears all three memos before each observation. [2]
- The repeated pass returns identical observations and makes one availability probe. The first pass looks up each of three paths once, reads two blobs and parses the Python module once. [3]
- A failed probe, lookup or blob read is asked again; only the success is remembered.  Anchor: "test_a_failure_is_never_remembered_and_the_later_success_is_observed" [4]
- An abbreviated id is never remembered; the admission test's refusals.  Anchor: "test_a_question_asked_with_an_abbreviated_tree_id_is_never_remembered" [5]

- The named cases check weight-bounded LRU eviction, oversized-value refusal and the same bound during concurrent access. [6]

- **A pruned or revoked tree reported unavailable for every anchor, not answered from memory.**  Anchor: "test_a_tree_that_stops_being_available_is_reported_unavailable_not_remembered" [7]
- The empty and blobless neighbors cannot receive another repository’s cached tree or content answers. The same blob under Python and TypeScript paths resolves the expected symbols in both query orders. [8]


- The unit-regression lane selects mcp/tests/test_read_anchor_memo.py. [9]
