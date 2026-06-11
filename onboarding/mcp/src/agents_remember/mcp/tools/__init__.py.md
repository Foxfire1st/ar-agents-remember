# mcp/src/agents_remember/mcp/tools/__init__.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember-md                               |
| path                   | `mcp/src/agents_remember/mcp/tools/__init__.py`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-10T09:56+02:00|
| lastVerifiedCommitHash | `a69b72e101d09423601916c03d4f59ecdee7dda6`                                        |
| lastVerifiedCommitDate | 2026-06-11T11:08:18+02:00|
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

- 2026-06-11T06:47+02:00 — No content impact: `direct_closeout_preview_payload`/`direct_closeout_apply_payload` left the facade exports (issue #62 worktree-only closeout) exactly per the documented re-export pattern; the facade contract this sidecar describes is unchanged.
- 2026-06-10T09:56+02:00 — No content impact: `worktree_sync_payload` joined the facade exports (GitHub #54 sub-task D) exactly per the documented re-export pattern; the facade contract this sidecar describes is unchanged.
- 2026-06-01T20:45+02:00 — Added `worktree_abandon_payload` to the tools-package facade exports for the new abandon tool.
- 2026-05-29T18:35+02:00: Created as the package facade when `mcp/tools.py` was split (commit `01f503d`).
