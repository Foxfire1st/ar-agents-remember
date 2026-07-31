# mcp/src/agents_remember/serving/injector.py

| Field                  | Value                                                     |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/injector.py`               |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-10T13:03+02:00                                      |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Diagnostic Boundary

Legacy injector and pane/log timing helpers remain available for offline diagnostics and ordinary
surfaces, but hosted dispatch no longer imports them as an authority or fallback.

## 260731-EFA-L2 Current Delta

Dispatch delivery now calls the **explicit** paster method instead of switching on an optional
argument: a row carrying a `dispatch_policy` goes to `paster.paste_dispatch(tmux_name, text,
accepted=…, policy=…)`, and everything else to `paster.paste(tmux_name, text, submit=True,
accepted=…)`. `paste()` no longer accepts `dispatch_policy` at all.

That also removed a runtime guard: `paste()` used to raise `ValueError("dispatch paste requires a
harness-log acceptance probe")` when a dispatch policy arrived without a probe. `paste_dispatch`
now **requires** `accepted` in its signature, so the same rule is enforced by the type, not by a
branch. A durable brief that cannot be proven accepted must still fail rather than be retried into
a duplicate.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `paste_dispatch` vs `paste` split — the acceptance-probe requirement is now enforced by the signature instead of a runtime `ValueError`.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented removal of hosted log-flush/paste authority.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

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
