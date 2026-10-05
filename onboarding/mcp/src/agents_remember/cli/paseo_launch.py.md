# mcp/src/agents_remember/cli/paseo_launch.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Builds the exact saved native workspace/agent launch call and classifies its result.

## Code Commentary

RoleLaunch carries minted identity, canonical selection, actual folder/workspace and selected provider options. tool_server_definition uses this interpreter/source/settings and exact binding; recovery_note retains artifact path/digest within its bound. The saved call keeps first message as JSON data and native parent/tier feature inputs. A reply is accepted only for the minted agent and expected server/workspace; unconfirmed replies remain retryable rather than reminting.

## Evidence

- Frozen implementation of tool_server_definition supporting the stated file behavior. [1]
- Frozen implementation of build_launch_call supporting the stated file behavior. [2]
- Frozen implementation of run_launch_call supporting the stated file behavior. [3]
- The launch observer checks complete receipt, stable UUID and stored call before runtime launch. [4]
- Interrupts between receipt and call and checks retry retains one agent identity. [5]
- Checks interpreter, -P module invocation, source, selected settings and single canonical server definition. [6]
- Starts generated stdio server and checks serving build package root and binding from selected source. [7]
- Checks emitted binding and explicitly empty absent references and seat identities before round-trip. [8]
