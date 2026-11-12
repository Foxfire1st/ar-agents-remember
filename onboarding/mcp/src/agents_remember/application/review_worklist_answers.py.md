# mcp/src/agents_remember/application/review_worklist_answers.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Bind worklist display and optional unexplained-open counts to the existing comparison, and delegate satisfaction entirely to the gate.

## Code Commentary

`worklist_bound` compares code B/C trees, memory-base commit and tree, and K_C tree. `worklist_answers` returns no states for another comparison; incomplete bound work becomes undecided, while complete work calls public item_verdicts for the recorded leaf. An exact held classifier/candidate may be reused only when its pairing matches; otherwise the gate reads its own candidates. `stored_unexplained_open` reads a complete matching stored worklist and counts only open unexplained hunk/file verdicts; absent, unreadable, unbound or undecided means no count. Attribution counts are separate, and no displayed state satisfies or waives an item.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- A worklist must match all comparison tree operands and memory-base commit. [1]
- The reviewer delegates item judgments to the public gate API over exact after trees. [2]
- Auxiliary open counts are omitted rather than guessed for absent or undecidable stored work. 

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_worklist_answers.py::stored_unexplained_open - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
