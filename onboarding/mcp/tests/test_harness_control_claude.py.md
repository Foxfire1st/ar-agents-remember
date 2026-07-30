# mcp/tests/test_harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T15:05+02:00 |
| lastVerifiedCommitHash | `2b47ed9520a770b9858e8af1f112f58745dcf473` |
| lastVerifiedCommitDate | 2026-07-30T16:00:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-transport conformance coverage for the native Claude stream-JSON adapter, including structured
startup, token-free and MCP-isolated model catalog discovery, same-session model/effort setters with
terminal evidence, correlated delivery, interactions, reconciliation, limits, shutdown, and
terminal normalization.

## Code Commentary

### Sub-Agent Text Forwarding Floor

The fail-closed `--forward-subagent-text` version floor is pinned here (fix-round review finding 8). The
fake transport learns scripted re-launch: `start_argvs` records every launch argv, and a
`restart_frames` script drains the stop sentinel and replays startup frames on the second `start`.
The below-floor case (2.1.210, L431-L445) requires the flag omitted, exactly ONE launch (no
re-launch), and an `unverified` note naming both the observed and floor versions. The at-floor
case (2.1.220, L466-L491) proves the two-launch flow: the probe launch omits the flag, the proven
re-launch carries it behind the `system/init` capture, and the note reports `enabled`. The
unparseable-version case (`dev-build`, L493-L510) stays fail-closed with one flagless launch. The
mapper-tier floor verdicts live in `test_conversation_projector_claude_agents.py`.

Those cases prove the argv contract but not the transport lifecycle it assumes: `_FakeClaudeTransport`
accepts a second `start` on the same object, so the at-floor case passed while the production
transport would have refused its own re-launch (260727-CHATS-IM-L4).
`ClaudeProductionTransportRelaunchTests` closes that gap by driving the real adapter with
`transport_factory=ClaudeSubprocessTransport` against a local stream-json stub that reports 2.1.220
and appends each launch argv to a log file. It asserts exactly two launches with the flag only on the
second, `control` = `ready`, and a selectable model whose effort options are advertised — the
dashboard's model/effort surface. The stub is a local interpreter script, so the case stays
credential-free while still exercising real process ownership.

### Discovery Isolation And Live Closure

Claude catalog discovery stays token-free while the transient probe is kept from starting
unrelated MCP servers inherited through the caller's native argv. The discovery-only regression
table covers the selector grammar accepted by the observed Claude Code 2.1.210 install: one
separate config, variadic and repeated separate configs, equals-attached configs, the exact strict
flag, and the first `--` end-of-options separator. It requires all accepted selectors before the
separator to be replaced by exactly one strict empty config. Unrelated options retain their order,
an equals-attached config never consumes a following positional, and the entire post-`--` suffix
remains byte-for-byte intact. The test deliberately does not invent rejected boolean or negated
strict spellings.

This isolation is scoped to `discover()`. A separate normal-start case requires existing caller MCP
selectors to survive byte-for-byte, so ordinary settings-owned sessions continue to load their
installed MCP configuration. The original fake discovery case still proves the synthetic bootstrap
has zero turns and zero cost, uses one strict empty config, and force-stops the transient transport.

Live evidence closes the relationship between those fake pins and the native process:
a two-marker A/B made normal startup create both configured markers while discovery created
neither, returned the same model-gated catalog at zero turns/cost, and cleaned up. The independent
reviewer then reproduced an adversarial marker collision against the corrected candidate; its
marker stayed absent and the same five observed model keys returned. Those row counts and keys are
live installation/auth observations, not production enums or expectations encoded by this suite.

### Same-Session Setter Evidence

The same-session scenarios drive `/model` and `/effort` as structured Claude session commands through the
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

### Effective-Launch Mismatch

The Claude suite can inject an expected `ResolvedLaunch` and now proves the fail-loud acceptance
boundary. When `system/init` echoes a different effective model, the adapter force-closes its
transport and propagates `HarnessControlError` so the runner can persist
`control=failed`/`acceptance=rejected` with exact bridge evidence. Genuine protocol negotiation
incompatibility remains the distinct `unsupported` result covered by the adjacent test.

### Logic

Pinned stream-JSON fixtures and a deterministic transport drive initialize, synthetic bootstrap,
catalog, turn, interaction, replay, failure, and result frames. Existing cases cover launch
preservation, discovery-only MCP isolation, compatible structured version negotiation, prompt
correlation, busy ordering, durable interaction responses, supported commands, ambiguous
disconnect reconciliation, bounded history, and safe terminal failure metadata.

