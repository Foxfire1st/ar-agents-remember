# mcp/tests/test_causal_quality_preflight.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Forces the quality wrapper to continue with the independently runnable pytest population after a
valid causal-owner failure, while falling back to unsuppressed safe mode when the causal subprocess
or its report contract is broken.

## Code Commentary

### Logic

A synthetic runner records every quality command. One test returns a valid failed causal report and
requires pytest to receive that report for exact-node suppression. Two safe-mode tests cover a
failed preflight with no report and a nominally successful preflight with invalid JSON; both require
pytest to run without the suppression option and the overall gate to stay failed.

### Conventions

The test uses the real `CheckConfig` and Dagger admission token but replaces subprocess execution,
so it proves orchestration order and arguments without minting quality acceptance.

### Invariants And Boundaries

- A valid failed causal report permits independent continuation but never converts the gate to
  success.
- Missing, malformed, or contradictory causal evidence disables suppression; it does not disable
  pytest.
- Safe mode must be louder and broader than a valid suppression route, never silently narrower.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; this is an internal wrapper contract.

No external documentation is required for this forcing test.

### Repo-Internal References

- A valid failed causal report reaches pytest while the overall quality result remains failed. [1]
- Missing or invalid reports disable suppression and still run the selected pytest population. [2]
- The fixture uses the real quality configuration and explicit failed-report vocabulary. [3]
- Continuation policy is centralized in its dedicated owner rather than duplicated in the test. [4]

### Cross-Repo References

No meaningful cross-repository boundary applies.

No external process contract is asserted beyond the repository-owned wrapper.
