# mcp/src/agents_remember/serving/terminal_observer_health.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the producer stage's **own** health: one atomic current
`observer_root/workspace/terminal-observer-health.json` row describing how recently the terminal
liveness sweeper observed, and what that observation concluded, plus the serve-time payload that
projects it onto `/api/state` and the SSE `snapshot` under the additive `terminalObserverHealth`
key. It exists because the motivating defect is invisible in the health model it sits beside: the
agent-notifier loop can report fresh ticks while nothing calls the sweeper, and one generic
"supervisor healthy" bit preserves exactly that ambiguity. Observer **health** is therefore a
distinct reading from observer **liveness** and from pane **control state** (`LOCR-R17@v1`).

## Code Commentary

### Logic

The module is one store, one record, one payload, one accumulator, and a fixed failure vocabulary.

- Constants `TERMINAL_OBSERVER_HEALTH_SCHEMA_VERSION` (`ar-terminal-observer-health/v1`),
  `TERMINAL_OBSERVER_HEALTH_FILE_NAME`, `TERMINAL_OBSERVER_HEALTH_STALE_SWEEP_MULTIPLIER` (`6`),
  `TERMINAL_OBSERVER_HEALTH_MAX_COUNT` (`2**32 - 1`) and
  `TERMINAL_OBSERVER_HEALTH_WRITE_FAILURE_LOG` fix the schema marker, destination, cutoff rule,
  counter ceiling and the one log line a failed publication may emit
  (`mcp/src/agents_remember/serving/terminal_observer_health.py:48-63`).
- `TERMINAL_OBSERVER_FAILURE_TYPES` is the ordered `isinstance` table
  (`HarnessControlError` → `TimeoutError` → `ConnectionError` → `OSError` → `RuntimeError` →
  `ValueError` → `Exception`); `classify_terminal_observer_failure` returns the first match's fixed
  NAME, never the raised object's own class or text, so a custom `RuntimeError` subclass publishes
  `RuntimeError`. `_PHASE_FAILURE_PUBLICATION` maps `startup`/`steady-state` to the one category and
  the one summary each, and nothing else selects the summary
  (`mcp/src/agents_remember/serving/terminal_observer_health.py:82-107`).
- `TerminalObserverHealthRecord` is the exact durable row: `extra="forbid"`, `frozen=True`, all
  eleven fields REQUIRED (nullable ones included), both serving-lifetime counters bounded at BOTH
  ends (`ge=0, le=TERMINAL_OBSERVER_HEALTH_MAX_COUNT`), and one `_aware_rfc3339` validator that
  rejects an unparseable or offset-less stamp on `servingStartedAt`/`lastAttemptAt`/`lastSuccessAt`
  (`mcp/src/agents_remember/serving/terminal_observer_health.py:131-174`).
- `TerminalObserverHealthPayload` is the declared wire form: the record's fields plus the four
  serve-time computed fields `ageSeconds`, `lastSuccessAgeSeconds`, `staleCutoffSeconds` and
  `status`, serialized WITHOUT `exclude_none` so `lastAttemptAt: null` travels as a reported fact
  (`:177-236`).
- `TerminalObserverHealthStore.read()` is validate-or-`None` over every unusable source, and
  `write()` is exactly one `atomic_write_text` replacement; `served_terminal_observer_health()`
  gates on the CURRENT lifetime's exact `servingStartedAt` and derives the cutoff as
  `6 * sweep_interval_seconds` (`:239-312`).
- `TerminalObserverHealthPublisher` is the serving-lifetime in-memory transition accumulator:
  `start_lifetime()` writes the initial row before the startup prime, `record_success` advances both
  timestamps, increments `attemptCount`, sets the sticky `initialObservationSucceeded`, clears every
  active failure field and resets the consecutive count, `record_failure` advances `lastAttemptAt`,
  increments BOTH counters, RETAINS `lastSuccessAt` and records the phase-selected category/type,
  and `served_payload()` reads the persisted row rather than the accumulator (`:315-469`).

### Conventions

