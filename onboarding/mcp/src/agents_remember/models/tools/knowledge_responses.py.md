# mcp/src/agents_remember/models/tools/knowledge_responses.py

## Governing Overview

[models route overview](../overview.md)

## Current source contract evidence

- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [54]

## Purpose

Strict ToolResponse contracts for the four mounted knowledge operations: knowledge_read, knowledge_diff, knowledge_integrity_check and knowledge_write. These shapes declare the wire envelope; they neither author knowledge nor reinterpret a view's payload.
## Code Commentary

### Logic

KnowledgeReadResponse retains view/page/snapshot/completeness and opaque continuation, but its delivered rows are text ID, kind, computed state and memory-file/heading or line locations. `memoryCommit` and `memoryDirty` bind location provenance; worktree reads join relative files to the absolute memoryTree.memoryRoot, while no-worktree reads use absolute files with commit. The application still computes rich family-complete selection, proofs and currentness internally; projected names and compact derived status cross the mounted boundary for the ordinary naming projections, not record bodies or proof facets; the requirement-authorized marks rows carry the weakness's own statement and optional measurement, and no record body. `report` is an admitted optional field, not evidence that a retired queue/worklist view is callable. Since MIK-R118 and MIK-R124 the `weakness` and `dependent` views answer through three more optional fields: `rows` (that kind's rows), `counts` (their counts) and `readOn` (how to read the rest when rows remain). They carry rows of the named kind, not a second payload contract.

KnowledgeWriteResponse declares `reportPath` and `reportError` as a pair: where the whole write report was written, and why it was not when it could not be (MIK-R108 rule 3). A run whose report could not be written keeps its own outcome and says that nothing about the report is claimed.

KnowledgeDiffResponse holds before/after revisions and both compared trees, counts by kind, at most the list-bound `decisionRecords` and their total `decisionRecordCount`, plus a caller-readable whole-comparison report. Its strict declared fields contain no `threshold`, `complete`, `diff` or `leftOut`: neither patches nor a patch-overflow/omission body form is this response. The report retains the rich comparison for file/dashboard readers; no semantic effect label is inferred. This schema account does not itself claim an executed bound measurement.

KnowledgeIntegrityCheckResponse carries the text-tree validator report against named memory bases and the paired code checkout: whole-report counts, per-rule counts and a bounded violations listing. Refusing violations are listed before report-only findings; violationsTruncated states an omitted listing without dropping whole-report totals. Validator ok describes these inputs, never a code or intent verdict. Optional worklistState and worklist report the leaf's persisted worklist when a leaf was named.

### Invariants And Boundaries

- Each model is a strict ToolResponse with its own closed operation/state vocabulary and typed refusal fields; modeled refusals remain distinct from transport failure.
- The mounted read is a mechanical naming projection of the existing view selection, not a second semantic classification; record bodies stay in the files; only the requested marks rows carry a weakness's statement and measurement, which is what MIK-R118 names.
- Wire schema validation enforces declared fields; these models define no additional cross-field outcome validator.
- knowledge_diff names text-tree changes beside its whole comparison report, not carried patches/omissions or semantic effect judgments.
- knowledge_integrity_check reports validator findings and applies no repair or publication.
- Optional values are omitted by the inherited exclude_none rendering; unmeasured facts are not turned into measured zeroes.

### Historical boundary — MIK-R26

KnowledgeChangeResponse and KnowledgeProjectResponse, their registered tools and canonical-database write/projection handlers were retired. Old dataset diff/integrity response fields, supplied effect labels, detection-run selector fields and compatible are not current response fields. Earlier additive database-read field accounts describe the pre-retirement surface; current knowledge selections are memory trees.
## 260928-MIK-L05 The Optional `routeChain` Field And The Route-Chain Rows (MIK-R05)

> Historical additive response account only: these earlier payload/proof/currentness/continuation descriptions do not authorize record text on the current mounted answer. The rich selection survives internally and paging remains, but rows and reference blocks are projected to names; database reads and `read_ar_files` publication continuations are not current capabilities.

- **`routeChain`** (`dict[str, Any] | None = None`) is on a `registration_absent` refusal of a path read from a
  converted tree: the mechanical chain (`directory`, `links`, `derivation`, `state`, `families`) stating
  `no_governing_family`. A page carries the same block inside `payload`, not in this field.
