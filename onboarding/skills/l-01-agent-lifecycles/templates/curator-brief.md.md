# skills/l-01-agent-lifecycles/templates/curator-brief.md

## Governing Overview

[lifecycle skill overview](../overview.md)

## Purpose

Defines the complete manager-compiled session start for a fresh per-leaf curator.

## Code Commentary

The brief feeds the read-only code worktree, writable memory worktree, enclosure contract, landed
change set, task/notes/design inputs, existing intent anchors, and now the **producers' curator
hand-off list**. It now also carries the
manager's immediately preceding `worktree_status` source-lineage projection, which must be current
across every applicable super→master→leaf code and external-memory edge.

The hand-off input names the path (or fenced-block location) of the builder's list, plus the
reviewer's own list when review was requested, and demands it be handed over **unparaphrased as
data**. The producer fields (`id`, `statement`, `kind`, `target`, `found_at`, `disposition`,
`disposition_source`, `evidence`, `authority`) arrive filled; the curator fields (`resolution`,
`validated_at`, `record_action`, `supersedes`) are `null` and are the curator's to fill. If the list
and a report prose summary disagree, the list governs — the brief requires attaching the list
itself, never a re-telling of it.

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
- The final coherence report names the affected scoped checks and preserves any failed, blocked, or
  not-run result; it is evidence for the Git transaction, not a full-memory gate.


## CCR-R12@v5 Handoff Boundary

This template records the exact targeted or scoped checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full quality, full tests, full memory quality, certification, and review are explicit requests rather than automatic template gates.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The worktree section requires the current pre-curator lineage projection and explains its evidence-only role. [1]
- Exact requirement packets and adjudications are mandatory task inputs. [2]
- The brief carries the producers' curator hand-off list as data, with the producer fields filled and the curator fields null. [3]
- Manager compiler notes require status before dispatch and the transaction repeats the proof before process creation. [4]
- Manager doctrine owns the ordered pre-curator gate, exact packet/adjudication inputs, and complete brief. [5]

### Cross-Repo References

No cross-repository implementation dependency governs this template.

## 260821-DAGQC-L2 Briefed Quality Grammar

The brief's self-check examples now use `memory_quality_check(request={...})` with an explicit
mode. This prevents a fresh curator from reconstructing the retired flat wait/run-id grammar and
keeps sync/start/poll fields mutually exclusive.
