# mcp/src/agents_remember/cli/dashboard_review_summary.py

## Governing Overview

[Owning route overview](../../../overview.md)

## Purpose

Bind native review-summary resolution and dependency observations at dashboard composition without giving serving layers selection authority.

## Code Commentary

The port asks one question by repository/master/leaf and optional comparison number. Invalid task context follows no invalid path. Initial observations include enclosure-directory selection, its recorded contract and knowledge worklist, the applicable code/memory repositories and existing or absent worktrees. A numbered request additionally observes the comparison directory even when the leaf is live. When the contract has no existing code worktree, observations also include retained comparison-generation selection.

`_resolved` reports the actual code/memory repositories, comparison record and database bytes consumed by native resolution. ContentRead tracks database contents rather than derived-index use timestamps. Missing paths remain explicit observations.

`review_intent_summary_port` binds resolve_review_comparison to the exact number and invokes summarize_review under a request-scoped capture-baseline memo. The observer receives the dependencies of that resolved comparison before counting. Recreating the stored worklist or the numbered-record population can invalidate reuse.

## Invariants And Boundaries

This composition owns dependency wiring, not intent-count semantics, path authorization or an atomic whole-workspace snapshot. The serving port cannot replace a missing recorded comparison with a live candidate.

## Evidence

- Initial observations include record-directory selection for numbered reads and preserve absence. [4]
- Resolved repositories, record and database contents are additional inputs. [5]
- One numbered/default resolver is composed with native summary and capture observation.

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/cli/dashboard_review_summary.py:84-96 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361. Retired means the anchor no longer stands, not that the cited subject was deleted.
