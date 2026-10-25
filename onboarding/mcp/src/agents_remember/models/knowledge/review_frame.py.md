# mcp/src/agents_remember/models/knowledge/review_frame.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The durable frame's shapes: one presentation lineage, its immutable revisions and manifests, its atomic ready pointer, its drafts, its reclamation receipts, and the opening, staleness and regeneration answers the store returns.

## Code Commentary

`FrameBinding` keeps the comparison owner's identity and the full identity per side — repository, tree, commit and ref — plus the conversion's effective tree, and `four_tree_digest`/`artifacts_digest` are conveniences over that identity and over the asset list's bytes only; neither is a signature against replacing both files.
`comparison_reference` addresses a recorded comparison, while `planned_reference` uses a separate planned address; owner equality prevents a planned binding from matching a landed comparison numbered zero.
`FrameLimits` bounds files, revision bytes, manifest bytes, task bytes and draft bytes. It carries no revision-count or lineage-byte eviction threshold.
`FrameManifest` holds the frame and revision identity, parent revision, binding, authoring identity, entrypoint, asset manifest with sizes and digests, the evidence packet, supplemental receipts and asset ancestry, and refuses a digest that disagrees with its asset list, an entrypoint it does not list, or a parent that is not older. `FramePointer` is the one atomic ready pointer, so a lineage's current revision is read in one act.
`FramePart` assigns known claim ids to uniquely named parts. `_parts_are_true` refuses unknown or multiply mapped claims and, when there is a mapping, requires every revision claim to appear. `_supplemental_is_true` requires the manifest receipts to match the packet ids, canonical sources, digests and read states exactly.
`FrameDraft` keeps an authoring attempt and its lease apart from the ready revision; `FrameReclamation` records intent before bytes are removed and the outcome after; `FrameOpening`, `FrameStaleness` and `FrameRegeneration` state usable/unavailable, `current`/`stale` with the moved sides, and the starting artifact an explicit regeneration receives. `FrameStalePart` carries each affected part and its changed-basis reasons; a nonempty stale-parts list requires the revision state to be `stale`.

## Evidence

- A revision binds the comparison's every side and the conversion tree, and its artifact digest covers asset bytes only. [1]
- A manifest refuses an inconsistent asset digest, an unlisted entrypoint and a parent that is not older. [2]
- A draft is a leased attempt, separate from the ready pointer. [3]
- A reclamation record is written as intent before removal and as outcome after it. [4]

- `_suffix` maps a kit licence's extensionless `LICENSE` basename to `.txt`, so a pinned licence is served under the plain-text type its manifest entry declares. [5]

- Recorded and planned bindings retain distinct owners and addresses. Limits omit revision-count and lineage-byte eviction thresholds; part maps keep each revision’s own claims and supplemental receipts match the packet exactly. Stale-part reasons are present only on stale revisions. [6]
