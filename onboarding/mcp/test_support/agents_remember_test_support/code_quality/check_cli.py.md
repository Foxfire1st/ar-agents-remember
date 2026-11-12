# mcp/test_support/agents_remember_test_support/code_quality/check_cli.py

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

## Evidence

### Docs References

No configured external Domain Documentation source governs this repository-owned CLI contract.

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

- Full/targeted inputs and diagnostic-only CRAP threshold [1]
- Evidence paths separated from policy arguments [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
