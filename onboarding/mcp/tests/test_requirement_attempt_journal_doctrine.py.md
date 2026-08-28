# mcp/tests/test_requirement_attempt_journal_doctrine.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_requirement_attempt_journal_doctrine.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:51+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused architecture-fitness proof that canonical lifecycle and light-task sources preserve the
M40-M45 Requirement Attempt Journal contract across workers, reviewers, managers, task workflows,
and master summaries.

## Code Commentary

### Logic

The module normalizes canonical Markdown and checks stable contractual phrases rather than full
snapshots. Its tests cover review-handoff-only immutable worker records; separate internal protocol
events with candidate/command/result/failure/repair/next-proof fields; lightweight
content-addressed expanded-evidence references; exact attempt/candidate reviewer records;
independent-regression proof plus owner-recorded bounded invalidation; the closed five failure
classes and developer-owned requirement revision; leaf-journal authority; and the rebuildable
non-gating master summary.

It also forces one physical per-leaf append-only journal: worker and reviewer records occupy the
same authoritative stream, while turn reports and verdicts link exact anchors rather than copying
records into competing authorities.
Each leaf journal records attempts for its one owned primary requirement manifestation; adjacent
dependency or preservation constraints cannot acquire closure authority through that stream.

The invalidation test also pins that an unrelated later candidate does not reopen an accepted
attempt. Internal pre-handoff candidate changes remain protocol events; a moved handed-off
candidate is adjudicated against its frozen attempt and advances only after reviewer rejection.

Projection identity remains owned by `scripts/sync-skills.py --check`. This module proves the
canonical behavior-bearing surfaces cannot silently omit the attempt contract; it does not create
a second sync mechanism or claim that a real candidate has passed review.

### Conventions

- Assert stable headings and authority phrases, not complete Markdown snapshots.
- Keep the five failure classes in one tuple so every required surface is checked consistently.
- Add a surface only when agents actually consume it as lifecycle or task doctrine.

### Invariants And Boundaries

- Semantic requirement versions and delivery attempts remain separate identities.
- Internal implementation/test/evidence events never advance formal attempt IDs.
- Attempt records remain requirement-specific and link rather than duplicate frozen expanded proof.
- A rendered worker-record scaffold is transient and must be removed after the journal append.
- Reviewer records never modify worker records or float to a later candidate.
- Accepted work reopens only through the two authorized invalidation paths.
- Master summaries are rebuildable projections and never task/lifecycle/closeout/integration/queue
  gates or authorities.
- The test is structural doctrine proof, not behavioral task-tool enforcement.

## Docs References

No external domain documentation governs this repository-owned lifecycle contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Worker roles/templates require immutable candidate-bound append before handoff. | `test_worker_appends_an_immutable_candidate_bound_attempt_before_handoff` | mcp/tests/test_requirement_attempt_journal_doctrine.py:30-66 |
| Reviewer roles/templates require separate exact-attempt adjudication. | `test_reviewer_appends_an_independent_exact_attempt_adjudication` | mcp/tests/test_requirement_attempt_journal_doctrine.py:69-93 |
| Regression reopening has independent proof plus bounded owner authority. | `test_acceptance_reopens_only_through_bounded_owner_authority` | mcp/tests/test_requirement_attempt_journal_doctrine.py:96-118 |
| Failure classification and requirement revision use closed authorities. | `test_failure_taxonomy_and_requirement_revision_authority_are_closed` | mcp/tests/test_requirement_attempt_journal_doctrine.py:121-142 |
| Leaf records remain authority while the master summary stays non-gating. | `test_leaf_journals_are_authority_and_master_summary_is_rebuildable_non_gating` | mcp/tests/test_requirement_attempt_journal_doctrine.py:145-168 |
| Internal runs remain protocol events rather than attempts. | `test_internal_protocol_runs_do_not_advance_delivery_attempts` | mcp/tests/test_requirement_attempt_journal_doctrine.py:190-211 |
| Worker records remain lightweight content-addressed views. | `test_attempt_records_are_lightweight_content_addressed_views` | mcp/tests/test_requirement_attempt_journal_doctrine.py:214-227 |
| Pre-handoff correction and handed-off rejection remain distinct formal states. | `test_attempt_boundary_distinguishes_pre_handoff_correction_from_rejected_successor` | mcp/tests/test_requirement_attempt_journal_doctrine.py:230-267 |

## Cross-Repo References

None. The test reads only canonical sources in this repository.

## Update History

- 2026-08-28T11:51+02:00 — Added structural proof that the turn-report worker-record scaffold is
  removed after append and cannot become a duplicate authority.

- 2026-08-28T11:32+02:00 — Pinned attempt authority to the leaf's one primary manifestation and
  kept adjacent requirements outside its closure stream.

- 2026-08-27T22:15+02:00 — Added structural proof that malformed pre-handoff rows consume no
  attempt ID while malformed handed-off records require reviewer rejection before successor.
- 2026-08-27T21:53+02:00 — M40@v2/M44@v2: added structural proof for review-handoff-only attempt
  advancement, separate protocol events, and lightweight content-addressed records; eight journal
  doctrine tests participate in the 16-test M38-M45 focused set.
- 2026-08-27T20:45+02:00 — Added structural forcing for the single physical leaf journal and
  link-only report/verdict references.
- 2026-08-27T19:59+02:00 — M42 clarification: added structural forcing for the accepted-attempt
  non-reopening boundary across canonical lifecycle and workflow sources; six pure tests pass.
- 2026-08-27T18:06+02:00 — M45: created focused structural proof for the complete Requirement
  Attempt Journal doctrine and non-gating authority boundary. Verification metadata remains empty
  until governed closeout stamps the PDLS commit.
