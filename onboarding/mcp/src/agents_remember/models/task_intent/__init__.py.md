# mcp/src/agents_remember/models/task_intent/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/task_intent/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-03T12:30:00+02:00                  |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00                  |
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models route overview](../overview.md)

## Purpose

Typed task-intent slot models and persisted identity states for the canonical
`task-intent/v1` projection (CCR-R02@v2). The package owns the strict wire shapes for
version-addressed approved requirement packet references, typed acceptance-obligation questions,
the canonical identity (schema + SHA-256 digest), and the bounded typed legacy absence sentinel
(`MissingTaskIntent`). It is the single shared vocabulary every closeout, door, lifecycle, route
review, and queue consumer imports; no consumer is allowed its own intent hash.

## Code Commentary

### Logic

`_StrictIntentModel` (line 14) is the shared frozen strict pydantic base: `extra="forbid"`,
`frozen=True`, `serialize_by_alias=True`, so a persisted `taskIntent` cell can never carry an
unclassified extra slot and identity cells are immutable.

- `ApprovedRequirementPacketRef` (line 22) is one version-addressed approved packet reference with
  bounded `path`/`stableId` and a `v[1-9][0-9]*` version pattern; validators strip and refuse blank
  identity fields. Prose never opts itself into authority; only a typed reference is a reference.
- `AcceptanceObligationQuestion` (line 39) is a question explicitly typed as an unresolved
  acceptance obligation (`kind="acceptance-obligation"`, bounded `id` + `question`).
- `TaskIntentIdentity` (line 55) is the canonical identity: closed `schema: task-intent/v1` plus a
  `^[0-9a-f]{64}$` digest. It has no extra semantics of its own.
- `MissingTaskIntent` (line 62) is the typed legacy absence sentinel with no digest; the docstring
  and `missing_task_intent()` (line 71) pin that it is materialized only at a persisted-record
  decode boundary and is deliberately not an identity.
- `TaskIntentState` (line 68) is the union of the two, and `task_intent_is_missing` (line 77) is
  the shared family predicate (`None` or `MissingTaskIntent`).
- `require_task_intent_identity` (line 81) is the one rejection seam: any currentness, reuse, or
  publication consumer that observes the sentinel raises the typed
  `{owner}-task-intent-unavailable` `TaskIntentError` with the exact `next_action`; nothing may
  synthesize a digest, search history for one, or accept a caller-supplied substitute.

### Conventions

The schema literal is `TASK_INTENT_SCHEMA = "task-intent/v1"` (line 11). New normative slots
require a projection-schema revision plus shared field-taxonomy classification; a label or prose
convention cannot opt content into intent (CCR-R02@v2 requirement).

### Invariants And Boundaries

- The sentinel means absence, not identity: it can never satisfy currentness, admission, evidence
  reuse, review acceptance, certificate reuse, or closeout readiness.
- Only the legacy persisted-record decoder/currentness boundary may materialize the sentinel; new
  or republished containers must carry the canonical identity and writers never emit it.
- Decision prose is rationale/audit only and never changes the accepted obligation.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical schema literal used by every child of this package. | `TASK_INTENT_SCHEMA` | mcp/src/agents_remember/models/task_intent/__init__.py:11-11 |
| Version-addressed approved packet reference typed model. | `ApprovedRequirementPacketRef` | mcp/src/agents_remember/models/task_intent/__init__.py:22-36 |
| Typed acceptance-obligation question. | `AcceptanceObligationQuestion` | mcp/src/agents_remember/models/task_intent/__init__.py:39-52 |
| Canonical schema-plus-digest identity and the legacy absence sentinel union. | `TaskIntentIdentity`; `MissingTaskIntent`; `TaskIntentState` | mcp/src/agents_remember/models/task_intent/__init__.py:55-59; mcp/src/agents_remember/models/task_intent/__init__.py:62-65; mcp/src/agents_remember/models/task_intent/__init__.py:68-68 |
| The single currentness/reuse/publication rejection seam. | `require_task_intent_identity` | mcp/src/agents_remember/models/task_intent/__init__.py:81-95 |
| The projection owner built on this vocabulary. | `task_intent_projection` | mcp/src/agents_remember/tasks/task_intent.py:132-177 |
| The field taxonomy that classifies which slots are normative. | `NORMATIVE_INTENT` | mcp/src/agents_remember/tasks/document_field_effects.py:50-54 |



## CCR-R02@v2 Normative Task-Intent Identity

This package is the model half of the canonical `task-intent/v1` identity introduced by
`CCR-R02@v2` (`requirements/CCR-R02-v2-normative-task-intent-identity.md`): closeout evidence must
bind a separate versioned normative task-intent identity that changes only for an obligation or
implementation-plan change, not for progress, lifecycle, acceptance, or audit-only edits. The
bounded `MissingTaskIntent` typed sentinel preserves the only mutation path capable of republishing
legacy containers while granting them no semantic or acceptance authority; the retirement census in
`worktrees/integration/closeout/task_intent_legacy_census.py` removes the compatibility decoder when
every record class reaches zero.

The canonical identity contract comes from the approved requirement packet
(requirements/CCR-R02-v2-normative-task-intent-identity.md, "Closeout evidence must bind a
separate, versioned normative task-intent identity"): closeout evidence binds one
versioned normative identity that changes only for an obligation or implementation-plan
change. The legacy sentinel rules ("Only the legacy persisted-record decoder/currentness
boundary may materialize a typed missing-intent sentinel") keep absence distinct from
identity and allow materialization only at the decode boundary.


## 260831-CCR-L25 Successor Repair

The sealed L02 Attempt-10 candidate, carried forward to landed state under L25 (commit `99dc249b`),
includes this new package cit:([`TaskIntentIdentity`], mcp/src/agents_remember/models/task_intent/__init__.py:55-62); the
package is verified at that landed commit. See `notes/reports/260831-CCR-L25-worker-delivery.md`.

## Update History

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact identity-contract rows as prose (absolute task artifact paths are not repo-relative citations).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  created this card for the new typed task-intent slot/identity model package (`TASK_INTENT_SCHEMA`,
  `ApprovedRequirementPacketRef`, `AcceptanceObligationQuestion`, `TaskIntentIdentity`,
  `MissingTaskIntent`, `TaskIntentState`, `require_task_intent_identity`); documented the
  sentinel-is-absence boundary, the decode-boundary-only materialization rule, and the shared
  vocabulary consumers. Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.
