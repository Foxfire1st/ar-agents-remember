# mcp/tests/test_serving_helper_behaviour.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/tests/test_serving_helper_behaviour.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-31T15:32+02:00                       |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`   |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural coverage for **eight serving helpers whose error and edge arms were untested**.
Every class drives the real helper over real inputs and asserts the value returned, the side
effect left, or the error raised.

## Method

Fakes stop at the **process/network seam only**: the terminal host (tmux kill), the
daemon's TCP probe and pid probe, and the Claude stream transport. The git repositories, the
terminal catalog, the FastAPI app and the contracts are all real. `_StepClock` is a
monotonic clock that advances only when the code under test sleeps, which makes the retry
cadence assertions exact.

## The Eight Helpers

| Class | Helper and the arms it adds |
| --- | --- |
| `ImageSniffTests` | `app._looks_like_image` — the magic-byte half of the paste-upload gate. Every accepted signature (PNG/JPEG/GIF87/GIF89/WEBP/BMP), the cross-format mismatches (a body of one format under another's extension), the too-short WEBP, and the rejected extension. The extension alone never admits a body. |
| `RetireResponseTests` | `app._retire_response` over the real route and catalog — unknown target, unknown actor, already-retired, the policy refusal, and the granted retire with its tmux kill plus persisted provenance. |
| `LeafFileDiffTests` | `changeset.leaf_file_diff` over real git repositories — the memory side, the missing-worktree and no-head refusals, and added/deleted files where one side of the diff is absent. `CodeSide` / `MemorySide` are frozen fixture dataclasses so a side is stated once and its fields cannot disagree; `MemorySide` is one optional object because a memory-less leaf has none of the three. |
| `SelectCurrentModelTests` | `claude_stream_capabilities._select_current_model` — mapping the model id the running harness echoes back onto one catalog key: exact-key precedence, a requested key that resolves to nothing, the sole-alias fallback, and both unresolvable shapes. |
| `ClaudeStatusActivityTests` | `claude_stream_state.ClaudeStreamState._status_activity` — compacting, requesting, blocked behind a pending interaction, idle with no turn, running with one accepted. Each arm distinct. |
| `WaitReadyTests` | `daemon._wait_ready` — the spawn readiness poll needs an alive child **and** an accepting bind within the budget: the wildcard-bind rewrite, a dead child, the retry cadence, the expired budget, and a real listening socket for the ready case. |
| `EvidencePageTests` | `harness_control_client._evidence_page` — every malformed-response refusal fails loudly and typed, plus the empty page and the optional per-frame identity fields. |
| `HeapDiagFramesTests` | `heap_diag._frames` — `AR_HEAP_DIAG_FRAMES` is the tracemalloc traceback depth: the default, the override asserted through the tracer it configures, garbage, a non-positive value, and the ambient-environment read. |

## Invariants And Boundaries

- No PTY, no tmux, no real daemon spawn; the process seam is the only double.
- `_looks_like_image` is a body check, not an extension check — a helper that trusted the
  filename would let any bytes through the paste route.
- `_wait_ready` must require both liveness and an accepting bind; either alone is not ready.
- Malformed control-plane evidence is a typed refusal, never a silently empty page.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The image and retire helpers under test. | "def _looks_like_image(body: bytes, ext: str) -> bool:"; "def _retire_response(" | mcp/src/agents_remember/serving/_app_common.py:160-160; mcp/src/agents_remember/serving/_app_terminal_routes.py:514-514 |
| The repository diff helper under test. | `leaf_file_diff` | mcp/src/agents_remember/serving/changeset.py:433-474 |
| The current-model helper under test. | `_select_current_model` | mcp/src/agents_remember/serving/claude_stream_capabilities.py:86-110 |
| The Claude activity helper under test. | `_status_activity` | mcp/src/agents_remember/serving/claude_stream_state.py:781-788 |
| The daemon readiness helper under test. | `_wait_ready` | mcp/src/agents_remember/serving/daemon.py:378-390 |
| The evidence-page parser under test. | "def _evidence_page(result: object, *, expected_bridge_epoch" | mcp/src/agents_remember/serving/_harness_control_parsing.py:348-348 |
| The heap diagnostic frame helper under test. | `_frames` | mcp/src/agents_remember/serving/heap_diag.py:66-75 |

## Update History
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: narrowed the pooled helper sentence to its cited image and retire owners while preserving the exact-owner rows for diff, model, state, readiness, evidence, and heap.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  serving-helper behavioural suite. Verification metadata is pinned to the leaf's reformat
  commit until closeout stamps the code commit.
