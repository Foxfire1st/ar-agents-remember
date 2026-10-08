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

## 260928-MIK-L96 Contract version, product Node and help texts

The three commands now take the release and the Node from the packaged contract, and their host operations come from the moved `serving/paseo` modules. The provision help says it restarts a running host when the version or a start-only setting differs and that this ends agent sessions; the stop help says stopping closes every open agent session and that sessions can be resumed after the next start.

- The command dispatch over the shared host modules. [4]
- The argument surface the three commands keep. [5]
