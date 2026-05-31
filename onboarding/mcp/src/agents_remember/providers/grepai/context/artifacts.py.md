# mcp/src/agents_remember/providers/grepai/context/artifacts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/grepai/context/artifacts.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:33+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`grepai/artifacts.py` detects, validates, and removes disposable GrepAI root artifacts from indexed memory roots.

## Code Commentary

### Logic

It finds configured GrepAI artifact names under each indexed root, raises `ContextProviderError` when artifacts are present during integrity checks, and removes only direct-child artifacts that match the known GrepAI artifact name set.

### Invariants And Boundaries

- Cleanup is limited to direct children of the configured root and currently only targets `.grepai`.
- Removal goes through shared `remove_runtime_path`, preserving the dry-run behavior used by provider cleanup tooling.
- Unexpected paths are rejected before deletion.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Artifact names come from the GrepAI constants module. | [constants.py](constants.py.md) |

## Update History

- 2026-05-31T12:40+02:00: Removed the stale provider-integrity reference row after `providers/integrity.py` was deleted in the 1.0.0 remediation; the exported artifact assertion currently has no caller.
- 2026-05-25T19:33+02:00: Created when GrepAI root artifact checks were split out of `grepai/core.py`.
