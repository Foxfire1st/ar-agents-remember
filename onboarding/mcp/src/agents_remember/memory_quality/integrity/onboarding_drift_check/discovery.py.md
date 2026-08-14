# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../../../../overview.md`               |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `sidecar.py` and `entities.py` parse metadata and relativize paths through these helpers. | `classify_sidecar_onboarding_units`, `parse_table_metadata`, `normalize_rel_path`, `parse_entity_fingerprint_rows`, `classify_entity_catalog` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:289-342; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py:17-32; mcp/src/agents_remember/kernel/coordination_context/paths.py:38-39; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:84-113; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:313-386 |
| Path normalization is provided by the kernel resolver. | `normalize_rel_path` | mcp/src/agents_remember/kernel/coordination_context/paths.py:38-39 |

## Update History

- 2026-08-03T03:59:59+02:00 — Curated 4 citation claims (2 table rows, 2 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-05-31T12:30+02:00 — Dropped citation of removed `is_file_level_onboarding` helper from Logic (1.0.0 review remediation).
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
