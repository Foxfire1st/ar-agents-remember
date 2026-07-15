# mcp/tests/test_harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:21+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-transport conformance coverage for the native Claude stream-JSON adapter, including structured
startup, token-free model catalog advertisement, same-session model/effort setters with terminal
evidence, correlated delivery, interactions, reconciliation, limits, shutdown, and terminal
normalization.

## Code Commentary

### 260714-ACPUI-L3 Same-Session Setter Evidence

The L3 scenarios drive `/model` and `/effort` as structured Claude session commands through the
native stream transport. A set becomes `echo-verified` only after the replayed user frame matches
the retained correlation, session id, and exact canonical command body and a following terminal
result echoes an allowed effective label. Model changes immediately re-gate effort against the
new model's dynamic menu; an unavailable effort is `unsupported` without another write. A
completed command with no effective echo is only `immediate` and does not promote advertised
state, while a failed native command is `unsupported`.

Fable behavior is deliberately native-result-driven. A provider-qualified model whose key does not
contain `fable` can return `noninteractive_set_blocked` and map to `unsupported` with launch-flag
guidance. Conversely, an advertised alias literally named `fable` can echo a Sonnet terminal label
and succeed. This proves there is no key/prefix heuristic. Exact terminal-label tests also reject
prefix impostors and arbitrary `(default)` strings; allowed aliases are derived from the dynamic
catalog row and matching resolved-model identities.

Timeout and cancellation cases retain only enough abandoned command state to neutralize late
replay/result frames before a clean retry. A later setter is not sent while an abandoned command
has not terminated, completed duplicate replay is ignored, strict correlation/body/session
mismatches fail loudly, and a duplicate retained correlation is never written a second time.

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
- Model/effort promotion requires same-session exact replay correlation plus terminal effective
  echo; completion without that echo never becomes `echo-verified`.
- Claude's native `noninteractive_set_blocked` result determines unsupported switching. Model keys,
  aliases, or provider prefixes are never used to guess a Fable refusal before sending.
- Dynamic model terminal aliases match exactly; prefix collisions and unrelated default labels do
  not promote capability state.
- Timed-out/cancelled command frames are neutralized without stealing a later setter result or
  writing a duplicate retained correlation.
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
| Token-free discovery uses one non-querying synthetic user frame, records zero turns/cost, selects the current model, and stops the transient transport. | L195-L209 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Startup preserves native launch settings, issues `list_models`, caches the selected catalog, gates efforts by model, leaves current effort unknown, and marks disabled rows non-selectable. | L211-L256 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Current initialization omits stale model/account fields, while duplicate or rejected catalog evidence yields unsupported/loud failure with no fallback. | L258-L309 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Same-session model/effort setters require native replay plus terminal echo, update the model gate only on evidence, and refuse effort unavailable for the selected model without a write. | L509-L563 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Native failure and non-echo completion remain unsupported/immediate without promotion; provider-qualified Fable refusal and a successful alias named `fable` prove there is no name heuristic. | L565-L654 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Exact dynamic terminal aliases reject prefix impostors and arbitrary default labels. | L656-L739 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Timeout/cancellation late frames are neutralized before retry, strict replay correlation/body/session mismatches fail, and duplicate retained correlations are not written twice. | L741-L848 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| The Claude catalog parser validates the native response, exact unique model keys, model-specific effort consistency, disabled state, and current-model membership. | L15-L31; L34-L97 | [claude_stream_capabilities.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_capabilities.py) |
| The adapter negotiates startup then catalog before readiness, retains the normalized snapshot, and provides transient discovery plus cached advertisement. | L96-L209 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| Native startup frames define the exact `list_models` control request and a synthetic non-querying bootstrap. | L56-L80 | [claude_stream_protocol.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) |
| Claude setters validate the dynamic catalog/model gate, send structured commands, promote only echo-verified results, and derive exact model terminal aliases from the selected catalog row. | L223-L298; L457-L507; L519-L540 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| State submission retains canonical command replay text, waits for a terminal result, and marks timed-out commands abandoned. | L102-L168 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |
| Replayed-user handling requires exact retained correlation, session, and body; completed abandoned replays are ignored rather than requeued. | L412-L450 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |

## Cross-Repo References

No sibling repository or transport implementation is required to prove this native-adapter test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented same-session structured setters,
  exact replay plus terminal-echo evidence, model-gated effort, native-result-driven Fable refusal,
  exact dynamic aliases, and cancellation/timeout/duplicate-correlation neutralization. Verification
  metadata remains pinned until closeout stamps the L3 code commit.
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
