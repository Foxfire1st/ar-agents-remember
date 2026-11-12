# mcp/tests/fixtures/repository_profiles/node/scripts/lint.mjs

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The Gate-1 (pre-test quality) rail of the Node repository-profile fixture: a tiny static lint
script that reads the fixture source and tests and refuses tabs or `var` usage. It proves the
generic executor invokes a repository-owned, non-Agents-Remember command for deterministic
pre-test quality.

## Code Commentary

`lint.mjs` iterates `src/math.mjs`, `test/unit.test.mjs`, `test/e2e.test.mjs`, reads each
file, and throws `static quality failed for <path>` if it contains a tab or `var `. It is run
as a repository-owned Node command (executed through the declared adapter), has no arguments, and
its failure is the fixture's Gate-1 refusal.

## Invariants And Boundaries

- Repository-owned fixture rail: the generic framework never hardcodes this command or path.
- Deterministic: passes exactly when the three files are clean; the fixture source is authored to
  stay clean.

## Evidence

### Docs References

CCR-R22@v1 classifies Gate 1 as deterministic pre-test quality that does not consume Gate-2
results and does not require the clean-room integration environment; repositories choose tools
and populations but not the ordering contract.

Gate 1 contains deterministic pre-test quality that does not consume Gate-2 results.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Fixture static-quality rail over the fixture source and tests. [1]
