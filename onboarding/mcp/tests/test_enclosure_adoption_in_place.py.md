# mcp/tests/test_enclosure_adoption_in_place.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Adoption of operation records written in place.

## Code Commentary

MIK-R82 rule 4 as amended: an enclosure holding its operation records in its own lifecycle folder, with no originals under `reports/` and no receipt, is adopted as found. The dry run names the state and lists each record with size and hash; the real run receipts them as found in place, copying and moving nothing. Every case fails without the amendment.

## Evidence

- In-place record adoption with hashed dry-run listing is pinned. [1]
