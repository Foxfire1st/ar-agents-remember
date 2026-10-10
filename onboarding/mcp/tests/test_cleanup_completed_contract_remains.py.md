# mcp/tests/test_cleanup_completed_contract_remains.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

A terminal completed contract with remains is finished by the repeated cleanup.

## Code Commentary

MIK-R82 rule 5 as amended: an earlier build wrote `cleanup: completed` and left the folder and branches, or a cleanup stopped midway. The repeated cleanup removes what remains and names it. The citation-cache guard does not refuse such a leaf for a missing state; an active state of another lifecycle for the same contract still refuses.

## Evidence

- Completed-contract-with-remains finish and cache-guard cases are pinned. [1]
