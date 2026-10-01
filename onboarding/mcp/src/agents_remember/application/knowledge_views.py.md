# mcp/src/agents_remember/application/knowledge_views.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The application seam for the five query views: the module that, in its own docstring's words, "resolves
the snapshot, admits the request, builds the reader port, and returns the typed payload the renderer
produced." It *deliberately does not have* any authority of its own, any durable state, or any selection
logic — "like them it decides no authority and holds no durable state" — and it owns no validation, no
SQL, no row shape and no ordering rule: its nine module-level functions and zero classes only admit,
dispatch, count and refuse. It also deliberately has no fallback snapshot: a view "cannot be handed a
snapshot a caller wrote down," because the identity it declares comes from the shipped
`open_read_context` resolver reading the dataset at the path, and a continuation presented against
another snapshot is refused outright — "There is no re-resolution and no partial answer."

## Code Commentary

### Logic

**`read_knowledge_view` is the whole public operation, and its four steps are the module's shape.**
It admits the request through `_admit` and returns `_refused(...)` immediately when that yields a
refusal; opens the database read-only through `open_read_only_database` and reads its schema identity
through `inspect_schema`, closing the probe in a `finally` before the real reader exists; builds the
reader port through `open_view_reader`, which is handed the request's `repository_id`, that identity and
the caller's optional `resolve_anchor`; and then renders inside a `try/finally` that closes the
connection. The probe is released before the reader is opened, so the seam never holds two handles on one
file, and the connection lifetime belongs to this function alone. `__all__` is the seam's public surface
— `VIEW_RENDERER_VERSION` and `read_knowledge_view` — and the seam's docstring names it the seventh
application seam in that series while listing seven siblings beside it.

**The snapshot comes from the shipped resolver, so a caller cannot declare one.** `_snapshot_of`
delegates to `snapshot_of_context` from `models/knowledge/read.py` rather than assembling a snapshot
here, and the same snapshot is what the payload, the completeness scope and the continuation all name.
The docstring states the consequence: "The snapshot a view declares comes from ``open_read_context``,
which reads the identity the dataset at that path actually holds," and the three comparisons the other
seams make — bound namespace, declared generation, declared logical digest — "are made here for the same
reason." `open_view_context` is the re-exported convenience constructor for that resolver, carrying the
same keyword arguments, and it is explicitly marked in the source as a re-exported convenience rather
than the ordinary path.

**The continuation is checked before any row is read, and both identities are named when it fails.**
That check is the last step of `_admit`, whose own docstring says the order: "Every admission check,
before a row is read: ordering input, then the continuation binding." `require_continuation_snapshot`
compares the token's recorded `snapshot_logical_digest` with the context's own and returns a `ViewRefusal`
with `code="continuation_binding_mismatch"`, `expected=continuation.snapshot_logical_digest` and
`observed=snapshot.logical_digest` — the two identities the docstring promises — plus the remedy "re-read
the scope at the snapshot the continuation names, or start a new walk." No rows are read on that path, so
a caller that presents a stale continuation receives no page at all rather than a page from the wrong
snapshot; and crucially the two identities are named even though the log line in the module's mind is
"no page" — nothing is silently re-resolved and nothing is returned partially.

**`_admit` is an ordered gate, and each of its three checks is a named refusal or `None`.** The first
screen is membership of `request.ordering_input` in the imported `ORDERING_INPUTS`, refused as
`unadmitted_ordering_input` with the detail that "no rows are returned and no default order is
substituted." The second is that the context's namespace equals the request's, refused as
`snapshot_unavailable` with "the declared snapshot belongs to another repository namespace." The third
is the continuation binding, and a request with no continuation returns `None` after the first two
screens — so an ordering input that is not admitted is refused before the namespace is even compared.
All three happen before the database is opened: `read_knowledge_view` calls `_admit` before it touches
`database_path`, so a refused request never opens the file. `_refused` is the one builder that turns any
of those refusals into `ViewResult(state="refused", repository_id=..., refusal=...)`, which is why every
failure in this module leaves through the shipped `ViewRefusal` vocabulary instead of an exception.

**`_render` dispatches one view, converts a raised ordering error back into a refusal, and assembles the
typed payload around the rows it got.** It calls `_RENDERERS[request.view](reader, request)` and unpacks
the four-element tuple the renderers return — rows, limitations, rule ids and the selection's own size.
An `UnadmittedOrderingInput` raised below the table is caught and returned as a
`ViewRefusal(code="unadmitted_ordering_input")`, so the renderer's exception never escapes the public
function. The row set is then checked with `require_distinct_row_subjects`
(`code="ambiguous_row_identity"`), and a duplicate subject refuses the whole view rather than letting the
seam choose which of two rows is authoritative. Counts come from `_counts`, and `ViewCompleteness` is
built with `complete_within_declared_scope=continuation is None` — a completeness statement that is a
fact about this page's paging rather than a claim about the dataset.

