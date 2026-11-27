# mcp/src/agents_remember/application/knowledge_writer/handoff_test_names.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Single parser for test spellings cited in hand-off evidence strings (MIK-R28 rule 2): Python test IDs, JS/TS test cases, single-identifier pytest `-k` selections, and bare test files.

## Code Commentary

Defines compiled patterns for JS/TS cases (`CASE_PROOF` and JSON-quoted `_CASE_EVIDENCE` on `*.{test,spec}.{c,m,}[jt]s[x]`), Python test IDs (`TEST_ID`: `<path>.py::name[::member]*`), single-identifier pytest `-k` selections (`_SELECTED_TEST`, explicitly refusing compound `and`/`or`/`not` expressions), and bare pytest files (`_TEST_FILE`: `test_*.py` / `*_test.py` not followed by `::`, ignoring helper modules like `conftest.py`). `TestReference(path, name)` stores Python nested names with `.` (`Class.method`) and renders `spelling` back to `path::Class::method` for `.py` paths (verbatim `path::name` otherwise). `TestFileMention(path)` flags a test file mentioned without naming a test inside it. `tests_named_in(evidence)` scans all evidence strings, suppresses `TestFileMention` for any file that already has a `TestReference` anywhere in `evidence`, sorts matches by `(evidence_index, char_offset)`, and deduplicates preserving first appearance. It performs purely lexical extraction and does not resolve whether tests exist at C.

## Relationships

Imported by `knowledge_writer/handoff.py` (`CASE_PROOF`, `TEST_ID`, `TestFileMention`, `TestReference`, `tests_named_in`). Has no internal dependencies outside the Python standard library.

## Evidence

- Regex definitions recognize JS/TS `path::"title"` cases, Python `path.py::name` IDs, single-identifier `path.py -k name` selections (excluding boolean expressions), and bare `test_*.py`/`*_test.py` file mentions. [1]
- `TestReference.spelling` formats Python dotted symbols back to `path::Class::method` while preserving non-Python case titles. [2]
- `TestFileMention` represents a bare test file mention from which no specific proof can be prepared. [3]
- `tests_named_in` returns deduplicated `TestReference` and unshadowed `TestFileMention` items in evidence appearance order without resolving against C. [4]
