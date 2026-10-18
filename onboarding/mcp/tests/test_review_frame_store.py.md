# mcp/tests/test_review_frame_store.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The frame store's contract cases: revision binding and ancestry, evidence surviving the authoring scratch, lineage and task byte ceilings, symlinked containment, live and abandoned drafts, corrupt bytes, refused publication, reclamation receipts, and restart at the largest admitted store.

## Code Commentary

The module exercises MIK-R103 rules 1-11 through the store: a foreign comparison is stale, a lineage ceiling counts revisions, drafts and metadata, a symlinked frame is held by every act, an archived frame is explained by the task receipt, and the default manifest and store ceilings are measured rather than assumed.

## Evidence

- A revision bound to a foreign comparison is stale. [1]
- The evidence survives the authoring scratch and regeneration names it. [2]
- A reclaimed revision is named when the frame is reopened. [3]
- The largest admitted store, filled to the default ceiling, reopens after a subprocess restart. [4]
