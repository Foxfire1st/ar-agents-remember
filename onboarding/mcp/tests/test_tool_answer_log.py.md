# mcp/tests/test_tool_answer_log.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Guards daily tool-log records, redaction, retention, enclosure placement and failure isolation.

## Code Commentary

The log tests require whole-result detail beside status answers, bounded/redacted arguments and no credential values, while ordinary environment values and nonsecret paths remain attributable. Raised/refused calls are logged through production entry. Terminating operations use root custody; ordinary live-leaf calls use enclosure logs. Hermetic enclosure cases check both worktrees stay clean, changed-path capture excludes logs, and cleanup removes enclosure logs. No real developer settings or ambient enclosure should be used as a fixture.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.

- Log fields, redaction and write-failure behavior are checked. [1]
- Raised and refused calls keep real entry logging. [2]
- Hermetic enclosure log placement and cleanup are asserted. [3]
