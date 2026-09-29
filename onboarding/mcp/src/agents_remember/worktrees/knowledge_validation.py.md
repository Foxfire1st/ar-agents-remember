# mcp/src/agents_remember/worktrees/knowledge_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/knowledge_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`|
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

**The knowledge validator at the worktree layer's memory commit routes (MIK-R22 rule 8).** A route calls `memory_commit_refusal` with the exact tree it is about to commit, its comparison bases and its paired code commit, before it commits. The validator ranks above this layer and is reached through `services.KnowledgeValidationPort`.

## Code Commentary

### Logic

- `PairedCode(repository, commit)` names the code commit a memory commit is paired with.
- `has_layout_marker(repository, treeish)` runs `git ls-tree --name-only <tree> -- knowledge/layout.json`. Empty output means absent. A non-zero exit raises `LayoutProbeError`, so an unreadable side is never taken for unconverted memory (review R1 finding 6).
- `memory_commit_refusal(*, memory_repository, candidate_tree, bases, paired_code)` probes the candidate and every base. A probe error is a refusal. If no side is converted it returns `None`. Otherwise it refuses when the paired code commit is unknown or when `worktree_services().knowledge_validation` is unbound, and else returns the port's answer.

### Conventions

- It imports only the kernel Git runner, the L21 layout constant and `worktrees.services`; the validator itself stays behind the port.
- Callers today: `sync_transaction_git._finish_staged_memory_merge`. MIK-R09 will call it from closeout and the landing routes.

### Invariants And Boundaries

- A converted memory commit is never made without a passing validator run: an unbound validator, an unknown paired code commit, or an unreadable tree refuses.
- Unconverted memory returns `None` before the validator is touched, so no route commits differently before the cutover (MIK-R37).
- There is no parameter that skips validation.

### Todos

MIK-R09 wires closeout, direct/record landing, and master and checkpoint landing through this helper; each of those routes also needs K_B, which MIK-R08/R09 resolve (worker gaps 1 and 2).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The route gate and its callers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The paired code commit. | `PairedCode` | mcp/src/agents_remember/worktrees/knowledge_validation.py:28-32 |
| The marker probe fails closed. | `has_layout_marker`; `LayoutProbeError` | mcp/src/agents_remember/worktrees/knowledge_validation.py:39-54; mcp/src/agents_remember/worktrees/knowledge_validation.py:35-36 |
| The refusal: unconverted passes, converted needs a paired code commit and a bound validator. | `memory_commit_refusal` | mcp/src/agents_remember/worktrees/knowledge_validation.py:57-91 |
| The port it calls. | `KnowledgeValidationPort` | mcp/src/agents_remember/worktrees/services.py:131-147 |
| The sync's memory merge calls it before committing. | `_finish_staged_memory_merge` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:495-519 |
| The route never commits converted memory unvalidated. | `test_the_worktree_route_never_commits_converted_memory_unvalidated` | mcp/tests/test_knowledge_validator_routes.py:129-153 |

## Cross-Repo References

The memory and code repositories are addressed explicitly by the caller; no external system is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
