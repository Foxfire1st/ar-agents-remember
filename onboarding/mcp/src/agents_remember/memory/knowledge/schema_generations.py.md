# mcp/src/agents_remember/memory/knowledge/schema_generations.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Declares and fingerprints the single schema used by disposable knowledge indexes.

## Code Commentary

CURRENT_GENERATION composes the retained table declarations into the current version-9 schema. The structure manifest and pinned fingerprint prevent an accidental schema change under the same identity. `generation_for_name` admits only that current schema; `generation_of_database` refuses a different user_version or structure. The former nine-generation runtime registry, per-generation constants, ancestry selector and declared-column helper are retired. Conversion of legacy memory is owned separately, not a read-time schema fallback.

## Evidence

### Repo-Internal References

- `structure_manifest` owns the current boundary described above. [37]
- `require_pinned_schema_unchanged` owns the current boundary described above. [38]
- `generation_for_name` owns the current boundary described above. [39]
- `generation_of_database` owns the current boundary described above. [40]
