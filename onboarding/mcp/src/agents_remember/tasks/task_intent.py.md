# mcp/src/agents_remember/tasks/task_intent.py

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

The normative task-intent projection of one leaf task document and its identity. The module turns a
resolved task document into the strict `task-intent/v1` projection of allowlisted normative fields, hashes
its canonical JSON into the intent digest, and offers the one currentness assertion that owners call
before they reuse evidence. It is also the owner that confines, reads and checks an approved requirement
packet.

## Code Commentary

### Projection and identity

- `TaskIntentV1` holds the leaf identity, objective, requirements, design, steps with substeps, code
  examples with their note, acceptance obligations and the optional `expectedKnowledgeEffects`. Every model
  is frozen and forbids extra fields. `canonical_value` drops `expectedKnowledgeEffects` when it is `None`,
  so a document that declares none projects without the key.
- `_ROOT_FIELDS` and `_NESTED_FIELDS` name the fields the projection consumes.
  `_validate_allowlisted_classifications` compares them with the shared field taxonomy
  (`document_field_effects`) in both directions and raises `task-intent-schema-unclassified` for a slot
  that is not classified normative and for a normative field outside the projection.
- `task_intent_projection` refuses a master (`task-intent-leaf-required`) and an unsupported schema
  version. `task_intent_identity` is the SHA-256 of the projection's canonical JSON with sorted keys and
  compact separators. `task_intent_master_projection` projects a master's own normative fields as a plain
  mapping and refuses a leaf.
- `require_current_task_intent(observed, current, owner=..., next_action=...)` raises
  `<owner>-task-intent-stale` when the observed identity differs from the current one.
- `_requirements` refuses blank requirement text, and refuses packet references without any exact text
  (`task-intent/v2-cutover-required`).

### The requirement packet owner

`_approved_packet_ref(task_root, reference)` is called for a packet reference of the projection and, through
`memory/knowledge/requirement_owner.consume_owner_resolution`, for every requirement endpoint of a
knowledge record.

1. It resolves the task root and then `<root>/<reference path>`, both through `observed_resolve`.
2. An absolute reference path, a resolved path outside the task root, or a suffix other than `.md` raises
   `task-intent-requirement-packet-outside-task`. This happens before any byte of the packet is read.
3. It reads the packet's bytes once. A missing or unreadable file raises
   `task-intent-requirement-packet-missing`.
4. The text is decoded as UTF-8 with `\r\n` and `\r` turned into `\n`. `_packet_metadata` reads the
   two-column table before the first `## ` heading; a repeated field raises
   `task-intent-requirement-packet-metadata-ambiguous`. `Stable ID` or `Requirement ID` must equal the
   reference's ID and `Version` its version, else `task-intent-requirement-packet-version-mismatch`.
5. The result names the packet by its resolved path relative to the task root.

Inside a recording block the call leaves these rows: one `resolve:` row for the task root, one `resolve:`
row for `<resolved task root>/<reference path>` with the reference path's own links unresolved, and one
byte row under that same path with the SHA-256 of the bytes read, `absent`, or `unreadable (...)`. The byte row is keyed by the caller's locator,
not by the file the locator pointed at. A symbolic link that is retargeted afterwards therefore changes the
`resolve:` row, even when the other target holds the same bytes, and a packet that resolves outside the
task root leaves the `resolve:` row and no byte row. Outside a recording block the function records nothing
and its answers and errors are the same.

## Evidence

- The strict projection and the dropped key for an absent declaration. [12]
- The fields the projection consumes. [13]
- The projection entry point refuses a master. [14]
- The digest of the canonical projection. [15]
- The currentness assertion. [16]
- The allowlist and the taxonomy must agree in both directions. [17]
- Requirement text and packet references. [18]
- The packet owner: recorded resolutions, confinement before reading, one read recorded under the caller's locator, identity check. [19]
- The metadata table of a packet. [20]
- The requirement owner calls the packet owner and carries its refusal back. [21]
- A packet link retargeted outside the task and back is recorded by its resolve row; outside, no packet byte is read or recorded. [22]
- A packet changed and restored while it is read, and a link retargeted during the read, are recorded under the link's own path. [23]
