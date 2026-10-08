# skills/l-01-agent-lifecycles/templates/turn-report.md

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

This is the mandatory durable worker handoff. It lets a fresh successor, curator, manager, and
independent reviewer recover the leaf from recorded state without relying on the transcript.

## Code Commentary

### Logic

The report records completed work, one acceptance envelope for the leaf-owned primary revision,
separate preservation checks for adjacent requirements, an explicit command/result table, the
separately governed durable-evidence promotion decision, issues and remaining work, curator inputs,
retrieval evidence, escalations, and respawn state. The primary acceptance block ties a delivery
claim to concrete artifacts and a verification claim to evidence that names the behavior
demonstrated and the regression caught.

The report and journal are distinct. The single physical leaf Requirement Attempt Journal contains
the immutable worker and reviewer record stream; the turn report links the exact worker attempts
appended only at review handoff and does not copy them into a second authority. Each worker record
is a lightweight requirement-specific view binding revision, manifestation, predecessor/findings,
exact candidate, status/rationales/citations/failure class, and a content-addressed frozen expanded-
evidence anchor. The complete acceptance corpus and command body live once in that artifact.
Internal implementation/test/evidence reruns use the separate protocol-event table and never
consume attempt IDs. Prior records are immutable; reviewer rejection advances through a successor
at the next handoff.
The rendered worker-record block is transient authoring input: after append it is removed from the
completed turn report and replaced by the exact authoritative journal anchor.

### Conventions

- Store the report under the series `notes/reports/` directory.
- Repeat the acceptance block without aggregating or sampling revisions.
- Use code path plus symbol for code and path plus section/anchor for non-code deliverables.
- Record a not-run reason when no check ran instead of omitting the Checks section.

### Invariants And Boundaries

- Only `satisfied`, `blocked`, or `approved-change` are valid worker statuses per requirement.
- A blocked or changed delivery cannot pass without durable developer approval.
- Requirement proof and artifact-lifecycle proof remain different contracts.
- The report records facts and continuity state; it does not decide the review gate.
- Branch names or “latest” are not candidate identities, and the worker record cannot accept itself.

### Todos

None.


## CCR-R12@v5 Handoff Boundary

This template records the exact targeted or scoped checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full quality, full tests, full memory quality, certification, and review are explicit requests rather than automatic template gates.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The turn report now names the leaf seat its content is handed to (the Reviewer's freeze, the Curator's list) instead of the parent Manager, and a report still does not replace the hand-over.

## Evidence

### Docs References

No external Domain Documentation source governs this report format.

### Repo-Internal References

- Every briefed manifestation receives an immutable candidate-bound worker record containing its complete envelope. [1]
- Exact commands and outcomes have a first-class report section. [2]
- Artifact lifecycle and task continuity are recorded separately. [3]

### Cross-Repo References

The report shape is generic; each dispatched repository supplies the actual verification command
and durable evidence paths.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.
