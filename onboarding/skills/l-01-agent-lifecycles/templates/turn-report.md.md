# skills/l-01-agent-lifecycles/templates/turn-report.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/turn-report.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:51+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

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

## Docs References

No external Domain Documentation source governs this report format.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Every briefed manifestation receives an immutable candidate-bound worker record containing its complete envelope. | `## Requirement Attempt Journal Records Appended For This Handoff` | skills/l-01-agent-lifecycles/templates/turn-report.md:56-132 |
| Exact commands and outcomes have a first-class report section. | `## Checks` | skills/l-01-agent-lifecycles/templates/turn-report.md:142-147 |
| Artifact lifecycle and task continuity are recorded separately. | `## Durable-Evidence Promotion Hold Point (separate concern)`; `## Respawn State (onboard a successor from this — no transcript needed)` | skills/l-01-agent-lifecycles/templates/turn-report.md:148-179; skills/l-01-agent-lifecycles/templates/turn-report.md:180-185 |

## Cross-Repo References

The report shape is generic; each dispatched repository supplies the actual verification command
and durable evidence paths.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History

- 2026-08-28T11:51+02:00 — Made the one-primary envelope and removal of the transient worker-record
  scaffold explicit after authoritative journal append.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2/M44@v2: added separate experimental protocol events and made
  formal attempt records lightweight content-addressed views created only at review handoff.
- 2026-08-27T20:45+02:00 — Separated the link-only turn report from the single physical leaf
  journal so copied records cannot become competing authorities.
- 2026-08-27T18:06+02:00 — M40/M43: converted the worker handoff into append-only attempt records
  with exact candidate/predecessor identity, embedded M38 envelope/checks, and closed failure rows.
- 2026-08-27T14:52+02:00 — Created onboarding for per-revision acceptance, the restored Checks
  section, and the separate artifact-lifecycle hold point.
