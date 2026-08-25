# mcp/src/agents_remember/testing/evidence_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/evidence_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the machine-enforced authority, provenance, cadence, lifetime, expiry/graduation, replacement,
and consumer contract for durable test evidence and shared support.

## Code Commentary

### Logic

`load_evidence_inventory` parses `mcp/tests/evidence-lifecycle.toml` into closed enums and typed
`EvidenceMetadata` rows, then validates every declared artifact, consumer, authority/lifetime
combination, expiry, replacement, and governed-path census. `node:` replacements are parsed from
real Python and must identify exactly one current top-level function or class method.

### Conventions

The catalog is the consumer/provenance authority used by collection, targeted selection, retry, and
reporting. Errors are accumulated and raised together so authors receive the full current delta.

### Invariants And Boundaries

- Temporary evidence needs a future expiry and executable replacement; migration evidence cannot
  be permanent.
- Retained evidence needs a permanence rationale; versioned evidence requires external authority.
- New snapshots, recordings, task/date baselines, large fixtures, and shared support cannot enter
  without a catalog row.
- The validator never preserves stale proof through compatibility prose.

### Todos

None.

## Docs References

No external documentation owns this repository lifecycle policy.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed metadata types include authority, fidelity, cadence, and lifetime. | `EvidenceMetadata` | mcp/src/agents_remember/testing/evidence_lifecycle.py:24-137 |
| Inventory loading fails on all current parse and schema findings. | `load_evidence_inventory` | mcp/src/agents_remember/testing/evidence_lifecycle.py:140-236 |
| Artifact, authority, replacement, and census validation is centralized. | `_validate_artifacts` | mcp/src/agents_remember/testing/evidence_lifecycle.py:254-421 |
| The current catalog uses the one lifecycle schema. | "ar-test-evidence-lifecycle/v1" | mcp/tests/evidence-lifecycle.toml:1-2 |

## Cross-Repo References

No cross-repository lifecycle authority is owned here.

## Update History

- 2026-08-25T01:56+02:00 — Created for enforced durable evidence lifecycle and expiry.
