# mcp/src/agents_remember/serving/leaf_ref_validation.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/leaf_ref_validation.py` |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`              |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared resolver and expected-form errors. | `# mcp/src/agents_remember/worktrees/leaf_refs.py` | onboarding/mcp/src/agents_remember/worktrees/leaf_refs.py.md:1-158 |
| Dashboard terminal open/attach routes that call this adapter. | "def create_app" | mcp/src/agents_remember/serving/app.py:232-232 |
| MCP terminal payload builders that call this adapter. | "def attach_terminal_session_to_leaf_payload" | mcp/src/agents_remember/mcp/tools/terminal.py:26-26 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18 wave curator (unowned card): rebound the two
  out-of-bounds onboarding-card citations to their code authorities; exact non-fixing check
  returns zero findings.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 3 repo-internal citation rows and preserved verification metadata.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added bounded legacy role-suffix detection and
  canonical leaf-plus-role refusal guidance shared by spawn and attach.

- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created to normalize terminal catalog leaf keys at serving
  and MCP write boundaries before persistence. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
