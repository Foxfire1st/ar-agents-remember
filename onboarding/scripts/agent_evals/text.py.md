# scripts/agent_evals/text.py

## Governing Overview

[overview](overview.md)

## Purpose

Compiles Curator-applicable operations through the production composition manifest and captures delivered details.

## Code Commentary

### Invariants And Boundaries

Compilation uses a fixed synthetic task binding. Text signatures and detail content do not establish actual case authority or a trial result.

Each captured entry also records its instruction origins: `_captured_origins` attributes the shared role block to the single `core:every-role` manifest source, verifies the full on-disk `core/every-role.md` SHA-256 against the manifest source revision, verifies that `shared_block` equals `filter_shared_block(source_bytes.decode("utf-8"), role)`, and offsets the compiled capsule's source spans past that block. A non-unique shared-block source, missing `shared_block`, digest mismatch, or filtered-text mismatch raises `AuthorityError`.

## Evidence

- `capture_curator_text` compiles Curator-applicable operations with a fixed synthetic task binding, prepending Curator-filtered `outcome.shared_block` under `## {SHARED_BLOCK_HEADING}` to the rendered capsule while retaining detail content, revisions, and digests without claiming case authority or a trial result. [1]
- `_captured_origins` verifies the full `core:every-role` source SHA-256 and exact `filter_shared_block` equality for `role`, attributes the shared block to that single source, offsets capsule origins past it, and raises `AuthorityError` on mismatch or ambiguity. [2]
