# mcp/src/agents_remember/worktrees/leaf_refs.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/leaf_refs.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814` |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`leaf_refs.py` is the dedicated task-tree leaf identity resolver. It validates user-provided leaf refs,
accepts canonical qualified ids, task document ids, and unambiguous legacy stems/slugs, and returns the
canonical identities each write surface persists.

## Code Commentary

### 260707-HFX2-L17 Resolution Guidance Channel

`LeafRefResolutionError` accepts optional guidance and appends it to the stable expected-form and
candidate diagnostics. The pair-binding validator uses this only for a proven legacy role suffix;
ordinary missing/ambiguous leaf behavior and status classification are unchanged.

### Logic

`resolve_leaf_ref(coordination_root, repo_name, ref, task_name, parent_task)` parses refs in the expected
`<repo>/<master-folder>/<doc-id>` form or as an unqualified legacy/doc-id value. It resolves the repository
scope, indexes active task roots from `task_resolver.py`, builds aliases from master subtask rows,
standalone/light `task.json` docs, sibling leaf task docs, file stems, slugs, and enclosure ids, then
returns `ResolvedLeafRef` with both the qualified catalog identity and the doc id used by worktree
contracts.

Candidate indexing identifies task-document JSON by the raw `schema: ar-task-document/v1` marker before
model validation. Sibling JSON artifacts without that marker are ignored; malformed or unreadable
non-task JSON siblings are skipped as inert artifacts, while marker-bearing malformed task documents
still run through `read_task_doc` and fail loudly.

`LeafRefResolutionError` is the loud failure surface for no-match and ambiguous refs. Its message names the
expected form and candidate qualified ids, and its `status` is either `leaf-ref-not-found` or
`leaf-ref-ambiguous` for API/tool adapters.

`resolve_leaf_enclosure_contract_for_ref()` is the compatibility bridge for worktree contract loading. It
first resolves aliases through the same task tree, then tries existing enclosure directories in canonical
doc-id and legacy forms. If the task tree cannot prove a unique alias, it falls back to the raw legacy
enclosure path so old contracts remain loadable.

### Invariants And Boundaries

- Terminal catalog assignments and spawn provenance persist `ResolvedLeafRef.qualified_id`.
- Worktree contracts persist `ResolvedLeafRef.doc_id`.
- Missing optional master `task.json` files and sibling non-task JSON artifacts are skipped; malformed
  non-task JSON artifacts are tolerated for boot safety, but malformed
  marker-bearing task documents are not swallowed.
- `task_resolver.py` owns task roots and raw contract paths; this module owns leaf-ref matching and
  candidate policy.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Task-root and raw contract path helpers imported by this resolver. | [task_resolver.py](task_resolver.py.md) |
| Worktree start adapter returning doc ids or command refusals. | [modules/leaf_ref_start.py](modules/leaf_ref_start.py.md) |
| Worktree contracts normalize legacy `leaf_id` values through this resolver. | [worktree_contract.py](worktree_contract.py.md) |
| Terminal serving adapter persists qualified catalog keys from this resolver. | [../serving/leaf_ref_validation.py](../serving/leaf_ref_validation.py.md) |
| Focused resolver tests pin accepted forms, ambiguity, no-match candidates, missing optional master docs, schema-marked malformed doc failures, sibling artifact skips, read-path contract tolerance, and light-task indexing. | [test_leaf_ref_resolution.py](../../../tests/test_leaf_ref_resolution.py.md) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added an optional error-guidance channel so legacy
  role-suffixed refs can name the canonical leaf-plus-role replacement without changing resolution.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (minimal projection robustness): `_has_task_doc_schema_marker`
  now tolerates malformed/unreadable non-task JSON siblings while preserving loud failures for
  marker-bearing task documents, allowing the current active-task corpus to boot with artifact JSON
  beside task docs. Verification metadata pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: candidate indexing now screens JSON siblings by the
  raw task-document schema marker before validation, ignores legitimate non-task JSON artifacts, keeps
  marker-bearing malformed task docs loud, and indexes standalone/light `task.json` docs as leaf
  candidates with slug, folder, and enclosure aliases. Verification metadata pinned until closeout stamps
  the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created as the dedicated qualified leaf-ref validation and
  normalization module, split out from task-root/contract path resolution. Verification metadata pinned
  until closeout stamps the 260707-HFX-L4 commit.
