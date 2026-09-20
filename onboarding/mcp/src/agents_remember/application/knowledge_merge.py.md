# mcp/src/agents_remember/application/knowledge_merge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_merge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T14:20+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l43-ar`, uncommitted; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| lastVerifiedCommitHash | `4ef4dddc9194930611db2b1dfbb6e02113f2226a` |
| lastVerifiedCommitDate | 2026-09-20T15:00:59+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The third composition seam of the knowledge substrate**: the guarded common-base merge, beside the single candidate write in `application/knowledge.py` and the candidate-lifecycle/publication seam in `application/knowledge_snapshot.py`. It exists for the same reason as the snapshot seam — a merge is a different composed operation from a single candidate write, and keeping it apart leaves each entry point readable as one intent.

Nothing here decides authority and nothing here holds durable state. It resolves a base claim, merges, and returns the typed result unchanged. Storage ranks below application, so a lower owner — the worktree or lifecycle package that would call a merge — receives `agents_remember.models.knowledge` values and never an import of this module or of the store.

**The adapter was *callable rather than wired*; CYCLE-02 wired it, and the non-claims it made about Git still hold.** No Git merge driver is installed, no attribute is configured and no commit is created anywhere on this path — that has not changed and is not what wiring meant. What changed is who calls it: the sync transaction now reaches this module through `merge_conflicted_stages`, the dataset half of a conflicted knowledge database's settlement, so the seam is no longer reachable only by a caller that already knew to compose `resolve_knowledge_merge_base` with `merge_resolved_knowledge_datasets` by hand. The Git half of that settlement lives in `worktrees/knowledge_conflict.py` and cannot live here, because a module under `worktrees/` may not import the memory domain; this half reads the three materialised stages' identities, proves the base and publishes the union, and returns a typed settlement rather than a compatibility verdict.

**CYCLE-02's remainder changed what the settlement *is*, and it is the reason this card reads differently.** `merge_conflicted_stages` used to answer a bare boolean: the adapter's own refusal and the engine's row-level `MergeConflict` were reduced to `False`, so the public sync could report only `sync-resolution-required` with `files: ["knowledge.sqlite"]` while the explanation sat one layer below the agent. It now returns `KnowledgeStageSettlement(settled, conflict, refusal, detail)`, carrying the engine's typed values **verbatim** — including the fact that nothing here re-renders them, because a caller that re-rendered the diagnosis would be reimplementing the thing this exists to preserve. Both failure shapes are reported: a stage that never reached the adapter carries the seam's own `detail` (`_stage_inputs`), and a stage the adapter answered carries the refusal or the conflict and leaves `detail` empty.

## Code Commentary

### Logic

Two entry points, each a rename of one storage operation onto the models vocabulary, each returning the storage layer's typed value unchanged:

- `resolve_knowledge_merge_base(request)` delegates to `memory.knowledge.merge_base.resolve_merge_base` and returns a resolution for shorthand — or `None` — so a caller composing a tool response is not handed a second resolution shape.
- `merge_resolved_knowledge_datasets(request)` delegates to `memory.knowledge.merge.merge_knowledge_datasets` and returns the whole `MergeOutcome`: the coverage of both deltas and the publication state when a destination was named. A resolution is returned as the proven value; a failure is returned as the typed refusal, so a caller branches on one code instead of catching an exception.

A third entry point is the driving half CYCLE-02 added, and it is the reason the lower layer can call this module without importing it:

- `merge_conflicted_stages(destination, stages, repository_root, commits, reconciliations=())` takes three materialised index stages and returns a `KnowledgeStageSettlement`. It reads each stage's identity with `dataset_identity`, opens the left stage read-only to decode the one `repository` row the base claim is about, composes the two entry points above, and answers `settled=True` only for `structurally_merged` **and** `published`. `KnowledgeStageSettlement` is the whole contract now: `settled` is the only success there is, `conflict` is the engine's row-level attribution (table, operation and the exact refused key), `refusal` is the typed explanation with the action it advertises, and `detail` is this seam's own reason for the cases that never reached the adapter — a stage that is not a dataset, an unreadable namespace row — and it is empty whenever the adapter itself answered. `_stage_inputs` is the extraction of those four never-reached-the-adapter reasons, split out so the identity read stays readable as one intent and so each `False` the old boolean collapsed now names which fact was missing.
- `reconciliations` is the sequence of authored decisions the caller has already accepted, and the **only** way an authored resolution enters the merge. It is a **sequence rather than one decision** because a retained merge is answered one conflict at a time and the answer to the second has to carry the first: with only the newest decision carried, a two-conflict merge alternates between the same two rows forever, re-offering a decision that has already been made and already had its effect. This layer still decides nothing about them — the tuple is passed through unchanged, and the adapter still refuses every row no decision named. `ConflictCommits` groups the three commits one conflicted merge spans, because the adapter requires all three together: a base claim naming two of them would not be a claim at all.