**The page arithmetic is derived from the token, not carried.** `_counts` returns `rows_remaining` as
`max(total - returned, 0)` where `total` is the selection's own size returned by the renderer that made
it, so "a page can never report a scope smaller than the walk it is a page of — which is the packet's own
non-conformance example." When rows remain, `_render` recovers the position from the continuation's token
by taking the last `:`-separated segment and parsing it as digits (falling back to `0`), then mints the
next cursor with `continuation_for(view=..., snapshot=..., position=offset + len(rows))`. The renderer
computes the same offset independently and discards its own result, so the seam's choice of the token as
the source of truth is the coupling that keeps a resumed walk contiguous.

**The required quantity set is measured from the reader and the selection, and the quantities that have
no meaning for a view say so.** `_counts` reads `reader.registered_counts()` for the two registered
totals, reports `rows_returned` as the page's own length, and sets `facets_omitted` to `None` for
`invariant` and `source_context` (the quantity "says so in the state it carries" rather than reporting a
zero) and to `0` for the other three. `dependency_content_identity_mismatches` is computed only for
`review_matrix`, through `_dependency_mismatches`, which walks `reader.rows("verification_observation")`
and counts rows whose `result_artifact` records `digest_checked_against_bytes is False`. Rows the
renderer withheld for want of a class are counted by the payload's `limitations` and by
`unresolved_references`, "because a withheld row is an unresolved input and not an absent fact." The
`ViewCounts` model itself is not owned here: the seam passes the named quantities to the shipped
`view_counts` constructor and the payload shape stays in the models layer.

**Two lookup tables keyed by the same five view names exist because the seam dispatches on one thing and
builds on another.** `_RENDERERS` maps each view name to the function that selects, orders and pages its
rows, and imports all five from `knowledge_view_render`; `_PAYLOADS` maps the same five names to the
shipped payload classes (`SourceContextView`, `InvariantView`, `FamilyView`, `ReviewMatrixView`,
`CurationQueueView`) and imports those from `models/knowledge/view.py`. The tables are separate
declarations of one vocabulary, which is what lets either an unhandled view name or a mismatched pair
fail as a `KeyError` at dispatch rather than producing an untyped payload. The view names themselves are
not spelled here as a vocabulary at all: they arrive on the request and are looked up, so adding a sixth
view requires an entry in both tables.

**`VIEW_RENDERER_VERSION` is a recorded value, not a package version read at display time.**
`"knowledge-view-renderer/1"` travels as the `extractors` member of `ViewScope` and again as the
payload's `renderer_version`, which is what the source comment means by "two payloads produced by
different renderer versions are distinguishable from the payloads themselves." `RECORDED_GRAPH` and
`TRAVERSAL_POLICY` are the other two named scope inputs — "The recorded graph the selection walks, and
the traversal policy it walks it under" — and the scope also carries
`snapshot_logical_digest=snapshot.logical_digest`, so a completeness statement is bounded to the three
inputs it was made about: one snapshot, one graph, one policy, plus the extractor version.

**The remaining two functions publish, rather than compute, what other surfaces need.** `view_purposes`
returns `dict(VIEW_PURPOSES)` — a copy of the models layer's mapping, so the interface `KS-R22@v1`
mounts reads the published one-line purpose of each view and cannot mutate the canonical mapping by
holding it. `open_view_context` re-exports the shipped resolver's constructor with the same
`repository_root`, `code_tree_id` and `task_ref` keywords, so a caller can resolve the context a view
read is addressed at without importing the read seam directly. Neither function computes anything.

### Conventions

The module holds no model of its own: no class is declared here, and every value it returns is a shipped
type imported from the models layer — `ViewResult`, `ViewRefusal`, `ViewRequest`, `ViewScope`,
`ViewCompleteness`, `ViewCounts`, `ViewSourceCounts` and the five payload classes — while
`KnowledgeReadContext`, `KnowledgeReadSnapshot` and `KnowledgeRefusal` come from
`models/knowledge/read.py` and `models/knowledge/result.py`. The reader port is imported, not
re-declared: `KnowledgeViewReader` is the protocol, `open_view_reader` is the store-side constructor, and
`read_knowledge_view`'s `reader` parameter is typed loosely because the port is the contract the renderers
consume. The ordering vocabulary is likewise imported — `ORDERING_INPUTS` from
`models/knowledge/classification.py` — so the seam's admission check and the renderer's raise test the
same tuple rather than two spellings of it. The five view names are a lookup, not a restated vocabulary:
the only place they appear is as the keys of the two dispatch tables, and the shipped `VIEW_PURPOSES`
keeps the prose. `_snapshot_of` and `_refused` are deliberately one-line wrappers over
`snapshot_of_context` and the refusal/payload constructors, so the seam's own vocabulary is visible at
the call sites and no second implementation of either exists. `__all__` names exactly the two public
names, leaving `_admit`, `_snapshot_of`, `_refused`, `_render`, `_counts`, `_dependency_mismatches`,
`_RENDERERS`, `_PAYLOADS`, `view_purposes` and `open_view_context` reachable but unpublished — and the
continuation token is treated as opaque in the only place it is parsed, with a digit check and a `0`
fallback rather than a schema.

