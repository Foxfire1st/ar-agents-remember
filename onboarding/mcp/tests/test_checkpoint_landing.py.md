# mcp/tests/test_checkpoint_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkpoint_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-12T02:30+02:00 |
| lastVerifiedCommitHash | `5410fb07d0d3a73f4d81d57ed020bbfcdaaa2267` |
| lastVerifiedCommitDate | 2026-09-12T18:45:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Locks the checkpoint landing route — the way an **unfinished** atomic master lands its accumulated
line into its super branch without being closed. `worktree_integrate` proves the master is a
finished unit (task document `Completed`, one landed enclosure per canonical leaf); a paused master
has neither, so before this route existed a partial master could not land at all. The cases pin
exactly the two differences — the recorded contract state and the dropped completion assumptions —
plus the abandon guard that must keep refusing to retire a master whose line is already upstream.

The suite is deliberately self-contained: it builds its own sprint/master/leaf task tree and its own
Git repository in a temporary directory rather than importing the shared lineage fixtures.

## Code Commentary

### Logic

`_fixture(root)` (cit:([`_fixture`], mcp/tests/test_checkpoint_landing.py:133-148)) writes a sprint
commanding one `atomic` master with one `inProgress` sub-task row and **no** `task_root/enclosures`
directory at all — so the same contract is refused by the final route and accepted by the checkpoint
route, which is the property under test rather than an incidental fixture detail. `_write_task_tree`
builds the documents, `_code_repo` initializes a real repository whose default branch is `super` and
which names `refs/remotes/origin/HEAD` the way a real clone does, and `_set_master` rewrites only the
master status and its single row status.

Four unittest classes:

- `IntegrationCellRecordingTests` cit:([`IntegrationCellRecordingTests`], mcp/tests/test_checkpoint_landing.py:169-206) drives the shared writer directly.
  `test_checkpoint_records_the_state_and_leaves_cleanup_untouched` sets `cleanup="reopened"` *before*
  the call so that a route which rewrote the cell and one which left it alone cannot be confused —
  leaving `cleanup` untouched is the whole reason nothing is retired — then asserts both the returned
  and the reloaded contract read `checkpointed` with `cleanup` still `reopened`.
  `test_final_landing_still_records_completed_and_marks_cleanup_pending` is the mirror case that keeps
  the final route's behavior pinned.
- `CheckpointResultTests` cit:([`CheckpointResultTests`], mcp/tests/test_checkpoint_landing.py:207-232) binds the default worktree services for one case, because
  `_checkpoint_result` builds its payload through the ordinary status projection, and patches
  `integrate.run_automatic_cleanup` to assert it is **never called** while the payload state is
  `checkpointed` and the stored cell agrees.
- `SeriesCheckpointAuthorityTests` cit:([`SeriesCheckpointAuthorityTests`], mcp/tests/test_checkpoint_landing.py:234-270) proves the two series-authority differences:
  `test_checkpoint_refuses_a_completed_master` asserts `CloseoutQueueError` with status
  `atomic-series-checkpoint-master-complete` and that the publication callback never ran, so a
  finished integration can never be downgraded to the weaker claim;
  `test_checkpoint_publishes_for_a_master_that_is_not_completed` asserts the *final* route refuses the
  very same contract with `atomic-series-closeout-master-incomplete` and the checkpoint route
  publishes.
- `SeriesAbandonGuardTests` cit:([`SeriesAbandonGuardTests`], mcp/tests/test_checkpoint_landing.py:272-312) covers the abandon guard's three states: `checkpointed` is
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
- **The checkpoint route must not reclaim.** The cleanup patch is an assertion, not a convenience: a
  checkpoint that ran cleanup would retire the worktrees, branches and enclosure the open master
  still needs.
- **`atomic-series-checkpoint-master-complete` is the downgrade guard.** If it is ever relaxed, a
  finished integration can be recorded as merely checkpointed, which is the claim-inversion this
  route was written to avoid.
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
| The single landing writer whose two outcomes the first class pins. | `record_landed_integration`; `LandedIntegration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:37-68; mcp/src/agents_remember/worktrees/modules/landing_record.py:28-36 |
| The checkpoint result whose no-cleanup behavior the second class patches. | `_checkpoint_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:674-714 |
| The non-final series authority and its already-completed refusal. | `publish_series_checkpoint_under_authority`; `atomic-series-checkpoint-master-complete` | mcp/src/agents_remember/worktrees/series_closeout.py:72-108; mcp/src/agents_remember/worktrees/series_closeout.py:99-104 |
| The final series authority this route deliberately does not prove completion against. | `publish_series_integration_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:53-71 |
| The abandon guard whose `{"completed", "checkpointed"}` predicate the third class asserts. | `_require_series_task_terminal` | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:233-279 |
| The lane row this module must declare, since the manifest refuses an unregistered tracked module. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:24-24 |

## Cross-Repo References

These are in-process contract and authority assertions against a fixture repository created in a
temporary directory; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-12T02:30+02:00 — Created by the 260831-LOCR-L30 curator pass. Documents the four classes
  and nine cases, the fixture whose master is open *and* enclosure-less so both series routes are
  provable on one contract, why `cleanup` is pre-set before the checkpoint call, and the lane
  registration the fail-closed manifest requires. Verification metadata is pinned to the leaf base
  commit and remains closeout-owned.
