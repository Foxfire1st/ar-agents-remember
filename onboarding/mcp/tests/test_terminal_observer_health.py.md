# mcp/tests/test_terminal_observer_health.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pins `LOCR-R17@v1`'s executable contract for the observer's own health: one exact atomic v1 record,
one exact serve-time payload, one additive omissive tail key, and publication on the observer CALL
for both outcomes. Sixteen cases in three classes: nine drive the record/store/accumulator
directly, two drive the real `_serving_lifespan` where publication ordering and the write-failure
recovery path are the subject, and five drive the served surface. It is deliberately separate from
[test_serving_observation_loop.py](test_serving_observation_loop.py.md), which owns the lifespan's
observation cadence and `LOCR-R11@v1`'s failure boundary, and from
[test_serving_startup_prime.py](test_serving_startup_prime.py.md), which owns the prime's ordering.

## Code Commentary

### Logic

`TerminalObserverHealthRecordTests` (`mcp/tests/test_terminal_observer_health.py:220-617`) pins the
durable row and the writer: the destination observed at the instant of replacement is still the
previous COMPLETE record and an interrupted replacement leaves it readable with no stray temp file
(25 further publications leave exactly one constant-size row); the persisted bytes are the exact v1
field set; both counters saturate at `2**32 - 1` and a persisted above-ceiling row is omitted; a
success → failures → success sequence advances exactly the documented fields, retains
`lastSuccessAt` across failures and resets the consecutive count on success; a failed write keeps
serving the LAST persisted row rather than the newer accumulator; the status ladder is
`initializing` → `degraded` → `healthy` → `stale` with `stale` outranking everything at the exact
cutoff boundary; the cutoff is exactly six configured sweeps; every unusable source (missing,
unreadable, non-object, wrong marker, extra key, missing key, wrong type, unparseable stamp, naive
stamp, prior-lifetime stamp, above-ceiling counter) omits the key and is left byte-identical rather
than repaired; and classification is bounded, ordered and secret-safe.

`TerminalObserverHealthLifespanTests` (`:619-732`) drives the real lifespan: the prime's own outcome
is the serving lifetime's first published transition (call 1), every steady pass publishes success
and failure distinctly with the phase-selected category, and a health-write failure logs only the
fixed line and lets the next observation retry the complete record.

`TerminalObserverHealthServedTailTests` (`:734-931`) drives the served surface through the real
`_state_response` handler and the real `stream_events` generator against stub projectors: the tail is
additive and leaves every existing served field byte-identical; `/api/state` serves the key without
touching revision, ETag or the 304 path; the SSE `snapshot` carries health while a `delta` carries no
tail; a fresh notifier cannot mask a stale or failed observer (cross-read rows 2, 3 and 5); and a
current success beside a fresh notifier reads `healthy` from its OWN row (row 4), with the health
half's provenance proved by equating every health fact to the persisted record and by showing the
notifier's later tick advanced no health counter (`ageSeconds` 1.0, not the notifier's 0.0).

Module-local harness: `_Clock` (`:101`), `_RouteProjector` (`:115`), `_StreamProjector` (`:128`) and
`_SecretTokenError` (`:216`), the last a `RuntimeError` subclass used to prove a custom class name
cannot reach the wire.

### Conventions

`unittest` / `unittest.IsolatedAsyncioTestCase` with module-local private harness classes and
temporary roots. Every case is a unit-lane case: no HTTP transport, no server, no real second. The
route half calls the production handler and generator directly rather than starting an ASGI app —
the integration population had only three cases of headroom, and the brief forbids raising it — so
the ETag/304 branch, the assembled body and the snapshot/delta asymmetry exercised are the
production ones.

### Invariants And Boundaries

The cases assert the contract, not a convenience reading of it: omission is asserted together with
byte-identity of the source file (so "no repair" is proved, not assumed), the failed-write case
asserts the persisted row rather than the newer accumulator, and the cross-read case asserts the
health half's provenance rather than only its status word. The module claims nothing about the
notifier's own internals, about the observer's cadence (the sibling module owns it), or about the
pre-serve prime's ordering. Written exceptions are asserted by their base category, never by message
or class text.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved memory root; the module tests a
repository-owned serving contract, so no external domain claim is needed.

### Repo-Internal References

- The record, writer and accumulator contract: exact v1 bytes, one atomic replacement, saturating counters, the failed-write source of truth, and the status ladder at the exact cutoff. [1]
- Every unusable source omits the wire key and is never repaired, including a prior-lifetime row and an above-ceiling counter. [2]
- Classification is bounded, ordered and secret-safe; a custom subclass publishes its base category. [3]
- Publication rides the observer call: the prime's own outcome is the first transition and both outcomes publish distinctly. [4]
- A health-write failure emits only the fixed log line and retries the complete record next observation. [5]
- The served tail is additive and omissive, and the read routes never mutate the row. [6]
- The cross-read table: a fresh notifier cannot mask a stale or failed observer, and a current success beside a fresh notifier reads healthy from its own row. [7]
- The served surface the cases drive: the fourth tail key and the payload model it carries. [8]
- The publication seam and the served payload the cases enter through the real lifespan and the real route handler. [9]
- The module is registered exactly once, in the explicit unit-regression lane. [10]

### Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.
