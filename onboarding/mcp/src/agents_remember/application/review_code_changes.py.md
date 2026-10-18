# mcp/src/agents_remember/application/review_code_changes.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Compute the whole leaf’s implementation facts from the existing family fact owner, without loading any roster, selected-subject review or excerpt.

## Code Commentary

`tree_request` serializes the already admitted comparison record, live flag and both wire/index sides for the child; `trees_from_request` reconstructs those same operands, not a new candidate resolution. `code_changes` ignores a held classification whose pairing is not bound to these trees. With an admitted classifier it reuses its CodeTrees, opens the lane once and calls `implementation_facts`. Missing memory indexes, any unread onboarding sidecar, unavailable code inventory, LaneReadError or APSW failure produce `unavailable` with a bounded reason; they never become no-code-change. Successful facts come from `_implementation`, not a second definition.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- Only the existing comparison record and side/index operands cross the child pipe. [1]
- The child reconstructs the admitted operands without resolving another candidate. [2]
- Whole-leaf facts reuse exact run classification and explicitly name unreadable sides. [3]
