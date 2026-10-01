# test_review_state.py

## Governing Overview

[tests/overview.md](overview.md)

## Purpose

Focused R27/R28 tests for the persisted fixed-list review state, ordinary three-round cap, and
direct recorded developer-permission transition.

## Code Commentary

### Logic

The fixture builds a minimal `TaskDocument` without `reviewState`, proving that missing state is
accepted as zero. The missing-state and explicit-zero tests then start round one and make the
pending bit observable; replaying a pending begin is idempotent.

The baseline test seals two findings on a blocking result, then verifies successor rounds advance
to rounds two and three while retaining the baseline and shrinking remaining IDs to an empty list.
The successor-refusal test rejects new IDs, duplicate IDs, and passing results with unresolved IDs.
The final R27 test accepts recording without `begin_task_review` as the baseline and rejects a
result without a valid verdict. The cap tests refuse a fourth ordinary round with an actionable
count, accept one
direct recorded developer approval only at exhaustion, accumulate a second allowance without
resetting the sealed issue list, and leave exhausted state unchanged for malformed permission
payloads.

### Conventions

This is implementation preparation evidence. The R27 worker report records the original state
checks and identity tests; the L41 report records the cap and direct-permission checks, plus the
32-test focused run and static checks. This card does not elevate those results to independent
review or acceptance. The tests exercise recorded permission fields only; they do not authenticate
the purported developer.

### Invariants And Boundaries

- Tests preserve the small state model: missing/zero state, pending admission, sealed baseline and
  monotonic remaining IDs.
- They preserve the ordinary three-round ceiling, cumulative explicit allowances, and pending
  replay idempotence.
- They do not prove authentication, human authorship, or integration review.

## Evidence

### Docs References

No external Domain Documentation source governs these repository-owned tests.

No configured external source applies.

### Repo-Internal References

- Missing/zero state starts round one and pending replay is idempotent. [1]
- Baseline sealing and successor rounds only shrink remaining IDs. [2]
- Successors reject new, duplicate, reintroduced and unresolved passing IDs. [3]
- Recording without begin starts the baseline and still requires a valid verdict. [4]
- Ordinary exhaustion refuses a fourth round with count and limit. [5]
- A direct developer permission adds cumulative rounds only after exhaustion and preserves findings. [6]
- Malformed permission payloads leave exhausted state unchanged. [7]

## Source File Binding

The current L41 source bytes are SHA-256
`b007e8ec8440b0aca8f7897f86108c982ec33e9c03e7517240993282874f5212`
(`7707` bytes, `209` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.
