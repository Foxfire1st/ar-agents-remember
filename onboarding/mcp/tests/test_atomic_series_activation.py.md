# mcp/tests/test_atomic_series_activation.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Contract-scoped forcing tests for the atomic-series activation record. The record is keyed by the
canonical series contract, so two atomic masters commanded by one sprint — which therefore derive the
SAME protected code and memory source branches — each own their own selection and progress
independently. The module also pins the two refusals that survive that re-keying: a record belonging to
another contract can never be adopted, and a terminal contract cannot be selected. A second class pins
the selecting operation's reporting of a selection left mid-flight: it is never presented as that
call's own success, and it leads with the contract the caller must resolve.

## Code Commentary

### Logic

`ActivationFixture` builds the premise instead of assuming it. One sprint document (`orchestrates`
`master-a` and `master-b`, `integrationBranch: super`) commands both masters, so both series contracts
are created through `ensure_master_series_contract` against the same `protected_branch`; only the work
branches differ. Because `activation_path` names its record by `contract_fingerprint` over the
resolved contract path, the two contracts address two different record files even though they share
the pair.

`AtomicSeriesActivationTests` then forces five contract-scoped behaviours:

- `test_contracts_sharing_one_source_pair_hold_independent_selection` asserts the shared
  `code_source_branch` and two distinct `activation_path` values, publishes `active` on A and
  `reconciling` on B, and observes both records intact. A's own state is not a reason for A to wait
  (`activation_waiting_reason` is `None`), and B's own `reconciling` state is the only reason B has.
  Both contract files remain on disk; neither selection replaced the other.
- `test_vacant_and_active_are_never_waiting_states` pins `activation_waiting_reason` to the single
  `atomic-series-reconciling` state: a vacant observation and a just-published `active` observation
  both return `None`.
- `test_release_addresses_only_the_released_contract` releases A and observes A vacant with its audit
  identity retained while B stays `active` on B's own master. Deleting A's record makes the next
  release refuse with `atomic-series-activation-selection-missing`, so a release still requires the
  exact selection it addresses.
- `test_another_contracts_record_can_never_be_adopted` writes both directions of a foreign record into
  A's path — B's fingerprint with A's contract path, and A's fingerprint with B's contract path — and
  expects `unreadable` plus `atomic-series-activation-contract-mismatch` for each. An explicit
  selecting repair on A then recovers the record.
- `test_a_terminal_contract_cannot_be_selected` rewrites B's contract as `integration_status
  "completed"` and expects the selection to refuse with `atomic-series-terminal`.

`ReconcilingResultTests` covers the selecting operation's own reporting boundary rather than the
record. `test_a_completed_pass_beside_a_mid_flight_selection_is_not_success` drives
`_reconciling_result` with a `synced` pass and a `reconciling` activation record, and asserts return
code 2, state `atomic-series-reconciling`, the activation observation attached unchanged, and a
summary naming the master's task-document ref and contract path, its publication time, its revision,
both `worktree_sync` exits, and the pass's own message last.
`test_a_refusal_that_left_a_record_mid_flight_leads_with_that_state` uses a `blocked` refusal and
asserts the mid-flight identity is stated before the refusal's own words, so a caller reads the state
it has to resolve rather than the symptom.

### Conventions

Cases assert observable record state, not internal helpers: they read `observe_atomic_series`,
`activation_waiting_reason`, `activation_path` and the two public transitions. The two result cases
drive the transaction's own `_reconciling_result` directly, because that reporting boundary is
exactly what they pin. Timestamps are the fixed
`NOW` constant, and temporary coordination/contract state is disposable. The card records source
behaviour; source inspection is memory preparation and does not claim a test run or acceptance. The
verification stamps above are closeout-owned and are not advanced by this card's prose.

### Invariants And Boundaries

- One activation record per canonical series contract; a shared protected source pair never shares
  this state.
- Only a contract's own `reconciling` state is a waiting reason. Vacant, active and a foreign master
  are never waiting reasons.
- Selection and release address exactly one contract. Another contract's record can never be adopted,
  and a release must find the exact selection it names.
- A terminal contract cannot enter selection.
- Real wave dependencies remain the sprint execution graph's own `predecessor-incomplete:` reasons;
  this module does not re-implement them (the cross-master concurrency card owns that forcing case).

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root (`system/sources.md` declares no
entries). These are repository-owned fixture and assertion contracts; no external library behavior is
inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The current source cases below replace the retired source-pair cases. They establish the fixture's
shared-pair premise and each contract-scoped behaviour, not a request to restore historical test counts
or percentage targets.

- One sprint commands both masters, so both series contracts share one protected source pair. [1]
- Contracts sharing one source pair hold independent selection. [2]
- Vacant and active are never waiting states. [3]
- A release addresses only the released contract and still requires its exact selection. [4]
- Another contract's record can never be adopted, in either direction, and only an explicit selecting repair recovers it. [5]
- A terminal contract cannot be selected. [6]
- A completed pass beside a mid-flight selection is not this call's success: the state is `atomic-series-reconciling` and the summary names the stuck master, its publication time, its revision, both exits, and the pass's own message last. [7]
- A refusal that left a record mid-flight leads with that state before the refusal's own words. [8]
- The record identity is the contract, so the record path is keyed by the contract fingerprint rather than a source pair. [9]
- A record whose fingerprint or contract path belongs to another contract is refused on read. [10]
- Only this contract's own reconciling state is projected as a waiting reason. [11]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
