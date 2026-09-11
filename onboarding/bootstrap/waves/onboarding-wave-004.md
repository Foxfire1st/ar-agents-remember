# PDLS Onboarding Wave 004 — Emergency-Landed Ownership Reconciliation

| Field | Value |
| --- | --- |
| repo | agents-remember |
| generated | 2026-08-25T08:27+02:00 |
| waveType | behavior-preserving moves, final high-risk owners, entity and route reconciliation |
| mode | existing-memory-slice-maintenance |
| status | complete — scoped curator pass |
| source commit | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| source tree | `65a8c5fcae3551dd596421d6cb0c56a4ca64bc0d` |

## Goal

Bind durable onboarding to the exact source tree emergency-landed before WSL compaction. Preserve
the existing behavior history through one-to-one sidecar moves, document the five newly extracted
high-risk owners, and keep the red Dagger result distinct from onboarding provenance.

## Behavior-Preserving Moves

Twenty sidecars move with their sources across `application/memory_quality/`, `models/closeout/`,
`worktrees/integration/closeout/`, `worktrees/integration/lifecycle/worker/`, and
`worktrees/modules/quality/`. Their purpose, invariants, references, and prior history are
preserved; path metadata, governing links, current evidence, and update history are refreshed.

## New High-Risk Owners

| Priority | Source | Reason |
| --- | --- | --- |
| high | `code_quality/check_cli.py` | parser policy must not become a second runner |
| high | `lifecycle/control/cancellation.py` | worker/door/journal cancellation transaction |
| high | `lifecycle/observation/projection.py` | total read-only retained-operation projection |
| high | `tests/task_reopen_test_support.py` | real lineage and terminal-predecessor fixture owner |
| high | `tests/_quality_evidence_fixture.py` | immutable published-quality consumer fixture |

## Structural Reconciliation

- Parent application, model, integration, worktree-module, MCP, and tests overviews name the final
  owners and explicitly reject duplicate/fallback authority.
- The entity catalog repairs moved closeout evidence paths and refreshes all nine drifted
  deterministic fingerprints after review.
- New package `__init__.py` markers remain governed by parent overviews; ordinary forcing tests and
  TOML manifests remain explicitly deferred in the coverage plan.
- Nine route indexes are regenerated; the final preview reports 66 unchanged routes.

## Acceptance

- Every preserved behavior owner maps one-to-one to its final source path.
- Every newly extracted high-risk owner has one sidecar and one file card.
- Entity fingerprints resolve against the emergency-landed source commit.
- Scoped citation and document-shape checks report their exact outcome.
- The wave never claims that a red Dagger gate is green or that lifecycle closeout completed.

## Curator Outcome

[`bootstrap/reviews/onboarding-wave-004.curator.md`](../reviews/onboarding-wave-004.curator.md)
passes the emergency-recovery onboarding delta. The authoritative 54-document citation scope decreased from
19 findings to zero in one repair round (68 evidence tables, 215 rows, 353 resolved citations).
Whole-tree deterministic document-shape checks report zero findings across 1,911 Markdown files,
and all 66 route indexes are current. These are memory-quality facts, not Dagger certification.
