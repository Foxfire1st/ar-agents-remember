# mcp/src/agents_remember/serving/review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T13:43:00+02:00 |
| lastVerifiedCommitHash |  `4a0442d62eb842661a3dd04686c376d0f0dbc61f`|
| lastVerifiedCommitDate |  2026-09-20T14:22:54+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| governingOverview | `mcp/src/agents_remember/serving/overview.md` |

## Governing Overview

[serving route overview](overview.md)

## Purpose

The Intent Reviewer's HTTP shim: **transport only, over two ports the composition root supplies.** The
module's own docstring states the boundary: it validates a query string, builds the one typed request
the composition consumes, calls the injected port and maps the typed result onto the change-set
routes' own 400/404 status idiom. It **selects nothing, ranks nothing, computes no scope and resolves
no reference** — every one of those answers comes from the application operations behind the ports,
and the value it returns is that call's own typed result serialized once.

**Why ports rather than direct imports.** `layers.toml` ranks `serving` below `application`, so this
module may not import the read, diff and view operations the adapter composes. It takes
`KnowledgeReviewPort` **and** `KnowledgeReviewEntriesPort` the same way the launch route takes the
capsule compiler: the composition root wires both in `cli/dashboard.py`, and a process that omits
either **refuses by name instead of serving an empty surface**.

**Two routes, because the surface answers two different questions from one resolution.**
`GET /api/review/intent` renders one comparison; `GET /api/review/intent/entries` lists the subjects
that comparison *can* be opened on. The source comment records why the second is a second **path**
rather than a second adapter: a caller that had to guess a subject id to reach the first would be
choosing the candidate, which the browser may not do. Both resolve through the identical application
operation, so the entry a caller is offered and the review it then opens cannot disagree about which
datasets are being compared.

**The candidate is never addressed by path.** The review route accepts a repository, a master, a leaf
id and one recorded subject selector; the entry route accepts the task context alone, because its
whole purpose is to *answer* what the subject is. No filesystem path is accepted on either, so a
browser cannot choose which dataset is reviewed; the resolution behind the ports owns that decision.

## Code Commentary

### Logic

**`KNOWLEDGE_REVIEW_ROUTE` is the comparison route, and `KNOWLEDGE_REVIEW_ENTRIES_ROUTE` is the
entry route; both are GET-only.** `"/api/review/intent"` and `"/api/review/intent/entries"` are
module constants so the browser client, the route registrars and the tests all name one spelling
each. The source comment on the first records why the verb is narrow: the surface produces no record,
and the assessment path this increment does not ship would not be reached from here. The comment on
the second records the split's reason — the two answer different questions from one resolution
("which subjects the pair can be compared on" versus "what one such comparison renders"), and a
caller that had to guess a subject id to reach the first would be choosing the candidate. Both routes
are registered through `register_review_routes`, whose docstring carries the ordering requirement —
**it must be called before the greedy static mount**, which is why `serving/app.py` calls it in the
block of explicit route registrars rather than after `mount_static`.

**`SELECTOR_KINDS` is the two-member admission vocabulary, and every other seed kind is refused rather
than mapped.** `("invariant", "family")` is exactly the two identity seeds R07 declares; the source
comment states that every other seed kind addresses a revision, a membership or a claim rather than a
subject a curator reviews. `review_request_from_query` is the whole parse: an `invariant` kind builds
`InvariantIdentitySeed(invariant_id=selector_id)`, a `family` kind builds
`FamilyIdentitySeed(family_id=selector_id)`, anything else returns `None` — and `None` is what the
handler turns into a `400` rather than a defaulted selector. On the admitted path it returns the one
`ReviewSurfaceRequest(repository_id=..., master=..., leaf_id=..., selector=seed)` that both the
transport and the composition consume.

**`KnowledgeReviewPort` and `KnowledgeReviewEntriesPort` are plain callable types, not protocol
classes.** `Callable[[ReviewSurfaceRequest], KnowledgeReviewResult]` and
`Callable[[str, str, str], ReviewEntryListResult]` are the whole contracts: one typed request in, one
typed result out — and the entry port's three positional strings are the task context
(`repository_id`, `master`, `leaf_id`) with **no selector at all**, because a selector is precisely
what that call exists to discover. The routes never inspect a port, so a caller that supplies the
application adapter and a test that supplies a fake are indistinguishable to the registrar. The
module re-exports `ReviewSurfaceRequest`, `KnowledgeReviewResult` and `ReviewEntryListResult`
conceptually through its imports from `models/knowledge/review.py` and its own `__all__`.

