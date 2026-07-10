# mcp/src/agents_remember/serving/leaf_ref_validation.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/leaf_ref_validation.py` |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`              |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving overview](overview.md)

## Purpose

`leaf_ref_validation.py` is the serving-layer adapter for normalizing terminal catalog leaf keys before
write surfaces persist them. It converts accepted refs into the canonical qualified id
`<repo>/<master-folder>/<doc-id>`.

## Code Commentary

### 260707-HFX2-L17 Anti-Suffix Guidance

Normal leaf resolution still runs first. Only after it fails does the validator recognize a
role-suffixed workaround whose de-suffixed base is canonical, then refuse it with guidance to pass
the canonical leaf key and role separately. This avoids misclassifying legitimate leaf ids while
retiring the old suffix hack.

`repo_scope_for_leaf_key(config, leaf_key)` uses the configured repository only for unqualified refs; a
qualified ref carries its own repo segment. `resolve_catalog_leaf_key(config, leaf_key)` delegates to
`worktrees.leaf_refs.resolve_leaf_ref` and returns `ResolvedLeafRef.qualified_id`, letting callers
catch `LeafRefResolutionError` and return transport-specific refusals.

## Invariants And Boundaries

- Terminal catalog writes persist qualified leaf ids.
- The shared resolver owns ambiguity/no-match policy; this module only chooses the serving repo scope.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared resolver and expected-form errors. | [../worktrees/leaf_refs.py](../worktrees/leaf_refs.py.md) |
| Dashboard terminal open/attach routes that call this adapter. | [app.py](app.py.md) |
| MCP terminal payload builders that call this adapter. | [../mcp/tools/terminal.py](../mcp/tools/terminal.py.md) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added bounded legacy role-suffix detection and
  canonical leaf-plus-role refusal guidance shared by spawn and attach.

- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created to normalize terminal catalog leaf keys at serving
  and MCP write boundaries before persistence. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