`KnowledgeMergeSeamDefect` is the one internal state the layer below makes unreachable — a refusal and a value both absent — and it is a defect rather than a caller-facing refusal for exactly that reason.

### Conventions

- Every function is a pure delegation with a docstring that states the boundary it does not cross; the module keeps no state, opens nothing itself and closes nothing.
- The seam returns storage's typed values unchanged, so a caller can branch on `state`/`refusal` without an application-level wrapper type — the same shape the two sibling seams use. `KnowledgeStageSettlement` is the one exception and it is a *union of the storage layer's own values plus this seam's reason*, not a re-rendering: the conflict and the refusal it carries are objects the engine produced.
- The one exception to "pure delegation" is `merge_conflicted_stages`, and it is a structural one rather than a stylistic one: it exists here because the module that owns the Git side of the conflict may not import the memory domain, so this is the lowest layer that can read a dataset's identity at all. It still decides nothing about the merge — and it decides nothing about the authored decision either, which travels through it untouched.
- The module docstring states the non-claim (no driver, no attribute, no commit) rather than leaving it to be inferred.
- A reason this layer owns is named as `detail` and kept disjoint from the engine's own values, so a reader can always tell "the adapter refused this" from "this never became a dataset".

### Invariants And Boundaries

- **No authority is conferred here.** The request models carry the identities a caller admitted; approval, acceptance and task status are not representable in anything this module returns.
- **No durable state and no Git.** The module creates no commit, moves no ref and writes no ledger row.
- **Storage ranks below application.** No lower-ranked package may import this module; a lower owner receives `models.knowledge` values.
- **The result carries no compatibility verdict.** A `structurally_merged` outcome is a statement about the candidate's structure and nothing about whether the merged knowledge is correct. `settled=True` is that same structural fact plus the publication, and adds no verdict of its own.
- **The seam is wired into exactly one caller, and the Git non-claims survive the wiring.** `worktrees/knowledge_conflict.py` imports `merge_conflicted_stages` and `ConflictCommits`; it is the one non-test importer in `mcp/src`, so the two delegating entry points above are now reachable from production code as well. No Git merge driver, no `.gitattributes` attribute and no commit were added by that change: the transaction still lets Git declare the conflict and then republishes the union itself.
- **A stage the adapter will not decide stays the agent's, and it now says why.** `settled=False` rather than raising or guessing, with the engine's own conflict or refusal carried out with it, so a schema disagreement narrows the agent's work instead of hiding it.
- **The diagnosis is carried, never re-rendered.** Every value in `KnowledgeStageSettlement` is the engine's or this seam's; nothing here reformats, summarises or re-keys the refused row, because a re-rendered diagnosis is a second implementation of it.

### Todos

