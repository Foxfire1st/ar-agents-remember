# mcp/tests/test_direct_landing.py

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Exercises branch-addressed direct landing with real temporary code and memory repositories,
including one content commit, interrupted-receipt recovery, and independence from the ledger cache.

## Code Commentary

### Logic

The retained integration scenario refuses a foreign requested code commit before dereferencing
it, previews with malformed cache bytes while checking that files stay unchanged, and then stages
real memory content. It interrupts `prove_git_commit` after Git has committed the content, so the
subsequent recovery must infer that exact object rather than publish another one.

`_recover_after_interrupted_receipt` requires a memory-only mutation record. It temporarily changes
the accepted code branch, memory branch, and content independently and expects a decision each time.
After restoring those facts, both cache absence and malformed cache text remain terminalizable.
Recovery goes through `recover_direct_landing_under_authority`, including the lifecycle requeue step,
and ends with the same HEAD, a completed journal, and proven `memoryContentCommit`.

The case asserts exactly one new memory commit, the caller body plus its real attribution trailer,
an ignored/untracked cache, and a derived cached pair. `_assert_clean_memory_reused` removes the
cache in a separate fixture and verifies successful reuse of the existing memory HEAD without a
new commit or invented attribution for the new code state.

### Conventions

The file retains one collected integration case with helper assertions over disposable repositories.
Its wrapper enters the production coordinator with a supplied contract; it does not prove the full
public scheduling fence or a live deployment. Source inspection of this card is not an execution
receipt or certification claim.

### Invariants And Boundaries

- Cache independence must not weaken actual code/ref/content contradiction checks.
- Recovery must reuse the real committed object and respect the lifecycle transition owner.
- No ledger-only commit, new code commit, or fabricated code-to-memory mapping is expected.
- Fixture repositories establish local behavior, not authorization to bypass production admission.

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

- The fixture owns real temporary code/memory refs and an admitted series contract. [1]
- The retained scenario proves one content commit and reads its attribution from Git. [2]
- Recovery rejects real drift and accepts cache misses without extra commits. [3]
- The lifecycle recovery owner performs the required same-generation resumption. [4]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.
