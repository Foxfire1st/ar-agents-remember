# mcp/src/agents_remember/models/knowledge/facet.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The retained attachment-endpoint vocabulary and derived-index column mapping. AttachmentEndpointKind closes invariant_revision, family_revision, source_anchor and realization_claim. Route is deliberately absent because the index envelope has its own governing-route association.

## Code Commentary

### Logic

ENDPOINT_COLUMNS maps each endpoint kind to its facet_attachment column. This is reader vocabulary: it names the checked column group an attachment row resolves, without writing a row or classifying a facet.

### Invariants And Boundaries

- Endpoint kinds form one closed set; an unrecognized kind has no mapped endpoint column.
- The route association stays separate; a fifth route endpoint would introduce a competing route mechanism.
- No facet payload, explanation-subject union, command, request/result or writable-table set is exposed here.
- Text facet records and their relationship ownership are declared in knowledge_files/records.py, not duplicated here.

### Historical boundary — MIK-R26

Canonical database facet payloads, schema/command registries, authored facet/explanation requests and receipts were retired. The prior distinction between authored content and provenance, and diagnostic guidance and a verdict, remains relevant to text records; removed classes here no longer enforce it. A retained endpoint mapping grants no canonical write admission.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The retained closed endpoint Literal. [1]


- The four endpoint kinds and exact derived-index column mapping. [5]


- Text facet meanings are declared by their own strict record classes. [11]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
