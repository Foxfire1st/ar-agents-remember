# mcp/src/agents_remember/models/runtime.py

## Governing Overview

[overview](overview.md)

## Current source contract evidence

- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance.

## Purpose

`runtime.py` defines the flexible `RuntimeInstallResponse` contract. It declares
no resolver-response model: mounted orientation is `context_packet`,
not a second response shape in this file.

## Code Commentary

`RuntimeInstallResponse` remains flexible because install reports include
summary and message blocks from installer services; it also
declares an optional `reportPath` — the full install detail (watcher rebind
runs, compose renders, transcripts) is filed under `temp/tool-reports/` while
the inline payload keeps counts and a compact rebind digest.
It declares a `runningServers` list of `core.RunningServerPayload` rows, empty by default, and an
optional flexible `dashboard` part reporting the action install took (or would take, on a dry run)
for a running dashboard with its detail and, when known, its pid and source digest.
This module declares no memory-mode field. Runtime install may retain flexible producer-owned detail, but that is not a typed readable-mode contract here.

## Invariants And Boundaries

- Runtime install response shape is modeled, but installer-specific summary
  details remain flexible for now.
- Installation detail is not the mounted orientation answer. Root authority
  still comes from MCP settings and resolved task scope.

## Evidence

### Repo-Internal References


- Runtime install application entry point produces the installer response payload. [1]


- The retired coordination tool's former computation, kept for its one remaining script caller and not registered as an MCP tool. [2]


## The host part of the install response

`RuntimeInstallResponse` carries the `host` part of the result: the provision report's fields plus the product Node payload, the configured/settings-path facts and the restart-required message.

- The install response shape carrying the host part. [3]

- The live installation response is flexible and retains reportPath and host data. [4]

- The install response carries the running-server inventory and the dashboard part. [5]