**A missing port is a named refusal, not an empty surface — and the entry route has its own.**
`register_review_routes` takes `port: KnowledgeReviewPort | None` and
`entries_port: KnowledgeReviewEntriesPort | None = None`; when the comparison port is `None`,
`api_review_intent` returns a `503` whose `detail` says no review adapter is wired into this process,
that the Intent Reviewer therefore cannot resolve a candidate, and that "the surface is not served
rather than served empty", with a `nextAction` naming the composition root that supplies the adapter.
When the *entry* port is `None`, `api_review_intent_entries` returns the module's own
`_UNWIRED_ENTRIES` body with `status: "unavailable"` and the same "not served rather than served
empty" reason and next action. The entry answer is deliberately **not** an empty list: "no subject is
reviewable here" and "nothing can answer that question" are different facts, and only one of them is
true when the process was composed without the port. That is the reason both ports are optional rather
than required at registration: a process that legitimately has no dashboard composition gets a typed
answer instead of a pane that renders nothing.

**`_status_for` maps one typed result onto the change-set routes' own two-shape idiom, and now serves
both result types.** The union `KnowledgeReviewResult | ReviewEntryListResult` is accepted because
both models carry the same two fields this function reads: a `refusal` and, inside it, a published
`code`. `result.refusal is None` is the `200` case — which is how the entry list's `state == "entries"`
and the review's `state == "review"` both map to success without a second local table. Otherwise
`review_adapter_unavailable` maps to `503`, the **four** candidate codes `candidate_unresolved`,
`candidate_not_live`, `candidate_dataset_absent` and `subject_unresolved` map to `404`, and every
remaining code (`comparison_refused`) maps to `400`. The status is therefore derived from the
refusal's own published code rather than from a local table of route conditions.

**The two exception types are caught at the comparison port call and turned into the same two
shapes.** `AuthorityError` becomes a `400` with `status: "bad-path"` and the error's own `str`, and
`FileNotFoundError` becomes a `404` with `status: "not-found"` and the offending `path`. Everything
else the port raises is left to propagate to the application's own error handling rather than being
silently reshaped here. The entry handler adds no catch of its own: an absent dataset half is the
application operation's own typed refusal, not an exception, so it arrives as a `404` through
`_status_for` like every other candidate state.

**`_json` serializes a typed result exactly once, through the model that declares its shape.**
`result.model_dump(mode="json", exclude_none=True)` is the whole function, and its union parameter is
what lets one serializer serve both routes. `exclude_none=True` is what makes the client's optional
fields *absent* rather than `null`, which is the same rule the browser client mirrors: a field the
server omits is absent on the client, so an unresolved reference stays unresolved rather than
becoming a defaulted empty one. It is also why an `entries` result carries no `refusal` key and a
refused one carries no `entries` key.

**`register_review_routes` accepts `config` and deliberately discards it.** `del config` is the first
statement of the body, with the docstring explaining that the parameter is kept for symmetry with the
other route registrars and for the workspace facts a port may need, while the routes themselves
resolve nothing from it because resolution belongs to the ports' own tier. The registrar then declares
both handlers inside its own scope — `api_review_intent_entries` first, then `api_review_intent` — so
the closures over `entries_port` and `port` are the only state each route carries.

**The two query aliases are spelled once, through `Query(alias=...)`.** `selectorKind` and `selectorId`
are `Annotated[str, Query(alias="selectorKind")]` and `Annotated[str, Query(alias="selectorId")]`, so
the camel-case wire names the browser client sends are declared at the signature rather than
normalized later. The `bad-request` body for an unadmitted selector echoes `offendingInput:
selectorKind` and `expected: ", ".join(SELECTOR_KINDS)`, so the refusal names what was sent and what
would have been admitted.

### Conventions

