# mcp/tests/test_leaf_structural_coverage.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_leaf_structural_coverage.py`                  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                   |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[tests overview](overview.md)

## Purpose

`mcp/tests/test_leaf_structural_coverage.py` covers structural-leaf seams not exercised by the
domain suites, including the L9 layering CLI/edges/render/stale behavior, coordination-resolver
CLI in-process execution, version fallback, gate vocabulary errors, drift-snapshot removal edges,
resolver reader-failure edges, and terminal-catalog method branches.

## Code Commentary

### Logic

Key L9 tests: `test_layering_cli_and_edges` (cit:([`test_layering_cli_and_edges`], mcp/tests/test_leaf_structural_coverage.py:83-83)),
`test_layering_import_target_edges` (cit:([`test_layering_import_target_edges`], mcp/tests/test_leaf_structural_coverage.py:122-122)),
`test_layering_render_and_stale` (cit:([`test_layering_render_and_stale`], mcp/tests/test_leaf_structural_coverage.py:140-140)) — the cycle and
`present=false` behavior (reviewer F-4); `test_coordination_resolver_cli_in_process`
(cit:([`test_coordination_resolver_cli_in_process`], mcp/tests/test_leaf_structural_coverage.py:169-169)); `test_resolver_missing_reader_and_contract_edges`
(cit:([`test_resolver_missing_reader_and_contract_edges`], mcp/tests/test_leaf_structural_coverage.py:247-247)); and `test_terminal_catalog_method_branches`
(cit:([`test_terminal_catalog_method_branches`], mcp/tests/test_leaf_structural_coverage.py:298-298)).

### Invariants And Boundaries

- This suite exists because the diff-coverage floor is 100% with no exemption list: any new
  structural seam must be reached here or in a domain suite.

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
| The suite complements the layering unit tests with wrapper-adjacent seams. | `test_layering_cli_and_edges` | mcp/tests/test_leaf_structural_coverage.py:83-83 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the structural-coverage suite;
  F-4 cycle-coverage note reflected. Verification metadata pinned until closeout stamps the L9
  code commit.
