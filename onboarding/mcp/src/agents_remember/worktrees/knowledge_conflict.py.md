# mcp/src/agents_remember/worktrees/knowledge_conflict.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/knowledge_conflict.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T14:20+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l43-ar`, uncommitted; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| lastVerifiedCommitHash | `4ef4dddc9194930611db2b1dfbb6e02113f2226a` |
| lastVerifiedCommitDate | 2026-09-20T15:00:59+02:00|
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
`merge_conflicted_stages` in the application package and this module hands it three paths and receives one
typed settlement.

**CYCLE-02's remainder changed what the caller receives, and it is the whole point of this module now.**
The settlement used to be a boolean, so a real production sync could report `sync-resolution-required`
with `files: ["knowledge.sqlite"]` while the engine's exact diagnosis — the table, the operation, the
refused row identity and the reconcile-and-retry action — sat one layer below the agent. What travels out
of here is now `RefusedKnowledgeStage`: the path, the engine's `MergeConflict`, the typed `KnowledgeRefusal`
with the action it advertises, and this layer's own `detail` for a path that never reached the adapter. It
also answers which authored decisions that conflict admits (`decisions`, read from
`expressible_decisions`), so the agent is offered exactly what the engine would accept and never one it
would refuse to apply. Nothing here re-renders the diagnosis: a caller that reformatted it would be
reimplementing the thing this exists to preserve.

## Code Commentary

### Logic

`settle_knowledge_conflicts(worktree, conflicts, left, right)` is the automatic pass — the whole surface the
transaction calls without a decision in hand. It walks the conflicted paths through
`settle_knowledge_conflict`, and returns a `KnowledgeConflictSettlement(remaining, refused)`. `remaining` is
the tuple of paths the caller still has to hand the agent; `refused` carries one `RefusedKnowledgeStage` per
path with the engine's own explanation. `guidance` picks the refusal whose explanation belongs in the public
response, preferring one that carries the engine's attribution or its typed refusal over one that carries only
this layer's reason — the first names a row an agent can reconcile, the second says the path never became a
dataset. That return value is the contract: whatever this cannot settle is exactly what the agent is still
asked to resolve, *and why*, so a refusal here narrows the agent's work rather than hiding it.

`settle_knowledge_conflict` (singular) is the per-path pipeline, and it is also the entry point the authored
retry uses: `reconciliations` is the sequence of decisions the caller has already accepted — each one
about exactly one conflict — and without it this is the
automatic pass. Every step reports its own reason instead of declining silently:

- `_stage` builds a `_Settlement` for the path, or a `RefusedKnowledgeStage` naming which fact was missing:
  the file is gone from the merge worktree, Git cannot name one common base, or a stage will not materialise.
  Those three details are this layer's, and they are empty whenever the engine answered.
- `_common_base` runs `git merge-base left right` and requires a unique answer. A base Git cannot name
  uniquely is the case the adapter refuses rather than choosing between candidates, so an unnameable
  base keeps the conflict and is never guessed at.
- `_materialise_stages` writes the three index positions with `git checkout-index --stage=<n>
  --prefix=<dir>/`, one prefix directory per stage so the three copies cannot overwrite one another.
- `merge_conflicted_stages` (application layer) merges the three materialised stages and publishes the
  union into the worktree path; this module stages the settled file with `git add` and reports success only
  when both halves agreed. A settle that could not be staged is its own `RefusedKnowledgeStage` reason
  rather than a silent failure.

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
- `__all__` exports `settle_knowledge_conflicts`, `settle_knowledge_conflict`, `RefusedKnowledgeStage` and
  `KnowledgeConflictSettlement`. The two settlement types are part of the contract because the caller
  journals and publishes their fields; `_Settlement`, `_STAGE_ROLES` and the helpers stay private, because a
  caller that reached past the entry points could settle one stage without staging the result.
- **The authored decision is passed through, never interpreted here.** Which row a conflict names, which
  decisions it admits and whether a decision is expressible are the adapter's answers; this module hands the
  decision down unchanged and reports whatever comes back.

### Invariants And Boundaries

- **A module under `worktrees/` never imports the memory domain.** This module reaches the dataset work
  through `application.knowledge_merge` and `models.knowledge.merge`, and the rule is enforced, not
  documented: `test_lower_ranked_owners_do_not_import_the_memory_domain` walks every module under
  `worktrees/` and `memory_quality/` and fails on any `agents_remember.memory` import.
