# mcp/src/agents_remember/application/knowledge_merge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_merge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The third composition seam of the knowledge substrate**: the guarded common-base merge, beside the single candidate write in `application/knowledge.py` and the candidate-lifecycle/publication seam in `application/knowledge_snapshot.py`. It exists for the same reason as the snapshot seam — a merge is a different composed operation from a single candidate write, and keeping it apart leaves each entry point readable as one intent.

Nothing here decides authority and nothing here holds durable state. It resolves a base claim, merges, and returns the typed result unchanged. Storage ranks below application, so a lower owner — the worktree or lifecycle package that would call a merge — receives `agents_remember.models.knowledge` values and never an import of this module or of the store.

**The adapter is deliberately *callable rather than wired*.** No Git merge driver is installed, no attribute is configured and no commit is created anywhere on this path. A later, separately reviewed change is what turns this boundary into a driver, and this module is the exact seam such a change would call.

## Code Commentary

### Logic

Two entry points, each a rename of one storage operation onto the models vocabulary, each returning the storage layer's typed value unchanged:

- `resolve_knowledge_merge_base(request)` delegates to `memory.knowledge.merge_base.resolve_merge_base` and returns a resolution for shorthand — or `None` — so a caller composing a tool response is not handed a second resolution shape.
- `merge_resolved_knowledge_datasets(request)` delegates to `memory.knowledge.merge.merge_knowledge_datasets` and returns the whole `MergeOutcome`: the coverage of both deltas and the publication state when a destination was named. A resolution is returned as the proven value; a failure is returned as the typed refusal, so a caller branches on one code instead of catching an exception.

`KnowledgeMergeSeamDefect` is the one internal state the layer below makes unreachable — a refusal and a value both absent — and it is a defect rather than a caller-facing refusal for exactly that reason.

### Conventions

- Every function is a pure delegation with a docstring that states the boundary it does not cross; the module keeps no state, opens nothing itself and closes nothing.
- The seam returns storage's typed values unchanged, so a caller can branch on `state`/`refusal` without an application-level wrapper type — the same shape the two sibling seams use.
- The module docstring states the non-claim (no driver, no attribute, no commit) rather than leaving it to be inferred.

### Invariants And Boundaries

- **No authority is conferred here.** The request models carry the identities a caller admitted; approval, acceptance and task status are not representable in anything this module returns.
- **No durable state and no Git.** The module creates no commit, moves no ref and writes no ledger row.
- **Storage ranks below application.** No lower-ranked package may import this module; a lower owner receives `models.knowledge` values.
- **The result carries no compatibility verdict.** A `structurally_merged` outcome is a statement about the candidate's structure and nothing about whether the merged knowledge is correct.
- **The seam is not yet wired.** Like the other two application seams, this module has no non-test importer in `mcp/src` as of this leaf; installing a merge driver is an explicit later change, and this leaf's requirement excludes it.

### Todos

None recorded for this slice. The unwired status is a carried limitation of the increment, not a defect this leaf left open: the requirement states that this increment supplies evidence and a callable boundary, not production configuration.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The base-resolution entry point and its refusal-or-resolution contract. | `resolve_knowledge_merge_base` | mcp/src/agents_remember/application/knowledge_merge.py:36-52 |
| The merge entry point, including the carried statement that the result holds no compatibility verdict. | `merge_resolved_knowledge_datasets` | mcp/src/agents_remember/application/knowledge_merge.py:55-64 |
| The defect the layer below makes unreachable. | `KnowledgeMergeSeamDefect` | mcp/src/agents_remember/application/knowledge_merge.py:67-68 |
| The two storage operations this seam delegates to. | `require_session_capability` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-105; mcp/src/agents_remember/memory/knowledge/merge.py:131-163 |
| The request and outcome vocabulary this seam takes and returns unchanged. | `MergeBaseRequest` | mcp/src/agents_remember/models/knowledge/merge.py:124-154; mcp/src/agents_remember/models/knowledge/merge.py:189-215; mcp/src/agents_remember/models/knowledge/merge.py:349-391 |
| The two sibling seams this module sits beside. | `write_authorship`; `publish_prepared_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge.py:102-124; mcp/src/agents_remember/application/knowledge_snapshot.py:142-147 |
|  The layer ranks that make a lower owner consume models rather than this module. | "[package.memory]"; "[package.application]" | layers.toml:206-207; layers.toml:314-315  |
| The unit node that drives the conforming merge end to end through the public operations. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:248-312 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new third composition seam. It records the two delegating entry points and the unchanged typed return, the non-claim the ruled design made explicit (**callable rather than wired**: no merge driver, no attribute, no commit anywhere on this path), the absent compatibility verdict, and the carried limitation that — like the two sibling seams — it has no non-test importer in `mcp/src`, because driver activation is a later separately reviewed change. Verification metadata remains empty until closeout stamps the code commit.
