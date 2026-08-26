# mcp/src/agents_remember/application/task_docs/task_execution_registration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_execution_registration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Persist monotonic task-owned execution registrations before typed evidence reclamation.

## Code Commentary

### Logic

The module resolves a canonical leaf registration address, captures the current task source or a narrowly proven retirement parent, and publishes a typed terminal-seat or operator-inbox registration through the task-first mutation boundary. Reclamation callers receive a durable success/refusal result rather than inferring task history from external records.

After preparing the registration document and its exact accepted source, this module delegates to
`publish_prepared_task_documents`. It does not independently resolve projection-scope unions or
assemble a weaker write path; registration receives the same source-CAS, task-first publication,
projection invalidation, and rebuild semantics as ordinary task authoring.

### Invariants And Boundaries

- Registration is task-owned historical truth and is monotonic.
- Routine terminal-seat or inbox evidence may be reclaimed only after the matching registration publishes.
- Missing or unreadable task authority fails closed except for the explicit parent-audit retirement route.
- The task publication lock protects the source CAS; queue state cannot veto registration.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The typed result and central registration route bind address, role, and source evidence. | `TaskExecutionRegistrationResult`; `register_task_execution_evidence` | mcp/src/agents_remember/application/task_docs/task_execution_registration.py:38-50; mcp/src/agents_remember/application/task_docs/task_execution_registration.py:72-124 |
| Source classification distinguishes current, retired, missing, and unreadable task state. | `_load_registration_source`; `_classify_missing_task_source` | mcp/src/agents_remember/application/task_docs/task_execution_registration.py:176-187; mcp/src/agents_remember/application/task_docs/task_execution_registration.py:190-212 |
| Terminal-catalog and operator-inbox adapters use the same registration owner. | `register_terminal_catalog_execution_evidence`; `register_operator_inbox_execution_evidence` | mcp/src/agents_remember/application/task_docs/task_execution_registration.py:284-320; mcp/src/agents_remember/application/task_docs/task_execution_registration.py:323-354 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-26T10:44:52+02:00 — Reconciled registration publication with the shared prepared-document API and removed the obsolete caller-owned transaction assembly narrative.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.