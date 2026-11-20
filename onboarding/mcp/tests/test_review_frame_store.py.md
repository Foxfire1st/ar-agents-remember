# mcp/tests/test_review_frame_store.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The frame store's contract cases: full comparison identity including the owner, durable evidence and part maps, the task-total byte ceiling, confinement, draft lifecycle, corruption, explicit removal receipts, and reopening retained revisions after restart. Revision count and lineage size are not ceilings.

## Code Commentary

- A foreign comparison owner is stale even when every operand stays equal; a moved live binding refuses publication before revision or ready-pointer writes. A binding that moves after the locked read leaves the published revision bound to the older comparison.
- Every publication retains earlier revisions. Nine- and ten-revision cases pass the former eight-revision ceiling, keep old bytes readable and write no silent-reclamation receipt. Only the developer's explicit removal produces the retained-revision reclamation account.
- The task total is measured over revisions, drafts and metadata. Admission of the next byte fails with `frame-store-full`, preserves the ready revision, and offers revision removal. Explicit per-revision and manifest bounds remain separate.
- Part maps persist with the revision and reopen without rereading the page; unknown claim IDs are refused, and the map derived from admitted page marks is the map written to the manifest.
- The maximum-store case fills real task-total bytes through one lineage past eight revisions, checks physical bytes, the earliest and latest assets, refusal at the boundary, subprocess restart and archive reclamation. These are source-declared assertions, not a new execution result.

The video publication case reopens both WebM and MP4 with their media types and checks that their published bytes match the drafts.

## Evidence

- A revision bound to a foreign comparison is stale. [1]
- The evidence survives the authoring scratch and regeneration names it. [2]

- The opened frame reports a developer-removed revision through the removal receipt. [3]


- Publishing and reopening WebM and MP4 preserves each asset's bytes and MIME type. [6]

- The store retains ten revisions. A fresh subprocess opens revision 10 and sees it as ready. [4]
- Nine revisions remain without a silent reclamation receipt. Revisions 1, 5 and 9 serve their original HTML bytes. [5]
