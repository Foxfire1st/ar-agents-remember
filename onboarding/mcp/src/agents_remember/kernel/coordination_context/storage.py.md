# mcp/src/agents_remember/kernel/coordination_context/storage.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/storage.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| JSON settings parsing produces the storage settings and path-rule models. | `parse_json_storage_settings`; `parse_json_path_rules` | mcp/src/agents_remember/kernel/coordination_context/json_settings.py:43-56; mcp/src/agents_remember/kernel/coordination_context/json_settings.py:86-93 |
| The storage resolver consumes `StorageSettings` path rules to select storage for a source. | `resolve_storage_for_source` | mcp/src/agents_remember/kernel/coordination_context/storage.py:103-114 |
| Missing-onboarding checks call the storage resolver through the public facade. | `missing_onboarding_for_source` | mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:88-108 |
| Drift checks classify source onboarding storage through the public facade. | `classify_source` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py:161-195 |

## Cross-Repo References

No cross-repository evidence is needed for storage policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-04T14:01:47+02:00 — 260731-EFA-L6 S18-B01 second same-reviewer residual correction: narrowed the resolver claim to its complete consumer predicate under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-05-31T12:50+02:00 — Renamed the boolean storage-mode predicate `sidecar_storage_label` to `is_sidecar_storage` (signature/return `bool` unchanged); added a Logic note naming the new symbol (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `rule_excludes_source` now returns `bool` via `bool(excludes)` instead of `list[str] | bool`; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:57+02:00: Created by extracting source storage/path-rule evaluation from the `c-08-ar-coordination-context-resolver` skill resolver.
