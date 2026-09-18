# mcp/src/agents_remember/models/tools/knowledge_responses.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/tools/knowledge_responses.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec` |
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l20` uncommitted staged source; base `9f88a6de572dc15bbed1802cf08b77c1193fb24c` |
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
declares `compatible: None = None` — `None` by design and not by omission — because `Doc13:186` says the
operation "produces no compatibility verdict or causal explanation"; a caller reads the `conditions`,
the `traversalScope` and the `limitations` and decides, and computing `true` from the absence of a
matched condition would be inferring a semantic conclusion from a detection's silence. That model also
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
`manifestGeneration`, `refusalCode`, `refusalDetail`) is `| None = None`, and a list that may
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
- **The state/payload exclusion is handler discipline, not a validator.** Unlike `ViewResult`, these five
  models have no cross-field rule, so a `view` state with no payload and a `refused` state with one
  remain constructible and are prevented only by the payload builders.

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
| The five public classes this module exports and nothing else — no constant, no helper, no base. | `__all__` | mcp/src/agents_remember/models/tools/knowledge_responses.py:26-32 |
| The read response: which view and which snapshot it was read at, echoed beside the payload verbatim. | `KnowledgeReadResponse`; `payload`; `snapshot`; `completeWithinDeclaredScope`; `continuation` | mcp/src/agents_remember/models/tools/knowledge_responses.py:35-52; mcp/src/agents_remember/models/tools/knowledge_responses.py:43-52 |
| The change response: a recorded proposal or a refusal, with the tool recording and never authoring. | `KnowledgeChangeResponse`; `recordKind`; `recordId`; `revisionId` | mcp/src/agents_remember/models/tools/knowledge_responses.py:55-65; mcp/src/agents_remember/models/tools/knowledge_responses.py:58-65 |
| The diff response: only the labels an identified source supplied, defaulting to the empty list. | `KnowledgeDiffResponse`; `semanticEffectLabels` | mcp/src/agents_remember/models/tools/knowledge_responses.py:68-82; mcp/src/agents_remember/models/tools/knowledge_responses.py:76-82 |
| The integrity response: conditions and their limits, with the typed `None` that records no verdict. | `KnowledgeIntegrityCheckResponse`; `conditions`; `limitations`; `compatible`; `unresolved` | mcp/src/agents_remember/models/tools/knowledge_responses.py:85-104; mcp/src/agents_remember/models/tools/knowledge_responses.py:94-104 |
| The project response: one managed projection's per-path outcomes as three separate lists beside its destination and renderer version. | `KnowledgeProjectResponse`; `published`; `retained`; `discrepancies`; `manifestGeneration` | mcp/src/agents_remember/models/tools/knowledge_responses.py:107-119; mcp/src/agents_remember/models/tools/knowledge_responses.py:110-119 |
| The envelope every one of the five derives from — a strict response plus the single required `operation` string each model then pins to a literal — and the shared header it inherits rather than redeclares. | `ToolResponse`; `operation`; `ResponseModel`; `to_payload`; `StrictResponseModel` | mcp/src/agents_remember/models/base.py:13-16; mcp/src/agents_remember/models/base.py:66-88; mcp/src/agents_remember/models/base.py:91-95; mcp/src/agents_remember/models/tools/knowledge_responses.py:43-43 |
| Where the five classes are imported and mapped to their tool names in the registry. | `KnowledgeChangeResponse`; `KnowledgeDiffResponse`; `KnowledgeIntegrityCheckResponse`; `KnowledgeProjectResponse`; `KnowledgeReadResponse` | mcp/src/agents_remember/models/tools/tool_registry.py:111-117; mcp/src/agents_remember/models/tools/tool_registry.py:248-252 |
| The registry entry point itself, whose docstring states that a package-owned response shape uses a strict model so the field set is a drift-proof contract. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:163-253 |
| The projection of the registry that the public surface pin compares against the advertised roster. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:255-259 |
| The five advertised tool names, closing the one cycle-free roster literal whose last entries are the knowledge family. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-97 |
| The choke point that validates a handler's plain dict against the registered model, so an undeclared key is a validation error. | `finalize_tool_response`; `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_response.py:15-26; mcp/src/agents_remember/models/tools/tool_response.py:23-23 |
| The read handler that stores the view payload's own JSON and echoes the snapshot, the completeness statement and the continuation token. | `knowledge_read_payload` | mcp/src/agents_remember/mcp/tools/knowledge.py:128-172 |
| The change handler whose two reachable branches answer `refused` with `registration_absent`, and the admitted kinds it checks against. | `knowledge_change_payload`; `ADMITTED_CHANGE_KINDS` | mcp/src/agents_remember/mcp/tools/knowledge.py:198-229; mcp/src/agents_remember/mcp/tools/knowledge.py:59-59 |
| The diff and integrity handlers: only caller-supplied labels survive, and the integrity payload carries no verdict. | `_supplied_effect_labels`; `knowledge_integrity_check_payload` | mcp/src/agents_remember/mcp/tools/knowledge.py:267-281; mcp/src/agents_remember/mcp/tools/knowledge.py:284-308 |
| The project handler that returns the per-path published/retained/discrepancy lists and the manifest generation. | `knowledge_project_payload` | mcp/src/agents_remember/mcp/tools/knowledge.py:368-407 |
| The one registered shape it is a payload of, where the state/payload exclusion is a validator rather than handler discipline. | `ViewPayload`; `ViewResult`; `_require_one_outcome` | mcp/src/agents_remember/models/knowledge/view.py:728-758; mcp/src/agents_remember/models/knowledge/view.py:903-918; mcp/src/agents_remember/models/knowledge/view.py:911-918; mcp/src/agents_remember/models/knowledge/change_set.py:279-279; mcp/src/agents_remember/models/knowledge/detection.py:1000-1000; mcp/src/agents_remember/models/knowledge/diff.py:529-529; mcp/src/agents_remember/models/knowledge/view.py:1063-1078; mcp/src/agents_remember/models/knowledge/change_set.py:280-287; mcp/src/agents_remember/models/knowledge/view.py:1079-1094 |
| The closed view refusal vocabulary the read handler's `unknown_view` code comes from, which these models carry as a plain string rather than re-declare. | `ViewRefusalCode` | mcp/src/agents_remember/models/knowledge/view.py:161-169 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. These are wire contracts for one package's own
MCP tool surface: every field is a store-local identity, a declared vocabulary member, or an envelope
value this package writes, and the module imports no store, no transport, no provider and no other
repository's vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the five strict `knowledge_*` response contracts. It records the properties the field sets enforce — one shape rather than five because the payload travels as the typed view payload's own JSON and this module adds only an envelope, a refusal as a state with no partial-success member in any of the five closed state vocabularies, `compatible` typed `None` with no payload field at all in the integrity model, no field a semantic effect label could be inferred into, and `knowledge_change`'s required `recordKind`/`repositoryId` beside optional `recordId`/`revisionId` — together with the two boundaries it deliberately leaves to its callers: `refusalCode` is a carried string rather than a re-declared closure, and the state/payload exclusion is handler discipline rather than a validator, unlike `ViewResult`. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
