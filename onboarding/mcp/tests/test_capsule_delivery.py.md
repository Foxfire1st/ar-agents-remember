# mcp/tests/test_capsule_delivery.py

## Governing Overview

[overview](overview.md)

## Purpose

Protects the conversion of a genuinely compiled role capsule into trusted instructions, binding, semantic digest and per-unit instruction origins without admitting task or skill content through an instruction-shaped field, and the launch-time binding of the instructions' relative Markdown links to absolute paths that resolve.

## Code Commentary

### Logic

Independent literals check exactly binding, trusted_instructions, semantic_digest, the separately admitted detail_references field (empty tuple by default) and instruction_origins, and reject blank instructions, malformed digest and empty binding facts. Task text still has no instruction-shaped field; typed detail references are not task text. real_compilation runs the shipped compiler with actual frozen DTOs; conversion checks admitted repository/task/role/operation, rendered instructions, semantic digest and that each instruction origin spans exactly its unit's content. Unknown seat kinds refuse; launcher bindings report the launcher sentinel. At launch, `compose_launch_instructions` resolves each relative link against the source file of the instruction unit it stands in (`bind_markdown_links` leaves non-destinations, code and fenced text alone) and refuses linked instructions whose origins are missing or do not cover the text; detail files bind links to their frozen siblings and the corpus, record revisions of the emitted bytes, and replay validation refuses an emitted detail whose bytes changed. One case composes every manifest role/operation pair and requires every local link in the launch file and its details to resolve.

### Invariants And Boundaries

The genuine role compilation test is distinct from the launcher-shaped stand-in used to exercise sentinel conversion. Static DTO/conversion assertions do not prove a provider session or delivery to a running agent.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- The exact delivery field census admits separate empty-default detail references and instruction origins while task text has no instruction field; genuine compilation supplies admitted binding, instructions, digest and one origin per instruction unit. [1]

- Launch composition binds each relative link to its own instruction unit's source without changing the compiled delivery. [2]
- Link binding rewrites inline, angle, image and reference-definition destinations and leaves external, absolute, detail-marker, code, fenced, indented and escaped text alone. [3]
- Linked instructions without complete covering origins are refused. [4]
- The emitted-link scan skips only fenced examples. [5]
- Every link in every emitted role/operation launch file and its detail files resolves, over the manifest's whole role/operation population. [6]
- Detail links bind to frozen sibling details, revisions hash the emitted bytes, and replay validation refuses a modified emitted detail. [7]
