# mcp/src/agents_remember/mcp/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/__init__.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-04T18:52+02:00                     |
| lastVerifiedCommitHash | `66a79a4f111b83c74a35556ca29b0ae51b1ed69e` |
| lastVerifiedCommitDate | 2026-06-04T19:03:03+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

Defines package-level MCP server identity constants used by public payload
builders.

## Code Commentary

The module exposes `SERVER_NAME` and `SERVER_VERSION`. `SERVER_VERSION` is now
derived from the installed package metadata via
`importlib.metadata.version("agents-remember-mcp")`, making `mcp/pyproject.toml`
the single source of truth; a `PackageNotFoundError` fallback hardcodes `2.3.2`
for source checkouts without an install. Payload builders in `mcp.tools` use
those constants for `ping` and `server_info`, so the version no longer needs a
manual bump here — keep `mcp/pyproject.toml` and the source-checkout fallback in
sync at release.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `ping_payload()` and `server_info_payload()` report `SERVER_VERSION`. | [tools/core.py](agents-remember-md/mcp/src/agents_remember/mcp/tools/core.py) |
| Tool tests assert the public version reported by `ping_payload()`. | [test_tools.py](agents-remember-md/mcp/tests/test_tools.py) |

## Update History

- 2026-06-04T18:52+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.3.2` for the runtime skill refresh patch; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-03T19:25+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.3.1` for the MCP package README correction patch; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-03T18:58+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.3.0` for the harness starter-package / package-first install ergonomics release; pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-03T04:25+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.2.0` (mcp 2.2.0 release); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-02T18:35+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.1.0` (mcp 2.1.0 release); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-02T05:10+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `2.0.0` (mcp 2.0.0 — the `l-01-session-job-lifecycle` skill lifecycle reshape, a major/breaking release); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-02T03:30+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `1.0.2` (mcp 1.0.2); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Bumped the source-checkout `SERVER_VERSION` fallback to `1.0.1` (mcp 1.0.1); pyproject remains the single source of truth. Verification metadata pinned until closeout.
- 2026-05-31T12:30+02:00 — `SERVER_VERSION` now reads from installed package metadata (`importlib.metadata.version`) with a `1.0.0` source-checkout fallback; pyproject is the single source of truth (1.0.0 review remediation).
- 2026-05-31T01:06+02:00: Bumped `SERVER_VERSION` to `0.9.6` (MCP 0.9.6); still aligned with `mcp/pyproject.toml`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T22:29+02:00: Bumped `SERVER_VERSION` to `0.9.5` for the S6 token-counter release; still aligned with `mcp/pyproject.toml`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T21:33+02:00: Verified `SERVER_VERSION` is `0.9.4` after the 0.9.0–0.9.4 run; still aligned with `mcp/pyproject.toml`. Repaired the broken builder reference — the former single `mcp/tools.py` was split into the `mcp/tools/` package at `01f503d`, so `ping_payload`/`server_info_payload` now live in `tools/core.py`.
- 2026-05-29T21:00+02:00: Bumped `SERVER_VERSION` to `0.3.0` for the MCP `0.3.0` release (the act-by-default `dry_run` flip), kept aligned with `mcp/pyproject.toml`.
- 2026-05-28T15:43+02:00: Created while preparing MCP package release `0.2.0`. Verification metadata remains pinned until closeout commits the source change.
