# mcp/tests/_pi_rpc_capabilities.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/_pi_rpc_capabilities.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Observe an installed Pi's RPC capability surface by driving the real process, so that
`fixtures/pi_rpc/<version>-capabilities.json` is a **recording** rather than a
hand-maintained file. Every field in the fixture is produced here from a Pi the suite
installed and drove: the version from `pi --version`, the framing from the bytes the
process actually wrote and read, the state fields from a live `get_state`, the events
from a real offline agent run, and the extension UI methods from a probe extension that
calls every one of them.

This is a helper module (leading underscore, not collected by pytest). Its only consumer
is `test_pi_rpc_real_smoke.py`, which compares the observation against the committed
fixture and fails on any disagreement.

## Code Commentary

### Public Surface

| Symbol | What it is |
| --- | --- |
| `CAPABILITY_SCHEMA` | `"ar-pi-rpc-capabilities/v1"` — the `schema` value the fixture must carry. |
| `ObservedCapabilities` | Frozen dataclass: `version`, `framing`, `dispatched_commands`, `unknown_command_rejected`, `state_fields`, `events`, `dialog_methods`, `fire_and_forget_methods`. |
| `observe_capabilities(executable, *, workspace, commands)` | Drives the installed Pi and returns `ObservedCapabilities`. |
| `observe_version(executable)` | The version string the installed binary reports for itself. |
| `PiRpcProbe` | One installed Pi process driven with strict LF-delimited JSONL. |

### Why The Probe Is Not The Adapter

`PiRpcProbe` deliberately re-implements framing rather than reusing
`serving/pi_rpc_process.py`. The adapter is the thing whose assumptions are under test; a
probe that reused it could only ever agree with it. The probe reads stdout with raw
`os.read`, keeps both the decoded frames and the untouched bytes (`raw`), and splits on
`\n` itself.

### How Each Recorded Field Is Observed

- **framing** — `_observe_framing` sets a session name containing U+2028 and U+2029 and
  proves the value survives inside one LF-delimited record (`unicodeLineSeparatorsAreContent`),
  sends a deliberately CRLF-terminated `get_state` and proves it still parses
  (`acceptsTrailingCR`), and reports `delimiter` from whether a CR appears in the raw
  stream at all.
- **commands** — `_sweep_commands` dispatches each claimed command with the minimum
  arguments its handler needs. `_accepted` treats any response that is not
  `error: "Unknown command…"` as dispatched, because a handler answering
  `success: false` for its own reasons still proves the command reached a handler.
- **the negative control** — `UNKNOWN_COMMAND_CONTROL = "ar_probe_not_a_pi_command"` is
  probed alongside them. Without it, "every recorded command was accepted" proves nothing:
  a runtime that silently swallowed everything would look identical. The smoke test
  asserts `unknown_command_rejected`.
- **turn commands** — `prompt`, `abort` and `extension_ui_response` are in
  `DRIVEN_SEPARATELY`. The first two start and end a turn, so they are driven by
  `_exercise_agent_run` rather than by the plain sweep (which must not leave Pi
  streaming). `extension_ui_response` is not a command at all — it is an inbound reply
  frame — and is proven instead by the dialog round-trip.
- **events** — `_exercise_agent_run` points Pi at `UNREACHABLE_ENDPOINT`
  (`http://127.0.0.1:9/v1`, the discard port), so a prompt runs the real streaming and
  auto-retry paths with no network egress; that is the only way `auto_retry_start` /
  `auto_retry_end` become observable without a provider account.
  `_exercise_queue_and_compaction` provokes `queue_update` and the compaction pair.
- **UI methods** — `PROBE_EXTENSION_SOURCE` is a TypeScript extension that calls all nine
  `ctx.ui.*` methods. The dialog/fire-and-forget split is *measured*, not assumed: the
  probe answers every request it saw, and each dialog announces its own resolution through
  `notify("resolved:<method>")`. `dialog = emitted & resolved`; everything else is
  fire-and-forget.
- **state fields** — `_observe_state_fields` reads the keys of a live `get_state`
  response and raises if Pi answers with no data mapping.

### Invariants And Boundaries

- The probe launches with `--mode rpc`, `--no-extensions`, and `OFFLINE_FLAGS`
  (`--offline`, `--no-skills`, `--no-prompt-templates`, `--no-themes`,
  `--no-context-files`), a synthetic `models.json` pointing at the discard port, and an
  isolated `HOME` / `PI_CODING_AGENT_DIR`. No network egress and no provider credential is
  ever required.
- `_require_path` refuses to launch without `PATH`; the child environment is built
  explicitly rather than inherited.
- `close()` suppresses `BrokenPipeError` on stdin close (the child exits on its own once
  its work is done, so the close can race it), waits, then kills on timeout, joins the
  reader thread and closes both streams — nothing is leaked into the rest of the suite.
- `frames` / `raw` are lock-guarded; the reader runs on a daemon thread.

### Todos

None known for this leaf.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The only consumer: installs the pinned Pi, calls `observe_capabilities`, and asserts the recording still describes it. | [test_pi_rpc_real_smoke.py](agents-remember/mcp/tests/test_pi_rpc_real_smoke.py) |
| The recording this module produces the evidence for. | [0.80.7-capabilities.json](agents-remember/mcp/tests/fixtures/pi_rpc/0.80.7-capabilities.json) |
| The product framing/protocol this probe deliberately does not reuse. | [pi_rpc_process.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_process.py) |
| The parser whose state-field dependencies the recording must keep listing. | [pi_rpc_protocol.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_protocol.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  capability-observation helper (probe, negative control, per-field observation method,
  measured dialog/fire-and-forget split). Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
