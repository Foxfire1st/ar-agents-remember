# mcp/src/agents_remember/package_data/paseo_plugin/paseo-plugin.json

## Governing Overview

[Route overview](../../../../overview.md)

## Purpose

The native manifest names the integration and its Paseo requirement.

## Code Commentary

ar-plugin identifies the canonical client/server contribution and requires Paseo >=0.12.0, the build's pinned host; the earlier >=0.11.1 requirement is superseded by the pin this leaf moves, and no 0.11.1 requirement is current.


**L184 — INV-0TCWT9.** The manifest is what the host reads at load, so the requested capabilities are stated here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Invariants And Boundaries

The minimum version range does not prove later versions preserve pinned unsupported web behavior.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Current source owner or exact assertion described above. [1]
- The plugin manifest requires Paseo >=0.12.0 under the current pin; the >=0.11.1 requirement belongs to the earlier pin. [2]
