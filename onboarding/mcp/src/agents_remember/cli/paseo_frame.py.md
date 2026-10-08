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

## MIK-R95 Workspace Owner Import

The frame route now takes `workspace_folder` from its extracted owner `role_launch_workspace` instead of the preparation module; the route behavior is unchanged.
## 260928-MIK-L96 The unreachable detail

The frame's `unreachable` answer now distinguishes the host states: a host that is not installed names the install step, a configured host that is down names the one start, and the `unreachable` detail no longer tells a user to provision as a remedy for an unloaded client.

- The frame answer with its host-state detail. [4]
- The host facts the frame reads. [5]
