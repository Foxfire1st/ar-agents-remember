# mcp/tests/test_task_intent_identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_intent_identity.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-03T12:30:00+02:00                  |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00                  |
| governingOverview      | `overview.md`                             |

## Governing Overview

[test suite overview](overview.md)

## Purpose

Canonical task-intent projection, mutation, and packet-ref matrices for the `task-intent/v1`
identity (CCR-R02@v2). Every root and nested task field carries an explicit intent mutation
expectation; step obligation fields change the digest while progress/audit fields do not; approval
prose is proven non-authoritative; and approved packet refs are supplemental and version-addressed
only.

## Code Commentary

### Logic

- `test_every_root_task_field_has_an_explicit_intent_mutation_expectation` (line 92) walks the
  full root field surface with an explicit change/stable judgment per field, and
  `test_every_step_obligation_field_changes_intent` / `test_every_step_progress_or_audit_field_is_excluded`
  do the same for step and substep fields (lines 174, 197, 207, 229, 243).
- `test_decisions_sections_and_ordinary_questions_cannot_opt_into_intent` (line 250) proves
  decision prose and generic questions never alter the identity.
- `test_task_document_ref_is_part_of_leaf_identity` (line 279) pins repository-qualified ref
  membership in the leaf identity.
- The typed approved-packet rows (lines 323-475) prove supplemental, version-addressed resolution,
  the metadata/readability/version-match refusal matrix, endorsement of the `Requirement ID`
  header, and that approval-like prose alone cannot create a typed reference; duplicate packet
  metadata refuses as ambiguous.
- `test_allowlisted_slot_without_shared_taxonomy_membership_refuses` (line 494) and
  `test_taxonomy_cannot_opt_a_new_slot_into_v1_without_schema_revision` (line 505) force the
  allowlist/taxonomy symmetry boundary.
- `test_projection_refuses_master_and_translates_internal_schema_failures` (line 539) and
  `test_projection_translates_both_shared_taxonomy_error_boundaries` (line 553) prove the facade
  error dialect at the public seam.
- `test_packet_metadata_may_end_at_eof_and_identity_fact_uses_wire_alias` (line 577) pins the
  EOF-terminated metadata parser and by-alias wire fact.

### Conventions

Helpers build a canonical subTask document and a typed `ResolvedTaskDocument` candidate; tests
invoke the production projection/identity owners directly and the reader projection for typed-form
coverage.

### Invariants And Boundaries

- Each field mutation expectation stays explicit; no unlisted field silently falls to a default.
- Approval prose is exact text only and can never mint an intent digest or a typed reference.
- Master documents and unsupported schema versions refuse before any digest.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Full root-field intent mutation matrix. | `test_every_root_task_field_has_an_explicit_intent_mutation_expectation` | mcp/tests/test_task_intent_identity.py:92-172 |
| Step/substep obligation vs progress/audit field matrices. | `test_every_step_obligation_field_changes_intent`; `test_every_step_progress_or_audit_field_is_excluded` | mcp/tests/test_task_intent_identity.py:174-195; mcp/tests/test_task_intent_identity.py:197-206 |
| Approved packet resolution, refusal matrix, and prose non-authority rows. | `test_typed_approved_packet_refs_are_supplemental_and_version_addressed`; `test_packet_ref_failure_matrix`; `test_approval_like_prose_cannot_create_a_typed_packet_reference` | mcp/tests/test_task_intent_identity.py:323-350; mcp/tests/test_task_intent_identity.py:374-393; mcp/tests/test_task_intent_identity.py:464-473 |
| Allowlist/taxonomy symmetry refusals. | `test_allowlisted_slot_without_shared_taxonomy_membership_refuses`; `test_taxonomy_cannot_opt_a_new_slot_into_v1_without_schema_revision` | mcp/tests/test_task_intent_identity.py:494-503; mcp/tests/test_task_intent_identity.py:505-515 |
| The projection/identity owners under test. | `task_intent_projection`; `task_intent_identity` | mcp/src/agents_remember/tasks/task_intent.py:132-177; mcp/src/agents_remember/tasks/task_intent.py:180-193 |

## CCR-R02@v2 Normative Task-Intent Identity

This suite is the mutation-matrix verification evidence class required by CCR-R02@v2
(`requirements/CCR-R02-v2-normative-task-intent-identity.md`): obligation changes stale the
digest, audit/progress edits do not, and unclassified fields or missing requirement refs fail
closed. Part of the landed L25 candidate (`99dc249b`).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  created this card for the new canonical task-intent identity/mutation matrix suite; documented
  the per-field mutation expectations, the packet-ref matrix, and the allowlist symmetry refusals.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.