- **The docstring paragraph "Route-chain families (MIK-R05)"** says that after the MIK-R01 content
  `payload.rows` hold one compact `chain_family` row per family with a route on the path's directory or an
  ancestor, that `payload.routeChain` states the chain, and that a `source_context` read naming
  `familyRevisionId` and no path returns that family's full content (the family seed, ruling Q1 of
  2026-09-30 03:32:18).
- **Additive and optional.** A database read never sets `routeChain`, so the installed runtime's responses are
  unchanged.

## 260928-MIK-L01 The Leaf Read's Page And The Optional `families` Field (MIK-R01)

> Historical additive response account only: these earlier payload/proof/currentness/continuation descriptions do not authorize record text on the current mounted answer. The rich selection survives internally and paging remains, but rows and reference blocks are projected to names; database reads and `read_ar_files` publication continuations are not current capabilities.

A docstring paragraph names the family-complete leaf read, and the model gains one optional field.

- **The leaf read is `state: "page"`.** On a converted tree, a `source_context` read of a path answers
  `state: "page"` whose `payload.rows` hold the path's invariants, each containing family's header and
  remaining members, their entries (each with its state) and the advertised families, in one declared order
  (rules 1 to 5). No new top-level field carries the rows: the leaf page is the `payload`, as a scope page
  already was.
- **`families`** is on an `invariant` view of a converted tree: the live families containing its invariant,
  by ID and title (rule 7).
- **Additive and optional.** A database read carries neither the leaf page nor `families`, so the installed
  runtime's responses are unchanged.

## 260928-MIK-L28 The Optional `proofs` Field On A Read (MIK-R28 Rule 4)

> Historical additive response account only: these earlier payload/proof/currentness/continuation descriptions do not authorize record text on the current mounted answer. The rich selection survives internally and paging remains, but rows and reference blocks are projected to names; database reads and `read_ar_files` publication continuations are not current capabilities.

`KnowledgeReadResponse` gained `proofs: list[dict[str, Any]] | None = None`. An `invariant` or `family`
read from a converted memory tree carries the `proves` entries of the invariant, or of every family member,
each `{id, invariant, path, anchor, facet, sidecar}`. The field is absent for a database read and for the
other three views; an unknown subject also has no field, which is distinct from `[]` ("no proof").

- **Additive and optional (architect ruling, 2026-09-29).** No existing field changed, and a database read
  never carries `proofs`, so the installed runtime's responses are unchanged.
- The module docstring states the boundary: a proof says what its test demonstrates, never that the test
  passed or that the invariant holds.
## 260928-MIK-L03 The Optional `currentness` Field On A Read (MIK-R03)

> Historical additive response account only: these earlier payload/proof/currentness/continuation descriptions do not authorize record text on the current mounted answer. The rich selection survives internally and paging remains, but rows and reference blocks are projected to names; database reads and `read_ar_files` publication continuations are not current capabilities.

`KnowledgeReadResponse` gained `currentness: dict[str, Any] | None = None`, and the module docstring a
paragraph that is the field's description. A read from a converted memory tree carries the state of every
invariant the answer carries at the code tree named by `codeTreeId`: `codeTree`, `counts` by state,
`invariants[]` with each entry that is not current, `families[]` with their stale members, and
`unverifiableReason` when the whole read cannot be observed.

- **Additive and optional.** A database read never carries it, so the installed runtime's responses are
  unchanged.
- **The docstring states the rulings:** with no `codeTreeId` every realized invariant is `unverifiable` and
  `HEAD` is never substituted (18:42:37 ruling 2); the counts cover every invariant the answer carries,
  named (for example as a relationship) or returned in full, plus every family member (19:13:41 review N5);
  a failure of the step is `unverifiableReason` and never refuses the read (N2); the payload is unchanged,
  so a stale invariant stays visible.

## 260928-MIK-L02 The Read Response States Its Page And Threshold (MIK-R02)

> Historical additive response account only: these earlier payload/proof/currentness/continuation descriptions do not authorize record text on the current mounted answer. The rich selection survives internally and paging remains, but rows and reference blocks are projected to names; database reads and `read_ar_files` publication continuations are not current capabilities.

`KnowledgeReadResponse.state` gains `"page"`, and the model gains two optional fields, `page` and
`threshold`, beside a docstring paragraph that describes them.

- **`page`** is on every read of a converted memory tree: the shared token threshold, the memory tree, the
  selection policy and manifest, the code tree the walk resolves at, and the walk's `total`, `returned`
  (through this page) and `remaining` rows, `enumerationComplete`, the `headerReference` a page that
  continues a family starts with (interim until MIK-R01 made it a row, ruling Q3 of 19:56:40: since
  260928-MIK-L01 a leaf page carries it as its literal first row and drops it from `page`, and a view page
  still names it here), and
  `flags: ["oversized_row"]` when one row alone exceeds the threshold.
