# mcp/src/agents_remember/cli/role_instruction_details.py

## Purpose

Bind compiled capsule detail pointers to immutable per-request files and validate them on replay.

## Governing Overview

[overview](../../../overview.md)

## Current Contract

`compose_launch_instructions(delivery, report_path, choice, *, compact_links=False, corpus_root=None)` freezes `delivery.detail_references` beside `report_path`, replaces `{{detail:<source>}}` placeholders in trusted baseline text, and delegates user append/`<overwrite>` composition to the existing instruction owner. Under default `compact_links=False` (used by standalone callers such as `scripts/agent_evals`), it writes flat sibling `<stem>.detail-<sha256>.md` files via `write_detail_artifacts` and substitutes their absolute paths. Under opt-in `compact_links=True` (used by Turn-1 launch preparation), it writes read-only files into `<stem>.details/<source_path>` via `_write_nested_detail_artifacts` — preserving outer report-access or locator symlinks while confining every interior directory under `<stem>.details/` to real non-symlink directories (`_require_non_symlink_directory`, `_ensure_real_directory`, `is_relative_to`) — and substitutes compact `detail/<quoted-source>` links. The composition record keeps `sourcePath`, `path` (exact on-disk path), `revision`, `sizeBytes`, and `step` for each detail.

Before freezing, relative Markdown links are bound through `cli/role_instruction_links` against `_corpus_root_context` (explicit `corpus_root`, else `durable_composition_corpus_root()` when `compact_links=True`, else `shipped_composition_corpus()`). Frozen detail files always bind internal links with `compact_links=False` to absolute durable corpus paths and sibling frozen detail paths (`_bound_details`) so every frozen detail stays self-contained after provider exit; a frozen detail's revision is the digest of its bound bytes and the compiler's delivery value is not changed. The inline baseline is bound span by span along `delivery.instruction_origins` (`_bound_baseline`), emitting compact `detail/<rel>` and `skill/<rel>` links under `compact_links=True` (keeping out-of-corpus targets absolute) and compacting `skill://` URIs via `compact_skill_uri_links` even when `instruction_origins` is absent; incomplete origins or unbound relative links refuse with `CapsuleDeliveryError`.

`validate_instruction_detail_artifacts` permits a detail-free composition, but a present `detailReferences` must be a list of valid objects. Every item requires `sourcePath`/`path`/`revision` and a saved report and handover reference. The handover's given path must resolve to the report's `.handover.txt` sibling — its parent may be the request's locator — and its recorded canonical basename must agree with that sibling. `_require_detail_target` accepts either the legacy flat `<stem>.detail-<sha256>.md` sibling or the confined nested `<stem>.details/<source_path>` layout (`_require_nested_detail_target`), validating POSIX source parts (`_validated_detail_source_parts`), confinement under `<canonical_handover_parent>/<stem>.details/`, and real non-symlink interior directories via `os.lstat`. A regular no-follow/nonblocking open must have SHA-256 equal to `revision`. This supports real local role-report directories and legacy report-access links without confusing the report's future collection destination with the frozen artifact's location.

A changed, missing, rebound, interior-symlinked, or nonregular snapshot refuses before sending with original-file/report-access restoration and same-request retry advice. It never regenerates details from a changed corpus. Validation establishes the saved references' targets and bytes, not a fresh compilation or independent semantic review.

Preparation calls composition; the receipt restoration path and delayed held-seat opening consume validation. User-note precedence remains with `compose_role_instructions`; detail snapshots do not confer new role authority.

## Evidence

- Every saved detail is shape/identity/type/revision checked. [2]
- The replay regression refuses a rebound canonical folder despite equal detail bytes and restores a missing valid legacy access link. [5]

- `compose_launch_instructions` freezes details (nested symlink-confined `<stem>.details/<source>` when `compact_links=True` or flat `.detail-<sha256>.md` when `compact_links=False`) and substitutes pointers before user-note composition. [1]
- `_require_detail_target` and `_require_nested_detail_target` accept either legacy flat `.detail-<sha256>.md` or interior-non-symlink-confined `<stem>.details/<source_path>` targets beside the saved handover's canonical directory. [3]
- Held-seat opening and receipt restoration invoke `validate_instruction_detail_artifacts` before sending the opening message. [4]
- `_bound_details` binds frozen detail internal links to absolute durable corpus and sibling frozen paths (`compact_links=False`) and re-digests the bound bytes before freezing. [6]
- `_bound_baseline` binds baseline links along `instruction_origins` (compact `detail/` and `skill/` under `compact_links=True`, plus `compact_skill_uri_links` without origins) and refuses incomplete origins or unbound relative links. [7]
- `nested_detail_root`, `_validated_detail_source_parts`, `nested_detail_path`, and `_corpus_root_context` define the confined nested detail layout and durable corpus root selection. [9]
