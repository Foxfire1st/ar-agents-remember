# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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

| Finding | Source Path |
| --- | --- |
| `sidecar.py` and `entities.py` parse metadata and relativize paths through these helpers. | [sidecar.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py) |
| Path normalization is provided by the kernel resolver. | [coordination_context_resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |

## Update History

- 2026-05-31T12:30+02:00 — Dropped citation of removed `is_file_level_onboarding` helper from Logic (1.0.0 review remediation).
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
