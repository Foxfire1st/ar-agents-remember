# test_review_state.py

## Governing Overview

[tests/overview.md](overview.md)

## Purpose

Focused pure-state tests for the persisted sealed review sequence, settings-owned limit, recorded architect/developer allowances, and same-round record-only candidate binding. These tests pass settings/identity inputs directly; they do not exercise a live server or resolve repository identity themselves.

## Code Commentary

### Logic

The fixture builds a minimal `TaskDocument` without `reviewState`, proving that missing state is
accepted as zero. The missing-state and explicit-zero tests then start round one and make the
pending bit observable; replaying a pending begin is idempotent.

The baseline test seals two findings, advances through the ordinary fallback budget while preserving definitions and shrinking remaining IDs, and records a final same-round clean result using the supplied unchanged binding. Successor cases exercise rejection of new IDs, duplicate IDs and a PASS with unresolved IDs. They do not exercise reintroducing an eliminated ID; source monotonicity is a separate implementation contract. Default and explicit-limit cases prove exhaustion with count and limit; extra-round cases accumulate architect/developer allowances without resetting findings, normalize legacy developer input and keep old developerApproval records readable. Malformed approvals leave state unchanged. New cases cover same-round success, changed/unresolved/absent binding refusal, checked-tree validation, no re-sealing after a clean record, first/legacy-limit backfill and preservation of a positive stored limit.

### Conventions

This is implementation preparation evidence. The R27 worker report records the original state
checks and identity tests; the L41 report records the cap and direct-permission checks, plus the
32-test focused run and static checks. This card does not elevate those results to independent
review or acceptance. The tests exercise recorded permission fields only; they do not authenticate
the purported developer.

### Invariants And Boundaries

- Tests preserve the small state model: missing/zero state, pending admission, sealed baseline and
  monotonic remaining IDs.
- They preserve settings-budget exhaustion, cumulative recorded allowances and pending replay idempotence, not a fixed ordinary ceiling.
- They do not prove authentication, human authorship, or integration review.

## Evidence

### Docs References

No external Domain Documentation source governs these repository-owned tests.

No configured external source applies.

### Repo-Internal References


- Missing/zero state starts round one and pending replay is idempotent. [1]


- Baseline sealing and successor rounds only shrink remaining IDs. [2]


- Successor witnesses reject new and duplicate IDs and a PASS with unresolved IDs; this extent does not exercise reintroduction of an eliminated ID. [3]

- Recording without begin starts the baseline and still requires a valid verdict. [4]

- Ordinary exhaustion refuses the sixth round at the default five-round limit, naming the count and the limit. [5]


- Recorded architect/developer approval adds cumulative rounds only at exhaustion and preserves findings; legacy developer words stay readable. [6]


- Malformed approval payloads leave exhausted state unchanged. [7]


## Historical L41 Source File Binding

At the historical L41 preparation, the source bytes were SHA-256
`b007e8ec8440b0aca8f7897f86108c982ec33e9c03e7517240993282874f5212`
(`7707` bytes, `209` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.
