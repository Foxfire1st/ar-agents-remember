# mcp/tests/integration_certification_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/integration_certification_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:46:49+00:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides real integration journal ownership and physically published original code-certification objects for focused tests. A separate helper supplies wire-shape references only, so callers can choose the authority boundary their assertions require.

## Code Commentary

### Logic

The former `integration_fixture` helper -- which created a Git repository, installed the requested generic profile with the 128 KiB result-document bound, and started the durable integration operation through `OperationRuntime` -- was deleted as unreachable: it had no consumer, and the detached lifecycle worker it drove no longer exists. The surviving fixture surface is `selected_code_fixture` and `structural_quality_references`, while production integration certification ownership remains `IntegrationCertificationOwner`.

`selected_code_fixture` creates a real checkout with the repository profile, derives its candidate lane, freezes the full run and persists admission. The shared injected outcome factory supplies code-rail results while actual publication owners write and reopen the result document. `record_published_generation` constructs original typed terminal references and the fixture requires no recording refusal. This is physical object/publication composition, not ordinary-suite execution in Dagger.

`render` calls the selected-certification renderer with those supplied originals, the fixture HEAD comparison base and frozen mode. `structural_quality_references` instead constructs deterministic small reference dictionaries and an empty canonical publication object for model-shape tests; it issues no backing objects or accepted certificates.

### Conventions

The journal fixture uses a caller-owned contract factory; the renderer fixture owns its repository and report generation. Fixture profile bounds are fixed before admission and do not change shipped profile configuration.

### Invariants And Boundaries

- Integration ownership comes from an actual started runtime and durable store.
- Selected renderer inputs retain the original frozen run, terminals and physical publication bytes.
- Injected code execution and shape-only dictionaries remain distinct from original stored evidence.
- Integration setup does not establish organizational completion or final memory acceptance.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source governs this file. | N/A | N/A |

## Repo-Internal References

These source anchors establish the actual owner calls, fixture inputs and execution limits described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The former runtime-owned integration fixture (`integration_fixture`/`IntegrationFixture`) was deleted as unreachable: it had no consumer, and the detached lifecycle worker whose `OperationRuntime` supplied its running record is gone. The surviving real-object fixture in this module is `selected_code_fixture`. | `selected_code_fixture` | mcp/tests/integration_certification_test_support.py:42-77 |
| The selected fixture retains one target, prepared run and ordered original terminals. | `SelectedCodeFixture` | mcp/tests/integration_certification_test_support.py:26-39 |
| Rendering consumes supplied originals and the frozen mode. | `render` | mcp/tests/integration_certification_test_support.py:32-39 |
| Stored objects derive from a physical publication with injected code execution. | `selected_code_fixture` | mcp/tests/integration_certification_test_support.py:42-77 |
| Structural references are deterministic shapes without a backing evidence publication. | `structural_quality_references` | mcp/tests/integration_certification_test_support.py:80-99 |

## Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file establishes no external repository or host lifecycle authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History
- 2026-09-11T23:05:00+00:00: The claim said the integration owner comes from an actual started operation runtime and anchored it to `integration_fixture`; that helper (and its `IntegrationFixture` dataclass) was deleted as unreachable, and the runtime it drove is gone, so the row now records the removal and points at the surviving `selected_code_fixture`.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `SelectedCodeFixture` repointed to mcp/tests/integration_certification_test_support.py:26-39. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `render` repointed to mcp/tests/integration_certification_test_support.py:32-39. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `selected_code_fixture` repointed to mcp/tests/integration_certification_test_support.py:42-77. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `structural_quality_references` repointed to mcp/tests/integration_certification_test_support.py:80-99. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T14:46:49+00:00 — Created after reviewing actual source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented runtime ownership, original physical publications and the separate shape-only helper. This source verification makes no gate or acceptance claim.
