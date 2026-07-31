# mcp/tests/test_codex_app_server_live.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_live.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Opt-in credential-safe live coverage for the native Codex app-server handshake plus the full L5
dynamic advertise, settings-shaped launch, and same-thread model/effort switching contract.

## Code Commentary

### Logic

The original smoke remains separately gated by `AR_CODEX_APP_SERVER_LIVE_SMOKE=1`. It launches an
ephemeral thread with explicit environment-selected model/effort, verifies the advertised and
effective effort, sends no prompt, and stops in `finally`.

The L5 case has its own `AR_CODEX_APP_SERVER_LIVE_CONFORMANCE=1` gate and states in the default-skip
reason that it sends two bounded turns. A safe transport recorder retains only method names,
model/effort/thread selectors, process id, and numeric token-usage counters. It never records the
environment, credentials, native config, prompt body, response body, or raw app-server payload.

The conformance sequence first calls dynamic discovery and proves the outgoing method set is only
`initialize` plus paginated `model/list`: there is no thread, turn, or token-usage event. It selects
the live default row as the launch pair, chooses a different selectable non-hidden row for the
switch (using the optional preferred target only when currently advertised), and derives efforts
from those specific model rows. Unknown model and model-local effort validation fails before the
configured session opens.

The launch pair travels through `ResolvedLaunch`, `LaunchKnobs`, and native thread config, with an
explicit negative assertion against `CODEX_CONFIG`. Once started, model and effort setters are
`queued`; the first fresh whole-message `turn/start` makes them effective. Repeating both setters
then returns `immediate`, and a second bounded turn proves the pair persists on the same app-server
PID and vendor thread. Invalid setters remain `unsupported`.

Discovery teardown is owned by the production session's `discover()` `finally`. The live session
is force-stopped by the test's outer `finally`, and production `connect()` separately stops its
transport if startup fails before that outer block is entered. Turn waits are bounded to 180
seconds.

Since 260731-EFA-L2 that sequence is a driver over named helpers rather than one long function —
the `C901`/`PLR0915` extraction. `test_live_dynamic_launch_and_mid_thread_selection` (L167-L258)
now reads as its own outline and delegates each step:
`_discover_without_starting_a_thread` (L269) returns a `_Discovery` carrying the catalog, the
recorder, and the elapsed probe seconds; `_selection_pair` (L297) returns the `_SelectionPair`
whose launch and switch rows must differ; `_assert_launch_selection_is_validated_against_the_catalog`
(L400) holds the two fail-loud validations; `_configured_adapter` (L324) builds the adapter,
recorder, and knob-applied launch with the `CODEX_CONFIG` negative assertion;
`_refused_unknown_selections` (L347) and `_queued_mid_thread_switch` (L358) hold the
unsupported and queued setter assertions; `_completed_turn` (L369) submits one bounded turn and
returns its vendor correlation id; `_accepted_turn_calls` (L387) checks both `turn/start` calls
carry the one thread and the switched pair. The evidence print moved into
`_print_conformance_evidence` (L447), which takes the `_LaunchedSession`, `_MidThreadSwitch`, and
`_BilledTurns` parameter objects instead of a long argument list. Every assertion, bound, and
allowlisted evidence key is the same as before the split; only where each one lives changed.

### Conventions

The two live paths have separate opt-ins so the ordinary suite skips all external work. Since
260731-EFA-L2 each also carries a registered marker beside its `skipif` —
`@pytest.mark.ar_codex_app_server_live_smoke` and
`@pytest.mark.ar_codex_app_server_live_conformance` — so the environment gate is selectable as
well as skippable. The markers are declared in the root `pyproject.toml` under `--strict-markers`,
and `mcp/tests/test_gated_integration_runner.py` fails if either one selects zero tests, which is
the regression that a marker decorating nothing (a silently empty `-m` run) cannot recur. Dynamic
catalog rows, defaults, effort menus, and any captured count/key are installation-, version-, and
account-specific observations; the test does not maintain them as production enums. Prompts are
fixed, minimal, whole-message requests used only to prove queued-to-effective and subsequent-turn
semantics.

### Invariants And Boundaries

- Default test runs must skip both live paths and spend no tokens.
- Discovery must create no thread or turn and must emit no token-usage event.
- Effort selection is always derived from the selected model's advertised row.
- Launch validation fails loud for unknown model/effort and never substitutes a default.
- Mid-session selection remains queued until a fresh accepted turn proves it effective; repeated
  selection is immediate only after that promotion.
- Both accepted turns retain the original PID and vendor thread, with no reconnect or resume.
- Safe evidence excludes secrets, environment/config values, prompts, response bodies, and raw
  transport payloads.
