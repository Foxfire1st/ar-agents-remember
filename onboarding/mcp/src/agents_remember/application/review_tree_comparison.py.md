# mcp/src/agents_remember/application/review_tree_comparison.py

## Governing Overview

[application route overview](overview.md)

## Purpose

A review comparison as four Git trees: the code base B, the code candidate C, the memory base K_B and the
memory candidate K_C. The module captures a live leaf's comparison, pins its uncommitted candidates with
Git refs, records it under the task's reports, opens each memory side through the derived index of its
tree, and reopens a recorded comparison from its tree IDs. It copies no tree and no database.

## Code Commentary

Both sides may share the existing index-cache owner, but cache construction remains inside each side's unavailable/error policy. Already unavailable sides do not touch it; construction/read failures retain named unavailable-history results. Fresh live rechecks authenticate observed HEAD as well as files and private-index evidence.


### The four sides of a live comparison

- Live review verifies the contract's recorded memory base against the real memory worktree's HEAD. The layout check examines the worktree and the recorded base. An unestablished base is a `candidate_unresolved` refusal naming the memory base. The legacy result requires established unconverted sides.
- `_live_draft` resolves B from the contract's code base commit, uses the established K_B and captures K_C through a private index. C is the tree supplied by the caller. A side that cannot be resolved becomes a `candidate_unresolved` refusal naming that side.
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
- `_record` serializes recording inside one process with `_RECORDING` and passes its matcher to
  `_recorded`. The shared helper reuses the latest record accepted by that matcher and recreates any missing pin.
- Live review supplies `same_live_comparison`. It requires the same recorded memory-base commit as well
  as `same_trees` identity: the same task and leaf, four repository/tree pairs, and converted base.
  Delivered review reuses the oldest `same_trees` match and uses that matcher by default when it needs to
  record a new comparison.
- When reuse fails, the new number follows both the highest recorded number and the highest existing
  ref number. The helper pins the candidates and publishes
  `notes/reports/review-comparisons/<leaf>/<n>.json` through
  `review_comparison_publication.publish_comparison_record`, whose exclusive create decides the winner
  (MIK-R195 F05). The caller that loses the race returns the winner if the same matcher accepts it.
  Otherwise `publication_refusal` names the occupied number. The former
  `is_file()`-then-`atomic_write_bytes` pair could replace the bytes of a record an earlier reader had
  already answered with.
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

`ReviewTrees` and `TreeKnowledge` now live in the model owner and are imported here as the same shared payload types. `_recorded` batches durable branch-tip hints with pin listings, but `_candidate_side` resolves an absent hint directly and keeps an explicitly committed delivered endpoint authoritative. Code-tree existence already verified for one live composition is remembered only in a scoped `ContextVar`, reset in `finally`; `_open_sides` supplies measured code states for live and reopened comparisons.

## Evidence

- The comparison, each memory side's index, the live flag and the code sides. 

- An available live memory worktree is compared when its layout marker or the readable recorded memory base marks converted memory. A failure to establish that base returns the named memory-base refusal before capture. [23]

- The task segment of a review ref is the task directory's name. [24]
- The ref name and the refused segments. [25]
- Capture, pin, record and open a live leaf's comparison. 
- The four sides of a live draft, K_B through the worklist's pairing. 
- A moved memory candidate is refused before publication. 
- Committed only when the durable line's tip holds exactly this tree. [29]
- The held converted tree is used only for the same inputs and while Git holds it. [30]
- Converted files are written as objects only. [31]
- The recording lock and the pin retry constants. [32]

- Recording takes turns inside one process. [33]

- The recorder uses the caller’s matcher for latest-record reuse and for a publication-race winner. Live review also matches the recorded memory-base commit. Delivered review uses `same_trees`.
- Each candidate with a ref is pinned; a refusal removes only the pins this call created. [35]
- One pin: same tree is success, another tree is refused, a held lock is retried. [36]
- Each memory side is opened through its tree's index. [37]
- Reopening marks every tree Git cannot produce. [38]
- A missing converted base is derived again and its ID compared. [39]
- A pin another reader made is kept and not rolled back; a ref naming another tree is refused; a held lock is waited out. [40]
- Four concurrent first reads of a new comparison give four equal answers. [41]
- Committed candidates need no ref, and a failed pin refuses naming repository and ref. [43]

- A converted base tree that Git holds is not written again. [44]


## 260928-MIK-L177 The Comparison's Memory Capture Carries Its Census

`live_review_trees` hands the memory capture a `captured` observer and notes the census the capture
produced, so `recheck_memory_candidate` proves movement from that census rather than a walk. The four
tree identities, the pins and the record are unchanged; only the proof that the memory worktree did
not move while the comparison was composed became cheaper, not weaker.

- The record is published by an exclusive create, so a lost race answers the winning record or refuses by name instead of replacing bytes a reader already holds. 


- ReviewTrees and TreeKnowledge live in the shared model owner. Live capture records its exact comparison inputs, uses create-only pins, and opens unavailable tree sides with named reasons. [46]


- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/models/knowledge/review_trees.py::ReviewTrees - the bytes it recorded now occur 8 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_tree_comparison.py::live_review_trees - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_tree_comparison.py::_live_draft - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_tree_comparison.py::recheck_memory_candidate - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_tree_comparison.py::_recorded - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- A live review is four trees with its uncommitted candidates pinned and reused. [42]
