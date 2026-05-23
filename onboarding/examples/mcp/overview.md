# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `examples/mcp`                             |
| lastUpdated            | 2026-05-24T00:37+02:00                     |
| lastVerifiedCommitHash | `ddf6fcd5981664813c915e94e1c5229b542a28a4` |
| lastVerifiedCommitDate | 2026-05-24T00:25:39+02:00                  |

## Purpose

`examples/mcp/` contains the MCP authority settings template. This route
replaces the removed coordinator `system/settings.json` provider example.

## Current Model

The example names one coordination root, one workspace root, allowed repository
ids, allowed provider ids, transcript log root, and timeout caps. Repository
source roots are derived from `workspaceRoot/<repo-id>`, and external memory
roots are derived from `coordinationRoot/memory-repos/ar-<repo-id>`. Provider
entries stay empty because the MCP server derives provider runtime roots, data
roots, logs, venvs, binaries, backends, and watch settings internally.
