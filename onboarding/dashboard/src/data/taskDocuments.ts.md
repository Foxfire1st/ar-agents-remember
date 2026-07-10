# dashboard/src/data/taskDocuments.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/taskDocuments.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T01:14+02:00                           |
| lastVerifiedCommitHash |                                                  `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`|
| lastVerifiedCommitDate |                                                  2026-07-10T22:22:16+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md) — the `data/` folder has no route-local overview, so the
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
`fetch`, typed return data, and no React state. Cache ownership and fallback behavior remain in the
panel that chooses the visible document.

### Invariants And Boundaries

The helper does not decide which document is visible, cache bodies, retry, or validate path
confinement. `DetailPanel` owns selection/cache policy; the serving snapshot layer resolves and
confines the client-supplied path under `coordination_root/tasks` before reading.

### Todos

No file-local follow-up. Long-lived body-cache eviction is a `DetailPanel` concern (reviewer N5),
not transport behavior for this adapter.

## Docs References

The resolved Domain Documentation registry has no configured entries. This same-repository adapter
has no external protocol dependency beyond the browser Fetch API already used throughout the
dashboard.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external/domain document defines this internal endpoint adapter. | — | — |

## Repo-Internal References

The helper is the frontend edge of the F6 split: selection/cache policy calls it, the server exposes
the endpoint, and the snapshot reader performs the confined full-body read. The new helper exists in
the named L13 code worktree but not yet in the official `agents-remember` checkout, so its durable
workspace-relative source link becomes live when closeout integrates L13; this pre-integration source-
link state is recorded rather than silently treated as already landed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper encodes `docPath`, rejects non-OK responses, and returns the decoded task node. | L1-L9 | [taskDocuments.ts](agents-remember/dashboard/src/data/taskDocuments.ts) |
| `DetailPanel` calls the adapter for the visible document and keys cached bodies by path plus revision. | L373-L401; L812-L813 | [DetailPanel.tsx](agents-remember/dashboard/src/panels/DetailPanel.tsx) |
| The serving route maps projection readiness and the confined snapshot read to HTTP responses. | L655-L670 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The snapshot reader resolves under `tasks`, validates the schema, and builds the full node. | L1091-L1130 | [snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists; the client, endpoint, and task-document reader all live in
`agents-remember`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository dashboard-to-serving contract only. | — | — |

## Update History

- 2026-07-10T01:14+02:00 — Created for 260707-HFX2-L13 F6: documented the on-demand task-document
  fetch adapter, its selection/cache boundary, and the server/snapshot confinement seam. Verification
  metadata remains blank until closeout stamps the eventual L13 code commit.