- Every transient/live process has a production or test-owned `finally` cleanup path.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The live cases exercise the same native adapter/session/launch contracts used by production, while
retaining only an allowlisted evidence projection.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The recorder allowlists method/model/effort/thread fields and numeric token counters instead of retaining raw transport messages. | L42-L110 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| The original opt-in smoke, marker- and env-gated, opens an ephemeral no-prompt thread and always stops it. | L118-L158 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| The L5 driver: independently marker/env opt-in, it sequences the conformance run and force-stops the adapter in its `finally` (L257-L258). | L161-L258 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| Discovery proves the probe emits only initialize/model-list, starts no thread or turn, and records no token usage; the selection pair is chosen from model-local dynamic rows. | L261-L285; L288-L321 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| Settings-shaped resolution validates unknown model/effort before launch and carries the accepted pair without `CODEX_CONFIG`. | L324-L344; L400-L414 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| Setters are refused as unsupported, move from queued to effective on a fresh turn, repeat as immediate, and both accepted `turn/start` calls carry the one thread and the switched pair. | L347-L397 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| Printed evidence stays allowlisted behind its three parameter objects, and turn completion has a bounded timeout. | L417-L495; L498-L503 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| The adapter carries launch state through native thread config, reports desired setters as queued until effective, and reports already-effective values as immediate. | L225-L306 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The session fails closed and stops on startup error, discovers via initialize/model-list with forced teardown, and bounds paginated catalog reads. | L108-L208; L347-L387 | [codex_app_server_session.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) |

## Cross-Repo References

Task-local live and independent-review artifacts establish that the opt-in test was run safely and
that its captured catalog is observation evidence rather than a maintained model list.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The live worker recorded separate opt-in/default-skip behavior, an allowlisted recorder, dynamic target selection, token-free discovery, same-thread queued-to-effective switching, bounded turn accounting, and safe output. | L14-L50; L102-L150; L165-L187 | [L5 Codex live report](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-codex-live-conformance.md) |
| The final matrix labels the eight captured rows and exact keys as account-visible live evidence; consumers must not promote them into static policy. | L28-L34 | [L5 worker closeout report](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-worker-closeout-report.md) |
| Independent review audited the environment gate, recorder allowlist, two-turn bound, PID/thread assertions, token accounting, and cleanup, confirming default runs skip the turns and retain no secret/raw/prompt body. | L155-L161 | [L5 reviewer verdict](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-reviewer-verdict.md) |

## 260715-FEUI-L5 Submission Authority Delta

The installed Codex smoke now exercises settings with an operation ref and no busy-queue
configuration. It remains an opt-in live proof; deterministic lifecycle races stay in fake-adapter
tests.

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The three
  behaviours the row names sit together at `codex_app_server_adapter.py` L225-L306: `launch_knobs`
  (L225-L243) returns `session_config={"model", "model_reasoning_effort"}` — native thread config,
  never `CODEX_CONFIG` — and `set_model` (L245-L276) / `set_effort` (L278-L306) return
  `acceptance="immediate"` when `has_pending_settings` is false and `"queued"` otherwise. The old
  L124-L208 spans the constructor and `start`. No claim text changed.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the conformance case this card describes was
  split, so the body was rewritten rather than attested. The `C901`/`PLR0915` extraction turned
  `test_live_dynamic_launch_and_mid_thread_selection` into a driver over nine named helpers —
  `_discover_without_starting_a_thread`, `_selection_pair`,
  `_assert_launch_selection_is_validated_against_the_catalog`, `_configured_adapter`,
  `_refused_unknown_selections`, `_queued_mid_thread_switch`, `_completed_turn`,
  `_accepted_turn_calls` and `_print_conformance_evidence` — with five `NamedTuple` carriers
  (`_Discovery`, `_SelectionPair`, `_LaunchedSession`, `_MidThreadSwitch`, `_BilledTurns`) standing
  in for what were long argument lists, chiefly around the evidence print. Both live tests also
  gained registered markers, `ar_codex_app_server_live_smoke` and
  `ar_codex_app_server_live_conformance`, declared in the root `pyproject.toml` under
  `--strict-markers` and guarded by `test_gated_integration_runner.py` against selecting zero
  tests; the Conventions section now records that beside the existing environment gates. All six
  own-file ranges in the references table were recomputed against the new layout and re-read at
  their new positions, with the discovery/selection and resolution/validation pairs now cited as
  two ranges each because their code no longer sits in one span. Nothing the suite proves moved:
  the discovery method set, the `CODEX_CONFIG` negative assertion, the unsupported/queued/immediate
  ladder, the two-turn bound, the same PID and vendor thread, the allowlisted evidence keys and the
  180-second wait are all unchanged. Verification metadata stays pinned until closeout stamps the
  code commit.

- 2026-07-17T21:39+02:00 — FEUI-L5: aligned the live Codex path to op-aware control without native
  queue configuration.

- 2026-07-16T07:25+02:00 — 260714-ACPUI-L5 test curator: documented the separately opted-in
  dynamic advertise/launch/same-thread conformance path, safe evidence recorder, two bounded turns,
  queued-to-effective-to-immediate semantics, subsequent-turn retention, and guaranteed teardown.
  Captured catalog counts/keys remain live observations rather than enums. Verification metadata
  remains at the last landed source commit until closeout stamps the uncommitted L5 candidate.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for the opt-in exact-version
  live handshake smoke and credential/prompt safety boundary. Verification remains unset until
  closeout stamps the code commit.
