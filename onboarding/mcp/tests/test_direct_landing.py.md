# mcp/tests/test_direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture owns real temporary code/memory refs and an admitted series contract. | `_series_fixture` | mcp/tests/test_direct_landing.py:92-153 |
| The retained scenario proves one content commit and reads its attribution from Git. | `test_direct_landing_publishes_memory_and_recovers_independently_of_cache` | mcp/tests/test_direct_landing.py:171-272 |
| Recovery rejects real drift and accepts cache misses without extra commits. | `_recover_after_interrupted_receipt` | mcp/tests/test_direct_landing.py:274-314 |
| The lifecycle recovery owner performs the required same-generation resumption. | `recover_direct_landing_under_authority` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py:39-70 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-15T00:51 UTC — Replaced separate ledger-publication assertions with the retained one-content-commit scenario, interrupted receipt recovery, real drift refusals, malformed/absent cache checks, and clean-memory reuse; no collected-case increase. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.

- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): assertion-only extension of `test_direct_landing_verifies_code_commit_then_ledger` — it now asserts the memory-content commit's `%B` equals `direct memory\n\nCode-Commit: <code sha>`, that `git interpret-trailers --parse` reads that trailer, and that the ledger commit yields `""` from `%(trailers:key=Code-Commit)`. No new test function and no new parametrized case. Rebound the row to the extended range `161-266`. Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_direct_landing_verifies_code_commit_then_ledger` repointed to mcp/tests/test_direct_landing.py:161-240. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-26T15:20+02:00 — Replaced the obsolete conflicting-mapping refusal claim with the
  current ledger-history contract: exact-current re-land is idempotent, while a historical
  same-code row is superseded by a recovered memory-only change without losing audit history.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: forced preview/landed results through the closed public outcome model. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T11:29+02:00 — 260821-CLIVE-L1 candidate12 rebind: corrected the
  overbroad explicit-message claim and recorded internal-memory omission as typed not-applicable,
  followed by the existing mutation-time `direct-landing-memory-required` refusal. Bound to reviewed
  candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`, full diff SHA
  `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`, same-reviewer PASS;
  verification metadata remains pinned until governed closeout.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for the direct landing operation and
  branch-addressed route-review binding (L16-R6/R7/R8/R9); covers the policy gate, commit
  verification, pre-commit candidate-tree gate, idempotent re-land, ledger conflict, and the
  recovery-naming refusal dialect. Verified at code commit a9d50e08.