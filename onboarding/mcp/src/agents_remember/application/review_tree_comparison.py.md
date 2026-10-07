# mcp/src/agents_remember/application/review_tree_comparison.py

## Governing Overview

[application route overview](overview.md)

## Purpose

A review comparison as four Git trees: the code base B, the code candidate C, the memory base K_B and the
memory candidate K_C. The module captures a live leaf's comparison, pins its uncommitted candidates with
Git refs, records it under the task's reports, opens each memory side through the derived index of its
tree, and reopens a recorded comparison from its tree IDs. It copies no tree and no database.

## Code Commentary

### The four sides of a live comparison

- `memory_converted(contract)` decides whether a leaf gets a tree comparison: its memory worktree, or the
  tip of its official memory line, holds the layout marker. Otherwise `live_review_trees` returns `None`.
- `_live_draft` resolves B from the contract's code base commit, pairs K_B with `paired_memory_commit`
  (the worklist's own pairing), and captures K_C through a private index (`_capture`). C is the tree the
  caller captured. A side that cannot be resolved raises `TreeSideUnreadable` and becomes a
  `candidate_unresolved` refusal naming the side.
- `_candidate_side` marks a candidate as committed when the tip of the durable source line holds exactly
  its tree; a committed side records the commit and needs no ref.
- When K_B lacks the layout marker and K_C has it, K_B is compared as its conversion (`_conversion`,
  `_converted_base`). The conversion's inputs are the memory commit, the pinned conversion version and
  the code commit it is anchored at. `_held_tree` uses the tree that the leaf's latest record names when
  that record was made from exactly these inputs and Git still holds the tree; otherwise
  `write_files_tree` writes the converted files as blobs and trees into the memory repository's object
  store, touching no ref, index or working tree.

### Recording and pinning

- `review_ref(task_id, leaf_id, n)` is `refs/ar/review/<task directory name>/<leaf>/<n>`. A segment that
  is empty, `.`, `..` or contains a slash or backslash raises `ValueError`. `review_task_id` is the task
  folder's name and reads nothing from the folder.
- `_record` serializes recording inside one process with the lock `_RECORDING` and calls `_recorded`.
  Readers of one dashboard that open the same new comparison at the same moment therefore take turns.
- `_recorded` reuses the latest record when it has the same four trees (`same_trees`), creating a pin
  again when it has gone. Otherwise the new number is one more than the highest recorded number and the
  highest existing ref number, the candidates are pinned, and only then is
  `notes/reports/review-comparisons/<leaf>/<n>.json` written atomically. If a record file with that
  number exists after pinning and it is the latest record with the same trees, that record is returned
  and nothing is written.
- `_pin` pins each candidate that has a ref. `_create_pin` makes one pin with
  `update-ref <ref> <tree> <zero>`, which only creates:
  - a ref that already names this tree is success, and it is not counted as created by this call;
  - a ref that names anything else is a refusal and is never moved;
  - when Git answers "cannot lock ref" or "already exists", the ref is read again and the creation is
    tried again, up to `_PIN_ATTEMPTS` (5) times with a pause of `_PIN_RETRY_SECONDS` (0.02 s) times the
    attempt number; any other Git failure ends the attempts at once.
- When a pin is refused, `_pin` deletes the pins this call created, and only those, and returns a
  `candidate_unresolved` refusal that names the repository and the ref (`_pin_refusal`).

### Opening and reopening

- `_open_side` opens a memory tree through `KnowledgeIndexCache.for_git_tree`. An index failure makes the
  side `unavailable-history` with the reason; an available side carries the index state and its problems.
  The before side is the converted base tree when the record has one.
- `reopen_review_trees` picks the named or the latest record; a number the leaf did not record is refused.
  `reopened_trees` marks each memory tree that Git cannot produce as `unavailable-history`, derives
  a missing converted base again and compares its ID (`_before_state`), and reports both code trees as
  `available` or `unavailable-history` (`_code_sides`). No current tree is read in place of a lost one.
- `recheck_memory_candidate` captures a live memory worktree again and refuses when its tree differs from
  the recorded one.
- `tree_resolution` builds the review's resolution over the two index files and the two code trees. An
  unavailable side names a path under `.review-knowledge-unavailable/` that is never created.
  `tree_sides_refusal` and `tree_limitations` give the refusal and the declared facts of a comparison.

## Evidence

- The comparison, each memory side's index, the live flag and the code sides. [22]
- A tree comparison applies when the worktree or the official line holds the layout marker. [23]
- The task segment of a review ref is the task directory's name. [24]
- The ref name and the refused segments. [25]
- Capture, pin, record and open a live leaf's comparison. [26]
- The four sides of a live draft, K_B through the worklist's pairing. [27]
- A moved memory candidate is refused before publication. [28]
- Committed only when the durable line's tip holds exactly this tree. [29]
- The held converted tree is used only for the same inputs and while Git holds it. [30]
- Converted files are written as objects only. [31]
- The recording lock and the pin retry constants. [32]
- Recording takes turns inside one process. [33]
- Reuse on the same trees, else number, pin, write; a record another reader wrote first is returned. [34]
- Each candidate with a ref is pinned; a refusal removes only the pins this call created. [35]
- One pin: same tree is success, another tree is refused, a held lock is retried. [36]
- Each memory side is opened through its tree's index. [37]
- Reopening marks every tree Git cannot produce. [38]
- A missing converted base is derived again and its ID compared. [39]
- A pin another reader made is kept and not rolled back; a ref naming another tree is refused; a held lock is waited out. [40]
- Four concurrent first reads of a new comparison give four equal answers. [41]
- A live review is four trees with its uncommitted candidates pinned and reused. [42]
- Committed candidates need no ref, and a failed pin refuses naming repository and ref. [43]
- A converted base tree that Git holds is not written again. [44]
