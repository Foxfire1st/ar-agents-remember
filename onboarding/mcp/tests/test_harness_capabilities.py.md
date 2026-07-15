# mcp/tests/test_harness_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05:47+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa`|
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused unit coverage for the normalized own-adapter model/effort capability contract and its
ACP-Sense-1-compatible JSON projection. The file tests the shared contract independently of Claude,
Codex, Pi, or any ACP transport.

## Code Commentary

### Logic

Synthetic model snapshots exercise the two category-keyed select projections: `model` and
`thought_level`. The selected model's effort menu is projected without leaking a different model's
effort values, disabled non-current models are excluded from selection, and model/effort metadata
survives JSON serialization.

A selected model remains in the model select even when it is hidden or currently non-selectable, so
the required `currentValue` remains honest. Conversely, the projection omits all selects when no
current model is known and omits only the effort select when the current effort is unknown. The
final test pins the `SetResult` JSON field names and demonstrates an `echo-verified` result with a
different effective value, while the implementation type owns the complete five-value acceptance
vocabulary.

### Conventions

Tests are small plain `pytest` functions with immutable dataclass fixtures. `typing.cast` is used
only at JSON-object inspection boundaries; no fake vendor adapter or process is involved.

### Invariants And Boundaries

- The projection adopts ACP's category-keyed select shape only; this module does not test or add ACP
  transport behavior.
- Effort options are model-gated and come only from the selected model.
- A selected hidden or non-selectable model remains visible in its own select projection so
  `currentValue` never points outside the available options.
- No select is emitted with an invented or null current value.
- The test verifies `SetResult` serialization with one allowed acceptance; the exact five allowed
  values are defined by the shared implementation type rather than duplicated as a test enum.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this new test file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test and its shared contract module are the direct evidence for the normalized projection.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The primary snapshot verifies exact category names, nested selected-model effort options, disabled-model filtering, and JSON metadata. | L15-L70 | [test_harness_capabilities.py](agents-remember/mcp/tests/test_harness_capabilities.py) |
| Selected hidden and non-selectable models remain in the select, while unknown current values suppress the corresponding projections. | L73-L126 | [test_harness_capabilities.py](agents-remember/mcp/tests/test_harness_capabilities.py) |
| `SetResult` serialization keeps the evidence fields and preserves requested versus effective values. | L129-L144 | [test_harness_capabilities.py](agents-remember/mcp/tests/test_harness_capabilities.py) |
| The shared types define the exact capability categories, five SetResult acceptances, model-gated effort structure, and current selection fields. | L13-L20; L23-L49; L60-L78 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |
| Config projection retains the selected model, gates effort to that model, omits unknown-current selects, and serializes required string current values. | L80-L130; L153-L159; L188-L214 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |

## Cross-Repo References

This is a same-repository contract test with no transport or sibling-repository dependency.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: created onboarding for the exact
  category-keyed projection, honest-current selection rules, model-gated effort menu, hidden/current
  visibility, and SetResult serialization. Verification hash and date remain empty because the test
  file is new and uncommitted.
