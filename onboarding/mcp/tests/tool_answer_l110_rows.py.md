# mcp/tests/tool_answer_l110_rows.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds MIK-R110's landed row data: for each subject it names the answer fields, the uses, the token bound and the
production paths, so the answer-size table can be checked without the data being restated in the test.

## Code Commentary

### Logic

Each subject is a block of four values — a `*_ROW_FIELDS` set of the keys an answer may carry, a `*_ROW_USES` map
of what each field is for, a `*_ROW_BOUND` token ceiling and a `*_PRODUCTION_PATHS` tuple of the paths the answer
is produced on. The blocks cover the coherence, citation-fix, quality, route, integrity, knowledge-write, drift,
migrate and baseline-adopt/status answers.

- The `COHERENCE_` block bounds the coherence answer at 850 tokens over `status`, `prepare`, `publish` and
  `validate`.
- The `CITATION_FIX_` block bounds it at 1500 tokens over `converted` and `unconverted`.
- `BASELINE_ADOPT_ROW_USES` and `BASELINE_STATUS_ROW_USES` carry the baseline rows' uses.
- The `USER_SETTINGS_INIT_` block names the settings answer's state, target and path, its changed and preserved keys, role-harness choices and refusal detail. It carries no settings-file text. Its bound is 900 tokens, its production-path tuple is `("path",)`, and `L110_ROW_DATA` includes that block. These are authored row declarations, not evidence that a settings write ran.

### Conventions

The data lives here rather than in the checking module so one subject's row is changed in one place; a case reads
these structures and asserts on the answers the product returns.

### Invariants And Boundaries

- A row's fields are exactly the keys its answer may carry, and its bound is a token ceiling rather than a byte or
  line count.

## Evidence

- MIK-R110's row data: fields, uses, bounds and production paths per subject. [1]

- Actual delivery guard must preserve an in-bound projection — `assert_answer_survives_the_guard` in mcp/tests/tool_answer_l110_rows.py. [2]
- Generic strip-and-cap supplies cases for unprojected tools — `delivery_shaped` in mcp/tests/tool_answer_l110_rows.py. [3]

- The quality row admits cutCardCount, addedFileCount, cutCards and addedFiles [4]


- Authored uses distinguish cut justification/addition requirement placement from blocking repair work [5]

- Quality row bound remains1500 with sync/start/poll production paths — mcp/tests/tool_answer_l110_rows.py:227-228. [6]
- Baseline status names the caller use of legacyCards — `BASELINE_STATUS_ROW_USES` in mcp/tests/tool_answer_l110_rows.py. [7]
- Baseline adoption names the caller use of legacyCards — `BASELINE_ADOPT_ROW_USES` in mcp/tests/tool_answer_l110_rows.py. [8]
- The quality row names informational proof coverage and actual cache-build/stale/error counters without changing its bound or production paths — mcp/tests/tool_answer_l110_rows.py:158-234. [9]

- The user-settings row declares its caller uses and 900-token bound without returning the settings file text. [10]
