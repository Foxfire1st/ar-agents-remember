# mcp/tests/test_dispatch_agent_ambient.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dispatch_agent_ambient.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash |  `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Ambient versus hosted dispatch identity, role and rollback contracts.

## Code Commentary

### Logic

Unknown task and role-altitude mismatch refuse before spawn. Missing or broken hosted identity cannot downgrade into ambient dispatch. The real spawn primitive with a host double records an ambient architect and durable brief; persistence failure retires the newly created child through system closure. Unauthorized structural children refuse.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Only a proven unbriefed child is eligible for rollback. Host doubles create no real tmux session, and fixture launch settings do not override real authority.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Ambient dispatch refuses unknown task reference before spawn. | `test_ambient_dispatch_refuses_unknown_task_reference_before_spawn` | mcp/tests/test_dispatch_agent_ambient.py:206-223 |
| Ambient dispatch refuses role altitude mismatch before spawn. | `test_ambient_dispatch_refuses_role_altitude_mismatch_before_spawn` | mcp/tests/test_dispatch_agent_ambient.py:225-240 |
| Role without hosted identity never falls back to ambient dispatch. | `test_role_without_hosted_identity_never_falls_back_to_ambient_dispatch` | mcp/tests/test_dispatch_agent_ambient.py:242-266 |
| Ambient dispatch runs the real spawn and persists the brief. | `test_ambient_dispatch_runs_the_real_spawn_and_persists_the_brief` | mcp/tests/test_dispatch_agent_ambient.py:268-293 |
| Ambient dispatch rolls back via system closure when brief persistence fails. | `test_ambient_dispatch_rolls_back_via_system_closure_when_brief_persistence_fails` | mcp/tests/test_dispatch_agent_ambient.py:295-324 |
| Plane dispatch refuses broken plane identity without downgrading. | `test_plane_dispatch_refuses_broken_plane_identity_without_downgrading` | mcp/tests/test_dispatch_agent_ambient.py:326-343 |
| Plane dispatch refuses an unauthorized child role. | `test_plane_dispatch_refuses_an_unauthorized_child_role` | mcp/tests/test_dispatch_agent_ambient.py:345-366 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-31T10:56+02:00 — 260821-ARSPAWN-L5 closeout quality repair: received the unchanged
  three-test plane dispatch rollback/refusal cohort from `test_structural_agent_tools.py`; this
  dispatch-focused suite now owns the full ambient/plane caller-mode failure boundary while both
  files remain below the hard size limit. Verification remains closeout-owned.

- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: added both incomplete
  hosted-identity directions and asserted that neither can reach the spawn primitive.
  Verification remains closeout-owned.

- 2026-08-26T16:03+02:00 — Post-failure repair: rebound ambient rollback forcing to the real
  `OperatorInboxStore.append` commit boundary; removed reliance on an obsolete log path. No
  certifying test execution is claimed.


- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: corrected the recovery
  contract so unknown durable state refuses reconciliation and only positively proven unbriefed
  generations authorize rollback; refreshed final-candidate anchors. No test execution is claimed.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: successful ambient dispatch now proves receipt
  binding, and rollback proves observer-log failure is secondary after durable retirement.
  Verification remains closeout-owned.

- 2026-08-21T04:00+02:00 — 260821-ARSPAWN-L1 fix round 4: the real-path cohort now runs against a
  settings-owned architect launch selection (`_write_architect_settings` → temp `system/settings.json`)
  with the `_FakeHost`/`_detected` fixtures, and the real rollback asserts the terminated-row
  listing (`catalog.list(include_terminated=True)`, exactly one `terminated` row matching the fake
  host); reference ranges refreshed for the shifted layout (552 lines). Verification metadata pinned
  until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T03:45+02:00 — 260821-ARSPAWN-L1 fix round 3: the suite grew to 526 lines with the
  real-path cohort — `resolve_ambient_caller` unit tests, real spawn+brief success, real rollback,
  and the rollback failure-branch seams; reference ranges refreshed for the shifted layout.
  Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T03:15+02:00 — 260821-ARSPAWN-L1 fix round 1: created for the new source file after
  the file-size fix moved the six ambient dispatch tests verbatim out of
  `test_structural_agent_tools.py`; the structural suite's card records the relocation. Verification
  metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.
