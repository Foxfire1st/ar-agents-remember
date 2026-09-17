# mcp/src/agents_remember/memory/knowledge/merge_base.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/merge_base.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Resolve which dataset is the common base, and prove it when Git ancestry is the authority.** A merge is defined by its base, and the failure this module exists to prevent is the quiet one: picking *some* commit — an arbitrary `git merge-base` result, or `HEAD` as a stand-in — and producing a delta against a base neither side descends from.

It is the merge's first step, and it also owns the two operation names the merge vocabulary is keyed by (`RESOLVE_OPERATION`, `MERGE_OPERATION`), because base resolution is a separately refusable step: a caller that cannot even establish which dataset is the common base has not attempted a merge, and the refusal has to say so in its own name.

## Code Commentary

### Logic

`resolve_merge_base(request)` runs a deliberate order — the datasets are identified and structurally checked **first**, because a Git question about a commit is not evidence about a file, and a caller that handed over a dataset this schema cannot read should hear that rather than a merge-base verdict:

1. `_materialize_inputs(request)` reads each input's identity one at a time and requires the admitted one.
2. `require_supported_structure` (from `merge_schema.py`) checks each input's declared structure against the supported generation.
3. `_adjudicate_git_base(request)` consults the ancestry evidence only when the claim asks for it.

The base claim is a closed union and neither member is a guess:

- `SuppliedGitBase` — the caller resolved the base itself and names the exact commit and tree. No ancestry command runs; the recorded fact is that this was a caller decision.
- `ResolvedGitBase` — the caller claims one commit is the *unique* common base and asks for the evidence. `_ancestry_refusal` requires the commit to be an ancestor of both sides, and `_uniqueness_refusal` requires the history to have exactly one common base, which must be the claimed commit. Zero bases, several bases, or one base that is not the claimed commit all refuse.

`BaseResolution` is the outcome: `resolved()` distinguishes the proven resolution from the refusal that replaced it.

### Conventions

- Inputs are materialized **sequentially and without any lock**. The resource lock belongs to the destination publication, and taking one here to read an immutable file would hold a lock this operation does not need while it still has three more inputs to read.
- Every Git command is a read-only ancestry query under an absolute root, and every one goes through the package's shared Git runner. `_git_refusal` builds a Git-base refusal with the repository it was decided in, so the refusal names the history the answer came from.
- `_is_ancestor` and `_common_bases` are thin wrappers over `git merge-base --is-ancestor` and `git merge-base --all`; nothing in this module interprets a Git object beyond those two questions.

### Invariants And Boundaries

- **The base is proven, never chosen.** The admitted commit is always `claim.base_commit_id`; `_common_bases` only feeds the ambiguity and equality comparisons, and no path substitutes `HEAD` or an arbitrary merge-base result. A criss-cross history refuses as `common_base_ambiguous` rather than having this operation pick between the two bases.
- **Identities come from the dataset, not from Git.** Nothing here reads a Git object to decide what a dataset *is*: the datasets are identified by their own logical digest, and Git answers one question about commit ancestry.
- **All of it happens before any session, lock or destination resource exists.** Nothing this module does creates a database, attaches a schema, or takes a lock.
- **Boundary.** This module resolves a base; it does not merge, produce a delta, apply anything, or publish.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The closed two-member base claim: a supplied commit or an ancestry-proven unique common base. | `SuppliedGitBase`; `ResolvedGitBase` | mcp/src/agents_remember/models/knowledge/merge.py:81-86; mcp/src/agents_remember/models/knowledge/merge.py:89-101 |
| The outcome value that separates a proven resolution from its refusal. | `BaseResolution` | mcp/src/agents_remember/memory/knowledge/merge_base.py:61-72 |
| The resolution entry point and the deliberate identity-before-ancestry order. | `resolve_merge_base` | mcp/src/agents_remember/memory/knowledge/merge_base.py:75-105 |
| The sequential, lock-free materialization of the three immutable inputs. | `_materialize_inputs` | mcp/src/agents_remember/memory/knowledge/merge_base.py:108-146 |
| The ancestry adjudication and the two refusals a base claim can earn. | `_adjudicate_git_base`; `_ancestry_refusal`; `_uniqueness_refusal` | mcp/src/agents_remember/memory/knowledge/merge_base.py:149-178; mcp/src/agents_remember/memory/knowledge/merge_base.py:181-196; mcp/src/agents_remember/memory/knowledge/merge_base.py:199-224 |
| The two read-only Git questions and the refusal that names the repository. | `_is_ancestor`; `_common_bases`; `_git_refusal` | mcp/src/agents_remember/memory/knowledge/merge_base.py:227-231; mcp/src/agents_remember/memory/knowledge/merge_base.py:234-240; mcp/src/agents_remember/memory/knowledge/merge_base.py:243-262 |
| The refusal for an input that is not there or could not be read. | `_unavailable` | mcp/src/agents_remember/memory/knowledge/merge_base.py:265-277 |
| The two operation names this module owns for the merge vocabulary. | `RESOLVE_OPERATION`; `MERGE_OPERATION` | mcp/src/agents_remember/memory/knowledge/merge_base.py:52-53 |
| The schema preflight and logical-identity readers this step reuses. | `require_supported_structure`; `dataset_identity` | mcp/src/agents_remember/memory/knowledge/logical.py:141-161; mcp/src/agents_remember/memory/knowledge/merge_schema.py:121-139 |
| The node that drives every base and input defect, including the criss-cross history. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:248-250 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T06:49:47+00:00: Generated citation repair: `require_supported_structure`; `dataset_identity` repointed to mcp/src/agents_remember/memory/knowledge/merge_schema.py:121-139; mcp/src/agents_remember/memory/knowledge/logical.py:141-161. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate` in the row 78 of this card from mcp/tests/test_knowledge_guarded_merge.py:392-486 to mcp/tests/test_knowledge_guarded_merge.py:248-250, the extent of the construct the claim is about (the checker named line(s) [19, 248] as its live location)

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new base-resolution module. It records the closed two-member claim (a caller-supplied commit, or a claim the ancestry evidence must confirm as the unique common base), the deliberate identity-and-structure-before-ancestry order, the sequential lock-free materialization that keeps the destination lock the only lock the merge ever takes, and the boundary a later reader most needs: nothing here reads a Git object to decide what a dataset *is*, and no path reaches `HEAD` or an arbitrary merge-base result. Verification metadata remains empty until closeout stamps the code commit.
