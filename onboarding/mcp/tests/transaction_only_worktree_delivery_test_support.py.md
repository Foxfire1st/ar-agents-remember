# mcp/tests/transaction_only_worktree_delivery_test_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The fixtures, hooks, seam racers and attribution assertions of the transaction-only delivery cases (CCR-R12), shared by the race and publication module and the memory-cache module.

## Code Commentary

The module builds temp Git fixtures bound to MCP authority without a profile, adds only the canonical enclosure binding to leave review evidence absent, and patches the historical acceptance entry points so an accidental call fails loudly. It installs real failing and real recording passing pre-commit hooks in both repositories, and `_closeout_through_failing_then_passing_hooks` requires the landing to refuse on the first and land on the second. The racers move a branch with a foreign commit at one named seam (`before-tip-check` or `after-commit-written`), or switch, detach or move a checkout at a named moment of the closeout. `_code_and_memory_state` collects every fact a refused publication must give back, and `_memory_preparations` collects the history file and the ignore rule. `_assert_landed_subject` requires a landed one-line message's subject to carry the pass fact, and `_assert_memory_attribution` requires exactly one code-commit trailer read back out of the committed object with no cached ledger beside it. `_ClosedCacheLeaf`, `_seed_converted_memory_layout` and `_seed_leaf_trace_row` build the cache and converted-memory fixtures.

## Invariants And Boundaries

The attribution is bound by the hash, not recorded beside it: the trailer is read from the committed object by both documented git readers. A refusal must give back refs, index and files, so a case can assert an unchanged world rather than an unchanged message. Hooks are real executables, not patched functions.

## Evidence

### Repo-Internal References

- Real failing and passing hooks are installed in both repositories, and a landing refuses on the first and lands on the second. [1]

- A refused publication gives back refs, index and files, and the memory attribution is read from the committed object. [2]

- Branch races are applied at named seams of the shared publication, and checkout disturbances at named moments. [3]
