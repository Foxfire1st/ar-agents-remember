# skills/l-01-agent-lifecycles/templates/curator-brief.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/curator-brief.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T08:47+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[lifecycle skill overview](../overview.md)

## Purpose

Defines the complete manager-compiled session start for a fresh per-leaf curator.

## Code Commentary

The brief feeds the read-only code worktree, writable memory worktree, enclosure contract, landed
change set, task/notes/design inputs, and existing intent anchors. It now also carries the
manager's immediately preceding `worktree_status` source-lineage projection, which must be current
across every applicable super→master→leaf code and external-memory edge.

That projection is evidence, not a caller-selected commit authority. Structural `dispatch_agent`
re-proves lineage before creating the hosted curator, closing the race between the manager's status
read and process creation. A stale or unavailable result synchronizes/reconciles before curation;
the curator never documents stale source and never repairs code.

## Invariants And Boundaries

- Every placeholder must be filled before dispatch.
- The brief carries no runtime address and never substitutes its lineage snapshot for plane truth.
- Curator writes are restricted to the leaf memory worktree; code is read-only.
- The final coherence report follows an empty curator-actionable checklist, not a partial pass.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The worktree section requires the current pre-curator lineage projection and explains its evidence-only role. | "Pre-curator lineage:" | skills/l-01-agent-lifecycles/templates/curator-brief.md:32-32 |
| Manager compiler notes require status before dispatch and the transaction repeats the proof before process creation. | "Immediately before compiling this brief" | skills/l-01-agent-lifecycles/templates/curator-brief.md:154-154 |
| Manager doctrine owns the ordered pre-curator gate and complete brief. | "Curator coherence pass — mandatory, not skippable." | skills/l-01-agent-lifecycles/roles/manager.md:137-161 |

## Cross-Repo References

No cross-repository implementation dependency governs this template.

## Update History

- 2026-08-13T08:47+02:00 — Created for the L23 pre-curator source-lineage gate and brief-carried current projection. Verification metadata remains closeout-owned.
