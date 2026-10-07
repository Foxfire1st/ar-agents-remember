# mcp/src/agents_remember/application/review_leaf_view_memo.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

The bounded memo of the reviewer's leaf-wide view in the process that serves the reviewer. It keeps the
two computed parts of a live comparison, the knowledge diff and the worklist view, under a key of exact
identities and together with every row the computation recorded outside the trees. It keeps no composed
answer, writes nothing to disk, and is empty after a restart.

## Code Commentary

### The key

`leaf_view_key(contract, trees)` returns a `LeafViewKey`, or `None` for a recorded comparison, a contract
without a memory worktree, an unreadable parent memory tip or leaf `HEAD`, or an input that cannot be
identified. Without a key nothing is looked up and nothing is kept.

The key holds:

- the gate memo's key for the same candidate (`gate_memo.memo_key`): the candidate code and memory trees,
  the contract's path and the SHA-256 of its bytes, the parent line's memory tip, the leaf's memory
  `HEAD`, the SHA-256 of the leaf's task document, and the build stamp;
- the comparison's code base tree, memory base tree, and the tree the before side is read as;
- `task_reads`: the byte rows that the strict task lookup recorded while the gate key was built, limited
  to JSON files directly in the task folder (`_task_reads`).

The strict lookup records the leaf's own document and — when it established a claimant — no sibling it
merely ruled out; a lookup that found no claimant records every opened document and the exact direct JSON
listing, so those files are inputs of the key. When a claimant is established, a write to another leaf's
document, a new sibling document or an edit of the master's `task.json` changes neither the key nor any
recorded row; when no claimant exists, the same write moves the recorded rows and the view is recomputed.
A sibling that starts to claim the leaf makes the lookup ambiguous: there is then no key, and the view is
computed and not kept. A caller that never performs the lookup records none of these rows.

### Serving a kept view

`remembered(key)` returns the kept parts only when the entry is at most `MAX_AGE_SECONDS` old and
`changed_observations` reports no change of its recorded rows. The check repeats every recorded path
resolution and existence probe first and reads files only when all of them still give the recorded
answer. On a hit the kept rows are replayed into the caller's recording block.

### Judging a computation

`moved_inputs(key, reads)` returns the sorted paths of inputs that moved:

- a task document the computation read whose bytes differ from the key's `task_reads`;
- a task document the computation read that the key does not name;
- every recorded row whose recheck gives another identity than the recorded one (`changed_observations`).

A task document that the key names and the computation never opened is not reported: it was not read,
which is not a change. With `key=None` only the file-system check runs.

`remember(key, parts, reads)` keeps the parts unless the rows hold a failed observation (a conflict or an
unreadable row), a task document was recorded as absent, or `moved_inputs` reports anything. The caller
decides beforehand whether the parts are settled.

### Bounds

`LEAF_VIEW_MEMO` is a `BoundedMemo` of `CAPACITY` 4 entries, least recently used first out.
`MAX_AGE_SECONDS` is the gate memo's value, 900 seconds. A live request captures both worktrees before it
gets here, so an edit of a worktree is a new tree and a new key.

## Evidence

- The two bounds. [5]
- The key's fields. [6]
- The key is built with the task lookup's reads recorded; several conditions give no key. [7]
- A kept view is served only when young enough and unchanged, and its rows are replayed. [8]
- A read with other bytes or an unnamed read is a move; a named document that was not read is not. [9]
- Task reads are the JSON files directly in the task folder. [10]
- Failed, absent or moved inputs keep the parts out of the memo. [11]
- The recheck repeats selections before it reads bytes. [12]
- Another leaf's document appearing, changing or vanishing, and a newline in task.json, leave the kept view in place; the leaf's own document recomputes. [13]
- A second document that claims the leaf is computed again and answers incomplete. [14]
- Not read, same bytes, other bytes, a conflict and an unnamed document, each judged. [15]
- Count and age bounds, and no answer for another key. [16]
- A view behind which a read failed is not kept. [17]
