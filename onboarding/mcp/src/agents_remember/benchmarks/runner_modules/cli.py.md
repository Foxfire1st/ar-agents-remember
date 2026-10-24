# mcp/src/agents_remember/benchmarks/runner_modules/cli.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Argparse command wiring for benchmark list, prepare, run, and analyze commands.

## Code Commentary

### Logic

`cli.py` converts command-line arguments into `BenchmarkPrepareRequest` and `BenchmarkRunRequest` service calls, prints captured messages, and handles user-facing parser errors.

### Invariants And Boundaries

- CLI functions are adapters; benchmark behavior belongs in service, execution, workspace, or analysis modules.
- Keep command payload shape aligned with the MCP service functions.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]

### Cross-Repo References

No configured sibling repository is required for this module.

## The removed skill-exposure switch

`--skill-exposure-mode` is gone from the prepare and run commands, and `SKILL_EXPOSURE_MODES` with it: a benchmark workspace reads the skills the tool server serves from the package copy, so there is no copy-or-none choice left to name. The commands and their other arguments are unchanged.

- The parser both commands are built from, without the exposure switch. [3]
