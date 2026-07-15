# mcp/tests/test_harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-transport conformance coverage for the native Claude stream-JSON adapter, including structured
startup, token-free model catalog advertisement, correlated delivery, interactions, reconciliation,
limits, shutdown, and terminal normalization.

## Code Commentary

### 260714-ACPUI-L2 Effective-Launch Mismatch

The Claude suite can inject an expected `ResolvedLaunch` and now proves the fail-loud acceptance
boundary. When `system/init` echoes a different effective model, the adapter force-closes its
transport and propagates `HarnessControlError` so the runner can persist
`control=failed`/`acceptance=rejected` with exact bridge evidence. Genuine protocol negotiation
incompatibility remains the distinct `unsupported` result covered by the adjacent test.

### Logic

Pinned stream-JSON fixtures and a deterministic transport drive initialize, synthetic bootstrap,
catalog, turn, interaction, replay, failure, and result frames. Existing cases cover launch
preservation, compatible structured version negotiation, prompt correlation, busy ordering,
durable interaction responses, supported commands, ambiguous disconnect reconciliation, bounded
history, and safe terminal failure metadata.

ACPUI-L1 moves the fixture baseline to the live-confirmed `2.1.210` shape and adds catalog-specific
coverage. Discovery performs only the synthetic `shouldQuery: false` bootstrap plus the
`list_models` control request, asserts zero turns and zero cost, and always stops the transient
process. Started advertisement is cached, selects the current model, keeps effort levels nested per
model, leaves current effort unknown instead of inventing it, and preserves disabled models as
non-selectable catalog rows. Current initialization is accepted without stale `models` or `account`
fields, while duplicate model keys or a rejected `list_models` response make the adapter
unsupported and fail advertisement loudly without a fallback.

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase`, fixed UUIDs/timestamps, and JSONL fixtures under
the exact observed version directory. Fake writes are inspected structurally; secrets placed in the
launch environment must never appear in handshake evidence.

### Invariants And Boundaries

- Enumeration is token-free: the bootstrap is synthetic and non-querying, and the fixture proves
  zero turns and zero cost before `list_models` completes.
- The adapter uses Claude's native control request; no ACP transport, composer paste, static enum,
  or Toad host is involved.
- Effort options remain model-gated, and current effort remains absent when Claude does not report
  it.
- Malformed, duplicate, contradictory, or rejected catalog evidence fails loudly; there is no
  hardcoded production fallback.
- Fixture versions are test evidence rather than a production pin, and credentials/model output
  remain excluded from retained startup evidence.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The tests and native Claude adapter modules directly prove the startup, parsing, and cached
advertisement contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Token-free discovery uses one non-querying synthetic user frame, records zero turns/cost, selects the current model, and stops the transient transport. | L171-L185 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Startup preserves native launch settings, issues `list_models`, caches the selected catalog, gates efforts by model, leaves current effort unknown, and marks disabled rows non-selectable. | L187-L230 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Current initialization omits stale model/account fields, while duplicate or rejected catalog evidence yields unsupported/loud failure with no fallback. | L234-L284 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| The Claude catalog parser validates the native response, exact unique model keys, model-specific effort consistency, disabled state, and current-model membership. | L15-L31; L34-L97 | [claude_stream_capabilities.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_capabilities.py) |
| The adapter negotiates startup then catalog before readiness, retains the normalized snapshot, and provides transient discovery plus cached advertisement. | L74-L159 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| Native startup frames define the exact `list_models` control request and a synthetic non-querying bootstrap. | L56-L80 | [claude_stream_protocol.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) |

## Cross-Repo References

No sibling repository or transport implementation is required to prove this native-adapter test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented expected-launch injection and the
  force-close/propagate behavior that distinguishes an effective model mismatch from protocol
  unsupported. Verification metadata remains pinned until closeout stamps the L2 code commit.

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented the `2.1.210` catalog fixture,
  zero-turn/zero-cost discovery, cached model-gated advertisement, honest unknown effort, modern
  initialize shape, and loud no-fallback catalog failures; corrected the governing overview
  backlink while preserving existing verification metadata.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: recorded structured Claude negotiation and incompatible
  contract coverage.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
