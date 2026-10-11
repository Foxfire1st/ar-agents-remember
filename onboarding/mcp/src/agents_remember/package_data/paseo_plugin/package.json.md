# mcp/src/agents_remember/package_data/paseo_plugin/package.json

## Governing Overview

[Route overview](../../../../overview.md)

## Purpose

The private manifest defines canonical plugin source packaging and standalone typecheck dependencies.

## Code Commentary

The file list includes native manifest, entries and client/server/shared directories. @getpaseo/plugin is pinned to 0.11.1; the command declares nonemitting tsc. Other listed development dependencies supply the package's types.

## Invariants And Boundaries

These declarations are not installation or successful typecheck evidence. The package is canonical source, not a generated skill mirror.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The plugin's development SDK is pinned to 0.11.1. [1]
- Current source owner or exact assertion described above. [2]
