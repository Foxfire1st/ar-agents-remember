# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This TOML file is the enforced lifecycle registry for durable Python test evidence, shared support,
fixtures, and their stable executable replacement contracts.

## Logic

Contract rows bind an owner to an executable evidence node. Artifact rows state authority,
category, fidelity, cadence, provenance, lifetime, permanence/expiry rationale, replacement
contract, and exact source-observed consumers. The public lifecycle validator rejects missing,
stale, contradictory, unowned, or consumer-incomplete rows.

## Current PDLS Delta

The `repository-ruff-policy-evidence` contract and `_ruff_repository_evidence.py` artifact register
the shared Ruff boundary created by the quality-test split, including every direct importer in the
quality-check, quality-scope, file-size, and tool-signature suites. `_quality_admission.py` now lists
the new tool-signature suite as an exact consumer. `large_fixture_bytes` is an operational discovery
threshold for unknown non-source suffixes, not dormant metadata. The catalog is the policy input to
that discovery and is intentionally excluded from its own artifact population, avoiding a recursive
requirement to catalog itself when it crosses the configured size.

## Update History

- 2026-08-28T05:10+02:00 — Recorded the operational unknown-suffix threshold and the lifecycle
  catalog's explicit policy-input/non-artifact boundary after Q5 v19 forced the self-reference case.
- 2026-08-27T13:32+02:00 — Registered the split Ruff support and its exact consumers. Verification
  remains closeout-owned.
