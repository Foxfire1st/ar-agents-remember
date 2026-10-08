# skills/l-01-agent-lifecycles/templates/verdict.md

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

This template defines independent reviewer evidence for leaf route review, master exit, super
exit, and monotonic loop-review deltas. A verdict recommends; the authorized gate owner decides.

## Code Commentary

### Logic

For every exact stable ID and version, the reviewer opens the canonical approved packet and cited
artifacts, checks evidence class, attempts refutation, and records `accepted` or `rejected` with an
independent rationale. Missing rationale, invalid citations, wrong-class proof, packet mismatch,
or absent developer approval forces rejection, and any rejected revision forbids an overall pass.

The verdict separately records route coverage, bound criteria catalogs, durable-evidence lifecycle
proof, and ranked findings. Delta review rechecks only previously rejected revisions and direct
regressions while retaining earlier accepted rows.

Each adjudication is now a separate immutable reviewer record bound to the exact worker attempt,
leaf manifestation, and candidate. Rejections carry one closed failure class. A reviewer may prove
direct regression, but the owning manager or flat-run architect must record the bounded
invalidation; the verdict never rewrites the worker record, requirement, or acceptance state by
itself.

The reviewer appends that record to the same single physical leaf journal as the worker attempt.
The independently authored verdict links the exact journal anchor rather than copying the record
into a second authority.

A moved unadjudicated manifestation requires a successor attempt and reviewer record. An unrelated
later candidate does not reopen an already accepted attempt.

### Conventions

- The reviewer seat must differ from the author seat.
- Findings are ranked, cited, and refute-tested.
- A block decomposes into fixable leaf-shaped work.
- Gate evidence names the exact durable verdict artifact.

### Invariants And Boundaries

- A verdict is evidence, never the gate decision.
- PASS or PASS-WITH-NOTES is invalid while any requirement is rejected.
- Worker rationale cannot be copied as reviewer reasoning without independent inspection.
- Requirement adjudication cannot replace stable-contract-or-expiry review.
- Acceptance never floats to a later candidate, and an accepted attempt stays closed without an
  authorized invalidation trigger.

### Todos

None.


## CCR-R12@v5 Handoff Boundary

This template records the exact targeted or scoped checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full quality, full tests, full memory quality, certification, and review are explicit requests rather than automatic template gates.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The verdict template now addresses the Worker (and, on a pass, the Curator) directly, distinguishes the ordinary Reviewer-recorded code round from the sealed memory lane, and keeps the gate evidence role it had; the 'Manager Fix Leaves' section names the Worker for a repair inside the leaf.

## 260928-MIK-R93 — a question for the developer goes up the chain

A request for a round beyond the ordinary three goes to the parent with `role_message` on `agents-remember-task` where one exists, or to the own chat without one; the developer's quoted words and the recorded approval are still required before any extra review.

## Evidence

### Docs References

No external Domain Documentation source governs this verdict template.

### Repo-Internal References

- Independent exact-attempt/candidate adjudication is mandatory in every variant. [1]
- Leaf review accounts for every material route and returns a recordable packet. [2]
- Delta review retains accepted rows and rechecks rejected rows plus direct regressions. [3]

### Cross-Repo References

Repository-specific criteria, tests, and evidence classes are supplied by the reviewed target
repository and its requirement packets.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.
