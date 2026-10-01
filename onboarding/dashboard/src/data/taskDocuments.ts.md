# dashboard/src/data/taskDocuments.ts

## Governing Overview

[data overview](overview.md)
frontend source overview governs this client helper.

## Purpose

Small fetch adapter for the dashboard's on-demand full task-document body endpoint. It keeps HTTP
URL construction and response-status handling out of `DetailPanel`, while sharing the projection's
`TaskDocNode` wire type.

## Code Commentary

### Logic

`fetchTaskDocument(docPath, base="")` URL-encodes the projected document path into
`GET {base}/api/task-document?path=...`. A non-2xx response raises an error containing the status;
a successful response is decoded as `TaskDocNode`. The optional base supports hosted/test contexts
without changing the production same-origin default.

### Conventions

This module follows the other `dashboard/src/data` adapters: one narrow transport operation, browser
`fetch`, typed return data, and no React state. `useTaskDocumentBody.ts` owns cache and availability
state; `DetailPanel` chooses the visible document and consumes that state.

### Invariants And Boundaries

The helper does not decide which document is visible, cache bodies, retry, or validate path
confinement. `DetailPanel` owns selection, `useTaskDocumentBody` owns hydration/cache policy, and the
serving snapshot layer resolves and confines the client-supplied path under `coordination_root/tasks`
before reading.

### Todos

No file-local follow-up. Long-lived body-cache eviction belongs to `useTaskDocumentBody`, not this
transport adapter.

## Evidence

### Docs References

The resolved Domain Documentation registry has no configured entries. This same-repository adapter
has no external protocol dependency beyond the browser Fetch API already used throughout the
dashboard.

No configured external/domain document defines this internal endpoint adapter.

### Repo-Internal References

The helper is the frontend edge of the F6 split: selection/cache policy calls it, the server exposes
the endpoint, and the snapshot reader performs the confined full-body read. The new helper exists in
the named L13 code worktree but not yet in the official `agents-remember` checkout, so its durable
workspace-relative source link becomes live when closeout integrates L13; this pre-integration source-
link state is recorded rather than silently treated as already landed.

- The helper encodes `docPath`, rejects non-OK responses, and returns the decoded task node. [1]
- `useTaskDocumentBody` calls the adapter for the visible document and keys cached bodies by path plus revision. [2]
- The serving route maps projection readiness and the confined snapshot read to HTTP responses. [3]
- The snapshot reader resolves under `tasks`, validates the schema, and builds the full node. [4]
- That reader reaches the schema through the shared tolerant parse, so a field a newer build wrote no longer turns a readable body into a 404. [5]

### Cross-Repo References

No meaningful cross-repo boundary exists; the client, endpoint, and task-document reader all live in
`agents-remember`.

Same-repository dashboard-to-serving contract only.
