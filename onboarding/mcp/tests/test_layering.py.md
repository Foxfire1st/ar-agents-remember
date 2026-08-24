# mcp/tests/test_layering.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_layering.py`                                  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview      | `overview.md`                                                |

## Governing Overview

[tests overview](overview.md)

## Purpose

`mcp/tests/test_layering.py` is the unit suite for the `layers.toml` layering fitness function
(260731-EFA-L9 R12): rank violations fail, clean trees pass, undeclared packages/imports fail
closed, and self/star/present-false imports are skipped.

## Code Commentary

### Logic

`test_rank_violation_fails` (cit:([`test_rank_violation_fails`], mcp/tests/test_layering.py:48-67)) proves an upward import fails;
`test_undeclared_package_directory_fails` (cit:([`test_undeclared_package_directory_fails`], mcp/tests/test_layering.py:109-130)) and
`test_undeclared_package_import_fails` (cit:([`test_undeclared_package_import_fails`], mcp/tests/test_layering.py:157-178)) pin the F-3 fail-closed
hardening; `test_generated_and_data_dirs_are_not_undeclared`
(cit:([`test_generated_and_data_dirs_are_not_undeclared`], mcp/tests/test_layering.py:133-154)) proves `__pycache__`/`package_data`/dot-directories
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

## 260824-PDLS Admission Boundary

The quality-wrapper step registration fixture now carries `QUALITY_TEST_ADMISSION`. Layering remains
a deterministic static rail; the admission field belongs to the shared quality configuration used
by its wrapper proof.

## Update History

- 2026-08-24T21:23+02:00 — Added typed admission to quality-wrapper construction.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: extended the ignored-artifact regression with
  cache-only deleted-package debris while retaining undeclared real-source coverage.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the layering unit suite; F-3
  branches and F-4 cycle-coverage note reflected. Verification metadata pinned until closeout
  stamps the L9 code commit.
