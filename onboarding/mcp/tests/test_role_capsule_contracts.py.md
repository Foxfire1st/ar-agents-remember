# mcp/tests/test_role_capsule_contracts.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Tests source-addressed handoff contract metadata in capsule compilation.

## Code Commentary

Contract markers are removed from rendered instructions while retaining their original path and line in metadata and contributing to semantic identity. Invalid markers are rejected even outside the selected audience; selected metadata includes only the applicable audience. A shipped-source enumeration requires one matching sender and receiver with equal fields for each declared handoff triple. The module states compiler assertions rather than a delivery or acceptance result.

## Evidence

- Marker removal preserves source-addressed metadata and validates malformed or off-audience declarations. [1]
- The shipped contract enumeration requires exactly matching sender/receiver sides and field lists. [2]