- **`state: "page"`** answers a continuation minted by the published-intent block of `read_ar_files`: the
  scope page is the `payload`.
- **`threshold`** is on a refusal of a converted-tree read, because every response states the threshold,
  refusals included (ruling F8, 20:40:40).
- **Additive and optional.** A database read carries neither field, and its refusals carry no `threshold`,
  so the installed runtime's responses are unchanged.

## 260928-MIK-L08 The Integrity Response Carries A Leaf's Worklist (MIK-R08 Rule 7)

`KnowledgeIntegrityCheckResponse` changed in two ways, both additive:

- `worklistState` (`present`, `absent` or `unreadable`) and `worklist` (a summary dict) are present only
  when the caller named a `contractPath`; the response is dumped with `exclude_none`, so a dataset-only
  call's wire shape is unchanged.

## Evidence

References to verbatim view payload, complete/leftOut diffs and pre-retirement database fields below are historical/internal witnesses only, not the current mounted shape. Present wire evidence is KnowledgeReadResponse provenance/naming fields, KnowledgeDiffResponse report fields and the naming projection. All test citations are fixture assertions, not execution in this review.

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The envelope every one of the four derives from — a strict response plus the single required `operation` string each model then pins to a literal — and the shared header it inherits rather than redeclares. [35]

- Where the four classes are imported and mapped to their tool names in the registry. [36]

- The four advertised knowledge tool names in the public roster. The module's own `__all__` re-exports three of them, and `KnowledgeWriteResponse` is defined and registered without being listed there. [37]


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


The four models are two declarations in one: the operation column and the base envelope. The module's `__all__`
re-exports three of them; `KnowledgeWriteResponse` is defined here and registered in the tool registry without
being listed in that export list. The envelope
(`ToolResponse` → `ResponseModel` → `StrictResponseModel`) is defined in `models/base.py`, the
classes are registered against their tool names in `models/tools/tool_registry.py`, the registry's public
projection is pinned to `PUBLIC_TOOLS` in `mcp/public_surface.py`, and the handler payload builders
whose dicts these models validate live in `mcp/tools/knowledge.py`. Every row below is a measured range
in the working candidate.


- The module's `__all__` re-exports three of the four mounted knowledge response models; `KnowledgeWriteResponse` is defined here and registered without being listed there. [16]


- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [17]


- The strict Git-tree diff response names revisions, trees, counts, bounded decision records and their total beside a report, without carried patch/completeness/omission fields. [19]


- The integrity response carries the text-tree validator report. [20]

- The registry entry point itself, whose docstring states that a package-owned response shape uses a strict model so the field set is a drift-proof contract. [53]

- The projection of the registry that the public surface pin compares against the advertised roster. [25]
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
- The docstring paragraph on the route-chain rows, `routeChain` and the family seed. [38]
- The docstring paragraph on the leaf read and family names. [39]
- The docstring paragraph on proofs beside the view. [40]
- The docstring paragraph on currentness beside the view. [41]
- The docstring paragraph on a memory tree's bounded page. [42]
- The module docstring's statement that a memory tree is named, never hidden, and that a partial index is never presented as complete. [43]
- The optional `proofs` field on the read response, beside L03's `currentness`, since MIK-R02 the `page` and `threshold` fields, since MIK-R01 the optional `families`, and since MIK-R05 the optional `routeChain`. [44]
- The optional `currentness` field on the read response, after `proofs`, re-read at MIK-R02 when the model gained `page` and `threshold`, at MIK-R01 when it gained `families`, and at MIK-R05 when it gained `routeChain`. [45]
- The `page` state (which since MIK-R01 also answers a leaf read, and since MIK-R05 a family seed) and the optional `page` and `threshold` fields on the read model. [46]
- The read response: which view and which snapshot it was read at, echoed beside the payload verbatim, plus the optional memory-tree binding and index completeness when the read went through a converted tree's index. [47]
- The read handler that stores the view payload's own JSON and echoes the snapshot, the completeness statement (forced to `false` by a partial index) and the continuation token, beside `memoryTree` and `indexComplete`. [48]
- The optional `routeChain` field on the read model, for a path's refusal. [49]
- The optional `families` field on the read model. [50]
- A family whose members have no proof shows `[]`. [51]
- The builder that fills them. [52]
