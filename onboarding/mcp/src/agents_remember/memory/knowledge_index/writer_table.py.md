# mcp/src/agents_remember/memory/knowledge_index/writer_table.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Counts writer revision history in the selected tree and binds each count to its stored revisions.

Each writer row also carries five consolidation pass columns from `consolidation_outcomes.OUTCOME_COLUMNS`: `consolidationKept`, `consolidationCorrected`, `consolidationMerged`, `consolidationRetired`, and `consolidationUnresolved`, counted for the writer of the revision read.

## Evidence

- The table aggregates written, reviewed, changed and retired revisions by attribution. [1]

- Named records and written entries identify the revisions available as evidence. [2]
