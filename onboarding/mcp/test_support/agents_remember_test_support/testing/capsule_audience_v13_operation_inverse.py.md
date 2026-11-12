# mcp/test_support/agents_remember_test_support/testing/capsule_audience_v13_operation_inverse.py

## Governing Overview

[overview](overview.md)

## Purpose

The module holds the admitted short-rule spans of the nine raw lifecycle operation sources as `(current text, earlier text)` pairs. `capsule_audience_v13_fixtures.py` is its only importer and places each operation's list in its short-rule inverse.

## Code Commentary

The module is data only. Each key is `operation/<name>`; the bootstrap operation has no admitted span. The importer requires each current text to occur exactly once in the operation source before replacing it with the earlier text, so a span edited without updating this table fails the audience test.

## Evidence

- The table maps each of the nine operations to its current/earlier span pairs. [1]
- The importer takes each operation's spans from this table. [2]
