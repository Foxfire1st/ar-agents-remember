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
## 260928-MIK-L05 The Optional `routeChain` Field And The Route-Chain Rows (MIK-R05)

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

`KnowledgeReadResponse` gained `proofs: list[dict[str, Any]] | None = None`. An `invariant` or `family`
read from a converted memory tree carries the `proves` entries of the invariant, or of every family member,
each `{id, invariant, path, anchor, facet, sidecar}`. The field is absent for a database read and for the
other three views; an unknown subject also has no field, which is distinct from `[]` ("no proof").

- **Additive and optional (architect ruling, 2026-09-29).** No existing field changed, and a database read
  never carries `proofs`, so the installed runtime's responses are unchanged.
- The module docstring states the boundary: a proof says what its test demonstrates, never that the test
  passed or that the invariant holds.
## 260928-MIK-L03 The Optional `currentness` Field On A Read (MIK-R03)

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

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The envelope every one of the three derives from — a strict response plus the single required `operation` string each model then pins to a literal — and the shared header it inherits rather than redeclares. [35]
- Where the three classes are imported and mapped to their tool names in the registry. [36]
- The three advertised knowledge tool names in the public roster. [37]


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


The three models are two declarations in one: the operation column and the base envelope. The envelope
(`ToolResponse` → `ResponseModel` → `StrictResponseModel`) is defined in `models/base.py`, the
classes are registered against their tool names in `models/tools/tool_registry.py`, the registry's public
projection is pinned to `PUBLIC_TOOLS` in `mcp/public_surface.py`, and the handler payload builders
whose dicts these models validate live in `mcp/tools/knowledge.py`. Every row below is a measured range
in the working candidate.


- The module exports the three mounted knowledge response models. [16]


- The current read response carries its named view/page and optional reader-owned tree, proof, currentness, family and route blocks. [17]


- The Git-tree diff response states exact revisions, completeness and omitted patch facts. [19]


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
