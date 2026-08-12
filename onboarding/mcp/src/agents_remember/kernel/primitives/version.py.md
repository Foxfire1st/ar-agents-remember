# mcp/src/agents_remember/kernel/primitives/version.py

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/kernel/primitives/version.py`         |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-08-08T14:38+02:00                                        |
| lastVerifiedCommitHash | `65cb81f7de4db13c0627264fec1eb46f444e0ee3`                    |
| lastVerifiedCommitDate | 2026-08-12T04:57:26+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/version.py` is the installed package identity (moved from the `mcp` package
root by 260731-EFA-L9). Every layer above kernel may name the server/version without importing
the `mcp` package.

## Code Commentary

### Logic

Defines `SERVER_NAME = "agents-remember"` (cit:([`SERVER_NAME`], mcp/src/agents_remember/kernel/primitives/version.py:11-11)) and re-exports the installed
version via `__version__`.

### Invariants And Boundaries

- Kernel stays importable by every layer; version identity must not drag `mcp` into kernel.

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
| Version fallback behavior is pinned by the structural-coverage suite. | `test_version_fallback` | mcp/tests/test_leaf_structural_coverage.py:189-189 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: re-anchored the version fallback
  proof after the structural test split; documented behavior is unchanged.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the kernel version-identity
  extraction. Verification metadata pinned until closeout stamps the L9 code commit.
