# mcp/tests/test_codex_app_server_live.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_live.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T07:25+02:00 |
| lastVerifiedCommitHash | `d99a1a7f3ac251957ae155ea9beb878b9ba1ab25`|
| lastVerifiedCommitDate | 2026-07-16T07:36:40+02:00|
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

### Conventions

The two live paths have separate opt-ins so the ordinary suite skips all external work. Dynamic
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
| The recorder allowlists method/model/effort/thread fields and numeric token counters instead of retaining raw transport messages. | L34-L96 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| The original opt-in smoke opens an ephemeral no-prompt thread and always stops it. | L104-L143 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| The L5 path is independently opt-in, discovers with initialize/model-list only, starts no thread/turn, records no token usage, and chooses model-local dynamic rows. | L146-L207 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| Settings-shaped resolution validates unknown model/effort before launch and carries the accepted pair without `CODEX_CONFIG`. | L209-L243 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| Setters move from queued to effective on a fresh turn, repeat as immediate, persist on a second turn, and retain one PID/thread. | L244-L303 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| Printed evidence stays allowlisted, the live adapter always force-stops, and turn completion has a bounded timeout. | L304-L362 | [test_codex_app_server_live.py](agents-remember/mcp/tests/test_codex_app_server_live.py) |
| The adapter carries launch state through native thread config, reports desired setters as queued until effective, and reports already-effective values as immediate. | L124-L208 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The session fails closed and stops on startup error, discovers via initialize/model-list with forced teardown, and bounds paginated catalog reads. | L108-L208; L347-L387 | [codex_app_server_session.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) |

## Cross-Repo References

Task-local live and independent-review artifacts establish that the opt-in test was run safely and
that its captured catalog is observation evidence rather than a maintained model list.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The live worker recorded separate opt-in/default-skip behavior, an allowlisted recorder, dynamic target selection, token-free discovery, same-thread queued-to-effective switching, bounded turn accounting, and safe output. | L14-L50; L102-L150; L165-L187 | [L5 Codex live report](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-codex-live-conformance.md) |
| The final matrix labels the eight captured rows and exact keys as account-visible live evidence; consumers must not promote them into static policy. | L28-L34 | [L5 worker closeout report](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-worker-closeout-report.md) |
| Independent review audited the environment gate, recorder allowlist, two-turn bound, PID/thread assertions, token accounting, and cleanup, confirming default runs skip the turns and retain no secret/raw/prompt body. | L155-L161 | [L5 reviewer verdict](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-reviewer-verdict.md) |

## Update History

- 2026-07-16T07:25+02:00 — 260714-ACPUI-L5 test curator: documented the separately opted-in
  dynamic advertise/launch/same-thread conformance path, safe evidence recorder, two bounded turns,
  queued-to-effective-to-immediate semantics, subsequent-turn retention, and guaranteed teardown.
  Captured catalog counts/keys remain live observations rather than enums. Verification metadata
  remains at the last landed source commit until closeout stamps the uncommitted L5 candidate.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for the opt-in exact-version
  live handshake smoke and credential/prompt safety boundary. Verification remains unset until
  closeout stamps the code commit.
