# mcp/src/agents_remember/application/knowledge_views.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The application seam for five knowledge views over a memory tree's derived index. It admits, opens, dispatches and returns a typed answer; it decides no semantic authority and keeps no durable state.

## Code Commentary

### Logic

Ordering, namespace and continuation bindings are checked before rows are read. A different snapshot is refused with both digests named; a malformed cursor is refused instead of becoming position zero. The seam admits the cursor once and passes the offset to the five renderers in `knowledge_view_rows.py`. Their returned next position governs continuation and remaining count.

### Invariants And Boundaries

The shipped resolver supplies the snapshot. The seam closes its reader in a `finally`. The last page has no remaining rows and no continuation. No default ordering, second token parse in a renderer or partial answer on a binding refusal is introduced. Selection and classification stay with their named renderer owners.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The current seam, derived-index reader and typed cursor models establish the boundaries below. The public converted-tree tool is a separate entry path; the former projection writer is retired.


- The seam admits the request, opens a read-only reader, renders its typed result and closes the handle. [1]

- The recorded-graph and traversal-policy scope inputs a completeness statement is bounded to, and the version the dispatch tables and every payload record. [2]
- The whole operation: admit, probe the schema read-only, build the reader, render, and close the connection. [3]

- The derived-index seam checks ordering, namespace and continuation binding before reading rows and returns a typed refusal. [4]

- The dispatch, the error-to-refusal conversion, the distinct-subject check, the counts call and the payload assembly, all through the renderer table. [5]
- The required quantity set, the withheld-row accounting, the review-matrix dependency mismatch count, and the payload table whose five names must agree with the renderer table's. [6]

- The context owns its snapshot and _snapshot_of carries that identity into the cursor binding. [7]

- The continuation that binds a token to one snapshot, its minter, and the both-identities check the seam calls first. [8]
- The completeness scope and the payload that refuses rows-remaining-without-a-continuation. [9]

- The current renderer dispatch assembles the typed payload through the read-only StoreViewReader and its opener. [10]

- The request the seam admits, the result it returns, and the refusal vocabulary both of them use. [11]

- The admitted ordering inputs and the current source-context and curation-queue renderers. [12]


- The former projection writer and MCP seam call were retired. The current public knowledge tool reads a converted tree through read_tree_page, rather than calling read_knowledge_view. [15]


### Cross-Repo References

No cross-repository behavior is implemented in this file. The seam reads one database bound to one
repository namespace, refuses a request whose declared namespace differs from the context's, and carries
no identity that ranges beyond that store; the recorded graph and traversal policy it names are local
constants of one walk.

No meaningful cross-repo references found.
