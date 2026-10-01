# mcp/src/agents_remember/models/tools/knowledge_responses.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The strict wire contracts for the five mounted `knowledge_*` operation families — `knowledge_read`,
`knowledge_change`, `knowledge_diff`, `knowledge_integrity_check` and `knowledge_project` — each one a
`ToolResponse` whose declared field set *is* the contract rather than a convention the handlers are
trusted to keep. It deliberately does **not** have a second renderer: requirement 6.8 says a mounted
tool's response payload is the same view payload requirements 2 and 3 define, "not a second shape", so
the payload travels as the typed view payload's own JSON and this module adds only the envelope around
it. It also has no refusal vocabulary of its own — every `refusalCode` field is a plain `str` carrying a
code the owning leaf closed — no field for a verdict, no field for an inferred semantic label, no
`compatible` value, and no validator that could turn a refusal into an empty result. There is no
behaviour here at all: the module imports pydantic and one envelope class, defines five models and
exports five names.

## Code Commentary

### Logic

**Five strict response models, and one of them is the payload contract the other four are not.**
`KnowledgeReadResponse` is the only model whose payload travels as an object: it echoes `view`,
`repositoryId`, `snapshot`, `completeWithinDeclaredScope` and `continuation` beside the payload itself,
so a caller can tell which of the five views it received and which snapshot it was read at without
parsing the payload's own body. `payload` is typed `dict[str, Any] | None` and the handler stores the
view payload's own `model_dump(mode="json")` there — which is precisely what "one shape, not five"
buys: a tool that re-rendered a view into its own format would create a second renderer and therefore a
second place for the classification rule to be violated, so this module declares an envelope and never
a rendering of the payload's interior.

**A memory tree is named, never hidden (MIK-R23).** When a caller's `databasePath` names a converted
memory tree, the handler reads the tree's derived knowledge index and the response gains two optional
fields: `memoryTree` on `KnowledgeReadResponse` and `KnowledgeProjectResponse` (`memoryTrees`, keyed
`before`/`after`, on `KnowledgeDiffResponse`) holding `{memoryRoot, treeId, indexState, problems[]}`, and
`indexComplete` — `false` when any side was read from a `partial` index. A read from a partial index also
reports `completeWithinDeclaredScope: false`, so a partial index is never presented as complete. Both
fields are `dict | None` / `bool | None` defaulting to `None`, and the choke point's `exclude_none` dump
leaves them absent for a database, which is why the change is additive and optional and on the response
side only: no input schema changed. The module docstring states the rule.

**Each model's `state` literal is its own closed success vocabulary, and a refusal is a state rather
than a partial success.** `KnowledgeReadResponse` may be `view`, `page` (a resumed scope walk of a
converted memory tree, since MIK-R02) or `refused`, `KnowledgeChangeResponse`
`recorded`, `no_change` or `refused`, `KnowledgeDiffResponse` `compared` or `refused`,
`KnowledgeIntegrityCheckResponse` `reported` or `refused`, and `KnowledgeProjectResponse` `projected` or
`refused`. None of them has a "partial" member, so a caller can always tell "nothing was selected" from
"the selection was refused", and the refusal fields — `refusalCode` and `refusalDetail` on every one of
the five — name the offending input instead of silently defaulting. The envelope keeps the two distinct
in the other direction as well: `ok` stays `True` on every branch, so the modeled refusal is not
expressed as a transport failure, and a handler never translates a refusal into an empty result or a
default value.

