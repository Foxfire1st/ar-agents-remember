# mcp/tests/test_layering.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_layering.py`                                  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                   |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[tests overview](overview.md)

## Purpose

`mcp/tests/test_layering.py` is the unit suite for the `layers.toml` layering fitness function
(260731-EFA-L9 R12): rank violations fail, clean trees pass, undeclared packages/imports fail
closed, and self/star/present-false imports are skipped.

## Code Commentary

### Logic

`test_rank_violation_fails` (cit:([`test_rank_violation_fails`], mcp/tests/test_layering.py:47-47)) proves an upward import fails;
`test_undeclared_package_directory_fails` (cit:([`test_undeclared_package_directory_fails`], mcp/tests/test_layering.py:108-108)) and
`test_undeclared_package_import_fails` (cit:([`test_undeclared_package_import_fails`], mcp/tests/test_layering.py:156-156)) pin the F-3 fail-closed
hardening; `test_generated_and_data_dirs_are_not_undeclared`
(cit:([`test_generated_and_data_dirs_are_not_undeclared`], mcp/tests/test_layering.py:132-132)) proves `__pycache__`/`package_data`/dot-directories
are excluded, including a deleted package directory whose only remaining content is cached bytecode;
the self/star/present-false tests pin the skip rules.

### Invariants And Boundaries

- Cycle coverage rides `test_leaf_structural_coverage.py`, not this file (reviewer F-4 note).

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The enforced contract lives in `layers.toml`. | "[contract]" | layers.toml:19-19 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: extended the ignored-artifact regression with
  cache-only deleted-package debris while retaining undeclared real-source coverage.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the layering unit suite; F-3
  branches and F-4 cycle-coverage note reflected. Verification metadata pinned until closeout
  stamps the L9 code commit.
