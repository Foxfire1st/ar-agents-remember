# PDLS Onboarding Wave 003 — Final Evidence-System Reconciliation

| Field | Value |
| --- | --- |
| repo | agents-remember |
| generated | 2026-08-25T02:13+02:00 |
| waveType | high-risk file onboarding, deleted-slice cleanup, route reconciliation |
| mode | existing-memory-slice-maintenance |
| status | onboarding complete; final source validation pending |
| source HEAD | `23d35f7799153e0c7f3d126291fe2da1662fb87b` |
| source candidate tree | `7d677bde8ac0756c9f2c4964ad3b9423509d1e66` |

## Goal

Reconcile the earlier Candidate-A onboarding to the final approved master: explicit bounded
cohort, executable evidence lifecycle/cadence, product-only scoring, one dependency-ownership
graph, and owner-level causal localization, with no retained generic analyzer or obsolete evidence
slice.

## New High-Risk Cards

| Priority | Card | Source | Reason |
| --- | --- | --- | --- |
| high | `testing/cohort_manifest.py.card.md` | `testing/cohort_manifest.py` | direct admission policy |
| high | `testing/evidence_lifecycle.py.card.md` | `testing/evidence_lifecycle.py` | durable evidence authority |
| high | `testing/evidence_lanes.py.card.md` | `testing/evidence_lanes.py` | category/cadence registry |
| high | `testing/cadence_runner.py.card.md` | `testing/cadence_runner.py` | non-accepting Dagger cadence |
| high | `testing/causal_failures.py.card.md` | `testing/causal_failures.py` | causal runtime evidence |
| high | `code_quality/dependency_ownership.py.card.md` | `code_quality/dependency_ownership.py` | sole consumer graph |
| high | `code_quality/causal_preflight.py.card.md` | `code_quality/causal_preflight.py` | owner-level validation |
| high | `tests/_adapter_event_scripts.py.card.md` | `tests/_adapter_event_scripts.py` | provider evidence split |
| high | `tests/_evidence_catalog_fixture.py.card.md` | `tests/_evidence_catalog_fixture.py` | single catalog builder |
| high | `tests/_direct_cohort_candidate.py.card.md` | `tests/_direct_cohort_candidate.py` | inert sealed cohort |

All card paths are rooted below `onboarding/bootstrap/file-cards/mcp/`; table paths are shortened
for readability.

## Refreshed Current Owners

- testing overview, direct runner, eligibility, selection contract, unsafe effects, phase reporter
- code-quality check, targeted scope, retry proof, scope, scope reporting
- lifecycle operation worker and control-plane harness
- MCP, repository, and tests overviews
- conversation models overview, initializer, primitives, and control-wire cards

## Deleted Stale Cards

- rejected analyzer: `collection_closure.py.md`, `dependency_closure.py.md`,
  `python_source.py.md`
- expired evidence: `test_model_split_baseline.py.md`,
  `model_split_baseline_260731_efa_l9.json.md`
- unused self-validating fixture: `build_rich_sim.py.md`, `test_sim_fixture_builder.py.md`

## Evidence Required

- exact source candidate tree and diff census
- current requirement/reconciliation reports
- source-backed one-to-one sidecars
- no live citations or generated routes to deleted source
- final route-index dry run
- focused source checks followed by the sole full Dagger master gate

## Acceptance

- Every new high-risk owner has one sidecar and one file card.
- Current overviews recover the explicit cohort, lifecycle, product-scoring, ownership, and causal
  boundaries.
- Deleted source has no sidecar, compatibility route, or live citation.
- Deferred ordinary forcing tests are named in the coverage plan.
- Generated indexes and reference checks are clean.
- Curator review records only the final delta and does not reopen approved decisions.

## Disposition

Wave-scoped curation passed on 2026-08-25: 36 changed documents have zero citation findings, the
fast document checks are green across 1,898 documents, and all 66 route indexes are current. The
single final full Dagger gate remains master-level source evidence and does not reopen this
onboarding verdict.
