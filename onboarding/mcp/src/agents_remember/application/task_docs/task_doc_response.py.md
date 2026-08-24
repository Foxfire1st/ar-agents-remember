# mcp/src/agents_remember/application/task_docs/task_doc_response.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_response.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Own shared task-document result and dry-run rendering.

## Code Commentary

### Logic

The helpers render applied task mutations, preview JSON/Markdown diffs, progress counts, graph titles, and optional master-sync effects from the same candidate TaskDocument used by publication.

### Invariants And Boundaries

- Preview and apply expose the same candidate task truth.
- Rendering does not consult queue rows or operation state.
- Graph and master-sync details are response evidence, not publication authority.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Source Range | Source Path |
| --- | --- | --- |
| Applied results and previews share one response shape. | L22-L75 | [source](mcp/src/agents_remember/application/task_docs/task_doc_response.py) |
| Graph-title and master-sync helpers render bounded supporting evidence. | L76-L137 | [source](mcp/src/agents_remember/application/task_docs/task_doc_response.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
