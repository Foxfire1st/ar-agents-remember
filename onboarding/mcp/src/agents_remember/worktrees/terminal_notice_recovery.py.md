# mcp/src/agents_remember/worktrees/terminal_notice_recovery.py

## Governing Overview

[overview](../overview.md)

## Purpose

The one answer an interrupted terminal notice needs — published, refuted or undecided — read only from the
durable record the publishing route itself left for the exact operation the intent names.

## Code Commentary

The module answers from the publishing route's own exact native record: a final landing's integration cell, a completed direct-landing generation's operation journal, or an abandonment's successful-result receipt. Archived abandonment requires the exact archive-generation receipt. An admitted no-remains enclosure requires its explicitly typed receipt beside the retained canonical contract, bound to its exact path, lifecycle identity, terminal note and canonical final-publication hash. Lifecycle prose, authored task status and a generic completed cell are never proof.

Two of its stated rules carry the design. The integration cell is **not** evidence for the direct-landing route:
a completed cell on the same enclosure belongs to some other publication, so it may neither prove nor refute
this generation, and the journal's verdict always wins. For abandonment, the live `integration.cleanup: abandoned` cell is rollbackable and an archive precedes the guard's success. Neither a cell, a bare archive nor the no-remains admission predicate alone proves success. The intent stays undecided until the native receipt commits the exact archive-generation or admitted no-remains outcome. Missing, unreadable or mismatched positive proof does not establish success.

The bounded journal reader carries typed records and an unreadability flag for its selected journals. Root-bearing intents and legacy live-contract lookup both preserve that flag. Direct settlement stays undecided before missing-generation refutation when a selected journal is unreadable or unparseable: a readable predecessor cannot establish the absence of its unreadable current owner. The eight-journal bound stays; validated archive records replace the live flag only on the existing archive path.

`NoticeVerdict` is `published` / `refuted` / `undecided`; `NoticeSettlement.proved` gives the three-valued
answer the settle pass consumes; `MAX_DIRECT_RECORDS = 8` bounds the generation journals one answer may read. An
undecidable intent is kept for a later pass, never erased.

## Evidence boundary

Current source interpretation at the reviewed freeze; the crash matrices for the ordinary, direct, abandonment
and after-cleanup routes are pinned by `mcp/tests/test_terminal_notice_recovery.py`,
`test_terminal_notice_commit_recovery.py` and `test_terminal_notice_subject.py`. No live-page witness and no
CPU or resource measurement: evidence item 6 is unrun and carried to L36, item 7 unrun.

## Evidence


- Selected journal unreadability survives both direct lookup routes and prevents partial negative evidence from refuting the pending occurrence. [1]
