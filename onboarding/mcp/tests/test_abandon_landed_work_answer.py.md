# mcp/tests/test_abandon_landed_work_answer.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Ancestry-based landed-work reporting before abandonment.

## Code Commentary

The positive helper case creates real unmerged code work, observes no landed fact, fast-forwards the source line and then expects the branch/line fact. A missing work branch produces no fact. A direct answer-helper case checks the landedWork shape and appended ancestry sentence.

The actual abandon_result preview case creates unlanded work and asserts refusal without landedWork or an already-on-line sentence. Positive public abandonment is not exercised by this file; its positive measurement and answer assertions call the helpers directly. These cases describe their assertions, not a new execution or installation verdict.

## Evidence

### Repo-Internal References

These tests establish the assertions below; their definitions are separate from retained execution receipts.

- The helper measures a real work branch against its source line before any removal; an unmerged branch has no fact and an ancestor has the named fact. [1]
- The helper reports no landed fact when the recorded work branch is missing. [2]
- The answer helper attaches the measured branch and line and the ancestry sentence to a successful result. [3]
- The actual public abandon preview of unlanded work refuses without landedWork or an already-on-line sentence; this is not a positive public abandonment case. [4]
