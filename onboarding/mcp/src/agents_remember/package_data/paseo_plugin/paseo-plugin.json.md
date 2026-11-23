# mcp/src/agents_remember/package_data/paseo_plugin/paseo-plugin.json

## Governing Overview

[Route overview](../../../../overview.md)

## Purpose

The native manifest names the integration and its Paseo requirement.

## Code Commentary

The native manifest identifies the canonical client and server contributions and requires Paseo >=0.15.0. The bundled host pin is 0.16.2.


## Invariants And Boundaries

The minimum version range does not prove later versions preserve pinned unsupported web behavior.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.


- Current source owner or exact assertion described above. [1]


- The plugin manifest requires Paseo >=0.15.0. [2]
