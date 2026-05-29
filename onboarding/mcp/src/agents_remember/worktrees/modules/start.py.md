# mcp/src/agents_remember/worktrees/modules/start.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/start.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns worktree start, attach, status result construction, and startup preparation
for external memory and providers.

## Code Commentary

`start_result()` resolves context, builds the default contract, prepares code
and optional memory worktrees, prepares CGC provider runtime state when MCP
provided settings are present, and writes the contract for real starts. Provider
setup remains typed through `ProviderSetupRequest`; there is no coordinator
script or host-binary fallback path here.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider setup requests are implemented by the providers package. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |
| Worktree tests cover memory compatibility, disabled-memory choices, and dirty external-memory blocking. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-05-29T18:35+02:00: `_load_memory_ledger` returns `MemoryLedger | dict[str, object]` so `prepare_memory_for_start` narrows the ledger before `find_mapping`/attribute access; behavior-preserving (commit `0549b28`).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
