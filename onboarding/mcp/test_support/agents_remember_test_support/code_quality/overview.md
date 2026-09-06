# Python Quality Verification Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/test_support/agents_remember_test_support/code_quality` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

The Dagger-executed Python quality producer. It owns broad static checks, product-only behavioral
scoring, source-derived test selection, persistent retry proof, causal prerequisite reporting, and
machine-readable quality artifacts. Being shipped in the source distribution does not make this
operational product behavior; its owner and consumers are repository verification.

## Hot Path Summary

`profile_selection.py` publishes the immutable repository-owned selector result;
`profile_rails.py` rederives that exact scope, compares path populations in canonical POSIX-string order without dropping duplicates, and executes the selected Python rails; its teardown adapter publishes hash-bound proof from the actual clean-room reports.
`check.py` executes and interprets the shared rail machinery; `quality_plan.py` owns their typed configuration,
progress state, and deterministic command plan. `scope.py` proves complete
product/verification package authority.
`dependency_ownership.py` consumes source-derived imports, recursive pytest plugins, and literal
artifact readers. `retry_proof.py` owns Dagger-cache identity/lifecycle, `retry_coverage.py` owns
retained/fresh Coverage.py composition, and `quality_subprocess_environment.py` owns the child-rail
environment boundary. `causal_preflight.py` binds failed contracts to exact dependent nodes;
`causal_continuation.py` rejects missing or contradictory reports into an unsuppressed run
of the already selected population; it does not broaden unknown ownership.

## Operating Model

Targeted selection and retry share one immutable source fact graph. Lifecycle declarations are
validated against observed consumers; they never make themselves complete. Missing, ambiguous, dynamic, stale, or contradictory ownership retains explicit unresolved
inputs; targeted `CheckConfig` construction refuses before tests run. Full mode and proven
global invalidators remain explicit scope decisions, not recovery from unknown ownership. Retry proof persists only in the locked `ar-quality-retry-v3` Dagger cache and
binds the exact lane population, environment digest, tools, immutable selection digest, candidate snapshot, and
coverage artifacts. Delta coverage keeps retained and fresh databases separate until a passing
pytest result is explicitly merged and atomically republished for all downstream scorers. An
all-contexts-affected delta carries an explicit known-empty retained state; an unexpected missing
retained database still fails closed.

Non-Python product inputs that cannot participate in the import graph use narrow repository-owned
consumer declarations only when independently observed literal reads match exactly. This lets the
Codex starter configuration select its two real contract consumers and the root layer contract
select its five architecture/structural consumers without treating every unrelated test as
affected. The ambient runner has sixteen exact pytest consumers because the profile fixture and its importers observe its output contract; this ownership remains distinct from the lifecycle policy file's explicit global invalidation. Any declaration/source mismatch marks the selector incomplete and names the reason.

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

Full mode compares the same selector and executable population using canonical path strings; component-wise `Path` ordering is not selector authority. Missing, extra or duplicate paths still refuse before pytest.

The profile rail writes Coverage.py and pytest event/phase artifacts through the declared reports directory. Its `verify-teardown` adapter now requires a proof destination and publishes `teardown-proof/v1` from exact summary and replication bytes after every listed report proves `L5-C10` passed. A skipped scenario has explicit not-applicable proof. The clean-room producer owns the two-replication population; the adapter validates every listed report. Dagger emission and export own persisted binary rail logs and the stable file publications consumed by the host certificate evidence owner. The previously absent Gate-4 artifacts are current declared outputs, with producer and retention forcing in the test route.

## File-Level Onboarding Map

All Python files in this route have one adjacent sidecar. The generated index is the exhaustive
source/sidecar map after refresh.

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact repository declarations are cross-checked against observed consumers. | `_repository_consumers` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:409-441 |
| Proved globals remain separate from unresolved ownership. | `_resolved_impact` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:345-377 |
| Teardown validates exact checkpoint observations and hashes real report bytes. | `_verify_teardown` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:246-297 |
| The adapter writes the declared proof artifact. | `_write_teardown_proof` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:300-310 |
| The adjacent suite carries real verifier bytes through retained publication. | `test_real_teardown_producer_bytes_reach_the_emitted_binding_and_export` | mcp/tests/test_rail_evidence_publication.py:288-353 |
| Canonical POSIX-string sorting preserves duplicates for exact membership validation. | `_paths` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:124-127 |
| The unchanged full population succeeds; missing, extra and duplicate executable members refuse. | `test_full_python_rail_uses_canonical_selector_order_and_still_refuses_scope_drift` | mcp/tests/test_repository_certification_profiles.py:930-968 |

## Docs And Boundary References

The canonical overview is `docs/design/python-evidence-system.md`; retry and direct-route details
are in `docs/design/python-test-evidence.md` and the PDLS evidence reports.

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation: Added canonical string scope ordering and exact population guards, refreshed the shifted teardown owner ranges, and retained the actual L32/C97 teardown contract; no later L33 source-applicability behavior is imported.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Reconciled exact ambient-runner ownership, persisted teardown proof and repaired producer/publication boundaries; removed obsolete print-only and missing-producer claims.

- 2026-09-05T07:08+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Removed obsolete safe-full selection behavior; added selector identity, exact rail scope, causal selected-population limit and unproduced teardown-proof boundary. Verification records current source claims, not execution or acceptance.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 registered the five exact, independently observed
  `layers.toml` consumers. The declaration avoids safe-full selection without making metadata
  self-proving or adding a fallback. Verification remains closeout-owned.

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
