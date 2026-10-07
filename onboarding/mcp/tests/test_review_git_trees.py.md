# mcp/tests/test_review_git_trees.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of the reviewer on Git trees: the four trees of a comparison, the pins, the tree view, reopening,
an unconverted side, archival, the route, the focused cards and the file read. The module also provides
the fixture `world` that the other reviewer test modules import.

## Code Commentary

### The fixture

`world` builds a coordination root with one task and one leaf enclosure, a code repository and a converted
memory repository whose `main` is the official line, and the leaf's two linked worktrees on their work
branches. `World.edit()` changes code and knowledge in the worktrees without committing, which is the
state a live review reads. `World.contract()` writes the leaf's enclosure contract.

### The cases

- **Comparison and pins.** A live review is four trees with its uncommitted candidates pinned, and a
  repeated read reuses the record. A read writes only review refs, comparison objects and the record, and
  a repeat writes nothing. Committed candidates need no ref, and a failed pin refuses naming the
  repository and the ref. Pins are named by the task directory, and archival removes them.
- **Tree view.** The view shows the knowledge diff, the currentness of each side and the worklist. A
  partial index shows its state on the affected side. No review path opens a database other than the
  derived index.
- **Reopen and conversion.** A comparison reopens from its tree IDs and names a tree Git cannot produce.
  An unconverted before side is compared as its conversion. A comparison recorded before the conversion
  keeps its code sides only. An unconverted leaf keeps the dataset review, and a tree comparison is never
  frozen into a dataset generation.
- **Route.** The route serves the port, keeps a live leaf's computed worklist for a numbered read of its
  current comparison, passes named invariants to the port, answers 400 for a name longer than 64
  characters and for more than 500 names, and answers 503 when no port is wired.
- **Cards.** The cards read locates each entry of the named invariants on both code sides, names an
  unreadable side unavailable and a missing file absent, carries an excerpt longer than its bound as a
  marked prefix, and its placement cache remembers answers only and stays within its bound. An unchanged
  path that only a proof names opens in a tree review.
- **History rows.** `test_history_rows_are_found_by_the_row_subject_an_item_names` replaces the
  collaborator `isolated_leaf_worklist` of `review_tree_knowledge` with a function that first runs the real
  isolated computation, so the view records real reads, and then returns a prepared worklist document. It
  checks that the view shows the row whose subject an item names in `facts.row`, and that of one owner's
  rows only the row of the latest attempt file is shown.

## Evidence

- The module docstring: the fixture world. [15]
- The fixture's state and helpers. [16]
- Four trees, pinned candidates, and reuse. [17]
- A repeat read writes nothing. [18]
- The tree view on the fixture. [19]
- Reopening names a tree Git cannot produce. [20]
- The route serves the port and refuses without one. [21]
- Rows are found by the row subject an item names, through the real isolated computation. [22]
