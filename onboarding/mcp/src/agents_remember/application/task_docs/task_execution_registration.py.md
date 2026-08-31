# mcp/src/agents_remember/application/task_docs/task_execution_registration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_execution_registration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T08:31+02:00 |
| lastVerifiedCommitHash |  `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Persist monotonic leaf-owned execution registrations and classify topology-valid higher-review
evidence before typed evidence reclamation.

## Code Commentary

### Logic

The module resolves a canonical registration address, captures the current task source or a narrowly
proven leaf-retirement parent, and publishes typed terminal-seat or operator-inbox registrations
through the task-first mutation boundary. Reclamation callers receive a durable success/refusal
result rather than inferring task history from external records.

The address boundary admits `task.json` only for a reviewer. After the exact source loads, the
canonical filename still dominates an untrusted payload-kind claim: every reviewer `task.json`
enters the non-leaf topology classifier before any leaf branch. Topology must prove that it is a
master or sprint before the result becomes `reviewer-non-leaf`;
this status permits ordinary TTL/hard-cap reclamation without mutating the task document. Missing,
orphaned, malformed, or ambiguous non-leaf authority blocks. Workers and curators remain confined
to JSON-primary leaf documents, and all leaf roles retain the ordinary monotonic mutation route.

After preparing the registration document and its exact accepted source, this module delegates to
`publish_prepared_task_documents`. It does not independently resolve projection-scope unions or
assemble a weaker write path; registration receives the same source-CAS, task-first publication,
projection invalidation, and rebuild semantics as ordinary task authoring.

### Invariants And Boundaries

- Registration is task-owned historical truth and is monotonic.
- Routine terminal-seat or inbox evidence may be reclaimed only after the matching registration publishes.
- Missing or unreadable task authority fails closed except for the explicit parent-audit retirement route.
- A missing `task.json` never enters the leaf-retirement proof; it is a blocked non-leaf reviewer
  source.
- Only a topology-valid reviewer master/sprint is durable without mutation. Worker and curator
  `task.json` references remain `not-leaf`, and organizational orphans remain blocked.
- A `task.json` payload that falsely declares `kind=subTask` cannot acquire leaf mutation authority;
  it is classified at the non-leaf boundary and blocks without changing JSON or Markdown bytes.
- The task publication lock protects the source CAS; queue state cannot veto registration.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The typed result and central registration route bind address, role, and source evidence. | `TaskExecutionRegistrationResult`; `register_task_execution_evidence` | mcp/src/agents_remember/application/task_docs/task_execution_registration.py:38-50; mcp/src/agents_remember/application/task_docs/task_execution_registration.py:72-124 |
| Reviewer-only `task.json` admission is classified through canonical topology before any leaf mutation; missing non-leaf authority blocks. | `_classify_missing_registration_source`; `_classify_non_leaf_reviewer`; `_registration_address` | mcp/src/agents_remember/application/task_docs/task_execution_registration.py:142-153; mcp/src/agents_remember/application/task_docs/task_execution_registration.py:168-196; mcp/src/agents_remember/application/task_docs/task_execution_registration.py:199-229 |
| Source classification distinguishes current, retired, missing, and unreadable task state. | `_load_registration_source`; `_classify_missing_task_source` | mcp/src/agents_remember/application/task_docs/task_execution_registration.py:250-261; mcp/src/agents_remember/application/task_docs/task_execution_registration.py:264-286 |
| Terminal-catalog and operator-inbox adapters use the same registration owner. | `register_terminal_catalog_execution_evidence`; `register_operator_inbox_execution_evidence` | mcp/src/agents_remember/application/task_docs/task_execution_registration.py:328-364; mcp/src/agents_remember/application/task_docs/task_execution_registration.py:367-398 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-31T08:31+02:00 — 260821-ARSPAWN-L5 final-round correction: made canonical
  `task.json` reviewer classification precede payload-kind branching, so a malformed subtask claim
  cannot enter leaf mutation.

- 2026-08-31T08:05+02:00 — 260821-ARSPAWN-L5 A004 correction: documented the now-reachable,
  reviewer-only master/sprint classifier, its no-mutation reclamation result, and fail-closed
  missing/orphan boundaries while preserving worker/curator leaf-only mutation.

- 2026-08-26T10:44:52+02:00 — Reconciled registration publication with the shared prepared-document API and removed the obsolete caller-owned transaction assembly narrative.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
