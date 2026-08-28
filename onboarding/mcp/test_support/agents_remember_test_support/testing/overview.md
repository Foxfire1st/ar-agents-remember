# Python Test Evidence Infrastructure Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/test_support/agents_remember_test_support/testing` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-28T10:16:27+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

Repository-owned test and evidence infrastructure: Dagger admission, hermetic pytest setup,
explicit evidence lanes, lifecycle governance, source-derived dependency facts, cadence execution,
retry/causal forcing routes, and representative route measurement.

## Hot Path Summary

`dependency_facts.py` is the declaration-free import/plugin/consumer fact graph.
`lane_manifest.py` binds every test file and override to one explicit category.
`evidence_lifecycle.py` validates every governed durable artifact/support file and its real
contract, lifetime, and observed consumers; `evidence_governance.py` owns the threshold-aware
discovery rule. `candidate_snapshot.py` and `evidence_provenance.py` bind non-accepting artifacts to
the exact staged candidate and machine. `retry_selection.py` rebuilds current collection/import
coverage while allowing only dependency-owned affected test modules to execute during a delta
retry. `route_measurement.py` compares exact pure, integration, and durability populations under
serial and repository-default xdist. `causal_failures.py` owns the exact-node suppression boundary
and distinct observed async/process/multiprocessing/subprocess/socket/timeout/environment families;
`causal_route_evidence.py` measures the three-symptom/two-independent repair protocol.

## Operating Model

Certifying pytest admits the Dagger capability before collection. Python has no supported host
pytest route: Candidate A was retired after its exact-candidate retention falsifier failed, and no
compatibility classifier or runner remains. Scheduled/provider/migration cadence and
retry/causal/measurement routes run only inside Dagger and write non-accepting reports. A retry
delta collects the canonical population so unattributed import coverage is current, then deselects
every body outside its explicit affected-module set. The eight evidence categories are explicit;
no unmarked item defaults to unit.

## Local Invariants And Traps

- Every current test file has exactly one explicit lane; missing, stale, unknown, or conflicting
  membership refuses collection.
- Recursive literal `pytest_plugins` edges are source facts in every Python module; dynamic
  declarations make ownership incomplete.
- Candidate-A host execution, manifest, classifier, and diagnostic evidence type are absent; the
  seven unique product assertions remain ordinary certifying regressions.
- Causal suppression skips only exact nodes with an independently proved contract chain.
- Retry selection requires each explicit affected path to own an executable item or have a passing
  Pytest module-collection report. This admits observed zero-body shared-definition modules while
  absent/uncollected paths still fail; neither case converts into broad execution.
- Controlled Python mutations used by retry-route evidence preserve Ruff-valid module spacing, so
  a matrix harness formatting defect cannot masquerade as retry invalidation.
- Plan-only retry scenarios prove non-execution through the wrapper's explicit `pytest SKIPPED`
  result; empty output is not accepted as evidence that pytest stayed closed.
- The product retry scenario uses the designated low-fan-out product owner. A central primitive
  would correctly select most of the suite and would no longer be a targeted product-consumer proof.
- Route evidence never becomes certifying merely because it ran inside Dagger.
- Every cadence/retry/causal/measurement artifact carries candidate and machine provenance; route
  measurement also records exact commands, population digests, phases, repeated distributions,
  and content-addressed raw logs.

## File-Level Onboarding Map

All Python files in this route have one adjacent sidecar. The generated index is refreshed from the
current source tree rather than copied from the retired `mcp/src` route.

## Docs And Boundary References

See `docs/design/python-evidence-system.md` and `docs/design/python-test-evidence.md`. Candidate
measurements and rollback evidence remain task reports, not timeless onboarding claims.

## Update History

- 2026-08-28T10:03:40+02:00 — Added the complete observed failure-family ownership split and the
  measured three-symptom causal repair protocol to the route hot path.
- 2026-08-28T04:37+02:00 — Retired Candidate-A host diagnostics, added threshold-aware evidence
  governance and shared provenance, and replaced pure-only route comparison with repeated
  pure/integration/durability serial/default-xdist measurement.
- 2026-08-27T22:09+02:00 — Recorded explicit `pytest SKIPPED` as the plan-only retry proof after
  the live matrix exposed a validator that incorrectly expected no result line.
- 2026-08-27T21:10+02:00 — Split observed zero-body module collection from genuinely
  missing/uncollected retry paths without adding a fallback.
- 2026-08-27T20:45+02:00 — Bound the product retry scenario to the low-fan-out seed owner after a
  central atomic-write mutation selected 486 test modules.
- 2026-08-27T20:12+02:00 — Recorded formatter-valid controlled retry mutations after the real
  product matrix exposed a pre-pytest harness defect.
- 2026-08-27T17:19+02:00 — Added the dependency-owned retry execution boundary: canonical
  collection restores current import evidence while only explicit affected modules execute.
- 2026-08-27T11:08+02:00 — Moved test infrastructure under verification ownership and reconciled
  explicit lanes, source-derived consumers, complete candidate binding, persistent retry, and
  exact-node causal evidence. Verification remains closeout-owned.
