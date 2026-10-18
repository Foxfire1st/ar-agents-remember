# mcp/src/agents_remember/application/review_evidence_adapter.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The prepared-evidence seam: takes the landed comparison owner's opened trees with their measured side/index states, reads the landed schemas at that exact tree, and produces the packet plus exact addresses its consumers can open.

## Code Commentary

`prepare_evidence` consumes the comparison owner's measured states rather than caller-supplied completeness, so a partial index stays partial and a lost history keeps its owner's reason. It builds the source, family, judgment, proof and sidecar collections at the memory candidate, records limitations beside the packet, and prepares addresses in the landed owners' own identifiers.
`consume_address` resolves one prepared address only for the comparison that prepared it; `_carried` checks the owner path, side, revision, row/attempt/proof identity together, so an address pointing at another owner or comparison is unresolved rather than merely missing.

## Evidence

- Preparation preserves the comparison owner's measured index and side states. [1]
- An address resolves only inside the comparison and owner path that prepared it. [2]
- A carried item is matched on its whole identity, not on a single field. [3]
