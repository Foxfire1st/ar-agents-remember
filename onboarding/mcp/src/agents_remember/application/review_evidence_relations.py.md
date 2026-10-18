# mcp/src/agents_remember/application/review_evidence_relations.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Follows the recorded relationships of one memory file at a bound side, through the owner that actually holds each edge, within declared depth, record and byte bounds.

## Code Commentary

`read_bound_relationships` walks a family's `members`, a decision's or invariant's `links` and `supersedes`, a sidecar's `realizes` and `proves`, and a history file's rows, reporting an edge another owner records as `recorded-by` rather than as a field of the inspected file. `_Relations` resolves a target by its native identifier and refuses a filename that merely looks like the identity, so a foreign revision is never credited to the requested record; an unreadable owner file is `invalid`, not absent, and a lost tree stays `unavailable`.
`_stream_names` stops the listing child at the name or byte budget, which keeps `ls-tree` bounded on a large memory tree; a depth or record bound beyond the declaration is refused rather than truncated silently.

## Evidence

- A relationship edge is reported from the owner that records it, with its own semantics. [1]
- A resolved target must carry the requested native identifier; a filename alone is only a locator. [2]
- A memory file this build does not read is invalid rather than absent. [3]
