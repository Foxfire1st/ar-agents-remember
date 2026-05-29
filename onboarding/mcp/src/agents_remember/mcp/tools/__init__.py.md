# mcp/src/agents_remember/mcp/tools/__init__.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember-md                               |
| path                   | `mcp/src/agents_remember/mcp/tools/__init__.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2`                                        |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Facade that preserves the public import surface of the former `mcp/tools.py`.

## Code Commentary

### Logic

Re-exports the shared constants and `_tool_payload` from `base`, and every
`*_payload` builder from the domain submodules (`core`, `memory`, `providers`,
`worktree`, `benchmark`). `__all__` lists the public builders and constants.

### Invariants And Boundaries

- Consumers import builders from `agents_remember.mcp.tools` regardless of which
  submodule owns them; the facade must keep re-exporting the full set.
- `_tool_payload` is re-exported with `from .base import _tool_payload as
  _tool_payload` so the conformance test's `tools._tool_payload` attribute
  access resolves and Ruff/Pyright treat it as an intentional re-export.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Conformance test reaches `tools._tool_payload`. | [test_tool_response_conformance.py](agents-remember-md/mcp/tests/test_tool_response_conformance.py) |

## Update History

- 2026-05-29T18:35+02:00: Created as the package facade when `mcp/tools.py` was split (commit `01f503d`).
