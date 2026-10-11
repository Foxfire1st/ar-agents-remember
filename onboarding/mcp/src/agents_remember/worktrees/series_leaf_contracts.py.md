# mcp/src/agents_remember/worktrees/series_leaf_contracts.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Resolves the non-abandoned atomic leaf population and checks its exact enclosure set.

## Code Commentary

`atomic_leaf_documents` returns non-abandoned leaf references and abandoned numbers. It skips abandoned rows before requiring a file, document or unique number. Non-abandoned rows require unique numbers and distinct exact owned documents. A colliding number belongs to its non-abandoned row and is removed from the abandoned set. A master without rows refuses; an all-abandoned master has no required leaf documents.

`exact_atomic_leaf_contracts(require_all=True)` requires one exact enclosure for each non-abandoned leaf at a final landing. Checkpoint, recorded landing and owner resolution pass `require_all=False`: rows with no enclosure published nothing and are omitted, but foreign, duplicate and unreadable present enclosures still refuse. It still inspects present enclosures: one recording completed integration for an abandoned number refuses. An unlanded abandoned enclosure is outside the landing chain.

Membership/enclosure checks use named `CloseoutQueueError` refusals. Canonical leaf-document failures retain `TaskDocumentRefError`, its status, and the added master, row, document and repair action.

## Evidence

- Only non-abandoned rows require exact owned documents; colliding numbers belong to those rows. [5]

- The exact enclosure population preserves the abandoned-but-landed refusal. [6]

- Static controls cover absent/unlanded abandoned enclosures and an empty file cell while preserving the master. [7]
