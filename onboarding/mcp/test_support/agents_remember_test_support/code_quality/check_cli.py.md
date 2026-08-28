# mcp/test_support/agents_remember_test_support/code_quality/check_cli.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Owns construction of the repository Python-quality command line after the parser was separated
from execution. It publishes the full/targeted policy controls and report-output paths without
becoming a second quality runner or a host-side acceptance route.

## Code Commentary

### Logic

`build_parser` declares the fixed gate contract: targeted versus full scope, optional process
memory cap, project root, CRAP and changed-line thresholds, and the evidence-output family.
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
- The parser must not duplicate execution or threshold logic owned by the quality wrapper.

### Todos

None recorded.

## Docs References

No configured external Domain Documentation source governs this repository-owned CLI contract.

## Repo-Internal References

The source file is the direct evidence for the extracted parser boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The parser exposes derived full/targeted policy, memory, CRAP, and diff-floor arguments. | `build_parser` | mcp/test_support/agents_remember_test_support/code_quality/check_cli.py:12-78 |
| Evidence output paths are grouped separately from policy arguments. | `_add_evidence_output_arguments` | mcp/test_support/agents_remember_test_support/code_quality/check_cli.py:81-124 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: created for the final parser ownership split and verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this provenance does not certify the red Dagger gate.
