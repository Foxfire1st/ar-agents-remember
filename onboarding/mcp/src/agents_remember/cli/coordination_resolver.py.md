# mcp/src/agents_remember/cli/coordination_resolver.py

## Governing Overview

[root overview](../../../../overview.md) — moved from `kernel/coordination_context/cli.py` by
260731-EFA-L9 so the resolver CLI sits in the `cli` package above kernel.

## Purpose

`coordination_resolver.py` owns command-line argument parsing for the package-local `c-08-ar-coordination-context-resolver` skill resolver
entrypoint.

## Code Commentary

### Logic

`main()` builds an `argparse` parser, forwards parsed arguments to
`resolve_coordination_context()`, and emits either JSON through
`context_to_dict()` or tab-separated text through `print_text()`.

The CLI flags are unchanged, but since 260731-EFA-L2 `main()` **packs them into the resolver's two
parameter objects**, nested in one `CoordinationRequest` with `WorktreeContractReader`, rather than passing nine keywords: `--topology` / `--coordination-root` /
`--settings-path` / `--onboarding-root` become a `CoordinationHints`, and `--contract-path` /
`--task-name` / `--parent-task` / `--leaf-id` / `--worktree-name` become an `EnclosureSelector`.
`code_repository_name`, `workspace_root` and `code_repository_root` are still passed directly.
This file is where the flag-to-bundle mapping is defined; a new resolver input needs a flag here
and a field on the matching bundle in `models.py`.

The package CLI shares `context_to_dict` with the resolver serialization owner, including external, internal and contract-backed fields (`contract_path`, `worktree_group`, `code_worktree`). Task lookup excludes archive roots; `--parent-task` disambiguates nested active roots and `--leaf-id` selects the exact enclosure. These are resolver decisions, not a CLI-side search implementation. See `mcp/src/agents_remember/cli/coordination_resolver.py:59-109` and `mcp/src/agents_remember/kernel/coordination_context/serialize.py:88-90`.

### Invariants And Boundaries

- The CLI is an adapter only; resolver decisions remain in `resolver.py`.
- Parser errors are reported as command-line errors, preserving the old
  `python -m agents_remember.kernel.coordination_context_resolver` behavior.

## Evidence

### Docs References

No external documentation is needed for this standard-library CLI adapter.

No relevant external documentation is needed.

### Repo-Internal References

- The public facade delegates its module entrypoint to this CLI. [1]

### Cross-Repo References

No cross-repository evidence is needed for this CLI adapter.

No meaningful cross-repo references found.

## Series-Contract Notes

The CLI mirrors the resolver API by accepting `--parent-task` and `--leaf-id`; `--contract-path` now means an explicit `series-contract.md` path rather than the retired task-root `contract.md`.
