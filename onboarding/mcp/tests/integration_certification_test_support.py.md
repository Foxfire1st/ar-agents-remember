# mcp/tests/integration_certification_test_support.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.

No configured external domain source governs this file.

### Repo-Internal References

These source anchors establish the actual owner calls, fixture inputs and execution limits described above.

- The former runtime-owned integration fixture (`integration_fixture`/`IntegrationFixture`) was deleted as unreachable: it had no consumer, and the detached lifecycle worker whose `OperationRuntime` supplied its running record is gone. The surviving real-object fixture in this module is `selected_code_fixture`. [1]
- The selected fixture retains one target, prepared run and ordered original terminals. [2]
- Rendering consumes supplied originals and the frozen mode. [3]
- Stored objects derive from a physical publication with injected code execution. [4]
- Structural references are deterministic shapes without a backing evidence publication. [5]

### Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file establishes no external repository or host lifecycle authority.

No cross-repository evidence is required.
