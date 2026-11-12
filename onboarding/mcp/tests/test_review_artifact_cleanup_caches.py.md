# mcp/tests/test_review_artifact_cleanup_caches.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Scratch caches go with the archived task; the hook's two trust statements hold.

## Code Commentary

MIK-R82 rules 3 and 6, hook side: the archive hook deletes `ar-cache-*` directories under an archived task folder and lists them with size. The module text and this leaf's decision say the hook guards against accidents rather than a second writer with the same rights, and the legacy cleanup trusts the control documents the product itself writes.

## Evidence

- Archived-task cache deletion with sizes, and the hook trust statements, are pinned. [1]
