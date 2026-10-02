# mcp/src/agents_remember/application/knowledge_worklist/registry.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The worklist item-kind registry and the stable item ID (MIK-R08 rules 1 to 3).** Every kind of worklist
item is registered here with four declarations: its subject key, its facts, its satisfying-row rule and its
owner packet. MIK-R08 registers the three kinds it raises (`touched_invariant`, `stale_invariant`,
`reached_family`); the later registrants (MIK-R06 `family_route_condition`, MIK-R10 `unexplained_hunk` /
`unexplained_file`, MIK-R11 `planned_untouched`, MIK-R14 `reconsideration_candidate`, MIK-R30
`onboarding_trace`) call `register_item_kind` when they land.

## Code Commentary

### Logic

- `ItemKind` is the frozen declaration: `name`, `subject` (what the subject names), `subject_pattern`
  (`^INV-` or `^FAM-`, checked by `accepts_subject`), `facts` (the field names the item's `facts` carries),
  `satisfying_row` (the rule as text), `row_lookup` (the rule as a callable, excluded from equality and
  repr) and `owner`.
- `register_item_kind` adds a kind to `ITEM_KINDS` and **refuses a second registration of the same name**
  with `ValueError`; it never overwrites. `registered_kind` looks one up by name, naming a missing kind.
- `subject_row(row_kind)` builds the common satisfying-row lookup: the first row of the leaf's history file
  whose subject is the item's subject and whose row kind (`row_kind_for_subject`) is `row_kind`.
  `satisfying_row(kind, subject, history)` applies the registered kind's lookup.
- `item_id(kind, subject, identities)` is `prefixed_sha256_digest([kind, subject, identities])`: the
  `sha256:<64 hex>` spelling (71 characters) that L07's `items[]` accepts.
- The three MIK-R08 registrations: `touched_invariant` and `stale_invariant` (subject an invariant ID,
  satisfied by the leaf's invariant row, MIK-R07 rule 2) and `reached_family` (subject a family ID,
  satisfied by the leaf's family row, MIK-R07 rule 5). `kinds_document` renders the registry as data,
  sorted by name, for the worklist file and the checklist.
- `GUARANTEE_CHANGED` (`"guarantee-changed"`, L37) is a `reached_family` item's `reachedBy` reason, beside
  `record-changed`: K_C restates the family's guarantee. The gate then holds the family's governing row to
  `changed` (INV-XN0FG8). Facts are not part of an item's identity, so the item ID does not change with it.

### Conventions

- Item identities are passed in by the caller (`compute._touched_item`, `_stale_item`, `_family_item`);
  the registry only hashes them.

### Invariants And Boundaries

- **Item IDs are stable.** They never include whole-file blobs, tree IDs or run IDs: range content
  identities for entries, and each member's `{ id, revision }` per side for a family. A mechanical blob
  change elsewhere in a file keeps the ID.
- **The lookup is not a judgement.** Whether the found row is current is MIK-R09 rule 2's; nothing here
  judges a row.
- **A registration is never replaced**, so a later packet cannot silently redefine a kind.

### Todos

- The five later registrants are not built yet; each registers when it lands.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R08@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`08_change-to-knowledge-worklist.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The four declarations per kind, the later registrants and the item-identity rule. [1]
- The common satisfying-row lookup. [2]
- The kind declaration. [3]
- A second registration is refused. [4]
- The satisfying row of a kind. [5]
- The stable item ID. [6]
- The three MIK-R08 kinds. [7]
- The registry as data. [8]
- Four declarations per kind, a refused duplicate, and a later registrant's lookup. [9]
- An edit elsewhere in the file keeps the ID; different range content changes it. [10]

- The reachedBy reason for a restated guarantee. [11]

### Cross-Repo References

No meaningful cross-repo references found: the registry is in-process data.

No cross-repo boundary is crossed by this file.
