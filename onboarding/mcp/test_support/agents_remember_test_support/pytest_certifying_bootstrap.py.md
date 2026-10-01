# mcp/test_support/agents_remember_test_support/pytest_certifying_bootstrap.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Composes certifying-only pytest plugins while deferring the worktree service graph until fixture execution.

## Code Commentary

### Logic

The verification-package plugin names the shared hermetic, evidence-lane, phase, and causal
plugins. Session/function fixtures bind and reset default worktree services with fixture-local
product imports, so collection does not eagerly load the service/lifecycle graph.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- This module stays at the verification-package root to avoid executing the testing package
  initializer; importing it must not eagerly load the service/lifecycle graph.
- Verification may import product fixtures at the fixture boundary. Product code must never import
  this bootstrap or any `agents_remember_test_support` module.
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
