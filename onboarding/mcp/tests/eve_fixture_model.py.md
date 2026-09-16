# mcp/tests/eve_fixture_model.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/eve_fixture_model.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `609756111eb3c239d0563d8631bfd564645bc9d1` |
| lastVerifiedCommitDate | 2026-09-16T10:25:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

A deterministic OpenAI-compatible chat-completions stub used as **eve's model provider**. It is a
model provider, not a harness and not a fake adapter: eve runs its real session protocol, real tool
loop, real compaction and real durable stream against it, so a fixture driving eve through this stub
exercises the production path with a provider whose answers are reproducible.

Not pytest-collected: the filename does not match `test_*.py`. It is a standalone server script the
live native fixture starts as a child process.

## Code Commentary

### Logic

The plan is a JSON list and request *N* is answered by entry *N*. Each entry is one of:

- `{"text": "..."}` — an assistant message streamed in small deltas, ending `finish_reason: stop`;
- `{"toolCalls": [{"callId", "name", "arguments"}]}` — one or more streamed tool calls, ending
  `finish_reason: tool_calls`;
- either may carry `"delaySeconds": N` to hold the response open, which is how a fixture gives a test
  time to cancel an in-flight turn.

`FixturePlan` holds one server's scripted answers **plus the request counter that walks them**.
`_Handler` serves the OpenAI-compatible routes over a `ThreadingHTTPServer`; `_chunks_for` streams an
assistant message, `_tool_chunk` emits tool calls and `_aggregate` builds the non-streaming
aggregate; `serve` and `main` are the CLI entry points (`--plan`, `--state`, `--port`).

### Conventions

- `DELTA_STEP` (7) and `ARGUMENT_STEP` (11) chunk deltas at fixed sizes, so a stream's shape is
  reproducible rather than incidental.
- The plan is read once per server and the counter lives on the server instance.
- Usage is printed in the module docstring; the live fixture starts this file as a subprocess.

### Invariants And Boundaries

- **`FixturePlan` is bound to the server instance, never to module globals.** A first draft used
  module-global plan state and the concurrent-session scenario cross-contaminated — two stub servers
  shared one plan, so one session received the other's answer. One provider per session is what makes
  the isolation scenario meaningful.
- The stub emits identity (`id`/`type`) on the **first chunk of each tool call**. A first draft omitted
  it and eve answered `MODEL_CALL_FAILED: Expected 'id' to be a string`.
- This module is a **test fixture only**. It is not a production provider integration and must not be
  wired into a non-test launch path.
- It supplies no hosted-model behavior: the real-provider probe in the live fixture deliberately does
  not use this stub.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the served shape is the OpenAI-compatible chat-completions API, which is a third-party contract this stub imitates rather than a configured domain source. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The live fixture starts this stub and points the runtime at it, and is the only consumer. | `LiveFixture`; `_plan` | mcp/tests/live_eve_native_fixture.py:177-363; mcp/tests/live_eve_native_fixture.py:534-740 |
| The runtime application reads the provider base URL, name and key from the adapter-owned launch environment. | `createOpenAICompatible`; `AR_EVE_PROVIDER_BASE_URL` | eve_runtime/agent/agent.ts:1-25; mcp/src/agents_remember/serving/eve_runtime_launch.py:67-76 |
| The adapter's launched runtime is what actually consumes this provider, so the stub never appears on a production path. | `EveRuntimeProcess.start` | mcp/src/agents_remember/serving/eve_runtime_client.py:127-157 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stub imitates the OpenAI-compatible chat-completions API, and the runtime reaches it through the pinned `@ai-sdk/openai-compatible` provider. | exact dependency pin | eve_runtime/package.json:14-20 |

## Update History

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): **no content impact from the A2
  revision.** This file is byte-identical between the A1 and A2 candidates of the same change set, so
  the body is retained unchanged; the pass refreshed the verification metadata to the leaf's current
  base `e9300687` and rewrote the three citation tables into the `Finding | Anchor | Source` shape
  (Anchor alone, `path:start-end` plain in Source). No claim was re-worded and no hash or fingerprint
  was invented; the governed closeout stamps the real code commit.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a fixture module added by the
  native eve session-adapter change set. Records that it is a model provider rather than a harness or
  adapter double, the two recorded failure modes that shaped it (module-global plan state causing
  cross-session contamination, and a tool-call opening chunk without identity), and that it is a
  test-only module outside pytest's collection. Verification metadata is pinned to the leaf's base
  commit `67b21aeb` because the candidate is deliberately uncommitted — the governed closeout stamps
  the real code commit, and no hash or fingerprint was invented here.
