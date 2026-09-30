# mcp/src/agents_remember/worktrees/knowledge_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/knowledge_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

**The knowledge validator at the worktree layer's memory commit routes (MIK-R22 rule 8).** A route calls `memory_commit_refusal` with the exact tree it is about to commit, its comparison bases and its paired code commit, before it commits. The validator ranks above this layer and is reached through `services.KnowledgeValidationPort`.

## Code Commentary

### Logic

- `PairedCode(repository, commit)` names the code commit a memory commit is paired with.
- `has_layout_marker(repository, treeish)` runs `git ls-tree --name-only <tree> -- knowledge/layout.json`. Empty output means absent. A non-zero exit raises `LayoutProbeError`, so an unreadable side is never taken for unconverted memory (review R1 finding 6). Since MIK-R09 (leaf 260928-MIK-L09, review R1 F9) a `subprocess.SubprocessError` (the probe failed or timed out) raises `LayoutProbeError` too, naming it ("the Git probe failed or timed out"), so every caller's refusal is named instead of an escaping error. The mandatory gate and the worklist now probe through this function as well.
- `memory_commit_refusal(*, memory_repository, candidate_tree, bases, paired_code, leaf_publication=False)` probes the candidate and every base. A probe error is a refusal. If no side is converted it returns `None`. Otherwise it refuses when the paired code commit is unknown or when `worktree_services().knowledge_validation` is unbound, and else returns the port's answer: since MIK-R09, `leaf_refusal(...)` when `leaf_publication` is set (a commit that publishes a leaf: the leaf's own history file is re-anchor-checked whatever its `closed` flag, review R1 F1), else `refusal(...)`.

### Conventions

- It imports only the kernel Git runner, the L21 layout constant and `worktrees.services`; the validator itself stays behind the port.
- Callers: `sync_transaction_git._finish_staged_memory_merge`; since MIK-R09 (the carried L22 obligation) also the worktree closeout's exact tree (`closeout_external._refuse_invalid_memory_commit`), direct landing's exact tree (`direct_landing._close_gated_leaf`), and record, master and checkpoint landing (`knowledge_gate.landing_gate_refusal`), the leaf routes with `leaf_publication=True`.

### Invariants And Boundaries

- A converted memory commit is never made without a passing validator run: an unbound validator, an unknown paired code commit, or an unreadable tree refuses.
- Unconverted memory returns `None` before the validator is touched, so no route commits differently before the cutover (MIK-R37).
- There is no parameter that skips validation.

### Todos

Resolved by MIK-R09 (leaf 260928-MIK-L09): closeout, direct and record landing, and master and checkpoint landing call this helper, each with its comparison base (the parent line's memory tip for a leaf, the series head for direct landing, the task's `memory_base_commit` for a recorded landing, the parent source for a master), with a refusal test through each public route entry (`test_knowledge_gate_routes.py`).

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
| The paired code commit. | `PairedCode` | mcp/src/agents_remember/worktrees/knowledge_validation.py:28-33 |
| The marker probe fails closed, since MIK-R09 on a timed-out probe too. | `has_layout_marker`; `LayoutProbeError`; "the Git probe failed or timed out" | mcp/src/agents_remember/worktrees/knowledge_validation.py:36-37; mcp/src/agents_remember/worktrees/knowledge_validation.py:40-61 |
| The refusal: unconverted passes, converted needs a paired code commit and a bound validator; since MIK-R09 a leaf publication takes the port's `leaf_refusal`. | `memory_commit_refusal`; "route = validator.leaf_refusal if leaf_publication else validator.refusal" | mcp/src/agents_remember/worktrees/knowledge_validation.py:64-104 |
| The port it calls. | `KnowledgeValidationPort` | mcp/src/agents_remember/worktrees/services.py:133-162 |
| The sync's memory merge calls it before committing, after closing any master-line crossing history file the merge adds (MIK-R24). | `_finish_staged_memory_merge` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:570-598 |
| The route never commits converted memory unvalidated. | `test_the_worktree_route_never_commits_converted_memory_unvalidated` | mcp/tests/test_knowledge_validator_routes.py:134-158 |

## Cross-Repo References

The memory and code repositories are addressed explicitly by the caller; no external system is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** Logic records the timed-out probe named as `LayoutProbeError` (review R1 F9) and `memory_commit_refusal`'s new `leaf_publication` keyword choosing the port's `leaf_refusal` (F1); Conventions list the new callers (the carried L22 obligation), and the Todo is marked resolved. The probe and refusal rows were extended. The fixer normalised the rows.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Reopened claim re-read (MIK-R24).** `_finish_staged_memory_merge` changed: it closes a crossing sync's master-line history file before calling this module. The row still holds and was reworded to say so. This folds in the fixer projection of this pass. The composition now binds this module's validator with `GitBaseConverter` (rule 7), so a crossing merge is validated against its converted base; this module's own logic is unchanged.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
