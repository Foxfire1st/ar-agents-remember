# mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test infrastructure overview](overview.md)

## Purpose

Owns typed lifecycle metadata and validation for durable test recordings, fixtures, and shared support.

## Code Commentary

### Logic

It loads the lifecycle catalog and validates its 34 governed artifacts. Governance covers every
non-test Python support module below the configured test roots, durable data/configuration inputs,
policy manifests, task/date-bound proof artifacts, and any non-Python file at or above the
configured large-fixture threshold. `evidence_governance.py` owns this discovery predicate so the
configuration is operational rather than descriptive. Each artifact declares authority, category,
fidelity, cadence, lifetime, replacement, and consumer scope. Real contract records bind an
existing owner symbol to an exact evidence node. Declared exact consumers are checked against the
source-derived import/reference graph; `all-tests` consumers are derived rather than copied into
the catalog.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Every governed artifact has one explicit authority and lifetime; expired or replaced evidence
  cannot remain silently active; internal and external truth sources stay distinct.
- The discovered governed-artifact inventory and catalog must be exact: missing and stale rows are
  both findings.
- Contract owners and exact evidence nodes must exist, and declared consumers must match observed
  source ownership.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `load_evidence_inventory` | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:161-207 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| Inventory loading validates the catalog against source-derived consumer facts. | `load_evidence_inventory`; `_validate_path_and_consumers` | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:158-206; mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:349-377 |
| Contract owners and exact evidence selectors must resolve to real source nodes. | `_validate_contracts` | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:453-492 |
| Discovery delegates the configured-threshold and durable-artifact predicate to one owner. | "def governed_artifact_paths("; `_validate_catalog_coverage` | mcp/test_support/agents_remember_test_support/testing/evidence_governance.py:15-52; mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:556-573 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `CATALOG_PATH` | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:21-21 |

## Update History

- 2026-08-28T04:37+02:00 — Corrected the post-Candidate-A catalog census to 34 and documented the
  operational configured-size threshold now owned by `evidence_governance.py`.
- 2026-08-27T11:14+02:00 — Reconciled the 35-artifact lifecycle inventory, real owner/node
  contracts, source-derived consumer verification, and exact missing/stale coverage boundary.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
