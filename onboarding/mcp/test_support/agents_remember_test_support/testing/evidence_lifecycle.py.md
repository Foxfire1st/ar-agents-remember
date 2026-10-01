# mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py

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

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- Inventory loading validates the catalog against source-derived consumer facts. [2]
- Contract owners and exact evidence selectors must resolve to real source nodes. [3]
- Discovery delegates the configured-threshold and durable-artifact predicate to one owner. [4]
- The module's own docstring names it the **consumer-completeness oracle** and separates it from the catalog byte pin beside it, naming each gate's documented repair. [5]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [6]
