# mcp/tests/test_tool_answer_table_enclosure.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The enclosure half of the tool-answer log's expected evidence, on a real enclosure, plus the reader-change helpers: where the log lives, and why it dirties nothing.

## Code Commentary

`ToolAnswerEnclosureTests` builds one hermetic entry-point world with a real leaf enclosure opened through the real start tool. It requires the logs directory to exist beside the worktrees after the enclosure is made, both worktrees to stay clean with a log file in that directory, the closeout changed-path source to list no log path in any tier, and the real cleanup path to offer the logs directory for removal and to remove it with the enclosure. `ToolAnswerReaderChangeTests` checks the naming helpers for a day's log file and detail directory, and that the enclosure logs directory is made in the worktree group rather than inside a code worktree.

## Invariants And Boundaries

The log lives in the enclosure beside the worktrees, never inside them, which is why both worktrees can stay clean while it is written. Cleanup removes it as part of the enclosure, and the closeout never lists it.

## Evidence

### Repo-Internal References

- The logs directory is made with the enclosure beside the worktrees and dirties neither worktree. [1]

- The closeout changed paths list no log, and cleanup removes the logs directory with the enclosure. [2]
