# mcp/tests/test_codex_app_server_live.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_live.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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
the `C901`/`PLR0915` extraction. cit:([`test_live_dynamic_launch_and_mid_thread_selection`], mcp/tests/test_codex_app_server_live.py:162-259)
now reads as its own outline and delegates each step:
cit:([`_discover_without_starting_a_thread`], mcp/tests/test_codex_app_server_live.py:270-286) returns a `_Discovery` carrying the catalog, the
recorder, and the elapsed probe seconds; cit:([`_selection_pair`], mcp/tests/test_codex_app_server_live.py:298-322) returns the `_SelectionPair`
whose launch and switch rows must differ; cit:([`_assert_launch_selection_is_validated_against_the_catalog`], mcp/tests/test_codex_app_server_live.py:418-432)
holds the two fail-loud validations; cit:([`_configured_adapter`], mcp/tests/test_codex_app_server_live.py:325-343) builds the adapter,
recorder, and knob-applied launch with the `CODEX_CONFIG` negative assertion;
cit:([`_refused_unknown_selections`, `_queued_mid_thread_switch`], mcp/tests/test_codex_app_server_live.py:361-369; mcp/tests/test_codex_app_server_live.py:373-381) hold the
unsupported and queued setter assertions; cit:([`_completed_turn`], mcp/tests/test_codex_app_server_live.py:385-400) submits one bounded turn and
returns its vendor correlation id; cit:([`_accepted_turn_calls`], mcp/tests/test_codex_app_server_live.py:404-414) checks both `turn/start` calls
carry the one thread and the switched pair. The evidence print moved into
cit:([`_print_conformance_evidence`], mcp/tests/test_codex_app_server_live.py:446-494), which takes the `_LaunchedSession`, `_MidThreadSwitch`, and
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The live cases exercise the same native adapter/session/launch contracts used by production, while
retaining only an allowlisted evidence projection.

| Finding | Anchor | Source |
| --- | --- | --- |
| The recorder allowlists method/model/effort/thread fields and numeric token counters instead of retaining raw transport messages. | `RecordingCodexTransport`, `_safe_token_usage` | mcp/tests/test_codex_app_server_live.py:43-91; mcp/tests/test_codex_app_server_live.py:94-111 |
| The original opt-in smoke, marker- and env-gated, opens an ephemeral no-prompt thread and always stops it. | `test_live_handshake_model_menu_and_ephemeral_thread` | mcp/tests/test_codex_app_server_live.py:119-159 |
| Discovery proves the probe emits only initialize/model-list, starts no thread or turn, and records no token usage; the selection pair is chosen from model-local dynamic rows. | `_discover_without_starting_a_thread`, `_selection_pair` | mcp/tests/test_codex_app_server_live.py:270-286; mcp/tests/test_codex_app_server_live.py:298-322 |
| Settings-shaped resolution validates unknown model/effort before launch and carries the accepted pair without `CODEX_CONFIG`. | `CODEX_CONFIG` | mcp/tests/test_codex_app_server_live.py:346-346 |
| Setters are refused as unsupported, move from queued to effective on a fresh turn, repeat as immediate, and both accepted `turn/start` calls carry the one thread and the switched pair. | `_refused_unknown_selections`, `_queued_mid_thread_switch`, `_completed_turn`, `_accepted_turn_calls` | mcp/tests/test_codex_app_server_live.py:361-369; mcp/tests/test_codex_app_server_live.py:373-381; mcp/tests/test_codex_app_server_live.py:385-400; mcp/tests/test_codex_app_server_live.py:404-414 |
| Printed evidence stays allowlisted behind its three parameter objects, and turn completion has a bounded timeout. | `_wait_for_turn` | mcp/tests/test_codex_app_server_live.py:518-523 |
| The adapter carries launch state through native thread config, reports desired setters as queued until effective, and reports already-effective values as immediate. | `codex_launch_knobs`, `set_model`, `set_effort` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:163-194; mcp/src/agents_remember/serving/codex_app_server_adapter.py:196-224; mcp/src/agents_remember/serving/codex_app_server_session.py:35-54 |
| The session fails closed and stops on startup error, discovers via initialize/model-list with forced teardown, and bounds paginated catalog reads. | `connect`, `discover`, `_read_models` | mcp/src/agents_remember/serving/codex_app_server_session.py:124-208; mcp/src/agents_remember/serving/codex_app_server_session.py:214-224; mcp/src/agents_remember/serving/codex_app_server_session.py:383-401 |

## Cross-Repo References

Task-local live and independent-review artifacts establish that the opt-in test was run safely and
that its captured catalog is observation evidence rather than a maintained model list.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260715-FEUI-L5 Submission Authority Delta

The installed Codex smoke now exercises settings with an operation ref and no busy-queue
configuration. It remains an opt-in live proof; deterministic lifecycle races stay in fake-adapter
tests.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 30 citations (citation_anchor_missing=9, citation_prose_not_in_cit_form=12, citation_source_malformed=9); final scoped citation check clean.
- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The three
  behaviours the row names sit together at
  cit:([`codex_launch_knobs`], mcp/src/agents_remember/serving/codex_app_server_session.py:35-54)
  and cit:([`set_model`, `set_effort`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:163-194; mcp/src/agents_remember/serving/codex_app_server_adapter.py:196-224):
  native thread config, never `CODEX_CONFIG`, and the immediate/queued acceptance ladder. No claim text changed.

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
