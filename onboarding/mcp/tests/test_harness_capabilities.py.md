# mcp/tests/test_harness_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:21+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892`|
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused unit coverage for the normalized own-adapter model/effort capability contract, its
ACP-Sense-1-compatible JSON projection, the closed setter-acceptance vocabulary, and the static
anti-paste boundary. The file tests the shared contract independently of any ACP transport.

## Code Commentary

### Logic

Synthetic model snapshots exercise the two category-keyed select projections: `model` and
`thought_level`. The selected model's effort menu is projected without leaking a different model's
effort values, disabled non-current models are excluded from selection, and model/effort metadata
survives JSON serialization.

A selected model remains in the model select even when it is hidden or currently non-selectable, so
the required `currentValue` remains honest. Conversely, the projection omits all selects when no
current model is known and omits only the effort select when the current effort is unknown.

The setter-result test proves that the implementation-owned vocabulary contains exactly
`echo-verified`, `immediate`, `queued`, `unknown`, and `unsupported`; serialization rejects an
arbitrary sixth token instead of passing adapter drift through to serving clients. A separate
static boundary test scans the complete native-setter delegation graph across the shared bridge,
queue, Claude stream modules, Codex app-server modules, and Pi RPC modules. It rejects dependencies
on terminal/chat paste surfaces and therefore pins the anti-paste rule at every transitive setter
delegate, not only at the three adapter entrypoints.

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
- The accepted `SetResult` vocabulary is closed to exactly five values, and serialization must fail
  when an adapter supplies any value outside that set.
- Native setter modules must remain independent of terminal panes, chat/composer injection, tmux,
  and session-command paste surfaces across the full transitive implementation graph.

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
| The primary snapshot verifies exact category names, nested selected-model effort options, disabled-model filtering, and JSON metadata. | L18-L73 | [test_harness_capabilities.py](agents-remember/mcp/tests/test_harness_capabilities.py) |
| Selected hidden and non-selectable models remain in the select, while unknown current values suppress the corresponding projections. | L76-L129 | [test_harness_capabilities.py](agents-remember/mcp/tests/test_harness_capabilities.py) |
| `SetResult` coverage proves the exact five-value set, preserves requested versus effective evidence in JSON, and rejects an arbitrary acceptance token. | L132-L156 | [test_harness_capabilities.py](agents-remember/mcp/tests/test_harness_capabilities.py) |
| The anti-paste guard scans every shared and harness-specific module in the native setter delegation graph for terminal/chat injection dependencies. | L159-L194 | [test_harness_capabilities.py](agents-remember/mcp/tests/test_harness_capabilities.py) |
| The shared types define the exact capability categories, five SetResult acceptances, model-gated effort structure, and current selection fields; serialization independently enforces acceptance membership. | L13-L23; L26-L81; L216-L225 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |
| Config projection retains the selected model, gates effort to that model, omits unknown-current selects, and serializes required string current values. | L75-L133; L162-L214 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |

## Cross-Repo References

This is a same-repository contract test with no transport or sibling-repository dependency.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented exact runtime enforcement of the
  five-value setter-acceptance vocabulary and the complete native-setter anti-paste delegate scan.
  Verification metadata remains pinned until closeout stamps the L3 code commit.
- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: created onboarding for the exact
  category-keyed projection, honest-current selection rules, model-gated effort menu, hidden/current
  visibility, and SetResult serialization. Verification hash and date remain empty because the test
  file is new and uncommitted.
