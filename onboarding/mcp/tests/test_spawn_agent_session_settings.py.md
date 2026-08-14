# mcp/tests/test_spawn_agent_session_settings.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_spawn_agent_session_settings.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Regression suite for configured harness definitions, role/level knob precedence, and override refusal.

## Code Commentary

### Logic

Cases prove repository-local task context selects the right settings layer, level and role defaults deep-merge deterministically, declared vocabularies validate model/effort, free-form knobs flow only from settings, and legacy arguments/environment overrides are refused.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the owning seam directly.

### Invariants And Boundaries

Callers never select harness/model/effort; provenance records the settings-owned resolution used by the plane-private spawn stage.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `_role_ref` | mcp/tests/test_spawn_agent_session_settings.py:36-46 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## L23 Settings Fixture Admission

Harness-settings and spawn-level cases seed current task-derived lineage before
testing settings-owned selection. This keeps launch knob assertions independent
from, but compatible with, fail-closed structural admission.

## Update History
- 2026-08-12T20:10+02:00 — L23 curator: documented current-lineage setup for settings-driven spawn tests; verification remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 expressed the fixture's existing role-to-task-altitude mapping as one lookup table; the settings and refusal contract is unchanged.
- 2026-08-11T19:58+02:00 — Reconciled `test_spawn_agent_session_settings.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
