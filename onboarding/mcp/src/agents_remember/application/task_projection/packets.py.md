# mcp/src/agents_remember/application/task_projection/packets.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Read one requirement packet through the existing owners, then split it into **verbatim** `##`
sections. Two concerns live here and nothing else: **location and presence** (owned elsewhere) and
**section split** (a projection concern with no other owner).

## Code Commentary

### Logic

**Location is not decided here.** `read_packet` is the only route that opens a packet, and it always
confines first:

- for an **exact-text** declaration the consumer supplies a task-root-relative location, which this
  module confines with the kernel's non-symlink artifact guard `confine_non_symlink_rel`;
- for an **`approved-requirement-packet`** reference the task-intent owner has already confined,
  read and header-verified the file, so `parse_packet` is handed bytes that are already admitted.

There is no third route, no search for "the packet that looks right", and no default. A missing,
escaping, symlinked, non-Markdown or non-UTF-8 packet is a concrete source-resolution refusal
(`projection-requirement-packet-invalid`, `projection-requirement-packet-missing`) — the projection
never substitutes another file and never proceeds without the obligation it was asked for.

**Section split is verbatim.** `split_sections` keeps every `##` section byte-for-byte in document
order; only the layout blank lines surrounding a body are stripped, never anything inside it. A
`###` sub-heading stays inside its parent section's body, so the packet's own structure is preserved
rather than flattened.

`INJECTED_PACKET_ROLES` names the six sections carrying an obligation the projection must not lose
(normative requirement, required behavior, preservation boundaries, exclusions, failure and
recovery, expected evidence). `PACKET_SECTION_HEADINGS` maps each role to its accepted exact
spellings — **template form first, shipped-corpus sentence-case form second** — and matching is
exact, never by substring, because a packet heading is a declared structure rather than prose to
guess at. A heading outside the table is never dropped: every section stays in
`RequirementPacketProjection.sections`, and a role with no section is reported as a gap.

`referenced_headings` lists every heading outside the injected roles, in document order, so
"referenced" is a decision with a visible record and never a silent drop.

### Conventions

The canonical packet shape comes from `skills/w-02-light-task-workflow/requirement-packet-template.md`.
A new injected role is one entry in `PacketSectionRole`, `INJECTED_PACKET_ROLES` and
`PACKET_SECTION_HEADINGS` in the same edit — the three must stay in step.

### Invariants And Boundaries

- **No length budget exists anywhere in this module.** If you find yourself adding a `[:n]`, a
  `max_lines` or a "summary" step, you are implementing the defect the requirement names
  (`CAPS-R03@v1` required behaviour 5).
- A packet heading is matched exactly against the declared spellings. Widening a match to a
  substring would let a differently-named section claim a role it does not play.
- A role with no section is a **gap**, never rendered as an empty obligation.
- `confine_non_symlink_rel` is reused rather than reimplemented; a second confinement check would be
  a second place for the rule to drift.
- Nothing here writes, and nothing here reaches outside the task root.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The confinement route, the verbatim splitter, the heading table and the refusal that guards an
absent obligation.

- The confined packet read — the only place a packet is opened. [1]
- The splitter for already-admitted bytes, and the verbatim section split. [2]
- The six obligation-carrying roles and their accepted exact spellings. [3]
- Exact heading lookup, and the headings that travel as references instead. [4]
- The refusal an absent or unreadable packet raises, naming both admissible remedies. [5]
- The kernel's non-symlink artifact guard this module reuses for a consumer-supplied path. [6]
- The canonical packet shape the heading table follows, including its template section headings. [7]
- The case that proves an owned obligation is carried verbatim and a missing section is a gap. [8]

### Cross-Repo References

No sibling-repository contract consumes this reader.

No meaningful cross-repo references found.
