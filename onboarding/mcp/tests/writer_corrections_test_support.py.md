# mcp/tests/writer_corrections_test_support.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Supplies shared writer-correction fixture ownership, native writer calls and linked-decision/requirement input constructors.

## Code Commentary

OWNER is derived from shared fixture task/leaf constants. run constructs a WriteRequest with explicit memory/code roots, handoff path and commit flag, forwarding an optional supplied worklist to the test-only prerequisite wrapper. linked_decision adds a reconsider_on link to a conforming fixture decision and reads the stored result. missing_requirement returns an intentionally unresolved exact task/packet/revision reference.

## Invariants And Boundaries

Synthetic fixture identities are not live task authority. The helper does not grant real memory-write permission or silently turn the intentionally missing packet into a valid reference.

## Evidence Scope

No test execution, CODE/MEMORY grade, new producer capability or landing is claimed. No Domain Documentation source is configured for this slice.

## Evidence

- Supplies shared writer-correction fixture ownership, native writer calls and linked-decision/requirement input constructors. Synthetic fixture identities are not live task authority. The helper does not grant real memory-write permission or silently turn the intentionally missing packet into a valid reference. [1]
