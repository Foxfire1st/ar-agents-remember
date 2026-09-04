# mcp/tests/test_task_intent_consumers_and_legacy.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_intent_consumers_and_legacy.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Consumer threading and bounded legacy task-intent cutover matrices: proves every evidence-currentness
owner (route review, door evidence, curator projection, door/operation projection, closeout start,
direct landing) rejects missing and stale task intent exactly, that legacy records decode typed
absence, and that the deterministic four-class legacy census gates decoder removal
cit:(["Consumer threading and bounded legacy task-intent cutover matrices."], mcp/tests/test_task_intent_consumers_and_legacy.py:1).

## Code Commentary

### Logic

The suite drives `require_current_task_intent` through every consumer with missing-intent sentinel
and stale-digest matrices, proves the R02 legacy decoder cannot be cut before the census reaches the
class population, and verifies that public start/landing entry points preserve typed intent refusal
cit:([`test_each_currentness_owner_rejects_missing_and_stale`,
`test_deterministic_four_class_census_controls_decoder_removal`], mcp/tests/test_task_intent_consumers_and_legacy.py:328-345; mcp/tests/test_task_intent_consumers_and_legacy.py:810-889).

Under CCR-R03@v1 the route-review and door-review provenance cases were re-driven through the new
content-addressed builders: `_route_review_author_payload` feeds `build_route_review` (which stamps
evidence digests and the record digest), and the door-review case mocks
`require_current_route_review` before asserting the intent-currentness refusal, matching the
record-digest review provenance consumed by the door
cit:([`_route_review_author_payload`, `test_door_review_provenance_reuses_route_review_intent_currentness`], mcp/tests/test_task_intent_consumers_and_legacy.py:132-157; mcp/tests/test_task_intent_consumers_and_legacy.py:347-398).

### Conventions

- Fixture payloads are authored exactly as a reviewer would author them; candidate trees, times, and
  digests are always plane-derived.
- Refusal assertions pin typed statuses; legacy sentinel classes are exercised through every
  projection boundary, never only the model.
- The suite shares leaf/master fixtures (`LEAF`, `_leaf_document`, `_closeout_record_payload`,
  `_route_review_author_payload`) with the evidence-dependency matrix.

## Invariants And Boundaries

- A legacy `missing-intent` decode can never produce a digest, currentness, reuse, or acceptance.
- Intent currentness is required by every evidence owner before publication state.
- The decoder-removal census is deterministic and refuses an absent lifecycle-owner root.
- Route-review records are built through the content-addressing path; door review provenance is the
  record digest.

## Docs References

No configured Domain Documentation applies; the matrices follow the CCR-R02@v2 and CCR-R03@v1
packets.

| Finding | Anchor | Source |
| --- | --- | --- |
| The cutover matrix is repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Intent identity and currentness owners under test. | `task_intent_identity`; `require_current_task_intent` | mcp/src/agents_remember/tasks/task_intent.py:180-216 |
| Legacy census and decoder-removal gate under test. | `task_intent_legacy_census`; `require_task_intent_decoder_removal` | mcp/src/agents_remember/worktrees/integration/closeout/task_intent_legacy_census.py:61-100 |
| R03 route-review builder consumed by the updated fixtures. | `build_route_review`; `_stamp_evidence_digests` | mcp/src/agents_remember/worktrees/route_review.py:65-122; mcp/src/agents_remember/worktrees/route_review.py:274-298 |
| R03 door-review currentness seam. | `_review_provenance`; `require_current_route_review` | mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:195-253 |
| Companion coverage for the dependency matrix. | `test_route_review_dependency_and_content_addressing_guards` | mcp/tests/test_evidence_dependencies.py:299-355 |

## CCR-R18@v1 Coherent Failed-After-Exit Fixture

260831-CCR-L18 updated the legacy worker-termination preservation fixture: because the state matrix refuses `cancelRequested` outside `termination-required`/`cancelled`, the failed-after-exit record mirrors `release_worker_after_exit` and now writes `cancelRequested: false` so it is a coherent journal revision while still preserving worker-termination evidence until exact exit.

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the coherent failed-after-exit fixture (`cancelRequested: false`) aligned to the state matrix. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): created the card covering the task-intent consumer/legacy matrix and its R03-related route-review and door-review fixture updates; the source file was modified by the R03 leaf but no prior sidecar existed.