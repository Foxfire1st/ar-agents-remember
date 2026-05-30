# mcp/src/agents_remember/mcp/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/__init__.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T22:29+02:00                     |
| lastVerifiedCommitHash | `5ccfed5b722ee34158b9533fb7e86e4196cfb569` |
| lastVerifiedCommitDate | 2026-05-30T22:38:37+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

Defines package-level MCP server identity constants used by public payload
builders.

## Code Commentary

The module currently exposes `SERVER_NAME` and `SERVER_VERSION` (`0.9.5` at this
verification). Payload builders in `mcp.tools` use those constants for `ping`
and `server_info`, so release version bumps must keep `SERVER_VERSION` aligned
with `mcp/pyproject.toml`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `ping_payload()` and `server_info_payload()` report `SERVER_VERSION`. | [tools/core.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/core.py) |
| Tool tests assert the public version reported by `ping_payload()`. | [test_tools.py](agents-remember-md/mcp/tests/test_tools.py) |

## Update History

- 2026-05-30T22:29+02:00: Bumped `SERVER_VERSION` to `0.9.5` for the S6 token-counter release; still aligned with `mcp/pyproject.toml`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T21:33+02:00: Verified `SERVER_VERSION` is `0.9.4` after the 0.9.0–0.9.4 run; still aligned with `mcp/pyproject.toml`. Repaired the broken builder reference — the former single `mcp/tools.py` was split into the `mcp/tools/` package at `01f503d`, so `ping_payload`/`server_info_payload` now live in `tools/core.py`.
- 2026-05-29T21:00+02:00: Bumped `SERVER_VERSION` to `0.3.0` for the MCP `0.3.0` release (the act-by-default `dry_run` flip), kept aligned with `mcp/pyproject.toml`.
- 2026-05-28T15:43+02:00: Created while preparing MCP package release `0.2.0`. Verification metadata remains pinned until closeout commits the source change.
