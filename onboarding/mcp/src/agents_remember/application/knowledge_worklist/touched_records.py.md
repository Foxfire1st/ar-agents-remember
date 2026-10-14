# mcp/src/agents_remember/application/knowledge_worklist/touched_records.py

## Governing Overview

[knowledge worklist overview](overview.md)

## Purpose

This module registers `touched_record` and detects exact JSON or Markdown changes to decisions and facet records that existed in the memory base. Its facts carry both sides' revisions and statuses; the satisfying leaf `record` row must match the candidate revision and the kind of change.

## Code Commentary

### Logic

The detector filters base record IDs by the supported decision/facet prefixes, locates the JSON and optional Markdown on both sides, and compares their bytes. A new record raises no item because iteration starts from the base. A missing candidate record is left to structural validation, not silently treated as a retirement judgment.

The only status-mark exemption is a JSON-only change to `under_reconsideration` backed by the current leaf's own `raise` row in an open history file. Changed prose, another JSON field, a foreign raise or a closed attempt prevents that exemption. The per-owner merged history aggregate is deliberately not used to establish this permission.

### Invariants And Boundaries

- A newly retired status requires `retired` at any revision; otherwise a higher revision requires `changed`, and the remaining case requires `no_impact`.
- Markdown addition, deletion and editing can raise an item even when the JSON bytes do not change.
- The detector creates items, not history rows, and does not infer authorship or acceptance from a file change.
- This is the general detector contract. The packet's L53 producer limitation exempts this leaf's own Curator record repairs from writing the new row kind; that handoff qualification is not implemented as a new byte-comparison exception here.

## Evidence

### Repo-Internal References

- The registered satisfying-row contract prioritizes newly retired status before revision growth. [1]
- A qualifying raise must belong to the current owner and an open individual history file. [2]
- The status-only exemption rejects other JSON field changes. [3]
- Exact JSON/prose comparison of base records emits revision/status facts and leaves structural deletion elsewhere. [4]
