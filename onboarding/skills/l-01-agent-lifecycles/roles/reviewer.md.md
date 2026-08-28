# skills/l-01-agent-lifecycles/roles/reviewer.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/reviewer.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

Governing overview: skills/l-01-agent-lifecycles/roles/overview.md

## Purpose

This is the canonical independent-review lifecycle. It inspects the exact candidate and adjudicates
each stable requirement ID from the same applicable set dispatched to the worker.

## Code Commentary

### Logic

The reviewer does not accept a worker assertion at face value. For every stable ID it independently
opens the implementation/deliverable and verification citations, checks the evidence class, and
records `accepted` or `rejected` with its own rationale. Missing rationale, invalid citations,
wrong-class evidence, or an absent durable developer ruling for blocked/changed delivery forces
rejection. One rejected ID prevents an overall pass; already accepted IDs stay accepted through a
delta round unless the repair directly regresses them.

The first citation check is the version-addressed canonical packet itself: its ID/version must
match, its state must be approved, and it must carry the durable corpus ruling. A task summary or
worker paraphrase cannot substitute for that approved revision.

Adjudication now binds the exact immutable worker attempt, leaf manifestation, and candidate. The
reviewer appends its own record without editing the worker record and classifies each rejection
with one of five exact classes. It may prove a direct regression, but only the owning manager (or
flat-run architect) records bounded invalidation; the finding alone cannot reopen accepted work or
extend scope.

The worker record is lightweight: the reviewer verifies its requirement-specific status,
rationales, citations, findings/failure class, and the digest plus exact anchor of the immutable
expanded evidence. Internal implementation/test/evidence protocol events may support a claim but
are never adjudicated as worker attempts and never inflate attempt or rejection counts.

The append target is the same single physical leaf journal that contains the worker attempt. The
reviewer's separately authored verdict links that journal anchor instead of duplicating the
adjudication as another authority.

If the manifestation candidate moves before adjudication, the stale attempt is rejected and a
successor is reviewed. An unrelated later candidate does not reopen an accepted attempt.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
outputs. Requirement adjudication and the durable-evidence stable-contract-or-expiry hold point
are independent mandatory concerns. Accepted attempts remain closed without one of the two
authorized invalidation paths.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker envelope, reviewer verdict template, manager exact-set dispatch, and governing route overview.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every exact requirement attempt and candidate receives a separate independent accepted/rejected record. | `## Per-Requirement Independent Attempt Adjudication` | skills/l-01-agent-lifecycles/roles/reviewer.md:101-160 |
| The verdict template structurally repeats one adjudication block per stable ID. | "## Mandatory Requirement Adjudication Block" | skills/l-01-agent-lifecycles/templates/verdict.md:60-60 |

## Cross-Repo References

No meaningful cross-repo references.

## 260815-DAG-L2 Candidate And Repair Scope

Master-exit review is nature-aware. Organizational review covers the exact proposed final super
candidate—prior landed contributions plus the proposed final leaf—before its one full gate and ref
movement; atomic review covers the isolated branch before its single landing. At super exit, every
blocking finding decomposes into an owning/reopened leaf or a new scoped fix leaf. The reviewer may
not route implementation onto the super worktree.

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

- 2026-08-27T21:53+02:00 — M40@v2/M44@v2: reviewers now validate lightweight
  content-addressed worker records and keep internal protocol events outside formal adjudication.
- 2026-08-27T20:45+02:00 — Clarified same-journal append-only adjudication and link-only verdict
  consumption.
- 2026-08-27T19:59+02:00 — M42 clarification: separated stale in-review candidate replacement from
  unrelated post-acceptance movement and preserved the two legal invalidation triggers.
- 2026-08-27T18:06+02:00 — M41-M43: bound independent adjudication to an exact immutable attempt
  and candidate, added closed failure classes, and separated regression proof from owner-recorded
  bounded invalidation.
- 2026-08-27T14:04+02:00 — Tightened M39 adjudication to inspect the approved,
  version-addressed packet and its packet-local durable corpus ruling before evidence review.
- 2026-08-27T13:32+02:00 — M39@v1: independent adjudication now verifies the canonical packet and
  rejects missing, stale, or mismatched requirement revisions. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: replaced aggregate review description with independent per-ID
  adjudication, forcing rejection rules, delta preservation, and the separate durable-evidence
  hold point. Verification metadata stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: aligned master-exit scope with the pre-landing candidate
  and made integration-branch repair routing fail closed to leaf-shaped work. Verification remains
  closeout-owned.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
