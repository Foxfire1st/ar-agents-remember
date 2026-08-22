# mcp/src/agents_remember/worktrees/modules/closeout_external.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/closeout_external.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Owns the external-memory and ledger phase of journaled worktree closeout after code acceptance. It refreshes governed memory, proves or creates the memory-content commit, then proves or creates the ledger commit using the immutable normalized messages.

## Code Commentary

### Logic

For ordinary external-memory leaves, `external_closeout_commits` receives the already validated `EffectiveCloseoutInput` explicitly, first resumes any proven output, then refreshes onboarding metadata, entity fingerprints, route overview metadata, and generated route indexes and reruns memory quality. The same typed value is passed to memory, ledger, and resume helpers; no helper rereads optional `WorktreeArgs.closeout_input`. If content is dirty it begins memory mutation evidence and commits with the effective memory message. If the content is already mapped or clean, it proves reachability and reports a verified-existing outcome instead of fabricating mutation evidence.

The ledger leg follows sequentially: an existing exact mapping is reused; otherwise the function announces ledger intent, writes and stages `memory.md`, binds the expected tree, commits with the explicit ledger message, and proves the commit. There is no generated ledger subject or `or` fallback. Series closeout remains its exact named-ref flow.

### Invariants And Boundaries

- Memory and ledger are two sequential Git commits, not an atomic transaction.
- Both enabled legs use the accepted stripped messages from `args.closeout_input`.
- Recovery facts must agree with mutation evidence and ledger ancestry.
- A crash between the two commits is journal-recoverable for worktree closeout; direct landing durability remains deferred.

### Todos

No local fallback is planned. L2 owns broader recover/revise controls.

## Docs References

See task `260821-CLIVE-L1` L1-R3, L1-R4, and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| External refresh and every external commit consumer receive one effective input explicitly. | `external_closeout_commits`; `_commit_memory_content` | `mcp/src/agents_remember/worktrees/modules/closeout_external.py:49-97`; `mcp/src/agents_remember/worktrees/modules/closeout_external.py:148-187` |
| Proven recovery consumes that same input rather than rereading transport or overwriting evidence. | `_resumed_external_outcome` | `mcp/src/agents_remember/worktrees/modules/closeout_external.py:268-286` |
| Ledger commit intent and proof bracket its Git mutation using the explicit ledger message. | `_commit_ledger_mapping` | `mcp/src/agents_remember/worktrees/modules/closeout_external.py:209-247` |

## Cross-Repo References

The external-memory worktree is another repository governed by the same closeout contract.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