The fixture baseline tracks the live-confirmed `2.1.210` shape with catalog-specific
coverage. Discovery performs only the synthetic `shouldQuery: false` bootstrap plus the
`list_models` control request, asserts zero turns and zero cost, and always stops the transient
process. Started advertisement is cached, selects the current model, keeps effort levels nested per
model, leaves current effort unknown instead of inventing it, and preserves disabled models as
non-selectable catalog rows. Current initialization is accepted without stale `models` or `account`
fields, while duplicate model keys or a rejected `list_models` response make the adapter
unsupported and fail advertisement loudly without a fallback.

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase`, fixed UUIDs/timestamps, and JSONL fixtures under
the exact observed version directory. Selector cases are table-driven by grammar shape rather than
captured model names. Fake writes and argv are inspected structurally; secrets placed in the launch
environment must never appear in handshake evidence.

### Invariants And Boundaries

- Enumeration is token-free: the bootstrap is synthetic and non-querying, and the fixture proves
  zero turns and zero cost before `list_models` completes.
- Discovery removes every installed-grammar MCP selector before the first `--`, inserts one strict
  empty config, preserves unrelated argv and the complete positional suffix, and always stops the
  transient transport.
- Normal session startup must preserve caller MCP selectors byte-for-byte; discovery isolation is
  never applied to the real settings-owned session path.
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
- `--forward-subagent-text` is fail-closed: emitted only behind a probed >= 2.1.220 install via a
  probe-launch-then-relaunch flow; below-floor or unparseable versions run exactly one flagless
  launch with an honest `unverified` note (fix-round finding 8).
- The fake transport is restart-tolerant and therefore cannot witness process ownership; any claim
  about the probe re-launch actually launching belongs to the real-transport case, not the fake tier.
- Fixture versions are test evidence rather than a production pin, and credentials/model output
  remain excluded from retained startup evidence.

### Todos

None.

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
| Token-free discovery uses one non-querying synthetic user frame, records zero turns/cost, inserts one strict empty config, selects the current model, and stops the transient transport. | L195-L215 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Discovery replaces separate, variadic/repeated, and equals-attached MCP selectors; preserves unrelated argv and the full post-`--` suffix; and leaves exactly one strict empty config before the separator. | L217-L329 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Normal startup preserves caller MCP selectors byte-for-byte, proving isolation is discovery-only. | L331-L351 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Startup preserves native launch settings, issues `list_models`, caches the selected catalog, gates efforts by model, leaves current effort unknown, and marks disabled rows non-selectable. | L353-L401 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Current initialization omits stale model/account fields, while duplicate or rejected catalog evidence yields unsupported/loud failure with no fallback. | L402-L453 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Same-session model/effort setters require native replay plus terminal echo, update the model gate only on evidence, and refuse effort unavailable for the selected model without a write. | L653-L708 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Native failure and non-echo completion remain unsupported/immediate without promotion; provider-qualified Fable refusal and a successful alias named `fable` prove there is no name heuristic. | L709-L799 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Exact dynamic terminal aliases reject prefix impostors and arbitrary default labels. | L800-L884 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Timeout/cancellation late frames are neutralized before retry, strict replay correlation/body/session mismatches fail, and duplicate retained correlations are not written twice. | L885-L993 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| The Claude catalog parser validates the native response, exact unique model keys, model-specific effort consistency, disabled state, and current-model membership. | L15-L31; L34-L97 | [claude_stream_capabilities.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_capabilities.py) |
| The adapter negotiates startup then catalog before readiness, isolates only transient discovery, force-stops that probe, and retains cached advertisement for started sessions. | L97-L215 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| The discovery argv builder removes only accepted pre-separator MCP selector spellings, preserves unrelated arguments/suffixes, and adds one strict empty set; the ordinary stream argv builder stays separate. | L41-L87 | [claude_stream_protocol.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) |
| Native startup frames define the exact `list_models` control request and a synthetic non-querying bootstrap. | L90-L116 | [claude_stream_protocol.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) |
| Claude setters validate the dynamic catalog/model gate, send structured commands, promote only echo-verified results, and derive exact model terminal aliases from the selected catalog row. | L233-L308; L467-L550 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| State submission retains canonical command replay text, waits for a terminal result, and marks timed-out commands abandoned. | L102-L168 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |
| Replayed-user handling requires exact retained correlation, session, and body; completed abandoned replays are ignored rather than requeued. | L412-L450 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |

## Cross-Repo References

The live and reviewer artifacts corroborate the fake selector grammar with real process
side-effect markers. Their five-row result is a captured install/auth observation, not a test enum.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The corrected live two-marker A/B preserved normal configured startup, isolated discovery, returned the same zero-turn/model-gated catalog, and cleaned up. | L72-L96 | [L5 worker closeout report](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-worker-closeout-report.md) |
| Independent review caught the append-only selector collision, then closed it only after fake grammar cases plus an independent marker replay returned the same five observed keys with no marker side effect. | L148-L151; L163-L173 | [L5 reviewer verdict](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-reviewer-verdict.md) |

## Submission Authority Delta

Claude hosted-control tests now prove sole-operation authority across prompt/interaction/setter
traffic, exact terminal completion, late/cancel/duplicate immunity, and bounded retained history.
Unknown setter evidence remains the shared barrier until exact resolution.

## Native Interrupt Acceptance Delta

Claude control regressions now pin native interrupt request acceptance and the corresponding typed failure/detail paths without mistaking acknowledgement for turn settlement.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: recorded `ClaudeProductionTransportRelaunchTests`, the
  real-transport probe/relaunch proof, and named the restart-tolerant fake as the reason the at-floor
  argv case passed over a transport that would have refused its own re-launch.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: recorded the `--forward-subagent-text`
  flag-floor coverage (fix-round finding 8) — the fake transport's scripted re-launch
  (`start_argvs`/`restart_frames`), the below-floor one-launch omission with the exact
  `unverified` note, the at-floor probe-then-relaunch flow, and the unparseable-version
  fail-closed case. Verification metadata stays pinned (uncommitted); closeout re-stamps the
  candidate commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-17T21:39+02:00 — FEUI-L5: added Claude sole-authority, exact completion, stale-event, and
  bounded-history regression proof.

- 2026-07-16T07:25+02:00 — 260714-ACPUI-L5 test curator: documented discovery-only Claude MCP
  selector isolation across separate, variadic/repeated, equals-attached, and end-of-options forms;
  normal-start argv preservation; the zero-turn fake/live relationship; and the independent marker
  collision closure. Live catalog counts/keys remain observations, not enums. Verification metadata
  remains at the last landed source commit until closeout stamps the uncommitted L5 candidate.
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
