# mcp/tests/test_tool_answer_table_install.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The runtime-install final row and its operation-produced cases (MIK-R112 F11): the row governs an answer the real operation produced, not a written-down example.

## Code Commentary

`_produced_install_compact` runs the real install as a disposable dry run from the packaged tree with the watcher stop mocked at the lifecycle boundary, in an ok and a failed variant; the failed variant finds a store of a removed part and a gate log in its root, which is what makes it the largest answer the operation gives. The class requires the final bounds to live in the production lookup with the install bound at six hundred, the row fields to match the production projection, and the interim ownership of the earlier leaves to be unchanged. Both stored cases must equal what the operation produces and fit the row bound; the projection must forward no undeclared field and no message longer than two hundred and one characters. The overflow case raises the largest case over the row bound but under the exception ceiling and requires the unchanged guard to overflow it and to write one log line marked as a guard cut.

## Invariants And Boundaries

The stored case is compared with a produced answer, so a change in the operation's shape fails here rather than passing silently. The answer no longer reads a user settings file, so these cases need no environment precondition. The row bound overflows through the existing guard and not a second one.

## Evidence

### Repo-Internal References

- The row's bound and fields come from the production lookup and projection, and both stored cases are operation-produced. [1]

- An over-bound install answer overflows through the unchanged guard and leaves one guard-cut log line. [2]
