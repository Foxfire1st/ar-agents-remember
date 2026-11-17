# mcp/test_support/agents_remember_test_support/testing/capsule_audience_v13_operation_inverse.py

## Governing Overview

[overview](overview.md)

## Purpose

The module holds the admitted short-rule spans of the nine raw lifecycle operation sources as `(current text, earlier text)` pairs. `capsule_audience_v13_fixtures.py` imports the table and places each operation's list in its short-rule inverse. The baseline card identified it as the table’s only importer; the complete current tracked-source import-name search still names that one file. This is static dependency evidence, not invocation of the retained inverse.

## Code Commentary

The module is data only. Each key is `operation/<name>`; the bootstrap operation has no admitted span. When called, the retained importer requires each recorded current span to occur exactly once before replacing it with the earlier text.

## Evidence

- The table maps each of the nine operations to its current/earlier span pairs. [1]
- The importer takes each operation's spans from this table. [2]
