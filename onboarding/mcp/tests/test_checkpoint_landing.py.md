# mcp/tests/test_checkpoint_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkpoint_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Locks the checkpoint landing route — the way an **unfinished** atomic master lands its accumulated
line into its super branch without being closed. `worktree_integrate` proves the master is a
finished unit (task document `Completed`, one landed enclosure per canonical leaf, and a completed
closeout); a paused master has none of those, so before this route existed a partial master could not
land at all. The cases pin exactly the differences — the recorded contract state, the dropped
completion assumptions, and (since 260831-LOCR-L34) the candidate the capture proved and publication
revalidates — plus the abandon guard that must keep refusing to retire a master whose line is already
upstream.

The suite is deliberately self-contained: it builds its own sprint/master/leaf task tree and its own
Git repository in a temporary directory rather than importing the shared lineage fixtures.

## Code Commentary

### Logic

`_fixture(root)` (cit:([`_fixture`], mcp/tests/test_checkpoint_landing.py:133-147)) writes a sprint
commanding one `atomic` master with one `inProgress` sub-task row and **no** `task_root/enclosures`
directory at all — so the same contract is refused by the final route and accepted by the checkpoint
route, which is the property under test rather than an incidental fixture detail. `_write_task_tree`
builds the documents, `_code_repo` initializes a real repository whose default branch is `super` and
which names `refs/remotes/origin/HEAD` the way a real clone does, and `_set_master` rewrites only the
master status and its single row status.

Four unittest classes:

- `IntegrationCellRecordingTests` cit:([`IntegrationCellRecordingTests`], mcp/tests/test_checkpoint_landing.py:169-204) drives the shared writer directly.
  `test_checkpoint_records_the_state_and_leaves_cleanup_untouched` sets `cleanup="reopened"` *before*
  the call so that a route which rewrote the cell and one which left it alone cannot be confused —
  leaving `cleanup` untouched is the whole reason nothing is retired — then asserts both the returned
  and the reloaded contract read `checkpointed` with `cleanup` still `reopened`.
  `test_final_landing_still_records_completed_and_marks_cleanup_pending` is the mirror case that keeps
  the final route's behavior pinned.
- `CheckpointResultTests` cit:([`CheckpointResultTests`], mcp/tests/test_checkpoint_landing.py:207-238) binds the default worktree services for one case, because
  `_checkpoint_result` builds its payload through the ordinary status projection. Since
  260831-LOCR-L31 that case no longer patches anything: `integrate.run_automatic_cleanup` is gone
  (reclamation belongs to `lifecycle_finalize_task`), so the case sets `cleanup="reopened"` on the
  contract before the call and then asserts the payload's `cleanup` key is that untouched cell, that
  `"removed"` is absent from the payload, and that both the returned and the reloaded contract still
  read `reopened`. The pre-set cell is the assertion: a route that reclaimed — or merely rewrote the
  cell — stays distinguishable from one that left the enclosure alone, without needing a mock to
  prove a non-call.
- `SeriesCheckpointAuthorityTests` cit:([`SeriesCheckpointAuthorityTests`], mcp/tests/test_checkpoint_landing.py:241-305) proves the series-authority differences and the
  publication revalidation. `test_checkpoint_refuses_a_completed_master` asserts `CloseoutQueueError`
  with status `atomic-series-checkpoint-master-complete` and that the publication callback never ran,
  so a finished integration can never be downgraded to the weaker claim;
  `test_checkpoint_publishes_for_a_master_that_is_not_completed` asserts the *final* route refuses the
  very same contract with `atomic-series-closeout-master-incomplete` and the checkpoint route
  publishes; and, added by 260831-LOCR-L34,
  `test_publication_refuses_a_candidate_that_moved_after_its_capture` passes a stale
  `SeriesCheckpointRefs` and asserts `atomic-series-checkpoint-candidate-moved` with the callback
  never run — the preflight captures the live refs once and publication re-reads them, so the route
  cannot land a pair the preview never showed. Every case in this class now supplies the candidate
  honestly through `capture_series_checkpoint_refs(contract)`, so the refusal under test is the
  reason the call fails rather than a missing required argument.