The module imports its vocabulary rather than declaring it: `KnowledgeReviewResult`,
`ReviewEntryListResult`, `ReviewSurfaceRequest`, `InvariantIdentitySeed`, `FamilyIdentitySeed` and
`KnowledgeReadSeed` all come from the models layer, and `McpRuntimeConfig` from the kernel. `__all__`
names exactly the six public names — `KNOWLEDGE_REVIEW_ROUTE`, `KNOWLEDGE_REVIEW_ENTRIES_ROUTE`,
`KnowledgeReviewPort`, `KnowledgeReviewEntriesPort`, `register_review_routes`,
`review_request_from_query` — leaving `_status_for`, `_json` and `_UNWIRED_ENTRIES` reachable but
unpublished. It uses `fastapi.APIRouter`-free direct `@app.get(...)` registration like the other
change-set route registrars, and its JSON bodies are plain dicts shaped like the change-set routes'
own error envelopes (`status`, `detail`, `nextAction`) rather than a second error model.

### Invariants And Boundaries

- **Transport only.** The module computes no scope, resolves no reference and selects no candidate; it
  builds one request, calls one port and maps one result. The entry route calls the other port with
  the task context alone and maps its result through the same status function.
- **Two routes, one resolution.** The entry list and the comparison are served from the same
  application operation, so an offered subject and the review that opens on it cannot name different
  candidates. The split is a second **path**, never a second adapter.
- **No path is accepted.** The comparison route's four query parameters are a task context and one
  recorded subject; the entry route takes the task context and nothing else. Neither accepts a path,
  so a browser cannot choose which dataset is reviewed.
- **Only two selector kinds are admitted, and every other is refused by name.** `SELECTOR_KINDS` is the
  admission vocabulary and the `400` echoes the offending input beside the admitted pair.
- **A process with no adapter refuses by name, on both routes.** The `503`s state that the surface is
  not served rather than served empty, so an unreachable adapter and an empty pane stay different
  facts — and the entry route in particular never answers an unwired process with an empty list.
- **The status is the refusal's own code.** `_status_for` reads the published `code` rather than
  re-deriving a condition locally, and it reads only `refusal is None` for success so one mapping
  serves both typed results.
- **The result is serialized once, by the model.** `exclude_none=True` keeps an omitted field absent,
  which is the rule the browser client mirrors and why a refused entry read carries no `entries` key.
- **Rank is the reason for the indirection.** `serving` may not import `application`, so the ports are
  the only route to the adapter; the wiring belongs to the composition root.
- **Registration order matters.** Both routes must be registered before the greedy static mount.

### Todos

