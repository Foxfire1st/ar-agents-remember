# skills/l-01-agent-lifecycles/templates/worker-brief.md

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

This template is the complete session-start packet for one worker on one canonical leaf. It binds
the worker to named worktrees, one implementation scope, exact approved requirement revisions,
repository-defined checks, and one durable turn report.

## Code Commentary

### Logic

The template's own boundary is now stated in the file: it **feeds inputs, it does not author
rules**. Where the packet states a rule, that rule's single home is `../roles/worker.md` (the seat's
own duties), `../operations/implementation.md` and `../operations/closeout.md` (the build procedure
and the targeted-check contract), or `../core/acceptance.md` (the acceptance envelope, attempt
lineage, and completion truth); the rows carry this leaf's *values*, and those files win on
disagreement.

The spawning seat lists every applicable stable ID and version with its immutable packet, corpus
approval, evidence classes, and any already-approved changed delivery. The worker opens those
packets before editing and records a separate acceptance envelope for each revision. The envelope
contains delivery and verification rationales, inspectable citations, the failure each proof would
catch, exact command/results, and approval details for blocked or changed delivery.

The brief also compiles the leaf manifestation, one physical append-only journal path, next
review-handoff attempt ID, predecessor and carried findings, and candidate identity class. Dispatch
and internal implementation/test/evidence reruns do not advance that ID; those runs remain separate
protocol events. Before review handoff, the worker appends one lightweight immutable attempt with
requirement-specific facts and a content-addressed expanded-evidence anchor. A reviewer-rejected
delivery creates a successor at its next handoff. An unrelated later candidate does not reopen
accepted work. Blocked findings use the closed failure taxonomy and requirement problems route
upward for developer-approved revision.
The independently authored reviewer appends a separate adjudication record to that same journal;
the worker turn report links its exact attempt anchors rather than becoming a competing authority.

The brief gives the curator changed paths, observations, and the worker's own **curator hand-off
list** — every requirement-shaped item of this leaf in the shape
`skills/l-01-agent-lifecycles/templates/curator-handoff-list.md`, one entry per item with its
`statement`, `kind`, `target`, `found_at`, `disposition` and `evidence`, while `resolution`,
`validated_at`, `record_action` and `supersedes` stay `null` for the curator to fill. Each entry
names where the thing lives (path plus the construct inside it, from one resolution act) and keeps
the worker's own wording; `target: []` stands where a ruling applies nowhere. The handoff the brief
promises closeout is now the curator's **complete** onboarding/check handoff, not a scoped subset.
None of this grants the worker onboarding,
commit, lifecycle, gate, or task-document mutation authority.

### Conventions

- Compile a fresh brief per leaf and fill every placeholder.
- Use `NONE (native reads only)` when retrieval providers are unavailable.
- Copy the target repository's actual acceptance command; never invent a host fallback.
- Full code-quality and full-test operations require an explicit developer request; **curation does
  not** — the curator always runs the memory-quality operation complete, and closeout and
  integration carry that result as a prerequisite.
- Write the turn report as the worker's last act.

### Invariants And Boundaries

- One worker brief targets one leaf and one primary implementation slice.
- The template feeds inputs: any rule it states has its single home in `../roles/worker.md`,
  `../operations/implementation.md`, `../operations/closeout.md`, or `../core/acceptance.md`, and
  those files win on disagreement.
- “Requirements addressed” is never a substitute for one block per exact ID and version.
- The Checks section and the durable-evidence hold point are both explicit and separate from the
  acceptance envelope.
- The worker never commits, closes out, integrates, or writes accepted onboarding.
- The brief never reuses an attempt ID or authorizes an in-place edit of attempt history.

### Todos

None.


## CCR-R12@v5 Handoff Boundary

This template records the exact targeted checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full code quality and full tests are explicit developer requests rather than automatic template gates, while **curation is the exception** — the curator always runs the full memory-quality operation as part of curation, and closeout and integration carry that result as a prerequisite.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The worker brief now routes the frozen candidate to the Reviewer and the structured hand-off list to the Curator, and its repair section names the Worker for a repair inside the leaf instead of the Manager.

## Evidence

### Docs References

No external Domain Documentation source governs this worker template.

### Repo-Internal References

- The brief binds the exact owned requirement revision and evidence classes. [1]
- The same block compiles leaf manifestation, attempt/predecessor lineage, and candidate identity before handoff. [2]
- Repository-defined checks and artifact lifecycle remain separate obligations. [3]
- The final report requires envelopes, checks, curator inputs, and continuity state. [4]
- The template declares itself an input-feeder whose stated rules live in the seat's own files. [5]
- The brief carries the worker's curator hand-off list, producer fields filled and curator fields null. [6]
- Curation is the standing exception: the curator always runs it complete, and closeout and integration carry the result. [7]

### Cross-Repo References

The concrete worktree paths, tool paths, and verification command come from the dispatched target
repository rather than from this generic template.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.
