# mcp/src/agents_remember/serving/conversation/control/asset_spool.py

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R4's staged-bytes filesystem boundary: every staged byte lives inside the session's user-private
asset spool (`<endpoint-root>/assets/<requestId>/<assetId>`, the L2E endpoint convention), written
through constructed paths only, with resolve-and-verify containment, safe path components, and
private permissions. Bytes are digest-computed at stage and re-verified at rebind. This module owns
the disk mechanics and the staged asset data types; the lifecycle policy lives in `attachments.py`.

## Code Commentary

### Logic

`StagedUpload` (frozen) is the inbound bytes+kind+name+alt; `AssetRecord` is the persisted record
whose `reference` yields the `AssetReference` the wire carries. cit:([`StagedUpload`, `AssetRecord`], mcp/src/agents_remember/serving/conversation/control/asset_spool.py:35-43; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:46-65) cit:([`AssetReference`], mcp/src/agents_remember/models/conversations/control_wire.py:154-162)
`stage_one` validates via `validate_upload` (MIME allow-list + byte cap against the
`AttachmentCapability`), computes sha256, and writes bytes through `_stage_bytes` into `confined_path`.
cit:([`stage_one`, `validate_upload`, `_stage_bytes`, `confined_path`], mcp/src/agents_remember/serving/conversation/control/asset_spool.py:68-83; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:86-98; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:101-122; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:171-176) cit:(["class AttachmentCapability(FeatureCapability):"], mcp/src/agents_remember/models/conversations/capabilities.py:48-48)
`confined_path` composes `<assets_root>/<requestId>/<assetId>` and `require_safe_component` rejects any
component that is empty, over 255 bytes, or carries separators/dot-segments before it is joined;
directories are created 0700 and files written 0600. cit:([`require_safe_component`], mcp/src/agents_remember/serving/conversation/control/asset_spool.py:179-187)
`exchange_bytes` performs the rebind byte swap and `verify_recoverable_bytes` re-verifies the digest on
recovery. `alt_for` resolves the accessible label + provenance (supplied description vs truthful
`name`/`mime` fallback). cit:([`exchange_bytes`, `verify_recoverable_bytes`, `alt_for`], mcp/src/agents_remember/serving/conversation/control/asset_spool.py:125-146; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:149-152; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:155-158)
`delete_asset_bytes` removes bytes on disposal. `wire_asset`, `upload_identity`, and
`upload_identity_from_record` build the identity dicts the receipts and digest parity use.
cit:([`delete_asset_bytes`, `wire_asset`, `upload_identity`, `upload_identity_from_record`], mcp/src/agents_remember/serving/conversation/control/asset_spool.py:161-168; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:190-196; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:199-206; mcp/src/agents_remember/serving/conversation/control/asset_spool.py:209-216)

### Conventions

Daemon-side staging lands only inside the session's user-private spool anchor (the L2E convention);
paths are constructed, never accepted from the wire. Digest verification happens at admission and at
rebind. This is the only module that touches the filesystem for attachments.

### Invariants And Boundaries

- Constructed paths only, resolve-and-verify containment, ≤255-byte safe components, no separators or
  dot-segments; 0700 dirs, 0600 files.
- Digest is computed at stage and re-verified at rebind; a mismatch refuses.
- The spool anchor is request-independent and session-user-private.
- Reviewer precision note 2: the daemon-side `require_safe_component` does not ban backslash while the
  L2E runner-side check does — harmless (the runner is the enforcement boundary; daemon-minted asset
  ids are safe by construction), noted for consistency.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; the spool convention is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The asset reference type and byte reader are the L2E substrate; the lifecycle policy consuming this
boundary is the sibling attachments module; the confinement mirrors the L2E runner-side check.

- The `AssetReference` type and `read_asset_bytes` this module produces/consumes. [1]
- The lifecycle policy that stages/exchanges/deletes through this boundary: `stage`, `submit`, `attachment_status`, `rebind`, `mark_recoverable`, `delete_recoverable`, plus the expiry sweep, live-store eviction, and spool byte deletion. [2]
- The `AttachmentCapability` limits `validate_upload` enforces (allow-listed MIME types, `max_bytes`, `max_count`, `description` required/fallback, and the supported-state actionability validator). [3]
- The upload validator applies those limits at the spool boundary. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
