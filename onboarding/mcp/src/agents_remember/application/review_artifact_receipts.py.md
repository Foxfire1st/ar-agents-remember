# mcp/src/agents_remember/application/review_artifact_receipts.py

## Governing Overview

[application overview](overview.md)

## Purpose

Owns archive-hook receipts. The canonical latest receipt is `review-artifact-cleanup.json`; earlier receipts use their own consecutive attempt numbers.

## Code Commentary

`ReceiptLedger.open` reads prior outcomes. When deletion is planned, `begin` writes an `in-progress` receipt with intended deletions before they occur; a refused receipt write prevents deletion. `finish` records the result.

`_set_aside` preserves the canonical receipt under its own attempt number. Repeating that step after interruption reuses that path, rather than allocating another copy. `_previous_attempt` only classifies the prior outcome.

The first attempt writes an initial receipt even when it deletes nothing. A later attempt writes none only if it has no deletion, release or failure, no unfinished receipt, and every reported absence was already recorded; it returns the unchanged receipt and attempt number. `already_absent` includes artifacts deleted earlier, planned by an interrupted attempt and now absent, or previously failed and now absent. Previously recorded absence alone does not require another receipt.

## Evidence

- The ledger records intended deletion before it happens and records the outcome afterward. [4]
- The first no-op records a receipt; an already-recorded unchanged repeat writes none. [5]
- Replacement preserves the prior receipt under that receipt's own number. [6]
- Recorded prior deletion or new absence is reported by the ledger. [7]