- `SeriesAbandonGuardTests` cit:([`SeriesAbandonGuardTests`], mcp/tests/test_checkpoint_landing.py:308-347) covers the abandon guard's three states: `checkpointed` is
  refused, `completed` is still refused, and `not-started` still passes the whole terminal guard
  (branch spelling included), because nothing was taken.

### Conventions

The suite is a unittest class, matching the surrounding `mcp/tests` convention. It is registered in
the `unit-regression` lane of `mcp/tests/test-evidence-lanes.toml` (row 24), which the manifest
requires of every tracked `test_*.py` module; that manifest is fail-closed, so the row is not
optional metadata.

`_git` passes the commit identity via `-c` flags rather than relying on repository or global Git
configuration, so the fixture works on a machine with no configured user.

`CheckpointResultTests` is the only case that needs bound services, and it binds and releases them in
`setUp`/`tearDown` rather than marking the module integration; the other three classes exercise the
contract write and the authority guards through pure fixtures.

### Invariants And Boundaries

- **The two landing states must stay distinguishable.** Any change that lets a checkpoint write
  `cleanup="pending"`, or lets the final route leave `cleanup` alone, breaks the meaning of both
  cells; the first case's pre-set `cleanup="reopened"` is what makes that visible.
- **The checkpoint route must not reclaim, and since 260831-LOCR-L31 neither does any landing route.**
  The pre-set `cleanup="reopened"` cell is the assertion, not a convenience: a checkpoint that
  reclaimed would retire the worktrees, branches and enclosure the open master still needs, and one
  that merely rewrote the cell would be indistinguishable from the final route. The mock that used to
  prove the old `run_automatic_cleanup` was never called is no longer needed, because there is no
  helper left to call — which is why the cell-level assertion is now the whole protection.
- **`atomic-series-checkpoint-master-complete` is the downgrade guard.** If it is ever relaxed, a
  finished integration can be recorded as merely checkpointed, which is the claim-inversion this
  route was written to avoid.
- **`expected` is required, and a stale one must refuse (260831-LOCR-L34).** Every call site supplies
  the candidate through `capture_series_checkpoint_refs`, and the added case proves publication
  re-reads the live refs: naming a candidate the live tips no longer match must raise
  `atomic-series-checkpoint-candidate-moved` before the callback runs. A case that passed `expected`
  by omission would be testing a fail-open hole rather than the route.
- **Assert the stored contract, not only the payload.** A payload state can be right while the write
  was skipped or duplicated; the cases reload the contract to check the durable result.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo, and these assertions
concern this repository's own contract write and branch authority, so the retained source is the
direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The single landing writer whose two outcomes the first class pins. | `record_landed_integration`; `LandedIntegration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:27-34; mcp/src/agents_remember/worktrees/modules/landing_record.py:37-68 |
| The checkpoint result whose no-reclamation behavior the second class pins through the pre-set `cleanup` cell. | `_checkpoint_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:923-962 |
| The non-final series authority and its already-completed refusal. | `publish_series_checkpoint_under_authority`; `atomic-series-checkpoint-master-complete` | mcp/src/agents_remember/worktrees/series_closeout.py:166-197; mcp/src/agents_remember/worktrees/series_closeout.py:139-160 |
| The final series authority this route deliberately does not prove completion against. | `publish_series_integration_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:79-95 |
| The L34 case: publication re-reads the live refs and refuses a candidate that moved after its capture, before the callback runs. | "class SeriesCheckpointRefs:" | mcp/tests/test_checkpoint_landing.py:290-306; mcp/src/agents_remember/worktrees/series_closeout.py:94-105 |
| The abandon guard whose `{"completed", "checkpointed"}` predicate the third class asserts. | `_require_series_task_terminal` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:232-276 |
| The lane row this module must declare, since the manifest refuses an unregistered tracked module. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:24-24 |

## Cross-Repo References

These are in-process contract and authority assertions against a fixture repository created in a
temporary directory; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

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
