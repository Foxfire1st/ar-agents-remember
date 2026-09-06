# mcp/tests/test_final_codex_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_final_codex_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `54ff803a05209e06f732f2de1f90e2a71a069e08` |
| lastVerifiedCommitDate | 2026-09-04T22:31:30+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Shared final-Codex scenario, run-record and authority builders.

## Code Commentary

### Logic

Helpers compile synthetic rail/scenario registries and manifests, create exact repetition identities and plan/attempt/environment records, then publish drafts through the run store. FakeInspector and engine_environ provide declared test authority without a real engine.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No model-contract tests remain in this file. A helper-generated green run or fake inspection is fixture input, not proof of fresh production executions.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Railspec. | `RailSpec` | mcp/tests/test_final_codex_models.py:96-99 |
| Identity. | `identity` | mcp/tests/test_final_codex_models.py:102-103 |
| Rail. | `rail` | mcp/tests/test_final_codex_models.py:106-157 |
| Scenario registry. | `scenario_registry` | mcp/tests/test_final_codex_models.py:160-184 |
| Certifying plan. | `certifying_plan` | mcp/tests/test_final_codex_models.py:187-192 |
| Manifest for. | `manifest_for` | mcp/tests/test_final_codex_models.py:195-245 |
| Scenario failure. | `scenario_failure` | mcp/tests/test_final_codex_models.py:248-273 |
| Gate4 manifest. | `gate4_manifest` | mcp/tests/test_final_codex_models.py:276-282 |
| Repetition identity. | `repetition_identity` | mcp/tests/test_final_codex_models.py:285-296 |
| Fresh identities. | `fresh_identities` | mcp/tests/test_final_codex_models.py:299-300 |
| Plan record. | `plan_record` | mcp/tests/test_final_codex_models.py:303-325 |
| Attempt record. | `attempt_record` | mcp/tests/test_final_codex_models.py:328-353 |
| Environment binding. | `environment_binding` | mcp/tests/test_final_codex_models.py:356-360 |
| Authority binding. | `authority_binding` | mcp/tests/test_final_codex_models.py:363-385 |
| Teardown record. | `teardown_record` | mcp/tests/test_final_codex_models.py:388-410 |
| Make draft. | `make_draft` | mcp/tests/test_final_codex_models.py:413-452 |
| Make store. | `make_store` | mcp/tests/test_final_codex_models.py:455-464 |
| Publish run. | `publish_run` | mcp/tests/test_final_codex_models.py:467-479 |
| Store codes. | `store_codes` | mcp/tests/test_final_codex_models.py:482-483 |
| Fakeinspector. | `FakeInspector` | mcp/tests/test_final_codex_models.py:486-515 |
| Engine environ. | `engine_environ` | mcp/tests/test_final_codex_models.py:518-530 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass: created this card for the new standalone CCR-R14 builder/model-contract suite delivered in code commit 54ff803a; anchors and ranges derived from the current worktree source and pinned to that commit (tree aff2e268968397ab8db042a782652957a3600dda).
