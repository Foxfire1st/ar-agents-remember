# skills/l-01-agent-lifecycles/templates/verdict.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/verdict.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

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

## Docs References

No external Domain Documentation source governs this verdict template.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Independent exact-attempt/candidate adjudication is mandatory in every variant. | `## Mandatory Requirement Adjudication Block (repeat once per stable ID + version in every variant)` | skills/l-01-agent-lifecycles/templates/verdict.md:60-105 |
| Leaf review accounts for every material route and returns a recordable packet. | `## Leaf Route-Review Variant (every code-changing leaf)` | skills/l-01-agent-lifecycles/templates/verdict.md:106-153 |
| Delta review retains accepted rows and rechecks rejected rows plus direct regressions. | `## Loop-Review Adaptation (leaf full-loop · plan review)` | skills/l-01-agent-lifecycles/templates/verdict.md:270-282 |

## Cross-Repo References

Repository-specific criteria, tests, and evidence classes are supplied by the reviewed target
repository and its requirement packets.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T20:45+02:00 — Bound reviewer append behavior to the same single physical leaf
  journal and made the verdict a link-only consumer of that authoritative record.
- 2026-08-27T19:59+02:00 — M42 clarification: distinguished stale in-review candidates from
  unrelated post-acceptance candidates, which do not reopen accepted work.
- 2026-08-27T18:06+02:00 — M41-M43: added exact attempt/candidate reviewer records, independent
  append-only separation, the five failure classes, and owner-recorded regression invalidation.
- 2026-08-27T14:52+02:00 — Created onboarding for exact-version independent adjudication and
  monotonic delta review.
