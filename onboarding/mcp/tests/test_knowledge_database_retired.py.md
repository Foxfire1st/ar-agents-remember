# mcp/tests/test_knowledge_database_retired.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Tests for the database retirement guard and its static checks.

## Code Commentary

The tests drive frameless events, coverage connections, retired names in index modules, the pinned helper callers, hook restoration at teardown and the SQL spellings the static reader must catch. `_ROW_WRITERS` authorizes the derived-index builder's three row-writing modules (`memory/knowledge_index/build.py`, `memory/knowledge_index/fts.py`, and `memory/knowledge_index/projection.py`) while keeping every other production SQL row write refused. Named static allowances exclude retired citation SQLite/index modules; scratch derived-index uses in `memory/carryover.py` are admitted by exact source path, not a blanket database exemption.

The computed-import admission names `canvas/proof_record.py` because it hashes its finite `ENFORCEMENT_SOURCES` tuple. Authors and requests cannot supply that module name. The SQLite import mutation probes remain in place; this is no general database admission.

## Evidence

The sidecar also carries the existing realization entries.

- The exact computed-import admission retains the static forbidden-import mutation witnesses. [1]