- **Refusal is preserved, never swallowed — and it now carries the reason.** Only a genuine knowledge
  dataset settles. A path the adapter will not decide — a schema disagreement above all — stays conflicted
  and remains the agent's to resolve, with the engine's `conflict`, its typed `refusal` and the decisions it
  admits travelling to the caller so a resumed sync re-projects the diagnosis rather than only the file name.
- **This layer's own reasons are disjoint from the engine's.** `detail` is empty whenever the engine answered,
  so a reader can always tell "the adapter refused this row" from "this never became a dataset".
- **No compatibility verdict is taken here.** A structurally merged dataset says nothing about whether
  the combined knowledge is correct, and nothing in this module may treat it as approval. An authored
  each reconciliation is the caller's own decision about one conflict and stays exactly that: this module passes,
in order, every decision the caller has already accepted,
  it through, names it nowhere and never invents one.
- **The merge itself is not re-implemented.** Common-base proof, identity reading and publication stay
  in the application and storage layers; this module contributes Git state only.

### Todos

No new file-local follow-up is identified. The narrow scope (Git state only, no compatible-base search) is
the contract, not an unfinished edge. **One orientation is deliberately not expressible and stays open for
the owning seat:** the referential refusal's other named option — *restore the removed row*, i.e. the
arriving side deleted a parent the left still references — is not offered as an authored decision, because
retracting an arriving `UPDATE` or `DELETE` would remove or overwrite content the left side authored. That
orientation keeps the refusal and its own `next_action`; it is recorded in the leaf's evidence
(`notes/reports/2026-09-21-l40-conflict-diagnosis/EVIDENCE.md`, "What is not covered") as a limitation
rather than as settled behaviour, and no claim here should be read as saying the referential shape is fully
reconcilable.

## Docs References

