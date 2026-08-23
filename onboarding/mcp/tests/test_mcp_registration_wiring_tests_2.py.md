# mcp/tests/test_mcp_registration_wiring_tests_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_mcp_registration_wiring_tests_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Registration wiring suite for worktree, task-document, lifecycle, and structural gate tools.

## Code Commentary

L23 proves `worktree_operation_cancel` forwards only the task address, operation kind, developer intent, and dry-run choice—never an operation ID.

### Logic

The suite pins closeout message grouping, task-document edit/read shapes, ambient lifecycle signals,
structural lifecycle-gate raise, and `gate_decide` by canonical document plus kind without a gate
id. Its closeout-queue case invokes the live registration, verifies the configuration identity,
and proves the wire request is validated into the strict status action and canonical sprint ref.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the registered or owning seam directly.

### Invariants And Boundaries

Registration must not reintroduce exact gate, lifecycle, or occupant addressing; application composition owns authority and refusal.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `RegistrationWiringTests2` | mcp/tests/test_mcp_registration_wiring_tests_2.py:6-591 |
| Closeout-queue registration validates and forwards the canonical request model. | `test_closeout_queue_registration_validates_and_forwards_the_request` | mcp/tests/test_mcp_registration_wiring_tests_2.py:30-49 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## 260821-CLIVE-L1 Public Wiring Coverage

Registration assertions now include worktree and direct-landing message fields plus structured refusal/effective-input response fields. Optional JSON-schema fields remain runtime-required when their resolved legs are enabled; the suite does not imply blank-message compatibility.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_worktree_enclosure_adopt_forwards_exact_preview_binding`, `test_closeout_queue_registration_validates_and_forwards_the_request`, `test_worktree_operation_control_forwards_exact_generation_request`, `test_worktree_start_defaults_to_a_real_light_task_start`. The L2 additions pin the closed public response/control vocabulary, exhaustive registration, and the absence of private operation ids or ad hoc lower-layer exception projection.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_worktree_enclosure_adopt_forwards_exact_preview_binding`, `test_closeout_queue_registration_validates_and_forwards_the_request`, `test_worktree_operation_control_forwards_exact_generation_request`, `test_worktree_start_defaults_to_a_real_light_task_start`. | L7-L28; L30-L49; L51-L82; L84-L101 | `mcp/tests/test_mcp_registration_wiring_tests_2.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: wiring/conformance updates for the declared-caller
  gate parameters and the `direct_landing` registration. Verified at code commit a9d50e08.


- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: invokes the live FastMCP
  `closeout_queue` registration, proves request validation into the strict model, and verifies
  the unchanged handler sentinel and loaded configuration.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_mcp_registration_wiring_tests_2.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the `include_terminal` poll kwarg
  pin (N11) and the `operator_inbox_supersede` wiring test (R11). Verification metadata pinned
  until closeout stamps the 260713-TES-L4 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
