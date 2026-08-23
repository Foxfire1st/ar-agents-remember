# mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Exhaustiveness suite for advertised tool vocabulary, worktree-contract degradation, and wire recovery guidance.

## Code Commentary

### Logic

The agent-session vocabulary contains structural dispatch, child retirement/rename, parent/child messaging, and self rename while exact-id session tools are absent. Contract readers degrade known cells explicitly, writers remain strict, and every refusal names its contract source.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Public vocabulary must remain structural and exhaustive; exact occupant, gate, lifecycle, and leaf-address tools cannot survive as aliases.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `AdvertisedVocabularyTests` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:49-118 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_the_workflow_kinds_advertised_and_declared_are_the_same_set`, `test_agent_session_tools_are_structural_and_exact_id_tools_are_absent`, `test_every_memory_mode_the_contract_accepts_validates_on_both_fields`, `test_it_emits_the_same_keys_in_the_same_order`. The L2 additions pin the closed public response/control vocabulary, exhaustive registration, and the absence of private operation ids or ad hoc lower-layer exception projection.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_the_workflow_kinds_advertised_and_declared_are_the_same_set`, `test_agent_session_tools_are_structural_and_exact_id_tools_are_absent`, `test_every_memory_mode_the_contract_accepts_validates_on_both_fields`, `test_it_emits_the_same_keys_in_the_same_order`. | L52-L69; L71-L104; L106-L118; L130-L140 | `mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-11T19:58+02:00 — Reconciled `test_wire_vocabulary_exhaustiveness_boundary.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
