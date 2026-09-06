# mcp/tests/test_git_closeout_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_git_closeout_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T17:13:06+00:00 |
| lastVerifiedCommitHash | |
| lastVerifiedCommitDate | |
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Real Git publication capability regression fixtures.

## Code Commentary

### Logic

Temporary repositories exercise exact expected-old ref updates, raw CRLF bytes, physical/index/ref drift, wrong prepared ancestry/tree, forged or cancelled capability, no-op/already-new observation, actual ref-lock failure and lost-response readback. Fixture callbacks provide bounded test authority; these cases do not establish public lifecycle approval or aggregate acceptance.

### Conventions

Use the named source owners directly. This card describes the current uncommitted implementation; commit-based verification remains pending.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_Publication` owns the corresponding behavior described above. | `_Publication` | `mcp/tests/test_git_closeout_publication.py:34-45` |
| `publication` owns the corresponding behavior described above. | `publication` | `mcp/tests/test_git_closeout_publication.py:49-88` |
| `test_cancelled_and_unminted_authority_cannot_publish` owns the corresponding behavior described above. | `test_cancelled_and_unminted_authority_cannot_publish` | `mcp/tests/test_git_closeout_publication.py:170-179` |
| `test_wrong_prepared_tree_and_non_direct_parent_are_not_publishable` owns the corresponding behavior described above. | `test_wrong_prepared_tree_and_non_direct_parent_are_not_publishable` | `mcp/tests/test_git_closeout_publication.py:182-197` |
| `test_existing_leg_is_observation_only` owns the corresponding behavior described above. | `test_existing_leg_is_observation_only` | `mcp/tests/test_git_closeout_publication.py:200-212` |
| `test_real_ref_lock_failure_is_retained_and_lost_response_reopens_exact_new_ref` owns the corresponding behavior described above. | `test_real_ref_lock_failure_is_retained_and_lost_response_reopens_exact_new_ref` | `mcp/tests/test_git_closeout_publication.py:215-244` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
