# mcp/tests/test_read_anchor_memo.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The executable pin for the anchor-observation memo (`260921-ICR-L56`, ICR-R24@v3): the process-lifetime
tables in [`read_anchor_memo.py`](../src/agents_remember/memory/knowledge/read_anchor_memo.py.md) and the
owner that fills them, [`read_anchors.py`](../src/agents_remember/memory/knowledge/read_anchors.py.md).
Nine cases run against a **real Git repository** rather than a stub and hold the memo to the properties
that make it safe: the same answers, fewer Git reads, and nothing remembered that can change.

## Code Commentary

### Logic

- **Fixtures.** `tree` writes one parsed module (a constant, a class with a method, a function) and one
  text file as a real tree object; `git_calls` and `parses` spy on the owner's `run_git` and on
  `extents.definitions` while delegating to the real ones; the autouse `_forgotten` empties all three
  tables before and after every case. `_claims` covers every outcome the memo sits behind (symbols, a
  qualified name, an invented name, a file, an in-range and a past-the-end line range, an absent path and
  a mismatched blob); `_observe` builds a fresh `_TreeAnchorResolver` per pass, as every reader does;
  `_unremembered` empties the tables before each observation to reproduce the path before the memo.
- **Same answers, one read per object.** A remembered pass equals the unremembered one; a repeat pass runs
  only the per-resolver `cat-file -e` probe; the first pass runs one `ls-tree` per distinct path (the
  absent one too), one blob read per distinct blob and one parse.
- **Failures are asked again.** A runner that fails each Git question once shows the probe, the lookup
  and the blob read each asked again and only the success remembered.
- **Abbreviations are never remembered**, and `is_complete_object_id` refuses an abbreviation, `HEAD`,
  upper case and a trailing newline.
- **The bound.** Weight, not count, bounds the table; a read refreshes recency; an oversized value is
  refused; an overwrite replaces its weight; a remembered empty answer is a hit; at 100 and 20,000
  inserts only the newest entries remain. Eight threads with a shortened switch interval all get the
  serial answer and the table stays within its bound.
- **Availability is never remembered** (the review L56-R1-F1 regression, parametrised `pruned` /
  `revoked`): after warming the memo in the repository and in an alternates borrower, the tree is released
  and pruned or the alternate revoked, and a fresh resolver must report `recorded_object_unavailable` for
  every anchor with no ranges.
- **No cross-repository or cross-grammar reuse** (review L56-R1-F2): an empty neighbour observed without a
  resolver fails its lookup instead of receiving the first repository's entry; a blobless neighbour
  holding only the trees refuses a range and a symbol rather than answering from the first repository's
  lines; one blob at `a.py` and `a.ts` resolves `x` only under Python and `g` only under TypeScript, in
  either order.

### Conventions

Registered in the `unit-regression` lane of `test-evidence-lanes.toml` (an unregistered test file is
refused by the lane gate). Git runs with `GIT_CONFIG_NOSYSTEM=1` and a per-case `HOME`, so no host Git
configuration leaks in. `_claim` gives every claim a fresh uuid `anchor_id`, so cases that build claims
separately compare resolutions and ranges rather than whole observations (worker event E2). Eight test
functions, one parametrised twice, make the nine cases.

### Invariants And Boundaries

The cases drive the shipped owner and the real Git binary; nothing is mocked except the spies that
count calls while delegating. The availability and isolation cases fail on the first attempt's code
(A1, which remembered positive tree probes), and the reviewer's mutants R2–R4 are killed by this module
alone (review R2).

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this test module.

No relevant domain documentation was found.

### Repo-Internal References

- The real repository, the Git and parser spies, and the per-case emptied tables. [1]
- Every outcome the memo sits behind, a fresh resolver per pass, and the unremembered reference path. [2]
- Identical answers from one Git read per object and one parse per blob. [3]
- A failed probe, lookup or blob read is asked again; only the success is remembered. [4]
- An abbreviated id is never remembered; the admission test's refusals. [5]
- Weight-bounded LRU eviction, refusal of oversized values, and the concurrent bound. [6]
- **A pruned or revoked tree reported unavailable for every anchor, not answered from memory.** [7]
- **No repository's answers served for another, and one parse per grammar.** [8]
- The lane registration. [9]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
