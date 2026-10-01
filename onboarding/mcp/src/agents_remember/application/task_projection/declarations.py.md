# mcp/src/agents_remember/application/task_projection/declarations.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The bound document's requirement declarations, read through the task-intent owner. This module is
where the two admissible requirement routes are told apart, and where an adjacent (non-owned)
declaration is deliberately kept as boundary context instead of being loaded.

## Code Commentary

### Logic

A requirement reaches the projection in one of two admissible forms, and the difference is
load-bearing:

- An **approved packet reference** (`kind: approved-requirement-packet`) is a version-addressed
  identity the task document itself declares. The task-intent owner is what makes it real: it
  confines the path to the task root, reads the file, and verifies the packet's own
  `Stable ID`/`Version` header against the declaring reference. A missing or mismatched packet is
  that owner's typed refusal, mapped here to `projection-requirement-declaration-unresolved` rather
  than swallowed into a partial projection. **This is the standardized policy route** (owner ruling
  of 2026-09-16T10:15 on the L3 leaf document): it needs zero consumer input, so task knowledge does
  not spread into transport adapters and a missing packet becomes a compile-time refusal.
- An **exact-text declaration** is prose. Prose does not opt itself into packet authority, so it is
  projected verbatim with no invented identity and no obligation claim attached to it. The consumer
  must then admit a version-addressed `RequirementPacketLocation` for it.

`read_declarations` normalises both document altitudes into one shape: a leaf projects through
`task_intent_projection`, a master through `task_intent_master_projection` and back into the same
typed union, so every caller sees one vocabulary.

`adjacent` is the deliberate **non-ownership** path. An adjacent declaration is dependency or
preservation context: this seat may not claim it closed, and its packet body is **not read** —
loading it would grow the projection without giving the seat anything it may claim.

`missing_section_gap` is the visible record of an obligation a packet does not carry. A role with no
section is reported as a gap naming the accepted headings, never rendered as nothing.

Nothing here searches for "the packet that looks right". A requirement the admitted binding makes
this seat accountable for, with no declared packet and no admitted location, is refused by the
caller — never resolved by a directory scan.

### Invariants And Boundaries

- Requirement identity is per stable ID **and** version, never aggregate. A packet reference is the
  only source of an owned `"<stable_id>@<version>"` identity; exact text has none.
- An adjacent declaration's packet must not be read. Reading it would turn boundary context into an
  obligation this seat is not accountable for.
- A missing packet section is a **gap**, not an empty obligation: it must stay visible in
  `TaskProjection.gaps`.
- No packet search, no nearest-name match, no directory scan — the three refusals are the whole
  resolution space.
- This module writes nothing; it reads through the task-intent owner only.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The declarations readers, the refusal they map, and the owners that decide packet reality.

- The declarations reader that normalises leaf and master altitudes into one typed union. [1]
- The identity helper: a packet reference yields `"<stable_id>@<version>"`, prose yields `None`. [2]
- The deliberate non-ownership path that does not read an adjacent packet. [3]
- A missing obligation is a reported gap, never an empty section. [4]
- The task-intent owner that confines a declared packet path, reads it and verifies its header. [5]
- The task-root-relative packet confinement the exact-text route reuses rather than reimplements. [6]
- The section role vocabulary a gap is reported against. [7]
- The case that proves every owned obligation is carried verbatim and a missing section is a gap. [8]

### Cross-Repo References

No sibling-repository contract consumes this declarations reader.

No meaningful cross-repo references found.
