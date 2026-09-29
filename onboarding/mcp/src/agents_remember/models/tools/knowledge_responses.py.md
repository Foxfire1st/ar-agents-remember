# mcp/src/agents_remember/models/tools/knowledge_responses.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/tools/knowledge_responses.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `719acba61e491d0b7f1ee82dbeea5314ecec5083` |
| lastVerifiedCommitDate | 2026-09-29T20:27:14+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

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
than a partial success.** `KnowledgeReadResponse` may be `view` or `refused`, `KnowledgeChangeResponse`
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

## 260928-MIK-L28 The Optional `proofs` Field On A Read (MIK-R28 Rule 4)

`KnowledgeReadResponse` gained `proofs: list[dict[str, Any]] | None = None`. An `invariant` or `family`
read from a converted memory tree carries the `proves` entries of the invariant, or of every family member,
each `{id, invariant, path, anchor, facet, sidecar}`. The field is absent for a database read and for the
other three views; an unknown subject also has no field, which is distinct from `[]` ("no proof").

- **Additive and optional (architect ruling, 2026-09-29).** No existing field changed, and a database read
  never carries `proofs`, so the installed runtime's responses are unchanged.
- The module docstring states the boundary: a proof says what its test demonstrates, never that the test
  passed or that the invariant holds.

| Finding | Anchor | Source |
| --- | --- | --- |
| The docstring paragraph on proofs beside the view. | "Proofs beside the view (MIK-R28 rule 4)." | mcp/src/agents_remember/models/tools/knowledge_responses.py:19-23 |
| The optional `proofs` field on the read response, beside L03's later `currentness`. | `KnowledgeReadResponse`; `proofs` | mcp/src/agents_remember/models/tools/knowledge_responses.py:58-79 |
| A family whose members have no proof shows `[]`. | `test_a_family_whose_members_have_no_proof_shows_an_empty_list` | mcp/tests/test_knowledge_proofs.py:322-337 |

## 260928-MIK-L08 The Integrity Response Carries A Leaf's Worklist (MIK-R08 Rule 7)

`KnowledgeIntegrityCheckResponse` changed in two ways, both additive:

- `repositoryId` is now optional (`str | None = None`), because a caller may name a leaf by its series
  contract without naming a dataset.
- `worklistState` (`present`, `absent` or `unreadable`) and `worklist` (a summary dict) are present only
  when the caller named a `contractPath`; the response is dumped with `exclude_none`, so a dataset-only
  call's wire shape is unchanged.

