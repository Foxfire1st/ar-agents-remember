# mcp/src/agents_remember/serving/terminal_observer_health.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_observer_health.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T20:42+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured in the resolved memory root; the module implements a
repository-owned serving contract, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact v1 record: eleven required fields, `extra="forbid"`, both counters bounded at the 32-bit ceiling, aware-RFC3339 stamps only. | `TerminalObserverHealthRecord` | mcp/src/agents_remember/serving/terminal_observer_health.py:131-174 |
| The declared wire form: the record plus the four serve-time computed fields, dumped without `exclude_none`. | `TerminalObserverHealthPayload` | mcp/src/agents_remember/serving/terminal_observer_health.py:177-191 |
| The one durable current row: validate-or-`None` read, one atomic replacement write. | `TerminalObserverHealthStore` | mcp/src/agents_remember/serving/terminal_observer_health.py:239-279 |
| The current-lifetime gate and the exact `6 × sweep_interval_seconds` cutoff rule. | `served_terminal_observer_health` | mcp/src/agents_remember/serving/terminal_observer_health.py:282-312 |
| The serving-lifetime accumulator: lifetime start, success and failure transitions, persisted-row reads, and the one fixed write-failure log line. | `TerminalObserverHealthPublisher` | mcp/src/agents_remember/serving/terminal_observer_health.py:315-469 |
| The bounded, ordered, secret-safe failure classification table. | `TERMINAL_OBSERVER_FAILURE_TYPES`; `classify_terminal_observer_failure` | mcp/src/agents_remember/serving/terminal_observer_health.py:82-90; mcp/src/agents_remember/serving/terminal_observer_health.py:122-128 |
| Publication rides the observer CALL for both outcomes, and only the phase separates a startup-prime failure from a steady-pass one. | `_observe_terminal_catalog` | mcp/src/agents_remember/serving/_app_lifespan.py:80-107 |
| The lifespan starts this serving lifetime's accumulator immediately before the prime, and derives the served cutoff from the configured sweep cadence. | `_terminal_observer_health_payload` | mcp/src/agents_remember/serving/_app_lifespan.py:288-352; mcp/src/agents_remember/serving/_app_lifespan.py:376-394 |
| One shared publisher on one observer root and one serving clock, read by the routes and written by the lifespan. | `_ServingRuntime`; `_build_serving_runtime` | mcp/src/agents_remember/serving/_app_common.py:458-479; mcp/src/agents_remember/serving/app.py:198-198; mcp/src/agents_remember/serving/app.py:242-242; mcp/src/agents_remember/serving/app.py:165-251 |
| The additive, omissive fourth tail key on the served workspace projection. | `ServedWorkspaceProjection`; `SERVED_TAIL_FIELDS`; `served_state_tail` | mcp/src/agents_remember/serving/served_state.py:50-66; mcp/src/agents_remember/serving/served_state.py:68-75; mcp/src/agents_remember/serving/served_state.py:81-109 |
| The generated mirror declares this payload and keeps its nulls, and the schema's supported refinement set states the counter ceiling. | `TerminalObserverHealth`; `MAXIMUM`; `SCHEMA_REFINEMENT_KEYWORDS` | dashboard/src/types/projection.ts:802-824; mcp/test_support/agents_remember_test_support/code_quality/projection_types.py:35-59 |
| The module's executable contract: sixteen cases over the record, the writer, publication, and the served tail. | `TerminalObserverHealthRecordTests`; `TerminalObserverHealthLifespanTests`; `TerminalObserverHealthServedTailTests` | mcp/tests/test_terminal_observer_health.py:220-617; mcp/tests/test_terminal_observer_health.py:619-732; mcp/tests/test_terminal_observer_health.py:734-931 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this module; the served
payload crosses a process boundary (browser), not a repository one.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, 13 paths, `git diff | sha256sum` = `b75a785d…`): created this file card for the
  new module. Recorded the current contract rather than a change narrative: the exact
  `ar-terminal-observer-health/v1` record with its eleven required fields and 32-bit counter
  ceiling, the additive `TerminalObserverHealthPayload` wire form dumped without `exclude_none`, the
  validate-or-`None` store over one atomic replacement, the current-lifetime serve gate with the
  exact `6 × sweep_interval_seconds` cutoff, the in-memory transition accumulator that is never
  served, the bounded ordered failure vocabulary, and the fixed write-failure log line. The
  boundaries that make the reading trustworthy are recorded as boundaries: the persisted file is the
  sole serve-time source, omission is the answer for every unusable source including a
  prior-lifetime row, a failed later write leaves the last valid row serving and aging into `stale`,
  GET/SSE never mutate the file, and health is diagnostic only — it owns no cursor, marker, gate or
  queue. Two negative facts are recorded because they are non-obvious: cancellation is deliberately
  not recorded, and a notifier tick is never observer evidence (so a live notifier beside a dead
  observer loop reads `stale`, a conservative direction recorded for the owner rather than as a
  defect). Verification metadata remains closeout-owned; no stamp advanced.
