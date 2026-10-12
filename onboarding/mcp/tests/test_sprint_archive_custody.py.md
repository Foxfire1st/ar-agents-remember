# mcp/tests/test_sprint_archive_custody.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Sprint-archive recovery, legacy-row, and preview-bound regressions.

## Code Commentary

MIK-R82 rule 1: each test mirrors a sealed review probe the leaf repaired — recorded retries refuse missing custody and changed archived bytes, resumed failures restore all and remove the record, open legacy seat rows refuse, and the fifteen-master preview stays bounded and exact.

The fifteen-master and already-archived previews deliver the bounded overflow outcome. The
fixture installs the same call context the server dispatch supplies so a full `log` result
exists; it checks exact move order, all master identities, cleanup counts, bounded change/write
lists and repeat no-change facts there. The preview snapshot remains unchanged, and actual
archive still proves every master file arrived. A direct call without the dispatch context
cannot stand in for a file-backed public answer.

## Evidence


- Archive custody, legacy admission and logged whole-preview bounds are pinned. [1]
