# mcp/src/agents_remember/code_quality/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/code_quality/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T16:10+02:00                     |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32` |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`__init__.py` marks `agents_remember.code_quality` as the package-local domain
for source-development quality helpers.

## Code Commentary

### Logic

The package currently exposes helper modules by explicit import. It does not
register MCP tools or runtime behavior.

### Invariants And Boundaries

- Code quality helpers are source-development utilities, not installed
  coordinator runtime behavior.
- Runtime MCP dependencies should not grow just because a development helper
  exists in this package.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CRAP-Calculator lives in this package. | `crap_score` | mcp/src/agents_remember/code_quality/crap_calculator.py:89-92 |
| The source quality suite wrapper lives in this package. | `quality_steps` | mcp/src/agents_remember/code_quality/check.py:320-366 |
| The changed-lines coverage floor lives in this package. | `DEFAULT_DIFF_COVERAGE_FLOOR` | mcp/src/agents_remember/code_quality/diff_coverage.py:30-30 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 3 citation items; scoped citation check now passes.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 **mechanical only, attested**. The leaf's only edit
  to this file was the whole-tree `ruff format` in `00e8379`, which removed a trailing blank
  line; the module is still the one-line package docstring it was. Every claim on this card
  was re-read against the file and remains true, so the prose was not rewritten. One factual
  addition: `diff_coverage.py` joined the package, so it is now listed beside its two
  siblings. `complexity_baseline.py` was created and deleted inside this leaf and never
  needs a row here. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.

- 2026-05-24T06:30+02:00: Updated after adding the source quality suite wrapper.
- 2026-05-24T06:05+02:00: Created for the code quality helper package.
