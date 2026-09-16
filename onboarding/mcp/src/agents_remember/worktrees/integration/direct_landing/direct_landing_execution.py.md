# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:06 |
| lastVerifiedCommitHash | `0dd1df9a950d59ac9622e5fb54250e528df08fa5` |
| lastVerifiedCommitDate | 2026-09-16T20:47:18+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Execution publishes or reuses real memory output and refreshes the cache afterward. | L42-L75; L175-L236; L316-L337 | [mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py](mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py) |
| Prepared attempts preserve repository and exact pre-commit tree evidence. | L239-L255; L258-L287 | [mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py](mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py) |
| Shared mutation intent and proof retain actual object checks. | L84-L105; L270-L301; L504-L518 | [mcp/src/agents_remember/worktrees/integration/mutation_evidence.py](mcp/src/agents_remember/worktrees/integration/mutation_evidence.py) |
| The lifecycle recovery owner resumes the generation before execution. | L39-L70 | [mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py](mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_recovery.py) |
| Lost-receipt recovery and clean reuse are exercised with real temporary repositories. | L274-L314; L316-L340 | [mcp/tests/test_direct_landing.py](mcp/tests/test_direct_landing.py) |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

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
