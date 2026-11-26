# mcp/tests/test_knowledge_state_conversion_verdict_ref.py

## Governing Overview

[overview](overview.md)

## Purpose

Unit-regression suite verifying that state conversion normalizes archived review verdict references in `review_fact` to durable `notes/reports/<rel>` paths without reading the filesystem, leaves invalid or non-report references unchanged, and writes durable `verdictRef` entries into `knowledge/history/converted-reviews.json`.

## Evidence

- Parametrized cases verify that absolute and relative `role-reports` and `notes/reports` paths, `./` prefixes, Windows backslashes, and surrounding whitespace normalize to `notes/reports/<rel>`. [1]
- Parametrized cases verify that empty tails, `..` path-traversal segments, non-report paths, and URLs containing `/role-reports/` remain unchanged. [2]
- End-to-end conversion test verifies `plan_state_conversion` writes normalized `notes/reports/<rel>` `verdictRef` entries into `knowledge/history/converted-reviews.json` across worktree and absolute forms. [3]
