# mcp/src/agents_remember/models/knowledge/review_frame.py

## Governing Overview

[overview.md](overview.md)

## Purpose

The durable frame's shapes: one presentation lineage, its immutable revisions and manifests, its atomic ready pointer, its drafts, its reclamation receipts, and the opening, staleness and regeneration answers the store returns.

## Code Commentary

`FrameBinding` keeps the existing comparison's full identity per side — repository, tree, commit and ref — plus the conversion's effective tree, and `four_tree_digest`/`artifacts_digest` are conveniences over that identity and over the asset list's bytes only; neither is a signature against replacing both files.
`FrameManifest` holds the frame and revision identity, parent revision, binding, authoring identity, entrypoint, asset manifest with sizes and digests, the evidence packet, supplemental receipts and asset ancestry, and refuses a digest that disagrees with its asset list, an entrypoint it does not list, or a parent that is not older. `FramePointer` is the one atomic ready pointer, so a lineage's current revision is read in one act.
`FrameDraft` keeps an authoring attempt and its lease apart from the ready revision; `FrameReclamation` records intent before bytes are removed and the outcome after; `FrameOpening`, `FrameStaleness` and `FrameRegeneration` state usable/unavailable, `current`/`stale` with the moved sides, and the starting artifact an explicit regeneration receives.

## Evidence

- A revision binds the comparison's every side and the conversion tree, and its artifact digest covers asset bytes only. [1]
- A manifest refuses an inconsistent asset digest, an unlisted entrypoint and a parent that is not older. [2]
- A draft is a leased attempt, separate from the ready pointer. [3]
- A reclamation record is written as intent before removal and as outcome after it. [4]

- `_suffix` maps a kit licence's extensionless `LICENSE` basename to `.txt`, so a pinned licence is served under the plain-text type its manifest entry declares. \[5] [5]