None recorded for this slice. The wiring that `merge_conflicted_stages` completes was a carried limitation of the earlier increment rather than a defect: the requirement had said this module supplies evidence and a callable boundary, not production configuration, and the separately reviewed change that turned it into a driver is the one recorded above.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The base-resolution entry point and its refusal-or-resolution contract. | `resolve_knowledge_merge_base` | mcp/src/agents_remember/application/knowledge_merge.py:59-75 |
| The merge entry point, including the carried statement that the result holds no compatibility verdict. | `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/application/knowledge_merge.py:78-87 |
| **The driving entry point: three materialised stages in, one typed settlement out, with the caller's one authored decision passed through untouched.** | `merge_conflicted_stages` | mcp/src/agents_remember/application/knowledge_merge.py:113-181 |
| **The settlement that replaced the boolean: the only success, the engine's conflict, the typed refusal, and this seam's own reason for a stage the adapter never saw.** | `KnowledgeStageSettlement` | mcp/src/agents_remember/application/knowledge_merge.py:94-111 |
| **The four reasons a path never reached the adapter, each named instead of collapsed into one `False`.** | `_stage_inputs` | mcp/src/agents_remember/application/knowledge_merge.py:184-220 |
| **The three commits one conflicted merge spans, grouped because the adapter's base claim needs them together.** | `ConflictCommits` | mcp/src/agents_remember/application/knowledge_merge.py:223-234 |
| The defect the layer below makes unreachable. | `KnowledgeMergeSeamDefect` | mcp/src/agents_remember/application/knowledge_merge.py:90-91 |
| The two storage operations this seam delegates to. | `resolve_merge_base`; `merge_knowledge_datasets` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-105; mcp/src/agents_remember/memory/knowledge/merge.py:133-167 |
| The request and outcome vocabulary this seam takes and returns unchanged. | `MergeBaseRequest`; `MergeInput`; `MergeOutcome` | mcp/src/agents_remember/models/knowledge/merge.py:212-243; mcp/src/agents_remember/models/knowledge/merge.py:113-124; mcp/src/agents_remember/models/knowledge/merge.py:444-486 |
| **The authored decision this seam carries without deciding anything about it.** | `AuthoredReconciliation` | mcp/src/agents_remember/models/knowledge/merge.py:175-211 |
| The two sibling seams this module sits beside. | `write_authorship`; `publish_prepared_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge.py:102-124; mcp/src/agents_remember/application/knowledge_snapshot.py:142-147 |
|  The layer ranks that make a lower owner consume models rather than this module. | "[package.memory]"; "[package.application]" | layers.toml:206-207; layers.toml:314-315  |
| **The one non-test importer this module has, and the Git half of the settlement that cannot live here — including the single-path reconcile entry point that carries the authored decision back in.** | `merge_conflicted_stages`; `settle_knowledge_conflicts`; `settle_knowledge_conflict` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:113-181; mcp/src/agents_remember/worktrees/knowledge_conflict.py:240-256; mcp/src/agents_remember/worktrees/knowledge_conflict.py:200-237 |
| The unit node that drives the conforming merge end to end through the public operations. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-381 |
| **The integration node that drives the structured diagnosis and the authored reconcile through the real transaction.** | `_assert_knowledge_conflict_is_diagnosed_and_reconciled` | mcp/tests/test_worktree_sync.py:250-338 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (uncommitted change set on `ar/260915-ks-l43-ar`, code base `fb719f89`): **the authored decision this layer passes through became a sequence, and the card says why rather than only what.** `merge_conflicted_stages` now takes `reconciliations: Sequence[AuthoredReconciliation] = ()` in place of the single `reconciliation`, forwarding `reconciliations=tuple(reconciliations)`. The parameter is a sequence because a retained merge is answered one conflict at a time: a decision that settles the first conflict reveals the second, and the attempt that answers the second must still carry the first, or the two conflicts alternate forever and the caller is offered a decision it has already made and that has already had its effect. The pass-through boundary the card already recorded is unchanged and was re-stated with it: this layer still decides nothing about a decision, and every conflict no decision names is still refused exactly as it was. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l43-ar` on base `fb719f89`, which is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands and no stamp was measured on it. No commit was made.

- 2026-09-20T05:52+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **the boolean that threw the diagnosis away is gone, and this card's central claim is rewritten rather than annotated.** `merge_conflicted_stages` now returns `KnowledgeStageSettlement(settled, conflict, refusal, detail)`, so the card records that the driver *reports* instead of collapsing: the engine's typed refusal and its row-level conflict travel out verbatim, and the four ways a path never reached the adapter are named in `detail` (extracted into `_stage_inputs`) instead of being one indistinguishable `False`. The reconciliation parameter is recorded with the exact boundary that matters for a reader of this card — this layer decides nothing about it, the adapter still refuses every row the caller did not name, and the diagnosis is carried rather than re-rendered, because a re-rendered diagnosis is a second implementation of it. A new invariant separates "the adapter refused this" from "this never became a dataset". Verification metadata is **advanced to the candidate's base `f79f4db7`** with the working candidate recorded beside it; the completed closeout still owns the final stamp.

- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **the adapter gained its driver and this card's carried limitation is retracted where the source retracts it.** The module gained `merge_conflicted_stages` and `ConflictCommits` — the dataset half of a conflicted knowledge database's settlement — so the *callable rather than wired* claim is now recorded as **wired, with its Git non-claims intact**: no merge driver, no attribute and no commit were added, and what changed is that `worktrees/knowledge_conflict.py` calls this module instead of an agent composing the two delegating entry points by hand. The invariant that said this module had no non-test importer is replaced by the exact one importer, and the Two-delegations convention now names the structural exception and why it exists (a `worktrees/` module may not import the memory domain, so the identity read can live nowhere lower). The Todos line that carried the unwired status as an increment limitation is retired because the separately reviewed change it named is this one. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.

- 2026-09-19T22:49:08+00:00: Generated citation repair: `merge_resolved_knowledge_datasets` repointed to mcp/src/agents_remember/application/knowledge_merge.py:74-83. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new third composition seam. It records the two delegating entry points and the unchanged typed return, the non-claim the ruled design made explicit (**callable rather than wired**: no merge driver, no attribute, no commit anywhere on this path), the absent compatibility verdict, and the carried limitation that — like the two sibling seams — it has no non-test importer in `mcp/src`, because driver activation is a later separately reviewed change. Verification metadata remains empty until closeout stamps the code commit.
