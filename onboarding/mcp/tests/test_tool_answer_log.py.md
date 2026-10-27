# mcp/tests/test_tool_answer_log.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Guards daily tool-log records, redaction, retention, enclosure placement and failure isolation.

## Code Commentary

The log tests require whole-result detail beside status answers, bounded/redacted arguments and no credential values, while ordinary environment values and nonsecret paths remain attributable. Raised/refused calls are logged through production entry. Terminating operations use root custody; ordinary live-leaf calls use enclosure logs. Hermetic enclosure cases check both worktrees stay clean, changed-path capture excludes logs, and cleanup removes enclosure logs. No real developer settings or ambient enclosure should be used as a fixture.

The path witnesses distinguish domains: ordinary nonsecret paths within 200 characters stay whole; a path beyond that threshold becomes its exact length and SHA-256 digest. Both a real temporary-root path and an explicitly over-long path are checked, independently of credential-value redaction. The enclosure-removal fixture also carries its task root so canonical report collection remains in the disposable task.

## Concurrent detail budget

A coordinated two-thread test gives both writers the same nearly exhausted folder budget. Both writers complete, but the shared process lock admits only the affordable detail, preventing concurrent overspend. This supplements the existing whole-record cross-process and redaction tests.


- Two detail writers cannot both spend one remaining budget. [5]



## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.






















- Log fields, redaction and write-failure behavior are checked.  Anchor: `ToolAnswerLogTests` [1]




- Raised and refused calls keep real entry logging.  Anchor: `ToolRaisedCallLoggingTests` [2]




- Hermetic enclosure log placement and cleanup are asserted.  Anchor: `ToolAnswerEnclosureTests` [3]




- Real temporary-root paths obey the exact preservation or length-and-digest rule.  Anchor: `ToolAnswerLogTests.test_home_folder_path_follows_the_length_rule` [4]
