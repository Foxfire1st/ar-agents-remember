# mcp/src/agents_remember/kernel/coordination_context/storage.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/storage.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`storage.py` resolves onboarding storage mode for a source file using parsed
storage settings and path rules.

## Code Commentary

### Logic

The module normalizes rule bases, evaluates include/exclude glob variants,
handles include and exclude file types, and returns the selected storage mode,
`disabled`, or the hybrid default for unmatched files. The boolean predicate
`is_sidecar_storage()` reports whether a storage mode writes a sidecar
(`repo-sidecar` or `memory-repo`).

### Invariants And Boundaries

- Storage decisions consume already-parsed settings; this module does not read
  settings files.
- Path-rule eligibility is separate from storage location selection.
- In non-hybrid modes, unmatched files resolve to `disabled` when path rules
  exist.

## Docs References

No external documentation is needed for this package-local storage policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| JSON settings parsing produces the path-rule model consumed here. | JSON parser | [json_settings.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/json_settings.py) |
| Missing-onboarding and drift checks call `resolve_storage_for_source()` through the public facade. | integrity checks | [check_missing_onboarding.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py); [drift.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py) |

## Cross-Repo References

No cross-repository evidence is needed for storage policy.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-31T12:50+02:00 — Renamed the boolean storage-mode predicate `sidecar_storage_label` to `is_sidecar_storage` (signature/return `bool` unchanged); added a Logic note naming the new symbol (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `rule_excludes_source` now returns `bool` via `bool(excludes)` instead of `list[str] | bool`; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:57+02:00: Created by extracting source storage/path-rule evaluation from the C-08 resolver.
