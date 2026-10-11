# mcp/tests/test_citation_fix_documents.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Guards multi-document citation fix parity, selection limits and CLI/registration wiring.

## Code Commentary

Cases compare final bytes between a finite document list and one call per card on converted and unconverted memory; dry runs leave bytes unchanged and unrelated cards remain untouched. Shape refusals happen before tree reads; maximum size derives from MAX_CURATOR_SOURCE_CANDIDATES. A refused or missing member does not prevent other selected cards. Repeated CLI --document preserves the same selection. These are executable assertion contracts, not a new claim that this Curator ran them.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.

- List-shape and bound assertions precede source reads. [1]
- Legacy list/single parity and isolation are asserted. [2]
- Converted list/single parity and partial refusal are asserted. [3]
- Repeated CLI selection and whole-result output are checked. [4]
