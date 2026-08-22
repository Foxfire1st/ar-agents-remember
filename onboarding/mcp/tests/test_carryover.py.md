# mcp/tests/test_carryover.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_carryover.py`              |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`test_carryover.py` validates branch-memory carryover planning/apply, with MX-FIX-4 focused on
fail-closed official-memory JSON/Markdown write authority and exact zero mutation on refusal.

## Code Commentary

### Logic

The existing real-repository fixtures cover sidecar, route-overview, memory-only-doc, and entity-
catalog candidates; evidence tiers; guarded official route-index regeneration; ledger mapping; and
ff-only memory-main advancement. MX-FIX-4 extends full apply with snapshots of official HEAD, Git
status, every non-Git byte, source bytes, and route-index presence.

Refusal cases include missing/invalid/unrelated settings, `onboarding:null`, invalid non-null
shapes, semantically empty rule containers and members, blank Markdown, final empty/reset lists,
unsupported recognized lists, unsupported storage labels, and truthy invalid fallback. Positive
controls cover root storage fallback, mode/layout selection, falsey fallback, valid global/scoped
rules, retained contributions across repeated keys, later repopulation, supported list names, and
official-over-source authority. Each case compares raw preflight outcome with the typed settings
parser, then runs production `apply_carryover_for_request()`.

### Conventions

Helpers create real code and memory Git repositories and drive the service API, not CLI adapters.
Refusal tests assert the whole observable mutation surface rather than only the raised exception.
JSON and Markdown cases are paired where their parser semantics correspond.

### Invariants And Boundaries

- Parser defaults cannot grant official-memory write authority when raw rules are empty.
- Missing, invalid, unsupported, or final-reset-to-empty authority refuses before all mutation.
- Retained explicit contributions and later repopulation remain valid exactly when the typed parser
  retains them.
- JSON sibling precedence, root fallback, mode/layout selection, and official-over-source settings
  are fixed and independently tested.
- Every refusal preserves official HEAD/status/non-Git bytes, source bytes, ledger, and route-index
  absence; successful apply reuses the validated storage authority for index refresh.

### Todos

Refresh verification metadata only after closeout commits the candidate.

## Docs References

No Domain Documentation source is configured for this repository. The full-apply fixtures and local
typed parser are the authority evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Carryover's internal apply owner requires configured repository, exact leaf-contract, protected-checkout, and target-settings authority before content/ledger/index/commit mutation. | `_apply_carryover_for_request`; `_require_carryover_authority` | mcp/src/agents_remember/memory/carryover.py:759-893 |
| Raw JSON/Markdown preflight mirrors typed parser semantics while rejecting default-only write authority. | `required_target_storage` | mcp/src/agents_remember/memory/carryover_authority.py:32-66 |
| Authority matrix spans missing/invalid/empty/reset/unsupported refusals and retention/repopulation/fallback positive controls. | `test_missing_official_settings_refuses_before_any_mutation`; `test_supported_nonempty_path_rules_remain_authoritative`; `test_unsupported_markdown_storage_labels_refuse_before_any_mutation` | mcp/tests/test_carryover_apply_1.py:113-126; mcp/tests/test_carryover_apply_2.py:455-494; mcp/tests/test_carryover_apply_2.py:569-603 |
| Earlier evidence-tier and ledger-mapping coverage remains in worktree tests. | `test_memory_ledger_roundtrip_and_prepend`; `test_memory_carryover_applies_landed_branch_onboarding` | mcp/tests/test_worktree_support_tests_1.py:360-371; mcp/tests/test_worktree_support_tests_3.py:701-761 |

## Cross-Repo References

Fixtures model separate code and external-memory repositories locally; no sibling repository is a
test dependency.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 4 citation claims; scoped result 0 findings.

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added full-apply JSON/Markdown official-settings
  authority matrices, typed-parser equivalence controls, retained/repopulated rule semantics,
  unsupported cases, selector isolation, and exact zero-mutation refusal proof.
- 2026-06-11T15:05+02:00 — Added entity-catalog and memory-only-doc candidate/evidence coverage.
- 2026-06-10T09:45+02:00 — Issue #54 sub-task C added memory-main advancement coverage.
- 2026-06-10T05:50+02:00 — Created for route-overview carryover candidates and guarded index
  regeneration (issue #56 sub-task 3).
