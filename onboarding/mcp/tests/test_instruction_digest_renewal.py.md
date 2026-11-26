# mcp/tests/test_instruction_digest_renewal.py

## Governing Overview

[Overview](overview.md)

## Purpose

Checks digest renewal relocation, explicit binding selectors and preservation of authored semantic choices.

## Code Commentary

The cases distinguish unchanged passage relocation from changed, replaced, removed or duplicate passages. They require separate selectors for evidence, digest places and clauses, reject uncovered prose and malformed authored maps, and retain authored reference audiences. HEAD text is shown only when it proves the held hash, with a mismatching-HEAD control. Repository-map copies exercise LF0.3 source/evidence separation and an AU4.1 clause split without widening audience; the reader-level `_assert_digest_places` case also names the authored clause decision for uncovered prose. These definitions use synthetic fixtures or copies of checkout inputs; their presence does not report execution.

## Relationships

The tests import the repository renewal module and digest-map test-support consumers. They cover independent selector responsibilities rather than treating one unit binding as authority for every association.

## Evidence

### Repo-Internal References (renewed)

- Relocation, changed passages, independent associations and held-hash-proven HEAD text exercise no-write and explicit-binding controls. [1]

- Independent new units, evidence, places and clauses, repository-map controls and reader coverage require their own authored decisions. [2]
