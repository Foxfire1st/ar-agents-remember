# mcp/src/agents_remember/mcp/registration/seat_retirement.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Registers only the retained native retire_child tool, for the starter’s receipt-tracked child seat. It is not the removed structural session-retirement plane.

## Code Commentary

The retire_child signature stays strict while the payload loads only when retirement is invoked.

### Logic

The public signature receives the selected task, role, reason, optional agent ID and explicit interrupt_turn. It constructs RetireChildRequest and delegates to retire_child_payload. Registration owns wire shape and description; receipt ownership and actual host retirement belong to the payload route.

### Invariants And Boundaries

A currently running turn needs explicit interruption authority. Other role agents are refused with the original starter named; repeated retirement is idempotent under the delegate’s contract. This module does not stage or land code.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- Native child retirement registration: implementation/assertion boundary described above. [1]

- The retire_child signature stays strict while the payload loads only when retirement is invoked. [2]
