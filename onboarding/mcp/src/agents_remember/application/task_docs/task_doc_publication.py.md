# mcp/src/agents_remember/application/task_docs/task_doc_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Exact task-document source-CAS and publication under short integration authority, still wrapped by
the pre-L3 governed queue publisher when a sprint queue scope exists.

## Code Commentary

### Logic

`publish_task_doc_set` resolves the governing queue scope and retains the existing
`publish_task_facts_update`/`publish_sprint_update` wrapper. Inside that transitional wrapper,
`TaskDocPublicationTransaction` holds every accepted JSON/Markdown source snapshot, the exact
topology authority check, and one publisher. `publish_task_doc_transaction` takes the short
integration-authority lock, rechecks all accepted bytes, and publishes atomically; dry-run performs
the same checks with `create=False` and no write. A mismatch raises `TaskDocPublicationConflict`
with bounded expected/observed evidence. L3, not this module, removes the queue wrapper and adds
post-write projection invalidation/rebuild.

### Conventions

Callers prepare all selected/affected source snapshots before entering the transaction and must not
re-read a weaker subset inside their own publisher.

### Invariants And Boundaries

- Exact JSON and Markdown bytes for every selected/affected document are one CAS precondition.
- The short integration lock closes task-write versus protected-ref publication races; it is not a
  lifecycle journal or a replacement for the transitional queue lock.
- Queue-governed refusal is still current source behavior until L3 and must not be documented as
  already removed.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines `TaskDocPublicationConflict`; `TaskDocPublication`; `TaskDocPublicationTransaction` as its public seam. | L36-L51; L55-L63; L67-L74 | `mcp/src/agents_remember/application/task_docs/task_doc_publication.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
