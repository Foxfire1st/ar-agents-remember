# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

- Execution publishes or reuses real memory output and refreshes the cache afterward. [1]
- Prepared attempts preserve repository and exact pre-commit tree evidence. [2]
- Shared mutation intent and proof retain actual object checks. [3]
- The lifecycle recovery owner resumes the generation before execution. [4]
- Lost-receipt recovery and clean reuse are exercised with real temporary repositories. [5]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.
