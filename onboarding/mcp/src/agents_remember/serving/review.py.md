# mcp/src/agents_remember/serving/review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T06:50:00+02:00 |
| lastVerifiedCommitHash |  `972b44cc07b307929535fe7974d6a30d53c9c4f1`|
| lastVerifiedCommitDate |  2026-09-23T07:48:19+02:00|
| governingOverview | `mcp/src/agents_remember/serving/overview.md` |

## Governing Overview

[serving route overview](overview.md)

## Purpose

The Intent Reviewer's HTTP shim: **transport only, over three ports the composition root supplies.** The
module's own docstring states the boundary: it validates a query string, builds the one typed request
the composition consumes, calls the injected port and maps the typed result onto the change-set
routes' own 400/404 status idiom. It **selects nothing, ranks nothing, computes no scope and resolves
no reference** — every one of those answers comes from the application operations behind the ports,
and the value it returns is that call's own typed result serialized once.

**Why ports rather than direct imports.** `layers.toml` ranks `serving` below `application`, so this
module may not import the read, diff and view operations the adapter composes. It takes
`KnowledgeReviewPort`, `KnowledgeReviewEntriesPort` and `ReviewSourceContentPort` the same way the
launch route takes the capsule compiler: the composition root wires all three in `cli/dashboard.py`,
and a process that omits any one of them **refuses by name instead of serving an empty surface** — and,
for the expansion route, instead of serving an empty file.

**One mapping, two adapters (ICR-R16).** The two failures the ports themselves can raise —
`AuthorityError` and `FileNotFoundError` — are not caught at each call site: both adapters reach their
port through one `_port_outcome`, which builds its bodies through one `_transport_refusal`, so the
`400`/`404` idiom and the actionable fields on its bodies cannot come to differ between the routes. Both
bodies now carry a `nextAction` (and, for the not-found case, the offending input), because a reader has
to be able to act on the failure rather than only read its message.

**Three routes, because the surface answers three different questions.** `GET /api/review/intent`
renders one comparison; `GET /api/review/intent/entries` lists the subjects that comparison *can* be
opened on; `GET /api/review/intent/source-content` opens **one listed entry's actual content** at the
two bound code trees the listing published. Each split is a second **path** rather than a second
adapter: a caller that had to guess a subject id to reach the first would be choosing the candidate,
and a payload that carried every changed file's text would be a document dump — so the browser asks
for exactly the row a reader opened. The comparison and the entry list resolve through the identical
application operation, so the entry a caller is offered and the review it then opens cannot disagree
about which datasets are being compared.

