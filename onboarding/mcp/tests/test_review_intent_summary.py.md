# mcp/tests/test_review_intent_summary.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The executable pin for the changed-intent summary behind the compact `Intent review +N −N` entry
(`ICR-R24@v3`, leaf `260921-ICR-L47`). Six cases build real knowledge snapshots through the shipped
write operations and read them through the real
[`review_intent_summary`](../src/agents_remember/application/review_intent_summary.py.md) and its
route, so every count class and every answer state is measured rather than asserted from a mock.

## Code Commentary

### Logic

- `_shared_base` authors a common ancestor (`A` shared by two families, `B`, `D` realized once,
  families `F1 {A, B}` and `F2 {A, D}`); `_extend` copies it to an after side; `_resolution` builds the
  `ReviewCandidateResolution` the summary reads.
- **Counts:** added, revised and removed statements and guarantees are `+`/`−`; realization-only and
  membership-only changes are typed apart (+3 −4, realization_only 1, membership_only 1). A revised
  member shared by two families counts once on each side.
- **Record-only successors (L47-R1-F3):** a status-only invariant successor and a version-only family
  successor each count (1, 1); a same-guarantee successor with a new member stays `membership_only`.
- **States:** divergent successors make the answer `partial`; an absent candidate dataset is
  `unavailable` with its refusal and no counts; the route answers every typed state with 200 and an
  unwired process with 503.

### Conventions

Registered in the `unit-regression` lane of `test-evidence-lanes.toml` (an unregistered test file is
refused by the lane gate). It uses local constants rather than the exact-consumer
`read_scope_test_support` module, which would have made it a consumer of that support (worker event
E2). The module docstring states the route's status idiom (review F6).

### Invariants And Boundaries

The fixture drives the shipped writers only; it does not hand-edit SQLite. A revert of the F3 rule
(`review_intent_summary.py` at A1) fails the record-only case (`assert (0, 0) == (1, 1)`, review R2).

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this test module.

No relevant domain documentation was found.

### Repo-Internal References

- The shared ancestor the count cases extend. [1]
- Added/revised/removed as +/−, relationship-only as typed counts. [2]
- A shared revised member counts once per side. [3]
- Record-only successors count; a same-guarantee member change stays typed. [4]
- Divergent heads are `partial`. [5]
- Absent knowledge is `unavailable`, never zero. [6]
- 200 for every typed state, 503 unwired. [7]
- The lane registration. [8]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
