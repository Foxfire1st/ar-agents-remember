# mcp/tests/test_expectation_rows.py

| Field                  | Value                                             |
| ---------------------- | ---------------------------------------------------|
| repository             | agents-remember                                     |
| path                   | `mcp/tests/test_expectation_rows.py`                |
| doc_type               | `file-level-onboarding`                             |
| lastUpdated            | 2026-07-08T16:15+02:00                              |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                                    |

## Governing Overview

[overview.md](../overview.md)

## Purpose

R2 (260707-HFX2-L1) unit tests for the durable expectation-row primitive itself: row
creation/transition semantics in `controlplane/expectation_rows.py`, the `ExpectationRowStore`
append/fold/query surface, and the `orchestration.expectations` SLA-settings parser in
`kernel/agentic_settings.py`.

## Code Commentary

### Logic

Since 260731-EFA-L2 both builders take a frozen `Expectation(kind, source_id, subject, note)` as
their first positional argument — `create_expectation_row(expectation, *, row_id, now, due_at)` and
`write_expectation_row(store, expectation, *, row_id, now, sla_seconds)` — with the addressee
nested one level deeper as `ExpectationSubject(agent_id, lifecycle_id, leaf_key, seat_role)`. The
former loose `kind=`, `source_id=` and `subject_agent_id=` keywords are gone; `row_id`, `now`,
`due_at` and `sla_seconds` stay keyword-only, because the clock and the row identity are minted by
the caller while everything else about an expectation travels together.

`ExpectationRowRecordTests` covers the pure builders: `create_expectation_row` stamps `dueAt` from
`due_at_from_sla`, `mark_met` is idempotent (a second `mark_met` call does not move `metAt`), and
`mark_missed` refuses to overwrite an already-`met` row (the first terminal transition wins,
per-row). `ExpectationRowStoreTests` drives the JSONL-backed store: `write_expectation_row` appends
a pending row; `pending()` excludes rows already marked `met`; `overdue(now=)` returns only rows
whose `dueAt` has passed, proven with one row past its SLA and a sibling still inside its (much
longer) SLA window; `find_by_source(source_id, kind=)` resolves a row by its dispatch-surface id
and kind, returning `None` for a wrong kind or an unknown source; `mark_missed` via the store
transitions a row to `missed` and removes it from `pending()` (reserved for the L2 sweep ladder,
not called by this leaf's dispatch surfaces); `mark_met` on a missing row id raises `KeyError`.
`ExpectationSettingsParserTests` covers `_parse_expectations`: an absent settings block returns
`DEFAULT_EXPECTATION_SLA_SECONDS` for every kind; a partial `defaults` override replaces only the
named kind's SLA and leaves the others at their documented default; an unknown expectation kind, a
non-positive SLA value, or an unknown top-level settings field each fail loud with
`AgenticSettingsError` rather than silently accepting malformed configuration.

### Conventions

Plain `unittest.TestCase` classes split by concern (record semantics / store semantics / settings
parsing), matching the sibling `test_agentic_settings.py` and `test_operator_inbox.py` layering
style; the store tests use a `tempfile.TemporaryDirectory()` fixture via `self.addCleanup`.

### Invariants And Boundaries

- `mark_met`/`mark_missed` are idempotent past the FIRST terminal transition — this is the
  regression that would catch either function ever overwriting an existing terminal state.
- The settings parser fails loud (never silently defaults) on unknown kinds, non-positive SLAs, or
  unknown top-level fields — pinned so a typo'd settings block cannot silently disable an SLA.

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
| Row creation/transition idempotency: `mark_met`/`mark_missed` never overwrite an existing terminal state. | "def test_mark_met_is_idempotent" | mcp/tests/test_expectation_rows.py:46-46 |
| Store query surface: `pending`, `overdue`, `find_by_source`, `mark_met`/`mark_missed` via the store. | "def test_pending_excludes_met_rows" | mcp/tests/test_expectation_rows.py:91-91 |
| `orchestration.expectations` SLA-settings parser: defaults, per-kind override, fail-loud validation. | "class ExpectationRowRecordTests" | mcp/tests/test_expectation_rows.py:33-33 |
| "class Expectation" | "class Expectation:" | mcp/src/agents_remember/controlplane/expectation_rows.py:79-79 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and source-backed ranges; exact non-fixing check returns zero findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` pass changed both builders this
  suite exercises, so the card now states the current call shape and its own-source citations were
  re-derived. `create_expectation_row` and `write_expectation_row` take a frozen `Expectation` as
  their first positional argument, carrying the kind, the source id, the nested
  `ExpectationSubject` address and an optional note; the loose `kind=`, `source_id=` and
  `subject_agent_id=` keywords no longer exist, while `row_id`, `now`, `due_at` and `sla_seconds`
  remain keyword-only. Nine call sites were rewritten and the import block grew by two names, which
  moved all three own-file ranges in the references table: the record tests from L32-L62 to L34-L66,
  the store tests from L71-L148 to L75-L149, and the settings-parser tests from L152-L174 to
  L153-L175. Each corrected range was re-read at its new position, and a row was added pointing at
  the parameter objects themselves. No behavioural claim moved: the seeded kinds, source ids, SLA
  seconds and subject agent are the same values as before, the idempotency and fail-loud invariants
  are untouched, and `find_by_source("entry-1", kind="ack-by")` still reads exactly as documented.
  Verification metadata stays pinned until closeout stamps the code commit.

- 2026-07-08T16:15+02:00 — Created for 260707-HFX2-L1 (curator delta round 2, closeout-preview
  gap): store/settings unit coverage for the R2 durable expectation-row primitive. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
