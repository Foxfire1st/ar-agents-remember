# mcp/tests/test_attention_native_kinds.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pins each builder's row: identity, class, the task it opens, the settled deadline, the dismissibility every kind
carries, and the newest-first ranking a mixed native queue takes through the real queue builder.

## Code Commentary

The deadline cases pin no row at 899 seconds and one at 900 — whose id carries the interval start it was
published under — no row for a working or unknown task, none for a planned, completed or aborted stage, and the
identity `task-stalled:{key}:{interval start}` with its task reference.

The last case pins that a declared wait is no stall: a task whose `activity` is `waiting` yields no row whatever its stall clock (:574-580). That the stall reader itself counts no silence while a seat's declared wait has its check to come is pinned in `mcp/tests/test_attention_native_wait_clock.py`.

The stall-break cases are the ones that matter for the detail: the row's detail does not move while only the age
grows, an old task event stamp never dates the interval, a paused master suppresses its started child, the same
child stalls again when no key is paused, and an unrelated paused master suppresses nothing.

The permission and held cases pin one row per prompt with two stable ids, no row for an agent with none, a bound
prompt's task key against a taskless prompt's `None`, a held row naming its store row and only its safe reason,
and a second held message as a second row. The notice and ranking cases pin a dismissible information occurrence,
an acknowledgement hiding one occurrence while a later one stays visible, and the order a mixed native and
operational queue takes.

### 20261023-L190-v2 Identity, Dismissibility And Newest-First

The stall id carries the interval start, so the 899/900
case computes its expectation from the same `_ago(idle_seconds)` stamp the facts carry (:171-177), and the
detail-stability case holds that stamp fixed while advancing `now` — an age-only pass moves `waitSeconds` under an
id that does not move (:193-206). The three live kinds assert `dismissible is True` (:151, :190, :316). The mixed
native/operational queue asserts newest-first: the notice, then the dated prompts, then the
held row, then the stalled task (:354-405).

## Evidence boundary

Source-level pytest cases, in memory over facts and the real `build_attention_queue`, not a live-page witness and
no measurement. The remaining operational kinds and the refusal of the retired provider kinds are covered by
`mcp/tests/test_observer_projection_attention.py`, not here.
