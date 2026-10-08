# mcp/src/agents_remember/models/tools/knowledge_responses.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Strict ToolResponse contracts for the three mounted knowledge operations: knowledge_read, knowledge_diff and knowledge_integrity_check. These shapes declare the wire envelope; they neither author knowledge nor reinterpret a view's payload.

## Code Commentary

### Logic

KnowledgeReadResponse carries a named view or bounded page, its snapshot and completeness, continuation/page/threshold data, and the view payload itself. memoryTree and indexComplete state the selected memory tree and derived-index completeness; a partial index is never presented as a complete read. Optional proofs, currentness, families and routeChain carry their existing reader-owned blocks.

Proofs state what anchored tests demonstrate, never that they passed. Currentness reports the states of returned obligations and family members at the caller's codeTreeId; no supplied code tree means realized obligations are unverifiable, and HEAD is not substituted. A currentness-step failure is reported beside the view rather than refusing it.

A source_context path read is the family-complete leaf page. Its payload rows carry the path's invariants, containing-family headers and members, advertised families and route-chain families in declared order. families names the containing families on an invariant view; routeChain states the chain on a path refusal, while a page carries it within payload. Page and continuation fields preserve bounded reading and name an oversized indivisible row rather than claiming completeness.

KnowledgeDiffResponse carries the bounded Git-tree diff of the selected knowledge files, with before/after revisions, threshold, complete flag and explicit leftOut facts. The diff groups file patches by record and source path. It carries no caller-supplied semantic effect labels, and neither infers an effect nor reads the trees through an index.

KnowledgeIntegrityCheckResponse carries the text-tree validator report against named memory bases and the paired code checkout: whole-report counts, per-rule counts and a bounded violations listing. Refusing violations are listed before report-only findings; violationsTruncated states an omitted listing without dropping whole-report totals. Validator ok describes these inputs, never a code or intent verdict. Optional worklistState and worklist report the leaf's persisted worklist when a leaf was named.

### Invariants And Boundaries

- Each model is a strict ToolResponse with its own closed operation/state vocabulary and typed refusal fields; modeled refusals remain distinct from transport failure.
- The read payload is the view's own JSON, not a second rendering or classification.
- Wire schema validation enforces declared fields; these models define no additional cross-field outcome validator.
- knowledge_diff reports text-tree changes and omissions, not semantic effect judgments.
- knowledge_integrity_check reports validator findings and applies no repair or publication.
- Optional values are omitted by the inherited exclude_none rendering; unmeasured facts are not turned into measured zeroes.

### Historical boundary — MIK-R26

KnowledgeChangeResponse and KnowledgeProjectResponse, their registered tools and canonical-database write/projection handlers were retired. Old dataset diff/integrity response fields, supplied effect labels, detection-run selector fields and compatible are not current response fields. Earlier additive database-read field accounts describe the pre-retirement surface; current knowledge selections are memory trees.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The integrity handler reports text-tree validation. [9]



- The integrity model carries validator inputs, report and optional leaf worklist fields. [8]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [14]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [13]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [11]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [10]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [6]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [5]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [4]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [3]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [2]



- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [1]


The five models are two declarations in one: the operation column and the base envelope. The envelope
(`ToolResponse` → `ResponseModel` → `StrictResponseModel`) is defined in `models/base.py`, the five
classes are registered against their tool names in `models/tools/tool_registry.py`, the registry's public
projection is pinned to `PUBLIC_TOOLS` in `mcp/public_surface.py`, and the handler payload builders
whose dicts these models validate live in `mcp/tools/knowledge.py`. Every row below is a measured range
in the working candidate.


- The module exports the three mounted knowledge response models. [16]


- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [17]


- The Git-tree diff response states exact revisions, completeness and omitted patch facts. [19]


- The integrity response carries the text-tree validator report. [20]

- The envelope every one of the five derives from — a strict response plus the single required `operation` string each model then pins to a literal — and the shared header it inherits rather than redeclares. [22]
- Where the five classes are imported and mapped to their tool names in the registry. [23]
- The registry entry point itself, whose docstring states that a package-owned response shape uses a strict model so the field set is a drift-proof contract. [24]
- The projection of the registry that the public surface pin compares against the advertised roster. [25]
- The five advertised tool names, closing the one cycle-free roster literal whose last entries are the knowledge family. [26]
- The choke point that validates a handler's plain dict against the registered model, so an undeclared key is a validation error. [27]

- The read builder returns the reader-owned payload and read extras. [28]


- The tree-diff and validator-report builders produce factual outputs, neither a semantic verdict. [30]


- The closed view refusal vocabulary the read handler's `unknown_view` code comes from, which these models carry as a plain string rather than re-declare. [33]

- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [34]


### Cross-Repo References

No cross-repository behavior is implemented in this file. These are wire contracts for one package's own
MCP tool surface: every field is a store-local identity, a declared vocabulary member, or an envelope
value this package writes, and the module imports no store, no transport, no provider and no other
repository's vocabulary.

No meaningful cross-repo references found.
