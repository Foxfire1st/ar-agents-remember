# mcp/src/agents_remember/certification/results.py

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns fail-closed construction and publication of typed rail terminal results against one exact
admitted gate plan.

## Code Commentary

### Logic

`build_rail_result` binds an observation to the planned rail identity and digest.
`compile_gate_result_manifest` admits the plan, checks the complete result catalog, validates every
identity, applicability decision, declared artifact, bounded evidence reference, and blocker, then
publishes the full gate manifest or raises one typed error containing all findings.

### Conventions

The manifest is a complete projection of the plan, not a summary of successful rails. Blocking is
derived from enforcing prerequisite results; report-only results remain visible but cannot make an
enforcing failure green.

### Invariants And Boundaries

- Omitted, inserted, duplicate, substituted, or candidate-mismatched results fail publication.
- Passing rails provide every promised artifact and required evidence reference, and no undeclared
  artifact/evidence may appear.
- Only real enforcing prerequisite failure/blocking may block a dependant rail.
- Independent siblings remain terminally represented when another rail fails.
- Diagnostic results cannot be promoted to certifying authority.
- A generic wrapper exception is not a terminal rail result; typed codes, owners, and evidence
  references remain in the result contract.

### Todos

The execution layer must translate adapter observations into these contracts without losing typed
failure evidence.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation could be checked.

### Repo-Internal References

- Result construction binds one terminal observation to a planned rail. [1]
- Manifest compilation re-admits the plan and accumulates complete catalog and contract findings before publication. [2]
- Catalog validation rejects result omission, insertion, duplication, and substitution. [3]
- Applicability, artifacts, and evidence are checked against the planned contract. [4]
- Blocking semantics distinguish enforcing prerequisites from independent or report-only failures. [5]

### Cross-Repo References

The result compiler has no knowledge of repository commands or Agents Remember test names.

- All result admission is driven by the generic `GatePlan`. [6]
