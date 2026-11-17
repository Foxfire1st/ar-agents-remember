# mcp/tests/test_knowledge_index_build_identity.py

## Governing Overview

[Tests](overview.md)

## Purpose

Checks that derived indexes belong to the loaded package source that built them.

## Code Commentary

A second build rebuilds an index that an older reader left incomplete, while the same build reuses its file, including after a process restart. Package source changes distinguish build identities; document changes outside the source do not. A running process retains its captured identity when disk source changes.

Tree-only legacy files and build-qualified files cannot be reused as each other. An unknown build creates private files that support real knowledge reads, cannot be reused by another cache object, and participate in the common eviction.

## Relationships

These tests exercise `KnowledgeIndexCache`, the process serving-build identity and actual indexed read APIs. Usage-marker preservation and age/size policy have separate tests in `test_knowledge_index_access_time.py`.

## Evidence

- A foreign partial index is rebuilt and a matching build is reused. [1]
- A matching build reuses its file after restart. [2]
- Loaded source identity survives disk changes and excludes documents. [3]
- Legacy and build-qualified filenames remain isolated. [4]
- Unknown builds support private reads and common eviction. [5]
