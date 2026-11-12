# mcp/src/agents_remember/models/role_capsules/contracts.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

New strict source marker parser, source-location carrier and render stripper.

## Code Commentary

CapsuleContractMarker records kind, key, peer role, ordered fields, source path and source line. read_contract_markers validates every ar:needs/ar:gives marker-shaped line in the original role/operation block, including passages another role will not receive. It requires needs/from or gives/to, a known manifest role, distinct fields and an operation audience marker. Only role-applicable operation endpoints are carried. Malformed markers raise contract-marker-invalid with path/line and a source-edit remedy. strip_contract_markers removes valid marker lines before downstream instruction parsing/rendering. This parser validates endpoint shape, not that a producer actually supplied values or that paired endpoints match.

## Evidence

- New strict source marker parser, source-location carrier and render stripper. [1]
