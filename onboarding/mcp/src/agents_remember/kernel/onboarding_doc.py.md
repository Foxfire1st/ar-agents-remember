# mcp/src/agents_remember/kernel/onboarding_doc.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

Kernel-level Markdown table and fence-aware meaningful-body/history parsing for old-card readers, conversion and crossing. Route normalization, changed-route membership and doc-type route discovery were removed from this module; the retained readers do not grant ordinary operational acceptance from Update History or verification metadata.

## Code Commentary

### Logic

`markdown_table_cells` splits table cells and `table_metadata` reads metadata rows for retained readers. `fence_delimiter`, `unfenced_lines` and `_section_lines` share fence-aware history boundaries. `ROUTE_OVERVIEW_DOC_TYPES` and the no-impact pattern remain constants, not a route-discovery or operational attestation API. `normalize_route`, `route_contains_changed_path` and `discover_route_overviews` are absent. The worktree onboarding owner imports only `markdown_table_cells`; metadata-row rewriting and its facade exports were removed.

`meaningful_body` removes the three verification metadata rows and the entire real Update History section, with fence-aware heading detection. `update_history_section` returns stripped nonempty history lines; `new_history_lines` returns newly appearing lines. `meaningful_body_changed`, active-claim filtering and `has_no_impact_marker` were removed with the legacy operational classifiers.

### Invariants And Boundaries

- Parsing excludes verification stamps and Update History from meaningful body.
- Real H2 headings delimit history; fenced lookalikes do not.
- These are reader/converter utilities, not an ordinary publication fallback or in-band no-impact authority.
- Kernel must not import worktree, application or provider owners.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References


- Meaningful-body normalization strips verification fields and history. [6]
- History extraction is section-aware. [7]


- History extraction and history-line delta parsing survive; metadata-row rewriting was removed. [1]

- The onboarding owner imports retained Markdown table parsing, not the removed body/history classifiers. [2]

- The public worktree facade still imports and exports source-onboarding plans and entity/index refresh helpers; metadata-row rewriting was removed. [5]
