# mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
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
| Current suite declaration anchoring this card. | `AdvertisedVocabularyTests` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:43-43 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `test_wire_vocabulary_exhaustiveness_boundary.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
