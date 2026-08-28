# mcp/tests/test_direct_landing_execution_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_direct_landing_execution_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves direct-landing ledger commit recovery helpers.

## Code Commentary

### Logic

The cases force candidate identity and every ordered code, memory, ledger, ref, and certification
proof stage. The focused recovery seams additionally require an already-present ledger mapping to
match the current memory commit, exact `HEAD` ledger bytes, and an exact clean branch snapshot;
memory recovery may converge through either a clean committed snapshot or a previously recorded
ledger-mutation intent, never an arbitrary dirty tree.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.
- Exact bytes and exact mutation state are independent inputs: a matching ledger row does not make
  a dirty repository safe, and a clean repository does not excuse changed ledger bytes.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `test_existing_mapping_requires_exact_head_bytes_and_clean_repository`; `test_existing_mapping_refuses_changed_head_ledger_bytes`; `test_memory_prestate_allows_only_clean_commit_or_prepared_ledger_intent` | mcp/tests/test_direct_landing_execution_helpers.py:79-204 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

## Update History

- 2026-08-27T19:47+02:00 — PDLS exact-candidate retry forcing exposed uncovered branches in the
  direct-landing CRAP repair. Added focused exact-byte, clean-snapshot, and prepared-ledger-intent
  forcing; eight paired pure tests and the Dagger delta candidate pass. The verification hash is
  the immutable non-landed candidate stored in the PDLS evidence bundle, not a moved real branch.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
