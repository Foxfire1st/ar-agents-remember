# mcp/tests/test_capsule_delivery.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Protects the conversion of a genuinely compiled role capsule into trusted instructions, binding and semantic digest without admitting task or skill content through an instruction-shaped field.

## Code Commentary

### Logic

Independent literals check the delivery dataclass’s exact fields, reject blank instructions, malformed digest and empty binding facts. real_compilation runs the shipped compiler with actual frozen DTOs; conversion checks admitted repository/task/role/operation, rendered instructions and semantic digest. Unknown seat kinds refuse; launcher bindings report the launcher sentinel.

### Invariants And Boundaries

The genuine role compilation test is distinct from the launcher-shaped stand-in used to exercise sentinel conversion. Static DTO/conversion assertions do not prove a provider session or delivery to a running agent.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- Capsule delivery value boundaries: implementation/assertion boundary described above. [1]
