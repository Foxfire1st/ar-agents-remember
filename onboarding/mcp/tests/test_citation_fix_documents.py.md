# mcp/tests/test_citation_fix_documents.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Guards multi-document citation fix parity, selection limits and CLI/registration wiring.

## Code Commentary

Cases compare final bytes between a finite document list and one call per card on converted memory through `citation_fix_tool` with fixture scope resolution, and on unconverted memory through the lower-level fixer with `expected_snapshot`; ordinary public legacy-memory writes are not admitted by those lower-level assertions. The old public missing-snapshot case is removed because public legacy-format refusal precedes snapshot checks, while converted document lists need no snapshot; the lower-level legacy dry-run case leaves Markdown bytes unchanged, and its selection-isolation case leaves the unselected card untouched. Shape refusals happen before tree reads; maximum size derives from MAX_CURATOR_SOURCE_CANDIDATES. The lower-level legacy mixed-selection case checks a rewritten sibling despite a missing member; the converted missing-card case checks the returned refusal/count, not successful sibling bytes. Repeated CLI --document preserves the same selection. These are executable assertion contracts, not a new claim that this Curator ran them.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.


### Current Source-Inspection References

- List-shape and bound assertions precede source reads. [1]
- Lower-level legacy list/single parity, dry-run Markdown-byte preservation and selection isolation are asserted; this is not public legacy admission. [2]
- Converted list/single byte parity and a single missing-card refusal/count are asserted; successful sibling bytes are not checked by the mixed-selection case. [3]
- Repeated CLI selection and whole-result output from a mocked tool payload are checked. [4]
