# mcp/tests/integration_certification_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/integration_certification_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:46:49+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides real integration journal ownership and physically published original code-certification objects for focused tests. A separate helper supplies wire-shape references only, so callers can choose the authority boundary their assertions require.

## Code Commentary

### Logic

`integration_fixture` creates a Git repository, installs the requested generic profile and commits it before starting integration. It raises the fixture result-document bound to 128 KiB and recomputes the profile digest so complete retained publication bindings fit the admitted declaration. The caller supplies the contract factory. Concrete settings and a repository alias locate that repository; the actual starter creates the durable operation with detached launch replaced by a no-op. `OperationRuntime.start` supplies the running record and store for `IntegrationCertificationOwner`.

`selected_code_fixture` creates a real checkout with the repository profile, derives its candidate lane, freezes the full run and persists admission. The shared injected outcome factory supplies code-rail results while actual publication owners write and reopen the result document. `record_published_generation` constructs original typed terminal references and the fixture requires no recording refusal. This is physical object/publication composition, not ordinary-suite execution in Dagger.

`SelectedCodeFixture.render` calls the selected-certification renderer with those supplied originals, the fixture HEAD comparison base and frozen mode. `structural_quality_references` instead constructs deterministic small reference dictionaries and an empty canonical publication object for model-shape tests; it issues no backing objects or accepted certificates.

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
| The integration owner comes from an actual started operation runtime. | `integration_fixture` | mcp/tests/integration_certification_test_support.py:54-108 |
| The selected fixture retains one target, prepared run and ordered original terminals. | `SelectedCodeFixture` | mcp/tests/integration_certification_test_support.py:112-124 |
| Rendering consumes supplied originals and the frozen mode. | `SelectedCodeFixture.render` | mcp/tests/integration_certification_test_support.py:117-124 |
| Stored objects derive from a physical publication with injected code execution. | `selected_code_fixture` | mcp/tests/integration_certification_test_support.py:127-162 |
| Structural references are deterministic shapes without a backing evidence publication. | `structural_quality_references` | mcp/tests/integration_certification_test_support.py:165-184 |

## Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file establishes no external repository or host lifecycle authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T14:46:49+00:00 — Created after reviewing actual source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented runtime ownership, original physical publications and the separate shape-only helper. This source verification makes no gate or acceptance claim.