No domain-documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The automatic pass over the conflicted paths and the settlement it returns. | `settle_knowledge_conflicts`; `KnowledgeConflictSettlement` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:240-256; mcp/src/agents_remember/worktrees/knowledge_conflict.py:100-126 |
| **The single-path pipeline, which is also the authored retry: the decision travels in, the engine's fresh explanation travels out.** | `settle_knowledge_conflict` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:200-237 |
| **The refusal that carries the engine's own conflict and refusal with the path, and the decisions that conflict admits.** | `RefusedKnowledgeStage` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:72-98 |
| **Which refusal's explanation belongs in the public response, and why the structured one is preferred.** | `guidance` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:110-126 |
| The per-path stage builder and the three reasons it declines to settle. | `_stage` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:174-197 |
| Binary-safe stage materialisation through `git checkout-index` rather than a text-decoding read. | `_materialise_stages` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:137-157 |
| The unique-common-base proof that refuses rather than choosing between candidates. | `_common_base` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:160-171 |
| The stage positions, named once and matching the adapter's own roles. | `_STAGE_ROLES` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:70-70 |
| The application half this module hands three paths to, the settlement it returns, and the one authored decision it passes through. | `merge_conflicted_stages`; `KnowledgeStageSettlement`; `AuthoredReconciliation` | mcp/src/agents_remember/application/knowledge_merge.py:113-181; mcp/src/agents_remember/application/knowledge_merge.py:94-111; mcp/src/agents_remember/models/knowledge/merge.py:175-211 |
| **The transaction seam that calls this module, journals the refusal it returns, and narrows the agent's conflict list.** | `_continue_memory_merge`; `SideMergeOutcome` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:364-395; mcp/src/agents_remember/worktrees/sync_transaction_git.py:35-48 |
| The layer rule that forces the two-module split, and the test that enforces it. | `test_lower_ranked_owners_do_not_import_the_memory_domain` | mcp/tests/test_knowledge_store.py:839-857 |
| The declared ranks and the sentence stating that lower owners receive `models/knowledge` values and never import the storage package. | "[package.worktrees]" | layers.toml:188-194; layers.toml:217-218 |
| The integration case that drives a real divergent knowledge dataset through the transaction and asserts both sides survive. | `_assert_knowledge_database_conflict_settles` | mcp/tests/test_worktree_sync.py:150-186 |
| **The integration cases that assert the diagnosis reaches the public response, that one authored decision settles it, that the row-less shape is retracted, that the orientation with nothing to retract advertises only a route that works, and that a schema disagreement is reported rather than reconciled.** | `_assert_knowledge_conflict_is_diagnosed_and_reconciled`; `_assert_delete_reference_conflict_is_retracted`; `_assert_unretractable_delete_reference_advertises_its_real_route`; `_assert_schema_disagreement_is_reported_not_reconciled` | mcp/tests/test_worktree_sync.py:268-354; mcp/tests/test_worktree_sync.py:357-399; mcp/tests/test_worktree_sync.py:402-455; mcp/tests/test_worktree_sync.py:458-490 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (uncommitted change set on `ar/260915-ks-l43-ar`, code base `fb719f89`): **the authored retry re-enters this pipeline with every decision already accepted, not only the newest one.** `settle_knowledge_conflict` now takes `reconciliations: Sequence[AuthoredReconciliation] = ()` and forwards `reconciliations=tuple(reconciliations)` into `merge_conflicted_stages`. The pass-through boundary the card records is unchanged and was re-stated with it: this module still decides nothing about a decision, each decision still answers only the row it named, and every conflict no decision names is still refused exactly as it was. The sequence exists because a retained merge is answered one conflict at a time — a decision that settles the first reveals the second, and the attempt that answers the second has to carry the first, or the two alternate forever. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l43-ar` on base `fb719f89`; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded. No commit was made.
- 2026-09-20T12:00:25+00:00: Generated citation repair: `_STAGE_ROLES` repointed to mcp/src/agents_remember/worktrees/knowledge_conflict.py:70-70. No content impact: mechanical anchor-range projection bound to citation source snapshot 23094be373d669ad77475ab6ebb610401913ce4b65c82d3b4cc642eb6bb44e43; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T07:30+02:00 — 260915-KS-L42 curator (citation repair in this document; this card's own source file is unchanged): **the row naming the integration cases was re-cited to those cases' own extents, and it now names the fourth case this change set added.** The three helpers it cited at `:250-338` / `:339-383` / `:384-418` were pushed down the file by this leaf's two new module-level helpers, and they now stand at `:268-354` / `:357-399` / `:458-490`; the row also gained `_assert_unretractable_delete_reference_advertises_its_real_route` at `:402-455`, which is the case for the orientation where the row-less retraction is unavailable and whose whole point is that the response advertises only a route that changes the state. The same read corrected the neighbouring row's `_assert_knowledge_database_conflict_settles` extent (`:150-188` → `:150-186`). No claim was weakened, no anchor renamed and no citation dropped; this card's metadata was not touched and no verification stamp was advanced.

- 2026-09-20T05:55+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **the boolean is replaced by a typed settlement, and this card's "receives one boolean" claim is retracted rather than annotated.** The card now records `RefusedKnowledgeStage` (path + the engine's `MergeConflict` + the typed `KnowledgeRefusal` + this layer's own `detail` + the decisions that conflict admits), `KnowledgeConflictSettlement(remaining, refused)` with the `guidance` preference that puts the *structured* refusal in the public response when several paths refused, and `settle_knowledge_conflict` as the single-path pipeline the authored retry re-enters with `reconciliation` — so the one public entry point is no longer the whole surface, and `__all__` grows to four names because the transaction journals and publishes those fields. `_settle_one` is gone: the per-path pipeline is `settle_knowledge_conflict`, and the three declines are now named details instead of one `None`. The invariant section gained the disjointness of this layer's reasons from the engine's and the pass-through boundary for an authored decision, and the Todos line now records the *one deliberately unexpressible orientation* (restore-the-removed-row) as an open limitation. Verification metadata is **advanced to the candidate's base `f79f4db7`**; the module remains new and uncommitted, so closeout owns the real stamp.

- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): created this one-to-one card for the new module. It records the Git half of the conflict settlement — binary-safe `git checkout-index` stage materialisation, the unique-common-base proof, the one exported entry point and the unresolved-path contract — and the layer rule that forces the two-module split, with the enforcing test cited rather than paraphrased. The file has no commit yet, so the commit fields name the candidate's base and closeout owns the real stamp.

