# mcp/tests/test_expectation_rows.py

| Field                  | Value                                             |
| ---------------------- | ---------------------------------------------------|
| repository             | agents-remember                                     |
| path                   | `mcp/tests/test_expectation_rows.py`                |
| doc_type               | `file-level-onboarding`                             |
| lastUpdated            | 2026-07-08T16:15+02:00                              |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`|
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Row creation/transition idempotency: `mark_met`/`mark_missed` never overwrite an existing terminal state. | L32-L62 | [test_expectation_rows.py](agents-remember/mcp/tests/test_expectation_rows.py) |
| Store query surface: `pending`, `overdue`, `find_by_source`, `mark_met`/`mark_missed` via the store. | L71-L148 | [test_expectation_rows.py](agents-remember/mcp/tests/test_expectation_rows.py) |
| `orchestration.expectations` SLA-settings parser: defaults, per-kind override, fail-loud validation. | L152-L174 | [test_expectation_rows.py](agents-remember/mcp/tests/test_expectation_rows.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-08T16:15+02:00 — Created for 260707-HFX2-L1 (curator delta round 2, closeout-preview
  gap): store/settings unit coverage for the R2 durable expectation-row primitive. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
