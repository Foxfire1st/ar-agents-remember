# mcp/tests/test_checkpoint_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkpoint_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Pin checkpoint/final landing cell differences, explicit candidate revalidation, and terminal abandon guards for an unfinished atomic master.

## Code Commentary

### Logic

The self-contained fixture builds a sprint, one atomic master, an unfinished leaf task, and a real code repository. Memory is disabled, so the legitimate memory output is empty and no ledger placeholder is supplied.

IntegrationCellRecordingTests contrasts checkpointed with completed and presets cleanup=reopened so an unintended rewrite is observable. CheckpointResultTests verifies the same no-reclamation result through status projection with scoped service binding. SeriesCheckpointAuthorityTests proves a completed master cannot use the weaker route, an unfinished master can publish through checkpoint authority while final authority refuses it, and a stale captured candidate prevents the callback. SeriesAbandonGuardTests preserves refusal for checkpointed/completed masters and permits the never-integrated terminal case.

### Conventions

The nine definitions use constructed contract states where state writing is the subject and real repository refs where authority is tested. Git identity is supplied locally. Assertions reload the contract instead of trusting only a correct-looking payload.

### Invariants And Boundaries

- Checkpoint leaves cleanup unchanged; final landing marks cleanup pending.
- A checkpoint cannot downgrade a completed master.
- Expected candidate data remains required and is revalidated before publication.
- Already-landed masters cannot be abandoned as if nothing had been published.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Checkpoint versus final durable integration cells. | `IntegrationCellRecordingTests` | mcp/tests/test_checkpoint_landing.py:169-204 |
| The checkpoint result retains the pre-existing cleanup state. | `test_checkpoint_result_publishes_without_running_cleanup` | mcp/tests/test_checkpoint_landing.py:217-238 |
| Completion and stale candidate publication refusals. | `test_publication_refuses_a_candidate_that_moved_after_its_capture` | mcp/tests/test_checkpoint_landing.py:290-305 |
| The landed-master abandon guard remains enforced. | n/a | [mcp/tests/test_checkpoint_landing.py](mcp/tests/test_checkpoint_landing.py) |
| Production checkpoint capture and publication authority. | `publish_series_checkpoint_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:147-178 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Removed the dummy ledger member from the checkpoint result input while retaining all nine lifecycle-cell, candidate, completion, and abandon-guard scenarios. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 9 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:10+00:00 — 260831-LOCR-L34: recorded the new third case in
  `SeriesCheckpointAuthorityTests`, `test_publication_refuses_a_candidate_that_moved_after_its_capture`
  (a stale `SeriesCheckpointRefs` must raise `atomic-series-checkpoint-candidate-moved` with the
  callback never run), and that every case in that class now supplies `expected` honestly through
  `capture_series_checkpoint_refs` so the refusal under test — not a missing argument — is why the
  call fails. Added the matching invariant, corrected the purpose from "two differences" to the
  closeout-free/series-authority/candidate-revalidation set, and re-derived every class range and the
  `series_closeout.py` reference ranges. Verification metadata remains closeout-owned; no acceptance
  claim.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `_fixture` repointed to mcp/tests/test_checkpoint_landing.py:131-145. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `IntegrationCellRecordingTests` repointed to mcp/tests/test_checkpoint_landing.py:167-202. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `CheckpointResultTests` repointed to mcp/tests/test_checkpoint_landing.py:205-236. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31: `CheckpointResultTests` no longer patches
  `integrate.run_automatic_cleanup` (that module and helper were deleted; reclamation belongs to
  `lifecycle_finalize_task`). Recorded what the case asserts instead — `cleanup` pre-set to
  `reopened`, the payload's `cleanup` key is that untouched cell, `"removed"` is absent from the
  payload, and both the returned and reloaded contract still read `reopened` — and why the cell-level
  assertion is now the whole protection rather than a convenience alongside a mock non-call. Also
  re-pointed the `_checkpoint_result` reference range (674-714 → 678-717) after this leaf's line
  movement. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T02:30+02:00 — Created by the 260831-LOCR-L30 curator pass. Documents the four classes
  and nine cases, the fixture whose master is open *and* enclosure-less so both series routes are
  provable on one contract, why `cleanup` is pre-set before the checkpoint call, and the lane
  registration the fail-closed manifest requires. Verification metadata is pinned to the leaf base
  commit and remains closeout-owned.
