# mcp/tests/test_record_landing_stale_debt.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Recording stale-entry debt at its actual proof boundaries.

## Code Commentary

The helper cases distinguish a complete stale-only finding set from mixed or truncated refusals and round-trip the `<path>#<entry id>` debt cell.

The reconciled-source case calls the real public tool in dry and apply modes after synchronization advances the code base; it records successfully with no staleEntries debt. The transport case obtains an actual gate finding before that sync, calls the real preconditions after sync and carries the finding across that boundary. It then checks the complete saved debt and next tool and verifies any conditionally delivered fields. Dry run leaves the contract bytes unchanged, and apply keeps the debt key and integrated commit.

A public stale-debt recording remains unexercised. No supported sequence preserving that complete case was found because supported synchronization advances the code base to the landed tip; the approved proof is at the nearest real boundary. The separate chain case uses the real registered tool without the debt-transport patch and asserts knowledge-gate-refused, the offending master-chain sentence, no staleEntries answer and unchanged contract for both dry run and apply.

A separate fixed-locator matrix runs the production response shaper and tokenizer in both landing states. It constructs whole delivery, cut delivery with IDs, named omission, count only and a cut whose exact locator leaves too little room for the next step. The assertions keep the 700-token whole and 400-token cut bounds distinct.

These source assertions and their retained route-review evidence do not supply a new test execution or memory acceptance.

## Evidence

### Repo-Internal References

These tests establish the assertions below; their definitions are separate from retained execution receipts.

- The parser recognizes a complete stale-only finding and rejects mixed or truncated finding sets. [1]
- The answer names the debt and the contract round-trip preserves its record keys. [2]
- The real public dry/apply route records a reconciled source with no remaining staleEntries debt. [3]

- The transport case carries earlier gate-produced findings across a controlled precondition boundary after real admission. It checks the complete saved result, delivered values when present and dry/apply contract persistence. [4]

- The unpatched real public dry/apply route refuses an invalid master chain without staleEntries or a contract write. [5]

- The two-state matrix constructs five measured answer shapes using the real shaper and controlled logging boundary, including the long-locator case with count and exact locators. [6]
