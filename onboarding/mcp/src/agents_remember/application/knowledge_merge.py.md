# mcp/src/agents_remember/application/knowledge_merge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_merge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `0da444b3b2b61f6a86fa4076b283c305db025d22` |
| lastVerifiedCommitDate | 2026-09-20T02:38:15+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The third composition seam of the knowledge substrate**: the guarded common-base merge, beside the single candidate write in `application/knowledge.py` and the candidate-lifecycle/publication seam in `application/knowledge_snapshot.py`. It exists for the same reason as the snapshot seam — a merge is a different composed operation from a single candidate write, and keeping it apart leaves each entry point readable as one intent.

Nothing here decides authority and nothing here holds durable state. It resolves a base claim, merges, and returns the typed result unchanged. Storage ranks below application, so a lower owner — the worktree or lifecycle package that would call a merge — receives `agents_remember.models.knowledge` values and never an import of this module or of the store.

**The adapter was *callable rather than wired*; CYCLE-02 wired it, and the non-claims it made about Git still hold.** No Git merge driver is installed, no attribute is configured and no commit is created anywhere on this path — that has not changed and is not what wiring meant. What changed is who calls it: the sync transaction now reaches this module through `merge_conflicted_stages`, the dataset half of a conflicted knowledge database's settlement, so the seam is no longer reachable only by a caller that already knew to compose `resolve_knowledge_merge_base` with `merge_resolved_knowledge_datasets` by hand. The Git half of that settlement lives in `worktrees/knowledge_conflict.py` and cannot live here, because a module under `worktrees/` may not import the memory domain; this half reads the three materialised stages' identities, proves the base and publishes the union, and returns one boolean rather than a compatibility verdict.

## Code Commentary

### Logic

Two entry points, each a rename of one storage operation onto the models vocabulary, each returning the storage layer's typed value unchanged:

- `resolve_knowledge_merge_base(request)` delegates to `memory.knowledge.merge_base.resolve_merge_base` and returns a resolution for shorthand — or `None` — so a caller composing a tool response is not handed a second resolution shape.
- `merge_resolved_knowledge_datasets(request)` delegates to `memory.knowledge.merge.merge_knowledge_datasets` and returns the whole `MergeOutcome`: the coverage of both deltas and the publication state when a destination was named. A resolution is returned as the proven value; a failure is returned as the typed refusal, so a caller branches on one code instead of catching an exception.

A third entry point is the driving half CYCLE-02 added, and it is the reason the lower layer can call this module without importing it:

- `merge_conflicted_stages(destination, stages, repository_root, commits)` takes three materialised index stages and returns whether the dataset was settled. It reads each stage's identity with `dataset_identity`, opens the left stage read-only to decode the one `repository` row the base claim is about, composes the two entry points above, and answers `True` only for `structurally_merged` **and** `published`. Every way of not settling returns `False` — a stage that is not a dataset, an adapter refusal (a schema disagreement above all), a publication that did not happen — so the caller leaves the path conflicted and the agent keeps it. `ConflictCommits` groups the three commits one conflicted merge spans, because the adapter requires all three together: a base claim naming two of them would not be a claim at all.

`KnowledgeMergeSeamDefect` is the one internal state the layer below makes unreachable — a refusal and a value both absent — and it is a defect rather than a caller-facing refusal for exactly that reason.

### Conventions

- Every function is a pure delegation with a docstring that states the boundary it does not cross; the module keeps no state, opens nothing itself and closes nothing.
- The seam returns storage's typed values unchanged, so a caller can branch on `state`/`refusal` without an application-level wrapper type — the same shape the two sibling seams use.
- The one exception to "pure delegation" is `merge_conflicted_stages`, and it is a structural one rather than a stylistic one: it exists here because the module that owns the Git side of the conflict may not import the memory domain, so this is the lowest layer that can read a dataset's identity at all. It still decides nothing — it returns one boolean.
- The module docstring states the non-claim (no driver, no attribute, no commit) rather than leaving it to be inferred.

### Invariants And Boundaries

