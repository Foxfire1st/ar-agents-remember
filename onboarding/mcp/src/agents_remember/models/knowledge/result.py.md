# mcp/src/agents_remember/models/knowledge/result.py

## Governing Overview
[models route overview](../overview.md)

## Purpose
The retained knowledge operation/refusal vocabularies and typed KnowledgeRefusal value. A refusal carries a code, exact operation, identifying facts and next action; vocabulary membership alone does not establish a surviving production mutation entry point.

## Code Commentary
### Logic

KnowledgeOperation retains operation spellings used by reader and historical contracts. KnowledgeRefusalCode retains the failure-code vocabulary, including codes of the retired canonical database route. KnowledgeRefusal carries code, operation, detail, optional table/record_id/expected/observed and required next_action.

The retained read layer constructs values through refusal and selected_input_unavailable_refusal. An absent explicit input is an input error, not an empty dataset or permission to substitute a current tree. Unclassified storage defects remain KnowledgeStorageError rather than an invented refusal code.

### Conventions

Codes are a declared vocabulary: a storage failure with no code here is a defect, not a new code invented at the raise site. A caller branches on `code`, never on message text.

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



- The remaining constructors serve index reads. [34]




- database_frozen remains a cutover vocabulary reservation, not a writer. [44]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- Operation spellings remain after canonical request/result retirement. [40]


- The failure-code union retains historical reservations. [41]

- **The two members this leaf added, each for the reason written beside it in the source: the scope construction is neither the retrieval selection nor the composition traversal, and the pipeline's composition act is neither the construction nor a record read — and no refusal code was added with either.** [45]
- The refusal value carrying code, operation, offending record and next action. [46]
- The declared mutating-operation vocabulary, including the six L4 operations, the two L5 merge operations, the two L6 portable operations, the one L7 read operation, the one L8 comparison operation, the two L10 route operations, the seven L11 facet operations, **the two L14 detection operations, the two L18 citation-binding operations and the two L16 family-integrity operations** — fifty members, re-counted from the literal on this candidate. [47]
- The declared refusal vocabulary, with each member naming a distinct observable failure — the seven L4 codes, the twelve L5 merge codes, the one L6 portable code, the six L7 read codes (L8, L10, L11, L16 and L18 added none) **the one L14 detection code** and the cutover's `database_frozen` (260928-MIK-L37); forty-six members, re-counted from the literal. [48]
- The refusal code of a database write into a converted tree. [49]
