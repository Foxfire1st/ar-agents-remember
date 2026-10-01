# mcp/tests/fixtures/repository_profiles/node/test/e2e.test.mjs

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The clean-room service-flow E2E test of the Node repository-profile fixture, run by the Gate-4
rail (`node --test test/e2e.test.mjs`). It composes repository behavior (JSON with
`add(20, 22)` = 42) to represent an integration scenario for the foreign fixture repository.

## Code Commentary

A single `node:test` case serializes `{ total: add(20, 22) }` and asserts it deep-equals
`{ total: 42 }`. The Gate-4 rail publishes an `{"status": "passed", "tool": "node:test"}`
result when it passes.

## Invariants And Boundaries

- Fixture-only integration scenario; the product never launches a real Codex or clean-room
  environment from framework code.
- Part of the Node fixture profile's Gate-4 applicability.

## Evidence

### Docs References

CCR-R22@v1: Gate 4 contains clean-room or external/runtime integration and E2E certification;
repositories may choose tools and populations but not the ordering contract.

Gate 4 contains clean-room or external/runtime integration and E2E certification.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Fixture e2e scenario executed by the Gate-4 rail. [1]
