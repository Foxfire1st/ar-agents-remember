# mcp/src/agents_remember/application/review_leaf_view_memo.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

The parent process's bounded reuse of a live comparison's knowledge diff and worklist parts. It stores no composed subject answer and writes no review copy to disk.

## Code Commentary

`LeafViewKey` carries the gate key's exact candidate/contract/parent-tip/memory-HEAD/task/build identities, the comparison's base/conversion trees, and the canonical task JSON path/data identities consumed while making this request. The gate memo is imported as an existing identity owner; its implementation, key and never-keep rules are unchanged.

Actual computation reads return to `moved_inputs`: both task lookups must agree with request inputs, repeated inconsistent reads remain conflicting, and every observed outside-tree dependency must still have its consumed bytes. An A-to-B-to-A edit therefore refuses the raced view through the existing currentness owner instead of storing or returning B under A.

`remembered` serves only the same key while its recorded reads still match, within four LRU entries and 900 seconds. `remember` rejects changed/conflicting inputs; the caller additionally requires readable knowledge, complete worklist and successful Git reads. A recovered aggregate failure remains unkeepable. Every live request still captures both worktrees. Recorded comparisons bypass this memo. R42 owns heavy first-computation process isolation and the original concurrent-click proof; this module supplies no concurrency acceptance.

## Evidence

No Domain Documentation entries are configured in this memory line's system/sources.md. These are repository source/test claims; approved task requirements and bound verification receipts live in the task reports.


- The key binds exact tree/input identities and canonical task reads. [1]
- Actual reads are checked against task inputs and their current bytes. [2]
- Reuse is bounded and requires unchanged recorded dependencies. [3]
- Conflicting or moved reads never enter the parent memo. [4]
