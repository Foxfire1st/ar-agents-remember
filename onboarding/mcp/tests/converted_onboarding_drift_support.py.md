# mcp/tests/converted_onboarding_drift_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Builds the trees, cards, anchors and validation binding the converted-drift cases share, so the two case modules cannot disagree about what a converted memory or a stale anchor is (MIK-R44@v2).

## Code Commentary

`_code_tree` makes a git checkout with two tracked sources; `_converted_memory` makes a memory checkout whose `knowledge/layout.json` holds the `ar-memory-layout/v2` marker. Anchors come from `_anchor` over `git_blob_id` and `content_identity`, with `_current_anchor` reading the file and `_stale_anchor` returning zeros. `_write_card` writes a canonical sidecar plus a marked card. `_context` returns the onboarding/memory/coordination/temp roots as a namespace. `bound_validation_services` binds real `WorktreeServices` with `GitKnowledgeValidation` over the git base converter so a first baseline validates before it commits, and resets on exit. `_world` writes a settings file with one repository; `_adoptable_converted_world` runs `memory_init_tool` and can plant a stale anchor on a present or absent source, or a current anchor with `card=True`. Adoption-path fixtures use the current form to reach their intended transaction behavior without waiving the reference-anchor rule. `_fingerprint` returns HEAD, the written index, porcelain status and a digest of every tracked file's bytes, so a no-write run can be compared exactly.

## Invariants And Boundaries

Every tree is disposable under `tmp_path`; nothing here writes into the checkout. The fingerprint covers refs, index, status and file bytes together, so a run that moves the index without a commit is still visible.

## Evidence

### Repo-Internal References


- A converted memory is identified by the `ar-memory-layout/v2` marker it holds. [1]



- Anchors are built from the file's git blob id and content identity, and the stale one carries zeros. [2]



- The no-write fingerprint covers HEAD, the index tree, porcelain status and every file's bytes. [3]
