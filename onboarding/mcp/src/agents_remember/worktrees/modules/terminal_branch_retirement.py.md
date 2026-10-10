# mcp/src/agents_remember/worktrees/modules/terminal_branch_retirement.py

## Governing Overview

[mcp/src/agents_remember/worktrees/modules/overview.md](overview.md)

## Purpose

Terminal branch retirement and its refusal guards, under one owner.

## Code Commentary

Moved whole out of `cleanup.py`: local and remote branch deletion primitives, single-branch retirement with its read-only guard phase, and the contract-derived branch authority with the repository-identity keys it is compared by. `delete_branch_if_merged_into` takes the kept-line proof, so a work branch whose tip sits on the landing line or the default line is deleted even where its master's line does not hold the tip. A refused retirement changes nothing; every check that can refuse runs before the first deletion.

## Evidence

- Branch retirement primitives with kept-line proof and read-only guards; refusals precede any deletion. [1]
