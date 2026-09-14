# mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
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
| Candidate identity binds the complete Git working candidate. | `candidate_identity`; `_candidate_tree` | mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py:265-293 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `PREFLIGHTS` | mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py:237-251 |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/test_support/agents_remember_test_support/code_quality/causal_preflight.py` changed since the
  recorded verification commit. Re-read the card against the frozen on-disk source and re-checked
  its claims and cited ranges: nothing this card asserts is falsified by the change, so no wording
  changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `terminal_operation_record` owner moved to the synchronous lifecycle store, adding two lines
  inside `PREFLIGHTS`. Repointed the `PREFLIGHTS` range (237-249 → 237-251) and the
  `candidate_identity`/`_candidate_tree` range (263-291 → 265-293). Verification metadata remains
  closeout-owned.
- 2026-08-27T11:14+02:00 — Reconciled source-derived exact-node chains, observer-edge exclusion,
  same-file independent execution, and non-accepting report ownership.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
