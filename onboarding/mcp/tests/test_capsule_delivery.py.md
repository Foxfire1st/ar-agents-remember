# mcp/tests/test_capsule_delivery.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Protects the conversion of a genuinely compiled role capsule into trusted instructions, binding and semantic digest without admitting task or skill content through an instruction-shaped field.

## Code Commentary

### Logic

Independent literals check exactly binding, trusted_instructions, semantic_digest and the separately admitted detail_references field (empty tuple by default), and reject blank instructions, malformed digest and empty binding facts. Task text still has no instruction-shaped field; typed detail references are not task text. real_compilation runs the shipped compiler with actual frozen DTOs; conversion checks admitted repository/task/role/operation, rendered instructions and semantic digest. Unknown seat kinds refuse; launcher bindings report the launcher sentinel.

### Invariants And Boundaries

The genuine role compilation test is distinct from the launcher-shaped stand-in used to exercise sentinel conversion. Static DTO/conversion assertions do not prove a provider session or delivery to a running agent.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- The exact delivery field census admits separate empty-default detail references while task text has no instruction field; genuine compilation still supplies admitted binding/instructions/digest. [1]
