# PDLS Onboarding Coverage Plan

## Required Coverage

| Route | Required outcome |
| --- | --- |
| repository guidance | Exact-node Python diagnostics are supported and non-certifying; raw host acceptance remains prohibited. |
| `mcp/src/agents_remember/testing` | Route overview and owner cards explain explicit cohort, lifecycle, lanes, cadence, bootstrap, phase, and causal evidence. |
| `mcp/src/agents_remember/code_quality` | Product-only scoring and one dependency graph govern targeted selection, retry, and causal preflight. |
| `mcp/src/agents_remember/models` | Diagnostic/certifying evidence altitude and stable conversation architecture are explicit without the retired snapshot. |
| `mcp/src/agents_remember/application/lifecycle` | Terminalization preserves accepted organizational-repair evidence at one pure owner. |
| `mcp/tests` | Fixture authority, lifecycle catalog, direct cohort, and deleted evidence dispositions are explicit. |
| `.dagger` / hooks / config / docs | Governing repository and testing overviews describe their policy; no duplicate file-level authority is created. |

## Wave 003 High-Risk Coverage

| Source | Sidecar | File card | Disposition |
| --- | --- | --- | --- |
| `testing/cohort_manifest.py` | yes | yes | covered |
| `testing/evidence_lifecycle.py` | yes | yes | covered |
| `testing/evidence_lanes.py` | yes | yes | covered |
| `testing/cadence_runner.py` | yes | yes | covered |
| `testing/causal_failures.py` | yes | yes | covered |
| `code_quality/dependency_ownership.py` | yes | yes | covered |
| `code_quality/causal_preflight.py` | yes | yes | covered |
| `tests/_adapter_event_scripts.py` | yes | yes | covered |
| `tests/_evidence_catalog_fixture.py` | yes | yes | covered |
| `tests/_direct_cohort_candidate.py` | yes | yes | covered |

## Wave 004 Final Ownership-Split Coverage

Wave 004 reconciles the source tree that was actually emergency-landed. Behavior-preserving
package moves retain their existing sidecar prose and history at the new one-to-one source paths;
the five new load-bearing owners receive new sidecars and file cards.

| Source family | Outcome | Disposition |
| --- | --- | --- |
| `application/memory_quality/{controller,runs}.py` | existing sidecars moved | covered |
| `models/closeout/{input,projection,source}.py` | existing sidecars moved | covered |
| `worktrees/integration/closeout/*.py` | eight existing sidecars moved | covered |
| `worktrees/integration/lifecycle/worker/*.py` | three existing sidecars moved | covered |
| `worktrees/modules/quality/*.py` | four existing sidecars moved | covered |
| `code_quality/check_cli.py` | new sidecar and file card | covered |
| `worktrees/integration/lifecycle/control/cancellation.py` | new sidecar and file card | covered |
| `worktrees/integration/lifecycle/observation/projection.py` | new sidecar and file card | covered |
| `tests/task_reopen_test_support.py` | new sidecar and file card | covered |
| `tests/_quality_evidence_fixture.py` | new sidecar and file card | covered |

The new package `__init__.py` markers remain governed by their nearest route overview. They carry
no independent behavior or public authority and therefore do not receive standalone file cards.

## Deliberate Deferrals

New ordinary forcing modules remain routed by `mcp/tests/overview.md` rather than receiving
separate durable cards in this wave: `test_cadence_runner.py`,
`test_causal_failure_localization.py`, `test_causal_quality_preflight.py`,
`test_conversation_model_architecture.py`,
`test_evidence_lanes.py`, and `test_evidence_lifecycle.py`. They assert the documented owners
and carry no independent runtime authority. Changed pre-existing tests retain their existing route
coverage. TOML manifests are documented by their consuming owner cards and the testing overview.

## Deleted-Slice Cleanup

The sidecars for `dependency_closure.py`, `python_source.py`, and
`collection_closure.py` are deleted with the rejected generic analyzer. The sidecars for the
retired model-split test/snapshot and rich-sim generator/self-test are also deleted. Useful stable
architecture and contract knowledge is preserved at current behavior owners.

## Validation

1. Added high-risk source/support files have exact sidecars and file cards.
2. Deleted source has no live sidecar, citation, compatibility reader, or generated route.
3. Governing overviews and `system/tools.md` agree on diagnostic versus acceptance authority.
4. Reference targets exist, update history names supersession or preservation, and verification
   metadata names the emergency-landed source commit without implying Dagger certification.
5. Route indexes are regenerated only after the content tree is final, then a dry run is current.
