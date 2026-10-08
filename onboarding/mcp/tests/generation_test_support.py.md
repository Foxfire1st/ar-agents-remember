# mcp/tests/generation_test_support.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

Test readers for the one schema of a derived knowledge index.

## Code Commentary

### Logic

current_generation_name returns CURRENT_GENERATION.schema_name. declared_pair opens the supplied file read-only, reads user_version, closes the connection and asserts it matches the single declaration before returning its name and version. declared_schema_name takes the name from that pair. SQLite stores the version, not this application schema name. Generation-1 dataset construction and registry dispatch are retired. [1] [3] [5] [6] [7]

### Invariants And Boundaries

- The helper creates no file and migrates no schema.
- Another version fails the precondition rather than being reinterpreted.

## Evidence

### Repo-Internal References


- Current schema name. [1]


- Read-only declared pair. [3]


- Single schema record. [5]


- Single admitted database version. [6]


- Read-only handle. [7]


### Cross-Repo References

No cross-repository contract is established by this file.
