# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:06 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Nearest governing overview](../overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Executes and recovers the actual memory-content output of an accepted direct-landing generation.
The code commit already exists; this module either commits changed memory with its attribution or
reuses the accepted clean memory HEAD.

## Code Commentary

### Logic

`execute_direct_landing` checks mechanical convergence, reconciles durable Git evidence, builds the
operation-bound Git arguments, and calls `_direct_memory_commit`. After the real memory output is
known, it refreshes the consumer cache best effort and finishes the journal with `codeCommit`,
`memoryContentCommit`, and `ledgerCache`. `memory.memoryHead` is the actual memory-content/ref output.

`_direct_memory_commit` reuses a proven or recovered commit, archives an unchanged interrupted
attempt before retry, and validates a prepared mutation against its accepted parent/ref/tree.
For a clean accepted snapshot it records the existing memory HEAD without a new commit or invented
attribution. For changed content it publishes intent, commits through the shared helper with
`exclude_paths=("memory.md",)`, and proves that the output matches the bound tree.

The memory message comes from `EffectiveCloseoutInput.memory_content_message(code_commit)`. The
caller-owned body and the single final attribution block are inside the object before its receipt
is published. The old ledger execution object, byte intent, mapping checks, and ledger commit path
are deleted.

`execute_or_require_direct_landing_recovery` preserves typed ambiguity and interruption diagnostics
on the same generation. The lifecycle recovery owner must resume that generation before invoking
execution again; directly skipping its requeue step is not a valid recovery call.

### Conventions

Prepared-state and clean-state checks use the shared mutation-evidence API with `memory_cache=True`.
This file owns execution sequencing, not a second definition of cache parsing, Git cleanliness, or
message rendering.

### Invariants And Boundaries

- A produced memory commit must match the journaled parent/ref and expected content tree.
- Cache refresh failure cannot turn a completed Git output into a failed ledger publication.
- Clean reuse may have no attribution for the newly accepted code state; that absence is a fact.
- Recovery cannot replace accepted input or silently adopt changed code, refs, or memory content.

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
| Execution publishes or reuses real memory output and refreshes the cache afterward. | `execute_direct_landing`; "ledgerCache" | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:42-75 |
| Prepared attempts preserve repository and exact pre-commit tree evidence. | `_require_accepted_memory_prestate`; `_require_prepared_direct_attempt` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:239-255; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:261-290 |
| Shared mutation intent and proof retain actual object checks. | `begin_git_mutation`; `_publish_mutation_intent` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:84-105 |
| The lifecycle recovery owner resumes the generation before execution. | `recover_direct_landing_under_authority`; "lifecycle-generation-changed" | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py:39-70 |
| Lost-receipt recovery and clean reuse are exercised with real temporary repositories. | `_recover_after_interrupted_receipt`; `test_direct_landing_publishes_memory_and_recovers_independently_of_cache` | mcp/tests/test_direct_landing.py:171-272 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:06 UTC — Rebound source citation ranges after final shared-helper updates and formatting; current body contracts rechecked against the working candidate. No committed-source hash or execution claim was advanced.


- 2026-09-15T00:51 UTC — Removed all ledger execution and recovery claims; documented one attributed content commit or clean HEAD reuse, cache-excluding shared staging, best-effort cache refresh, and lifecycle-owned recovery resumption. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.


- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): `_direct_memory_commit` gained a required keyword-only `code_commit`, and `execute_direct_landing` passes `operation_input.codeCommit`, so this branch-addressed closeout route commits `effectiveInput.memory_content_message(code_commit)` — the closeout's own body plus exactly one `Code-Commit: <sha>` trailer naming the verified code commit, rendered from the shared `EffectiveCloseoutInput` definition instead of a route-local copy. Recorded that `_direct_ledger_commit` is deliberately unattributed (`message_for("ledger")`, no trailer). Rebound the stale ranges on this card (`_existing_direct_mapping`/`_require_head_ledger_bytes` 365-420, `snapshot_is_clean_at_head` mutation_evidence.py:42-57) and added the attribution rows. Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-08-27T18:33+02:00 — Simplified the exact-current-mapping branch into named predicates and
  centralized clean-snapshot truth in mutation evidence. Behavior and refusal vocabulary remain
  unchanged; the former CRAP offender now has cyclomatic complexity 3.
- 2026-08-26T14:32+02:00 — Documented memory-only direct landing: a later memory state for unchanged
  code prepends a new current row and preserves same-code history; only exact current equality is
  idempotent. Verification remains closeout-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
