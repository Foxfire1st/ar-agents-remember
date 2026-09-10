# mcp/tests/test_closeout_certification_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_certification_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:45+02:00|
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532` |
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises owner-derived R05 certification recovery decisions through real plan, result, certificate, and selected-reuse compilers. The suite distinguishes exact input deltas, unchanged interruption reuse, prior-red catalog requirements, and retained evidence mismatch refusal.

## Code Commentary

### Logic

`_snapshot`, `_catalog`, and `_chain` build exact fixture authority. The retained tests select only the required suffix after a gate-input change, reject reuse after code change, preserve exact certificates across unchanged interruption, and require complete prior-red evidence before recovery.

### Invariants And Boundaries

- Recovery decisions derive from immutable candidate/profile/plan evidence.
- Unchanged interruption reuses the exact original prefix; changed inputs reopen the required suffix.
- Prior-red recovery refuses missing, reordered, or mismatched original evidence.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Recovery behavior is repository-owned by the exact retained tests. | `test_actual_gate_input_delta_selects_only_its_required_suffix` | mcp/tests/test_closeout_certification_recovery.py:230-244 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Snapshot and certificate fixtures bind exact recovery inputs. | `_snapshot`; `_catalog`; `_chain` | mcp/tests/test_closeout_certification_recovery.py:87-226 |
| Gate input deltas reopen only their required suffix. | `test_actual_gate_input_delta_selects_only_its_required_suffix`; `test_code_change_invalidates_all_gates_and_does_not_reuse_old_certificates`; `test_unchanged_interruption_reuses_the_original_exact_certificates` | mcp/tests/test_closeout_certification_recovery.py:230-267 |
| Prior-red recovery requires the exact original catalog and evidence dependencies. | `test_prior_red_requires_every_independent_root_and_blocked_dependant`; `test_prior_red_gate_two_requires_the_exact_original_gate_one_certificate`; `test_retained_report_inventory_refuses_mismatched_evidence_before_any_source_read` | mcp/tests/test_closeout_certification_recovery.py:456-473; mcp/tests/test_closeout_certification_recovery.py:616-652; mcp/tests/test_closeout_certification_recovery.py:794-823 |

## Cross-Repo References

None; the tests use local certification owners.

## Update History

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent test sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `12b41cb717bd56605d95625e5a16f0719204a22d34da3258ea117b7114e68cf9`). No test execution or future candidate verification stamp is claimed.
