# mcp/test_support/agents_remember_test_support/testing/__init__.py

## Governing Overview

[Python test infrastructure overview](overview.md)

## Purpose

Marks the test-infrastructure package without re-exporting leaf-module contracts.

## Code Commentary

### Logic

The initializer is intentionally documentation-only. Callers import admission, bootstrap, eligibility, evidence, and lifecycle APIs from their owning modules.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Do not add convenience re-exports: package-level imports recreate pytest bootstrap fan-out and ambiguous contract ownership.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

- No external domain source is required to establish this repository-owned implementation. [1]

### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

- The module's concrete API, control flow, and validation boundary are implemented here. [2]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [3]
