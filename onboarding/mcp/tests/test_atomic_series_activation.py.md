# mcp/tests/test_atomic_series_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T13:20+02:00 |
| lastVerifiedCommitHash |  `e0820b04a499cbfb2079c78485346c50917a238a`|
| lastVerifiedCommitDate |  2026-09-13T18:02:04+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in this memory root (`system/sources.md` declares no
entries). These are repository-owned fixture and assertion contracts; no external library behavior is
inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The current source cases below replace the retired source-pair cases. They establish the fixture's
shared-pair premise and each contract-scoped behaviour, not a request to restore historical test counts
or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| One sprint commands both masters, so both series contracts share one protected source pair. | `ActivationFixture` | mcp/tests/test_atomic_series_activation.py:63-111 |
| Contracts sharing one source pair hold independent selection. | `test_contracts_sharing_one_source_pair_hold_independent_selection` | mcp/tests/test_atomic_series_activation.py:122-145 |
| Vacant and active are never waiting states. | `test_vacant_and_active_are_never_waiting_states` | mcp/tests/test_atomic_series_activation.py:147-155 |
| A release addresses only the released contract and still requires its exact selection. | `test_release_addresses_only_the_released_contract` | mcp/tests/test_atomic_series_activation.py:157-177 |
| Another contract's record can never be adopted, in either direction, and only an explicit selecting repair recovers it. | `test_another_contracts_record_can_never_be_adopted` | mcp/tests/test_atomic_series_activation.py:179-214 |
| A terminal contract cannot be selected. | `test_a_terminal_contract_cannot_be_selected` | mcp/tests/test_atomic_series_activation.py:216-228 |
| A completed pass beside a mid-flight selection is not this call's success: the state is `atomic-series-reconciling` and the summary names the stuck master, its publication time, its revision, both exits, and the pass's own message last. | `ReconcilingResultTests`; `test_a_completed_pass_beside_a_mid_flight_selection_is_not_success` | mcp/tests/test_atomic_series_activation.py:231-297; mcp/tests/test_atomic_series_activation.py:255-274 |
| A refusal that left a record mid-flight leads with that state before the refusal's own words. | `test_a_refusal_that_left_a_record_mid_flight_leads_with_that_state`; `_reconciling_result`; `_mid_flight_summary` | mcp/tests/test_atomic_series_activation.py:276-297; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:280-294; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:297-335 |
| The record identity is the contract, so the record path is keyed by the contract fingerprint rather than a source pair. | "def contract_fingerprint(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134 |
| A record whose fingerprint or contract path belongs to another contract is refused on read. | `_require_record_identity` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:360-372 |
| Only this contract's own reconciling state is projected as a waiting reason. | `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:275-287 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-14T13:20+02:00 — Recorded the new `ReconcilingResultTests` class: a `synced` pass beside a
  `reconciling` selection returns 2 with state `atomic-series-reconciling` and a summary naming the
  master, its contract path, its publication time, its revision, both `worktree_sync` exits and the
  pass's own message last, while a `blocked` refusal left beside a mid-flight record leads with that
  mid-flight state before its own words. Added the Purpose, Logic and Conventions statements and the
  two reference rows, and re-derived every existing fixture and case anchor against the current
  source. Verification stamps remain closeout-owned.

- 2026-09-13T14:20:09+02:00 — Rebound the card to the rewritten contract-scoped forcing suite: replaced the two retired source-pair cases (the former "logical active owner switch" and "source pairs are isolated" claims) with the five current ones, recorded the shared-source-pair premise and the two surviving refusals, and re-pointed every reference row at the current class/def lines. Verification stamps remain closeout-owned.

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-26T08:20+02:00 — Final frozen reconciliation of selector replacement, isolation,
  archive, vacancy, and exact-release forcing.

- 2026-08-26T05:40+02:00 — Added the completed nonregular selector quarantine forcing case to the
  suite description. Final ranges remain post-Dagger-owned.

- 2026-08-26T02:55+02:00 — Drafted focused selector-test onboarding; post-Dagger test inventory,
  nonregular-entry case, exact ranges, and verification remain open.
