# mcp/tests/test_spawn_agent_session_resolution.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_spawn_agent_session_resolution.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Regression suite for harness/profile resolution and the lower-level terminal paste endpoint.

## Code Commentary

### Logic

Repository-local launch preferences resolve from canonical task-document repository identity; unbound internal spawn uses global settings. Legacy direct harness overrides fail, registry absence is explicit, and paste delivery uses transport evidence without becoming structural dispatch authority.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Settings own profile selection; missing or conflicting selection fails loud; terminal paste is not an exact-id agent tool.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `SpawnHarnessResolutionTests` | mcp/tests/test_spawn_agent_session_resolution.py:34-34 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `test_spawn_agent_session_resolution.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
