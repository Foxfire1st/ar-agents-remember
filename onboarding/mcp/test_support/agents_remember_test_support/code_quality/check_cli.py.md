# mcp/test_support/agents_remember_test_support/code_quality/check_cli.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:35:26+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Quality support overview](overview.md)

## Purpose

Owns construction of the repository Python-quality command line after the parser was separated
from execution. It publishes the full/targeted policy controls and report-output paths without
becoming a second quality runner or a host-side acceptance route.

## Code Commentary

### Logic

`build_parser` declares the fixed gate contract: targeted versus full scope, optional process
memory cap, project root, diagnostic CRAP review threshold, diff comparison base, and evidence outputs. There is no `--diff-floor` argument or mandatory coverage percentage.
`_add_evidence_output_arguments` groups the coverage, pytest event/phase, causal-failure, coverage
data, and progress paths so evidence plumbing does not obscure the policy arguments.

### Conventions

The parser describes what the Dagger-owned wrapper accepts. Actual scope derivation, rail
execution, evidence verification, and pass/fail ownership stay in `check.py` and its collaborators.

### Invariants And Boundaries

- No path argument may let a caller hand-select the quality scope; full and targeted scope remain
  derived from repository state.
- Evidence-output arguments select publication locations, not acceptance authority.
- Direct host invocation does not become certifying merely because it uses this parser.
- The parser must not duplicate execution or report interpretation owned by the quality wrapper.

### Todos

None recorded.

## Docs References

No configured external Domain Documentation source governs this repository-owned CLI contract.

## Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| Full/targeted inputs and diagnostic-only CRAP threshold | `build_parser` | mcp/test_support/agents_remember_test_support/code_quality/check_cli.py:13-71 |
| Evidence paths separated from policy arguments | `_add_evidence_output_arguments` | mcp/test_support/agents_remember_test_support/code_quality/check_cli.py:74-117 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-09-06T21:35:26+00:00 — Reconciled the d3610903 test-policy reduction against the current source, preserved integrity/ownership boundaries, and replaced stale forcing-suite citations with current owner evidence. Existing verification hash/date retained; source comparison is not final acceptance.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: created for the final parser ownership split and verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this provenance does not certify the red Dagger gate.
