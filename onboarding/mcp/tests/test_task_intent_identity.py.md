# mcp/tests/test_task_intent_identity.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_task_intent_identity.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00                  |
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks task-intent identity across step obligations versus progress/audit metadata. Exact task-document location participates in identity; typed packet references are supplemental and version-addressed, while approval-looking prose cannot manufacture authority. Duplicate packet metadata refuses as ambiguous. This is the retained subset, not the old exhaustive root-field mutation census.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every step obligation field changes intent | `test_every_step_obligation_field_changes_intent` | mcp/tests/test_task_intent_identity.py:81-88 |
| Every step progress or audit field is excluded | `test_every_step_progress_or_audit_field_is_excluded` | mcp/tests/test_task_intent_identity.py:104-110 |
| Task document ref is part of leaf identity | `test_task_document_ref_is_part_of_leaf_identity` | mcp/tests/test_task_intent_identity.py:113-117 |
| Typed approved packet refs are supplemental and version addressed | `test_typed_approved_packet_refs_are_supplemental_and_version_addressed` | mcp/tests/test_task_intent_identity.py:157-183 |
| Packet approval prose is non authoritative identity invariant | `test_packet_approval_prose_is_non_authoritative_identity_invariant` | mcp/tests/test_task_intent_identity.py:205-219 |
| Approval like prose cannot create a typed packet reference | `test_approval_like_prose_cannot_create_a_typed_packet_reference` | mcp/tests/test_task_intent_identity.py:222-230 |
| Duplicate packet metadata refuses as ambiguous | `test_duplicate_packet_metadata_refuses_as_ambiguous` | mcp/tests/test_task_intent_identity.py:233-249 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  created this card for the new canonical task-intent identity/mutation matrix suite; documented
  the per-field mutation expectations, the packet-ref matrix, and the allowlist symmetry refusals.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.
