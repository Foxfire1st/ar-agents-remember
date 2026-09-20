# mcp/src/agents_remember/serving/review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:05+02:00 |
| lastVerifiedCommitHash |  `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate |  2026-09-20T02:00:33+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| governingOverview | `mcp/src/agents_remember/serving/overview.md` |

## Governing Overview

[serving route overview](overview.md)

## Purpose

The Intent Reviewer's HTTP shim: **transport only, over a port the composition root supplies.** The
module's own docstring states the boundary: it validates a query string, builds the one typed request
the composition consumes, calls the injected port and maps the typed result onto the change-set
routes' own 400/404 status idiom. It **selects nothing, ranks nothing, computes no scope and resolves
no reference** — every one of those answers comes from the application operations behind the port, and
the value it returns is that call's own typed result serialized once.

**Why a port rather than a direct import.** `layers.toml` ranks `serving` below `application`, so this
module may not import the read, diff and view operations the adapter composes. It takes
`KnowledgeReviewPort` the same way the launch route takes the capsule compiler: the composition root
wires it in `cli/dashboard.py`, and a process that omits it **refuses by name instead of serving an
empty surface**.

**The candidate is never addressed by path.** The route accepts a repository, a master, a leaf id and
one recorded subject selector. No filesystem path is accepted, so a browser cannot choose which
dataset is reviewed; the resolution behind the port owns that decision.

## Code Commentary

### Logic

**`KNOWLEDGE_REVIEW_ROUTE` is the one route the surface is reached through, and it is GET-only.**
`"/api/review/intent"` is a module constant so the browser client, the route registrar and the tests
all name one spelling. The source comment records why the verb is narrow: the surface produces no
record, and the assessment path this increment does not ship would not be reached from here. The route
is registered through `register_review_routes`, whose docstring carries the ordering requirement —
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

**`KnowledgeReviewPort` is a plain callable type, not a protocol class.**
`Callable[[ReviewSurfaceRequest], KnowledgeReviewResult]` is the whole contract: one typed request in,
one typed result out. The route never inspects the port, so a caller that supplies the application
adapter and a test that supplies a fake are indistinguishable to the registrar. The module re-exports
`ReviewSurfaceRequest` and `KnowledgeReviewResult` conceptually through its imports from
`models/knowledge/review.py` and its own `__all__`.

**The missing port is a named refusal, not an empty surface.** `register_review_routes` takes
`port: KnowledgeReviewPort | None`; when it is `None`, `api_review_intent` returns a `503` whose
`detail` says no review adapter is wired into this process, that the Intent Reviewer therefore cannot
resolve a candidate, and that "the surface is not served rather than served empty", with a `nextAction`
naming the composition root that supplies the adapter. That is the reason the port is optional rather
than required at registration: a process that legitimately has no dashboard composition gets a typed
answer instead of a pane that renders nothing.

**`_status_for` maps one typed result onto the change-set routes' own two-shape idiom.** A
`state == "review"` result is `200`. Otherwise the function asserts the refusal is present — the model
guarantees it — and maps `review_adapter_unavailable` to `503`, the three candidate codes
`candidate_unresolved`, `candidate_not_live` and `candidate_dataset_absent` to `404`, and every
remaining code (`comparison_refused`) to `400`. The status is therefore derived from the refusal's own
published code rather than from a local table of route conditions.

**Two exception types are caught at the port call and turned into the same two shapes.**
`AuthorityError` becomes a `400` with `status: "bad-path"` and the error's own `str`, and
`FileNotFoundError` becomes a `404` with `status: "not-found"` and the offending `path`. Everything
else the port raises is left to propagate to the application's own error handling rather than being
silently reshaped here.

**`_json` serializes the typed result exactly once, through the model that declares its shape.**
`result.model_dump(mode="json", exclude_none=True)` is the whole function. `exclude_none=True` is what
makes the client's optional fields *absent* rather than `null`, which is the same rule the browser
client mirrors: a field the server omits is absent on the client, so an unresolved reference stays
unresolved rather than becoming a defaulted empty one.

**`register_review_routes` accepts `config` and deliberately discards it.** `del config` is the first
statement of the body, with the docstring explaining that the parameter is kept for symmetry with the
other route registrars and for the workspace facts a port may need, while the route itself resolves
nothing from it because resolution belongs to the port's own tier. The registrar then declares the
handler `api_review_intent` inside its own scope, so the closure over `port` is the only state the
route carries.

**The two query aliases are spelled once, through `Query(alias=...)`.** `selectorKind` and `selectorId`
are `Annotated[str, Query(alias="selectorKind")]` and `Annotated[str, Query(alias="selectorId")]`, so
the camel-case wire names the browser client sends are declared at the signature rather than
normalized later. The `bad-request` body for an unadmitted selector echoes `offendingInput:
selectorKind` and `expected: ", ".join(SELECTOR_KINDS)`, so the refusal names what was sent and what
would have been admitted.

### Conventions

The module imports its vocabulary rather than declaring it: `KnowledgeReviewResult`,
`ReviewSurfaceRequest`, `InvariantIdentitySeed`, `FamilyIdentitySeed` and `KnowledgeReadSeed` all come
from the models layer, and `McpRuntimeConfig` from the kernel. `__all__` names exactly the four public
names — `KNOWLEDGE_REVIEW_ROUTE`, `KnowledgeReviewPort`, `register_review_routes`,
`review_request_from_query` — leaving `_status_for` and `_json` reachable but unpublished. It uses
`fastapi.APIRouter`-free direct `@app.get(...)` registration like the other change-set route
registrars, and its JSON bodies are plain dicts shaped like the change-set routes' own error
envelopes (`status`, `detail`, `nextAction`) rather than a second error model.

### Invariants And Boundaries

- **Transport only.** The module computes no scope, resolves no reference and selects no candidate; it
  builds one request, calls the port and maps one result.
- **No path is accepted.** The four query parameters are a task context and one recorded subject; a
  browser cannot choose which dataset is reviewed.
- **Only two selector kinds are admitted, and every other is refused by name.** `SELECTOR_KINDS` is the
  admission vocabulary and the `400` echoes the offending input beside the admitted pair.
- **A process with no adapter refuses by name.** The `503` states that the surface is not served
  rather than served empty, so an unreachable adapter and an empty pane stay different facts.
- **The status is the refusal's own code.** `_status_for` reads the published `code` rather than
  re-deriving a condition locally.
- **The result is serialized once, by the model.** `exclude_none=True` keeps an omitted field absent,
  which is the rule the browser client mirrors.
- **Rank is the reason for the indirection.** `serving` may not import `application`, so the port is
  the only route to the adapter; the wiring belongs to the composition root.
- **Registration order matters.** The route must be registered before the greedy static mount.

### Todos

None recorded. An assessment-publication route is deliberately not shipped by this increment.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the shim's own docstring, the one
route constant, the parse function, the result-to-status mapping, the registrar and its handler, the
serializer, the port field the composition supplies, and the two cases that drive the route with and
without an adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| The shim's own statement of what it decides (nothing), why the port exists rather than a direct import, and the fact that no path is accepted. | `SELECTOR_KINDS` | mcp/src/agents_remember/serving/review.py:1-18; mcp/src/agents_remember/serving/review.py:47-56 |
| The published surface: one route constant, one port type, one parser and one registrar. | `__all__` | mcp/src/agents_remember/serving/review.py:40-45 |
| **The two admitted selector kinds and the one parse that maps them onto the read operation's own seeds, returning `None` for every other kind.** | `review_request_from_query`; `InvariantIdentitySeed`; `FamilyIdentitySeed` | mcp/src/agents_remember/serving/review.py:59-75; mcp/src/agents_remember/models/knowledge/read.py:1-60 |
| The port type: one typed request in, one typed result out. | `KnowledgeReviewPort`; `ReviewSurfaceRequest`; `KnowledgeReviewResult` | mcp/src/agents_remember/serving/review.py:56-56; mcp/src/agents_remember/models/knowledge/review.py:136-149; mcp/src/agents_remember/models/knowledge/review.py:546-561 |
| **The result-to-status mapping derived from the refusal's own published code, with the three candidate codes going to 404.** | `_status_for` | mcp/src/agents_remember/serving/review.py:78-89 |
| **The registrar: the missing-port `503`, the unadmitted-selector `400`, the two caught exception types, and the ordering requirement against the greedy static mount.** | `register_review_routes`; `api_review_intent` | mcp/src/agents_remember/serving/review.py:92-149 |
| The one serializer, which keeps an omitted field absent rather than `null`. | `_json` | mcp/src/agents_remember/serving/review.py:152-155 |
| The route constant itself, GET-only, and the comment recording that the surface produces no record. | `KNOWLEDGE_REVIEW_ROUTE` | mcp/src/agents_remember/serving/review.py:47-49 |
| The port field on the collaborators the composition supplies, and its reason in the layer ranking. | `knowledge_review` | mcp/src/agents_remember/serving/_app_common.py:456-467 |
| The registration call, made before the greedy static mount. | `register_review_routes` | mcp/src/agents_remember/serving/app.py:139-139; mcp/src/agents_remember/serving/app.py:292-296 |
| The composition root that supplies the port, so an omitted adapter refuses rather than serving empty. | `review_port` | mcp/src/agents_remember/cli/dashboard.py:76-98 |
| **The case that the transport admits exactly the two reviewable selector kinds.** | `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` | mcp/tests/test_knowledge_review_surface.py:767-783 |
| **The case that the route serves the typed result and refuses by name with no adapter.** | `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` | mcp/tests/test_knowledge_review_surface.py:786-842 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The route serves one repository namespace's
candidate and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T22:28:52+00:00: Generated citation repair: `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds` repointed to mcp/tests/test_knowledge_review_surface.py:767-783. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` repointed to mcp/tests/test_knowledge_review_surface.py:786-842. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's HTTP shim. It records that the module is **transport only** — it selects nothing, ranks nothing, computes no scope and resolves no reference — and the three facts a reader of this route needs: the port exists because `layers.toml` ranks `serving` below `application`, so the shim may not import the operations the adapter composes; the candidate is never addressed by path, because the four query parameters are a task context and one recorded subject and nothing else; and a process with no adapter **refuses by name** (`503`, "not served rather than served empty") instead of rendering an empty surface. It also records the 400/404/503 mapping as derived from the refusal's own published code, and the registration-order requirement against the greedy static mount. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
