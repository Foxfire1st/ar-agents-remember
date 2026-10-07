# mcp/tests/test_knowledge_worklist_leaf.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of a leaf's worklist from its contract: pairing the memory base by trailer, following a sync,
persistence beside the contract, the surfaces that show the worklist, the writer's carrying of moved
anchors, the converted-base cache, and the read-ahead of changed blobs. The fixture (`Leaf`) is a real code
repository and a real converted memory repository on `main`, with a task root that holds the leaf's task
document and its series contract in the leaf's enclosure.

## Code Commentary

- **Pairing and persistence.** A leaf pairs its memory base by the `Code-Commit` trailer, follows its sync,
  and persists the worklist beside its contract. A base that no memory commit pairs with gives an
  `incomplete` worklist naming the pairing.
- **Scope and conversion.** The task document's maintenance scope classifies every entry. An unconverted
  base is compared as its conversion. Converted bases are cached by memory commit, conversion version and
  code commit; the second run reads the cache.
- **Writer.** The writer carries moved blobs and the rows that cover them, never edits another owner's row
  or a closed history file, and a proof authored through the writer raises its invariant when its test
  changes.
- **Surfaces.** The tool returns the latest worklist and the checklist shows it. The memory-quality run
  recomputes, persists and names its own failure, and the controller path persists the worklist and
  renders it in the checklist.
- **Sync.** A completed sync recomputes through the bound port; the recompute never raises and a failure
  never fails a completed sync; the continue replay of a completed sync recomputes as well.
- **Read-ahead.** `test_warming_reads_the_changed_blobs_in_one_batch_and_never_fails_the_run` opens
  `CodeTrees` on two commits that change two files. `warm` with those two paths and one path that is in
  neither tree makes exactly one call of the batched blob reader, whose arguments include the base and
  candidate blobs of the changed code file and the candidate blob of the other file. Reading those blobs
  afterwards makes no further call. `warm` on trees the store does not hold returns without raising, and
  the read of such a tree raises `CodeReadError`.

## Evidence

- The module docstring: the fixture's repositories and task root. [17]
- Pairing by trailer, following a sync and persisting beside the contract. [18]
- A base without a paired memory commit is incomplete. [19]
- An unconverted base is compared as its conversion. [20]
- Converted bases are cached. [21]
- The recompute never raises. [22]
- One batch for the changed blobs, answers from the cache, and no failure from the read-ahead. [23]
- The read-ahead under test. [24]
