# mcp/tests/test_memory_ledger.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_ledger.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T14:32+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused kernel-level proof that the external-memory ledger is newest-first state history rather
than a globally unique code-to-memory map.

## Code Commentary

### Logic

The test starts from one code/memory edge, prepends a later memory commit for the same code commit,
round-trips the canonical text, and proves both views of authority: `find_mapping` returns the
newest memory state while `contains_mapping` still finds the older exact audit edge.

### Conventions

The scenario uses the public immutable ledger helpers directly. It stays small enough for the
sealed pure-unit route when that cohort is explicitly extended; executing it outside Dagger before
then is not acceptance evidence.

### Invariants And Boundaries

- Repeated code commits are valid when they record ordered memory states.
- The newest matching row is current authority.
- Older exact rows remain preserved audit history.
- This test does not weaken ledger schema, metadata, or first-row validation.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this repository-local ledger format.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for this repository-owned regression contract. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused scenario proves newest current lookup and exact historical containment after round-trip serialization. | `test_roundtrip_preserves_newest_same_code_history` | mcp/tests/test_memory_ledger.py:13-28 |
| The kernel owns the current-versus-historical lookup distinction. | `find_mapping`; `contains_mapping` | mcp/src/agents_remember/kernel/memory_ledger.py:232-242 |

## Cross-Repo References

No cross-repository implementation source governs this focused unit.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T14:32+02:00 — Created for the IAS ledger-history correction. Verification metadata
  remains blank until the source commit exists.
