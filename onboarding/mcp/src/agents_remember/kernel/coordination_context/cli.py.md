# mcp/src/agents_remember/kernel/coordination_context/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

The CLI flags are unchanged, but since 260731-EFA-L2 `main()` **packs them into the resolver's two
parameter objects** rather than passing nine keywords: `--topology` / `--coordination-root` /
`--settings-path` / `--onboarding-root` become a `CoordinationHints`, and `--contract-path` /
`--task-name` / `--parent-task` / `--leaf-id` / `--worktree-name` become an `EnclosureSelector`.
`code_repository_name`, `workspace_root` and `code_repository_root` are still passed directly.
This file is where the flag-to-bundle mapping is defined; a new resolver input needs a flag here
and a field on the matching bundle in `models.py`.

### Invariants And Boundaries

- The CLI is an adapter only; resolver decisions remain in `resolver.py`.
- Parser errors are reported as command-line errors, preserving the old
  `python -m agents_remember.kernel.coordination_context_resolver` behavior.

## Docs References

No external documentation is needed for this standard-library CLI adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public facade delegates its module entrypoint to this CLI. | `resolve_coordination_context` | mcp/src/agents_remember/kernel/coordination_context/resolver.py:151-164 |

## Cross-Repo References

No cross-repository evidence is needed for this CLI adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The CLI mirrors the resolver API by accepting `--parent-task` and `--leaf-id`; `--contract-path` now means an explicit `series-contract.md` path rather than the retired task-root `contract.md`.

## Update History

- 2026-08-03T02:41:30+02:00 — W3-B01 curator: curated 1 Repo-Internal table citation with the current resolver identifier and source path. Verification metadata remains unchanged for closeout.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `main()` now builds `CoordinationHints` and `EnclosureSelector` from the parsed flags and passes
  them as `hints=` / `selector=`. No flag was added, removed or renamed, and the emitted JSON/text
  is identical. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the CLI now describes `series-contract.md`, accepts `--parent-task` and `--leaf-id`, and resolves task names under active task roots with `0_archive` excluded. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-25T20:57+02:00: Created by extracting the resolver command-line adapter from the monolithic facade.
