# mcp/src/agents_remember/application/review_artifact_receipts.py

## Governing Overview

[application overview](overview.md)

## Purpose

Owns archive-hook receipts. The canonical latest receipt is `review-artifact-cleanup.json`; earlier receipts use their own consecutive attempt numbers.

## Code Commentary

`ReceiptLedger.open` reads prior outcomes. When deletion is planned, `begin` writes an `in-progress` receipt with intended deletions before they occur; a refused receipt write prevents deletion. `finish` records the result.

`_set_aside` preserves the canonical receipt under its own attempt number. Repeating that step after interruption reuses that path, rather than allocating another copy. `_previous_attempt` only classifies the prior outcome.

`arCaches` entries carry `path`/`bytes` like `datasetCopies`: the cache-deletion class belongs to the shared artifact keys so every consumer — planned receipts, already-absent replay, remainder counts, deleted names, preview accounting — treats cache deletions exactly like the older classes.

The first attempt writes an initial receipt even when it deletes nothing. A later attempt writes none only if it has no deletion, release or failure, no unfinished receipt, and every reported absence was already recorded; it returns the unchanged receipt and attempt number. `already_absent` includes artifacts deleted earlier, planned by an interrupted attempt and now absent, or previously failed and now absent. Previously recorded absence alone does not require another receipt.

`frameRevisions` joins the shared `_ARTIFACT_KEYS`, so planned receipts, already-absent replay, remainder counts, deleted names and preview accounting treat reclaimed frame revisions exactly like the older deletion classes.

`explainerArtifacts` is also a shared artifact key, so the same planned-receipt, attributed-absence replay, remainder and deleted-name consumers account for the explicitly scoped explainer artifacts. Retirement itself is reported separately from the deletion receipt; a refused deletion receipt does not undo a seat already retired.

## Evidence

- The reclaimed frame revisions are a shared artifact class for every receipt consumer. [8]

- The ledger records intended deletion before it happens and records the outcome afterward. [4]


- The first no-op records a receipt; an already-recorded unchanged repeat writes none. [5]


- Replacement preserves the prior receipt under that receipt's own number. [6]


- Recorded prior deletion or new absence is reported by the ledger. [7]

- The current implementation adds explainerArtifacts to the shared deletion keys and retires environments before deletion receipt admission. [9]
