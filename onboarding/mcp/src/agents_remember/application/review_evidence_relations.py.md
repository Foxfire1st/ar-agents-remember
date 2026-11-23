# mcp/src/agents_remember/application/review_evidence_relations.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Follows the recorded relationships of one memory file on a bound side through the owners of the edges, at the selected depth.

## Code Commentary

`read_bound_relationships` walks a family's `members`, a decision's or invariant's `links` and `supersedes`, a sidecar's `realizes` and `proves`, and a history file's rows, reporting an edge another owner records as `recorded-by` rather than as a field of the inspected file. `_Relations` resolves a target by its native identifier and refuses a filename that merely looks like the identity, so a foreign revision is never credited to the requested record; an unreadable owner file is `invalid`, not absent, and a lost tree stays `unavailable`.
The walk reads the complete bound knowledge and onboarding listing and builds an identifier-to-path index. It returns every edge in the selected walk and reports the number of paths and bytes inspected.

## Evidence

- A relationship edge is reported from the owner that records it, with its own semantics. 
- A resolved target must carry the requested native identifier; a filename alone is only a locator. 
- A memory file this build does not read is invalid rather than absent. [3]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_evidence_relations.py::read_bound_relationships - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/application/review_evidence_relations.py::_Relations - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The relationship reader indexes the complete bound listing and returns the selected walk with observed path and byte counts. \[4] [4]
