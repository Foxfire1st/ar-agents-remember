# mcp/tests/test_knowledge_index_surfaces.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Checks converted knowledge reads, bounded file diffs, index integrity and explicit legacy-format refusals.

## Code Commentary

Current cases read a converted tree through its index; compare knowledge files and adjacent cards; name unknown paths, unheld records, directories and unknown revisions; and report omitted items within the read threshold. Separate cases compare an omitted after revision with the working tree and refuse an unconverted working tree. Retired records are not live selections, partial indexes stay incomplete, and unbuildable indexes return a refusal. The removed combined database-unchanged case is not current coverage; no test execution is asserted here.

## Evidence

### Repo-Internal References

- `test_knowledge_diff_serves_the_git_diff_of_the_knowledge_files` owns the current boundary described above. [8]
- `test_knowledge_diff_with_no_after_revision_compares_with_the_working_tree` owns the current boundary described above. [9]
- `test_knowledge_diff_answers_within_the_read_threshold_and_names_what_it_leaves_out` owns the current boundary described above. [10]
- `test_every_knowledge_tool_refuses_legacy_memory_and_opens_no_database` owns the current boundary described above. [11]
