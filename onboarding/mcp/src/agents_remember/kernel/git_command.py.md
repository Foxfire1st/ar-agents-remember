# mcp/src/agents_remember/kernel/git_command.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/src/agents_remember/kernel/git_command.py`           |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-07-18T20:03+02:00                                   |
| lastVerifiedCommitHash | `7ca29c3b6dd2c0184253e2690f1ebe78c511573b`               |
| lastVerifiedCommitDate | 2026-07-18T20:18:51+02:00|
| governingOverview      | `../../../overview.md`                                   |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

`git_command.py` is the shared low-level Git subprocess boundary for package kernel and memory
services. It fixes command isolation, decoding, stdin, and timeout behavior in one place.

## Code Commentary

### Logic

`git_environment()` copies the process environment and removes all eight repository-selection
variables: `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
`GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, and `GIT_PREFIX`.
`run_git()` injects `safe.directory`, runs at the supplied repository root with `stdin=DEVNULL`,
captures output as UTF-8 with `surrogateescape`, applies the scrubbed environment, enforces a
five-second timeout, and returns non-zero outcomes for typed interpretation by its caller.

### Conventions

The selector tuple is production authority and is imported by tests instead of copied. Repository
paths are rendered with `as_posix()` for stable Git configuration values. The module stays standard-
library-only and does not interpret Git records.

### Invariants And Boundaries

- Ambient repository selectors must never redirect a command away from the explicit `repo_root`.
- UTF-8 `surrogateescape` is required so NUL-delimited Git records retain non-UTF-8 path identity.
- `check=False` is intentional: callers translate return codes and stderr into their domain's typed
  failure without losing evidence.
- The timeout and `stdin=DEVNULL` are process-boundary requirements, not speculative fallback paths.
- Root validation, census parsing, and containment belong to callers such as
  `route_index_census.py`; this runner only executes the bounded command.

### Todos

None known for the MX-FIX-4 Git command boundary.

## Docs References

No Domain Documentation source is configured for this repository. Git behavior is verified by the
package's production-path regression matrix.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The deterministic route-index census consumes NUL-delimited output from this runner and preserves typed causes. | L1-L226 | [route_index_census.py](agents-remember/mcp/src/agents_remember/kernel/route_index_census.py) |
| Carryover uses the same scrubbed environment for its separate input-bearing Git adapter. | Git runner | [carryover.py](agents-remember/mcp/src/agents_remember/memory/carryover.py) |
| Tests import the production selector inventory and cover every selector. | L34-L39; L595-L644 | [conftest.py](agents-remember/mcp/tests/conftest.py); [test_route_index.py](agents-remember/mcp/tests/test_route_index.py) |

## Cross-Repo References

The runner can execute against configured code or external-memory repositories, but no sibling
repository defines this implementation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the authoritative selector scrub and
  surrogate-preserving output boundary used by deterministic route-index census and carryover.
- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
