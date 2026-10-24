# mcp/tests/test_review_evidence_intended.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The `intended` authority and its enforcement: on a planned binding a claim resting only on packet, task-document or reference receipts is refused as recorded fact and accepted as intended, while every other binding is unchanged.

## Code Commentary

- Only the three intended roots are admitted; developer direction and every other root are not intended sources, and an intention cannot rest on a tree blob alone.
- The same claim on another binding keeps today's kinds, so pages already written are untouched.
- A claim that also cites code or memory at the master tip keeps its recorded kind rather than being relabelled.
- `prepare_evidence` runs the enforcement itself, on a planned binding and only there, and a comparison with no measured code side is a named refusal while a lost side is carried with its limitation.

## Evidence

- The case `test_the_admitted_intended_roots_are_the_three_the_rule_names` protects the admitted intended roots being exactly the named ones. [1]
- The case `test_a_planned_binding_refuses_a_receipt_only_claim_as_recorded_fact` protects a receipt-only claim being refused as a recorded fact on a planned binding. [2]
- The case `test_the_same_claim_on_another_binding_is_unchanged` protects a claim on another binding keeping its kinds. [3]
- The case `test_prepare_evidence_refuses_the_claim_on_a_planned_binding` protects the enforcement running inside evidence preparation on a planned binding. [4]
- The case `test_e01_a_truly_absent_code_side_is_a_named_refusal_never_a_packet` protects a comparison with no measured code side being refused by name instead of becoming a packet. [5]
