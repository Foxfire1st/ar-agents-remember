# mcp/src/agents_remember/application/review_frame_store.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The task-confined frame store: leases an authoring draft in its working folder, publishes an immutable revision atomically under every ceiling, reopens and serves one verified snapshot, judges staleness against the selected comparison, and reclaims superseded bytes with durable receipts.

## Code Commentary

`FrameScope` verifies the task and frame physically before any IO, including symlinked intermediates; `begin_draft` requires the caller's explicit working directory outside the task, keeps only a bounded attempt record beside the task, and imports the recorded assets under the task lock after size and digest checks, so a ready page never depends on the authoring scratch. `publish_revision` validates the draft, binding, evidence, manifest, containment and every ceiling before it writes anything, writes the revision directory completely and then moves the ready pointer last, and a retry of the same request and bytes adds no second revision.
`_manifest_bytes` and `_snapshot` read stored metadata through the finite sentinel bound and verify a revision's manifest digest and every asset digest from one read, so reopening, asset serving and regeneration share one integrity-checked snapshot; a corrupt or changed byte yields `unavailable` naming the asset. `frame_staleness` compares the retained binding with the selected comparison's full identity and reports the moved sides, offering regeneration and starting nothing; `regeneration_request` hands the stale revision's own assets and evidence to the authoring attempt.
`cleanup_frames` and `reclaim_task_frames` are the reclamation owners: a dry run, newest-N retention with the ready revision always kept, per-target failure records, task-lock serialization with publication, and an archive receipt written before the bytes are removed.

## Evidence

- Every store act is verified against the admitted task and frame before it touches the filesystem. [1]
- A draft is leased in its caller's working folder and imported only under the task lock after digest checks. [2]
- A publication validates everything before it writes, then moves the ready pointer last. [3]
- A stored metadata read is bounded by the admitted byte sentinel. [4]
- Reopening, serving and regeneration read one verified snapshot of manifest and assets. [5]
- Staleness names the comparison sides that moved and starts no regeneration. [6]
- Reclamation records intent before removal and the outcome after it, under the task lock. [7]

- `_media_type` names the same plain-text type for an extensionless `LICENSE`, which is what lets a frame serve a pinned kit licence at all. \[8] [8]
