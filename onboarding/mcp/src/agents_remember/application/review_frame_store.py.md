# mcp/src/agents_remember/application/review_frame_store.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The task-confined frame store: leases an authoring draft in its working folder, publishes an immutable revision under its byte bounds, reopens and serves one verified snapshot, judges staleness against the selected comparison, and receipts the developer’s explicit removal of retained revisions.

## Code Commentary

`FrameScope` verifies the task and frame physically before any IO, including symlinked intermediates; `begin_draft` requires the caller's explicit working directory outside the task, keeps only a bounded attempt record beside the task, and imports the recorded assets under the task lock after size and digest checks, so a ready page never depends on the authoring scratch. `publish_revision` validates the draft, binding, evidence, manifest, containment and the task byte cap before installing a revision. The staged advisory inventory is included in the byte meter when it fits. A fitting revision still publishes with a plain omission reason when storage runs short for the advisory sidecar. The ready pointer moves after the revision directory lands. A retry of the same request and bytes adds no second revision.
`_manifest_bytes` and `_snapshot` read stored metadata through the finite sentinel bound and verify a revision's manifest digest and every asset digest from one read, so reopening, asset serving and regeneration share one integrity-checked snapshot; a corrupt or changed byte yields `unavailable` naming the asset. `frame_staleness` compares the retained binding with the selected comparison's full identity and reports the moved sides, offering regeneration and starting nothing; `regeneration_request` hands the stale revision's own assets and evidence to the authoring attempt.
`cleanup_frames` removes only expired drafts and keeps every published revision. `remove_revisions` is the developer’s explicit revision-removal owner: it validates the whole request under a finite-budget task lock, protects the verified agreed pin and any ancestor a retained revision’s regeneration lineage needs, and records the removed numbers and artifact digests before and after deletion. Removing the ready revision moves the pointer to the newest retained revision or clears it; a removed number is never issued again. `reclaim_task_frames` remains the archived task’s reclamation owner with its own intent/outcome receipt.

The store derives the binding and admits planned claims before it enters its task lock. Under that lock it revalidates the live binding when the optional callback returns one, checks mandatory bytes and stages any inventory that fits. Registered explainer render already holds the shared task lock around publication and inventory recording. Direct Presenter publication supplies no binding callback. It persists readiness’s admitted part map. Explicitly configured per-revision limits still apply. A full store offers the explicit removal control.

The asset store maps .webm to video/webm and .mp4 to video/mp4. Both formats use the same admission, byte accounting and publication path as other draft assets.

## Evidence

- Every store act is verified against the admitted task and frame before it touches the filesystem. [1]
- A draft is leased in its caller's working folder and imported only under the task lock after digest checks. [2]
- A publication validates everything before it writes, then moves the ready pointer last. 
- A stored metadata read is bounded by the admitted byte sentinel. [4]
- Reopening, serving and regeneration read one verified snapshot of manifest and assets. 
- Staleness names the comparison sides that moved and starts no regeneration. [6]
- Reclamation records intent before removal and the outcome after it, under the task lock. 



- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_frame_store.py::publish_revision - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_frame_store.py::_snapshot - the bytes it recorded now occur 7 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_frame_store.py::reclaim_task_frames - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The store admits WebM and MP4 through its asset media-type table. [10]

- The media-type resolver treats the extensionless kit LICENSE as plain text. [8]


- The store derives the binding and admits planned claims before it enters its task lock. Under that lock it revalidates the live binding when the optional callback returns one, checks mandatory bytes and stages any inventory that fits. Registered explainer render already holds the shared task lock around publication and inventory recording. Direct Presenter publication supplies no binding callback. [9]
