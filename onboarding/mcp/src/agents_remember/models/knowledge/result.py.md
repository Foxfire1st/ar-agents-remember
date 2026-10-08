# mcp/src/agents_remember/models/knowledge/result.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The retained knowledge operation/refusal vocabularies and typed KnowledgeRefusal value. A refusal carries a code, exact operation, identifying facts and next action; vocabulary membership alone does not establish a surviving production mutation entry point.

## Code Commentary

### Logic

KnowledgeOperation retains operation spellings used by reader and historical contracts. KnowledgeRefusalCode retains the failure-code vocabulary, including codes of the retired canonical database route. KnowledgeRefusal carries code, operation, detail, optional table/record_id/expected/observed and required next_action.

The retained read layer constructs values through refusal and selected_input_unavailable_refusal. An absent explicit input is an input error, not an empty dataset or permission to substitute a current tree. Unclassified storage defects remain KnowledgeStorageError rather than an invented refusal code.

### Invariants And Boundaries

- A consumer branches on code and offending facts, not prose or mere Literal membership.
- This value vocabulary manufactures no acceptance, executes no operation and confers no write admission.
- The no_change refusal reservation differs from historical operation result states; listing it creates no producer.
- unsupported_schema is vocabulary; the retained index opener's unsupported-version storage-error path is separate.

### Historical boundary — MIK-R26

Canonical database drafts, mutation requests/results, outcome helpers, graph/anchor endpoint requests, label-write results and candidate ChangeBatch/MutationResult/RecordIdentity/ExpectedRecord were retired. Their old factories, publication lifecycle and portable/merge producers are not current paths merely because their spellings remain in these Literals. database_frozen records the earlier MIK-R37 cutover reservation, not a current write capability.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The retained operation Literal is vocabulary, not proof of a reachable writer. [1]


- The retained closed failure-code vocabulary. [3]


- A typed refusal carries code, operation, offending facts and required next action. [12]

- The graph's request vocabulary and the anchor-endpoint union. [14]


- The remaining constructors serve index reads. [34]




- database_frozen remains a cutover vocabulary reservation, not a writer. [44]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- Operation spellings remain after canonical request/result retirement. [40]


- The failure-code union retains historical reservations. [41]
