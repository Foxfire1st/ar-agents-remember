# scripts/agent_evals/adapters/hermes.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Captures selected Hermes session, message and usage rows and verifies retained exports before replay.

## Code Commentary

### Invariants And Boundaries

Active rows and unique archived rows from the selected session can drive observed actions in native ID order. Active copies take precedence by native call/result identity; ordinary no-call prose is deduplicated by role and content. Every row remains raw export provenance, and unrelated sessions are not extracted.

Partially copied archived rows remain raw and unknown. Recognized compaction rows remain context. Native ID order is checked across all retained rows. Counters and chronology concern the active projection, and the terminal candidate is its last assistant stop; any parser unknown, including a partially copied archived row, prevents that terminal proof. A missing native call id can use call_id in the parsed call view, but a malformed present id is not replaced. Retained replay rebuilds these observations without reopening the original SQLite database and preserves the frozen raw rows and export digest.


Superseded card wording retained for custody (not the current source locator or capture account):

> Active rows drive actions; inactive rows remain provenance. Unrelated sessions are not extracted.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
