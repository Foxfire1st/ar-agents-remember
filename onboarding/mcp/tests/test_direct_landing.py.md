# mcp/tests/test_direct_landing.py

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Exercises branch-addressed direct landing with real temporary code and memory repositories,
including existing-code memory pairing, prospective code creation, interrupted-generation recovery and ledger-cache independence.

## Code Commentary

### Logic

The retained integration scenario refuses a foreign requested code commit before dereferencing
it, previews with malformed cache bytes while checking that all bytes outside loose Git objects stay unchanged, and then stages
real memory content. It interrupts `prove_git_commit` after Git has committed the content, so the
subsequent recovery must infer that exact object rather than publish another one.

`_recover_after_interrupted_receipt` requires a memory-only mutation record. It temporarily changes
the accepted code branch, memory branch, and content independently and expects a decision each time.
After restoring those facts, both cache absence and malformed cache text remain terminalizable.
Recovery goes through `recover_direct_landing_under_authority`, including the lifecycle requeue step,
and ends with the same HEAD, a completed journal, and proven `memoryContentCommit`.

The cache-independence case asserts exactly one new memory commit, the caller body plus Code-Commit and tree-bound Commit-Check-Pass trailers, an ignored/untracked cache, and a derived cached pair. `test_converted_direct_landing_reuses_clean_memory_and_replays_terminal` ports the non-format reuse guarantees onto converted memory: exactly one paired commit, with only the asserted first-landing scaffolding and gate-authored sidecar changes. Repeating the accepted request refuses with `direct-landing-input-conflict`, names the accepted fingerprint, and leaves the completed generation, HEAD and attribution unchanged, including after cache deletion.

The create fixture defaults to an answered world, but the pre-code census case selects `answer=False`. It first performs its legal revoke, negative ungranted-call control and give; only then does it edit the code, reanchor and compute `trace_rows(world, *TRACES)`, which materializes the enclosure. The existing message/tree refusal and admitted code-leg assertions stay in the same fixture. The converted reuse/replay case also passes its actual `world` to the trace helper.

### Conventions

The current source contains multiple direct landing cases over disposable repositories, including verify-existing, exact-pair create, same-generation public recovery and ambiguous-cut refusal. A historical single-case account does not describe the expanded source population.
Its wrapper enters the production coordinator with a supplied contract; it does not prove the full
public scheduling fence or a live deployment. Source inspection of this card is not an execution
receipt or certification claim.

### Invariants And Boundaries

- Cache independence must not weaken actual code/ref/content contradiction checks.
- Recovery must reuse the real committed object and respect the lifecycle transition owner.
- No ledger-only commit or fabricated code-to-memory mapping is expected. Verify-existing creates no code commit; create publishes one admitted code output and recovery reuses it, never a second commit.
- Fixture repositories establish local behavior, not authorization to bypass production admission.

### Todos

No new file-local follow-up is established by this documentation pass.

## Verify-existing and create-code cases

The retained memory-only interrupted-receipt scenario is verify-existing mode, not the whole direct tool. Create cases additionally assert canonical grant/leaf binding, non-mutating preview, exact code/memory pair, pre-code census state preservation, tree/source refusal, generation-isolated retry/public recovery and sibling proof. Test source and historical passed receipts have distinct epochs; this card claims neither a new run nor full-suite/host acceptance.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.




- The lifecycle recovery owner performs the required same-generation resumption. [4]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.

- The fixture owns real temporary code/memory refs and an admitted series contract. [1]
- The retained scenario proves one content commit and reads its attribution from Git. [2]
- Converted paired-commit/replay guarantees and retained interrupted-receipt recovery [3]
- The pre-code census case performs grant controls before real edit, reanchor and source-bound trace computation. [5]