The record is a frozen Pydantic wire model in the serving package's usual shape; the payload
subclasses it additively. Private helpers (`_duration_seconds`, `_current`, `_publish`) are
module-local. Out-of-range arithmetic is clamped rather than raised (`saturate_observer_count`,
`max(0.0, …)`), because the contract states bounds the published values must satisfy.

### Invariants And Boundaries

- **The persisted file is the sole serve-time health source.** The accumulator is not a second
  durable store and is never served directly; it exists only so a failed file write does not erase
  attempt counters from the next full-record publication attempt.
- **Omission is the answer for every unusable source**: no lifetime started, file missing,
  unreadable, non-object, wrong marker, extra or missing key, wrong type, unparseable/naive
  timestamp, or another serving process's `servingStartedAt`. The state request and the SSE snapshot
  still succeed, and no old-lifetime bytes are served.
- **A failed later write leaves the last valid current-lifetime row serving** — the newer in-memory
  accumulator is never substituted — so the served payload can age into `stale` while a newer
  record waits unpublished.
- **GET/SSE never rewrites, deletes, repairs or creates the file**, and no validation failure
  becomes a request failure.
- Publication is diagnostic only: it cannot advance a catalog cursor, stamp a signal marker, admit
  closeout, lock task authoring, or become a queue authority. The read route cannot refresh health,
  so browser traffic never makes the observer look fresh.
- `status` precedence is exact: `stale` whenever `ageSeconds >= staleCutoffSeconds`, else
  `initializing` with no attempt, else `degraded` with an active failure, else `healthy`.
- Failure publication is bounded by construction: only the fixed type NAME, the phase-selected
  category/summary, counters and timestamps reach the record, and a failed write emits only
  `TERMINAL_OBSERVER_HEALTH_WRITE_FAILURE_LOG` — never exception text or a traceback — and never
  raises into the observer's own containment.
- Both counters saturate at `2**32 - 1` on write and are rejected above the ceiling on read, so a
  persisted above-ceiling row is omitted rather than served.
- Negative knowledge, recorded rather than implied: **cancellation is not recorded** — a cancelled
  observer call is incomplete and `CancelledError` is not an `Exception`; and a **notifier tick is
  never observer evidence**, so a live notifier beside a dead observer loop ages the record into
  `stale` while a sweeper call may in fact have completed on the notifier's own inline refresh
  (L14's boundary, byte-identical to base). That direction is conservative — it can never produce a
  false `healthy` — and it is an owner-visible observation, not a defect of this module.

### Todos

None. Any future change to `ServedWorkspaceProjection` or its payload models must be accompanied by
the dashboard companion update (generated mirror, `contract.test.ts` `VOCABULARIES` registry, served
sample in `fixtures/snapshot.json`) and verified with the dashboard typecheck plus the contract
vitest, not only with pytest.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory root; the module implements a
repository-owned serving contract, so no external domain claim is needed.

### Repo-Internal References

- The exact v1 record: eleven required fields, `extra="forbid"`, both counters bounded at the 32-bit ceiling, aware-RFC3339 stamps only. [1]
- The declared wire form: the record plus the four serve-time computed fields, dumped without `exclude_none`. [2]
- The one durable current row: validate-or-`None` read, one atomic replacement write. [3]
- The current-lifetime gate and the exact `6 × sweep_interval_seconds` cutoff rule. [4]
- The serving-lifetime accumulator: lifetime start, success and failure transitions, persisted-row reads, and the one fixed write-failure log line. [5]
- The bounded, ordered, secret-safe failure classification table. [6]
- Publication rides the observer CALL for both outcomes, and only the phase separates a startup-prime failure from a steady-pass one. [7]
- The lifespan starts this serving lifetime's accumulator immediately before the prime, and derives the served cutoff from the configured sweep cadence. [8]
- One shared publisher on one observer root and one serving clock, read by the routes and written by the lifespan. [9]
- The additive, omissive fourth tail key on the served workspace projection. [10]
- The generated mirror declares this payload and keeps its nulls, and the schema's supported refinement set states the counter ceiling. [11]
- The module's executable contract: sixteen cases over the record, the writer, publication, and the served tail. [12]

### Cross-Repo References

No meaningful cross-repository implementation boundary is established by this module; the served
payload crosses a process boundary (browser), not a repository one.
