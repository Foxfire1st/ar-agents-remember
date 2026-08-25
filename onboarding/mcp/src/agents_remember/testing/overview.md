# Python Testing and Evidence Boundary Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `mcp/src/agents_remember/testing/` |
| onboardingRoute | `onboarding/mcp/src/agents_remember/testing/overview.md` |
| parentOverview | [`mcp overview`](../../../overview.md) |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |

## What This Area Is

This route owns Python test-evidence policy below the quality/lifecycle plane:

1. durable evidence category, authority, fidelity, cadence, lifetime, and replacement;
2. the bounded exact-node diagnostic cohort and its fail-closed admission;
3. shared hermetic pytest preparation versus Dagger-only certifying admission;
4. non-accepting scheduled/provider/migration cadence;
5. route-neutral phase and causal-failure observations.

The route does not own acceptance publication. Direct diagnostics and cadence results remain
non-accepting; only the Dagger quality executor's immutable candidate-bound publication can mint
certifying evidence.

## Hot Path Summary

Start with `evidence_lifecycle.py` and `evidence_lanes.py` for evidence authority/cadence;
`cohort_manifest.py` and `eligibility.py` for direct admission; `direct_runner.py` for exact local
feedback; `dagger_admission.py` plus the certifying bootstrap for acceptance startup; and
`causal_failures.py` for downstream failure localization.

## What Belongs Here

| Path | Role |
| --- | --- |
| `evidence_lifecycle.py` | Durable artifact metadata, census, expiry, graduation, and replacement. |
| `evidence_lanes.py` | Closed evidence categories, pytest markers, and cadence expressions. |
| `cadence_runner.py` | Non-accepting scheduled/provider/migration Dagger execution. |
| `cohort_manifest.py` | Strict explicit direct-cohort schema and reachability. |
| `eligibility.py` | Sole whole-request classifier and candidate-binding verifier. |
| `selection_contract.py` / `unsafe_effects.py` | Closed decision, refusal, and effect vocabulary. |
| `diagnostic_bootstrap.py` / `direct_runner.py` | Current-selection validation and one serial diagnostic command. |
| `hermetic_bootstrap.py` / `global_state.py` / `random_order.py` | Shared deterministic process state. |
| `dagger_admission.py` / `certifying_bootstrap.py` | Dagger-only admission and certifying composition. |
| `pytest_bootstrap.py` / `pytest_certifying_bootstrap.py` | Shared versus certifying-only pytest plugins. |
| `pytest_phase_reporter.py` | Route-neutral phases and node outcomes. |
| `causal_failures.py` | Graph-proven blocking and independent/process-sensitive failure records. |
| `consumer_inventory.py` | Closed accepting-consumer inventory used by firewall proof. |

## What Does Not Belong Here

| Concern | Owner |
| --- | --- |
| Test consumer graph, quality scope, retry, and owner preflight | `mcp/src/agents_remember/code_quality/` |
| Diagnostic/certifying serialized capability model | `mcp/src/agents_remember/models/test_evidence.py` |
| Immutable Dagger generation publication | `mcp/src/agents_remember/worktrees/modules/` |
| Dagger container graph | `.dagger/src/agents_remember_quality/main.py` |
| Fixture/event support worlds | `mcp/tests/` with lifecycle-catalog ownership |

## Operating Model

### Durable evidence

The lifecycle catalog is validated before behavior runs. New governed artifacts cannot enter
without complete authority, fidelity, cadence, provenance, lifetime, replacement, and consumer
metadata. Temporary migration proof expires; external versioned proof stays independent of product
generators.

### Direct diagnostic

The v2 manifest seals seven exact nodes, eight audited Python files, configuration bytes, symbols,
local imports, effects, fixtures, and per-node closure. The classifier verifies the whole request;
one refusal executes zero nodes. The runner uses canonical pytest configuration, shared hermetic
setup, `-n=0`, and no conftest discovery. It rechecks the binding after execution and emits only
diagnostic JSON.

### Certifying quality

Root conftest obtains Dagger admission before certifying plugin load or collection. Certifying
pytest adds evidence lanes, causal reporting, and real worktree service composition. The quality
executor outside this route publishes the only accepted candidate-bound result.

