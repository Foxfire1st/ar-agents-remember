# mcp/src/agents_remember/canvas/evidence.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Resolves one requested evidence reference against one admitted revision. The frame may ask; the host decides, using only the references the revision's own admitted packet carries, and answers a limitation instead of a destination it cannot prove.

## Code Commentary

- `resolve_evidence_reference` admits a claim basis, a claim, a collection item or a supplemental receipt, and requires the packet and the session binding to name the same comparison in both of its identities.
- A historical or unavailable object keeps its own limitation; the resolver never re-points a reference at today's record.
- Two claims carrying one unnamed reference are refused as ambiguous rather than answered with a guessed basis.

## Evidence

- The host resolves a requested reference only against the revision's own admitted packet. [1]
- The packet and the binding must name the same comparison in both identities. [2]
- A retained receipt answers with its own read state; an unread capture never opens. [3]
