# mcp/tests/test_transaction_only_worktree_delivery.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Protect public transaction-only closeout/integration and recovery with two accepted outputs and a disposable memory cache.

## Code Commentary

### Logic

The seven existing scenario definitions forbid the named quality, certification, curator, and review-related acceptance entry points while exercising the real transaction paths. Public closeout begins with malformed cache text and must create exactly one code commit and one memory commit; recovery begins with a missing cache, interrupts after code publication, rejects a wrong recovery code identity, and resumes without another code commit.

Configured failing pre-commit hooks are probed to prove they work, then the transaction scenarios assert no hook log. `_assert_memory_attribution` checks the exact memory message and both native trailer readers, and verifies memory.md is absent from the memory-content commit. The resulting cache is present and untracked; retired ledger result fields are absent. Integration still publishes exact refs and refuses a moved source before pair publication.

The sync/recloseout case passes the accepted code commit to _commit_memory_content and proves an unchanged memory candidate reuses the actual merged head. The final two cache tests derive canonical data from Git, keep an already-correct cache unchanged, recreate a missing cache, and repair malformed, forged, reordered, or header-inconsistent text. They compare refs and all commit objects in both repositories and preserve real file bytes and clean content state.

### Conventions

Existing mocks forbid acceptance-tool calls or inject the deliberate interruption; they do not mask production failures. The cache test fixture creates no ledger-only commit and never treats its observed cache as canonical input. Scenario definitions and their execution receipts are separate evidence.

### Invariants And Boundaries

- Normal transaction delivery does not acquire the forbidden acceptance tools.
- Recovery retains exact code identity and one real memory output.
- Both Git trailer readers see the attribution, while the committed tree contains no memory cache.
- Cache rebuilds change no refs, commit objects, or substantive content.
- Hook non-invocation applies to the installed scenario hooks, not arbitrary unrelated commands.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Named acceptance-tool prohibition and real failing-hook probes. [1]
- One code/memory commit, cache absence from the committed tree, and both trailer readers. [2]
- Interrupted public closeout resumes only its exact accepted code identity. [3]
- Integration publishes accepted refs or refuses source movement before publication. [4]
- A recloseout after sync records the actual memory head. [5]
- Cache materialization preserves both repositories' refs/commit objects and real content. [6]
- None [7]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

## 260918-TSIP-L6 The Closed Payload's Own Address, Driven End To End

This module gained one assertion (`:275-284`) inside
`test_public_closeout_commits_code_and_memory_without_acceptance_tools`: the applied closeout
payload's `contractPath` must equal `contract.contract_path.as_posix()`. It is the **producer
half** of `260918-TSIP` `T54` — `status_payload` emits the snake_case `contract_path`, while the
guidance guard a seat's next move depends on reads `contractPath`/`enclosurePath`, so a closed
closeout declaring neither made the guard withhold the guidance **entirely** and the seat silently
lost "integrate the task branches". This is the only case that drives the real producer end to
end; the guard's own four cases are in `mcp/tests/test_response_address_binding.py`.
