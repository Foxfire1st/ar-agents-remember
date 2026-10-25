# mcp/src/agents_remember/models/runtime.py

## Governing Overview

[overview.md](overview.md)

## Current source contract evidence

- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance.

## Purpose

`runtime.py` defines the flexible `RuntimeInstallResponse` contract. It no longer
declares a resolver-response model: mounted orientation is `context_packet`,
not a second response shape in this file.

## Code Commentary

`RuntimeInstallResponse` remains flexible because install reports include
summary and message blocks from installer services; since 2.5.1 it also
declares an optional `reportPath` — the full install detail (watcher rebind
runs, compose renders, transcripts) is filed under `temp/tool-reports/` while
the inline payload keeps counts and a compact rebind digest.
This module declares no memory-mode field. Runtime install may retain flexible producer-owned detail, but that is not a typed readable-mode contract here.

### Retired resolver-response model

The earlier `ResolveContextResponse`/resolver-output account survives only as
historical provenance; it is not a callable recovery path or current model.

## Invariants And Boundaries

- Runtime install response shape is modeled, but installer-specific summary
  details remain flexible for now.
- Installation detail is not the mounted orientation answer. Root authority
  still comes from MCP settings and resolved task scope.

## Evidence

### Repo-Internal References


- Runtime install application entry point produces the installer response payload. [1]


- The retired coordination tool's former computation, kept for its one remaining script caller and not registered as an MCP tool. [2]


## 260928-MIK-L96 The host part of the install response

`RuntimeInstallResponse` gains the `host` part of the result: the provision report's fields plus the product Node payload, the configured/settings-path facts and the restart-required message; the existing fields and parameters are unchanged.

- The install response shape carrying the host part. [3]

- The live installation response is flexible and retains reportPath and host data. [4]
