# mcp/src/agents_remember/mcp/tools/enclosure_adoption.py

## Governing Overview

[mcp/src/agents_remember/mcp/tools/overview.md](overview.md)

## Purpose

Explicit public migration into canonical lifecycle-enclosure addressability.

## Code Commentary

MIK-R82 rule 4: the only old-layout address migration. `worktree_enclosure_adopt` validates one exact contract and root pair and publishes its audited locator receipt. Normal readers never invoke it; adoption stays explicit, and no reader or other tool adopts an enclosure on its own. Operation records written in place are taken as they are: the dry run lists each with size and hash, and the real run's receipt marks them found in place, copying and moving nothing.

## Evidence

- One explicit adoption tool migrates pre-locator enclosures, including records written in place, with dry-run listing and receipted real runs. [1]
