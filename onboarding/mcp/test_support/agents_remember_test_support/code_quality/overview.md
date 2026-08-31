# Python Quality Verification Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/test_support/agents_remember_test_support/code_quality` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-30T21:25+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

The Dagger-executed Python quality producer. It owns broad static checks, product-only behavioral
scoring, source-derived test selection, persistent retry proof, causal prerequisite reporting, and
machine-readable quality artifacts. Being shipped in the source distribution does not make this
operational product behavior; its owner and consumers are repository verification.

## Hot Path Summary

`check.py` executes and interprets the rails; `quality_plan.py` owns their typed configuration,
progress state, and deterministic command plan. `scope.py` proves complete
product/verification package authority.
`dependency_ownership.py` consumes source-derived imports, recursive pytest plugins, and literal
artifact readers. `retry_proof.py` owns Dagger-cache identity/lifecycle, `retry_coverage.py` owns
retained/fresh Coverage.py composition, and `quality_subprocess_environment.py` owns the child-rail
environment boundary. `causal_preflight.py` binds failed contracts to exact dependent nodes;
`causal_continuation.py` rejects missing or contradictory reports into full-population safe mode.

## Operating Model

Targeted selection and retry share one immutable source fact graph. Lifecycle declarations are
validated against observed consumers; they never make themselves complete. A missing, ambiguous,
dynamic, stale, or contradictory graph selects the full current test population with a stable
fresh-rerun reason. Retry proof persists only in the locked `ar-quality-retry-v3` Dagger cache and
binds the exact lane population, environment digest, tools, selection, candidate snapshot, and
coverage artifacts. Delta coverage keeps retained and fresh databases separate until a passing
pytest result is explicitly merged and atomically republished for all downstream scorers. An
all-contexts-affected delta carries an explicit known-empty retained state; an unexpected missing
retained database still fails closed.

Non-Python product inputs that cannot participate in the import graph use narrow repository-owned
consumer declarations only when independently observed literal reads match exactly. This lets the
Codex starter configuration select its two real contract consumers without treating every unrelated
test as affected; any declaration/source mismatch widens safely and names the reason.

## Local Invariants And Traps

- Unknown ownership cannot produce `complete=True`.
- Cache rejection names the exact reason and starts fresh; it is not a silent route fallback.
- Only a fresh full pytest pass followed by a later quality failure may publish reusable proof.
- Candidate-test subprocesses inherit semantic admission/invocation settings but never the outer
  wrapper's retry-cache or progress-report controls.
- Retained proof is never handed to pytest-cov/xdist as an append target.
- Known-empty retained proof is explicit and cannot mask a missing expected artifact.
- Causal suppression is exact-node and non-accepting; unproven and same-file independent nodes run.
- Static rails cover product and verification packages; behavioral scores cover product authority
  only.
- Plan construction and execution remain separate owners behind the stable `check` facade.
- Projection generation accepts the canonical Python 3.13 Pydantic shape for named literal
  vocabularies: a local enum definition plus local `$ref`. Every other referenced vocabulary shape
  still fails closed.
- A non-Python consumer declaration never self-proves and cannot silently narrow targeted scope.

## File-Level Onboarding Map

All Python files in this route have one adjacent sidecar. The generated index is the exhaustive
source/sidecar map after refresh.

## Docs And Boundary References

The canonical overview is `docs/design/python-evidence-system.md`; retry and direct-route details
are in `docs/design/python-test-evidence.md` and the PDLS evidence reports.

## Update History

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 added source-verified exact consumer ownership for `.codex/config.toml`; the candidate resolves completely without global invalidation or a silent narrow fallback. Verification remains closeout-owned.

- 2026-08-29T19:04+02:00 — Reconciled the projection generator with Python 3.13 named-literal
  schema definitions after the lifecycle-owned fast gate exposed the former inline-only assumption.
  Verification remains closeout-owned.

- 2026-08-28T04:48+02:00 — Split typed plan construction from quality execution and added the
  causal-report safe-continuation owner; unavailable evidence now selects the full population.
- 2026-08-27T19:13+02:00 — Added the explicit all-contexts-affected retry state while retaining
  missing-artifact refusal.
- 2026-08-27T18:33+02:00 — Added the explicit retained/fresh coverage-composition owner and
  outer-wrapper/child-rail environment boundary after the real xdist retry run exposed both
  ownership collisions.
- 2026-08-27T11:08+02:00 — Rehomed the quality producer under verification authority; documented
  explicit package scope, source-derived ownership, persistent Dagger retry, and exact causal
  behavior. Verification remains closeout-owned.
