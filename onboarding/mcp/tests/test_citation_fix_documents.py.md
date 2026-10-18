# mcp/tests/test_citation_fix_documents.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Guards multi-document citation fix parity, selection limits and CLI/registration wiring.

## Code Commentary

Cases compare final bytes between a finite list and one call per card on converted memory through `citation_fix_tool` with fixture scope resolution. Shape and size refusals precede source reads; the bound derives from MAX_CURATOR_SOURCE_CANDIDATES. The converted missing-card case checks refusal/count, not successful sibling bytes. Returned authoring refusals preserve malformed sidecar bytes and are excluded from the subsequent refresh, while valid selected siblings refresh. Repeated CLI `--document` preserves selection; registration exposes `documents`. These are assertion contracts, not fresh execution evidence.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.


### Current Source-Inspection References


- List-shape and bound assertions precede source reads. [1]


- Converted list/single parity and missing-card refusal/count remain; returned refusals preserve malformed bytes and are excluded from refresh. [3]


- Repeated CLI selection and whole-result output from a mocked tool payload are checked. [4]
