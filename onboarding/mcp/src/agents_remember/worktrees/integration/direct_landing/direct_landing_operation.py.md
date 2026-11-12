# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py

## Governing Overview

[Nearest governing overview](../overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Owns the durable synchronous coordinator for one direct-landing generation: progress, exact output
projection, completion, input-required reporting, and unchanged-attempt reset.

## Code Commentary

### Logic

`DirectLandingRuntime` locates the canonical operation store. `progress` validates mutation
observations and reported recovery cells, then derives the code/memory recovery projection through
the shared closeout evidence owner. It preserves monotonic output proof and records when a real
commit boundary was crossed. `finish` publishes completion — and one terminal-notice occurrence keyed by the leaf reference plus this
operation's generation, begun before the completion row and confirmed after it — while `require_input`
records a recoverable interruption or a developer-decision surface and takes no notice.

direct_landing_record persists the accepted typed request and initial mutation evidence. Verify mode records its existing code output immediately; create mode records accepted exact pair/input/policy and initial mutation evidence after provisional object creation but before branch publication, then proves that one output. Full pre-code verdict results are not record fields. Admission remains by canonical leaf, grant, series roots and messages; there is no closeout-door or ledger-byte intent.

`reconcile_direct_landing` reconciles launched Git commands, derives proven output cells, and asks
the pure classifier whether an omitted memory receipt can be recovered. Only the actual
`memoryContentCommit` is added from that proof. Updates use the current stored record and bounded
compare/update retries. `reset_reconciled_attempt` archives an exactly unchanged attempt before
resetting that leg within the same generation.

### Conventions

Typed mutation observations and recovery cells flow through their shared models. The canonical
root journal and its locator own durable state; mutable task prose and queue rows do not supply
fallback evidence.

### Invariants And Boundaries

- Accepted request identity and already proven output commits stay immutable.
- Missing memory receipts are recovered only from mechanically convergent Git evidence.
- No ledger mutation cell, ledger commit output, or DirectLandingLedgerIntent is published.
- Reconciliation and reset preserve the generation; action-required state must use the lifecycle recovery owner.

### Todos

No new file-local follow-up is established by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.


- The runtime validates and publishes progress, completion, and input-required evidence. [1]

- Request-owned generation construction and memory-only output reconciliation. [2]
- Recovery cells are derived from authoritative mutation evidence. [3]

- The classifier supplies exact memory output evidence. [4]


### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.

- The accepted create record stores input/policy and initial mutation evidence before branch publication, after provisional object creation; no full pre-code verdict fields. [5]
