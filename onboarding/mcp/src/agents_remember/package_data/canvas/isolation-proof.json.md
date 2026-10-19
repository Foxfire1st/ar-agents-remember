# mcp/src/agents_remember/package_data/canvas/isolation-proof.json

## Governing Overview

[governing route overview](../../../../overview.md)

## Purpose

The generated browser proof record: the check table, observations and artifact bindings a policy digest is admitted against. It is produced by the proof harness and read by the host's script gate.

## Code Commentary

- `policy` names the served policy digest the record attests; the enforcement and frontend digests bind the code the checks ran against.
- The check table lists each required check with its expected value, and the observations record what the browser actually answered.
- A regenerated record binds the current enforcement modules as well as the built frontend. A change to either binding requires a record for those bytes; a prior frontend-only refresh does not cover a later guard change.
- The record is a generated artifact; the host re-reads it and refuses scripts when it does not cover the policy now served.

## Evidence

- The record binds the served policy digest and the artifacts it ran against. [1]

- Every required check and its observed value are in the record. [2]