None recorded. An assessment-publication route is deliberately not shipped by this increment.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the shim's own docstring, the two
route constants, the entry port and its unwired answer, the parse function, the result-to-status
mapping, the registrar and its two handlers, the serializer, the two port fields the composition
supplies, and the cases that drive the routes with and without an adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| The shim's own statement of what it decides (nothing), why the ports exist rather than direct imports, and the fact that no path is accepted. | `SELECTOR_KINDS` | mcp/src/agents_remember/serving/review.py:1-30; mcp/src/agents_remember/serving/review.py:51-63 |
| The published surface: two route constants, two port types, one parser and one registrar. | `__all__` | mcp/src/agents_remember/serving/review.py:40-49 |
| **The two admitted selector kinds and the one parse that maps them onto the read operation's own seeds, returning `None` for every other kind.** | `review_request_from_query`; `InvariantIdentitySeed`; `FamilyIdentitySeed` | mcp/src/agents_remember/serving/review.py:83-99; mcp/src/agents_remember/models/knowledge/read.py:1-60 |
| The comparison port type: one typed request in, one typed result out. | `KnowledgeReviewPort`; `ReviewSurfaceRequest`; `KnowledgeReviewResult` | mcp/src/agents_remember/serving/review.py:65-65; mcp/src/agents_remember/models/knowledge/review.py:145-158; mcp/src/agents_remember/models/knowledge/review.py:574-589 |
| **The entry port type: the task context alone and no selector, because discovering the subject is what that call is for — and the typed entry result it returns.** | `KnowledgeReviewEntriesPort`; `ReviewEntryListResult` | mcp/src/agents_remember/serving/review.py:66-66; mcp/src/agents_remember/models/knowledge/review.py:592-620 |
| **The result-to-status mapping derived from the refusal's own published code, with the four candidate codes — now including `subject_unresolved` — going to 404 and success read as `refusal is None` so one mapping serves both typed results.** | `_status_for` | mcp/src/agents_remember/serving/review.py:102-117 |
| **The registrar: the comparison route's missing-port `503`, the unadmitted-selector `400`, the two caught exception types, and the ordering requirement against the greedy static mount.** | `register_review_routes`; `api_review_intent` | mcp/src/agents_remember/serving/review.py:120-136; mcp/src/agents_remember/serving/review.py:146-190 |
| **The entry route's handler: it takes the task context alone and answers an unwired process with `_UNWIRED_ENTRIES` rather than an empty list.** | `api_review_intent_entries`; `_UNWIRED_ENTRIES` | mcp/src/agents_remember/serving/review.py:137-143; mcp/src/agents_remember/serving/review.py:68-80 |
| The one serializer, which keeps an omitted field absent rather than `null` and so serves both result types. | `_json` | mcp/src/agents_remember/serving/review.py:193-196 |
| The comparison route constant itself, GET-only, and the comment recording that the surface produces no record. | `KNOWLEDGE_REVIEW_ROUTE` | mcp/src/agents_remember/serving/review.py:51-52 |
| **The entry route constant and the comment recording why it is a second path rather than a second adapter.** | `KNOWLEDGE_REVIEW_ENTRIES_ROUTE` | mcp/src/agents_remember/serving/review.py:54-58 |
| The two port fields on the collaborators the composition supplies, and their reasons in the layer ranking. | `knowledge_review`; `knowledge_review_entries` | mcp/src/agents_remember/serving/_app_common.py:456-456; mcp/src/agents_remember/serving/_app_common.py:467-467 |
| The registration call, made before the greedy static mount and now passing both ports. | `register_review_routes` | mcp/src/agents_remember/serving/app.py:139-139; mcp/src/agents_remember/serving/app.py:292-298 |
| The composition root that supplies both ports, so an omitted adapter refuses rather than serving empty. | `review_port`; `review_entries_port` | mcp/src/agents_remember/cli/dashboard.py:85-104 |
| **The case that the transport admits exactly the two reviewable selector kinds.** | `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` | mcp/tests/test_knowledge_review_surface.py:770-786 |
| **The case that the route serves the typed result and refuses by name with no adapter.** | `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` | mcp/tests/test_knowledge_review_surface.py:789-845 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The route serves one repository namespace's
candidate and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): the shim now serves **two routes from one resolution**. `KNOWLEDGE_REVIEW_ENTRIES_ROUTE` (`/api/review/intent/entries`) lists the subjects the resolved pair can be compared on, and `KnowledgeReviewEntriesPort` is its own port — the task context alone and no selector, because discovering the subject is what that call is for. This card records the three consequences a reader of the transport needs: `_status_for` now accepts both typed results and reads success as `refusal is None` (the entry list has no `state == "review"`), `subject_unresolved` joined the four candidate codes that answer `404`, and the entry handler answers an unwired process with `_UNWIRED_ENTRIES` rather than an empty list, because "no subject is reviewable here" and "nothing can answer that question" are different facts. It also records that the split is a second **path** and never a second adapter, since a caller that had to guess a subject id to reach the comparison route would be choosing the candidate the browser may not choose.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` repointed to mcp/tests/test_knowledge_review_surface.py:767-783. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` repointed to mcp/tests/test_knowledge_review_surface.py:786-842. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's HTTP shim. It records that the module is **transport only** — it selects nothing, ranks nothing, computes no scope and resolves no reference — and the three facts a reader of this route needs: the port exists because `layers.toml` ranks `serving` below `application`, so the shim may not import the operations the adapter composes; the candidate is never addressed by path, because the four query parameters are a task context and one recorded subject and nothing else; and a process with no adapter **refuses by name** (`503`, "not served rather than served empty") instead of rendering an empty surface. It also records the 400/404/503 mapping as derived from the refusal's own published code, and the registration-order requirement against the greedy static mount. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
