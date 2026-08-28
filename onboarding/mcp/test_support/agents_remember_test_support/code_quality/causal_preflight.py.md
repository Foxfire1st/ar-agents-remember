# mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

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

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `evaluate_preflights` | mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py:57-99 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| Owner outcomes and source-derived exact dependents form the causal report. | `evaluate_preflights`; `_blocked_consumers` | mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py:57-99; mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py:132-146 |
| Candidate identity binds the complete Git working candidate. | `candidate_identity`; `_candidate_tree` | mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py:263-291 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `PREFLIGHTS` | mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py:237-249 |

## Update History

- 2026-08-27T11:14+02:00 — Reconciled source-derived exact-node chains, observer-edge exclusion,
  same-file independent execution, and non-accepting report ownership.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
