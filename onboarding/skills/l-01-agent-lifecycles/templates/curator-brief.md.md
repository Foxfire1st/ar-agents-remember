# skills/l-01-agent-lifecycles/templates/curator-brief.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/curator-brief.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T14:18+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
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

It also carries the durable corpus ruling, exact primary and adjacent stable-ID + version packet
paths, and the reviewer's independent row for each revision. Every onboarding edit maps back to an
accepted revision; a missing/unapproved/version-mismatched packet or rejected/worker-blocked row is
a blocker rather than current intent.

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
| Exact requirement packets and adjudications are mandatory task inputs. | "## Task inputs" | skills/l-01-agent-lifecycles/templates/curator-brief.md:44-54 |
| Manager compiler notes require status before dispatch and the transaction repeats the proof before process creation. | "Immediately before compiling this brief" | skills/l-01-agent-lifecycles/templates/curator-brief.md:178-178 |
| Manager doctrine owns the ordered pre-curator gate, exact packet/adjudication inputs, and complete brief. | "Curator coherence pass — mandatory, not skippable." | skills/l-01-agent-lifecycles/roles/manager.md:207-207 |

## 260821-DAGQC-L2 Briefed Quality Grammar

The brief's self-check examples now use `memory_quality_check(request={...})` with an explicit
mode. This prevents a fresh curator from reconstructing the retired flat wait/run-id grammar and
keeps sync/start/poll fields mutually exclusive.

## Cross-Repo References

No cross-repository implementation dependency governs this template.

## Update History

- 2026-08-28T14:18+02:00 — Reconciled curator-brief citations against the committed PDLS
  candidate; the post-review onboarding boundary remains unchanged.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T16:27+02:00 — Added exact approved requirement packets and reviewer adjudications to
  curator intake/output, closing the bare-ID briefing gap. Verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: aligned the curator brief with the canonical discriminated quality request. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-13T08:47+02:00 — Created for the L23 pre-curator source-lineage gate and brief-carried current projection. Verification metadata remains closeout-owned.
