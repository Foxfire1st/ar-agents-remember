# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`discovery.py` finds onboarding artifacts and parses their pipe-table metadata.
It is a parsing/discovery helper with no git or side effects, shared by the
classifiers.

## Code Commentary

### Logic

`parse_table_metadata` reads the leading metadata table;
`is_supported_sidecar_onboarding` gates by `doc_type`; `discover_onboarding_files`
rglobs supported sidecars; `mirror_onboarding_path` maps a source path to its
mirrored sidecar; `normalize_overview_route` canonicalizes overview routes; `rel`
relativizes a path against the onboarding root.

### Invariants And Boundaries

- Pure discovery/parsing: no git calls, no mutation, no policy decisions.
- Foundational for `report`, `entities`, and `sidecar`; depends only on `models`
  and the kernel resolver helpers.

## Evidence

### Repo-Internal References

- Sidecar and entity discovery classify metadata, normalize paths, and parse entity evidence through these helpers. [1]
- Path normalization is provided by the kernel resolver. [2]
