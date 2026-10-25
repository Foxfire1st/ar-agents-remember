# mcp/src/agents_remember/package_data/paseo_plugin/package.json

## Governing Overview

[Route overview](../../../../overview.md)

## Purpose

The private manifest defines canonical plugin source packaging and standalone typecheck dependencies.

## Code Commentary

The file list includes native manifest, entries and client/server/shared directories. @getpaseo/plugin is pinned to 0.12.0; typecheck declares nonemitting tsc, while test runs the server decision tests through Node's experimental type stripping. Other listed development dependencies supply the package's types. A host-free decision test command is not a live-plugin installation or event-delivery witness.


**L184 — INV-0TCWT9.** The package's dependencies are what the build sees, so the SDK's version is fixed here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Invariants And Boundaries

These declarations are not installation or successful typecheck evidence. The package is canonical source, not a generated skill mirror.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.


- The plugin's development SDK is pinned to 0.12.0. [1]


- Current source owner or exact assertion described above. [2]
