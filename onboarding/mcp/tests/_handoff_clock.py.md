# mcp/tests/_handoff_clock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_handoff_clock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T21:25+02:00 |
| lastVerifiedCommitHash | `8ee51cc2cea0be7326937a3b1bbfdad6cafdbd33` |
| lastVerifiedCommitDate | 2026-09-15T21:57:55+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

Reviewed at 2026-09-15T21:25+02:00 against the leaf base `e9678c56`; this module is an uncommitted
candidate at that base, so it does not exist at the commit above and normal closeout owns the final
verification-metadata stamping. The hash records only the base this card was read against.

## Purpose

Shared test support for the observer-to-notifier handoff proof (`LOCR-R04@v1`): the deadline-correct
virtual timeline and the two synchronization primitives that proof needs. It is an instrument, not an
assertion suite — it declares no test case and asserts nothing about production behaviour.

The module exists because the shared `_VirtualClock` in
[test_serving_observation_loop.py](test_serving_observation_loop.py.md) is coherent only while **one**
loop owns the timeline. The handoff harness runs two independently scheduled loops at once (the
observer parked on `P` and the notifier parked on `N`), so that clock's release rule would date the
notifier's wake-up late. `_DeadlineClock` subclasses it and repairs exactly that, leaving the sibling
fixture untouched, so its own consumers keep the clock they were verified against.

## Code Commentary

### Logic

`_DeadlineClock` records each sleep's **deadline** when it parks (`self.seconds + delay`, keyed by the
future's identity) and `release_delay` moves time to that recorded deadline rather than adding the
delay to the current time. The two differ only when the clock has already advanced past a sleep's park
time, which is precisely the two-loop case: adding `N` at a moment the clock has already reached that
sleep's park time plus `N` would date the wake-up late and corrupt both the sweeper's retained rate
limits and every latency measured against the clock. Time never moves backwards (`max`), so a sleep
parked now still expires exactly one delay later and an overdue sleep fires wherever it is released. A
cancelled sleep is removed from the parked list before the `CancelledError` propagates, so a cancelled
pass cannot leave a phantom entry that a later `has_pending` would report as a live loop.

`_Gate` parks one chosen pass until the case releases it. `arm()` sets the armed flag and clears both
events, so arming is also the reset: a case arms the gate immediately before the step whose pass it
wants to park, and the hook that fires next is that pass. The first call after arming clears the flag,
signals `entered` and blocks on `release`. The bounded wait (10 s) turns a gate that is never reached
into a failure rather than a hang — a case that loses its race fails loudly instead of wedging the run.

`_Sequence` gives the events of different threads one real-time total order. Virtual time stands still
while a pass works, so "the read returned before the commit" is not expressible in it; every recorded
event takes its number under one lock instead, which makes that claim a single integer comparison.
`lock` is public and reentrant so a recorder whose callers are different threads can hold the number
and the record that carries it in one critical section: two concurrent callers must not take the same
number, and a record must not be appended between another caller's number and its own record.

### Conventions

Module-local private support classes with a leading underscore, matching the sibling
`_store_durability.py` / `_quality_admission.py` support modules in this directory. The module inserts
`mcp/src` on `sys.path` itself rather than relying on the caller, the same preamble the sibling support
modules use, so it is importable both from the handoff proof and from a focused single-module run. It
starts no process, opens no socket and reads no durable state.

### Invariants And Boundaries

- `_DeadlineClock.sleep` must append the request and the timeline entry **before** awaiting, and must
  remove its own future from `_parked` on cancellation; both are load-bearing for the handoff driver's
  "the loop re-parked, so its attempt settled" wait.
- `release_delay` raises rather than silently doing nothing when no sleep of that delay is parked: a
  driver step that releases a sleep nobody parked is a broken scenario, not a no-op.
- The clock changes virtual time only; it never replaces the loops' scheduling, so it cannot make a
  non-overlapping production loop look overlapping or the reverse.
- `_Sequence.next` is the only public mutator; `value` is read as "the last number handed out", which
  is how the sweep witness counts `refresh()` attempts without a second counter.
- No production module imports this file. It is test-side support only.

### Todos

None. The three primitives are complete for the handoff proof's scenarios; a second consumer that needs
a different release rule should subclass or extend here rather than fork the class.

## Docs References

No Domain Documentation entries are configured in the resolved memory root. Every claim on this card is
about repository-owned test support, so no external domain source is cited.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The declarations below establish the current instrument; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module is test support only and declares no case; it exists to make a two-loop timeline coherent. | `_DeadlineClock` | mcp/tests/_handoff_clock.py:30-74 |
| The imported shared clock this one corrects for two simultaneously parked loops, left byte-unchanged. | `_VirtualClock` | mcp/tests/test_serving_observation_loop.py:115-159 |
| Sleeps park with their own deadline recorded, and a cancelled sleep is removed before the error propagates. | `sleep` | mcp/tests/_handoff_clock.py:47-57 |
| A parked sleep of an exact delay is how the driver proves an attempt settled without racing the loop's cadence. | `has_pending` | mcp/tests/_handoff_clock.py:59-62 |
| Release advances time to the released sleep's own deadline, never backwards, and raises when nothing is parked at that delay. | `release_delay` | mcp/tests/_handoff_clock.py:64-74 |
| One chosen pass is parked until the case releases it; arming is also the reset. | `_Gate`; `arm` | mcp/tests/_handoff_clock.py:77-101; mcp/tests/_handoff_clock.py:90-93 |
| A gate that is never reached fails within a bounded wait instead of hanging the run. | `__call__` | mcp/tests/_handoff_clock.py:95-101 |
| One real-time total order across threads, which is what makes "the read returned before the commit" decidable while virtual time stands still. | `_Sequence`; `next` | mcp/tests/_handoff_clock.py:104-124; mcp/tests/_handoff_clock.py:121-124 |
| The source-root preamble the sibling test-support modules share. | `MCP_SRC` | mcp/tests/_handoff_clock.py:24-25 |
| The handoff proof that is this module's only consumer in the candidate change set. | `ServingNotifierHandoffTests` | mcp/tests/test_serving_notifier_handoff.py:52-376 |

## Cross-Repo References

No separate cross-repository authority is established by this repository-owned test-support module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T21:25+02:00 — 260831-LOCR-L04 curator (uncommitted change set on `ar/260831-locr-l04`,
  base `e9678c56`, `mcp/tests/_handoff_clock.py` new, 124 lines, sha256 `30cb716d…`): created this
  card for the leaf's second new support module. It is an instrument rather than a suite, so the card
  records what each primitive is **for** and where its boundary is, not a case census. Three
  properties are recorded as the reason the module exists rather than as decoration: the deadline rule
  (`seconds = max(seconds, deadline)`) is what keeps a second concurrently parked loop's wake-up from
  being dated late; `_Gate`'s bounded wait converts a lost race into a failure instead of a hang; and
  `_Sequence` exists because "the read returned before the commit" has no expression in virtual time
  once a pass is working. The class is a subclass of the sibling fixture's `_VirtualClock` precisely so
  that fixture's own consumers keep the clock they were verified against. `LOCR-R04@v1` is a
  preservation requirement — the module adds no production behaviour and no production file is touched
  by this change set. Verification metadata is pinned to the leaf base only; the source is an
  uncommitted candidate, so normal closeout owns the final stamping.
