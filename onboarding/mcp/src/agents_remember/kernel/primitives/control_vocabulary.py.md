# mcp/src/agents_remember/kernel/primitives/control_vocabulary.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The control vocabulary the role-execution and bridge seams share: the spellings a receipt, a held store, a report log and a provider-limit hold carry on disk and across the wire.

## Code Commentary

- Each name is one `Final` string defined once here because the tier that writes it (`cli`), the tiers that read it (`application`, `canvas`, `serving`) and the wire that types it must agree on the same bytes.
- The set covers the directory role-execution receipts live in, their schema name, the report log's name, the held store's schema, the reason a provider-limit hold names, and the bridge's three outcomes.
- The bridge's outcomes are distinguished here rather than collapsed: a timeout, a refused call and a send whose outcome is unknown are three different facts a caller classifies a failed call by.
- This module imports nothing internal and holds no policy — it is vocabulary only, so any tier may import it.

## Evidence

- Role-execution receipts live under one shared directory name [1]
- Every execution receipt of this line carries one schema name [2]
- A held-message store is recognisable by one schema name [3]
- A send whose outcome is unknown is its own named outcome, not a timeout or a refusal [4]
