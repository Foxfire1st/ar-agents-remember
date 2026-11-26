# mcp/tests/test_githooks_l29_repairs.py

## Governing Overview

[MCP tests](overview.md)

## Purpose

Behavioral protection for the repository hook's own performance repairs: one bounded xargs batch, one scope-batch invocation, concurrent Python and dashboard rails, content-addressed ESLint and incremental TypeScript caches, and a quieter Pyright wrapper. Each case asserts that the repair changes cost, not the tier's verdict.

## Code Commentary

The R1 cases run a real script through the hook's tracked-Python population and check ordered output, spawn reduction, splitting above 256 KiB and late-failure propagation. The R2 cases compare the one-invocation scope batch byte for byte with separate spawns, check the lazy on-disk count walk, and prove the hook invokes the batch once and removes its temporary directory. The R3 cases prove the two rails overlap but replay Python first, and that a failure in either rail fails the tier with its own message and order preserved. The R4 and R5 cases introduce a real lint or type error behind the caches and require the tier to fail; they also prove the cache files are gitignored and do not trip the landing check. The R6 case proves the Pyright wrapper notice is silenced while a real type error still fails.

## Relationships

The cases exercise `.githooks/_gate.sh`, `scope_reporting.py` and `hook_scope_batch.py` against small controlled trees and real Node tools where the case names them. They supplement the existing hook and landing-check suites; catalog membership selects them, and this card claims no execution.

## Evidence

- One 256 KiB xargs batch preserves file order and reduces spawns. [1]
- The one-invocation scope batch matches separate spawns byte for byte. [2]
- The two rails overlap while their output keeps Python-then-dashboard order. [3]
- The ESLint and tsc caches stay gitignored and do not trip the landing check. [4]
- Pyright wrapper notices are silenced and a real type error still fails. [5]
