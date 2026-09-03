# mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Legacy lifecycle bridge overview](overview.md)

## Purpose

Isolates schema-1 inspection, migration, and evidence-gated archive behavior from the current lifecycle model.

## Code Commentary

### Logic

It parses exact legacy bytes, classifies migrate/archive/inspect actions, publishes a current generation once, detects exact existing migration, and delegates terminal archive mechanics.

Since 260831-CCR (commit `99dc249b`) the schema-1 to schema-3 closeout migration binds canonical
task intent: `_migrated_closeout_record` (line 664-689) resolves the contract's current
`contract_task_intent(contract)` (line 674) and stamps it on the migrated `LifecycleOperationRecord`
(`taskIntent=intent`, line 688). If the contract cannot produce a canonical intent (e.g. the task
document or door is missing/legacy), the migration refuses with `LegacyBridgeError` carrying the
typed status and `next_action` (default `task_doc`, line 676-681), so a migrated generation is
always intent-bound and never recreated without one.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- No silent schema fallback or permanent compatibility reader exists; migration identity binds original bytes, task, contract, kind, and resulting generation.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- A migrated closeout generation must carry canonical task intent; absence refuses before the
  record is published.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `LegacyOperationCommand` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_bridge.py:1-879 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `LegacyOperationCommand` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_bridge.py:1-879 |
| Migrated closeout records bind the contract's current canonical task intent. | `_migrated_closeout_record` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_bridge.py:664-689 |
| The intent source the migration resolves. | `contract_task_intent` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_identity.py:60-66 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `LegacyOperationCommand` | mcp/src/agents_remember/worktrees/integration/legacy/legacy_operation_bridge.py:1-879 |

## CCR-R02@v2 Intent-Bound Migration

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, newly published containers must
carry the exact canonical intent identity and writers may not emit the sentinel. Schema-1 closeout
migration therefore computes and stamps the contract's canonical intent, and refuses when no intent
can be established. Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  schema-1 closeout migration now binds the contract's canonical task intent and refuses with a
  typed error+next-action when intent cannot be established; documented the intent-bound migration
  invariant. Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
