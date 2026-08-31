# mcp/tests/test_clean_quality_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_clean_quality_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T04:50+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite forces the host-side Dagger executor through exact candidate capture, export, result parsing, report publication, Git guards, progress streaming, and native executable resolution.

## Code Commentary

### Logic

Tests build temporary Git repositories and intercept only the Dagger process boundary. They prove the staged candidate and ancestry are passed once, invalid modes and Windows roots refuse, export failures cannot proceed, invalid results cannot be guessed green, and partial output is observable before completion.

The publication fixture now exports both canonical Python proof files and requires each to resolve
through the immutable published-generation reader. This catches an executor allowlist that would
silently discard runtime provenance even when Dagger produced it.

The publication cases also export the nested ambient E2E summary and both run reports. They require
the immutable manifest to preserve those relative paths, reject undeclared files/directories and
links, verify every copied digest/size, and resolve each nested artifact through the same current
generation reader. This catches the earlier flat allowlist behavior that discarded evidence Dagger
had actually produced.

### Conventions

Real Git state is used where candidate identity matters; process transport is doubled narrowly.

### Invariants And Boundaries

- The executor must publish no invented result after export failure.
- Candidate and report Git guards fail closed.
- Dagger resolution passes through the native-command policy.
- Both base-interpreter and venv-interpreter proof artifacts survive immutable publication and
  content lookup.
- Nested E2E artifacts survive recursive publication exactly once; unsafe or undeclared paths fail
  before the manifest pointer moves.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external document is required for the repository-owned executor contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact candidate, refusal, export, result, reporting, and native-command behavior are forced. | `CleanQualityExecutorTests` | mcp/tests/test_clean_quality_executor.py:38-223 |

## Cross-Repo References

No sibling-repository contract is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary Git repositories isolate each executor proof. | `repository` | mcp/tests/test_clean_quality_executor.py:18-36 |

## L23 Final Candidate Disposition

The executor suite proves every quality attempt is fresh, both report projections share one result,
status failures refuse, output remains bounded without rewrite amplification, stale predecessor
reports are pruned, and no local/direct-Docker fallback exists.

## 260821-DAGQC-L2 Strict Manifest Writer/Reader Proof

The focused publication cases pin the exact schema-1.0 object root, immutable generation/file facts,
attestation handling, and one stable error family for malformed, legacy, or alternate shapes. They
also prove artifact lookup consumes the parsed manifest instead of rereading the pointer.

## 260824-PDLS Immutable Evidence Proof

Publication fixtures now bind every generation to an explicit candidate tree and schema `2.0`.
Passing executor outcomes carry certifying evidence; failed outcomes carry none. A source export
without one valid authoritative result refuses instead of publishing an incomplete generation.

## 2026-08-26 Causal-Report Publication Reconciliation

The atomic report-generation tests now include `causal-failures.json` and
`causal-failures.md`. Interrupted publication must leave the prior generation intact, while a
successful pointer rotation makes the causal JSON discoverable through
`published_report_path` alongside the authoritative clean-quality result. Causal reporting is
therefore part of one immutable published generation rather than an adjacent best-effort file.

## Update History

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: added the recursive
  nested-report publication, path-safety, digest verification, and lookup regression contract.
  Verification remains closeout-owned.

- 2026-08-29T16:27+02:00 — Added immutable publication and lookup proof for both canonical Python
  runtime artifacts.

- 2026-08-26T10:44:52+02:00 — Reconciled atomic causal-failure report publication and lookup with the candidate-bound quality generation.
- 2026-08-24T21:23+02:00 — Added candidate-bound schema-2 publication and evidence assertions.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: added strict manifest schema/error and parsed-snapshot artifact lookup coverage. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-14T06:38+02:00 — L23 final candidate review: executor forcing cases cover fresh attempts,
  shared authoritative projections, fail-closed status, bounded live output, stale-report pruning,
  exact candidate bundles, and no direct-Docker/local fallback.

- 2026-08-12T15:19+02:00 — Created with L23 clean quality executor tests; verification provenance remains closeout-owned.
