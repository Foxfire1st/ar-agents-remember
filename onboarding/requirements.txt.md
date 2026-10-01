# requirements.txt

## Governing Overview

[repository overview](overview.md)

## Purpose

`requirements.txt` pins the checkout-level Python quality tools used to run the repository-owned
quality gate reproducibly.

## Code Commentary

### Logic

The file pins Ruff, Radon, Coverage.py, pytest, pytest-cov, and pytest-xdist. Ruff is pinned
exactly to 0.16.1 so the checkout cannot silently run a different stable rule set from the package
development extra; this matters because `PLR0917` became stable in Ruff 0.16.0. pytest-xdist is pinned
to 3.8.0 because root pytest `addopts` enables `-n=4` for both raw and wrapped runs; the package
metadata admits the same major-version range in its `dev` extra.

### Invariants And Boundaries

- These are development quality-tool pins, not MCP runtime dependencies.
- The pytest-xdist pin and the package `dev` range must remain compatible with the root pytest
  configuration that owns automatic worker selection.
- Ruff must be an identical exact pin here and in `mcp/pyproject.toml`; a permissive range is not a
  reproducible lint contract.

## Evidence

### Repo-Internal References

- The checkout pins pytest-xdist 3.8.0 with the other quality tools. [1]
- Root pytest configuration selects four workers by default. [2]
- The checkout requirements pin Ruff 0.16.1 exactly. [3]
- The package development extra independently pins the same Ruff release. [4]
