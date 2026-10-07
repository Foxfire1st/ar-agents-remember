# mcp/src/agents_remember/application/knowledge_worklist/leaf.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

A leaf's worklist from its contract: which four trees are compared, when a worklist applies, how the
onboarding items join it, and where the latest document is persisted. The module also offers the same
computation over sides that a caller names directly.

## Code Commentary

### The four sides

- **B** is the contract's code base commit. **C** is the code worktree captured as a tree
  (`worktree_candidate_tree`), or a tree the caller names.
- **K_B** is the memory tree of the newest commit of the official memory line whose `Code-Commit` trailer
  names B or an ancestor of B (`paired_memory_commit`). **K_C** is the memory worktree read as a
  directory, or a Git tree the caller names.
- When K_B is unconverted and K_C is converted, K_B is compared as its conversion
  (`_converted_base_side`, through the converted-base cache). A worklist exists only where K_B or K_C
  holds the layout marker; `_sides` returns `None` when neither does.
- The document records the pairing: repositories, base commit and tree, candidate tree, memory base
  commit and tree with `convertedBase` and the pinned conversion version, and the memory candidate's tree
  and location.

### Sides given by the caller

- `CandidateTrees(code, memory)` names C and K_C as Git trees that are already in their object stores.
  With it the worklist captures neither worktree.
- `CapturedBase(code, memory, read_tree)` names B, K_B's commit, and the tree K_B is read as. With it
  `_leaf_document` takes K_B's commit from the caller instead of pairing it, and uses the caller's B
  instead of the contract's. `_leaf_converted` then probes the layout marker in `read_tree` instead of on
  the official line's tip.
- `ExplicitSides.held_base_tree` carries `read_tree` into `_sides` and into the onboarding gate's sides.
  When K_B is unconverted, `_sides` reads the held tree with `knowledge_tree_from_git` and derives the
  route coverage from its files; no conversion runs and the converted-base cache is not consulted. When
  K_B is converted, the held tree is not used and K_B is read from its own commit.

A caller that passes neither object gets the contract's own sides, captured and paired as described above.
The reviewer's worklist child passes both; the gate passes `CandidateTrees` only.

### Entry points

- `leaf_worklist(contract, persist=True, candidate=None, base=None)` returns `None` for a contract that is
  not a leaf, a leaf without a memory worktree, and a leaf whose two memory sides are unconverted. A marker
  probe that Git cannot answer gives an `incomplete` document naming `layout marker`. The document is
  written beside the contract when `persist` is true.
- `_leaf_document` reads the leaf's declared effects and maintenance scope through the strict task lookup.
  A leaf document that cannot be established gives an `incomplete` document naming `leaf task document`; a
  pairing or Git failure names its input.
- `worklist_for_sides(sides)` runs `compute_worklist` over explicit sides and turns an unreadable side, a
  `CodeReadError` and a Git failure into an `incomplete` document.
- `worklist_over(contract, sides)` adds the onboarding gate's items (`worklist_onboarding`) and settles
  the unexplained changes of uncovered files (`_settled_unexplained`): such a change is answered by its
  file's onboarding trace, the digest and the open count are recomputed, and a row that answers such a
  trace is not listed as unnecessary.
- `recompute_leaf_worklist(contract)` computes and persists and never raises: a Git failure and any other
  exception become an `incomplete` document, and an enclosure that cannot be written returns the document
  without a path. `LeafWorklistRecompute` is the port bound into the worktree layer.
- `leaf_gate_applies(contract, candidate)` is the marker probe alone.
- `leaf_onboarding_trace_sides(contract, memory_tree=None)` gives the onboarding gate's sides from the
  contract, `None` where neither side is converted, and an `incomplete` side for anything that cannot be
  established.

### Persistence

`worklist_path` is `knowledge-worklist.json` in the leaf's enclosure directory beside its series contract.
`persist_worklist` writes it atomically as sorted, indented JSON. `read_leaf_worklist` returns the persisted
document or `None`.

## Evidence

- The module docstring: the four sides, applicability and persistence. [46]
- C and K_C given as Git trees. [47]
- B, K_B's commit and the tree K_B is read as, given by the caller. [48]
- The explicitly named sides, with the held base tree. [49]
- K_B's commit by the Code-Commit trailer. [50]
- The sides: the held tree for an unconverted K_B, the cache without one, the snapshot for a converted K_B, and the pairing. [51]
- The conversion of an unconverted K_B through the cache. [52]
- The marker probe, on the held tree when a base is given. [53]
- The entry point with its three not-applicable cases and the persistence. [54]
- Declared effects, scope and K_B's commit, from the caller's base when given. [55]
- The onboarding items and the settling of uncovered files. [56]
- The recompute entry point never raises. [57]
- The held tree gives the same document and reads as the conversion, at two sizes, with no second capture, pairing or conversion. [58]
- The reviewer passes the comparison's candidate trees and base commits. [59]
