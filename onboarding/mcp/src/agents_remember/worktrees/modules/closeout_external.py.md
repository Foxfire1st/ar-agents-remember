# mcp/src/agents_remember/worktrees/modules/closeout_external.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/closeout_external.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T22:00:40+00:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Owns the external-memory and ledger phase of journaled worktree closeout after code acceptance. It refreshes governed memory, proves or creates the memory-content commit, then proves or creates the ledger commit using the immutable normalized messages.

## CCR-R12@v5 Current External Transaction Boundary

`external_closeout_commits` performs the mechanical closeout leg after code acceptance. It refreshes
existing onboarding metadata, route-overview metadata, entity fingerprints, and generated route
indexes through the raw refresh helpers, then commits memory content and the ledger mapping in
sequence. It does not run memory quality, curator coherence, strict code quality, or selected
certification in the normal transaction. Both created commits use the existing staged-index helper
with `--no-verify`, so configured pre-commit hooks are not invoked by these transaction commits;
the focused transaction test proves this boundary. A crash between the two commits remains
journal-recoverable.

## Code Commentary

### Logic

For ordinary external-memory leaves, `external_closeout_commits` receives the already validated
`EffectiveCloseoutInput` and the accepted code change. It first resumes any proven output, then
refreshes onboarding metadata, entity fingerprints, route overview metadata, and generated route
indexes. No helper reruns memory quality or reparses a curator report on this path. If content is
dirty it stages and commits with the effective memory message; if content is already mapped or
clean, it proves reachability and reports a verified-existing outcome instead of fabricating
mutation evidence.

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
| External refresh and every external commit consumer receive one effective input explicitly. | `external_closeout_commits`; `_commit_memory_content` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:44-89; mcp/src/agents_remember/worktrees/modules/closeout_external.py:135-186 |
| Proven recovery consumes that same input rather than rereading transport or overwriting evidence. | `_resumed_external_outcome` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:262-284 |
| Ledger commit intent and proof bracket its Git mutation using the explicit ledger message. | `_commit_ledger_mapping` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:202-241 |

## Cross-Repo References

The external-memory worktree is another repository governed by the same closeout contract.

## 260821-CLIVE-L2 Current Contract

The current source seams include `external_closeout_commits`. Closeout uses closed admission, immutable generation input, root-journal mutation evidence, and same-generation recovery. Missing commit-message or other input errors are refused before authority; retries cannot amend accepted intent or strand work behind queue state.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `external_closeout_commits` at this ownership boundary. | `external_closeout_commits` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:44-89 |

## Update History
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `_commit_memory_content`, `external_closeout_commits` repointed to mcp/src/agents_remember/worktrees/modules/closeout_external.py:135-186, mcp/src/agents_remember/worktrees/modules/closeout_external.py:44-89. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `external_closeout_commits` repointed to mcp/src/agents_remember/worktrees/modules/closeout_external.py:44-89. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `_resumed_external_outcome` repointed to mcp/src/agents_remember/worktrees/modules/closeout_external.py:256-274. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `_commit_ledger_mapping` repointed to mcp/src/agents_remember/worktrees/modules/closeout_external.py:199-235. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `external_closeout_commits` repointed to mcp/src/agents_remember/worktrees/modules/closeout_external.py:45-89. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-06T22:00:40+00:00 — Corrected current journal recovery semantics against production source while preserving previous verification pins. Source inspection only.


- 2026-08-29T18:29+02:00 — Added `ExternalCloseoutEvidence` so post-commit memory refresh consumes
  the same validated coherence decisions as reversible closeout admission.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input and closeout-memory-quality package relocations; external memory, memory-content, and ledger commit order is unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first verification stamp remains governed-closeout-owned.
