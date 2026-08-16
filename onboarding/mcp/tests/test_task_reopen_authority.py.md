# mcp/tests/test_task_reopen_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_reopen_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T07:05+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

Forces terminal leaf reopen to preserve completed landing evidence when the exact contract, code
source, external-memory source, or integrated ledger proof changes between preflight and the locked
task-fact publication.

## Code Commentary

The suite builds real organizational sprint-super task documents and Git repositories. Its external
fixture creates a content commit followed by a canonical code-to-memory ledger commit. Race tests
advance code or memory immediately before the production publication callback, while forged-ledger
tests retain exact source tips but alter mapping or reachability. Every refusal proves contract,
task-document, and frozen-landing artifacts are unchanged by reopen.
Valid concurrent leaf/master edits that invalidate the reset edge are introduced between outer
preflight and the production callback; the locked re-plan refuses and preserves their exact bytes.

## Invariants And Boundaries

- Apply revalidates the exact reviewed contract and landed source pair while queue/repository
  authority is held.
- External reopen may erase integration fields only after exact mapping and content reachability.
- A competing contract write is preserved; reopen never overwrites it from a stale candidate.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Locked code/memory races and stale-contract publication are production-bound through the reopen task entry point. | `ReopenPublicationAuthorityTests` | mcp/tests/test_task_reopen_authority.py:99-178 |
| Forged mapping and unreachable-content commits refuse before reset. | `test_external_reopen_requires_exact_reachable_integrated_ledger_mapping` | mcp/tests/test_task_reopen_authority.py:235-274 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-16T07:15+02:00 — Added leaf/master task-document races proving locked re-planning prevents stale overwrite and preserves the competing publication.
- 2026-08-16T07:05+02:00 — 260815-DAG-L4: created for the queue-to-repository reopen authority recheck, stale-contract race, and exact external-ledger proof.
