# mcp/tests/test_lifecycle_status_wait_outcomes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_status_wait_outcomes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `e375f2ebdc87f6843bc76168b646d606fa79caec` |
| lastVerifiedCommitDate | 2026-09-04T20:19:44+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Verifies the typed outcomes of lifecycle status waiting: meaningful change, unchanged timeout, successor generation and precise read-only refusals.

## Code Commentary

### Logic

Self-contained fixtures create a claimed lifecycle generation and durable task/door context. The tests establish that a wrong cursor refuses before reading a journal; absent, malformed, replaced or wrong-generation journals cannot silently redirect the waiter. Meaningful change ignores heartbeat/noise fields and produces a new cursor, while a proven successor explicitly identifies the successor generation.

Application cases require typed refusals to recommend only the exact read-only status snapshot. Bad paths, unpublished locators, incoherent projections and unproved successor archives are refused. A missing optional observed projection can be omitted without inventing an operation envelope.

### Conventions

Keep fixtures self-contained under the evidence-lifecycle isolation rule. Synthetic scheduling doors stand in for below-queue lifecycle setup; they are not production scheduling proof.

### Invariants And Boundaries

- Waiting never admits, resumes, cancels or mutates an operation.
- Wrong identity and unreadable authority remain typed refusals.
- Heartbeat-only changes do not count as meaningful progress.
- Public results expose bounded status/cursor information, not private process or operation identifiers.

### Todos

No source behavior changed in this documentation repair.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Cursor/journal refusals and meaningful-change classification | `test_wrong_cursor_is_refused_before_any_journal_read`; `test_no_operation_refuses_typed_when_journal_is_absent`; `test_malformed_journal_is_a_typed_unreadable_refusal`; `test_meaningful_classification_ignores_noise_and_flags_meaningful_fields` | mcp/tests/test_lifecycle_status_wait_outcomes.py:538-621 |
| Timeout, change and explicit successor outcomes | `test_wait_reports_unchanged_timeout_without_failure`; `test_wait_reports_changed_with_next_cursor_after_meaningful_advance`; `test_generation_successor_wakes_old_wait_with_explicit_information`; `test_unproven_successor_archive_refuses_wrong_generation` | mcp/tests/test_lifecycle_status_wait_outcomes.py:624-750 |
| Read-only application refusal guidance | `test_application_refusals_never_recommend_mutation`; `test_application_incoherent_projection_is_a_read_only_refusal` | mcp/tests/test_lifecycle_status_wait_outcomes.py:753-953 |
| Optional projection, successor archive validation and registered response shape | `test_coherent_payload_omits_projection_when_observation_is_unavailable`; `test_unproven_successor_archive_variants_refuse_wrong_generation`; `test_wait_tool_is_registered_and_response_model_is_typed` | mcp/tests/test_lifecycle_status_wait_outcomes.py:976-1059 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Repaired literal template markers and restored canonical sections/references while retaining the read-only wait and explicit-successor contract. Historical leaf-pass wording below is retained as history; this refresh establishes documentation currentness only.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): created
  this card for the new status-wait test module.
