# skills/l-01-agent-lifecycles/templates/curator-brief.md

## Intake record and direct producer inputs

- The Manager supplies the Curator's intake values; the Worker sends its frozen change set and handoff list and the Reviewer the passed freeze and code verdict directly. The template supplies values, not rules: the Curator role, curation operation and acceptance govern a disagreement. [7]

## Paired roots and memory review

The brief retains exact paired roots, producer fields and source-lineage requirements. It defers code and memory lanes to the review operation, where MEMORY review is separately sealed/counted and a pass beyond the settings limit needs architect/developer approval recorded by Manager, not a fresh CODE baseline. File-only message material, passed-candidate evidence and independent acceptance are distinct.

- The brief retains exact paired roots, producer fields and source-lineage requirements. It defers code and memory lanes to the review operation, where MEMORY review is separately sealed/counted and a pass beyond the settings limit needs architect/developer approval recorded by Manager, not a fresh CODE baseline. File-only message material, passed-candidate evidence and independent acceptance are distinct. [6]

## Message/file transport

This canonical template requires messages to be short wake-ups naming requested work or a handover and its files. Report, verdict, list and evidence contents travel through file-only `body` or existing-file `attach`, not pasted into message text. Within a shared task, files stay with its record and a leaf workspace exposes the message-folder link. Text uses the effective settings limit without a pinned number. The canonical source and the packaged copy share this contract; transport does not change their existing write/start powers, peer destinations or independent acceptance authority.

## Governing Overview

[overview](../overview.md)

## Purpose

Defines the intake values the Manager supplies to a leaf's Curator — the frozen change set, intent and current source lineage — as an intake record, not a session-start brief.

## Code Commentary

The brief feeds the read-only code worktree, writable memory worktree, enclosure contract, the frozen
pre-closeout candidate change set, task/notes/design inputs, existing intent anchors, and the
**producers' curator hand-off list** the Worker and Reviewer hand over directly. It also carries the
manager's immediately preceding `worktree_status` source-lineage projection, which must be current
across every applicable super→master→leaf code and external-memory edge.

The hand-off input names the path (or fenced-block location) of the builder's list, plus the
reviewer's own list when review was requested, and demands it be handed over **unparaphrased as
data**. The producer fields (`id`, `statement`, `kind`, `target`, `found_at`, `disposition`,
`disposition_source`, `evidence`, `authority`) arrive filled; the curator fields (`resolution`,
`validated_at`, `record_action`, `supersedes`) are `null` and are the curator's to fill. The brief requires
attaching the lists themselves as data, in the supplied handoff-list format, without paraphrasing.

It also carries the durable corpus ruling, exact primary and adjacent stable-ID + version packet
paths, and the reviewer's independent row for each revision. Every onboarding edit maps back to an
accepted revision; a missing/unapproved/version-mismatched packet or rejected/worker-blocked row is
a blocker rather than current intent.

That projection is evidence, not a caller-selected commit authority. The Manager calls `worktree_status` for the canonical leaf immediately before starting the Curator
and requires `sourceLineage.state=current`. A stale or unavailable result synchronizes/reconciles before curation;
the curator never documents stale source and never repairs code.

Routing and handover rules sit in detail files: `reference/curator/change-routing.md` for routing change-set and notes items, `reference/curator/memory-handover.md` for the memory handover to the Reviewer, and `reference/message-handover.md` for message payloads and full-store refusals; the Manager's compilation checks point to `operations/curation.md#authority-gates`, `operations/coordination.md#start-leaf-stages-and-deliver-the-first-intake` and `operations/review.md`.

## Invariants And Boundaries

- Every placeholder must be filled before the intake values are supplied.
- The brief carries no runtime address and treats its lineage snapshot as evidence, not commit-identifier authority.
- Curator writes are restricted to the leaf memory worktree; code is read-only.
- The final coherence report names the affected scoped checks and preserves any failed, blocked, or
  not-run result; it is evidence for the Git transaction, not a full-memory gate.

## CCR-R12@v5 Handoff Boundary

This template records the exact targeted or scoped checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full quality, full tests, certification and review are explicit requests rather than automatic template gates, while the normal curation pass always runs the complete `memory_quality_check`.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The worktree section requires the current pre-curator lineage projection and explains its evidence-only role. [1]

- Exact requirement packets and adjudications are mandatory task inputs. [2]

- The brief carries the producers' curator hand-off list as data, with the producer fields filled and the curator fields null. [3]

- The Manager's compilation checks require `worktree_status` with `sourceLineage.state=current` immediately before the Curator starts; a stale or unavailable lineage is synchronized and reconciled first. [4]

### Cross-Repo References

No cross-repository implementation dependency governs this template.

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority.

- The authored source owns this contract; the distribution copy is not a separate authority. [8]

- The Manager starts the Curator stage through the coordination operation after code PASS; the Worker and Reviewer hand their inputs directly. [9]
