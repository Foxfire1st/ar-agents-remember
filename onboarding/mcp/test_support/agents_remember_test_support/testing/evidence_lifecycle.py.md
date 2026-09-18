# mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted change set; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `overview.md` |

## Governing Overview

[Python test infrastructure overview](overview.md)

## Purpose

Owns typed lifecycle metadata and validation for durable test recordings, fixtures, and shared support.

## Code Commentary

### Logic

It loads the lifecycle catalog and validates its currently declared governed artifacts. Governance covers every
non-test Python support module below the configured test roots, durable data/configuration inputs,
policy manifests, task/date-bound proof artifacts, and any non-Python file at or above the
configured large-fixture threshold. `evidence_governance.py` owns this discovery predicate so the
configuration is operational rather than descriptive. Each artifact declares authority, category,
fidelity, cadence, lifetime, replacement, and consumer scope. Real contract records bind an
existing owner symbol to an exact evidence node. Declared exact consumers are checked against the
source-derived import/reference graph; `all-tests` consumers are derived rather than copied into
the catalog.

**This module is the consumer-completeness oracle, and that is one of two gates rather than the whole
guard.** Its docstring (`:1-18`) now says so in those terms: `load_evidence_inventory` derives the
repository's real dependency graph and requires every `consumer_scope = "exact"` artifact's declared
`consumers` list to equal the test modules that actually reach it, so it reddens exactly when a module
starts or stops consuming a governed artifact — with the catalog's own **bytes untouched** — and its
documented repair is a registry row. The **catalog byte pin** named beside it
(`LIFECYCLE_CATALOG_SHA256`, `LIFECYCLE_CONTRACT_COUNT`, `LIFECYCLE_ARTIFACT_COUNT` in
`mcp/tests/test_dependency_ownership_ast_helpers.py:43-46`) answers a different question — is this the
exact catalog file that was measured, at the populations it was measured at — and its documented repair
is a re-pin. The two assertions run inside one test and therefore read as one gate; they are not, which
is why the pin's constants move when a registry row is *added* rather than when the source tree drifts,
and `mcp/tests/test_evidence_catalog_gate_boundaries.py` holds the case that reddens this oracle while
the pin stays green.

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
| Discovery delegates the configured-threshold and durable-artifact predicate to one owner. | "def governed_artifact_paths("; `_validate_catalog_coverage` | mcp/test_support/agents_remember_test_support/testing/evidence_governance.py:16-16; mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:581-598 |
| The module's own docstring names it the **consumer-completeness oracle** and separates it from the catalog byte pin beside it, naming each gate's documented repair. | "consumer-completeness oracle" | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:1-18 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `CATALOG_PATH` | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:38-38 |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_validate_catalog_coverage`; "def governed_artifact_paths(" repointed to mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:581-598; mcp/test_support/agents_remember_test_support/testing/evidence_governance.py:16-16. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `CATALOG_PATH` repointed to mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:38-38. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T19:24+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded what item 13 changed in this module. Its docstring was rewritten (`:1-18`) to name it the **consumer-completeness oracle** and to separate it from the **catalog byte pin** in `mcp/tests/test_dependency_ownership_ast_helpers.py`: the two assertions run in one test and read as one gate, they are not, and the distinction is what explains the direction each moves — the oracle's documented repair is a registry row, the pin's is a re-pin, so the pin's constants move when a row is *added* rather than when the source tree drifts. A new paragraph in `### Logic` states that, and one reference row was added for the docstring. Nothing behavioural in the body changed: the loading, contract-owner, consumer-derivation and coverage statements were re-read against the source and stand as they were. Verification metadata is not advanced — the change is uncommitted and closeout owns the stamp — and the metadata block now carries a `reviewedWorkingCandidate` row naming this leaf's candidate as what was read.
- 2026-08-28T04:37+02:00 — Corrected the post-Candidate-A catalog census to 34 and documented the
  operational configured-size threshold now owned by `evidence_governance.py`.
- 2026-08-27T11:14+02:00 — Reconciled the 35-artifact lifecycle inventory, real owner/node
  contracts, source-derived consumer verification, and exact missing/stale coverage boundary.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
