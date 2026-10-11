# mcp/src/agents_remember/package_data/paseo_plugin/tsconfig.json

## Governing Overview

[Route overview](../../../../overview.md)

## Purpose

The configuration supplies strict nonemitting analysis for canonical TypeScript/TSX plugin sources.

## Code Commentary

ES2020 target, ESNext/Bundler resolution, ES2023 libraries, React/node types and React JSX apply with strict/noEmit to the package's TS/TSX files.

`allowImportingTsExtensions` permits explicit `.ts` imports used by the host-free decision tests while retaining nonemitting analysis. This option supplies no missing dependencies and proves no successful whole-plugin typecheck.

## Invariants And Boundaries

Configuration alone is not a passed check; helper and separately qualified native entry/server coverage remain distinct.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Strict nonemitting analysis permits explicit TypeScript imports and applies to the declared TS/TSX source population. [1]
