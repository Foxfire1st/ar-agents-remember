# mcp/tests/test_direct_landing_leaf_identity.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Protect explicit direct-landing leaf identity, closed history creation and kept closing-receipt recovery.

## Code Commentary

Supplied leaf_id is exercised through the public direct-landing tool as well as the history selector. Wrong/open and invalid owners refuse by name. Recovery proof deliberately has two scopes: the public lifecycle control currently refuses intent-less interrupted direct generations as lifecycle-control-not-legal, while the real recovery executor settles the kept receipt. The latter does not establish public-control availability; that separate owner is MIK-R143.

## Evidence

No external Domain Documentation source is configured for this repository. The following source witnesses establish the contract, not a new execution receipt.

- The supplied identity reaches the operation record and closed history. [1]
- Public recover is currently unavailable and preserves the generation. [2]
- The real executor settles the kept receipt independently of public-control legality. [3]
