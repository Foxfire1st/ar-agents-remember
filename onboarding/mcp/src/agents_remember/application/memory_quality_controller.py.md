# mcp/src/agents_remember/application/memory_quality_controller.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_quality_controller.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Owns the single typed sync/start/poll API for memory quality. It resolves canonical scope once,
forms complete run identity, executes the check, publishes leaf curator checklists when required,
and translates registry outcomes into stable public results.

## Code Commentary

### Logic

`run_memory_quality_request` executes an explicit sync request. `start_memory_quality_request`
resolves the same execution contract and admits it to the bounded registry; equivalent live work
returns its existing run, while full live capacity returns `capacity-reached` plus retry guidance.
`poll_memory_quality_request` accepts only configured `repo_id` and `run_id`, so a wrong repository
observes the same `run-not-found` result as an absent or evicted run.

`MemoryQualityExecution.identity` freezes repository, resolved scope, normalized checks,
`detail_limit`, and the report-publication decision. A full leaf check composes missing-onboarding,
route-index preview, drift rows, and commit-owned versus curator-owned findings into the one
enclosure-local checklist. Sync and async paths therefore share one execution implementation.

### Invariants And Boundaries

- Public callers choose exactly one request mode; no flat legacy overload or inferred wait mode is
  accepted.
- Every result-affecting input is part of `QualityRunIdentity`; distinct work cannot alias.
- Capacity is a typed refusal with guidance, not an exception or an unbounded extra thread.
- Polling never discloses whether another configured repository owns the supplied run id.
- Curator-report publication is derived from resolved leaf scope and a full check, never from a
  caller-provided path.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the controller contract is repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The execution identity contains normalized checks, detail limit, publication semantics, and frozen scope. | `MemoryQualityExecution` | mcp/src/agents_remember/application/memory_quality_controller.py:48-64 |
| Sync, start, and poll are separate typed request entry points with capacity and nondisclosing poll translations. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality_controller.py:67-144 |
| Full leaf checks compose and atomically publish the curator checklist. | `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality_controller.py:167-251 |

## Cross-Repo References

No meaningful cross-repository implementation reference applies.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: created for the canonical typed memory-quality controller and complete run identity. Verification remains blank until architect-owned closeout stamps the code commit.
