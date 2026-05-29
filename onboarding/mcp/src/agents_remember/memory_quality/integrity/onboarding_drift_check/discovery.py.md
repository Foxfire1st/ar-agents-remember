# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `12737deaac2fd75563ca1e3037cdac911023cf93` |
| lastVerifiedCommitDate | 2026-05-29T12:28:42+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`discovery.py` finds onboarding artifacts and parses their pipe-table metadata.
It is a parsing/discovery helper with no git or side effects, shared by the
classifiers.

## Code Commentary

### Logic

`parse_table_metadata` reads the leading metadata table; `is_file_level_onboarding`
and `is_supported_sidecar_onboarding` gate by `doc_type`; `discover_onboarding_files`
rglobs supported sidecars; `mirror_onboarding_path` maps a source path to its
mirrored sidecar; `normalize_overview_route` canonicalizes overview routes; `rel`
relativizes a path against the onboarding root.

### Invariants And Boundaries

- Pure discovery/parsing: no git calls, no mutation, no policy decisions.
- Foundational for `report`, `entities`, and `sidecar`; depends only on `models`
  and the kernel resolver helpers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `sidecar.py` and `entities.py` parse metadata and relativize paths through these helpers. | [sidecar.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py) |
| Path normalization is provided by the kernel resolver. | [coordination_context_resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |

## Update History

- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
