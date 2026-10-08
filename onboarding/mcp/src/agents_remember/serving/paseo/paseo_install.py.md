# mcp/src/agents_remember/serving/paseo/paseo_install.py

## Governing Overview

[overview](../overview.md)

## Purpose

The host part of `runtime_install`: it reads the shared host block at call time, runs the provision or a strictly read-only preview, and returns the host part of the install result.

## Code Commentary

`install_host` returns `configured: false` and the message naming the block when the shared settings hold none. `preview_host` observes without a lock, download, npm run, setting write or daemon start and reports what would change, the Node it would install and whether a restart holds it back. A failure returns the typed error payload while the earlier install steps stand.

## Evidence

- The install host entry point and its configured/absent result. [1]
- The read-only preview that makes no changing call. [2]
