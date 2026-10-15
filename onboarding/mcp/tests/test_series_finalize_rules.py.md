# mcp/tests/test_series_finalize_rules.py

## Governing Overview

[tests overview](overview.md)

## Purpose

What finalizing a master decides again, reads, and refuses by name. Finalization completes a master's document and its sprint row; it decides once more that no abandoned row has landed, it reports an unreadable sibling as a fact only when that sibling's canonical identity is established, it refuses an unbound title with a named unresolved identity and the canonical-folder repair, it does not finalize a task whose own document cannot be read, and it refuses a master that several sprints command with the edit that works on each of them.

## Code Commentary

`_finalize` and `_blocked` drive the finalize route and read its refusal. The cases cover an abandoned row that landed and one that did not, an unreadable enclosure of an abandoned row, another unreadable member reported by file, a seat row found by its file, a missing member, canonical identity for an unreadable member, a readable admitted title member, a missing admitted canonical member, duplicate and foreign typed refs, an unreadable own document, and several commanding sprints. In the unreadable-sibling case, setup writes the target master inProgress so native finalization must actually complete it. The dry run compares the complete world snapshot without changes; the real call asserts Completed master with nonnull completedAt and the unchanged empty master decisions. Its sprint row completes while sprint decisions remain empty and sprint completedAt stays absent; the sibling's broken file remains unchanged. These asserted producer effects are not inferred from status setup or a seeded DOM view.

`_leaf_rows` gives its derived leaf a scratch memory-worktree path and ledger path, so the external-memory
contract passes structural admission before the abandoned/landed status is judged. These cells do not alter the
finalizer's contradiction rule or create live open-work directories.



## Completion Record Boundary

The unreadable-sibling happy path distinguishes completing the master itself from updating its sprint row: only the master receives completedAt, neither document receives an appended decision, and the dry run writes nothing.


- Finalization assertion setup forces real master completion; dry-run preserves complete world, real call requires completedAt and unchanged master/sprint decisions with absent sprint completedAt. [5]


A readable ordinary no-master document still cannot authorize completion: after restoring its bytes, the source case requires `task-document-resolution-blocked` and byte equality. The genuinely absent ordinary-document case requires the same refusal in both dry and real calls, names the contract-bound document/master-row requirement and leaves the path absent. These are distinct negative controls from the admitted master-completion case above.

## Evidence


- Finalization refuses an abandoned row that landed and names the row, for masters of either nature. [1]
- Canonical unreadable sibling is reported by file while native master finalization timestamps only the completed master and preserves master/sprint decisions; dry run preserves the world. Unbound title/missing member refusals remain separate. [2]


- An unreadable proven canonical sibling is reported as a fact without changing its membership, row, node or bytes; an unbound title is a named unresolved identity. [3]

- The finalization control supplies the external-memory leaf cells before testing retained landing truth. [4]

- Restoring readability is not authority for a no-master completion, and dry/real absent-document finalization preserves absence. [6]
