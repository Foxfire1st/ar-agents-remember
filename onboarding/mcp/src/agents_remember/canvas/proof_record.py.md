# mcp/src/agents_remember/canvas/proof_record.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Checks the mandatory served-policy, effective-source and artifact observations of a browser record. A check table alone is not a witness: a record with missing or weakened observations keeps script execution off.

## Code Commentary

- `record_gaps` reports what a record does not observe or binds, so admission is a property of the record rather than of a green table.
- The module separates header, artifact, matrix and request gaps, which is why a narrowed proof cannot pass by dropping the rows it cannot meet.

## Evidence

- A record with missing or weakened observations keeps execution off. [1]
