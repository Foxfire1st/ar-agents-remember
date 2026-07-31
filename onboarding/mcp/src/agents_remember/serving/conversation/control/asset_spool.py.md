# mcp/src/agents_remember/serving/conversation/control/asset_spool.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/asset_spool.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

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

`StagedUpload` (L35, frozen) is the inbound bytes+kind+name+alt; `AssetRecord` (L46) is the persisted
record whose `reference` (L58) yields the `AssetReference` the wire carries. `stage_one` (L67) validates
via `validate_upload` (L85 — MIME allow-list + byte cap against the `AttachmentCapability`), computes
sha256, and writes bytes through `_stage_bytes` (L100) into `confined_path` (L170). `confined_path`
composes `<assets_root>/<requestId>/<assetId>` and `require_safe_component` (L178) rejects any
component that is empty, over 255 bytes, or carries separators/dot-segments before it is joined;
directories are created 0700 and files written 0600. `exchange_bytes` (L124) performs the rebind
byte swap and `verify_recoverable_bytes` (L148) re-verifies the digest on recovery. `alt_for` (L154)
resolves the accessible label + provenance (supplied description vs truthful `name`/`mime` fallback).
`delete_asset_bytes` (L160) removes bytes on disposal. `wire_asset` (L189), `upload_identity` (L198),
and `upload_identity_from_record` (L208) build the identity dicts the receipts and digest parity use.

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

## Docs References

No Domain Documentation source is configured; the spool convention is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The asset reference type and byte reader are the L2E substrate; the lifecycle policy consuming this
boundary is the sibling attachments module; the confinement mirrors the L2E runner-side check.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `AssetReference` type and `read_asset_bytes` this module produces/consumes. | L1-L120 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The lifecycle policy that stages/exchanges/deletes through this boundary: `stage`, `submit`, `attachment_status`, `rebind`, `mark_recoverable`, `delete_recoverable`, plus the expiry sweep, live-store eviction, and spool byte deletion. | L135-L497; L710-L741 | [attachments.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/attachments.py) |
| The `AttachmentCapability` limits `validate_upload` enforces (allow-listed MIME types, `max_bytes`, `max_count`, `description` required/fallback, and the supported-state actionability validator). | L678-L690 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations that drifted as both targets grew. The attachments lifecycle policy is now L135-L497 (`stage` L135, `submit` L204, `attachment_status` L345, `rebind` L375, `mark_recoverable` L460, `delete_recoverable` L484) plus L710-L741 (expiry sweep, eviction, spool byte deletion) in a 795-line file. `AttachmentCapability` in `models.py` is L678-L690, not L406-L678; both claims were made specific about what the ranges cover.

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the attachment spool
  boundary — confined constructed paths, resolve-and-verify containment, 0700/0600 permissions,
  digest compute/verify, and the staged asset data types, extracted from `attachments.py` this round.
  Verification is blank because the new source file is uncommitted; closeout owns its first source
  stamp.
