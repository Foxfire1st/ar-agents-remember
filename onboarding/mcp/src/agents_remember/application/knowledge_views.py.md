# mcp/src/agents_remember/application/knowledge_views.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_views.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l32-ar`, uncommitted; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the seam's own docstring and functions,
the shipped resolver and snapshot model it delegates to, the read-only connection and schema probe it
opens, the reader port it builds, the payload and refusal vocabulary it imports, the renderer module it
dispatches into, and the case that proves a continuation presented against another snapshot is refused.
One detail a reader should carry: the two dispatch tables are the only place this module spells the five
view names, and the seam's own ordering arithmetic is derived from the continuation token's tail rather
than from the renderer's returned offset.

| Finding | Anchor | Source |
| --- | --- | --- |
| The seam's own statement of what it decides, resolves, admits and returns, plus the continuation rule and the seventh-seam claim with its seven named siblings. | `open_read_context` | mcp/src/agents_remember/application/knowledge_views.py:1-18 |
| The recorded-graph and traversal-policy scope inputs a completeness statement is bounded to, and the version the dispatch tables and every payload record. | `RECORDED_GRAPH`; `TRAVERSAL_POLICY`; `VIEW_RENDERER_VERSION`; `__all__` | mcp/src/agents_remember/application/knowledge_views.py:65-75; mcp/src/agents_remember/application/knowledge_views.py:83-83; mcp/src/agents_remember/application/knowledge_views.py:82-82 |
| The whole operation: admit, probe the schema read-only, build the reader, render, and close the connection. | `read_knowledge_view`; `open_read_only_database`; `inspect_schema` | mcp/src/agents_remember/application/knowledge_views.py:78-104; mcp/src/agents_remember/memory/knowledge/connection.py:52-65; mcp/src/agents_remember/memory/knowledge/connection.py:111-129 |
| The ordered admission gate and its three refusals, run before the database is opened, and the single builder that turns a refusal into a typed result state. | `_admit`; `_refused`; `ViewRefusal` | mcp/src/agents_remember/application/knowledge_views.py:107-150; mcp/src/agents_remember/models/knowledge/view.py:171-184; mcp/src/agents_remember/application/knowledge_diff.py:790-790; mcp/src/agents_remember/application/knowledge_evidence.py:244-244; mcp/src/agents_remember/application/knowledge_facets.py:244-244; mcp/src/agents_remember/application/knowledge_family_integrity.py:193-193; mcp/src/agents_remember/application/knowledge_diff.py:790-806 |
| The dispatch, the error-to-refusal conversion, the distinct-subject check, the counts call and the payload assembly, all through the renderer table. | `_render`; `_RENDERERS` | mcp/src/agents_remember/application/knowledge_views.py:153-201; mcp/src/agents_remember/application/knowledge_views.py:239-245 |
| The required quantity set, the withheld-row accounting, the review-matrix dependency mismatch count, and the payload table whose five names must agree with the renderer table's. | `_counts`; `_dependency_mismatches`; `_PAYLOADS`; `ViewCounts`; `view_counts` | mcp/src/agents_remember/application/knowledge_views.py:204-253; mcp/src/agents_remember/models/knowledge/view.py:245-262; mcp/src/agents_remember/models/knowledge/view.py:273-331; mcp/src/agents_remember/application/knowledge_views.py:277-277; mcp/src/agents_remember/application/knowledge_views.py:277-283 |
| The published per-view purposes, the re-exported context resolver, and the shipped resolver behind both it and `_snapshot_of`. | `view_purposes`; `VIEW_PURPOSES`; `open_view_context`; `open_read_context`; `snapshot_of_context` | mcp/src/agents_remember/application/knowledge_views.py:256-278; mcp/src/agents_remember/models/knowledge/view.py:115-142; mcp/src/agents_remember/application/knowledge_read.py:103-136; mcp/src/agents_remember/models/knowledge/read.py:540-552; mcp/src/agents_remember/application/knowledge_views.py:286-286; mcp/src/agents_remember/application/knowledge_views.py:292-292; mcp/src/agents_remember/application/knowledge_views.py:292-308; mcp/src/agents_remember/application/knowledge_views.py:286-289 |
| The continuation that binds a token to one snapshot, its minter, and the both-identities check the seam calls first. | `ViewContinuation`; `continuation_for`; `require_continuation_snapshot` | mcp/src/agents_remember/models/knowledge/view.py:366-389; mcp/src/agents_remember/models/knowledge/view.py:392-414; mcp/src/agents_remember/application/knowledge_views.py:68-68; mcp/src/agents_remember/application/knowledge_views.py:145-145; mcp/src/agents_remember/models/knowledge/view.py:552-552; mcp/tests/test_knowledge_views_and_projection.py:64-64; mcp/src/agents_remember/models/knowledge/view.py:552-574 |
| The completeness scope and the payload that refuses rows-remaining-without-a-continuation. | `ViewScope`; `ViewPayload` | mcp/src/agents_remember/models/knowledge/view.py:353-365; mcp/src/agents_remember/models/knowledge/view.py:934-978; mcp/src/agents_remember/application/knowledge_projection.py:54-54; mcp/src/agents_remember/application/knowledge_projection.py:90-90; mcp/src/agents_remember/application/knowledge_projection.py:105-105; mcp/src/agents_remember/application/knowledge_projection.py:187-187 |
| The five payload classes the table dispatches to, the five names the seam indexes, and the reader port with its store-side opener. | `SourceContextView`; `CurationQueueView`; `VIEW_PAYLOADS`; `VIEW_NAMES`; `KnowledgeViewReader`; `open_view_reader` | mcp/src/agents_remember/models/knowledge/view.py:981-985; mcp/src/agents_remember/models/knowledge/view.py:1009-1013; mcp/src/agents_remember/models/knowledge/view.py:1027-1033; mcp/src/agents_remember/models/knowledge/view.py:124-124; mcp/src/agents_remember/models/knowledge/view.py:1068-1114; mcp/src/agents_remember/memory/knowledge/view_source.py:405-428; mcp/src/agents_remember/memory/knowledge/view_source.py:431-455 |
| The request the seam admits, the result it returns, and the refusal vocabulary both of them use. | `ViewRequest`; `ViewResult`; `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/view.py:1117-1148; mcp/src/agents_remember/models/knowledge/view.py:1151-1166; mcp/src/agents_remember/models/knowledge/result.py:235-245 |
| The four admitted ordering inputs the admission gate screens the request against, and the five renderers the dispatch table imports one per view name. | `ORDERING_INPUTS`; `render_source_context`; `render_curation_queue` | mcp/src/agents_remember/models/knowledge/classification.py:86-86; mcp/src/agents_remember/application/knowledge_view_render.py:949-984; mcp/src/agents_remember/application/knowledge_view_render.py:1129-1158; mcp/src/agents_remember/application/knowledge_view_render.py:987-1022; mcp/src/agents_remember/application/knowledge_view_render.py:1064-1120; mcp/src/agents_remember/application/knowledge_view_render.py:1028-1061 |
| The case proving a continuation presented against another snapshot is refused with both identities named. | "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" | mcp/tests/test_knowledge_views_and_projection.py:318-318 |
| The case proving a continuation presented against another snapshot is refused with both identities named. | "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" | mcp/tests/test_knowledge_views_and_projection.py:318-318 |
| The two real callers of the seam: the MCP tool registration and the projection writer, both importing `read_knowledge_view` from this module. | `read_knowledge_view` | mcp/src/agents_remember/mcp/tools/knowledge.py:34-34; mcp/src/agents_remember/mcp/tools/knowledge.py:158-158; mcp/src/agents_remember/application/knowledge_projection.py:40-40; mcp/src/agents_remember/application/knowledge_projection.py:229-229 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The seam reads one database bound to one
repository namespace, refuses a request whose declared namespace differs from the context's, and carries
no identity that ranges beyond that store; the recorded graph and traversal policy it names are local
constants of one walk.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" repointed to mcp/tests/test_knowledge_views_and_projection.py:318-318. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" repointed to mcp/tests/test_knowledge_views_and_projection.py:318-318. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator, **memory-side sync conflict resolved as a UNION; no side dropped.** The memory source branch advanced to `92f444b04` (260915-KS-L45) while this leaf's curation was in flight, so the sync's re-apply conflicted in this file. Both sides were kept because both are true: 260915-KS-L45's landed additions (the Intent-review entry path, the two published half-names `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, the `missing_dataset_half` pair preflight, the receipt-derived `review_namespace`, and the enumerating reads) and this leaf's 260915-KS-L43 edits (the allocated-identity/derived-citation split, the retry key and its journal, the explicit anchor reuse, and the recovery's journaled decisions with the bounded cycling refusal). Where the two sides carried the same row in different line numbers, the row was re-measured against the moved line rather than picked: L45 curated against `fb719f89` and this leaf's source moves every citation below `:306` of `knowledge_curator_ingest.py` and renumbers `cli/knowledge_ingest.py` entirely, so the surviving ranges are the post-merge measurement for both. One **contradiction** is recorded rather than silently resolved: the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` frontmatter pair is L45's (recorded against the moved line, the newest verification on record), while the `reviewedWorkingCandidate` row is this leaf's reading — two different claims, kept beside each other instead of one overwriting the other. No verification stamp was advanced by this leaf.
- 2026-09-20T12:00:25+00:00: Generated citation repair: "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" repointed to mcp/tests/test_knowledge_views_and_projection.py:317-317. No content impact: mechanical anchor-range projection bound to citation source snapshot 23094be373d669ad77475ab6ebb610401913ce4b65c82d3b4cc642eb6bb44e43; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" repointed to mcp/tests/test_knowledge_views_and_projection.py:317-317. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T05:40+02:00 — 260915-KS-L41 curator (uncommitted change set on `ar/260915-ks-l41-ar`, code base `756c47b3` before the L39 sync and `f79f4db745ad00b908d6ce4871d0b4ab2320207c` after it): **body update for the same seed frontier this leaf completes, with the reader-port repairs this card's own rows needed.** `_admit` screens the caller's ordering input against `ORDERING_INPUTS` before any read and `_render` converts the renderer's raised refusal into a typed `ViewRefusal`, and this leaf changed what those calls read: `application/knowledge_view_render.py` now computes one path-seed frontier per reader (`_seed_revisions`, `_seed_memo`, `_seeded_realizations`, `_seed_selects`, plus `_seeded_family_revisions` and `_selected_invariant_revisions`) and applies it in `source_context` as well, and `_family_members` reads membership through `reader.family_member_rows()` from the dedicated `family_member` table instead of asking the envelope reader for the kind by name. The five-renderers row's own-file cells were re-read against the merged candidate and now cite each renderer's declaration extent (`949-984`, `987-1022`, `1028-1061`, `1064-1120`, `1129-1158`). The payload-classes row had been over-collapsed in this pass: `VIEW_NAMES` lives at `124`, not inside the payload-class span, so the row's cells are back in the row's own anchor order — `953-957`, `981-985`, `999-1005`, `124-124` — which is the order the anchors are written in and the only form that carries every one of them. No claim was re-worded to fit a stale pointer and no anchor or range was dropped. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded — the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-20T03:34:37+00:00: Generated citation repair: "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" repointed to mcp/tests/test_knowledge_views_and_projection.py:316-316. No content impact: mechanical anchor-range projection bound to citation source snapshot c5faa16605389532116ca8537ba85846231e118f9e26a30bea3b89dd82307c30; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" repointed to mcp/tests/test_knowledge_views_and_projection.py:278-278. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:24+02:00 — 260915-KS-L32 curator, post-sync citation pass (uncommitted change set on `ar/260915-ks-l32-ar`, code base `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`, memory base `4ffb8d8d3ff372847784fe8f7d2a13e57d9509a5`): **cleared the three enforced `citation_anchor_absent_from_range` rows this card carried, by RANGE REPAIR — every range repointed to its anchor's own declaration extent in the merged code tree, and no claim re-worded, no anchor dropped and no row deleted.** The mechanical `citation_fix` path was unavailable workspace-wide (the managed citation namespace was at its 4-namespace ceiling with every occupant live), so each substitution was read in the code worktree before it was written and none was inferred by arithmetic. (a) The payload/reader row cited ten ranges, **none** of which held any of its six anchors: `VIEW_PAYLOADS` reads `994-1000` → `999-1012` (the tuple's declaration, opened at `999`); `VIEW_NAMES` reads `119-119` → `124-124` (a comment mentioning the name is not the name — `124` is the binding `VIEW_NAMES: tuple[ViewName, ...] = get_args(ViewName)`); the five payload classes' old `819-827`, `863-881`, `935-939`, `981-987` and `963-967` cells did not hold `SourceContextView` or `CurationQueueView` at all and are replaced by the two classes' own extents `953-959` and `981-989`; `KnowledgeViewReader` reads `114-114` → `1041-1077` (the `Protocol` body, opened at `1041`); and `open_view_reader` reads `memory/knowledge/view_source.py:383-407` → `391-416` (the shipped opener, declared at `391`). The row's words still describe exactly what those constructs are — the five payload classes the dispatch table maps, the five names the seam indexes, and the reader port with its store-side opener — so the wording was retained. (b) The request/result row's nine cells were six ranges that hold nothing the row names plus three leftovers: `ViewRequest` reads `884-918` → `1078-1111` and `ViewResult` reads `1079-1094` → `1112-1128`, each now the class's own declaration extent; the `1044-1060` and `1063-1078` cells, which sat inside the reader port and the request rather than on the result, are gone with the stale projections they were; `KnowledgeRefusal` keeps `models/knowledge/result.py:235-245`, re-read and unchanged. (c) The renderer-dispatch row is re-cited to the renderers the dispatch table actually imports, one per view name: `render_source_context` reads `716-751` → `835-872`, and the old `805-822`, `876-876` and `876-905` cells did not hold `render_source_context` OR `render_curation_queue` on either side, so they are replaced by the two named renderers' own extents plus their two siblings' — `835-872` (`render_source_context`), `873-910` (`render_invariant`), `914-949` (`render_family`), `950-1008` (`render_review_matrix`) and `1015-1046` (`render_curation_queue`). `ORDERING_INPUTS` keeps `classification.py:86-86`, re-read and unchanged, and the two `knowledge_views.py` cells `35-35` and `274-274` are left exactly as written because both really do hold `render_curation_queue` — in the import block and in the `_RENDERERS` registry. **Stamp accounting:** the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained unchanged, and the superseded `ar/260915-ks-l20` candidate row (which named a base the merged candidate no longer stands on) is replaced by the single `reviewedWorkingCandidate` row naming `ar/260915-ks-l32-ar` at base `7dcec036`; no commit hash was invented and no stamp was advanced.
- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 3 enforced citation rows this card carried (citation_anchor_absent_from_range) — `VIEW_PAYLOADS` was repointed to mcp/src/agents_remember/models/knowledge/view.py:994-1000 and `VIEW_NAMES` to mcp/src/agents_remember/models/knowledge/view.py:119-119 in the payload/reader row, and `render_source_context` to mcp/src/agents_remember/application/knowledge_view_render.py:716-751 in the renderer-dispatch row; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" repointed to mcp/tests/test_knowledge_views_and_projection.py:277-277. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 2 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `knowledge_views.py.md:217` (`SourceContextView`, `CurationQueueView`, `VIEW_PAYLOADS`, `VIEW_NAMES`, `KnowledgeViewReader`, `open_view_reader`); `knowledge_views.py.md:219` (`ORDERING_INPUTS`, `render_source_context`, `render_curation_queue`).
- 2026-09-18T17:30:57+00:00: Generated citation repair: "def test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named(" repointed to mcp/tests/test_knowledge_views_and_projection.py:275-275. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the five-view application seam. It records the seam's four moves (resolve the snapshot through the shipped `open_read_context`, admit the request, build the reader port, return the typed payload), the continuation check performed before any row is read with both snapshot identities named and no partial answer, the ordered admission gate and its three refusals, the honest page arithmetic tied to the renderer's own selection size, and the two dispatch tables keyed by the same five view names. It also records the deliberate absences: no authority, no durable state, no selection or ordering logic, and no fallback snapshot for a continuation to be re-resolved against. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
