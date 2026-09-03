# mcp/src/agents_remember/memory_quality/incremental_scope/errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `993953760ef65c4670a40c63a6d6ef0fbcddbe3b`|
| lastVerifiedCommitDate | 2026-09-03T02:13:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Owns the typed, fail-closed result vocabulary for an unproved incremental memory scope: the
`ScopeFailure` evidence record, the base `ScopeUnprovenError`, and — since CCR-R07@v3 — the
`GateFiveClosureRefusedError` that rejects one exact Gate-5 affected closure.

## Code Commentary

### Logic

`ScopeFailure` (`errors.py:10-19`) is a frozen dataclass carrying code, detail, and optional
authority evidence (checker, node, edge class, snapshot, candidate, owner).
`ScopeUnprovenError` (`errors.py:22-47`) subclasses `AgentsRememberError`, sets status
`scope-unproven`, formats `status:code: detail`, and emits a structured `response_fields`
payload with non-None evidence keys spelling `edgeClass`, `candidateDigest`, and `owner`.
`GateFiveClosureRefusedError` (`errors.py:50-53`) narrows the status to
`gate-5-closure-refused` for R07 refusals.

### Conventions

Every refusal in the package raises one of these typed errors instead of returning an
unstructured failure, so callers can discriminate proof failures from environment errors.

### Invariants And Boundaries

- A failure record is immutable and always carries at least code and detail.
- `GateFiveClosureRefusedError` reports `gate-5-closure-refused`; no fallback or safe-full
  result is ever represented as this refusal.
- The structured response keeps the exact evidence keys the checker supplied.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for the typed Gate-5 refusal.

| Finding | Anchor | Source |
| --- | --- | --- |
| CCR-R07@v3 failure behavior: incomplete ownership, stale input, unknown consumer, missing result, or changed certificate produces a typed Gate-5 closure refusal. | "Failure And Recovery" | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R07-v3-incremental-affected-closure-validation.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| All R07 modules raise `GateFiveClosureRefusedError` for typed closure refusals. | `_refuse` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:375-385; mcp/src/agents_remember/memory_quality/incremental_scope/affected_execution.py:493-503; mcp/src/agents_remember/memory_quality/incremental_scope/subresult_store.py:146-154 |
| The base error carries the canonical agents-remember failure status machinery. | `AgentsRememberError` | mcp/src/agents_remember/errors.py |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external boundary is exercised by the error vocabulary. | — | — |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card for the typed scope failure vocabulary, including the new `GateFiveClosureRefusedError`; no prior sidecar existed.
