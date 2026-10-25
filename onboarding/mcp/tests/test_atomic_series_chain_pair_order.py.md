# mcp/tests/test_atomic_series_chain_pair_order.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Contract-scoped forcing tests for the atomic-series landing validator `worktrees/series_closeout.py`. The property they pin is the **ordering predicate over the landing pair**: two leaves can share one code commit and still be two distinct landings ordered by memory ancestry, duplicate pairs refuse only for two nonempty landings; empty pairs on-chain stand outside ordering, off-chain empties refuse. Every contract here runs with external memory; there is no disabled-memory path left to pin.

## Code Commentary

The fixtures build real Git state instead of fabricating commit ids. `_contract` fixes each leaf's recorded pair independently of its work branch and always sets `memory_mode="external"` with a real memory repository, so the predicate's pair logic is what every case exercises. The pair-order class now holds three cases: a shared code commit with ordered memory is a chain step, code ancestry still orders when the code position moved, and an identical pair stays unordered in both directions over both fixture memories. The removed `test_disabled_memory_keeps_the_code_only_rule` went with the removed mode (MIK-R50): with no opt-out, there is no code-only enclosure whose ordering needs pinning. Leaf-sync-position cases add empty-landings rules; three vacating shapes now name the empty leaf, not a foreign commit. a leaf-level sync position the chain's own contracts recorded is admissible, a silent one is refused.

## Evidence

- Fixture always builds an external-memory contract pair [14]
- Shared code plus ordered memory is a chain step [15]
- Code ancestry still orders when the code position moved [16]
- An identical pair stays unordered over both fixture memories [17]

- Leaf-level sync positions admitted, silent ones refused [18]
