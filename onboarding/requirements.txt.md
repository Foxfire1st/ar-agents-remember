# requirements.txt

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `requirements.txt` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

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
to 3.8.0 because root pytest `addopts` enables `-n=auto` for both raw and wrapped runs; the package
metadata admits the same major-version range in its `dev` extra.

### Invariants And Boundaries

- These are development quality-tool pins, not MCP runtime dependencies.
- The pytest-xdist pin and the package `dev` range must remain compatible with the root pytest
  configuration that owns automatic worker selection.
- Ruff must be an identical exact pin here and in `mcp/pyproject.toml`; a permissive range is not a
  reproducible lint contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The checkout pins pytest-xdist 3.8.0 with the other quality tools. | "pytest-xdist==3.8.0" | requirements.txt:10-10 |
| The package development extra admits pytest-xdist 3.x, and root pytest configuration enables automatic worker selection. | "pytest-xdist>=3,<4"; "-n=auto" | mcp/pyproject.toml:64-64; pyproject.toml:133-133 |
| The checkout requirements pin Ruff 0.16.1 exactly. | "ruff==0.16.1" | requirements.txt:1-8 |
| The package development extra independently pins the same Ruff release. | "\"ruff==0.16.1\"," | mcp/pyproject.toml:67-67 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: aligned the checkout and package development
  entry points on exact Ruff 0.16.1 after master integration exposed a stable-rule mismatch.

- 2026-08-12T00:20+02:00 — Corrected ownership: the checkout pin supplies pytest-xdist 3.8.0,
  while root pytest `addopts` owns the automatic worker default. Verification metadata remains
  blank until governed closeout stamps the real code commit.

- 2026-08-11T23:56+02:00 — Created from the current checkout-level quality-tool pin set after
  pytest-xdist 3.8.0 became the executor for the repository's `-n auto` pytest rail. Verification
  metadata remains blank until governed closeout stamps the real code commit.
