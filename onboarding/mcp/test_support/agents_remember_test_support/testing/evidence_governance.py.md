# mcp/test_support/agents_remember_test_support/testing/evidence_governance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/evidence_governance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Owns the threshold-aware discovery predicate for durable evidence and test-support artifacts.

## Code Commentary

### Logic

`governed_artifact_paths` walks configured test roots and selects non-test Python support,
known durable data suffixes, policy manifests, task/date-shaped proof, and any non-Python file at
or above the configured byte threshold. Python source remains governed by source/file-size rails,
so the fixture threshold cannot accidentally reclassify ordinary implementation files. The
lifecycle catalog is the policy input that supplies the threshold and is explicitly outside its
own artifact population; otherwise a sufficiently large catalog would recursively require an
entry in itself.

### Conventions

The configured threshold is positive and operational. Unknown suffixes are governed by size rather
than falling through a fixed extension allowlist.

### Invariants And Boundaries

- Discovery is repository-relative and returns one exact path set.
- A non-positive threshold refuses instead of disabling large-fixture governance.
- The lifecycle catalog must exactly cover this discovered population.
- The lifecycle catalog is not a durable evidence artifact governed by itself.
- No compatibility suffix list shadows this predicate.

### Todos

None recorded.

## Docs References

No external domain documentation governs this repository-owned predicate.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Discovery combines support, durable suffix, policy, task/date, and configured-size authority while excluding the lifecycle catalog policy input. | `governed_artifact_paths`; `LIFECYCLE_CATALOG_PATH` | mcp/test_support/agents_remember_test_support/testing/evidence_governance.py:11-52 |
| The lifecycle validator consumes this exact predicate. | `_validate_catalog_coverage` | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:553-571 |
| Focused forcing proves an unknown suffix crosses governance only at the configured threshold and the catalog remains excluded even below its byte size. | `test_configured_size_threshold_governs_unknown_fixture_suffixes` | mcp/tests/test_evidence_lifecycle.py:185-209 |

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-28T05:10+02:00 — Made the lifecycle catalog's policy-input exclusion explicit after the
  first v19 Dagger proof caught self-referential threshold discovery.
- 2026-08-28T04:37+02:00 — Created for the operational configured-size evidence-governance owner.