**The field sets are what make the deliberate omissions structural.** `KnowledgeIntegrityCheckResponse`
declares `compatible: None = None` — the field is **declared** and its value is **always** `None` —
because `Doc13:186` says the operation "produces no compatibility verdict or causal explanation"; a
caller reads the `conditions`, the `traversalScope` and the `limitations` and decides, and computing
`true` from the absence of a matched condition would be inferring a semantic conclusion from a
detection's silence. The declaration is not what the caller sees: the shared response choke point
(`models/tools/tool_response.py`'s `finalize_tool_response`, over `ResponseModel.to_payload`) dumps with
`exclude_none=True`, so `compatible` is **absent from the wire** rather than present-and-null. Absence
means this build reached no verdict, never that a verdict was suppressed, and the field stays declared
rather than deleted precisely so a producer that computed one would have to put the key back. That model also
declares no `payload` field at all, so there is nowhere for a rendered view to arrive. Both
`conditions` and `unresolved` are declared, so "a condition matched" and "no condition matched" are two
facts rather than one empty list. `KnowledgeDiffResponse.semanticEffectLabels` is a `list` defaulting to
empty: it carries only labels an identified agent or assessment supplied, a diff with no supplied label
returns the empty list, and requirement 6.2 quotes `Doc13:184`'s "not inferred from the diff" as the
whole contract — the model has no field a computed label could be written into.
`KnowledgeProjectResponse` describes one managed projection's per-path outcomes with `published`,
`retained` and `discrepancies` as three separate lists plus `destinationRoot`, `rendererVersion` and an
optional `manifestGeneration`, so a run that published nothing and retained a user's edit is
distinguishable from a run that wrote nothing at all.

**The integrity response binds its conditions to the run they were measured over, and the five run
fields are what make that binding readable off the wire.** `selectedRunId` (`str | None`) and
`inputDigest` (`str | None`) name the run the reported conditions actually came from; `inputIdentities`
is a list of the canonical input identity values; `matchingRunIds` is a list of every run the requested
scope holds, each carrying its own id, registered route and input digest; and `exactInputSelector` is the
caller's own selector echoed back as `{"runId": …, "inputDigest": …}` or `None` when the caller named
neither. The four list/dict fields default to empty and the two scalars default to `None`, which is the
same optionality discipline as the rest of the module: an empty `matchingRunIds` and a selected run are
different facts, and "the caller named no exact input" is reported as `exactInputSelector: None` rather
than as a silent absence. Before those five fields existed the response carried conditions alone, so a
caller could not tell a report about its own candidate from a report about another run recorded in the
same scope — the omission was not a missing convenience but a missing binding, and a scope holding two
runs over different input snapshots made the two indistinguishable.

**`KnowledgeChangeResponse` records and does not author, and its field set says so.**
`recordKind` and `repositoryId` are required while `recordId` and `revisionId` are optional, which is
the shape of "the tool records a caller-authored proposal through an admitted operation another leaf
owns": a refusal for a kind with no admitted write operation on this surface is reported as
`refused` with `registration_absent` naming the owner rather than written through a second path this
leaf would have to invent. The three-member `state` includes `no_change` beside `recorded`, so
"the proposal was already recorded" is its own answer rather than a silent success; in the shipped
candidate both reachable branches answer `refused`, because a read-only mounting of this module's own
registry is what the working candidate carries — the `recorded` and `no_change` members are the
declared vocabulary for the branches the admitted operations produce.

**The five models add only an envelope, and the envelope is inherited rather than redeclared.**
`ToolResponse` is `ResponseModel` plus one required `operation: str`, and `ResponseModel` is
`StrictResponseModel` carrying `ok`, `tokens`, `tokenizer`, `tokenCountExact`, the optional `nextStep`
hint and the agent-notifier banner fields. Each of the five models pins its own `operation` down to a
literal default — `"knowledge_read"` through `"knowledge_project"` — so the envelope's single free
string becomes five closed ones, and it declares the remaining fields itself. `to_payload()` on that
base dumps with `mode="json"` and `exclude_none=True`, which is why a refused read can leave
`snapshot`, `continuation`, `payload`, `completeWithinDeclaredScope` and the refusal fields all unset
and still produce a payload that says exactly what happened.

**Validation is the registry's job, and this module is the declaration that registry validates
against.** The five classes are imported by `models/tools/tool_registry.py` and mapped to
`"knowledge_read"` through `"knowledge_project"` in `TOOL_RESPONSE_MODELS`;
`PUBLIC_TOOL_RESPONSE_MODELS` is the projection of that mapping minus `INTERNAL_COMPAT_TOOL_NAMES`, and
`mcp/public_surface.py` requires that projection to equal `PUBLIC_TOOLS` exactly, in order. The choke
point is `models/tools/tool_response.py`'s `finalize_tool_response`, which loads
`TOOL_RESPONSE_MODELS[tool_name]`, validates the handler's plain dict against it and dumps it again —
so an undeclared key in a knowledge response is a validation error rather than a tolerated extra, and
the five handler payload builders are required to produce exactly these field sets.

**Two boundaries the shapes leave to their callers are worth naming, because they are real.**
First, `refusalCode` is a plain `str | None` and not a literal, in all five models: the codes
(`unknown_view`, `registration_absent`, and the projection/`ViewRefusalCode` closures) belong to the
leaves that own those operations, and pinning them here would either widen or duplicate a shipped
vocabulary — the same discipline `models/knowledge/projection_manifest.py` applies when it keeps its
seven-member closure out of `KnowledgeRefusalCode`. Second, nothing in these five models enforces the
state/payload exclusion by validator: `KnowledgeReadResponse` can hold `state="view"` with
`payload=None`, and `KnowledgeDiffResponse` can hold `state="refused"` with a populated payload. The
exclusion is the handlers' discipline, unlike `models/knowledge/view.py`'s `ViewResult`, whose
`_require_one_outcome` validator refuses both mixtures — so the wire contract here is the field set and
the closed state member, not a cross-field rule.

### Conventions

Every model derives from `ToolResponse`, so `extra="forbid"` arrives from `StrictResponseModel` and an
undeclared key is refused rather than carried; the same import supplies `ok`, the token counters, the
`nextStep` hint and the notifier banners that this module never re-declares. Field names follow the
response vocabulary rather than the knowledge vocabulary: `repositoryId`, `recordKind`, `recordId`,
`revisionId`, `refusalCode`, `refusalDetail`, `destinationRoot`, `rendererVersion`,
`manifestGeneration`, `semanticEffectLabels`, `traversalScope`, `completeWithinDeclaredScope` — while
the payload's own interior keeps the knowledge vocabulary, because that interior is not this module's
shape to spell. Optionality is declared rather than implied: an echoed value that may legitimately be
absent (`snapshot`, `continuation`, `completeWithinDeclaredScope`, `payload`, `recordId`, `revisionId`,
`manifestGeneration`, `memoryTree`, `memoryTrees`, `indexComplete`, `refusalCode`, `refusalDetail`) is
`| None = None`, and a list that may
legitimately be empty (`semanticEffectLabels`, `conditions`, `limitations`, `unresolved`, `published`,
`retained`, `discrepancies`) is `Field(default_factory=list)`. No bounded-length constants are used at
all: this module declares no free prose, no identity and no path, so nothing here reaches for
`PROSE_MAX_LENGTH`, `REFERENCE_MAX_LENGTH` or `LABEL_MAX_LENGTH` — the payload's own model carries those
bounds. The five state and operation vocabularies are inline `Literal` annotations on the fields they
govern rather than module-level names, because no other module needs to read them, and no
`model_validator` is defined anywhere in the file. `__all__` names the five public classes and nothing
else — the module exports no constant, no helper and no base — and the import block is two stdlib names
plus pydantic's `Field` plus one sibling `models` class, so this vocabulary module imports no
application module, no store and no `mcp` module, which is what keeps `models` read from above rather
than depending on its consumers.

### Invariants And Boundaries

- **The payload is the view payload's own JSON, never a second rendering.** `KnowledgeReadResponse.payload`
  is an untyped `dict` the handler fills with the view payload's `model_dump(mode="json")`, and this
  module declares no field that re-renders, summarises or reclassifies it.
- **A refusal is a state, never a partial success.** Each of the five models closes its own `state`
  vocabulary with a `refused` member and no "partial" member, `ok` stays `True`, and the refusal fields
  name the offending input rather than defaulting a result.
- **`compatible` is `None` by design, and the integrity model has no payload field.**
  `KnowledgeIntegrityCheckResponse.compatible` is typed `None` with a `None` default, so a compatibility
  verdict cannot be written into the contract even by a well-meaning handler.
- **A reported condition set is bound to the run it was measured over.** `KnowledgeIntegrityCheckResponse`
  declares `selectedRunId`, `inputDigest`, `inputIdentities`, `matchingRunIds` and `exactInputSelector`
  beside its conditions, so "these conditions" and "the exact inputs they were measured over" are one
  answer on the wire. The selector is echoed as the caller wrote it (or `None`), and `matchingRunIds`
  carries every run the scope holds — the selected one included — so a caller that received one match can
  see it was one of several and issue an exact request from the response it already holds.
- **No semantic label is inferred.** `semanticEffectLabels` may only carry entries the caller supplied,
  defaults to the empty list, and no field exists for a label computed from the diff.
- **`knowledge_change` records and does not author.** `recordKind` and `repositoryId` are required,
  `recordId` and `revisionId` are optional, and a kind with no admitted write operation is answered
  `refused` with `registration_absent` rather than written through a second path.
- **The five models add only an envelope.** `operation` is pinned to a literal default on each model and
  the shared header (`ok`, `tokens`, `tokenizer`, `tokenCountExact`, `nextStep`, the notifier banners) is
  inherited from `ToolResponse`/`ResponseModel` rather than redeclared.
- **Refusal codes are carried, not closed, here.** All five `refusalCode` fields are `str | None`, so the
  codes stay the property of the leaves that own those operations instead of being re-declared or widened.
- **A memory tree read is named on the wire, and a database read is unchanged.** `memoryTree`/`memoryTrees`
  and `indexComplete` appear only when a selection named a converted memory tree; `indexComplete: false`
  (and, on a read, `completeWithinDeclaredScope: false`) is how a partial index reaches a tool caller.
- **The state/payload exclusion is handler discipline, not a validator.** Unlike `ViewResult`, these five
  models have no cross-field rule, so a `view` state with no payload and a `refused` state with one
  remain constructible and are prevented only by the payload builders.

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

- The docstring paragraph on the route-chain rows, `routeChain` and the family seed. [1]
- The optional `routeChain` field on the read model, for a path's refusal. [2]

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

- The docstring paragraph on the leaf read and family names. [3]
- The optional `families` field on the read model. [4]

## 260928-MIK-L28 The Optional `proofs` Field On A Read (MIK-R28 Rule 4)

`KnowledgeReadResponse` gained `proofs: list[dict[str, Any]] | None = None`. An `invariant` or `family`
read from a converted memory tree carries the `proves` entries of the invariant, or of every family member,
each `{id, invariant, path, anchor, facet, sidecar}`. The field is absent for a database read and for the
other three views; an unknown subject also has no field, which is distinct from `[]` ("no proof").

- **Additive and optional (architect ruling, 2026-09-29).** No existing field changed, and a database read
  never carries `proofs`, so the installed runtime's responses are unchanged.
- The module docstring states the boundary: a proof says what its test demonstrates, never that the test
  passed or that the invariant holds.

- The docstring paragraph on proofs beside the view. [5]
- The optional `proofs` field on the read response, beside L03's `currentness`, since MIK-R02 the `page` and `threshold` fields, since MIK-R01 the optional `families`, and since MIK-R05 the optional `routeChain`. [6]
- A family whose members have no proof shows `[]`. [7]

## 260928-MIK-L08 The Integrity Response Carries A Leaf's Worklist (MIK-R08 Rule 7)

`KnowledgeIntegrityCheckResponse` changed in two ways, both additive:

- `repositoryId` is now optional (`str | None = None`), because a caller may name a leaf by its series
  contract without naming a dataset.
- `worklistState` (`present`, `absent` or `unreadable`) and `worklist` (a summary dict) are present only
  when the caller named a `contractPath`; the response is dumped with `exclude_none`, so a dataset-only
  call's wire shape is unchanged.

- The optional repository and the two worklist fields, with their comment. [8]
- The builder that fills them. [9]

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

- The docstring paragraph on currentness beside the view. [10]
- The optional `currentness` field on the read response, after `proofs`, re-read at MIK-R02 when the model gained `page` and `threshold`, at MIK-R01 when it gained `families`, and at MIK-R05 when it gained `routeChain`. [11]
- The block the field carries, computed once per page since MIK-R02. [12]

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

- The docstring paragraph on a memory tree's bounded page. [13]
- The `page` state (which since MIK-R01 also answers a leaf read, and since MIK-R05 a family seed) and the optional `page` and `threshold` fields on the read model. [14]
- Where the page facts are built. [15]

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The five models are two declarations in one: the operation column and the base envelope. The envelope
(`ToolResponse` → `ResponseModel` → `StrictResponseModel`) is defined in `models/base.py`, the five
classes are registered against their tool names in `models/tools/tool_registry.py`, the registry's public
projection is pinned to `PUBLIC_TOOLS` in `mcp/public_surface.py`, and the handler payload builders
whose dicts these models validate live in `mcp/tools/knowledge.py`. Every row below is a measured range
in the working candidate.

- The five public classes this module exports and nothing else — no constant, no helper, no base. [16]
- The read response: which view and which snapshot it was read at, echoed beside the payload verbatim, plus the optional memory-tree binding and index completeness when the read went through a converted tree's index. [17]
- The change response: a recorded proposal or a refusal, with the tool recording and never authoring. [18]
- The diff response: only the labels an identified source supplied, defaulting to the empty list, plus `memoryTrees` naming each side read through a converted tree's index and `indexComplete`. [19]
- The integrity response class as it now reads: the conditions, their limits and the typed `None` that records no verdict, the five fields that bind those conditions to the run they were measured over, and (since MIK-R08) an optional `repositoryId` beside the leaf's optional worklist state and summary. [20]
- The project response: one managed projection's per-path outcomes as three separate lists beside its destination and renderer version, plus the optional memory-tree binding when the projected dataset was a converted tree's index. [21]
- The envelope every one of the five derives from — a strict response plus the single required `operation` string each model then pins to a literal — and the shared header it inherits rather than redeclares. [22]
- Where the five classes are imported and mapped to their tool names in the registry. [23]
- The registry entry point itself, whose docstring states that a package-owned response shape uses a strict model so the field set is a drift-proof contract. [24]
- The projection of the registry that the public surface pin compares against the advertised roster. [25]
- The five advertised tool names, closing the one cycle-free roster literal whose last entries are the knowledge family. [26]
- The choke point that validates a handler's plain dict against the registered model, so an undeclared key is a validation error. [27]
- The read handler that stores the view payload's own JSON and echoes the snapshot, the completeness statement (forced to `false` by a partial index) and the continuation token, beside `memoryTree` and `indexComplete`. [28]
- The change handler, which branches on nothing: **every** kind — declared or not — answers `refused` with `registration_absent` and a detail naming the reachable entry point, and the kinds the surface may be asked about are its own declared roster rather than a check the handler consults. [29]
- The diff and integrity handlers: only caller-supplied labels survive, and the integrity payload carries no verdict but does carry the selected run, its input identity and the digest over it. [30]
- The project handler's body (behind the thin public `knowledge_project_payload` wrapper) that returns the per-path published/retained/discrepancy lists and the manifest generation, beside `memoryTree` and `indexComplete`. [31]
- The one registered shape it is a payload of, where the state/payload exclusion is a validator rather than handler discipline. [32]
- The closed view refusal vocabulary the read handler's `unknown_view` code comes from, which these models carry as a plain string rather than re-declare. [33]
- The module docstring's statement that a memory tree is named, never hidden, and that a partial index is never presented as complete. [34]

### Cross-Repo References

No cross-repository behavior is implemented in this file. These are wire contracts for one package's own
MCP tool surface: every field is a store-local identity, a declared vocabulary member, or an envelope
value this package writes, and the module imports no store, no transport, no provider and no other
repository's vocabulary.

No meaningful cross-repo references found.
