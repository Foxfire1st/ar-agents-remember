# mcp/tests/eve_fixture_model.py

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
- The trace record gained a **`messages` key** beside the four original ones (`model`, `stream`,
  `messageCount`, `messages`). The four original keys are unchanged; `messages` carries the provider's
  own view of the request, which is the only place a consumer can read the **effective prompt** a model
  would actually receive — the system block and the durable history — instead of inferring it from the
  plan the fixture wrote. This is what makes the capsule scenarios' "the binding reaches the model"
  assertion a measurement rather than a restatement.
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
- **The trace's `messages` field is the effective-prompt evidence, and it must stay the provider's own
  view.** Recording a re-rendered or fixture-constructed message list here would make the capsule
  scenarios assert against the fixture's intent instead of what the model received, which is exactly the
  class of self-confirming evidence the seam's cases are built to avoid.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; the served shape is the OpenAI-compatible chat-completions API, which is a third-party contract this stub imitates rather than a configured domain source.

### Repo-Internal References

- The live fixture starts this stub and points the runtime at it, and is the only consumer. [1]
- The runtime application reads the provider base URL, name and key from the adapter-owned launch environment. [2]
- The adapter's launched runtime is what actually consumes this provider, so the stub never appears on a production path. [3]

### Cross-Repo References

- The stub imitates the OpenAI-compatible chat-completions API, and the runtime reaches it through the pinned `@ai-sdk/openai-compatible` provider. [4]
