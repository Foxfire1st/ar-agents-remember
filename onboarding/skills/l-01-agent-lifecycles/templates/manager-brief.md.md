# skills/l-01-agent-lifecycles/templates/manager-brief.md

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

This is the orchestrator-compiled, self-contained session start for a manager that owns one
master. It transfers task topology, source-edge truth, targeted/scoped evidence, closeout scheduling, and
the exact approved requirement revisions the manager must dispatch and close.

## Code Commentary

### Logic

Before each worker dispatch, the manager receives one stable ID, exact version, matching approved
canonical packet, corpus ruling, and expected evidence classes for every applicable requirement.
The manager requires one worker acceptance block and one independent reviewer adjudication per
revision. It separately preserves the durable-evidence promotion hold point, optional requested
review, curator handoff, and repository-defined transaction boundaries.

The brief also requires the manager to compile the next review-handoff attempt identity without
advancing it during dispatch or internal implementation/test/evidence reruns, validate the
lightweight candidate-bound worker record and content-addressed expanded-evidence anchor, and
dispatch that exact candidate to independent review. The reviewer proves any direct regression;
the owning manager records bounded invalidation. The rebuildable master summary links authoritative
leaf journals, excludes separate protocol events from attempt counts, and never gates task,
lifecycle, closeout, integration, or queue work.

A reviewer-rejected manifestation creates a successor at the next handoff; an unrelated later
candidate does not reopen accepted work.

The brief also keeps task authoring independent of disposable closeout projections: valid task
mutations proceed, projection effects are reported, and affected door generations are re-proved
rather than treating queue state as a task lock.

### Conventions

- The orchestrator fills every placeholder before dispatch.
- Canonical task documents and plane-owned contracts carry branch and source identity.
- Stable requirement IDs and versions are copied exactly; master prose never replaces packets.
- Worker, reviewer, and curator seats remain distinct; the reviewer is also distinct from the seat
  that authored the plan, preventing plan-author self-adjudication.

### Invariants And Boundaries

- An unstable, unapproved, missing, duplicated, or version-mismatched requirement makes dispatch
  invalid.
- Any rejected requirement blocks the overall reviewer recommendation.
- Requirement acceptance cannot substitute for stable-contract-or-expiry evidence, or vice versa.
- A manager reports readiness but does not rank the portfolio or decide developer-owned gates.
- Requirement problems route to architect/developer revision authority; worker/reviewer records
  cannot change semantic versions.

### Todos

None.


## CCR-R12@v5 Handoff Boundary

This template records the exact targeted or scoped checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full quality, full tests, full memory quality, certification, and review are explicit requests rather than automatic template gates.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The manager brief no longer describes the manager -> builder -> reviewer -> curator relay chain: the leaf's Worker, Reviewer and Curator hand freezes, findings, verdicts and memory changes directly to each other, and the Manager starts the set and reads state from reports.

## 260928-MIK-R93 — a question for the developer goes up the chain

The master-exit round-limit sentence now requests authorization through the parent with `role_message` on `agents-remember-task` where one exists, or in the own chat without one, and still records the developer's quoted answer before acting.

## Evidence

### Docs References

No external Domain Documentation source governs this dispatch template.

### Repo-Internal References

- The source edge and every requirement revision are compiled before worker dispatch. [1]
- Master exit carries the full revision set and independent adjudications. [2]
- Attempt dispatch, bounded invalidation, and the non-gating master summary are explicit manager obligations. [3]

### Cross-Repo References

No sibling-repository contract is defined here; repository-specific executors are resolved from
the target repository's system guidance.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## MIK-R95 Shared Start Preparation

This template now sends each leaf role through `role_start` as the operation that prepares its admitted task environment; no separate `worktree_status`/`worktree_start` call precedes it. A start that reports moved source names the contract-addressed `worktree_sync` recovery to follow instead, and the brief still forbids inferring a source branch from the checkout or carrying a prior super tip forward. The bundled runtime copy is byte-identical to this source template.
