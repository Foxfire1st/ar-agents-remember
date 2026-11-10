# mcp/src/agents_remember/models/build_currentness.py

## Governing Overview

[overview](overview.md)

## Purpose

Declares `BuildCurrentnessPayload`, the one wire shape for how a process's loaded Python build compares with the files currently at its package root, shared by serving status and the public response envelope.

## Code Commentary

The model forbids extra fields. `mode` is `installed` or `checkout`; `state` is `current`, `stale` or `unknown`. The loaded and installed digests, the first time a mismatch was seen, the reason and the remedy are optional, so an unknown reading can name why it could not compare.

The module only declares the shape. `serving/build_currentness.py` computes the reading (it reports `unknown` when the package root or a digest is missing, and `stale` with a restart remedy when the digests differ). Its consumers are the optional `buildCurrentness` field on both response envelopes in `base.py`, `core.py::RunningServerPayload.currentness`, the dashboard serving state and daemon identity, and the MCP server's stale-build dispatch refusal in `mcp/build_staleness.py`. A reading performs no restart and grants or refuses nothing by itself.

## Evidence

- The strict currentness shape with its closed mode and state vocabularies and optional digests, first-seen time, reason and remedy. [1]

- Both response envelopes carry the reading as an optional field. Anchor: `buildCurrentness` [2]

- Each running-server row carries its observed reading. [3]
- The serving comparison produces unknown, current or stale readings. [4]
