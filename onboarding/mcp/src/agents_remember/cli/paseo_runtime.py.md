# mcp/src/agents_remember/cli/paseo_runtime.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Exposes provision/status/stop for the selected Paseo runtime settings block.

## Code Commentary

Each command requires an explicit settings file and reads only that file's `paseoRuntime` host block, without claiming coordination process authority. Missing authority refuses exit two before process operation. One JSON report carries observed changes/failure step; this adapter neither starts role agents nor changes global harness configuration.

`provision` alone also takes `--accept-harness-home-change`, which runs `provision_with_home_change`: a restart may then change the harness-home variables the running host inherited. Without the flag the provisioning refuses such a restart with `harness-home-would-change` before it stops anything. A `process_record_unverifiable` failure reports `inheritedHarnessHomes` as `unknown` with no remedy.

## Evidence

- `add_arguments` declares the three commands, each with a required `--config`, and `--accept-harness-home-change` on `provision` alone. [1]

- `run` reads the named settings file's `paseoRuntime` block, refuses with exit two before any operation when it is missing or unusable, dispatches the command and prints one JSON report. [2]

- Runs all three commands without the block and checks named refusal, exit two and no process operation. [3]

## Contract version, product Node and help texts

The three commands take the release and the Node from the packaged contract, and their host operations come from the `serving/paseo` modules. The provision help says a changed version, product Node or start-only setting restarts a running host, that open sessions close and running turns and permission prompts are lost, and that sessions remain resumable; the stop help says stopping closes every open agent session and that sessions can be resumed after the next start.

- The command dispatch over the shared host modules. [4]

- The argument surface the three commands keep: a required `--config` on each, and `--accept-harness-home-change` on `provision` only. [5]

- `run` routes `provision --accept-harness-home-change` to the accepting provisioning and marks an unverifiable process record's harness homes unknown. [6]
