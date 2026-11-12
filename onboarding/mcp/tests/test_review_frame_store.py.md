# mcp/tests/test_review_frame_store.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The frame store's contract cases: full comparison identity including the owner, durable evidence and part maps, the task-total byte ceiling, confinement, draft lifecycle, corruption, explicit removal receipts, and reopening retained revisions after restart. Revision count and lineage size are not ceilings.

## Code Commentary

- A foreign comparison owner is stale even when every operand stays equal; a moved live binding refuses publication before revision or ready-pointer writes. A binding that moves after the locked read leaves the published revision bound to the older comparison.
- Every publication retains earlier revisions. Nine- and ten-revision cases pass the former eight-revision ceiling, keep old bytes readable and write no silent-reclamation receipt. Only the developer's explicit removal produces the retained-revision reclamation account.
- The one store byte ceiling is the task total, measured over revisions, drafts and metadata under the store's admission rules. The next byte refuses as `frame-store-full`, offers the revision selector and preserves the ready revision. Per-revision and manifest bounds remain separate.
- Part maps persist with the revision and reopen without rereading the page; unknown claim IDs are refused, and the map derived from admitted page marks is the map written to the manifest.
- The maximum-store case fills real task-total bytes through one lineage past eight revisions, checks physical bytes, the earliest and latest assets, refusal at the boundary, subprocess restart and archive reclamation. These are source-declared assertions, not a new execution result.

## Evidence

- A revision bound to a foreign comparison is stale. [1]
- The evidence survives the authoring scratch and regeneration names it. [2]
- A developer-removed revision is named when the frame is reopened. [3]

- Ten retained revisions reopen after a subprocess restart; there is no lineage-count ceiling. [4]

- Comparison identity, retained revision bytes, task-total bounds and persisted part maps are checked by the named cases. [5]
