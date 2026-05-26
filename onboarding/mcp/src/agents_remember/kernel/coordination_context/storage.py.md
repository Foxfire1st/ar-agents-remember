# mcp/src/agents_remember/kernel/coordination_context/storage.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/storage.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
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
`disabled`, or the hybrid default for unmatched files.

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

- 2026-05-25T20:57+02:00: Created by extracting source storage/path-rule evaluation from the C-08 resolver.