### Cadence and causal reporting

Affected quality excludes sustained stress; full release runs every category. Separate Dagger
cadence commands run stress, provider-bump, or migration evidence without acceptance. An owner
preflight may mark only complete import/catalog consumers as causally blocked; independent failures
continue and retain reproduction metadata.

## Local Invariants And Traps

- The removed `dependency_closure.py`, `python_source.py`, and `collection_closure.py` have no
  compatibility readers or sidecars. Seven nodes do not justify a generic repository analyzer.
- Hash drift is a refusal requiring deliberate re-audit, not an auto-refresh opportunity.
- Diagnostic/cadence use of shared bootstrap or Dagger containers does not grant authority.
- Direct requests are atomic, exact, serial, and bounded to eight nodes.
- Evidence categories are exhaustive and mutually exclusive; unmarked means unit regression.
- Affected execution may omit sustained stress, but full release and scheduled cadence preserve it.
- Incomplete causal ownership never becomes blanket suppression.
- Phase reporters wait for every xdist worker's collection callback before closing collection.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle catalog validates every durable artifact and replacement. | `_validate_artifacts` | mcp/src/agents_remember/testing/evidence_lifecycle.py:254-265 |
| The lane registry routes affected, release, provider, stress, migration, and diagnostic evidence. | `EVIDENCE_LANES` | mcp/src/agents_remember/testing/evidence_lanes.py:42-111 |
| The explicit manifest and classifier replace generic static analysis. | `load_direct_cohort_manifest`; `classify_direct_selection` | mcp/src/agents_remember/testing/cohort_manifest.py:89-127; mcp/src/agents_remember/testing/eligibility.py:50-75 |
| The certifying plugin loads lanes and causal reporting only after admission. | `pytest_plugins` | mcp/src/agents_remember/testing/pytest_certifying_bootstrap.py:15-19 |

## Cross-Repo References

No adjacent repository supplies or overrides this route's evidence authority.

## Docs References

Repository design authority is in `docs/design/python-evidence-system.md` and the four focused
`docs/design/python-*.md` documents. No external domain-documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| The complete evidence-system contract is repository-owned. | `# Python Test Evidence System` | docs/design/python-evidence-system.md:1-227 |

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `cadence_runner.py` | [`cadence_runner.py.md`](cadence_runner.py.md) | covered |
| `causal_failures.py` | [`causal_failures.py.md`](causal_failures.py.md) | covered |
| `cohort_manifest.py` | [`cohort_manifest.py.md`](cohort_manifest.py.md) | covered |
| `evidence_lanes.py` | [`evidence_lanes.py.md`](evidence_lanes.py.md) | covered |
| `evidence_lifecycle.py` | [`evidence_lifecycle.py.md`](evidence_lifecycle.py.md) | covered |
| `eligibility.py` | [`eligibility.py.md`](eligibility.py.md) | covered |
| `selection_contract.py` | [`selection_contract.py.md`](selection_contract.py.md) | covered |
| `unsafe_effects.py` | [`unsafe_effects.py.md`](unsafe_effects.py.md) | covered |
| `direct_runner.py` | [`direct_runner.py.md`](direct_runner.py.md) | covered |
| `pytest_phase_reporter.py` | [`pytest_phase_reporter.py.md`](pytest_phase_reporter.py.md) | covered |
| Other existing route sources | adjacent one-to-one sidecars | covered |

## Child Overviews

None. The route is one cohesive execution/evidence boundary.

## How To Use This Area

Read the route overview, then the exact owner sidecar. Changes to a category, effect family,
lifecycle field, cohort member, cadence trigger, or causal blocking rule are policy changes and need
explicit requirement authority plus forcing proof.

## Update History

- 2026-08-25T01:56+02:00 — Replaced the generic-analyzer onboarding with the final explicit cohort,
  lifecycle/lanes/cadence, dependency ownership, and causal-localization architecture; removed three
  stale deleted-source cards.
- 2026-08-24T21:23+02:00 — 260824-PDLS created the testing route after separating structural
  diagnostics, reusable bootstrap, Dagger admission, and evidence altitude end to end.
