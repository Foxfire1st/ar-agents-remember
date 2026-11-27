# mcp/src/agents_remember/application/knowledge_views.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The application seam for three knowledge views over a memory tree's derived index. It admits, opens, dispatches and returns a typed answer; it decides no semantic authority and keeps no durable state. The seam serves `source_context`, `invariant` and `family`.

## Code Commentary

### Logic

Ordering, namespace and continuation bindings are checked before rows are read. A different snapshot is refused with both digests named; a malformed cursor is refused instead of becoming position zero. The seam admits the cursor once and passes the offset to the three renderers in `knowledge_view_rows.py`. Their returned next position governs continuation and remaining count.

### Invariants And Boundaries

The shipped resolver supplies the snapshot. The seam closes its reader in a `finally`. The last page has no remaining rows and no continuation. No default ordering, second token parse in a renderer or partial answer on a binding refusal is introduced. Selection and classification stay with their named renderer owners.

### Todos

None recorded.

### Logic

**`read_knowledge_view` supplies typed slices to the paged reader.**
It admits the request through `_admit` and returns `_refused(...)` immediately when that yields a
refusal; opens the database read-only through `open_read_only_database` and reads its schema identity
through `inspect_schema`, closing the probe in a `finally` before the real reader exists; builds the
reader port through `open_view_reader`, which is handed the request's `repository_id`, that identity and
the caller's optional `resolve_anchor`; and then renders inside a `try/finally` that closes the
connection. The probe is released before the reader is opened, so the seam never holds two handles on one
file, and the connection lifetime belongs to this function alone.

**The snapshot comes from the shipped resolver, so a caller cannot declare one.** `_snapshot_of`
delegates to `snapshot_of_context` from `models/knowledge/read.py` rather than assembling a snapshot
here, and the same snapshot is what the payload, the completeness scope and the continuation all name.
The docstring states the consequence: "The snapshot a view declares comes from ``open_read_context``,
which reads the identity the dataset at that path actually holds," and the three comparisons the other
seams make — bound namespace, declared generation, declared logical digest — "are made here for the same
reason."

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
of those refusals into `ViewResult(state="refused", repository_id=..., refusal=...)`. The database probe and reader open run outside a refusal conversion.

**`_render` dispatches one view, converts a raised ordering error back into a refusal, and assembles the
typed payload around the rows it got.**
An `UnadmittedOrderingInput` raised below the table is caught and returned as a
`ViewRefusal(code="unadmitted_ordering_input")`, so the named ordering error leaves as a typed result. The row set is then checked with `require_distinct_row_subjects`
(`code="ambiguous_row_identity"`), and a duplicate subject refuses the whole view rather than letting the
seam choose which of two rows is authoritative. Counts come from `_counts`, and `ViewCompleteness` is
built with `complete_within_declared_scope=continuation is None` — a completeness statement that is a
fact about this page's paging rather than a claim about the dataset.

**`_counts` reports the measured size of the walk.** It reads the registered realization and
family totals, counts the returned rows and subtracts the next position from the selection total for
`rows_remaining`. `facets_omitted` is `None` for `invariant` and `source_context`, and zero for
`family`. The result uses the model layer's `view_counts` constructor.

**The renderer and payload tables use the same three view names.** `_RENDERERS` dispatches
`source_context`, `invariant` and `family`. `_PAYLOADS` pairs those keys with their typed models.

**`VIEW_RENDERER_VERSION` is a recorded value, not a package version read at display time.**
`"knowledge-view-renderer/1"` travels as the `extractors` member of `ViewScope` and again as the
payload's `renderer_version`, which is what the source comment means by "two payloads produced by
different renderer versions are distinguishable from the payloads themselves." `RECORDED_GRAPH` and
`TRAVERSAL_POLICY` are the other two named scope inputs — "The recorded graph the selection walks, and
the traversal policy it walks it under" — and the scope also carries
`snapshot_logical_digest=snapshot.logical_digest`, so a completeness statement is bounded to the three
inputs it was made about: one snapshot, one graph, one policy, plus the extractor version.

### Conventions

The module uses the model layer's requests, refusals, counts and three payload classes. The
`open_view_reader` function supplies the reader and connection. `ORDERING_INPUTS` supplies the
admitted ordering vocabulary. The module exports `VIEW_RENDERER_VERSION` and
`read_knowledge_view`.

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
  `_PAYLOADS` are two declarations of one three-name vocabulary, so a view present in one and absent from
  the other fails at the lookup rather than yielding a payload of the wrong type.
- **Admission and ordering refusals are typed.** `_refused` wraps a `ViewRefusal` in a
  `ViewResult`. The renderer's `UnadmittedOrderingInput` is converted to that same result.
- **The connection the reader is opened with is closed by this seam.** `open_view_reader` returns the
  reader and the handle together, and `read_knowledge_view` closes the handle in a `finally`, so the
  reader's lifetime cannot outlive the call.
- **Version and scope values are recorded, not computed.** `VIEW_RENDERER_VERSION` is a literal that
  travels on every payload, and `RECORDED_GRAPH` and `TRAVERSAL_POLICY` are named constants, so a payload
  is distinguishable from another one produced by a different renderer or a different walk.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The current seam, derived-index reader and typed cursor models establish the boundaries below. The mounted tool projects the paged read. The paged reader uses this seam for the ordered view slices.


- The seam admits the request, opens a read-only reader, renders its typed result and closes the handle. [1]

- The recorded-graph and traversal-policy scope inputs a completeness statement is bounded to, and the version the dispatch tables and every payload record. [2]

- The whole operation: admit, probe the schema read-only, build the reader, render, and close the connection. [3]


- The derived-index seam checks ordering, namespace and continuation binding before reading rows and returns a typed refusal. [4]


- The dispatch, the error-to-refusal conversion, the distinct-subject check, the counts call and the payload assembly, all through the renderer table. [5]

- The seam serves exactly three views [6]

- The context owns its snapshot and _snapshot_of carries that identity into the cursor binding. [7]

- The continuation that binds a token to one snapshot, its minter, and the both-identities check the seam calls first. [8]
- The completeness scope and the payload that refuses rows-remaining-without-a-continuation. [9]




- The request the seam admits, the result it returns, and the refusal vocabulary both of them use. [11]

- The row-rendering module supplies the source context, invariant and family renderers. [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The seam reads one database bound to one
repository namespace, refuses a request whose declared namespace differs from the context's, and carries
no identity that ranges beyond that store; the recorded graph and traversal policy it names are local
constants of one walk.

No meaningful cross-repo references found.

### Repo-Internal References

- The ordered admission gate and its three refusals, run before the database is opened, and the single builder that turns a refusal into a typed result state. [16]

- The three payload classes the table dispatches to — source context, invariant and family — the three view names the seam indexes, and the reader port with its store-side opener. [17]


- The four admitted ordering inputs the admission gate screens the request against, and the three renderers the dispatch table imports one per view name. [18]



- The mounted knowledge read projects the converted tree result. Its paged reader uses read_knowledge_view internally to collect the renderer’s ordered slices. [15]


- The current renderer dispatch assembles the typed payload through the read-only StoreViewReader and its opener. [10]
