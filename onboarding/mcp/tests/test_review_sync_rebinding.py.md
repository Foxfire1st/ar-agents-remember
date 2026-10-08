# mcp/tests/test_review_sync_rebinding.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Managed-sync evidence compares both actual candidate trees with one retained tree comparison.

## Code Commentary

### Logic

Cases measure an exact pair as current, then a memory-only edit as moved while code still matches. Durable read-back must name the reviewed comparison and actual memory capture. [10]

Staged/unstaged edits are captured with both real Git indexes unchanged. States carrying no completed sync or unavailable captures never claim pair coverage. [11] [15]

Historical v1 receipts remain readable but prove no memory-tree coverage. The v2 model rejects changed source/digest/identity fields and retired generation keys. [18] [34]

### Invariants And Boundaries

- Currency requires both exact trees to match.
- Movement evidence is not successor publication or acceptance.

## Evidence

### Repo-Internal References


- Exact pair and memory-only movement. [10]


- Candidate capture preserves real indexes. [11]


- Absent measurements claim no coverage. [15]


- Historical v1 cannot prove tree pair coverage. [18]


- Current exact-pair recorder. [20]


- Actual no-measurement reason. [29]


- Recorder binds complete tree comparison. [30]


- Memory is captured or reported unavailable. [31]


- Complete v2 source binding validator. [34]


- Statement names trees, not a canonical dataset carrier. [35]


### Cross-Repo References

No cross-repository contract is established by this file.
