# mcp/src/agents_remember/serving/injector.py

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

## Evidence

### Docs References

No relevant external documentation applies to this local delivery module.

No relevant external documentation applies to this local delivery module.

### Repo-Internal References

- `get_adapter` supplies every per-harness signature (`blocked_reason`, `turn_started`) this module reads. [1]
- `TerminalPaster.paste` is the transport `deliver` calls exactly once per invocation; its own capture-verify/idempotent-retry loop is UNCHANGED by this leaf. [2]
- `deliver_inbox_entry` builds a `DeliveryRow` (`envelope=False`) and calls `deliver` — the inbox-row half of the ONE path (dispatch/nudge/redelivery/signal-emit, all via `agent_notifier.py`). [3]


### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary owns or consumes this local delivery path.

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
