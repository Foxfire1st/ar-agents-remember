# mcp/src/agents_remember/cli/paseo_live_agents.mjs

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Read the bounded live-agent census and stable OS process-start identity through the existing bridge. Each `fetchAgents` request includes background agents. The census retains unarchived IDs and reports completeness only when the host explicitly answers `hasMore: false`. An unreached agent remains unknown. PID, birth tick and boot identity are confirmed across the same host observation.

## Code Commentary

Read the bounded live-agent census and stable OS process-start identity through the existing bridge. Each `fetchAgents` request includes background agents. The census retains unarchived IDs and reports completeness only when the host explicitly answers `hasMore: false`. An unreached agent remains unknown. PID, birth tick and boot identity are confirmed across the same host observation.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

`readRoleRegistry` pages unarchived history with background and unavailable persisted providers included. It uses the cursor and call deadline and reports incomplete history when the scan cannot finish. Its exact route requests each canonical UUID from the same daemon and distinguishes a matching result with its archive timestamp, an authoritative null and an incomplete reply. The separate ten-page `agents-live` census remains the live discovery route.

## Evidence


- Each live-agent request includes background agents. The answer retains unarchived IDs, reports explicit completeness and checks the answering process identity. [1]

- Registry history includes unarchived background and unavailable persisted roles. Exact results distinguish archive, absence and incomplete observation. [2]
