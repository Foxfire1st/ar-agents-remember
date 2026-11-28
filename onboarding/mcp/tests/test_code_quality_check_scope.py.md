# mcp/tests/test_code_quality_check_scope.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Explicit product/verification package ownership tests and root `[tool.pyrefly]` scope and CLI exclusion tests.

## Code Commentary

### Logic

A newly importable support package refuses until assigned a product or verification owner. Declaring it verification preserves lint/type inclusion while excluding it from product coverage paths. Overlapping and stale ownership declarations refuse.

`PyreflyScopeConfigurationTests` validates root `pyproject.toml` via `validate_quality_config`, asserts `project-includes = [".", ".dagger"]` and `disable-project-excludes-heuristics = true`, verifies all twelve depth-independent `**/` `project-excludes` entries and the absence of blanket dot-folder patterns, and confirms that zero tracked `*.py` files (including `.dagger/`) match any `project-excludes` entry. It also runs Pyrefly with `--force-exclude --python-interpreter-path` against temporary checkouts to verify that an explicit CLI file list checks listed files outside `project-includes`, that `--force-exclude` drops explicitly listed files matching `project-excludes` while keeping tracked paths including `.dagger/` checked, and that a bare run with `project-includes = [".", ".dagger"]` skips nested `mcp/.venv` and `dashboard/node_modules` while checking checkout code including `.dagger/`.

### Conventions

Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Coverage paths describe measurement scope, not a percentage requirement. No fallback ownership broadening is allowed for unowned packages. `[tool.pyrefly] project-excludes` patterns must stay disjoint from tracked Python files because Pyrefly `--force-exclude` drops explicitly listed paths that match `project-excludes`, and no blanket dot-folder pattern is permitted while tracked Python lives under `.dagger/`.

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

- Root `[tool.pyrefly]` validates cleanly, excludes nested environments/caches without blanket dot-folder rules, and matches zero tracked Python files including `.dagger/`. [3]
- Real Pyrefly runs verify CLI file lists check listed files outside `project-includes`, `--force-exclude` drops excluded paths while keeping `.dagger/` checked, and bare runs skip nested environments while checking checkout code including `.dagger/`. [4]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
