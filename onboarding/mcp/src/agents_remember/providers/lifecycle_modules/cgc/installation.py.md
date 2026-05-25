# mcp/src/agents_remember/providers/lifecycle_modules/cgc/installation.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/cgc/installation.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`installation.py` owns CodeGraphContext install, status, patch, and doctor
operations.

## Code Commentary

### Logic

The module installs the CGC Python dependency set, cleans old source artifacts,
applies local compatibility patches to the installed CGC package, reports patch
status, initializes runtime layout state, and runs doctor checks. Install-all
also coordinates backend installation and per-root install results from
settings.

### Invariants And Boundaries

- Patches are checked and applied explicitly; status should report which patch
  IDs are present.
- Runtime source artifacts under the code repository are cleanup targets; active
  provider runtime belongs under coordinator provider roots.
- Process start/stop and bounded CGC commands belong in `process.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC layout and backend settings come from the CGC core module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/core.py) |
| CGC backend install/start behavior is delegated to the backend module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/backend.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from CGC install, status, patch, and doctor logic extracted out of provider lifecycle.
