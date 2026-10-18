# mcp/src/agents_remember/application/review_judgment_proofs.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Show proof entries for the selected invariant, or members of the selected after-tree family, with MIK-R03 observation at the bound after code tree.

## Code Commentary

`judgment_proofs` obtains family members from the after index, otherwise uses the invariant subject directly. It opens the bound candidate code tree and calls the shared observe_entry for each proof. The result keeps entry identity, invariant, test path, symbol when the locator is a symbol, facet, state and the observation reason. A current anchor does not mean that a test was run, passed, or establishes semantic satisfaction. This owner reads no history and does not alter proof entries.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- Proof projection uses after-tree family membership and shared after-code currentness, not execution acceptance. [1]
