# scripts/pnt_sandbox/build_tool_calls.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

This helper starts the selected build MCP server over stdio with the requested config, checks exact server_info roots/repository scope and absent providers before corpus calls, and skips a creation only when its public probe succeeds. A failed call ends the sequence with a bounded report. The bounded mocked admission unit case (`test_foreign_package_admission_prevents_public_install_calls`) imports and runs this script against a mocked MCP transport; the sequence beyond that admission seam remains untested at unit level.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
