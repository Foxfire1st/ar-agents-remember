# mcp/src/agents_remember/cli/paseo_live_agents.mjs

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Read the bounded live-agent census and stable OS process-start identity through the existing bridge. Each `fetchAgents` request includes background agents. The census retains unarchived IDs and reports completeness only when the host explicitly answers `hasMore: false`. An unreached agent remains unknown. PID, birth tick and boot identity are confirmed across the same host observation.

## Code Commentary

Read the bounded live-agent census and stable OS process-start identity through the existing bridge. Each `fetchAgents` request includes background agents. The census retains unarchived IDs and reports completeness only when the host explicitly answers `hasMore: false`. An unreached agent remains unknown. PID, birth tick and boot identity are confirmed across the same host observation.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- Each live-agent request includes background agents. The answer retains unarchived IDs, reports explicit completeness and checks the answering process identity. [1]
