# mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py

## Governing Overview

[Python quality overview](overview.md)

## Purpose

Runs owner-level compatibility preflights for high-fanout prerequisites before pytest.

## Code Commentary

### Logic

It binds the complete candidate, environment, and Dagger attempt identity, evaluates each registered
contract owner once, and asks the source-derived causal dependency graph for exact dependent node
chains. Observer/reporting imports are excluded from causal edges. Each blocked row records its
owner, exact node, evidence altitude, corrective owner, and full dependency chain; the paired JSON
and Markdown reports describe the same result.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Only source-graph-proven exact nodes may be classified as blocked; observer edges and file-level
  proximity do not create causality.
- Independent and same-file sibling nodes remain visible; a failed preflight cannot publish
  acceptance evidence.
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

- Owner outcomes and source-derived exact dependents form the causal report. [2]
- Candidate identity binds the complete Git working candidate. [3]

### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No meaningful cross-repository reference applies. [4]
