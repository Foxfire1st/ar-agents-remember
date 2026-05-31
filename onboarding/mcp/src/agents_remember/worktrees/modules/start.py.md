# mcp/src/agents_remember/worktrees/modules/start.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/start.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree start, attach, status result construction, and startup preparation
for external memory and providers.

## Code Commentary

Every entry point and helper takes the typed `WorktreeArgs` dataclass (imported
from `agents_remember.worktrees.modules.args`), replacing the former
`argparse.Namespace`; `import argparse` is gone. `start_result()` resolves
context, builds the default contract, prepares code and optional memory
worktrees, prepares provider runtime state when MCP-provided settings are
present, and writes the contract for real starts. `_build_start_contract`
asserts `args.task_name`/`args.worktree_name` are non-`None`, and
`_provider_start_paths` asserts `args.provider_setup_config` is non-`None`,
before use. Provider setup remains typed through `ProviderSetupRequest`; there is
no coordinator script or host-binary fallback path here. `provider_setup.load_settings`
and `provider_setup.settings_path` are now called with the settings path alone
(the `target_coordination_root` argument was dropped), and the dead
`_cgc_enablement_state` helper was removed in favour of the unified
`_provider_enablement_state`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Defines the `WorktreeArgs` dataclass that types every start/attach/status input. | [args.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/args.py) |
| Provider setup requests are implemented by the providers package. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |
| Worktree tests cover memory compatibility, disabled-memory choices, and dirty external-memory blocking. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-31T12:50+02:00 — Re-typed every `args` param from `argparse.Namespace` to the new `WorktreeArgs` dataclass (dropping `import argparse`), added `task_name`/`worktree_name`/`provider_setup_config` non-`None` asserts, switched `provider_setup.load_settings`/`settings_path` to the path-only signature, and removed the dead `_cgc_enablement_state` helper; corrected Code Commentary and added the args.py reference (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `_load_memory_ledger` returns `MemoryLedger | dict[str, object]` so `prepare_memory_for_start` narrows the ledger before `find_mapping`/attribute access; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
