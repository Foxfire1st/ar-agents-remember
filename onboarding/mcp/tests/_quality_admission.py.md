# mcp/tests/_quality_admission.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Provides modeled admission input for quality-plan tests using injected runners.

## Code Commentary

The helper creates a temporary nonce file and calls `require_dagger_admission` with an explicit local environment mapping and attestation path. `QUALITY_TEST_ADMISSION` is a modeled input to these tests. It does not import a global certifying bootstrap, modify the process environment, or change the real Dagger attestation path.

## Invariants And Boundaries

Real delivery obtains its capability through the executor handshake. This fixture does not declare a daemon identity or certify host test execution. Its temporary file is cleaned after constructing the input.

## Evidence

### Repo-Internal References

- Explicit modeled input with no process-environment mutation. [1]
