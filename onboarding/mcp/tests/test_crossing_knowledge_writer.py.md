# mcp/tests/test_crossing_knowledge_writer.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Covers commit binding for dependent-document confirmations during a master's parked memory sync.

## Code Commentary

The confirmation test seeds an existing dependent record, advances the fixture code, and sends a crossing write. It checks that the confirmation commit and writer code base both equal the sync's settled commit and that the confirmation carries that commit's tree. The refusal test checks absent sync authority, a different crossing, an incomplete code side and a moved code branch. Each refusal preserves the fixture memory bytes. Separate snapshot cases cover Git ref resolution and the constructor's full-object-ID format check.

## Relationships

Exercises the crossing route in `application/knowledge_write_route.py` and the snapshot contract in `application/knowledge_writer/code_anchors.py`.

## Evidence

- A crossing confirmation uses one settled commit for both evidence and the writer base. [1]
- Missing, different, unsettled or displaced sync authority refuses the write without changing memory. [2]
- The snapshot resolves a commit ref and refuses tree and blob operands. [3]
- The constructor checks full commit ID syntax without a Git lookup. [4]
