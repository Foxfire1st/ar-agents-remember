# mcp/src/agents_remember/application/review_evidence_claims.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Resolves a claim's bases against the packet that cites it: an address is evidence only when the packet holds the object it names, and each typed basis must match the item's own identity, revision and inspected range.

## Code Commentary

`evidence_address` parses a `side:path#L1-L2` reference and `read_claim_basis` reads exactly that range through the same bounded investigation read. `resolve_claim` is mechanical and local: `_item_matches` requires a present item of the right kind, side, revision and owner path, and `_range_matches` requires every claimed interval to fit the range actually inspected, so a nonexistent range or a caller-written `present` label cannot supply authority.
A judgment row whose owner the packet does not carry stays unresolved, and an execution result is established only by an admitted proof entry — a proof reference alone is not a passing test.

## Evidence

- A claim's address is read through the same bounded read as other investigation. 
- A basis resolves only when the packet holds a present item of that identity, revision and owner. [2]
- A claimed interval must fit the range the read actually inspected. [3]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_evidence_claims.py::read_claim_basis - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
