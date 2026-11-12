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

- The served policy is hashed into the value a proof record must name.
- A frame document is sandboxed without `allow-same-origin`. 
- Generated scripts are enabled only when the shipped proof covers the policy now served. 
- Every clause the record does not meet is named. 

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/policy.py:380-384 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/src/agents_remember/canvas/policy.py::frame_sandbox - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/canvas/policy.py::scripts_enabled - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/src/agents_remember/canvas/policy.py::proof_gaps - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976. Retired means the anchor no longer stands, not that the cited subject was deleted.