**The expansion route is the one route that accepts a `path` — and it is not a filesystem path.** It is
a repository-relative entry path, sent together with both bound code tree ids, and the application
owner reads it only if a *measured* change set lists it (the requested generation's own, or, when that
measurement is unavailable, the change set the leaf's review publishes). The two tree ids are named by
the caller rather than resolved by the server, which is what keeps an expansion bound to the generation
the reader was looking at. No route accepts a filesystem path or a root, so a browser still cannot
choose which dataset or which repository is read.

## Code Commentary

### Logic

**Three GET-only route constants, one spelling each.** `KNOWLEDGE_REVIEW_ROUTE`
(`"/api/review/intent"`), `KNOWLEDGE_REVIEW_ENTRIES_ROUTE` (`"/api/review/intent/entries"`) and
`KNOWLEDGE_REVIEW_SOURCE_CONTENT_ROUTE` (`"/api/review/intent/source-content"`) are module constants so
the browser client, the route registrars and the tests all name one spelling each. The comment on the
third records why it is a third **path**: the inventory is the whole task's change set and a payload
carrying every file's text would be a document dump, so the browser asks for exactly the row a reader
opened, naming the generation the listing published. All three are registered through
`register_review_routes`, whose docstring carries the ordering requirement — **it must be called before
the greedy static mount**, which is why `serving/app.py` calls it in the block of explicit route
registrars rather than after `mount_static`.

**`SELECTOR_KINDS` is the two-member admission vocabulary of the comparison route, and every other seed
kind is refused rather than mapped.** `("invariant", "family")` is exactly the two identity seeds R07
declares; the source comment states that every other seed kind addresses a revision, a membership or a
claim rather than a subject a curator reviews. `review_request_from_query` is the whole parse: **no
selector at all** is the task context (the review is opened from the task and lists the complete source
change inventory of the pair it resolves), one named kind with its id is a reviewed subject, and a
half-named selector or an unadmitted kind returns `None` — which the handler turns into a `400` rather
than a defaulted selector.

**The three port types are plain callable types, not protocol classes.**
`Callable[[ReviewSurfaceRequest], KnowledgeReviewResult]`,
`Callable[[str, str, str], ReviewEntryListResult]` and
`Callable[[ReviewSourceContentRequest], ReviewSourceContentResult]` are the whole contracts: one typed
request in, one typed result out. The entry port's three positional strings are the task context with
**no selector at all**, because a selector is precisely what that call exists to discover. The routes
never inspect a port, so a caller that supplies the application adapter and a test that supplies a fake
are indistinguishable to the registrar.

**`SourceContentRef` is the expansion's whole selector, and it is a `Depends()` value for the same
reason `ChangesetFileRef` is.** The task context, the entry path and the two code tree ids travel as
one frozen dataclass from the query string down to the read, because a file read is answerable only
once all of it is known and any one of them alone selects nothing. The two camel-case wire names are
declared at the signature through `Query(alias=...)`, and it carries no filesystem path and no root.

**`source_content_request_from_query` refuses a blank component rather than defaulting it.** All three
of `path`, `beforeCodeTreeId` and `afterCodeTreeId` are required together; a missing one returns `None`
and the handler answers with `_incomplete_generation`. A defaulted tree id would make the server choose
a generation, which is exactly the substitution this read exists to prevent.

**A missing port is a named refusal, not an empty surface — and each route has its own.**
`register_review_routes` takes `port: KnowledgeReviewPort | None`,
`entries_port: KnowledgeReviewEntriesPort | None = None` and
`source_content_port: ReviewSourceContentPort | None = None`. When the comparison port is `None`,
`api_review_intent` returns a `503` whose `detail` says no review adapter is wired into this process,
that the Intent Reviewer therefore cannot resolve a candidate, and that "the surface is not served
rather than served empty". The entry route answers with `_UNWIRED_ENTRIES` (`status: "unavailable"`)
because an empty entry list would say "nothing is reviewable here", a different fact from "nothing can
answer that question". The expansion route answers with `_UNWIRED_SOURCE_CONTENT`, the same reason and
next action with the one word that matters changed: **"the surface is not served rather than served as
an empty file"**, because an empty document would read as a file this repository does not hold. That is
why all three ports are optional rather than required at registration.

**`_status_for` maps one typed result onto the change-set routes' own two-shape idiom, and now serves
three result types.** The union `KnowledgeReviewResult | ReviewEntryListResult | ReviewSourceContentResult`
is accepted because all three models carry the same two fields this function reads: a `refusal` and,
inside it, a published `code`. `result.refusal is None` is the `200` case — which is how the entry
list's `state == "entries"`, the review's `state == "review"` and the expansion's `state == "content"`
all map to success without a second local table. Otherwise `review_adapter_unavailable` maps to `503`,
the **four** candidate codes `candidate_unresolved`, `candidate_not_live`, `candidate_dataset_absent`
and `subject_unresolved` map to `404`, and every remaining code maps to `400` — which is where the
expansion's own `source_content_unresolved` lands, together with `comparison_refused`. The status is
therefore derived from the refusal's own published code rather than from a local table of route
conditions.

**The two exception types are mapped once, by `_port_outcome`, and both bodies are actionable.**
`AuthorityError` becomes a `400` with `status: "bad-path"`, the error's own `str` as `detail`, and
`_AUTHORITY_NEXT_ACTION` ("name a repository the configured workspace authority admits, then reopen the
review; these routes read no other repository in its place"); `FileNotFoundError` becomes a `404` with
`status: "not-found"`, the offending `path` (also carried as `offendingInput`, the field vocabulary the
typed refusals use), and `_NOT_FOUND_NEXT_ACTION` (reopen from a task context whose recorded paths
exist). `_transport_refusal(status, detail, *, next_action, offending_input=None)` is the one body
builder both use, so neither route can acquire a field the other lacks. The comparison handler and
`_source_content_response` each call `_port_outcome` and return its `Response` unchanged when it is one;
everything else a port raises is left to propagate to the application's own error handling rather than
being silently reshaped here. The entry handler adds no catch of its own: an absent dataset half is the
application operation's own typed refusal, not an exception, so it arrives as a `404` through
`_status_for`.

**`_source_content_response` is a module-level function rather than the route body, and that is the
extraction that cleared two lint findings without a suppression.** It holds the expansion read's whole
transport — the unwired answer, the selector check, the `400`/`404` map — so the registrar stays a
composition of three one-line registrations and `register_review_routes` no longer exceeded the
cyclomatic-complexity rail; the parse function takes the selector value instead of six positional
scalars, which is what cleared the argument-count findings. Since ICR-R16 the status idiom it reaches —
and the actionable fields on its bodies — is the one implementation both adapters share through
`:func:`_port_outcome``, which is what its own docstring now states.

**`_json` serializes a typed result exactly once, through the model that declares its shape.**
`result.model_dump(mode="json", exclude_none=True)` is the whole function, and its union parameter is
what lets one serializer serve all three routes. `exclude_none=True` is what makes the client's
optional fields *absent* rather than `null`, which is the same rule the browser client mirrors: a field
the server omits is absent on the client, so an unresolved reference stays unresolved rather than
becoming a defaulted empty one — and an expansion's non-textual side carries no `text` key at all
rather than a `null` that a renderer could draw as an empty document.

**`register_review_routes` accepts `config` and deliberately discards it.** `del config` is the first
statement of the body, with the docstring explaining that the parameter is kept for symmetry with the
other route registrars and for the workspace facts a port may need, while the routes themselves resolve
nothing from it because resolution belongs to the ports' own tier. The registrar then declares all
three handlers inside its own scope — `api_review_intent_entries`, then `api_review_intent_source_content`
(one line into `_source_content_response`), then `api_review_intent` — so the closures over
`entries_port`, `source_content_port` and `port` are the only state each route carries.

**The comparison route's two query aliases are spelled once, through `Query(alias=...)`.**
`selectorKind` and `selectorId` are `Annotated[str | None, Query(alias=...)]` with `None` defaults, so
both absent is the task context, and its `400 bad-request` body names the option the caller actually
has: `expected` lists the two admitted kinds **or no selector at all**, `nextAction` says to name both
parameters or omit both, and `offendingInput` falls back to whichever of the two was supplied. The
expansion route's own `400` body (`_incomplete_generation`) has the same shape: it echoes the offending
component (`path or beforeCodeTreeId or afterCodeTreeId`), states `expected: "path, beforeCodeTreeId and
afterCodeTreeId"`, and points at the inventory as the address of the content.

### Conventions

The module imports its vocabulary rather than declaring it: `KnowledgeReviewResult`,
`ReviewEntryListResult`, `ReviewSurfaceRequest`, `InvariantIdentitySeed`, `FamilyIdentitySeed` and
`KnowledgeReadSeed` from the models layer, `ReviewSourceContentRequest`/`ReviewSourceContentResult` from
`models/knowledge/review_source_content.py`, and `McpRuntimeConfig` from the kernel. `__all__` names
exactly the **nine** public names — the three route constants, the three port types, `SourceContentRef`,
`register_review_routes`, `review_request_from_query` and `source_content_request_from_query` — leaving
`_status_for`, `_json`, `_UNWIRED_ENTRIES`, `_UNWIRED_SOURCE_CONTENT`, `_source_content_response`,
`_incomplete_generation`, and the R16 mapping's own `_transport_refusal`, `_port_outcome`,
`_AUTHORITY_NEXT_ACTION` and `_NOT_FOUND_NEXT_ACTION` reachable but unpublished. It uses `fastapi.APIRouter`-free direct
`@app.get(...)` registration like the other change-set route registrars, and its JSON bodies are plain
dicts shaped like the change-set routes' own error envelopes (`status`, `detail`, `nextAction`) rather
than a second error model.

### Invariants And Boundaries

- **Transport only.** The module computes no scope, resolves no reference and selects no candidate; it
  builds one request, calls one port and maps one result. The entry route calls its port with the task
  context alone, and the expansion route calls its port with the selector value.
- **Three routes, one resolution each.** The entry list and the comparison are served from the same
  application operation, so an offered subject and the review that opens on it cannot name different
  candidates. The expansion is a third **path**, never a field on the payload or a second adapter.
- **No filesystem path is accepted, on any route.** The comparison route's inputs are a task context
  and one recorded subject; the entry route takes the task context and nothing else; the expansion
  route takes a repository-relative entry path with both bound tree ids, and the read that receives it
  admits the path only from a measured change set. No route accepts a root, and the browser never
  chooses which dataset or which repository is read.
- **Only two selector kinds are admitted, and every other is refused by name.** `SELECTOR_KINDS` is the
  comparison route's admission vocabulary and its `400` echoes the offending input beside the admitted
  pair.
- **The expansion's generation is required whole.** A blank path or a blank tree id is a `400` naming
  what was expected rather than a server-chosen generation.
- **A process with no adapter refuses by name, on all three routes.** The `503`s state that the surface
  is not served rather than served empty — and the expansion route's says "not served rather than
  served as an empty file" — so an unreachable adapter, an empty pane and an empty document stay three
  different facts.
- **The status is the refusal's own code.** `_status_for` reads the published `code` rather than
  re-deriving a condition locally, and it reads only `refusal is None` for success so one mapping
  serves all three typed results.
- **The result is serialized once, by the model.** `exclude_none=True` keeps an omitted field absent,
  which is the rule the browser client mirrors, why a refused entry read carries no `entries` key, and
  why a non-textual side carries no `text` key.
- **One mapping, one body builder.** Both adapters reach their port through `_port_outcome` and both
  bodies are built by `_transport_refusal`, so the `400`/`404` idiom and its fields cannot drift between
  the routes; each body names the action its own failure implies rather than only the message it held.
- **Rank is the reason for the indirection.** `serving` may not import `application`, so the ports are
  the only route to the adapter; the wiring belongs to the composition root.
- **Registration order matters.** All three routes must be registered before the greedy static mount.

### Todos

None recorded. An assessment-publication route is deliberately not shipped by this increment.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the shim's own docstring, the three
route constants, the three ports and their unwired answers, the selector value, the two parse
functions, the result-to-status mapping, the registrar and its three handlers, the serializer, the
port fields the composition supplies, and the cases that drive the routes with and without an adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| The shim's own statement of what it decides (nothing), why the ports exist rather than direct imports, and the fact that no filesystem path is accepted. | `SELECTOR_KINDS` |mcp/src/agents_remember/serving/review.py:108-108|
| The published surface: three route constants, three port types, the expansion's selector value, two parsers and one registrar. | `__all__`; `SourceContentRef`; `ReviewSourceContentPort` |mcp/src/agents_remember/serving/review.py:50-70; mcp/src/agents_remember/serving/review.py:191-208; mcp/src/agents_remember/serving/review.py:102-102|
| The comparison route constant, GET-only, and the comment recording that the surface produces no record. | `KNOWLEDGE_REVIEW_ROUTE` |mcp/src/agents_remember/serving/review.py:80-80|
| **The entry route constant and the comment recording why it is a second path rather than a second adapter.** | `KNOWLEDGE_REVIEW_ENTRIES_ROUTE` |mcp/src/agents_remember/serving/review.py:86-86|
| **The expansion route constant and the comment recording why it is a third path: the inventory is the whole task's change set, and a payload carrying every file's text would be a document dump.** | `KNOWLEDGE_REVIEW_SOURCE_CONTENT_ROUTE` |mcp/src/agents_remember/serving/review.py:93-93|
| The two admitted selector kinds, and the three port types as one-request-in-one-result-out callables. | `SELECTOR_KINDS`; `KnowledgeReviewPort`; `KnowledgeReviewEntriesPort` |mcp/src/agents_remember/serving/review.py:109-109; mcp/src/agents_remember/serving/review.py:106-106; mcp/src/agents_remember/serving/review.py:108-108|
| **The entry route's unwired answer: an empty entry list would say "nothing is reviewable here", a different fact from "this process cannot answer".** | `_UNWIRED_ENTRIES` |mcp/src/agents_remember/serving/review.py:107-116|
| **The expansion route's own unwired answer, which refuses rather than serving an empty file.** | `_UNWIRED_SOURCE_CONTENT` |mcp/src/agents_remember/serving/review.py:121-130|
| **The expansion's whole selector as one value: the task context, the entry path and the two camel-case tree ids, travelling together because any one alone selects nothing.** | `SourceContentRef` |mcp/src/agents_remember/serving/review.py:191-208|
| **The parse that admits two shapes and refuses a half-named selector or an unadmitted kind with `None` rather than a default.** | `review_request_from_query`; `InvariantIdentitySeed`; `FamilyIdentitySeed` |mcp/src/agents_remember/serving/review.py:36-36; mcp/src/agents_remember/serving/review.py:294-327; mcp/src/agents_remember/models/knowledge/read.py:189-193|
| **The expansion's own parse: the path and both tree ids required together, and a blank component refused rather than defaulted, because a defaulted tree id would make the server choose a generation.** | `source_content_request_from_query` |mcp/src/agents_remember/serving/review.py:499-519|
| **The result-to-status mapping derived from the refusal's own published code, now over three result types: the four candidate codes go to `404`, `review_adapter_unavailable` to `503`, and everything else — including the expansion's `source_content_unresolved` — to `400`.** | `_status_for`; `ReviewSourceContentResult`; `source_content_unresolved` |mcp/src/agents_remember/serving/review.py:522-539; mcp/src/agents_remember/models/knowledge/review_source_content.py:191-211; mcp/src/agents_remember/models/knowledge/review.py:151-151|
| **The registrar: the three optional ports, the entry route's missing-port `503` and unadmitted-selector `400`, the expansion route's one-line registration, the comparison route's `503`/`400`, the two caught exception types, and the ordering requirement against the greedy static mount.** | `register_review_routes`; `api_review_intent_entries` |mcp/src/agents_remember/serving/review.py:627-627; mcp/src/agents_remember/serving/review.py:644-655|
| **The expansion route's handler and the module-level transport it delegates to: the unwired `503`, the incomplete-generation `400`, and the same two exception shapes the comparison handler uses.** | `api_review_intent_source_content`; `_source_content_response` |mcp/src/agents_remember/serving/review.py:658-658; mcp/src/agents_remember/serving/review.py:720-738|
| The comparison route's handler: the task context, the optional selector pair, and the `400` body that names "or no selector at all" and reports the value that was wrong. | `api_review_intent` |mcp/src/agents_remember/serving/review.py:576-624|
| The one serializer, which keeps an omitted field absent rather than null and so serves all three result types. | `_json` |mcp/src/agents_remember/serving/review.py:627-632|
| The `400` body for a query that did not name the generation it wants opened: the offending component, the exact expected set, and the inventory as the address of the content. | `_incomplete_generation` |mcp/src/agents_remember/serving/review.py:656-672|
| **The three port fields on the collaborators the composition supplies, and their reasons in the layer ranking.** | `knowledge_review`; `knowledge_review_entries`; `review_source_content` | mcp/src/agents_remember/serving/_app_common.py:460-460; mcp/src/agents_remember/serving/_app_common.py:471-471; mcp/src/agents_remember/serving/_app_common.py:481-489 |
| The registration call, made before the greedy static mount and now passing all three ports. | `register_review_routes` | mcp/src/agents_remember/serving/app.py:295-301 |
| The composition root that supplies all three ports, so an omitted adapter refuses rather than serving empty. | `review_port`; `review_entries_port`; `review_source_content_port` | mcp/src/agents_remember/cli/dashboard.py:88-126 |
| **The case that the transport admits exactly the two reviewable selector kinds.** | `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` | mcp/tests/test_knowledge_review_surface.py:1016-1034; mcp/tests/test_knowledge_review_surface.py:1015-1015 |
| **The case that the route serves the typed result and refuses by name with no adapter.** | `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` | mcp/tests/test_knowledge_review_surface.py:1000-1057 |
| **The cases that drive the expansion route through the real composition: a query missing a tree id refused by the transport, and an unwired process refused by name with `_UNWIRED_SOURCE_CONTENT` rather than an empty file.** | `test_a_query_that_does_not_name_the_generation_is_refused_by_the_transport`; `test_an_unwired_process_refuses_the_route_by_name`; `_UNWIRED_SOURCE_CONTENT` |mcp/tests/test_knowledge_review_source_content.py:771-793; mcp/tests/test_knowledge_review_source_content.py:796-819; mcp/src/agents_remember/serving/review.py:121-130|
| The client that names this route and reads its typed body whatever the status, so a refusal renders instead of becoming a transport error. | `reviewSourceContent` | dashboard/src/data/review.ts:654-654; dashboard/src/data/review.ts:421-421 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The routes serve one repository namespace's
candidate and carry no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **the 400/404 mapping collapsed into one implementation, and the two bodies that published no next action now do.** The duplicated `try/except AuthorityError/FileNotFoundError` pair that the comparison handler and `_source_content_response` each carried is now one `_port_outcome(port, request)` reached by both adapters, building its two bodies through one `_transport_refusal(status, detail, *, next_action, offending_input=None)`; both call sites now read `result = _port_outcome(...)` and return it unchanged when it is a `Response`. The **substantive** half of the change is what the bodies say: `bad-path` gained `_AUTHORITY_NEXT_ACTION` and `not-found` gained `_NOT_FOUND_NEXT_ACTION` plus the offending input (the path, in both the `path` and `offendingInput` spellings), because ICR-R16 requires every refusal on this route to carry a usable next action. No status, route, key or model was removed and no other client read those fields — the change is additive on this route's own bodies inside S08. Line count 349 → 401. The card's earlier paragraph that said the two exception types were "caught at each port call" and that the status idiom was "unchanged" has been **replaced** rather than carried. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00), and the leaf's own recorded working candidate states what was actually read; nothing in this leaf is committed, so closeout owns the stamp.
- 2026-09-21T23:25+02:00 — 260921-ICR-L3 curator (same uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation-range repair that clears a `claim_reopen` without any commit.** The finding was not a provenance problem: this leaf's new construct resolves exactly once in the working tree, but its **declaration line** fell outside the range the row cited, so the gate could not see the pointer landing on the new content. The row now cites the declaration beside the statement it already cited (the statement and the construct are one evidence unit, so both ranges belong on the row), and the claim's wording is unchanged because it was already true. Nothing was deleted, weakened, invented or re-stamped.

- 2026-09-21T23:00:00+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the shim became three routes over three ports, and the invariant that said no path is accepted was corrected rather than carried.** ICR-R03@v1 added `KNOWLEDGE_REVIEW_SOURCE_CONTENT_ROUTE` (`/api/review/intent/source-content`), `SourceContentRef` (the whole expansion selector as one `Depends()` value, the `ChangesetFileRef` idiom the change-set routes already use), `ReviewSourceContentPort`, `source_content_request_from_query`, `_source_content_response` and `_incomplete_generation`, and widened `_status_for`/`_json` by the third result type. The card now records the three facts a reader of the transport needs. First, the split's reason: the inventory is the whole task's change set and a payload carrying every file's text would be a document dump, so the expansion is a third **path** and the browser asks for exactly the row a reader opened. Second, the corrected boundary: this is the one route that accepts a `path` — a repository-relative entry path, always sent with both bound code tree ids, and read only if a **measured** change set lists it, with the two tree ids named by the caller rather than resolved by the server so an expansion stays bound to the generation the reader was looking at; no route accepts a filesystem path or a root. Third, the refusal shape: `_UNWIRED_SOURCE_CONTENT` refuses an unwired process as "not served rather than served as an empty file" (an empty document would read as a file this repository does not hold), the expansion's `source_content_unresolved` reaches `400` through the same fall-through as `comparison_refused`, and a blank path or tree id is a `400` naming the exact expected set rather than a server-chosen generation. It also records the extraction that cleared the complexity and argument-count rails without a suppression: the expansion's whole transport became `_source_content_response` and the compare route's parse now takes the selector value instead of six positional scalars. **Citation accounting:** every row of this document was re-derived against this candidate, because the file grew 223 → 349 lines and every construct below the new route constant moved (the selector kinds `:51-63` → `:76-79`, the port types `:65-66` → `:81-83`, `_status_for` `:125-140` → `:199-216`, `register_review_routes` `:143-217` → `:219-247`, `api_review_intent` `:146-190` → `:249-298`, `_json` `:220-223` → `:301-306`, `review_request_from_query` `:83-99` → `:134-173`, `_UNWIRED_ENTRIES` `:68-80` → `:85-97`, and the two `_app_common.py` port rows `:456`/`:467` → `:460`/`:471`); two rows were added for the new route's own constructs and one for its production cases. **No verification stamp was advanced** — the candidate is uncommitted, so the stamp names the master line this card was read against (`d80a0513…`, committed `2026-09-21T19:51:20+02:00`) and the governed closeout owns the real stamp.

- 2026-09-21T15:17:00+02:00 — 260921-ICR-L2 curator, **post-sync citation re-derivation, forced by the merge rather than by a claim change.** The sync brought leaf `260921-ICR-L5`'s landed work into this candidate, which moved the review adapter and the review-surface test module; the two case rows were re-pointed at the merged module's extents (`test_knowledge_review_surface.py:979-997` and `1000-1057`). No claim was re-worded, no anchor dropped and no stamp advanced.

- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the selector became optional at the boundary, and the refusal learned to name the omission.** `review_request_from_query` now returns the task-context request when both selector parameters are absent, refuses a half-named selector and an unadmitted kind with `None` exactly as before, and the route signature declares both parameters optional. The `400` body gained the "or omit both" option in `expected`/`nextAction` and falls back to `selectorId` for `offendingInput` when only that parameter was supplied. Every row in the reference table was re-derived against this candidate — this file grew by 30 lines above the registrar — and the case row now cites the transport case's new lines. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): the shim now serves **two routes from one resolution**. `KNOWLEDGE_REVIEW_ENTRIES_ROUTE` (`/api/review/intent/entries`) lists the subjects the resolved pair can be compared on, and `KnowledgeReviewEntriesPort` is its own port — the task context alone and no selector, because discovering the subject is what that call is for. This card records the three consequences a reader of the transport needs: `_status_for` now accepts both typed results and reads success as `refusal is None` (the entry list has no `state == "review"`), `subject_unresolved` joined the four candidate codes that answer `404`, and the entry handler answers an unwired process with `_UNWIRED_ENTRIES` rather than an empty list, because "no subject is reviewable here" and "nothing can answer that question" are different facts. It also records that the split is a second **path** and never a second adapter, since a caller that had to guess a subject id to reach the comparison route would be choosing the candidate the browser may not choose.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` repointed to mcp/tests/test_knowledge_review_surface.py:767-783. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` repointed to mcp/tests/test_knowledge_review_surface.py:786-842. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's HTTP shim. It records that the module is **transport only** — it selects nothing, ranks nothing, computes no scope and resolves no reference — and the three facts a reader of this route needs: the port exists because `layers.toml` ranks `serving` below `application`, so the shim may not import the operations the adapter composes; the candidate is never addressed by path, because the four query parameters are a task context and one recorded subject and nothing else; and a process with no adapter **refuses by name** (`503`, "not served rather than served empty") instead of rendering an empty surface. It also records the 400/404/503 mapping as derived from the refusal's own published code, and the registration-order requirement against the greedy static mount. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. What was actually read is this leaf's uncommitted working tree, and closeout owns the stamp once the code commit exists.

## 260921-ICR-L10 The Route Admits The Page Itself And Names The Input It Refused

`260921-ICR-L10` (`ICR-R10@v1`) keeps a caller's page-size mistake from escaping as a server
error and makes each refusal name its own offending input. The route takes the paging pair as one
`Depends()` reference each (`ReviewPagingRef`, `ReviewSelectorRef`, with `NO_PAGING` and `NO_SELECTOR` for
the absent spellings) and admits the size in `_admitted_paging`, so a value above the maximum is this
route's own `400` naming the value and the maximum rather than an uncaught request-model error.
`paged_review_request` returns a typed `UnadmittedReviewQuery` carrying the input that actually failed,
which is what the `400` body names; `review_request_from_query` keeps its long-standing contract for its
existing callers, which is why two spellings exist rather than one widened signature.

The route stays transport-only: it reaches every answer through its port, so the page it publishes is the
composition's page and never one this layer built.

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **the route admits the page size in its own vocabulary and names the input it refused.**
`ReviewPagingRef`/`ReviewSelectorRef` (with `NO_PAGING`/`NO_SELECTOR`), `AdmittedPaging`/
`UnadmittedReviewQuery`, `paged_review_request` and `_admitted_paging` are new, so an out-of-range size is
this route's own `400` naming the value and the maximum and a refused cursor names the value that failed.
Every row on this card that cited `serving/review.py` by line was re-derived against this candidate,
because this leaf moved them. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.

## 260921-ICR-L12 The Route Admits One Historical Spelling And Refuses Every Other By Name

`260921-ICR-L12` (`ICR-R12@v1`) admits the record selector at the transport and decides nothing
else about it:

- **the admitted vocabulary is the model's own literal, re-exported as `RECORDED_HISTORY`.** The route
  therefore has one owner for what a historical request may say, and this module decides nothing about
  which records exist.
- **`ReviewSelectorRef` became `ReviewQuestionRef`**, because the fields are one question: which
  subject of which reviewable kind (`ICR-R09@v1`), and whether the caller is reading the live candidate
  or the leaf's recorded comparison (`ICR-R12@v1`). The old name is kept as an alias so the modules and
  cases that already spell it keep working — the same value, because a second class would be a second
  admission of the same three fields.
- **`_admitted_history` refuses everything that is not the one admitted form.** An absent spelling and
  the empty spelling a form sends when the reader picked the live view both mean "no record named"; the
  one historical form is admitted; and any other name is refused in this route's own 400 vocabulary
  with the expected value stated — never resolved to the leaf's record, because a caller that asked for
  a generation the surface does not address must not be handed a different one.
- **the entries route has no record parameter, and that is deliberate rather than an omission.**
  FastAPI drops the parameter it does not declare, and the route's own comment records why: a list is
  offered for a *leaf*, and a leaf whose enclosure is closed lists the subjects of the comparison its
  records hold — the one record a review of that leaf can be opened on. The read is therefore
  unambiguous without a selector, and the route's 400 detail now names the history form alongside the
  selector and the cursor.

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the route admits one historical spelling and refuses every other by name (ICR-R12@v1).** The
admitted form is the request model's own literal (`RECORDED_HISTORY`); the selector ref became
`ReviewQuestionRef` (subject **and** record) with the old name kept as an alias; `_admitted_history`
refuses any other name in the route's own vocabulary and never resolves it to the leaf's record; and the
entries route deliberately takes no record parameter, documented at the route. **Citation accounting:**
every row into this module was re-derived against the candidate. **Stamp accounting:** no verification
stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.

## 260921-ICR-L17 The Route Admits The Previous Binding In Its Own Vocabulary

`260921-ICR-L17` (`ICR-R17@v1`) makes this route's one query parameter richer and gives the admission
two fields to answer for instead of one.

**The parameter.** `ReviewQuestionRef` gains
`previous_binding_digest: Annotated[str | None, Query(alias="previousBindingDigest")]` — the comparison
the caller was already looking at, when the read replaces one. It is admitted here rather than as a
sixth route parameter because it is part of the same question (which subject, which record, and which
generation the answer must be measured against), and because the admission's own vocabulary check
belongs with the two fields it guards.

**The admission, split into its parts.** `_SHA256_DIGEST` compiles the models' own published
`SHA256_PATTERN` rather than re-spelling it, so the transport cannot come to accept a shape the request
model would refuse. `_admitted_binding_digest` treats an **empty spelling as an absent parameter, not a
value** (`previousBindingDigest=` is what a form sends when nothing was displayed), refuses a
non-digest with the offending input named and an `expected` that says what the field is for, and
otherwise returns the value whole. `AdmittedQuestion` is the frozen pair of answers, and
`_admitted_question` performs both admissions as **one decision** — "is this a question this route can
address" — returning the problem each failure earns. `paged_review_request` calls it once and puts
`asked.history` and `asked.previous_binding_digest` on both `ReviewSurfaceRequest` constructions it can
reach.

**What the transport does not do.** It does not compare the digest, resolve it or repair it. Whether it
is the comparison that is there now is the owners' answer, and a digest that no longer matches is
reported as `stale` rather than refused — which is why the shape check is the whole of this route's
business with the value.


## Update History
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the route admits the previous binding identity in its own vocabulary (`ICR-R17@v1`).** `ReviewQuestionRef` gains the `previousBindingDigest` query parameter; `_SHA256_DIGEST` compiles the models' published pattern instead of re-spelling it; `_admitted_binding_digest` collapses the empty spelling to absent and refuses a non-digest by name; `AdmittedQuestion`/`_admitted_question` answer for the record and the previous identity as one decision, and `paged_review_request` forwards both onto the request without comparing either. **Citation accounting:** the rows this leaf's insertions moved were re-derived from each construct's own declaration on the 757-line candidate — `InvariantIdentitySeed` (declared in `models/knowledge/read.py:174`, imported at `serving/review.py:36`), `__all__` `:53-73`, `SELECTOR_KINDS` `:106`, `KnowledgeReviewPort` `:108`, `KnowledgeReviewEntriesPort` `:109`, `api_review_intent_entries` `:645`, `api_review_intent_source_content` `:658`, `_source_content_response` `:720`, `register_review_routes` `:627`. **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the parameter and its admission exist only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.
