# mcp/tests/test_agents_remember_quality.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_agents_remember_quality.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the Dagger module itself is pinned, parseable, fail-closed, and builds the intended clean quality graph before live Docker execution is considered trustworthy.

## Code Commentary

### Logic

In-process fake Dagger objects record container graph construction. The tests cover pinned
manifest/image inputs, targeted and full argument selection, real/fake Codex probe wiring,
export-before-verdict behavior, invalid public inputs, and green/red verification. The public
quality and non-accepting evidence routes must expose their generated Dagger contracts. Tests
load the Dagger package from the explicit `.dagger/src` source root; the surrounding `.dagger`
directory is not an import root.

### Conventions

The suite tests graph semantics without a daemon; live field proof remains a separate Dagger run.

### Invariants And Boundaries

- Unit doubles may replace Dagger transport but not command/graph selection.
- Reports must export at the exact completed boundary even for a red run.
- Invalid mode, omitted/blank diff base, or memory inputs refuse.
- Generated Dagger help is tested as part of the public quality-function contract.
- `load_dagger_module` must prepend exactly `DAGGER_SOURCE_ROOT`; broadening the certifying
  container's global `PYTHONPATH` to hide a bad test loader would mix orchestration code into the
  application import surface.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The test contract is defined by the pinned repository module and its explicit source root. | `DAGGER_MANIFEST`; `DAGGER_SOURCE_ROOT`; `DAGGER_MODULE` | mcp/tests/test_agents_remember_quality.py:21-24 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dynamic graph-contract tests load the package from `.dagger/src`, independent of ambient host paths. | `load_dagger_module` | mcp/tests/test_agents_remember_quality.py:28-34 |
| Tests cover pinning, Dagger-attestation refusal, single-result export, and real graph construction. | `test_agents_remember_quality_module_is_pinned_and_parseable`; `test_python_suite_refuses_missing_or_mismatched_dagger_attestation`; `test_agents_remember_quality_exports_failures_as_the_only_authoritative_result`; `test_dagger_quality_builds_the_real_probe_and_targeted_wrapper_graph` | mcp/tests/test_agents_remember_quality.py:101-124; mcp/tests/test_agents_remember_quality.py:200-227; mcp/tests/test_agents_remember_quality.py:242-247; mcp/tests/test_agents_remember_quality.py:310-366 |

## Cross-Repo References

No sibling-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fake Dagger objects isolate graph verification from external transport. | `FakeContainer`; `FakeDag` | mcp/tests/test_agents_remember_quality.py:38-87; mcp/tests/test_agents_remember_quality.py:90-98 |

## R39 Guard Wiring Proof

The quality entry-point tests patch the shared production validator through conftest and require
its Dagger refusal to become pytest usage failure. They no longer test a second local attestation
implementation.

## 260824-PDLS Certifying Graph Proof

The suite now exercises `testing.dagger_admission` and the conftest certifying composition instead
of the deleted code-quality validator. Dagger command construction must export
`/reports/pytest-phases.json`, and result timestamps must be ordered. Invalid admission still
refuses before collection; phase output remains observation rather than authority.

## 2026-08-26 Evidence-Graph Reconciliation

The Dagger module contract exposes `quality` for certifying acceptance plus separate non-accepting
cadence, causal, retry, retry-matrix, and route-measurement evidence routes. The quality graph
fetches the candidate bundle, stages the complete candidate, requests the causal-failure report,
and publishes that report reference in its authoritative result. Evidence routes cannot become
acceptance merely because their commands execute successfully.

The retry-matrix graph distinguishes an executing scenario from a plan-only fail-closed scenario
using the wrapper's explicit pytest result. Executing scenarios require `result: pytest PASS`;
plan-only scenarios require `result: pytest SKIPPED ...` and reject an absent result or a real
pytest failure. This prevents the harness from treating its own explicit non-execution marker as
evidence failure.

Candidate construction has one deterministic base boundary: pinned image and dependency caches,
OS/tool installation, exact source and repository-bundle reconstruction, and the editable package
install all precede attempt-specific state. Only after that base is built may the graph mount the
retry-proof cache or bind the attestation nonce, report paths, and other per-attempt environment.
`test_candidate_setup_precedes_every_attempt_specific_cache_input` structurally rejects a graph
that lets a fresh nonce or report destination invalidate the expensive shared candidate base.

## Update History

- 2026-08-28T02:38+02:00 — Recorded the deterministic candidate-base versus attempt-binding
  boundary and its structural graph regression after repeated evidence runs exposed nonce-driven
  rebuilds of otherwise identical OS, tool, source, and editable-install layers.
- 2026-08-27T22:09+02:00 — Documented the focused regression contract that distinguishes actual
  pytest execution from the wrapper's explicit plan-only `SKIPPED` marker.
- 2026-08-27T14:36+02:00 — Recorded the explicit `.dagger/src` import boundary after clean Dagger
  exposed an off-by-one source-root calculation; refreshed the six-route public contract.
- 2026-08-26T10:44:52+02:00 — Documented the separate non-accepting cadence graph, causal-failure artifact, candidate staging, and exact two-function Dagger public surface.
- 2026-08-24T21:23+02:00 — Updated admission ownership and added Dagger phase/timestamp wiring proof.

- 2026-08-14T11:27+02:00 — R39 curator: recorded one shared environment-authorization owner.
  Verification remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: replaced the retired verify-method test reference with the
  current Dagger-attestation, single-authoritative-result, and graph-construction tests.
  Verification remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final curator pass: recorded the required explicit diff base and
  generated argument-help contract for both Dagger functions. Focused clean proof covered all 26
  tests with 20 workers; Ruff, formatting, layering, Pyright, CRAP, and all 7 changed coverage lines
  passed. Final commit provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — Created with L23's Dagger graph contract tests; verification provenance remains closeout-owned.
