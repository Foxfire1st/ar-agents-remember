# mcp/tests/test_knowledge_index_inserts.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R74 rule 3: tests read a real index.** Static census proving no test or test-support module stages index rows by hand: every fixture builds a text memory tree and calls `build_index`. The single exception is `knowledge_conversion_test_support.py`, which builds the legacy database for the conversion's reader — the one exception rule 3 names.

## Code Commentary

The census parses every module under `mcp/tests` and `mcp/test_support` as AST and fails on any executable `INSERT INTO` / `REPLACE INTO` literal naming an index table (the eight logical tables or any `ix_*` table). The retired-writer detector's spelling vectors in `test_knowledge_database_retired.py` are not excepted: they are proved inert data — bare strings in vector tuples, never a call argument — by a zero-`execute`/`executemany`-call assertion plus assigned/subscripted taint probes that run as pure AST. `DROP TABLE` / `DELETE FROM` fault injection on tmp copies is not an insert and is not flagged; each use carries its own call-site comment.

## Evidence

- No test/support module holds an executable index-table insert [1]
- Retired detector vectors are inert data, never called [2]
- The detector module holds no execute call to feed [3]
- Assigned and subscripted vectors still count as executed [4]
- The census exception is exactly the one rule 3 names [5]
