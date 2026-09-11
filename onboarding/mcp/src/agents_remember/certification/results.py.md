# mcp/src/agents_remember/certification/results.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/results.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Result construction binds one terminal observation to a planned rail. | `build_rail_result` | mcp/src/agents_remember/certification/results.py:26-61 |
| Manifest compilation re-admits the plan and accumulates complete catalog and contract findings before publication. | `compile_gate_result_manifest` | mcp/src/agents_remember/certification/results.py:63-112 |
| Catalog validation rejects result omission, insertion, duplication, and substitution. | `_validate_result_catalog` | mcp/src/agents_remember/certification/results.py:149-181 |
| Applicability, artifacts, and evidence are checked against the planned contract. | `_validate_result_applicability`; `_validate_result_artifacts`; `_validate_result_evidence` | mcp/src/agents_remember/certification/results.py:217-294 |
| Blocking semantics distinguish enforcing prerequisites from independent or report-only failures. | `_validate_blocking_semantics`; `_expected_blockers` | mcp/src/agents_remember/certification/results.py:296-355 |

## Cross-Repo References

The result compiler has no knowledge of repository commands or Agents Remember test names.

| Finding | Anchor | Source |
| --- | --- | --- |
| All result admission is driven by the generic `GatePlan`. | `compile_gate_result_manifest` | mcp/src/agents_remember/certification/results.py:63-72 |

## Update History

- 2026-09-01T03:11+02:00 — Created for complete typed gate-result publication and failure
  preservation. Verification remains closeout-owned until the source candidate is committed.
