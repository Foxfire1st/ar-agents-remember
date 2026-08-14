# mcp/tests/test_inbox_backoff.py

| Field                  | Value                                       |
| ---------------------- | ---------------------------------------------|
| repository             | agents-remember                               |
| path                   | `mcp/tests/test_inbox_backoff.py`             |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-07-09T11:19+02:00                        |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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
`len(BACKOFF_SCHEDULE_SECONDS)` rather than indexing out of range. HFX2-L9 changes the
`next_attempt_at` assertion: attempt `0` now stamps `now + MIN_REDELIVERY_INTERVAL_SECONDS`, and a
sub-floor override raises `ValueError("at least 900 seconds")`. `DueAndRateLimitTests` covers
`is_due`: a fresh entry with no `nextAttemptAt` schedule is due immediately; an entry whose
`nextAttemptAt` is still in the future is not due; one whose `nextAttemptAt` has already passed is
due; a `consumed` entry is never due regardless of its schedule (redelivery only ever targets
unacked rows). `is_rate_limited` covers the separate per-target cooldown: an entry whose
`lastAttemptAt` is inside the 900-second rate-limit window is limited; one outside the window is not;
and a sub-floor rate limit override refuses loudly. HFX2-L8 adds the terminal predicate regression:
a `ladder-resolved` row is never due/redeliverable, regardless
of schedule or delivery state.
`test_redeliverable_filters_due_and_unlimited_entries_only` drives `redeliverable(...)` — the
combinator a sweep actually calls — against three entries (due-and-clear, due-but-rate-limited,
not-yet-due) and asserts only the due-and-clear entry survives, proving `is_due` and
`is_rate_limited` are both applied, not just one.

### Conventions

Plain `unittest.TestCase` classes split by concern (pure backoff math vs. due/rate-limit
predicates); a local keyword-only `_entry(*, entry_id="A", agent_id="agent-a")` helper builds a base
`OperatorInboxEntry` via `create_operator_inbox_entry` — which takes `InboxMessage(ask=…,
response=…)` positionally plus `routing=InboxRouting(address=InboxAddress(lifecycle_id=…,
agent_id=…))` and `poster=InboxPoster(created_by=…, created_via=…)` — and layers
`model_copy(update={...})` for schedule/state variants, matching the fixture style of
`test_operator_inbox.py`. The helper exposes only the two fields any test actually varies, so it is
fully typed and no longer needs the `# type: ignore[arg-type]` its old `**overrides` splat carried.

### Invariants And Boundaries

- The backoff ladder clamps at its ceiling rather than raising or wrapping past its final index —
  the regression that would catch an off-by-one or unclamped lookup.
- `is_due` and `is_rate_limited` are independent predicates; `redeliverable` requires BOTH
  (due AND not rate-limited), after the ladder-resolved exclusion — a sweep that checked only one
  would over- or under-deliver.
- A `consumed` row is categorically excluded from `is_due`, independent of any stamped schedule.
- The early 30/60/300-second ladder rungs no longer make first-send redelivery due before the
  900-second production floor.

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf).

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Backoff ladder climbs then clamps at its ceiling; `next_attempt_at` respects the 900-second floor and rejects sub-floor overrides. | `BackoffMathTests` | mcp/tests/test_inbox_backoff.py:45-69 |
| `is_due`/`is_rate_limited`/`redeliverable` combinator semantics, including the consumed-row, ladder-resolved, 900-second-rate-limit, and sub-floor-refusal cases. | `DueAndRateLimitTests` | mcp/tests/test_inbox_backoff.py:72-128 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:40:21+02:00 — 260731-EFA-L6 curator W2-B10: repaired 4 citation findings (2 reference rows); scoped recheck clean.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2: `create_operator_inbox_entry` moved onto parameter
  objects, which invalidated this card's description of the fixture helper. `_entry` is no longer
  the untyped `**overrides` splat with a `# type: ignore[arg-type]`; it is a keyword-only
  `_entry(*, entry_id="A", agent_id="agent-a")` passing `InboxMessage` positionally plus
  `routing=InboxRouting(address=InboxAddress(...))` and `poster=InboxPoster(...)`. Rewrote
  Conventions to match and re-anchored both Repo-Internal citations for the one-line growth
  (L45-L68 → L46-L69, L71-L127 → L72-L128). No test name, ladder value, floor or predicate
  assertion changed.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: updated redelivery-math tests for the 900-second
  `next_attempt_at` floor, sub-floor refusal, 900-second rate-limit window, and sub-floor
  rate-limit refusal. Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R1): added the ladder-resolved
  exclusion regression asserting terminal rows are never due/redeliverable. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T16:15+02:00 — Created for 260707-HFX2-L1 (curator delta round 2, closeout-preview
  gap): backoff-ladder math and due/rate-limit predicate coverage for the R3 redelivery module.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
