# mcp/src/agents_remember/kernel/coordination_context/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`cli.py` owns command-line argument parsing for the package-local `c-08-ar-coordination-context-resolver` skill resolver
entrypoint.

## Code Commentary

### Logic

`main()` builds an `argparse` parser, forwards parsed arguments to
`resolve_coordination_context()`, and emits either JSON through
`context_to_dict()` or tab-separated text through `print_text()`.

### Invariants And Boundaries

- The CLI is an adapter only; resolver decisions remain in `resolver.py`.
- Parser errors are reported as command-line errors, preserving the old
  `python -m agents_remember.kernel.coordination_context_resolver` behavior.

## Docs References

No external documentation is needed for this standard-library CLI adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The public facade delegates its module entrypoint to this CLI. | facade entrypoint | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |

## Cross-Repo References

No cross-repository evidence is needed for this CLI adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The CLI mirrors the resolver API by accepting `--parent-task` and `--leaf-id`; `--contract-path` now means an explicit `series-contract.md` path rather than the retired task-root `contract.md`.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the CLI now describes `series-contract.md`, accepts `--parent-task` and `--leaf-id`, and resolves task names under active task roots with `0_archive` excluded. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-25T20:57+02:00: Created by extracting the resolver command-line adapter from the monolithic facade.
