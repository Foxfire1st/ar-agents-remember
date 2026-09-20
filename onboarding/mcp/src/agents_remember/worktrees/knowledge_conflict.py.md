# mcp/src/agents_remember/worktrees/knowledge_conflict.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/knowledge_conflict.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T23:20+00:00 |
| lastVerifiedCommitHash | `0da444b3b2b61f6a86fa4076b283c305db025d22` |
| lastVerifiedCommitDate | 2026-09-20T02:38:15+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

This module is **new and uncommitted** in the CYCLE-02 candidate: no commit contains it, so the two
commit fields name the base commit the candidate sits on rather than a commit that touched this file,
and they claim nothing about the candidate's acceptance. Closeout owns the real stamp.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

**The Git half of a knowledge-dataset conflict settlement inside the sync transaction**, and the module
that makes `application/knowledge_merge.py` a *driver* rather than a callable seam. A knowledge database
is binary to Git, so an ordinary merge can only declare the whole file conflicted and no amount of
staging resolves it. Before this module the transaction handed that file to the agent —
`sync-resolution-required` with `resolutionOwner: agent` — and the union was obtainable only by calling
`resolve_knowledge_merge_base` and `merge_resolved_knowledge_datasets` by hand, which is not a
composition seam an agent should have to discover. This module routes the three-way merge; the adapter
still decides it.

**It owns exactly the Git half.** Materialising the three index stages and staging the settled file are
worktree facts; reading a dataset's identity, proving the common base and performing the merge are
application facts. The split is forced by the layer contract rather than chosen: a module under
`worktrees/` may not import the memory domain at all, so the dataset work lives behind
`merge_conflicted_stages` in the application package and this module hands it three paths and receives
one boolean.

## Code Commentary

### Logic

`settle_knowledge_conflicts(worktree, conflicts, left, right)` is the whole public surface — one
function, exported alone in `__all__`. It walks the conflicted paths, keeps the ones `_settle_one` could
not settle, and returns them as the tuple the caller still has to hand the agent. That return value is
the contract: whatever this cannot settle is exactly what the agent is still asked to resolve, so a
refusal here narrows the agent's work rather than hiding it.

`_settle_one` is the per-path pipeline, and every step can decline:

- `_stage` builds a `_Settlement` for the path, or `None` when the file is gone, when Git cannot name
  one common base, or when a stage will not materialise.
- `_common_base` runs `git merge-base left right` and requires a unique answer. A base Git cannot name
  uniquely is the case the adapter refuses rather than choosing between candidates, so an unnameable
  base is reported as "not settled" and never guessed at.
- `_materialise_stages` writes the three index positions with `git checkout-index --stage=<n>
  --prefix=<dir>/`, one prefix directory per stage so the three copies cannot overwrite one another.
- `merge_conflicted_stages` (application layer) merges the three materialised stages and publishes the
  union into the worktree path; `settle_knowledge_conflicts` stages the settled file with `git add` and
  reports success only when both halves agreed.

`_STAGE_ROLES` is the single place the index positions are named, and it is deliberately the same
vocabulary the adapter's request uses — `base` is the merge base, `left` is the side being merged into
(ours), `right` is the side arriving (theirs) — so nothing is translated twice.

### Conventions

- **Binary safety is a property of the command, not of a code path.** The stages are materialised with
  `git checkout-index`, where Git writes the bytes itself, rather than with `git show :1:<path>`:
  `kernel.git_command.run_git` returns `CompletedProcess[str]`, so reading a SQLite file through that
  text layer would corrupt it before the adapter ever saw it — and the corruption would surface as a
  row-count mismatch rather than as corruption.
- Every Git call goes through the shared `run_git` runner and is judged on its `returncode`; a
  non-zero exit is a reason the path stays conflicted, not an exception to catch.
- `__all__` exports `settle_knowledge_conflicts` only. `_Settlement`, `_STAGE_ROLES` and the three
  helpers stay private, because a caller that reached past the one entry point could settle one stage
  without staging the result.

### Invariants And Boundaries

- **A module under `worktrees/` never imports the memory domain.** This module reaches the dataset work
  through `application.knowledge_merge` and `models.knowledge.merge`, and the rule is enforced, not
  documented: `test_lower_ranked_owners_do_not_import_the_memory_domain` walks every module under
  `worktrees/` and `memory_quality/` and fails on any `agents_remember.memory` import.
- **Refusal is preserved, never swallowed.** Only a genuine knowledge dataset settles. A path the
  adapter will not decide — a schema disagreement above all — stays conflicted and remains the agent's
  to resolve.
- **No compatibility verdict is taken here.** A structurally merged dataset says nothing about whether
  the combined knowledge is correct, and nothing in this module may treat it as approval.
- **The merge itself is not re-implemented.** Common-base proof, identity reading and publication stay
  in the application and storage layers; this module contributes Git state only.

### Todos

No new file-local follow-up is identified. The narrow scope (one exported function, no compatible-base
search) is the contract, not an unfinished edge.

## Docs References

No domain-documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one public entry point and the still-unresolved paths it returns. | `settle_knowledge_conflicts` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:141-154 |
| The per-path pipeline, including the three ways it declines to settle. | `_settle_one` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:120-138 |
| Binary-safe stage materialisation through `git checkout-index` rather than a text-decoding read. | `_materialise_stages` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:64-84 |
| The unique-common-base proof that refuses rather than choosing between candidates. | `_common_base` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:87-98 |
| The stage positions, named once and matching the adapter's own roles. | `_STAGE_ROLES` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:49-52 |
| The application half this module hands three paths to, and the commits it names. | `merge_conflicted_stages`; `ConflictCommits`; `_STAGE_NUMBERS` | mcp/src/agents_remember/application/knowledge_merge.py:90-161; mcp/src/agents_remember/application/knowledge_merge.py:164-175; mcp/src/agents_remember/application/knowledge_merge.py:193-193 |
| The transaction seam that calls this module and narrows the agent's conflict list. | `_continue_memory_merge` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:341-366 |
| The layer rule that forces the two-module split, and the test that enforces it. | `test_lower_ranked_owners_do_not_import_the_memory_domain` | mcp/tests/test_knowledge_store.py:839-857 |
| The declared ranks and the sentence stating that lower owners receive `models/knowledge` values and never import the storage package. | "[package.worktrees]" | layers.toml:188-194; layers.toml:217-218 |
| The integration case that drives a real divergent knowledge dataset through the transaction and asserts both sides survive. | `_assert_knowledge_database_conflict_settles` | mcp/tests/test_worktree_sync.py:129-183 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): created this one-to-one card for the new module. It records the Git half of the conflict settlement — binary-safe `git checkout-index` stage materialisation, the unique-common-base proof, the one exported entry point and the unresolved-path contract — and the layer rule that forces the two-module split, with the enforcing test cited rather than paraphrased. The file has no commit yet, so the commit fields name the candidate's base and closeout owns the real stamp.
