# mcp/src/agents_remember/mcp/__init__.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

Defines package-level MCP server identity constants used by public payload
builders.

## Code Commentary

The module exposes `SERVER_NAME` and `SERVER_VERSION`. `SERVER_VERSION` is now
derived from the installed package metadata via
`importlib.metadata.version("agents-remember-mcp")`, making `mcp/pyproject.toml`
the single source of truth; a `PackageNotFoundError` fallback hardcodes the
current release version for source checkouts without an install (bumped in
lockstep with pyproject at every release). Payload builders in `mcp.tools` use
those constants for `ping` and `server_info`, so the version no longer needs a
manual bump here — keep `mcp/pyproject.toml` and the source-checkout fallback in
sync at release.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- `ping_payload()` and `server_info_payload()` report `SERVER_VERSION`. [1]
- Tool tests assert the public version reported by `ping_payload()`. [2]
