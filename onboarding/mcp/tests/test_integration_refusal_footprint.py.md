# mcp/tests/test_integration_refusal_footprint.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Protect no-write landing refusal and exact closeout-cell pair selection.

## Code Commentary

Snapshots cover contract bytes, worklist presence/content and both ref inventories across preview and apply. The edited-cell witness contrasts a readable closeout memory without a record deletion with one that deletes a base-held record: the current cell, not a stale verdict, decides which findings appear.

## Evidence

No external Domain Documentation source is configured for this repository. The following source witnesses establish the contract, not a new execution receipt.

- Apply refusal preserves contract, worklist and refs. [1]
- Recorded landing refusal also preserves its footprint. [2]
- Changed cells produce their actual record-kept finding. [3]
