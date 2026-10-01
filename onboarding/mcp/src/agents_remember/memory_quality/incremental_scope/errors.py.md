# mcp/src/agents_remember/memory_quality/incremental_scope/errors.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for the typed Gate-5 refusal.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Failure And Recovery") requires a typed Gate-5 closure refusal for incomplete ownership,
stale input, unknown consumer, missing result, or changed certificate.


### Repo-Internal References

- The R07 planner raises typed closure refusals. [1]
- The R07 executor raises typed closure refusals. [2]
- The R07 subresult store raises typed closure refusals. [3]
- The base error carries the canonical agents-remember failure status machinery. [4]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No external boundary is exercised by the error vocabulary.