- **No authority is conferred here.** The request models carry the identities a caller admitted; approval, acceptance and task status are not representable in anything this module returns.
- **No durable state and no Git.** The module creates no commit, moves no ref and writes no ledger row.
- **Storage ranks below application.** No lower-ranked package may import this module; a lower owner receives `models.knowledge` values.
- **The result carries no compatibility verdict.** A `structurally_merged` outcome is a statement about the candidate's structure and nothing about whether the merged knowledge is correct. `merge_conflicted_stages` returns that same structural fact as a boolean and adds no verdict of its own.
- **The seam is wired into exactly one caller, and the Git non-claims survive the wiring.** `worktrees/knowledge_conflict.py` imports `merge_conflicted_stages` and `ConflictCommits`; it is the one non-test importer in `mcp/src`, so the two delegating entry points above are now reachable from production code as well. No Git merge driver, no `.gitattributes` attribute and no commit were added by that change: the transaction still lets Git declare the conflict and then republishes the union itself.
- **A stage the adapter will not decide stays the agent's.** `merge_conflicted_stages` answers `False` rather than raising or guessing, so a schema disagreement narrows the agent's work instead of hiding it.

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
| The base-resolution entry point and its refusal-or-resolution contract. | `resolve_knowledge_merge_base` | mcp/src/agents_remember/application/knowledge_merge.py:55-70 |
| The merge entry point, including the carried statement that the result holds no compatibility verdict. | `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/application/knowledge_merge.py:74-83 |
| **The driving entry point CYCLE-02 added: three materialised stages in, one settled-or-not boolean out, and the identity read that only this layer may perform.** | `merge_conflicted_stages` | mcp/src/agents_remember/application/knowledge_merge.py:90-161 |
| **The three commits one conflicted merge spans, grouped because the adapter's base claim needs them together.** | `ConflictCommits` | mcp/src/agents_remember/application/knowledge_merge.py:164-175 |
| The defect the layer below makes unreachable. | `KnowledgeMergeSeamDefect` | mcp/src/agents_remember/application/knowledge_merge.py:86-87 |
| The two storage operations this seam delegates to. | `resolve_merge_base`; `merge_knowledge_datasets` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-105; mcp/src/agents_remember/memory/knowledge/merge.py:131-163 |
| The request and outcome vocabulary this seam takes and returns unchanged. | `MergeBaseRequest`; `MergeInput`; `MergeOutcome` | mcp/src/agents_remember/models/knowledge/merge.py:124-154; mcp/src/agents_remember/models/knowledge/merge.py:189-215; mcp/src/agents_remember/models/knowledge/merge.py:349-391 |
| The two sibling seams this module sits beside. | `write_authorship`; `publish_prepared_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge.py:102-124; mcp/src/agents_remember/application/knowledge_snapshot.py:142-147 |
|  The layer ranks that make a lower owner consume models rather than this module. | "[package.memory]"; "[package.application]" | layers.toml:206-207; layers.toml:314-315  |
| **The one non-test importer CYCLE-02 gave this module, and the Git half of the settlement that cannot live here.** | `merge_conflicted_stages`; `settle_knowledge_conflicts` | mcp/src/agents_remember/worktrees/knowledge_conflict.py:43-43; mcp/src/agents_remember/worktrees/knowledge_conflict.py:141-154 |
| The unit node that drives the conforming merge end to end through the public operations. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **the adapter gained its driver and this card's carried limitation is retracted where the source retracts it.** The module gained `merge_conflicted_stages` and `ConflictCommits` — the dataset half of a conflicted knowledge database's settlement — so the *callable rather than wired* claim is now recorded as **wired, with its Git non-claims intact**: no merge driver, no attribute and no commit were added, and what changed is that `worktrees/knowledge_conflict.py` calls this module instead of an agent composing the two delegating entry points by hand. The invariant that said this module had no non-test importer is replaced by the exact one importer, and the Two-delegations convention now names the structural exception and why it exists (a `worktrees/` module may not import the memory domain, so the identity read can live nowhere lower). The Todos line that carried the unwired status as an increment limitation is retired because the separately reviewed change it named is this one. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.

- 2026-09-19T22:49:08+00:00: Generated citation repair: `merge_resolved_knowledge_datasets` repointed to mcp/src/agents_remember/application/knowledge_merge.py:74-83. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new third composition seam. It records the two delegating entry points and the unchanged typed return, the non-claim the ruled design made explicit (**callable rather than wired**: no merge driver, no attribute, no commit anywhere on this path), the absent compatibility verdict, and the carried limitation that — like the two sibling seams — it has no non-test importer in `mcp/src`, because driver activation is a later separately reviewed change. Verification metadata remains empty until closeout stamps the code commit.
