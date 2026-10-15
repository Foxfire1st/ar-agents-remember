# mcp/tests/writer_worklist_test_support.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Prepares the one native persisted-worklist prerequisite for positive writer fixtures, preserving explicitly supplied inputs.

## Code Commentary

prepare_worklist requires PYTEST_CURRENT_TEST. Only a leaf request with no worklist and a real code directory computes explicit B/K_B/C/K_C sides, with caller bases, roots and conversion cache. A computed list is written to the fixture contract enclosure or XDG cache and read back before replacing the frozen request. write_knowledge then delegates to the native writer, forwarding an optional code snapshot.

## Invariants And Boundaries

Negative tests that supply malformed worklists are not repaired by this helper. This pytest-only preparation is neither a runtime bypass nor authority to recompute a live leaf through scratch roots.

## Evidence Scope

No test execution, CODE/MEMORY grade, new producer capability or landing is claimed. No Domain Documentation source is configured for this slice.

## Evidence

- Prepares the one native persisted-worklist prerequisite for positive writer fixtures, preserving explicitly supplied inputs. Negative tests that supply malformed worklists are not repaired by this helper. This pytest-only preparation is neither a runtime bypass nor authority to recompute a live leaf through scratch roots. [1]
