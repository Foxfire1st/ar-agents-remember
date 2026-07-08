# mcp/tests/test_inbox_backoff.py

| Field                  | Value                                       |
| ---------------------- | ---------------------------------------------|
| repository             | agents-remember                               |
| path                   | `mcp/tests/test_inbox_backoff.py`             |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-07-08T23:59+02:00                        |
| lastVerifiedCommitHash | `5f9163882857114319552d303e2e301082b588ba`|
| lastVerifiedCommitDate | 2026-07-08T18:21:20+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

R3 (260707-HFX2-L1) unit tests for `controlplane/inbox_backoff.py`'s redelivery backoff ladder
math and per-target rate limiting — the predicate an L2 redelivery sweep will use to decide which
pending, unacked `OperatorInboxEntry` rows are due for another delivery attempt right now.

## Code Commentary

### Logic

`BackoffMathTests` pins `backoff_seconds_for_attempt`: it returns the ladder's per-index value for
in-range attempt counts and clamps at the ladder's final (ceiling) value for any attempt count past
`len(BACKOFF_SCHEDULE_SECONDS)` rather than indexing out of range; `next_attempt_at` stamps
`now + backoff_seconds_for_attempt(attempt_count)` for attempt `0`. `DueAndRateLimitTests` covers
`is_due`: a fresh entry with no `nextAttemptAt` schedule is due immediately; an entry whose
`nextAttemptAt` is still in the future is not due; one whose `nextAttemptAt` has already passed is
due; a `consumed` entry is never due regardless of its schedule (redelivery only ever targets
unacked rows). `is_rate_limited` covers the separate per-target cooldown: an entry whose
`lastAttemptAt` is inside the rate-limit window is limited; one outside the window is not. HFX2-L8
adds the terminal predicate regression: a `ladder-resolved` row is never due/redeliverable, regardless
of schedule or delivery state.
`test_redeliverable_filters_due_and_unlimited_entries_only` drives `redeliverable(...)` — the
combinator a sweep actually calls — against three entries (due-and-clear, due-but-rate-limited,
not-yet-due) and asserts only the due-and-clear entry survives, proving `is_due` and
`is_rate_limited` are both applied, not just one.

### Conventions

Plain `unittest.TestCase` classes split by concern (pure backoff math vs. due/rate-limit
predicates); a local `_entry(**overrides)` helper builds a base `OperatorInboxEntry` via
`create_operator_inbox_entry` and layers `model_copy(update={...})` for schedule/state variants,
matching the fixture style of `test_operator_inbox.py`.

### Invariants And Boundaries

- The backoff ladder clamps at its ceiling rather than raising or wrapping past its final index —
  the regression that would catch an off-by-one or unclamped lookup.
- `is_due` and `is_rate_limited` are independent predicates; `redeliverable` requires BOTH
  (due AND not rate-limited), after the ladder-resolved exclusion — a sweep that checked only one
  would over- or under-deliver.
- A `consumed` row is categorically excluded from `is_due`, independent of any stamped schedule.

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf).

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Backoff ladder climbs then clamps at its ceiling; `next_attempt_at` adds the ladder offset. | L43-L58 | [test_inbox_backoff.py](agents-remember/mcp/tests/test_inbox_backoff.py) |
| `is_due`/`is_rate_limited`/`redeliverable` combinator semantics, including the consumed-row and ladder-resolved exclusions. | L62-L103 | [test_inbox_backoff.py](agents-remember/mcp/tests/test_inbox_backoff.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R1): added the ladder-resolved
  exclusion regression asserting terminal rows are never due/redeliverable. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T16:15+02:00 — Created for 260707-HFX2-L1 (curator delta round 2, closeout-preview
  gap): backoff-ladder math and due/rate-limit predicate coverage for the R3 redelivery module.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
