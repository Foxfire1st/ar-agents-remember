# mcp/tests/test_knowledge_index_build_identity.py

## Governing Overview

[Tests](overview.md)

## Purpose

Checks loaded-build index identity, cold lookup coordination and abandoned temporary-file cleanup.

## Code Commentary

A second build rebuilds an index that an older reader left incomplete, while the same build reuses its file, including after a process restart. Package source changes distinguish build identities; document changes outside the source do not. A running process retains its captured identity when disk source changes.

Tree-only legacy files and build-qualified files cannot be reused as each other. An unknown build creates private files that support real knowledge reads, cannot be reused by another cache object, and participate in the common eviction.

The concurrency cases check eight readers sharing one build with the real lock, a capability error or a timeout, and two processes sharing one result through the file lock. They cover shared failure and retry, ordinary lock errors, changed keys during capture, and eviction that prunes dead-builder files while active or ambiguous files stay.

## Relationships

These tests exercise `KnowledgeIndexCache`, the process serving-build identity and actual indexed read APIs. Usage-marker preservation and age/size policy have separate tests in `test_knowledge_index_access_time.py`.

## Evidence

- A foreign partial index is rebuilt and a matching build is reused. [1]
- A matching build reuses its file after restart. [2]
- Loaded source identity survives disk changes and excludes documents. [3]
- Legacy and build-qualified filenames remain isolated. [4]

- Unknown builds use private files for knowledge reads, and shared eviction removes their SQLite files while leaving the existing directory lock in place. [5]
