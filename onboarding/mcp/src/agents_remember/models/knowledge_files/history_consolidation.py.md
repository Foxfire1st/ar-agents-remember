# mcp/src/agents_remember/models/knowledge_files/history_consolidation.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Defines the consolidation-pass history row vocabulary (`stands`, `unresolved`) and the Pydantic test-evidence models (`TestRun`, `TestNotRun`, `ConsolidationEvidence`) carried on rule and family history rows.

## Code Commentary

Exports `STANDS = "stands"`, `UNRESOLVED = "unresolved"`, and `CONSOLIDATION_DISPOSITIONS = (STANDS, UNRESOLVED)`. `TestRun` (`{test: Label, result: Literal["passed", "failed"]}`) and `TestNotRun` (`{test: Label, reason: Text}`) extend `FileModel` (strict `extra="forbid"`) and set `__test__ = False` to keep pytest from collecting them as test classes. `ConsolidationEvidence` defines optional aliased fields `testsRun` (`min_length=1`), `testsNotRun` (`min_length=1`), and `noProofRecorded: Literal[True] | None` (omitted rather than `false`). Its `@model_validator(mode="after")` `_require_distinct_tests` forbids naming the same test more than once across `testsRun` and `testsNotRun`, and `names_tests()` reports whether any test fact is present. This module validates shape only; which rows must carry test evidence in a consolidation task is enforced by `knowledge_writer/row_tests.py`.

## Relationships

Imported by `models/knowledge_files/history.py` (`CONSOLIDATION_DISPOSITIONS`, `STANDS`, `ConsolidationEvidence`), `application/knowledge_worklist/consolidation.py` (`STANDS`, `UNRESOLVED`), `application/knowledge_gate/predicates.py` (`CONSOLIDATION_DISPOSITIONS`), `application/knowledge_writer/row_tests.py` (`ConsolidationEvidence`), and `memory/knowledge_index/consolidation_outcomes.py` (`UNRESOLVED`). Depends on `models.knowledge_files.shapes`.

## Evidence

- `CONSOLIDATION_DISPOSITIONS` pairs the `STANDS` (`"stands"`) and `UNRESOLVED` (`"unresolved"`) disposition constants. [1]
- `TestRun` validates a `{test, result}` entry with `result` constrained to `"passed"` or `"failed"` and `__test__ = False`. [2]
- `TestNotRun` validates a `{test, reason}` entry with `__test__ = False` for named tests that could not be executed. [3]
- `ConsolidationEvidence` validates non-empty `testsRun`/`testsNotRun`, true-only `noProofRecorded`, cross-list test uniqueness via `_require_distinct_tests`, and exposes `names_tests()`. [4]
