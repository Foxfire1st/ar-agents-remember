# mcp/src/agents_remember/serving/injector.py

| Field                  | Value                                                     |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/injector.py`               |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-08T22:30+02:00                                      |
| lastVerifiedCommitHash | `75587f00070ae0903e42a2a677c51c3125eb7188`                  |
| lastVerifiedCommitDate | 2026-07-08T08:46:23+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Created for 260707-HFX2-L3 (paste injector hardening, R1 + R3): the ONE delivery path every payload
class — spawn briefs, dispatch orders, nudges, redeliveries, expectation-timeout wake-ups — funnels
through. Developer ruling (2026-07-07T22:45, verbatim): "As injector we will then use the paste into
chat method... This is the one thing we got all the control over we need." Before this leaf, two
independent call sites talked to `TerminalPaster.paste` directly (the spawn-brief path in
`mcp/tools/terminal.py`, and `serving/inbox_delivery.py`); this module is now the single funnel both
route through, returning a four-way `DeliveryOutcome` instead of raw booleans.

## Code Commentary

### Logic

`DeliveryRow` is the standardized payload envelope (R3): `kind`, `entry_id`, `text`,
`ack_instruction` (optional), `submit`, `envelope` (bool — `False` skips rendering the header into
the pasted bytes; used by both current callers, see Invariants). `envelope_text(row)` renders the
header (`"[Agents Remember delivery:{kind} id={entry_id}]"` + an optional `"ack: ..."` line) prefixed
to `row.text`, or `row.text` verbatim when `envelope=False`.

`deliver(row, *, tmux_name, paster, harness=None)`:
1. Calls `paster.paste(tmux_name, envelope_text(row), submit=row.submit)` — `TerminalPaster`'s own
   capture-verified, non-blind-retrying dance across the harness boot window is UNCHANGED and still
   owns the actual paste attempt(s).
2. Reads `get_adapter(harness).blocked_reason(outcome.capture)` against the FINAL capture. A modal
   trap (codex quota/rate-limit #20, a permission prompt) OVERRIDES every other reading — a paste
   that nominally "landed" into a modal is `blocked(reason)`, never treated as delivered.
3. `not outcome.delivered` → `failed(reason="paste was not capture-verified as landed")`.
4. `not row.submit` → `landed-unacked(reason="draft-only delivery (submit=False)")`.
5. Submitted: `adapter.turn_started(outcome.capture, advanced=outcome.submitted)` — `True` (via the
   paster's own advance flag OR the harness-aware spinner corroboration) → `acked`; `False` →
   `landed-unacked(reason="submitted but the turn did not visibly start")` (closes drop point 8,
   "delivered into a dead turn").

### Conventions

The injector NEVER retries — `TerminalPaster` already retries internally, but only after
re-capturing proof the previous attempt did not land (the F-V lesson, untouched by this leaf). A
second `deliver()` call for the same row is the CALLER's decision (the L2 supervisor owns retries
against the four-way outcome), never this module's.

### Invariants And Boundaries

- R1 contract: `deliver(row) -> {acked, landed-unacked, blocked(reason), failed(reason)}` — never a
  bare boolean.
- R4 non-goals (developer-ruled): harness hooks, Agent SDK sessions, and the codex app-server
  protocol are NOT delivery channels here or anywhere downstream. A future harness adds one
  `HarnessAdapter` registration (`harness_adapters.py`), never a second `deliver`.
- `envelope=False` on BOTH current callers, for two DIFFERENT reasons, documented on `DeliveryRow`:
  the spawn path's first paste must stay byte-identical to the pre-existing wire format (other
  machinery — the `briefed-by` expectation row, `contextDelivered` — already keys off the session,
  not a parsed header, and changing the first bytes a fresh harness composer receives would be an
  undocumented behavior change); the inbox path's `_push_text` already renders an equivalent header
  (`from:`/`entry:`/`ack:`) so a second wrapper would be redundant. `envelope_text`'s header-rendering
  path IS exercised (`EnvelopeTests`, `test_envelope_text_is_what_gets_pasted`) for a future payload
  kind that carries no header of its own.
- `blocked` is classified from the FINAL pane capture (post-paste-attempt), not a separate pre-paste
  read — no new tmux round-trip, no new injectable capturer parameter.

### Todos

No known follow-up in this file. A future leaf could widen `InboxDeliveryState` (currently pinned
unchanged by `inbox_delivery.py`, see that file's Invariants) to carry `blocked` as a first-class
dashboard-visible state instead of a `deliveryDetail` string prefix — deliberately out of this
leaf's scope (bigger blast radius: dashboard type, `inbox_backoff.py`).

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
| `_deliver_spawn_pastes` builds `DeliveryRow`s (`envelope=False`) and calls `deliver` — the spawn-brief half of the ONE path; the raw-spawn seam's separate delivery loop is retired into this call. | `_deliver_spawn_pastes` | [../../mcp/tools/terminal.py](../../mcp/tools/terminal.py.md) |
| Outcome-mapping unit tests (all four `DeliveryOutcome` branches) plus an end-to-end injection test against a scripted in-memory tmux pane (R5). | `DeliveryOutcomeMappingTests`; `ScriptedTmuxE2ETests` | [../../../tests/test_injector.py](../../../tests/test_injector.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local delivery path. | — | — |

## Update History

- 2026-07-08T22:30+02:00 — Created for 260707-HFX2-L3 (paste injector hardening, R1 + R3): the ONE
  delivery path — `DeliveryRow`/`DeliveryResult`/`DeliveryOutcome`, `envelope_text`, `deliver`.
  Unifies the previously-separate spawn-brief (`mcp/tools/terminal.py`) and inbox-row
  (`serving/inbox_delivery.py`) paste call sites onto one function and one four-way outcome
  contract, reusing `TerminalPaster`'s existing capture-verify/idempotent-retry loop unchanged and
  `harness_adapters.HarnessAdapter` for the blocked-check + turn-started corroboration. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