| Finding | Anchor | Source |
| --- | --- | --- |
| The optional repository and the two worklist fields, with their comment. | "MIK-R08 rule 7: the leaf's latest persisted worklist"; "worklistState: Literal[" | mcp/src/agents_remember/models/tools/knowledge_responses.py:148-149 |
| The builder that fills them. | `leaf_worklist_fields` | mcp/src/agents_remember/application/knowledge_worklist/surface.py:26-49 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The docstring paragraph on currentness beside the view. | "Currentness beside the view (MIK-R03)." | mcp/src/agents_remember/models/tools/knowledge_responses.py:25-33 |
| The optional `currentness` field on the read response, after `proofs`. | `KnowledgeReadResponse`; `currentness` | mcp/src/agents_remember/models/tools/knowledge_responses.py:58-79 |
| The block the field carries. | `read_currentness` | mcp/src/agents_remember/application/knowledge_currentness/surface.py:83-109 |

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The five models are two declarations in one: the operation column and the base envelope. The envelope
(`ToolResponse` → `ResponseModel` → `StrictResponseModel`) is defined in `models/base.py`, the five
classes are registered against their tool names in `models/tools/tool_registry.py`, the registry's public
projection is pinned to `PUBLIC_TOOLS` in `mcp/public_surface.py`, and the handler payload builders
whose dicts these models validate live in `mcp/tools/knowledge.py`. Every row below is a measured range
in the working candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The five public classes this module exports and nothing else — no constant, no helper, no base. | `__all__` | mcp/src/agents_remember/models/tools/knowledge_responses.py:49-55 |
| The read response: which view and which snapshot it was read at, echoed beside the payload verbatim, plus the optional memory-tree binding and index completeness when the read went through a converted tree's index. | `KnowledgeReadResponse`; `payload`; `snapshot`; `completeWithinDeclaredScope`; `continuation`; `memoryTree`; `indexComplete` | mcp/src/agents_remember/models/tools/knowledge_responses.py:58-79 |
| The change response: a recorded proposal or a refusal, with the tool recording and never authoring. | `KnowledgeChangeResponse`; `recordKind`; `recordId`; `revisionId` | mcp/src/agents_remember/models/tools/knowledge_responses.py:82-92; mcp/src/agents_remember/models/tools/knowledge_responses.py:87-87; mcp/src/agents_remember/models/tools/knowledge_responses.py:89-90 |
| The diff response: only the labels an identified source supplied, defaulting to the empty list, plus `memoryTrees` naming each side read through a converted tree's index and `indexComplete`. | `KnowledgeDiffResponse`; `semanticEffectLabels`; `memoryTrees`; `indexComplete` | mcp/src/agents_remember/models/tools/knowledge_responses.py:95-111 |
| The integrity response class as it now reads: the conditions, their limits and the typed `None` that records no verdict, the five fields that bind those conditions to the run they were measured over, and (since MIK-R08) an optional `repositoryId` beside the leaf's optional worklist state and summary. | "class KnowledgeIntegrityCheckResponse(ToolResponse):"; "worklist: dict[str, Any]" | mcp/src/agents_remember/models/tools/knowledge_responses.py:114-114; mcp/src/agents_remember/models/tools/knowledge_responses.py:150-150 |
| The project response: one managed projection's per-path outcomes as three separate lists beside its destination and renderer version, plus the optional memory-tree binding when the projected dataset was a converted tree's index. | `KnowledgeProjectResponse`; `published`; `retained`; `discrepancies`; `manifestGeneration`; `memoryTree` | mcp/src/agents_remember/models/tools/knowledge_responses.py:153-167 |
| The envelope every one of the five derives from — a strict response plus the single required `operation` string each model then pins to a literal — and the shared header it inherits rather than redeclares. | `ToolResponse`; `operation`; `ResponseModel`; `to_payload`; `StrictResponseModel` | mcp/src/agents_remember/models/base.py:13-16; mcp/src/agents_remember/models/base.py:66-88; mcp/src/agents_remember/models/base.py:91-94; mcp/src/agents_remember/models/tools/knowledge_responses.py:49-49 |
| Where the five classes are imported and mapped to their tool names in the registry. | `KnowledgeChangeResponse`; `KnowledgeDiffResponse`; `KnowledgeIntegrityCheckResponse`; `KnowledgeProjectResponse`; `KnowledgeReadResponse` | mcp/src/agents_remember/models/tools/tool_registry.py:111-117; mcp/src/agents_remember/models/tools/tool_registry.py:248-252 |
| The registry entry point itself, whose docstring states that a package-owned response shape uses a strict model so the field set is a drift-proof contract. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:163-253 |
| The projection of the registry that the public surface pin compares against the advertised roster. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:255-259 |
| The five advertised tool names, closing the one cycle-free roster literal whose last entries are the knowledge family. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-97 |
| The choke point that validates a handler's plain dict against the registered model, so an undeclared key is a validation error. | `finalize_tool_response`; `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_response.py:15-26; mcp/src/agents_remember/models/tools/tool_response.py:23-23 |
| The read handler that stores the view payload's own JSON and echoes the snapshot, the completeness statement (forced to `false` by a partial index) and the continuation token, beside `memoryTree` and `indexComplete`. | `knowledge_read_payload`; `_read_result` | mcp/src/agents_remember/mcp/tools/knowledge.py:351-362; mcp/src/agents_remember/mcp/tools/knowledge.py:365-460 |
| The change handler, which branches on nothing: **every** kind — declared or not — answers `refused` with `registration_absent` and a detail naming the reachable entry point, and the kinds the surface may be asked about are its own declared roster rather than a check the handler consults. | `knowledge_change_payload`; `DECLARED_CHANGE_KINDS` | mcp/src/agents_remember/mcp/tools/knowledge.py:114-121; mcp/src/agents_remember/mcp/tools/knowledge.py:491-508 |
| The diff and integrity handlers: only caller-supplied labels survive, and the integrity payload carries no verdict but does carry the selected run, its input identity and the digest over it. | `_supplied_effect_labels`; `knowledge_integrity_check_payload` | mcp/src/agents_remember/mcp/tools/knowledge.py:636-650; mcp/src/agents_remember/mcp/tools/knowledge.py:665-702 |
| The project handler's body (behind the thin public `knowledge_project_payload` wrapper) that returns the per-path published/retained/discrepancy lists and the manifest generation, beside `memoryTree` and `indexComplete`. | `_project_result` | mcp/src/agents_remember/mcp/tools/knowledge.py:1013-1060 |
| The one registered shape it is a payload of, where the state/payload exclusion is a validator rather than handler discipline. | `ViewPayload`; `ViewResult`; `_require_one_outcome` | mcp/src/agents_remember/models/knowledge/view.py:934-978; mcp/src/agents_remember/models/knowledge/view.py:1151-1166; mcp/src/agents_remember/models/knowledge/change_set.py:279-287; mcp/src/agents_remember/models/knowledge/detection.py:1000-1006; mcp/src/agents_remember/models/knowledge/diff.py:530-535 |
| The closed view refusal vocabulary the read handler's `unknown_view` code comes from, which these models carry as a plain string rather than re-declare. | `ViewRefusalCode` | mcp/src/agents_remember/models/knowledge/view.py:174-182 |
| The module docstring's statement that a memory tree is named, never hidden, and that a partial index is never presented as complete. | "A memory tree is named, never hidden" | mcp/src/agents_remember/models/tools/knowledge_responses.py:12-17 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. These are wire contracts for one package's own
MCP tool surface: every field is a store-local identity, a declared vocabulary member, or an envelope
value this package writes, and the module imports no store, no transport, no provider and no other
repository's vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T18:10:01+00:00: Generated citation repair: "MIK-R08 rule 7: the leaf's latest persisted worklist"; "worklistState: Literal[" repointed to mcp/src/agents_remember/models/tools/knowledge_responses.py:148-148; mcp/src/agents_remember/models/tools/knowledge_responses.py:149-149. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:10:01+00:00: Generated citation repair: `__all__` repointed to mcp/src/agents_remember/models/tools/knowledge_responses.py:49-55. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:10:01+00:00: Generated citation repair: "class KnowledgeIntegrityCheckResponse(ToolResponse):"; "worklist: dict[str, Any]" repointed to mcp/src/agents_remember/models/tools/knowledge_responses.py:114-114; mcp/src/agents_remember/models/tools/knowledge_responses.py:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 704ba74355bb1716854facdd857416a0cc403be7304c687768829065b4665abc; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): **body updated for MIK-R03.** Added the section "260928-MIK-L03 The Optional `currentness` Field On A Read": the field and its docstring paragraph, recording architect rulings 18:42:37 (2: only `codeTreeId`, no `HEAD`) and 19:13:41 (N2: never refuses; N5: the counts cover every invariant carried, named or in full). Rows below the inserted lines were re-pointed by the installed fixer. **The reopened `KnowledgeReadResponse` row (L28's `proofs` row) was re-read and reworded** to name the field beside `currentness`; the class now spans the new field, and the generated bullet this pass's fixer wrote for it was removed.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): Added the section "260928-MIK-L08 The Integrity Response Carries A Leaf's Worklist (MIK-R08 Rule 7)" (optional `repositoryId`, the `worklistState` and `worklist` fields, present only when a leaf is named). **Reopened `KnowledgeIntegrityCheckResponse` claim re-read and reworded:** the class now also declares the optional `repositoryId` and the worklist fields, so the row names them and is anchored on the class line and the `worklist` field line instead of the ten field names the committed generated-repair bullets list; its range is re-measured to the class's current extent, `103-139`.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): Added the section "260928-MIK-L28 The Optional `proofs` Field On A Read": the new optional field and its docstring paragraph, with the architect ruling that the additive field is accepted and absent for database reads. Three cited rows. The docstring paragraph moved every range below it by six lines and the field by one more; the rows were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map. No claim wording changed there. No verification stamp was advanced.
- 2026-09-29T13:18:53+00:00: Generated citation repair: `KnowledgeIntegrityCheckResponse`; `conditions`; `limitations`; `compatible`; `unresolved`; `selectedRunId`; `inputDigest`; `inputIdentities`; `matchingRunIds`; `exactInputSelector` repointed to mcp/src/agents_remember/models/tools/knowledge_responses.py:103-136; mcp/src/agents_remember/models/tools/knowledge_responses.py:124-124; mcp/src/agents_remember/models/tools/knowledge_responses.py:131-131; mcp/src/agents_remember/models/tools/knowledge_responses.py:132-132; mcp/src/agents_remember/models/tools/knowledge_responses.py:134-134; mcp/src/agents_remember/models/tools/knowledge_responses.py:126-126; mcp/src/agents_remember/models/tools/knowledge_responses.py:127-127; mcp/src/agents_remember/models/tools/knowledge_responses.py:128-128; mcp/src/agents_remember/models/tools/knowledge_responses.py:129-129; mcp/src/agents_remember/models/tools/knowledge_responses.py:130-130. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): **body update for the optional MIK-R23 response fields.** `memoryTree` and `indexComplete` on the read and project responses and `memoryTrees` plus `indexComplete` on the diff response: a new Logic paragraph, the optionality list, a new invariant, reworded read/diff/project response rows and a row for the new docstring paragraph. Re-read and reworded the reopened rows for `KnowledgeProjectResponse`, the read handler and the project handler (whose two identical rows are collapsed to one, since both named the same construct, and re-cited to the handler's body `_project_result`, where the per-path lists are built — the one-line public wrapper's range had been placed by the 2026-09-25 mechanical projection below, which is left as written); the fixer's generated bullets for those three claims, written minutes earlier in this same pass, are folded into this entry because their "claim bytes unchanged" would be false. The change-handler and diff/integrity-handler rows, which were stale before this leaf, were re-derived from the builders' extents in `mcp/tools/knowledge.py`. The verification stamp is not advanced: closeout owns it.
- 2026-09-29T05:54:39+00:00: Generated citation repair: `__all__` repointed to mcp/src/agents_remember/models/tools/knowledge_responses.py:33-39. No content impact: mechanical anchor-range projection bound to citation source snapshot 08ce78606da3cc2a7c0249e0af5ee18d9cd313bdb4222c759c5a89e3e75efdf0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:54:39+00:00: Generated citation repair: `KnowledgeIntegrityCheckResponse`; `conditions`; `limitations`; `compatible`; `unresolved`; `selectedRunId`; `inputDigest`; `inputIdentities`; `matchingRunIds`; `exactInputSelector` repointed to mcp/src/agents_remember/models/tools/knowledge_responses.py:96-129; mcp/src/agents_remember/models/tools/knowledge_responses.py:117-117; mcp/src/agents_remember/models/tools/knowledge_responses.py:124-124; mcp/src/agents_remember/models/tools/knowledge_responses.py:125-125; mcp/src/agents_remember/models/tools/knowledge_responses.py:127-127; mcp/src/agents_remember/models/tools/knowledge_responses.py:119-119; mcp/src/agents_remember/models/tools/knowledge_responses.py:120-120; mcp/src/agents_remember/models/tools/knowledge_responses.py:121-121; mcp/src/agents_remember/models/tools/knowledge_responses.py:122-122; mcp/src/agents_remember/models/tools/knowledge_responses.py:123-123. No content impact: mechanical anchor-range projection bound to citation source snapshot 08ce78606da3cc2a7c0249e0af5ee18d9cd313bdb4222c759c5a89e3e75efdf0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `knowledge_project_payload` repointed to mcp/src/agents_remember/mcp/tools/knowledge.py:849-852. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `knowledge_project_payload` repointed to mcp/src/agents_remember/mcp/tools/knowledge.py:849-852. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T00:00+02:00 — 260915-KS-L47 curator (uncommitted change set on `ar/260915-ks-l47-ar`, code base `be325216416326a66950c9e320ff8d08f41e5d66`, memory base `2f415d930d1f8122ae0226bd296add3265600749`): **body update for the `compatible` declaration this leaf's change set makes explicit, on the developer's ruling that the incoming response choke point wins.** The module docstring for `KnowledgeIntegrityCheckResponse` now reads "`compatible` is declared here and is always `None`" and states both halves: the field is declared so the response vocabulary carries the no-verdict position, and the shared choke point (`models/tools/tool_response.py::finalize_tool_response`, dumping through `ResponseModel.to_payload` with `exclude_none=True`) omits `None`-valued declared fields from the wire, so a caller sees the key **absent** rather than present-and-null. The Logic paragraph that carried the old phrasing ("`None` by design and not by omission") is corrected to the same two facts, because the old sentence left a reader free to expect `compatible` among the response's keys, which the shipped candidate does not do. This is a body change and not a metadata-only refresh: the paragraph's claim set grew by the wire-omission fact. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded — no commit contains this body and no stamp was measured on it — and only `lastUpdated`/the recorded working candidate move with this reading. No commit was made.
- 2026-09-20T17:23:31+00:00: Generated citation repair: `KnowledgeIntegrityCheckResponse`; `conditions`; `limitations`; `compatible`; `unresolved`; `selectedRunId`; `inputDigest`; `inputIdentities`; `matchingRunIds`; `exactInputSelector` repointed to mcp/src/agents_remember/models/tools/knowledge_responses.py:85-118; mcp/src/agents_remember/models/tools/knowledge_responses.py:106-106; mcp/src/agents_remember/models/tools/knowledge_responses.py:113-113; mcp/src/agents_remember/models/tools/knowledge_responses.py:114-114; mcp/src/agents_remember/models/tools/knowledge_responses.py:116-116; mcp/src/agents_remember/models/tools/knowledge_responses.py:108-108; mcp/src/agents_remember/models/tools/knowledge_responses.py:109-109; mcp/src/agents_remember/models/tools/knowledge_responses.py:110-110; mcp/src/agents_remember/models/tools/knowledge_responses.py:111-111; mcp/src/agents_remember/models/tools/knowledge_responses.py:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:23:31+00:00: Generated citation repair: `KnowledgeProjectResponse`; `published`; `retained`; `discrepancies`; `manifestGeneration` repointed to mcp/src/agents_remember/models/tools/knowledge_responses.py:121-133; mcp/src/agents_remember/models/tools/knowledge_responses.py:129-129; mcp/src/agents_remember/models/tools/knowledge_responses.py:130-130; mcp/src/agents_remember/models/tools/knowledge_responses.py:131-131; mcp/src/agents_remember/models/tools/knowledge_responses.py:128-128. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `knowledge_project_payload` repointed to mcp/src/agents_remember/mcp/tools/knowledge.py:840-843. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `knowledge_project_payload` repointed to mcp/src/agents_remember/mcp/tools/knowledge.py:840-843. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T05:41+02:00 — 260915-KS-L41 curator (uncommitted change set on `ar/260915-ks-l41-ar`, code base `756c47b3` at this leaf's cut and `f79f4db745ad00b908d6ce4871d0b4ab2320207c` after the L39 sync, memory base `da33325c` at the cut and `37d0787571bfbf92890049ee0614fa159012be39` after it): **body update for the five run-binding fields this leaf adds to the integrity response, and the citation cells the report named on this card.** `KnowledgeIntegrityCheckResponse` now declares `selectedRunId`, `inputDigest`, `inputIdentities`, `matchingRunIds` and `exactInputSelector` (`models/tools/knowledge_responses.py:105-109`) beside its conditions, so "these conditions" and "the exact inputs they were measured over" are one answer on the wire: the two scalars default to `None` and the three containers to empty, `matchingRunIds` carries every run the requested scope holds — the selected one included — and `exactInputSelector` echoes the caller's own `runId`/`inputDigest` or `None` rather than reporting a silent absence. The Logic section gained a paragraph stating that binding and why the response could not be read correctly without it, the Invariants list gained an entry, and the Conventions field-name and optionality sentences now name the five. Six stale cells were re-read against the candidate rather than shifted: the integrity row now cites the model's own extent (`89-122`, with the fields at `105-109` inside it), the project row cites `125-137` so the three per-path field cells (`manifestGeneration`, `published`, `retained`, `discrepancies`) fall inside it, and the cross-file handler cells now cite `mcp/tools/knowledge.py:262-328`, `:359-387`, `:458-473`, `:477-530` and `:775-814` — the declarations they name. No claim was re-worded to fit a stale pointer and no anchor or range was dropped. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded — the candidate is uncommitted and the governed closeout owns the real stamp — the superseded `ar/260915-ks-l32-ar` candidate row is replaced by the recorded working candidate above, and no stamp was advanced or invented. This entry also carries a disposition that was first written as its own bullet and is folded in here so the history block stays newest-first: the generated bullet that recorded the earlier mechanical projection of the read handler's range was retired, because a mechanically projected range is unverified evidence and the reading recorded above replaces it; the row now cites the handler's own extent in the merged candidate. No other history entry was changed by that disposition.
- 2026-09-20T02:05:20+00:00: Generated citation repair: `knowledge_project_payload` repointed to mcp/src/agents_remember/mcp/tools/knowledge.py:610-613. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:24+02:00 — 260915-KS-L32 curator, post-sync citation pass (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`, memory base `4ffb8d8d3ff372847784fe8f7d2a13e57d9509a5`): **cleared the two enforced `citation_anchor_absent_from_range` rows this card carried, by RANGE REPAIR on the one row that carried both.** The mechanical `citation_fix` path was unavailable workspace-wide (the managed citation namespace was at its 4-namespace ceiling with every occupant live), so every substitution was read in the code worktree before it was written and none was inferred by arithmetic. The row — "the one registered shape it is a payload of, where the state/payload exclusion is a validator rather than handler discipline" — was re-read against the merged tree and its **wording holds exactly**: `ViewResult` declares `payload: ViewPayloadUnion | None` beside `refusal: ViewRefusal | None`, and its `@model_validator(mode="after")` `_require_one_outcome` really does refuse both mixtures with "a view result carries a payload and no refusal" / "a refused result carries its refusal and no payload", which is the validator-not-discipline contrast the row draws against this card's five handler-side models. Three `models/knowledge/view.py` cells were stale by a different amount each and are repointed to the declarations they name: `ViewPayload` `901-945` → `906-952` (the base class's own extent, `class ViewPayload` at `906`), `ViewResult` `1092-1107` → `1112-1128` (its own extent, `class ViewResult` at `1112`) and `_require_one_outcome` `1102-1107` → `1122-1128` (the validator's own extent, `def _require_one_outcome` at `1122`). The three cross-file cells, which cite the same validator shape in the sibling models, were one line short each — they cited the `@model_validator` decorator rather than the method — and now read `change_set.py:280-287`, `detection.py:1001-1006` and `diff.py:530-535`, each the method's own extent. No anchor was added or removed, no citation dropped, and no other row or cell touched. Two further cells were repointed in the same pass as STALE-BY-MOVE, reported for review rather than enforced: the project-handler row named `knowledge_project_payload` and cited `mcp/tools/knowledge.py:507-546`, whose declaration now spans `557-597`; and the refusal-vocabulary row named `ViewRefusalCode` and cited `view.py:161-169`, whose declaration now spans `174-182`. Both anchors resolve exactly once in their cited file, so these were pointer drift rather than wrongness, and both rows' wording was left exactly as written. **Stamp accounting:** the card's `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained unchanged and the superseded `ar/260915-ks-l30-ar` candidate row is replaced by the single recorded working candidate naming `ar/260915-ks-l32-ar` at base `7dcec036`; no commit hash was invented and no stamp was advanced — the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T01:29+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared this card's one remaining reopened claim, answering both questions the checklist put to it.** (1) Does the construct the projected range covers support the claim's own words? Yes, verified line by line: `knowledge_read_payload` returns `"payload": payload.model_dump(mode="json")` — the view payload's own JSON, not a second shape — beside `"snapshot": payload.snapshot.logical_digest`, `"completeWithinDeclaredScope": payload.completeness.complete_within_declared_scope` and `"continuation": ... payload.continuation.token`. (2) Was the range rebound from a mention to a declaration elsewhere? No: `mcp/src/agents_remember/mcp/tools/knowledge.py:192-257` is the handler's own declaration extent (def at 192 through its return statement at 257), so the mechanically projected range is the location the claim is about and it is **retained** — no re-cite and no re-wording was needed. **Stamp accounting:** the stale `lastVerifiedCommitHash`/`lastVerifiedCommitDate` rows (and the L20-era recorded working candidate beside them) were replaced by ONE recorded working candidate naming this candidate, because no commit contains the body as it now stands and no stamp was measured on it. The "evidence changed" condition was an artifact of the older comparison base: the handler's body is byte-identical between this candidate's base `7dcec036` and the working tree, so the claim is current against the base this card now names. This entry supersedes the earlier note that these rows could only be cleared by closeout advancing the stamp.
- 2026-09-20T01:20+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 4 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `knowledge_responses.py.md:197` (`DECLARED_CHANGE_KINDS`) — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy; `knowledge_responses.py.md:199` (knowledge_project_payload) — re-read the claim against the landed module: `knowledge_project_payload` is at 558, not 368, and the range was regenerated from its real extent; `knowledge_responses.py.md:9` () — STAMP ADVANCE: the card's four knowledge.py rows and the two reopened claims were re-read against the landed commit, which is the pair measured here; `knowledge_responses.py.md:10` () — STAMP ADVANCE: date moves with the commit.
- 2026-09-20T01:01:10+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): verified, and where necessary finished by hand-reading `mcp/src/agents_remember/mcp/tools/knowledge.py` and `models/knowledge/view.py`, the 4 enforced citation rows this card carried (citation_anchor_absent_from_range ×4). All four are now true on this candidate: `knowledge_change_payload` cites `:287-315` (declared 287, refusal body to 315) and its roster anchor is the live `DECLARED_CHANGE_KINDS` at `:80-87`, the dead `ADMITTED_CHANGE_KINDS` name being gone from the tree; `_supplied_effect_labels` cites `:388-402` and `knowledge_integrity_check_payload` `:405-443`; `ViewPayload` cites the class's own extent `view.py:901-945` beside `:1092-1107` and `:1102-1107`. No further range was needed by this pass, so no range was rewritten here. The card's 4 `citation_claim_reopened` / `citation_provenance_invalid` rows are NOT cleared: their content was re-read by the earlier 00:31 entry above, but the check is gated on advancing the card's verification stamp, which this residue pass is forbidden to touch and closeout owns. Claim wording, anchors and every other range are unchanged; no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read the three reopened claims in this card against the constructs they cite, because the checklist reported their evidence changed after verification and one of them had already been repointed mechanically. (1) `knowledge_read_payload` at `mcp/tools/knowledge.py:192-257` still does what the row says — it returns the view payload's own JSON beside the snapshot digest, the completeness flag and the continuation token — so the wording was **retained** and the range kept. (2) `knowledge_change_payload` no longer branches: it refuses **every** kind with `registration_absent` and a detail naming the reachable entry point, and the constant the row named, `ADMITTED_CHANGE_KINDS`, **exists nowhere in the code tree any more** — the surface's roster is `DECLARED_CHANGE_KINDS` (`:80-87`), which the handler does not consult. The row was therefore re-worded to the unconditional refusal and the roster's real name, and its two ranges re-cited from `:198-229` / `:59-67` to `:287-315` / `:80-87`. (3) `knowledge_integrity_check_payload` (`:405-443`) still carries no verdict, so that row's wording was retained; its sibling range `_supplied_effect_labels` (`:388-402`) is unchanged. One further row was corrected rather than carried: the `ViewPayload` row cited `view.py:903-918` and two later ranges where the class name never appears, and now cites the class's own extent `:901-945`, with `ViewResult` and `_require_one_outcome` re-cited to `:1092-1107` and `:1102-1107`. Anchors were neither added nor removed and no claim was deleted. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real code and memory commits.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 2 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `_supplied_effect_labels`; `knowledge_integrity_check_payload`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:29+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `knowledge_responses.py.md:196` (knowledge_read_payload) — re-read the claim against the current source: the construct moved and the range was re-derived from its real extent.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `knowledge_project_payload` repointed to mcp/src/agents_remember/mcp/tools/knowledge.py:507-546. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `knowledge_responses.py.md:197` — re-read: 'the admitted kinds it checks against' is the same renamed constant; the handler's refusal is unconditional, so the wording is corrected to 'declared' and the range re-derived.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 2 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `knowledge_responses.py.md:198` (`_supplied_effect_labels`, `knowledge_integrity_check_payload`); `knowledge_responses.py.md:200` (`ViewPayload`, `ViewResult`, `_require_one_outcome`).
- 2026-09-18T19:56:02+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) The change-handler row cited `knowledge.py:59-59`, one name in the tool roster, for `ADMITTED_CHANGE_KINDS`; the declaration is at `67`, so the range was widened to `59-67`. (b) The diff/integrity row cited `284-308` (`_diff_request`'s body) for `knowledge_integrity_check_payload`, whose definition sits at `317`; the range was widened to `284-317` so the cited span ends at the handler the claim names. Claims, anchors and every other range are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the five strict `knowledge_*` response contracts. It records the properties the field sets enforce — one shape rather than five because the payload travels as the typed view payload's own JSON and this module adds only an envelope, a refusal as a state with no partial-success member in any of the five closed state vocabularies, `compatible` typed `None` with no payload field at all in the integrity model, no field a semantic effect label could be inferred into, and `knowledge_change`'s required `recordKind`/`repositoryId` beside optional `recordId`/`revisionId` — together with the two boundaries it deliberately leaves to its callers: `refusalCode` is a carried string rather than a re-declared closure, and the state/payload exclusion is handler discipline rather than a validator, unlike `ViewResult`. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. What was actually read is this leaf's uncommitted working tree, and closeout owns the stamp once the code commit exists.
