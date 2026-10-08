# mcp/src/agents_remember/memory/knowledge/connection.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Opens a selected derived knowledge index read-only and checks or creates its one declared schema on an explicitly supplied connection.

## Code Commentary

`open_read_only_database` uses APSW read-only flags and a bounded busy timeout. `create_or_validate_schema` creates only the current declared schema when the supplied database is empty, inside an immediate transaction, then sets user_version; otherwise it inspects the existing schema. Inspection checks the declared tables, columns and triggers. Transaction errors roll back and propagate. The retired connection-contract helper and canonical-store WAL/journal selection are absent; this module does not turn an index read into an authoring connection.

## Evidence

### Repo-Internal References

- `open_read_only_database` owns the current boundary described above. [13]
- `create_or_validate_schema` owns the current boundary described above. [14]
- `inspect_schema` owns the current boundary described above. [15]
