# mcp/tests/test_codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-transport conformance tests for the native Codex app-server adapter. The suite proves both the
hosted control lifecycle and the dynamic, token-free model/effort advertisement path used by the
normalized harness capability contract.

## Code Commentary

### 260714-ACPUI-L2 Codex Initial Configuration

The adapter tests now pin both settings-resolved and roleless initial configuration. A configured
session sends model at `thread/start` and includes both `model` and
`model_reasoning_effort` in its configuration, retaining the same pair on resume. A roleless
session selects the single visible advertised default model and that model's own default effort
after token-free discovery, ignoring any need for a reconnect or a TUI launch override. Assertions
inspect the exact request and effective echo; no turn is submitted by this setup coverage.

### Logic

The deterministic transport records requests, notifications, responses, and shutdown modes while
the pinned app-server fixture supplies structured initialize, model-list, thread, turn, approval,
and elicitation frames. Existing scenarios cover startup/resume identity, exact reasoning-effort
acceptance, busy steer/queue policy, structured interactions, terminal mapping, reconnect without
resend, and strict correlation.

The ACPUI-L1 additions assert that a started adapter returns its retained model catalog without
issuing another request, including display text, descriptions, the current model, and the current
effort. A separate discovery scenario pages through `model/list` with `includeHidden: true`, retains
hidden models and their model-specific effort menus, leaves current selections unset before a
thread exists, and proves discovery never calls `thread/*` or `turn/*`. A repeated pagination cursor
fails loudly and still forces the transient app-server process to stop.

### Conventions

Tests use `pytest` with the AnyIO asyncio backend. `FakeCodexTransport` deep-copies protocol values
so fixture mutation and adapter behavior remain deterministic. The pinned `0.144.3` fixture is
schema evidence for the tests, not a production version enum or fallback catalog.

### Invariants And Boundaries

- Catalog discovery is protocol-only and prompt-free; it initializes app-server and reads every
  `model/list` page without opening a thread or turn.
- `advertise()` is a cached read after startup and must not spend another transport request.
- Hidden installed models remain represented in the full normalized catalog, with effort options
  nested under the model that advertised them.
- Repeated pagination cursors and absent or unconfirmed effort fail loudly; no static default model
  or effort menu is substituted.
- Existing reconnect coverage requires `resend: false`, and the tests do not register a production
  driver or exercise pane/log readiness.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test module and native Codex implementation directly prove the catalog-retention and
thread-free discovery contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The started-adapter test verifies cached advertisement, retained descriptions, current model/effort, and no extra request after startup. | L186-L238 | [test_codex_app_server_adapter.py](agents-remember/mcp/tests/test_codex_app_server_adapter.py) |
| Discovery retains a paginated hidden model, sends only initialize/model-list requests, opens no thread or turn, and rejects a repeated cursor while stopping the process. | L241-L305 | [test_codex_app_server_adapter.py](agents-remember/mcp/tests/test_codex_app_server_adapter.py) |
| The adapter validates the native Codex harness id and delegates transient discovery and cached advertisement to its session. | L88-L126 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| Session discovery performs initialize plus paged model-list only and always stops its transient transport; started advertisement requires a retained catalog. | L173-L183; L205-L213 | [codex_app_server_session.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) |
| The fixture path remains an explicit test baseline rather than a runtime catalog source. | L27-L29 | [test_codex_app_server_adapter.py](agents-remember/mcp/tests/test_codex_app_server_adapter.py) |

## Cross-Repo References

The earlier coordination-repo review remains useful historical evidence for the pre-ACPUI Codex
protocol contract; it does not replace the current source tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The prior reviewer verdict confirms initialize/model-list/thread behavior, protocol-only effort handling, normalized state, interactions, reconnect, and fixture provenance. | L24-L33 | [260713-PHA-L3 reviewer verdict](ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

## Update History

- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added the configured and roleless Codex
  `thread/start` launch contract, including model-local default effort and resume preservation.
  Verification metadata remains pinned until closeout stamps the L2 code commit.

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented cached current-session
  advertisement, paginated hidden-model discovery, model-gated effort metadata, thread/turn-free
  enumeration, and repeated-cursor cleanup; corrected the governing overview backlink while
  preserving existing verification metadata.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: documented null-requestId correlation, same-row
  completion projection, loud failure cases, and no-replacement terminal state assertions.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented negotiated-version acceptance and loud rejection
  coverage.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for fake-protocol
  conformance, R11 strictness, server requests, busy policy, terminal mapping, and no-resend
  reconnect coverage. Verification remains unset until closeout stamps the code commit.
