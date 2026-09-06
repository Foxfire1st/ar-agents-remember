# mcp/src/agents_remember/worktrees/modules/closeout_external.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/closeout_external.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T22:00:40+00:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Owns the external-memory and ledger phase of journaled worktree closeout after code acceptance. It refreshes governed memory, proves or creates the memory-content commit, then proves or creates the ledger commit using the immutable normalized messages.

## Code Commentary

### Logic

For ordinary external-memory leaves, `external_closeout_commits` receives the already validated
`EffectiveCloseoutInput` and one `ExternalCloseoutEvidence` value containing the reversible
memory-quality result plus the exact validated coherence no-impact projection. It first resumes any
proven output, then refreshes onboarding metadata, entity fingerprints, route overview metadata,
and generated route indexes and reruns memory quality. The same typed values are passed through the
refresh, memory, ledger, and resume boundaries; no helper rereads optional transport or reparses a
curator report. If content is dirty it begins memory mutation evidence and commits with the
effective memory message. If content is already mapped or clean, it proves reachability and
reports a verified-existing outcome instead of fabricating mutation evidence.

The ledger leg follows sequentially: an existing exact mapping is reused; otherwise the function announces ledger intent, writes and stages `memory.md`, binds the expected tree, commits with the explicit ledger message, and proves the commit. There is no generated ledger subject or `or` fallback. Series closeout remains its exact named-ref flow.

### Invariants And Boundaries

- Memory and ledger are two sequential Git commits, not an atomic transaction.
- Both enabled legs use the accepted stripped messages from `args.closeout_input`.
- Recovery facts must agree with mutation evidence and ledger ancestry.
- Refresh may consume only the no-impact identities already accepted during reversible closeout
  admission; it cannot invent, widen, or silently omit them.
- A crash between the two commits is journal-recoverable. Direct landing has its own journaled owner in `integration/direct_landing/direct_landing_execution.py`: it reconciles the accepted generation, resumes memory then ledger, checks ancestry, and records typed recovery requirements after ambiguous failure. This module does not own that direct-landing execution.

### Todos

No local fallback is planned. L2 owns broader recover/revise controls.

## Docs References

See task `260821-CLIVE-L1` L1-R3, L1-R4, and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| External refresh and every external commit consumer receive one effective input explicitly. | `external_closeout_commits`; `_commit_memory_content` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:50-96; mcp/src/agents_remember/worktrees/modules/closeout_external.py:149-194 |
| Proven recovery consumes that same input rather than rereading transport or overwriting evidence. | `_resumed_external_outcome` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:288-306 |
| Ledger commit intent and proof bracket its Git mutation using the explicit ledger message. | `_commit_ledger_mapping` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:210-246 |

## Cross-Repo References

The external-memory worktree is another repository governed by the same closeout contract.

## 260821-CLIVE-L2 Current Contract

The current source seams include `external_closeout_commits`. Closeout uses closed admission, immutable generation input, root-journal mutation evidence, and same-generation recovery. Missing commit-message or other input errors are refused before authority; retries cannot amend accepted intent or strand work behind queue state.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `external_closeout_commits` at this ownership boundary. | `external_closeout_commits` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:50-96 |

## Update History

- 2026-09-06T22:00:40+00:00 — Corrected current journal recovery semantics against production source while preserving previous verification pins. Source inspection only.


- 2026-08-29T18:29+02:00 — Added `ExternalCloseoutEvidence` so post-commit memory refresh consumes
  the same validated coherence decisions as reversible closeout admission.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input and closeout-memory-quality package relocations; external memory, memory-content, and ledger commit order is unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
