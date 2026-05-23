# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `examples/mcp`                             |
| lastUpdated            | 2026-05-23T05:35+02:00                     |
| lastVerifiedCommitHash | `7ab4b520b9178a31c4a5f5f8a5393b9b6ba82e0e` |
| lastVerifiedCommitDate | 2026-05-23T00:34:51+02:00                  |

## Purpose

`examples/mcp/` contains the MCP authority settings template. This route
replaces the removed coordinator `system/settings.json` provider example.

## Current Model

The example names one coordination root, one workspace root, allowed repository
ids, allowed provider ids, transcript log root, and timeout caps. Provider
entries stay empty because the MCP server derives provider runtime roots, data
roots, logs, venvs, binaries, backends, and watch settings internally.

