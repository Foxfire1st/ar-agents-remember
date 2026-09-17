# mcp/src/agents_remember/worktrees/modules/closeout_external.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/closeout_external.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:58 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the external-memory content leg of journaled closeout after code acceptance, then refreshes the disposable ledger view for consumers. A new memory-content commit carries exactly one `Code-Commit:` trailer naming the accepted code commit; cache rendering creates no commit.

## CCR-R12@v5 Current External Transaction Boundary

`external_closeout_commits` receives the accepted code change and normalized input. It refreshes existing onboarding metadata, route-overview metadata, entity fingerprints, and generated route indexes, then creates a memory-content commit only if real memory content changed. The prepared staged-index commit uses `--no-verify`; this owner does not introduce an additional quality or curator gate.

Attribution is rendered before the commit object is created: `effective_input.memory_content_message(code_commit)` supplies the accepted message body and the `Code-Commit:` trailer, and `prove_git_commit` records the exact output. The later cache refresh derives from Git history and returns only informational state. Failure to render or write that cache cannot undo or block a proven memory output.

## Code Commentary

### Logic

Series closeout delegates immediately to `series_memory_closeout`, which reads the exact named memory ref and its source ancestry. Ordinary leaves resume an already recorded memory output through `resume_external_commits`; otherwise they run the raw metadata refreshes and `_commit_memory_content`.

The memory writer ignores root `memory.md` when testing content dirtiness. If no actual content changed, it returns existing HEAD and reports that verified-existing output without mutation evidence. For a real content change it prepares the ignored cache location, publishes memory mutation intent, stages content with `memory.md` excluded, commits the attributed message, and proves that exact object. The final writer boundary strips a force-staged cache too. There is no lookup of cached pairings and no second ledger commit.

`refresh_memory_cache` runs only after the memory output is fixed. `MemoryCloseoutOutcome.ledger_repair` contains its informational result, not a ledger commit or recovery prerequisite.

### Conventions

Accepted messages and the `VerifiedChange` travel explicitly into their consumers. New commits publish intent and exact proof; verified-existing commits publish recovery cells without fabricated mutation evidence.

#### Invariants And Boundaries

- Only real code and memory outputs belong to the recoverable Git transaction.
- The attributed memory commit excludes root `memory.md`, including an ignored file force-staged after admission.
- Cache-only changes reuse HEAD and cannot create a maintenance commit.
- A series never enters leaf memory mutation or owns a synthetic leaf memory checkout.
- Real ref, tree, and ancestry contradictions remain recovery failures. Missing or malformed cache bytes do not.
- Direct landing retains its own journal owner; this module does not execute that route.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `external_closeout_commits` resumes or creates the memory output, then refreshes its informational cache. | `external_closeout_commits` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:36-41 |
| `_commit_memory_content` reuses clean content or commits attributed memory with root memory.md excluded. | `_commit_memory_content` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:79-85 |
| `_refresh_external_memory` refreshes onboarding, overview, entity, and generated index data before content publication. | `_refresh_external_memory` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:121-125 |
| `_report_memory_commit` reports verified-existing code/memory outputs without fabricated mutation evidence. | `_report_memory_commit` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:150-159 |

The memory mutation boundary and the cache renderer have separate owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| Cache rendering returns informational state and creates no Git commit. | `refresh_memory_cache` | mcp/src/agents_remember/kernel/memory_cache.py:65-91 |

## Cross-Repo References

The external-memory worktree is another repository governed by the same closeout contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## 260821-CLIVE-L2 Current Contract

The current entry point is `external_closeout_commits`. Closed admission, immutable generation input, root-journal mutation evidence, and same-generation recovery still govern memory content. Ledger-specific intent, mapping reconciliation, and commits have been removed from this owner rather than retained as a parallel route.

## Update History

- 2026-09-15T00:58 UTC — Rechecked the formatted L9 working candidate and rebound current references after source cleanup; source-sha256=34ad2b8d7424260a75ef5e0aa844d4d2632dbc15fc5b078e03842f7ac87924d4. The older working-candidate snapshot and verification provenance are retained.

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=16d5e75c399d8b7d97f4ec63d5ae0d5e7fd1067892447147ea1cbb60c5f900cb. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): `_commit_memory_content` now takes the accepted code commit (`code_commit=change.commit` from the entry point) and commits `EffectiveCloseoutInput.memory_content_message(code_commit)`, so the memory-content commit object carries exactly one `Code-Commit: <sha>` trailer naming the code commit this same closeout landed; the ledger leg deliberately keeps `message_for("ledger")` and no trailer. Rebound every stale range on this card to the post-change source (`external_closeout_commits` 44-90, `_refresh_external_memory` 107-133, `_commit_memory_content` 136-196, `_commit_ledger_mapping` 212-251, `_resumed_external_outcome` 272-294) and added the attribution rows. Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T17:40+02:00 — 260831-LOCR-L36 curator reconciliation: the series leg of `external_closeout_commits` now returns through `series_memory_closeout` (the reconciled-pair reader), not `exact_series_memory_closeout`; recorded that a `series` contract is routed before the leaf memory-worktree assertion and that this module therefore owns no completion proof and no series memory worktree. Re-cited the two rows whose ranges had been written by a 2026-09-11 mechanical projection: the effective-input row is rebound to the exact consumers that carry the input (`_refresh_external_memory`, `_commit_memory_content`, `_commit_ledger_mapping`), and the ownership-boundary row to the literal declaration `def external_closeout_commits(` at its current location, so both ranges are the curator's own reading of the current source rather than a projected symbol mention. Verification metadata remains closeout-owned; no acceptance claim.
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
