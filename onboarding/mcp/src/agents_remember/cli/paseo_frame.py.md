# mcp/src/agents_remember/cli/paseo_frame.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Determines which configured native frame URL a dashboard-origin browser may use.

## Code Commentary

frame_descriptor derives dashboard origin and exact embed mapping, then obtains native frame facts for the selected server/agent. No fixed loopback default substitutes for a missing embed route; unavailable origin/runtime/native facts remain a named descriptor state. The browser builds URLs from this supplied base rather than secrets or inherited host variables.

## Evidence

- Frozen implementation of frame_descriptor supporting the stated file behavior. [1]
- Frozen implementation of frame_base_url_for supporting the stated file behavior. [2]
- Frozen implementation of host_frame_facts supporting the stated file behavior. [3]
