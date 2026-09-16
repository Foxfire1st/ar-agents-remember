# mcp/src/agents_remember/application/task_projection/declarations.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/declarations.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| lastVerifiedCommitDate | 2026-09-16T10:52:30+02:00|
| governingOverview      | `../overview.md`                           |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The declarations readers, the refusal they map, and the owners that decide packet reality.

| Finding | Anchor | Source |
| --- | --- | --- |
| The declarations reader that normalises leaf and master altitudes into one typed union. | `read_declarations`; `RequirementDeclaration` | mcp/src/agents_remember/application/task_projection/declarations.py:50-74; mcp/src/agents_remember/application/task_projection/declarations.py:43-47 |
| The identity helper: a packet reference yields `"<stable_id>@<version>"`, prose yields `None`. | `declaration_identity` | mcp/src/agents_remember/application/task_projection/declarations.py:77-82 |
| The deliberate non-ownership path that does not read an adjacent packet. | `adjacent` | mcp/src/agents_remember/application/task_projection/declarations.py:85-107 |
| A missing obligation is a reported gap, never an empty section. | `missing_section_gap` | mcp/src/agents_remember/application/task_projection/declarations.py:110-120 |
| The task-intent owner that confines a declared packet path, reads it and verifies its header. | `task_intent_projection`; `task_intent_master_projection`; `TaskIntentRequirementPacket`; `TaskIntentRequirementText` | mcp/src/agents_remember/tasks/task_intent.py:132-177; mcp/src/agents_remember/tasks/task_intent.py:196-222; mcp/src/agents_remember/tasks/task_intent.py:52-56; mcp/src/agents_remember/tasks/task_intent.py:47-49 |
| The task-root-relative packet confinement the exact-text route reuses rather than reimplements. | `confine_non_symlink_rel` | mcp/src/agents_remember/kernel/sidecar_pairing.py:52-88 |
| The section role vocabulary a gap is reported against. | `PacketSectionRole`; `PACKET_SECTION_HEADINGS` | mcp/src/agents_remember/application/task_projection/packets.py:43-50; mcp/src/agents_remember/application/task_projection/packets.py:64-81 |
| The case that proves every owned obligation is carried verbatim and a missing section is a gap. | `test_every_owned_obligation_is_carried_verbatim_and_a_missing_section_is_a_gap` | mcp/tests/test_task_projection.py:801-830 |

## Cross-Repo References

No sibling-repository contract consumes this declarations reader.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the requirement-declaration
  reader added by the scoped-task-context leaf (`CAPS-R03@v1`). Records both admissible routes (the
  typed `approved-requirement-packet` reference as the standardized policy, and the exact-text route
  needing an admitted location), the deliberate non-ownership path that does not read an adjacent
  packet's body, the missing-section gap rule, and the no-search boundary. Verification metadata is
  left at the leaf base commit because the source is uncommitted — the governed closeout stamps the
  real code commit.
