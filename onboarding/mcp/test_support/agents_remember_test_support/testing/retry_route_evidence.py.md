# mcp/test_support/agents_remember_test_support/testing/retry_route_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/retry_route_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Provides controlled candidate mutations and cache inspection for the real Dagger retry matrix.

## Code Commentary

### Logic

The CLI creates one real post-pytest diff-coverage seed failure, clones its integrity-checked proof
inside invocation-unique evidence namespaces, and mutates one product, test, support, fixture,
plugin, unknown, lane, or context input inside the disposable Dagger candidate. It can corrupt or
remove only an explicitly validated evidence-owned cache namespace and never produces acceptance.

The seed uses the ordinary wrapper at its normal thresholds: pytest passes, then an intentionally
uncovered source return makes diff coverage fail and causes the Dagger-owned proof to be published.
The seed lives in the source-derived one-consumer `cli/context_packet.py` leaf. Every scenario
repairs it before applying its own mutation. The product scenario deliberately mutates that same
low-fan-out product owner; choosing `kernel/atomic_write.py` would correctly select almost the
entire suite and would test central fan-out rather than targeted product retry. Each
scenario restores an isolated copy into the same compatibility-key cache path. Product,
ordinary-test, shared-support, fixture, and recursive-plugin mutations must then complete through
pytest and the post-coverage rails without a conservative full fallback. Unknown ownership,
lane/environment drift, corruption, and explicit disablement append a deliberate Ruff stop after
retry planning; those cases prove the named conservative decision with zero pytest execution.
Python comment mutations normalize only terminal newlines and insert the two module-level blank
lines Ruff requires. The evidence mutator therefore cannot turn a correct retry selection into a
false pre-pytest formatter failure.

### Conventions

Scenarios are explicit. Cache absence, corruption, and the rollback switch remain distinct cases.

### Invariants And Boundaries

- No host or product runtime imports this evidence helper.
- Mutations are confined to the disposable Dagger workspace/cache.
- Seed proof copies are isolated per scenario while the active cache path remains stable so cache
  location cannot masquerade as a compatibility-key change.
- A recursive-plugin mutation is not plan-only: every source-derived plugin consumer must rerun and
  the matrix requires `result: pytest PASS`.
- Executing mutation scenarios require wrapper success and reject the conservative full-rerun line;
  plan-only conservative cases require the wrapper's explicit `result: pytest SKIPPED` marker and
  zero pytest execution. An absent result is not proof of non-execution.
- The report is non-accepting even when every expected decision matches.

### Todos

None.

## Docs References

No external contract applies.

## Repo-Internal References

`.dagger/src/agents_remember_quality/retry_evidence_route.py` orchestrates the matrix.

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-27T22:09+02:00 — Corrected plan-only evidence semantics: the quality wrapper emits an
  explicit `pytest SKIPPED` result, which proves no pytest execution and is not an empty result set.
- 2026-08-27T20:45+02:00 — Corrected the product scenario to reuse the designated low-fan-out
  product owner after the central atomic-write mutation selected 486 test modules and exposed an
  invalid executable population.
- 2026-08-27T20:12+02:00 — Made controlled Python comment mutations formatter-valid after the
  real product scenario selected the correct consumers but stopped at Ruff format before pytest.
- 2026-08-27T16:27+02:00 — Moved the temporary post-pytest seed from central `atomic_write.py` to
  the source-derived one-consumer context-packet leaf after the real matrix showed central repair
  fan-out contaminating every scenario. Verification remains Dagger-owned.

- 2026-08-27T15:55+02:00 — Replaced the `threshold=-1` simulation, which forced every delta into a
  full fallback, with a Ruff-clean post-pytest seed failure plus isolated proof restoration. Executing
  scenarios now prove a successful affected-only route; conservative cases prove zero pytest work.
- 2026-08-27T15:29+02:00 — Required the recursive-plugin scenario to execute and pass its complete
  affected pytest consumer population; retained plan-only stopping only for conservative
  miss/disable decisions.
- 2026-08-27T11:08+02:00 — Created for canonical-route retry and rollback proof.
