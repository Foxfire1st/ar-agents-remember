# mcp/src/agents_remember/memory/knowledge/durable_evidence.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Publishes bounded evidence files into the durable task report area and independently reads their bytes back.

## Code Commentary

Publication confines a plain filename to the task reports root, writes the supplied content and returns its content identity. Read-back distinguishes matched, missing, mismatched and unreadable evidence. Those states describe the actual retained file, not successful cleanup or a historical observer. The old refused-destination constant and `enclosure_reports_removed` helper were removed; evidence retention is not inferred from their historical names.

## Evidence

### Repo-Internal References

- `publish_durable_evidence` owns the current boundary described above. [13]
- `read_back_evidence` owns the current boundary described above. [14]
- `_require_one_file_name` owns the current boundary described above. [15]
