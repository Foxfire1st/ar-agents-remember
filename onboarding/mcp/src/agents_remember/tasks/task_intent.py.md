# mcp/src/agents_remember/tasks/task_intent.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/task_intent.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-03T12:30:00+02:00                  |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00                  |
| governingOverview      | `overview.md`                             |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Canonical normative task-intent projection and identity for one leaf task document (CCR-R02@v2).
The module turns an already-resolved task document into a strict `task-intent/v1` projection
containing only explicitly allowlisted normative slots, hashes that canonical JSON into the
SHA-256 intent digest, and provides the single currentness assertion
(`require_current_task_intent`) that closeout, door, and lifecycle consumers call before any
evidence reuse.

## Code Commentary

### Logic

The projection operates on `ResolvedTaskDocument` (never on raw paths or prose) and reads the
shared exhaustive field taxonomy from `document_field_effects.py`:

- `TaskIntentV1` (line 88) is the strict frozen projection: `schema: task-intent/v1`, the leaf
  identity, objective, requirement texts or approved packet refs, design, allowed step/substep
  obligation text, normative code examples, `codeExamplesNote`, and typed acceptance obligations.
  Generic freeform sections, comments, notes, decisions, progress, lifecycle, and audit fields are
  never projected; `canonical_value` (line 101) emits the by-alias JSON for hashing.
- `_ROOT_FIELDS` (line 105) / `_NESTED_FIELDS` (line 122) enumerate exactly which
  `TaskDocument`/nested-model fields task-intent/v1 consumes; `_validate_allowlisted_classifications`
  (line 239) refuses both a slot missing its normative taxonomy membership and a taxonomy-normative
  slot outside the projection, so projecting can never silently drop a newly classified field.
- `task_intent_projection` (line 132) refuses a master (`task-intent-leaf-required`), requires
  the supported schema version, and translates taxonomy failures into
  `task-intent-schema-unclassified`.
- `task_intent_identity` (line 180) hashes the canonical projection with
  `json.dumps(sort_keys=True, separators=(",", ":"))` into a 64-hex digest, producing
  `TaskIntentIdentity`.
- `require_current_task_intent` (line 196) reuses the model-layer rejection seam and raises
  `{owner}-task-intent-stale` when the observed identity differs from the current one, with the
  owner-chosen `next_action`.
- `_requirements` (line 259): exact text must be non-blank, and `task-intent/v1` refuses a
  packet-ref replacement of exact task text (`task-intent/v2-cutover-required`). An approved
  packet ref resolves task-root-relative, must be a Markdown file inside the task root, must be
  readable, and its structured `Stable ID`/`Version` metadata must match exactly
  (`_approved_packet_ref` line 283, `_packet_metadata` line 316); duplicate metadata fields
  refuse as ambiguous.
- `_acceptance_obligations` (line 336) projects only questions typed as
  `AcceptanceObligationQuestion`.

### Conventions

The projection is never a whole-document hash and never a digest of decision prose. New normative
slots require both a schema revision and a taxonomy classification; the pair is enforced at
projection time.

### Invariants And Boundaries

- Only allowlisted normative slots change the digest; step status, decisions, timestamps, audit
  prose, lifecycle id, enclosures, evidence, and status notes are excluded by construction.
- An approved requirement packet ref is authoritative only after confined path/readability,
  unambiguous metadata, and exact id/version checks; approval-like prose alone cannot create a
  typed reference.
- Integration generations do not carry leaf task intent; this module is leaf-only.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict allowlisted v1 projection model. | `TaskIntentV1` | mcp/src/agents_remember/tasks/task_intent.py:88-102 |
| Normative slot allowlists for the document and nested models. | `_ROOT_FIELDS`; `_NESTED_FIELDS` | mcp/src/agents_remember/tasks/task_intent.py:105-129 |
| Projection entry point refusing masters and translating taxonomy failures. | `task_intent_projection` | mcp/src/agents_remember/tasks/task_intent.py:132-177 |
| Canonical digest production from the projection. | `task_intent_identity` | mcp/src/agents_remember/tasks/task_intent.py:180-193 |
| Currentness/staleness assertion for owners. | `require_current_task_intent` | mcp/src/agents_remember/tasks/task_intent.py:196-214 |
| Allowlist/taxonomy symmetry enforcement. | `_validate_allowlisted_classifications` | mcp/src/agents_remember/tasks/task_intent.py:239-256 |
| Requirement text/packet handling and the v2-cutover refusal. | `_requirements`; `_approved_packet_ref` | mcp/src/agents_remember/tasks/task_intent.py:259-313 |
| The shared exhaustive field-effect taxonomy consumed here. | `TaskDocumentFieldEffect`; `fields_with_effect` | mcp/src/agents_remember/tasks/document_field_effects.py:45-61 |
| The typed slot/identity models imported from the sibling model module. | `TaskIntentIdentity`; `ApprovedRequirementPacketRef` | mcp/src/agents_remember/models/task_intent/__init__.py:55-59; mcp/src/agents_remember/models/task_intent/__init__.py:22-36 |

## CCR-R02@v2 Normative Task-Intent Identity

This module is the projection/identity half of CCR-R02@v2. Its canonical packet
(`requirements/CCR-R02-v2-normative-task-intent-identity.md`) requires closeout evidence to bind
a separate versioned normative task-intent identity that changes only for obligation/plan changes.
The allowlist + shared-taxonomy rule and the "decision prose is audit-only" rule are implemented
here. The L25 delivery verified at `99dc249b` carries the sealed L02 Attempt-10 candidate per
`notes/reports/260831-CCR-L25-worker-delivery.md`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  created this card for the new canonical task-intent projection module (`task_intent_projection`,
  `task_intent_identity`, `require_current_task_intent`, allowlist/taxonomy symmetry checks,
  approved-packet resolution); documented the leaf-only and never-a-whole-document-hash boundaries.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.
