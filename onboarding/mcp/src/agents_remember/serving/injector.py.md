# mcp/src/agents_remember/serving/injector.py

| Field                  | Value                                                     |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/injector.py`               |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-10T13:03+02:00                                      |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`                  |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`injector.py` is the single delivery/classification path for spawn briefs, session commands,
durable inbox rows, redeliveries, signals, and REST paste requests. It transports through tmux but
accepts submitted input only from the target harness's bound JSONL record. Pane text is restricted
to duplicate-retry safety and final failure diagnostics.

## Code Commentary

### Logic

`DeliveryRow` carries one independent input and its existing unique id. `envelope_text` guarantees
that id appears in every non-command message. `deliver` selects a calibrated log window (`40.3 s`
Claude, `29.0 s` Codex), delegates the bounded input ladder to `TerminalPaster`, and returns `acked`
only when `HarnessSessionLog.message_present(entry_id)` succeeds. A bound session command instead
requires `command_evidence(...).succeeded` (command record plus non-error stdout). An unbound spawn
command is transported first as `landed-unacked`; after the brief binds the log,
`verify_or_reissue_command` accepts existing evidence or reissues only the missing/errored command.
Drafts remain `landed-unacked`. A final capture may be labeled `blocked`, but only after log-backed
acceptance failed.

### Conventions

The injector owns acceptance semantics and calibrated windows; `TerminalPaster` owns the fixed
initial/Enter-repress/re-paste transport ladder. Command reissue is a named, narrow operation rather
than a generic second delivery path.

### Invariants And Boundaries

- `deliver(row)` retains the four-way outcome and never returns a bare boolean.
- Submitted acceptance never comes from pane movement, composer content, turn-state glyphs, or knob
  text; only harness-log message/command evidence may produce `acked`.
- Commands and messages are separate entries. A command is never concatenated with a brief.
- Pane modal classification is failure-only diagnostics and cannot override successful log evidence.
- Harness hooks, Agent SDK sessions, and app-server protocols remain outside this delivery channel.

### Todos

Reviewer residual: Codex session commands have no command-record parser today; current settings do
not configure them and Codex effort rides argv. A future change must either add real-record evidence
or refuse that settings shape rather than claiming generic command verification.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for a
one-delivery-path contract; the leaf task doc's R1/R3 and this implementation are the source of
truth, same posture as the other 260707-HFX2-L3 modules.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines the delivery-outcome contract; the leaf task doc (R1, R3) and this implementation are the source of truth. | whole module | [injector.py](injector.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `get_adapter` supplies every per-harness signature (`blocked_reason`, `turn_started`) this module reads. | `HarnessAdapter` | [harness_adapters.py](harness_adapters.py.md) |
| `TerminalPaster.paste` is the transport `deliver` calls exactly once per invocation; its own capture-verify/idempotent-retry loop is UNCHANGED by this leaf. | `TerminalPaster.paste` | [terminal_paste.py](terminal_paste.py.md) |
| `deliver_inbox_entry` builds a `DeliveryRow` (`envelope=False`) and calls `deliver` — the inbox-row half of the ONE path (dispatch/nudge/redelivery/signal-emit, all via `supervisor.py`). | `deliver_inbox_entry` | [inbox_delivery.py](inbox_delivery.py.md) |
| `_deliver_spawn_pastes` builds separate command/brief `DeliveryRow`s and calls `deliver` — the spawn half of the one path. | `_deliver_spawn_pastes` | [terminal.py](../mcp/tools/terminal.py.md) |
| Outcome-mapping unit tests (all four `DeliveryOutcome` branches) plus an end-to-end injection test against a scripted in-memory tmux pane (R5). | `DeliveryOutcomeMappingTests`; `ScriptedTmuxE2ETests` | [../../../tests/test_injector.py](../../../tests/test_injector.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local delivery path. | — | — |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 removal round: made harness JSONL the sole submitted
  acceptance authority, added calibrated per-harness windows and retroactive isolated command
  verification/reissue, and reduced pane use to retry safety/failure diagnostics. Verification
  metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-08T22:30+02:00 — Created for 260707-HFX2-L3 (paste injector hardening, R1 + R3): the ONE
  delivery path — `DeliveryRow`/`DeliveryResult`/`DeliveryOutcome`, `envelope_text`, `deliver`.
  Unifies the previously-separate spawn-brief (`mcp/tools/terminal.py`) and inbox-row
  (`serving/inbox_delivery.py`) paste call sites onto one function and one four-way outcome
  contract, reusing `TerminalPaster`'s existing capture-verify/idempotent-retry loop unchanged and
  `harness_adapters.HarnessAdapter` for the blocked-check + turn-started corroboration. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
