# mcp/tests/test_direct_test_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_test_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Proves the canonical direct command's exact serial invocation, non-certifying output, total refusal,
candidate-drift discard, wrapper pinning, and phase-report integrity.

## Code Commentary

A fake executor captures the complete command/environment and writes controlled route-neutral
phase evidence. Tests cover success, every request refusal with zero executor calls, missing or
contradictory child reports, candidate mutation, executable wrapper contents, and CLI help/payload.
The reporter hook is also forced through an early pytest exit to prove missing collection phases
remain `null` instead of masking the original exit.

## Invariants And Boundaries

- Test fakes do not grant certifying authority.
- Exact node order and child outcome set must match the admitted selection.
- Wrapper proof pins Python 3.12, `uv --no-config`, one module entrypoint, and no Dagger fallback.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Success asserts serial exact-node/environment behavior. | `test_success_runs_exact_nodes_serially_under_canonical_config` | mcp/tests/test_direct_test_runner.py:96-126 |
| Early reporter exit preserves the original pytest code. | `test_phase_report_preserves_original_exit_when_collection_never_finishes` | mcp/tests/test_direct_test_runner.py:162-184 |

## 2026-08-26 Structural Fixture And Xdist Timing Reconciliation

Direct-diagnostic fixtures now materialize both a synthetic direct cohort and the canonical
evidence catalog before a request can run, so eligibility tests exercise the same structural
owners as production. Phase timing also waits for every xdist worker's collection-finished signal;
the first worker cannot prematurely close the collection phase.

## Update History

- 2026-08-26T10:44:52+02:00 — Documented canonical cohort/catalog fixture setup and all-worker xdist collection timing for direct diagnostics.
- 2026-08-24T21:23+02:00 — Created for 260824-PDLS.
