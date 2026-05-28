# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `examples/mcp`                             |
| lastUpdated            | 2026-05-28T15:10:01+02:00                  |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00                  |

## Purpose

`examples/mcp/` contains the MCP authority settings template. This route
replaces the removed coordinator `system/settings.json` provider example.

## Current Model

The example names one coordination root, one workspace root, allowed repository
ids, allowed provider ids, transcript log root, and timeout caps. Repository
source roots are derived from `workspaceRoot/<repo-id>`, and external memory
roots are derived from `coordinationRoot/memory-repos/ar-<repo-id>`. Provider
entries stay empty because the MCP server derives provider runtime roots, data
roots, central logs, Docker backends, and watch settings internally.
