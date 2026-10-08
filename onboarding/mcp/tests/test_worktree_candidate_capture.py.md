# mcp/tests/test_worktree_candidate_capture.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Exact source-tree and index-isolation evidence for the one shared copied-index capture owner, on code and external memory sides.

## Code Commentary

The previous full capture is retained only as the test reference. The state matrix covers clean/edited/added/deleted/staged/ignored and trust flags with explicit derived exclusions; separate checks pin subdirectory flag clearing, same-second same-size rewrites, trusted unchanged files, object retention and unusable-copy recovery. Changed conversion rules over an untouched stat-matching file follow what the real index stages rather than unconditional reconversion equality. Real index bytes/time/flags/locks and working files are preserved. Test results do not grant closeout or semantic acceptance.

The same-size, same-second Git rewrite scenario imports the single `rewrite_in_the_second_of_the_index_write` owner from [knowledge_index_test_support.py](knowledge_index_test_support.py.md). Its real clock alignment is the scenario's subject; the 120-second alignment guard does not assert scheduler speed. The original captured-tree/currentness assertions remain at this file's test owner.

## Evidence

No Domain Documentation entries are configured in this memory line's system/sources.md. These are repository source/test claims; approved task requirements and bound verification receipts live in the task reports.


- The state matrix compares exact trees and original-index state. [1]
- Same-size same-second rewrite changes the captured tree. [2]
- Changed conversion rule alone follows actual indexed staging. [3]
- Unusable copied-index capture recovers through the original full owner. [4]

- The shared owner establishes a same-size rewrite in the index-write second. [5]
