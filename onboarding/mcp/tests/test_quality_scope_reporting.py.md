# mcp/tests/test_quality_scope_reporting.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_scope_reporting.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Defines the module-level API of test_quality_scope_reporting.py.

## Code Commentary

### Logic

Module-level surface:

- `run_git` (function, lines 27-34)
- `write_quality_config` (function, lines 37-57)
- `sample_repository` (function, lines 60-87)
- `config_for` (function, lines 90-97)
- `digest_text` (function, lines 100-101)
- `digest_bytes` (function, lines 104-105)
- `workflow_run_blocks` (function, lines 108-132)
- `WrapperScopeOutputTests` (class, lines 135-309)
- `ConfigTruthTests` (class, lines 312-343)
- `UntrackedExposureTests` (class, lines 346-516)
- `CallerProvenanceTests` (class, lines 519-705)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `run_git` (lines 27-34). | `run_git` | mcp/tests/test_quality_scope_reporting.py:27-34 |
| Defines the function `write_quality_config` (lines 37-57). | `write_quality_config` | mcp/tests/test_quality_scope_reporting.py:37-57 |
| Defines the function `sample_repository` (lines 60-87). | `sample_repository` | mcp/tests/test_quality_scope_reporting.py:60-87 |
| Defines the function `config_for` (lines 90-97). | `config_for` | mcp/tests/test_quality_scope_reporting.py:90-97 |
| Defines the function `digest_text` (lines 100-101). | `digest_text` | mcp/tests/test_quality_scope_reporting.py:100-101 |
| Defines the function `digest_bytes` (lines 104-105). | `digest_bytes` | mcp/tests/test_quality_scope_reporting.py:104-105 |
| Defines the function `workflow_run_blocks` (lines 108-132). | `workflow_run_blocks` | mcp/tests/test_quality_scope_reporting.py:108-132 |
| Defines the class `WrapperScopeOutputTests` (lines 135-309). | `WrapperScopeOutputTests` | mcp/tests/test_quality_scope_reporting.py:135-309 |
| Defines the class `ConfigTruthTests` (lines 312-343). | `ConfigTruthTests` | mcp/tests/test_quality_scope_reporting.py:312-343 |
| Defines the class `UntrackedExposureTests` (lines 346-516). | `UntrackedExposureTests` | mcp/tests/test_quality_scope_reporting.py:346-516 |
| Defines the class `CallerProvenanceTests` (lines 519-705). | `CallerProvenanceTests` | mcp/tests/test_quality_scope_reporting.py:519-705 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
