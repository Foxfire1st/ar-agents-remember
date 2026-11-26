# mcp/tests/test_code_quality_check_scope.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Explicit product/verification package ownership tests and root `[tool.pyright]` scope and CLI exclusion tests.

## Code Commentary

### Logic

A newly importable support package refuses until assigned a product or verification owner. Declaring it verification preserves lint/type inclusion while excluding it from product coverage paths. Overlapping and stale ownership declarations refuse.

`PyrightScopeConfigurationTests` validates root `pyproject.toml` via `validate_quality_config`, asserts `include = ["."]`, verifies all eleven depth-independent `**/` `exclude` entries and the absence of blanket dot-folder patterns, and confirms that zero tracked `*.py` files (including `.dagger/`) match any `exclude` entry. It also runs Pyright against temporary checkouts to verify that a CLI file list replaces `include`, that `exclude` still filters explicitly listed paths (`filesAnalyzed == 0` when excluded) while non-dot tracked paths (`scripts/script_err.py`) stay checked (accounting for Pyright `1.1.414+` auto-excluding `**/.*` independently of `[tool.pyright] exclude`), that a bare run checks checkout code outside excluded trees while skipping nested `mcp/.venv` and `dashboard/node_modules`, and that explicit file-list invocations match the legacy top-level `exclude` list identically.

### Conventions

Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Coverage paths describe measurement scope, not a percentage requirement. No fallback ownership broadening is allowed for unowned packages. `[tool.pyright] exclude` patterns must stay disjoint from tracked Python files because Pyright drops explicitly listed paths that match `exclude`, and no blanket dot-folder pattern is permitted while tracked Python lives under `.dagger/`.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- New importable package requires explicit product or verification owner. [1]
- Package authority rejects overlap and stale declarations. [2]

- Root `[tool.pyright]` validates cleanly, excludes nested environments/caches without blanket dot-folder rules, and matches zero tracked Python files including `.dagger/`. [3]

- Real Pyright runs verify CLI file lists replace `include`, `exclude` still filters listed paths, non-dot tracked paths stay checked under Pyright `1.1.414+`, bare runs skip nested environments, and file-list results match legacy excludes. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
