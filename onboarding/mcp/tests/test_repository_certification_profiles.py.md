# mcp/tests/test_repository_certification_profiles.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_repository_certification_profiles.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Forcing suite for the repository-owned certification profile contract: two-language distinct
fixture profiles compile the same four-gate protocol, the Agents Remember profile preserves its
complete approved gate inventory, selection/plan identity is digest-bound and reorder-stable, and
the L19 selector-result contract is canonical and content-addressed.

## Code Commentary

### Logic

The suite builds profiles through `repository_profile_test_support` and exercises admission,
plan compilation, gate-identity stability, semantic-input closures, and every noncanonical refusal
branch. L19 additions force the v2 selector-result contract directly: the result digest binds
candidate/population/reasons/outputs and changes under any candidate edit; unreasoned outputs and
targeted-to-full expansion refuse; declared external selector inputs change the profile digest; and
the Node and Rust fixture scripts emit `repository-selector-result/v2` JSON accepted by
`RepositorySelectionResult.model_validate_json`. The agents-remember profile's selector
configuration digest is asserted equal to `profile_selection.ownership_configuration_digest()`.

The teardown refusal case invokes the current two-path adapter with a proof destination and a passed summary whose report contains no cleanup checkpoint. It must still reject that report; supplying an output path does not make missing observations valid. Producer-backed positive and negative proof publication is covered in the adjacent rail-evidence suite.

The full-scope regression builds the actual repository selector result and executable `_profile_config` with Dagger admission, compares canonical string-ordered populations and the selection digest, and explicitly alters the executable scope with one missing, extra or duplicate path. All three altered populations must refuse at `_require_exact_scope`; the unchanged population succeeds without launching pytest from the fixture.

### Conventions

Fixture profile compilation and in-process owner execution are distinct from live Dagger certification.

### Invariants And Boundaries

- Canonical digests are deterministic across reorderings; every digest mismatch refuses.
- Later-gate edits retain earlier-gate plan identities (the aggregate profile digest is excluded
  from per-gate semantic identity).
- A selector result must reason every output and never broaden a targeted result to full.
- The suite exercises production owners through the shared fixture builder.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| Node and Rust fixtures use the same generic protocol. | `test_two_language_distinct_repositories_compile_the_same_four_gate_protocol` | mcp/tests/test_repository_certification_profiles.py:106-131 |
| The real profile inventory and selector configuration digest are asserted. | `test_agents_remember_profile_preserves_the_complete_approved_gate_inventory` | mcp/tests/test_repository_certification_profiles.py:153-172 |
| Profile edits invalidate the associated identities. | `test_profile_edit_changes_profile_and_plan_identity` | mcp/tests/test_repository_certification_profiles.py:264-301 |
| Later-gate changes preserve independent earlier-gate identity. | `test_later_gate_edit_retains_earlier_gate_plan_identities` | mcp/tests/test_repository_certification_profiles.py:304-336 |
| Selector identity binds candidate, population, reasons and output. | `test_selector_result_digest_binds_candidate_population_reasons_and_outputs` | mcp/tests/test_repository_certification_profiles.py:571-601 |
| Unreasoned output and targeted expansion refuse. | `test_selector_result_refuses_unreasoned_output_and_targeted_full_expansion` | mcp/tests/test_repository_certification_profiles.py:604-640 |
| External selector input declarations are digest-bound. | `test_profile_digest_binds_declared_external_selector_inputs` | mcp/tests/test_repository_certification_profiles.py:643-650 |
| Non-Python scripts produce the canonical selection schema. | `test_non_python_selector_fixture_emits_the_canonical_generic_result` | mcp/tests/test_repository_certification_profiles.py:653-686 |
| The current proof-writing adapter still refuses a report with no passing cleanup checkpoint. | `test_repository_profile_teardown_adapter_requires_a_passing_cleanup_checkpoint` | mcp/tests/test_repository_certification_profiles.py:689-707 |
| Actual full selector/configuration accept equal populations and refuse missing, extra or duplicate executable paths. | `test_full_python_rail_uses_canonical_selector_order_and_still_refuses_scope_drift` | mcp/tests/test_repository_certification_profiles.py:930-968 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Added the four-case full selector ordering regression and refreshed exact current source anchors without importing later L33 applicability behavior. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Reconciled the teardown proof-output argument without relaxing the missing-checkpoint refusal, and replaced stale task-document citations with exact repository test evidence.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 v2 selector-result forcing — digest binding, unreasoned-output/targeted-full refusals,
  external-input digest coupling, identity-bound fixture emission, and the ownership
  configuration-digest equality assertion. Verification is pinned to the owning commit.
