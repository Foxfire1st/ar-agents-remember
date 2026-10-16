# dashboard/src/data/taskDocuments.ts

## Governing Overview

[data overview](overview.md)
frontend source overview governs this client helper.

## Purpose

Transport and dashboard-store-owned resources for full task bodies and pure revision preparation; selection and availability remain with the reader hook.

## Code Commentary

### Logic

`fetchTaskDocument(reference, base, signal)` URL-encodes taskReferenceKey, rejects non-OK status and returns TaskSummary/ETag/UTF-8 bytes. taskBodyKey adds revision. TaskDocumentResources owns separate 64-entry/16-MiB body and preparation LRUs and at most 64 pending reads. Duplicate keys share a promise; capacity aborts oldest pending. Storage uses returned bodyRevision, not the initiating revision.

### Conventions

The store owns resources across navigation and unmounts. `prepare` caches pure data; callbacks and rendered nodes remain with live readers.

### Invariants And Boundaries

No visible-document choice, path authorization or task-state inference occurs here. The serving endpoint owns path confinement. Budgets limit history, not one active document, and confer no transactional workspace-read guarantee.

### Todos

No additional file-local work is asserted.

## Evidence

### Docs References

The resolved Domain Documentation registry has no configured entries. This same-repository adapter
has no external protocol dependency beyond the browser Fetch API already used throughout the
dashboard.

No configured external/domain document defines this internal endpoint adapter.

### Repo-Internal References

The transport fetches the qualified visible body; the store resource owns retention and pending-read deduplication; the hook owns current-summary merge and availability.

- The serving route maps projection readiness and the confined snapshot read to HTTP responses. [3]
- That reader reaches the schema through the shared tolerant parse, so a field a newer build wrote no longer turns a readable body into a 404. [5]

### Cross-Repo References

No meaningful cross-repo boundary exists; the client, endpoint, and task-document reader all live in
`agents-remember`.

Same-repository dashboard-to-serving contract only.
