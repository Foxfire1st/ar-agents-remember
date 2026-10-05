# mcp/src/agents_remember/cli/paseo_runtime.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Exposes provision/status/stop for the selected Paseo runtime settings block.

## Code Commentary

Each command requires an explicit settings file and loads only paseoRuntime without claiming coordination process authority. Missing authority refuses exit two before process operation. One JSON report carries observed changes/failure step; this adapter neither starts role agents nor changes global harness configuration.

## Evidence

- Frozen implementation of add_arguments supporting the stated file behavior. [1]
- Frozen implementation of run supporting the stated file behavior. [2]
- Runs all three commands without the block and checks named refusal, exit two and no process operation. [3]