### Invariants And Boundaries

- **The continuation is checked before any row is read.** `_admit`'s own docstring states the order
  (ordering input, then the continuation binding), and `require_continuation_snapshot` names both the
  continuation's snapshot digest and the context's in its refusal; a mismatched continuation therefore
  produces a refusal and no page.
- **No admission check touches the database.** All three screens in `_admit` run before
  `read_knowledge_view` opens `database_path`, so a refused request opens no file and reads no row.
- **The seam decides no authority and holds no durable state.** It selects nothing, orders nothing,
  classifies nothing and stores nothing; the request is passed through to the renderer and the rows come
  back already ordered and already classified.
- **The two dispatch tables must stay in step, and their disagreement is loud.** `_RENDERERS` and
  `_PAYLOADS` are two declarations of one five-name vocabulary, so a view present in one and absent from
  the other fails at the lookup rather than yielding a payload of the wrong type.
- **Page arithmetic is honest about scope.** `rows_remaining` is `max(total - returned, 0)` with `total`
  the renderer's own selection size, and the completeness scope carries the snapshot digest, the recorded
  graph, the traversal policy and the renderer version together, so completeness is claimed for declared
  inputs only.
- **Every failure leaves as a typed refusal.** `_refused` wraps a `ViewRefusal` into
  `ViewResult(state="refused", ...)`, the `UnadmittedOrderingInput` raised by the renderer is converted
  the same way, and no code path in this module raises out of `read_knowledge_view`.
- **The connection the reader is opened with is closed by this seam.** `open_view_reader` returns the
  reader and the handle together, and `read_knowledge_view` closes the handle in a `finally`, so the
  reader's lifetime cannot outlive the call.
- **A resumed page continues from the token, not from the renderer's offset.** `_render` re-derives the
  position from the continuation token's tail and mints the next `ViewContinuation` through
  `continuation_for` at `offset + len(rows)`, while the renderer's own next offset is discarded.
- **Version and scope values are recorded, not computed.** `VIEW_RENDERER_VERSION` is a literal that
  travels on every payload, and `RECORDED_GRAPH` and `TRAVERSAL_POLICY` are named constants, so a payload
  is distinguishable from another one produced by a different renderer or a different walk.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the seam's own docstring and functions,
the shipped resolver and snapshot model it delegates to, the read-only connection and schema probe it
opens, the reader port it builds, the payload and refusal vocabulary it imports, the renderer module it
dispatches into, and the case that proves a continuation presented against another snapshot is refused.
One detail a reader should carry: the two dispatch tables are the only place this module spells the five
view names, and the seam's own ordering arithmetic is derived from the continuation token's tail rather
than from the renderer's returned offset.

- The seam's own statement of what it decides, resolves, admits and returns, plus the continuation rule and the seventh-seam claim with its seven named siblings. [1]
- The recorded-graph and traversal-policy scope inputs a completeness statement is bounded to, and the version the dispatch tables and every payload record. [2]
- The whole operation: admit, probe the schema read-only, build the reader, render, and close the connection. [3]
- The ordered admission gate and its three refusals, run before the database is opened, and the single builder that turns a refusal into a typed result state. [4]
- The dispatch, the error-to-refusal conversion, the distinct-subject check, the counts call and the payload assembly, all through the renderer table. [5]
- The required quantity set, the withheld-row accounting, the review-matrix dependency mismatch count, and the payload table whose five names must agree with the renderer table's. [6]
- The published per-view purposes, the re-exported context resolver, and the shipped resolver behind both it and `_snapshot_of`. [7]
- The continuation that binds a token to one snapshot, its minter, and the both-identities check the seam calls first. [8]
- The completeness scope and the payload that refuses rows-remaining-without-a-continuation. [9]
- The five payload classes the table dispatches to, the five names the seam indexes, and the reader port with its store-side opener. [10]
- The request the seam admits, the result it returns, and the refusal vocabulary both of them use. [11]
- The four admitted ordering inputs the admission gate screens the request against, and the five renderers the dispatch table imports one per view name. [12]
- The case proving a continuation presented against another snapshot is refused with both identities named. [13]
- The case proving a continuation presented against another snapshot is refused with both identities named. [14]
- The two real callers of the seam: the MCP tool registration and the projection writer, both importing `read_knowledge_view` from this module. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The seam reads one database bound to one
repository namespace, refuses a request whose declared namespace differs from the context's, and carries
no identity that ranges beyond that store; the recorded graph and traversal policy it names are local
constants of one walk.

No meaningful cross-repo references found.
