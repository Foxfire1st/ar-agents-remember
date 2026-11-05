# scripts/agent_evals/package_budget.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Builds exact disk evidence and binds the inline judge request to its manifest and access grant.

## Code Commentary

### Invariants And Boundaries

Actual UTF-8 bytes and the Codex character cap are checked before judging. Loading revalidates paths, files and package identity rather than accepting an older schema silently.

## Evidence

- The source defines this file's responsibility and the boundaries described here.

Old citation custody (Git blobs): scripts/agent_evals/package_budget.py @ 96a6792a9fdbc4a87013171f686becf45a849e2a.

- The final judge request is measured against UTF-8 byte limits and the applicable harness character limit. Disk loading verifies roots, paths, file content, manifest, inline digest, access grant and package identity. The grading reference and policy trace use the fixed, hash-bound g1-20261030 epoch, independently of current instruction text. 

- The final judge request is measured against UTF-8 byte limits and the applicable harness character limit. Disk loading verifies roots, paths, file content, manifest, inline digest, access grant and package identity. The grading reference and policy trace use the fixed, hash-bound g1-20261030 epoch, independently of current instruction text. [1]
