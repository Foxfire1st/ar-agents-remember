# mcp/src/agents_remember/memory_quality/style/citations/resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T02:22:00+02:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Resolve citation source paths against the code and memory roots, preserving ordinary filesystem lookup and an explicit Git-candidate selection.

## Code Commentary

### Logic

`Trees` carries the roots, optional managed-cache authority, and optional exact candidate tree. Ordinary lookup checks an existing code file before memory. With a candidate tree, code lookup first requires Git membership and verifies that member's current bytes; an absent member can resolve only as a file contained within the memory root. A failed candidate proof propagates instead of selecting different code bytes.

`ours` recognizes a first path component already present under either root so diagnostics can distinguish missing repository paths from external dependencies. It does not establish candidate membership. `operation_trees` binds an operation to the supplied onboarding root and revalidates managed-cache root authority.

### Conventions

An absent `candidate_tree` selects ordinary filesystem semantics. A supplied identity uses the canonical validator in `source_index_state`; `GitSourceCandidate` owns Git census and byte verification.

### Invariants And Boundaries

- Code takes precedence over a colliding memory path.
- Candidate lookup cannot admit an untracked/generated code competitor through the memory branch or a memory symlink escaping to code.
- Resolving sources does not acquire an index lease, publish memory, or grant write authority.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Root and optional candidate selection belong to the same immutable lookup value. | `Trees` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:30-78 |
| Candidate code lookup proves membership and bytes; memory lookup remains contained. | `resolve` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:48-64 |
| Existing top-level names classify unresolved repository paths without proving Git membership. | `ours` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:66-78 |
| Onboarding and managed-cache roots must match the operation's Trees. | `operation_trees` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:81-93 |

## Update History

- 2026-09-06T02:22:00+02:00 — L30 recovery source review: Documented exact Git-candidate source resolution, contained memory lookup, and managed root validation; replaced stale source ranges. Verified against prepared code commit `97e8ed2e1fae21756c3ad995c30613d4fbfcc503`; source review does not claim Gate-5 execution or recovery acceptance.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
