# mcp/tests/test_checkpoint_memory_ignore.py

## Governing Overview

[Test overview](overview.md)

## Purpose

Exercise the converted-memory ignore merge through checkpoint publication and source synchronization.

## Code Commentary

The tests distinguish conflicts in generated ignore rules from conflicts in authored text. The successful final-rule replacements use common files both with and without a terminal newline. They check the exact merge parents, the merged ignore bytes and whether Git ignores derived briefs. Conflict cases retain the unmerged stages and check authored rule bytes, including an internal newline conflict and an owner's edit after Git produces the conflict file.

## Evidence

- Both final-newline cases publish the exact merged ignore file with its two parents and effective Git ignore rules. [1]
- A true authored conflict survives in the working file and index, including when it changes an internal newline. [2]
- An owner edit to Git's conflict bytes is still present when sync reports the unresolved merge. [3]
