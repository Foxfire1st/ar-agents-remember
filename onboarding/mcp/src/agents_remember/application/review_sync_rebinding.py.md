# mcp/src/agents_remember/application/review_sync_rebinding.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Measure the complete post-sync code and memory candidates against one retained tree comparison. Missing inputs are states after a completed sync, never transaction gates.

## Code Commentary

### Logic

Recording requires a successful carrying sync and an exact comparison selected by `select_review_comparison`. Code capture uses the existing future-code owner. `_resolved_memory` captures the complete candidate through an isolated index copy and checks that memory HEAD did not move; the real index is never staged.

Each channel retains reviewed/resolved trees and its match. Unavailable memory is unmeasured, never agreement. `rebinding_names_the_generation` accepts only a tree-bound record equal to the retained comparison. Historical v1 dataset rebinding proves no exact memory-tree coverage.

### Invariants And Boundaries

Failed capture invents no identity; a moved pair remains moved and needs renewed comparison coverage. No non-carrying result records a resolution. Read-back separates absence, unreadability and historical limits. This measurement changes no landing authority or earlier review.

### Todos

None recorded.

### Logic

**What counts as a completed sync is three checked facts, not an inference from payload keys.**
`resolved_pair_completed` (`:196-220`) requires the operation to be `worktree_sync`, `ok` to be true, and
the state to be one of the three in `_CARRYING_SYNC_STATES` (`:155-161`) — `synced`,
`sync-pass-completed-memory-skipped`, `sync-pass-completed-source-moved-again`. `already-current` is
deliberately **not** a carrying state: that result reports that the recorded pair and the participating
work branches already contained the official line, so nothing was carried and there is no resolved pair to
measure a review against. The success conjunct is carried even though every producer of those three states
returns zero today, because a carrying state beside `ok: false` is a result this tool must not measure.

**Every state that carried nothing is described by its own entry.** `_CARRIED_NOTHING` (`:167-193`) is a
table rather than a ladder, one row per state, each pairing a block state with the store fact it observed:
`would-sync` → `preview`, `already-current` → `no-movement`, `sync-resolution-required` → `not-resolved`,
`sync-cancelled` → `cancelled`, `memory-sync-choice-required` → `choice-required`. A state outside the
table answers `not-measured` naming the state it was actually given. This is the shape that replaced a
single false sentence ("this result is not a completed sync"), which was false for several of these.

### Invariants And Boundaries

- **No refusal reaches the sync.** `rebinding_result_block` (`:316-373`) catches the unmeasurable-capture
  control-flow exception and the storage/os/runtime/value errors, and writes a state onto the payload in
  each case. Nothing in this module can block the Git transaction it describes.
- **One file per (leaf, generation), not per sync.** A later sync over the same generation replaces that
  answer instead of accumulating a second one beside it, because the question is "does the review still
  describe what the leaf holds".
- **Boundary: paths are recorded as produced.** `task_root` and `contract_path` travel as the contract
  gave them, so a relocated coordination root leaves a record whose paths no longer resolve where they
  did; the identities remain readable.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstrings and functions and in the cases that
drive the real tool. The three details a reader should carry: **the record's verdict is derived from one
rule shared with its own validator**; **a sync that cannot be measured is still returned unchanged**, with
the reason on the payload; and **the record is checked against the store before it is read as a
measurement of a generation**, because a forged record is internally consistent.


- The module docstring states what it measures — the exact post-sync code and memory candidates against one retained tree comparison — and that a missing comparison, capture or evidence is a result state rather than an admission gate, with historical v1 records readable but proving no memory-tree coverage. [1]


- The module's surface: the two result dataclasses, the per-generation reader and the result block, with the record types imported from the knowledge model module. [2]

- The one durable file-name prefix, one file per leaf and judged generation. [3]

- **The one action that produces a comparison current with the resolved pair, stated once.** [4]

- **The three states in which the transaction carried the official line, and why `already-current` is not one.** [5]
- **The five states that carried nothing, each with the store fact it observed.** [6]
- **The three checked facts, including the success conjunct carried for a producer that does not exist yet.** [7]

- The resolved source side as a state, with the named reason it could not be measured. [8]


- One published rebinding: the durable artifact, the record, and the read-back that proves it. [9]


- The read-back's four states — recorded, legacy-limit for a v1 record that proves no memory-tree coverage, not-recorded naming the location, and unreadable with the reason — with covers_resolved_pair() as the predicate a consumer branches on. [10]


- The one durable destination a generation's rebinding is published to. [11]


- **Measuring one finished sync and publishing it, and the two cases that publish nothing at all.** [12]


- **The never-raising entry point the sync tool calls, and the states it writes instead of raising.** [13]


- Reading one generation back: recorded, legacy-limit for a v1 record that keeps its identities but proves no reviewed memory tree, not-recorded naming the location, and unreadable with the reason. [14]


- **The check against the store that a forged-but-consistent record cannot pass.** [15]


- **The carried-nothing vocabulary, one entry per observed state.** [18]


- **The generation vocabulary in this block's own words, with the selection owner's answer carried beside it.** [19]


- The shipped capture owner's refusal converted into a state rather than an exception. [21]

- **The one verdict rule the writer and the record's validator share.** [24]

- The sealed record itself: the reviewed pair, the resolved pair, both channel matches and the state. [25]

- The generation store's own order and the manifest this module reads and never rewrites. [26]

- Select the retained tree comparison, not a canonical dataset generation. [27]

- The durable-evidence pair every rebinding is published and read back through. [29]

- **The shipped capture owner whose add-all tree is the resolved source side.** [30]


- The publication route whose declared location the resolved knowledge side is read at. [31]

- **The production call site: the sync tool's result, after its Git work and contract write.** [32]


- **The reopen owner's fifth channel, which makes the per-generation reader a production consumer.** [33]


- **The live read that renders the measurement, and the movement that outranks a carried identity.** [34]


- Exact/memory-only movements are measured without relabeling; parked work is captured without staging. [35]


- Unavailable memory and historical v1 records claim no pair coverage. [36]


- Live movement names its exact memory input and refuses contradictory fields. [37]


### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads a task root, the leaf's own worktree and
a publication location that all lie inside the contract's own repository boundary; the relocation boundary
that follows from a recorded absolute path is stated above.

No meaningful cross-repo references found.
