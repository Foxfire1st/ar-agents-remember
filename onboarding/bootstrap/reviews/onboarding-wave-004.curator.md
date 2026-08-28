# PDLS Onboarding Wave 004 Curator Review

| Field | Value |
| --- | --- |
| repo | agents-remember |
| reviewed | 2026-08-25T08:54+02:00 |
| waveManifest | `bootstrap/waves/onboarding-wave-004.md` |
| status | pass — emergency-recovery scope |
| source commit | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| source tree | `65a8c5fcae3551dd596421d6cb0c56a4ca64bc0d` |

## Summary

Wave 004 reconciles the onboarding slice to the exact code tree emergency-landed before WSL
compaction. Twenty behavior-preserving source moves retain their prior sidecar knowledge at the new
one-to-one paths, while five newly extracted high-risk owners receive full sidecars and worker
cards. This review passes the onboarding recovery delta only; it does not certify the red Dagger
result or declare lifecycle closeout complete.

## Files Reviewed

| Onboarding File | Source Route/File | Result |
| --- | --- | --- |
| `mcp/src/agents_remember/application/memory_quality/controller.py.md` | `mcp/src/agents_remember/application/memory_quality/controller.py` | pass — moved |
| `mcp/src/agents_remember/application/memory_quality/runs.py.md` | `mcp/src/agents_remember/application/memory_quality/runs.py` | pass — moved |
| `mcp/src/agents_remember/models/closeout/input.py.md` | `mcp/src/agents_remember/models/closeout/input.py` | pass — moved |
| `mcp/src/agents_remember/models/closeout/projection.py.md` | `mcp/src/agents_remember/models/closeout/projection.py` | pass — moved |
| `mcp/src/agents_remember/models/closeout/source.py.md` | `mcp/src/agents_remember/models/closeout/source.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/closeout/door.py.md` | `mcp/src/agents_remember/worktrees/integration/closeout/door.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/closeout/door_control.py.md` | `mcp/src/agents_remember/worktrees/integration/closeout/door_control.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py.md` | `mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/closeout/door_source.py.md` | `mcp/src/agents_remember/worktrees/integration/closeout/door_source.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/closeout/initial_door_recovery.py.md` | `mcp/src/agents_remember/worktrees/integration/closeout/initial_door_recovery.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/closeout/ledger_recovery.py.md` | `mcp/src/agents_remember/worktrees/integration/closeout/ledger_recovery.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py.md` | `mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py.md` | `mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/launch.py.md` | `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/launch.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/state.py.md` | `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/state.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py.md` | `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py.md` | `mcp/src/agents_remember/worktrees/modules/quality/clean_executor.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/modules/quality/closeout_memory.py.md` | `mcp/src/agents_remember/worktrees/modules/quality/closeout_memory.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/modules/quality/gate.py.md` | `mcp/src/agents_remember/worktrees/modules/quality/gate.py` | pass — moved |
| `mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py.md` | `mcp/src/agents_remember/worktrees/modules/quality/published_manifest.py` | pass — moved |
| `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py.md` | `mcp/test_support/agents_remember_test_support/code_quality/check_cli.py` | pass — new owner |
| `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py.md` | `mcp/src/agents_remember/worktrees/integration/lifecycle/control/cancellation.py` | pass — new owner |
| `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py.md` | `mcp/src/agents_remember/worktrees/integration/lifecycle/observation/projection.py` | pass — new owner |
| `mcp/tests/task_reopen_test_support.py.md` | `mcp/tests/task_reopen_test_support.py` | pass — new owner |
| `mcp/tests/_quality_evidence_fixture.py.md` | `mcp/tests/_quality_evidence_fixture.py` | pass — new owner |

## Compliance Checklist

| Check | Result | Notes |
| --- | --- | --- |
| Durable overview placement is route-local and mirrored | pass | Existing parent governance is preserved across package splits. |
| File-level onboarding is strict 1-to-1 | pass | Twenty moved and five new sidecars map to existing final source paths. |
| File onboarding backlinks to nearest governing overview | pass | All new/moved sidecars retain a governing backlink. |
| Overview downlinks list governed files | pass | Parent overview and generated route projections name the final owners. |
| Durable onboarding contains no task-local planning | pass | Stable ownership, failure, and invariant knowledge only. |
| Docs References cite direct evidence | pass | No external specification is claimed for these repository-owned boundaries. |
| Repo-Internal References use same-repo evidence only | pass | Scoped range check resolved 263 citations. |
| Cross-Repo References prove real boundaries | pass | Draft same-repo claims were removed from the cross-repo bucket. |
| No `system/sources.md` registry rows used as proof | pass | Registry is inventory only. |
| No embedding hit cited as proof | pass | Direct final source was used. |
| No absolute filesystem paths | pass | Durable documents use repository-relative paths. |
| Update History is append-only | pass | Moved history is preserved and the newest recovery entry is prepended. |
| LOW-confidence claims are not stated as facts | pass | No unresolved LOW-confidence claim remains. |
| Deferred files are recorded | pass | Package markers, ordinary forcing tests, and TOML manifests are explicit in the coverage plan. |
| STATE.md updated | pass | Exact source, scope, checks, and certification boundary recorded. |

## Reference Health

The first draft scope used plain porcelain status, which collapsed untracked directories and was
discarded because it enumerated only 29 documents. The corrected
`--untracked-files=all` scope covers all 54 changed onboarding documents. Its first pass returned
19 move/split findings; one complete delta repair reduced that same scope to zero across 68
evidence tables, 215 rows, and 353 resolved citations. Whole-tree diff-marker, entity-alignment,
history-order, and table-shape checks each report zero findings across 1,911 Markdown documents
(entity alignment checks the one catalog). All 66 route indexes are current with zero stale
indexes.

## Bucket Corrections

| Claim | Current Bucket | Correct Bucket | Reason |
| --- | --- | --- | --- |
| Cancellation and observation use configured contract/enclosure authority. | Draft Cross-Repo | Repo-Internal | The proving sources and authority are inside this repository. |
| Temporary external-memory fixture setup is a cross-repository boundary. | Draft Cross-Repo | No cross-repo claim | The helper creates temporary same-test-world directories, not an adjacent repository contract. |

## Required Fixes

None in the wave-owned onboarding delta.

## Developer Questions

None. The developer already authorized the emergency memory and ledger recovery checkpoint.

## Next-Wave Recommendation

Hold onboarding expansion. Land this recovery checkpoint, then repair the retained Dagger failures
through the master lifecycle. Do not treat this curator pass as source acceptance.
