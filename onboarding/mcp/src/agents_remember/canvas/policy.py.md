# mcp/src/agents_remember/canvas/policy.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

States the isolation policy one admitted page executes under, once, so the served bytes, the browser proof and the runtime gate cannot drift apart. It also reads the shipped proof record and decides whether scripts may be served.

## Code Commentary

- `policy_digest` hashes the facts a proof is bound to; `_enforcement_digest` hashes the enforcement modules' own source bytes, so a change to the enforcement code invalidates an old proof.
- `frame_sandbox` returns a token set that never carries `allow-same-origin`; `document_headers` and `asset_headers` carry the policy a document or an admitted asset is served with.
- `scripts_enabled` answers true only when the proof record meets every clause of the policy now served, and `scripts_gap` names the reasons it does not.
- `proof_gaps` and `_catalog_gaps` check the record's own check table and observations; a table that cannot be read covers nothing.

## Evidence

- The served policy is hashed into the value a proof record must name. [1]
- A frame document is sandboxed without `allow-same-origin`. [2]
- Generated scripts are enabled only when the shipped proof covers the policy now served. [3]
- Every clause the record does not meet is named. [4]
