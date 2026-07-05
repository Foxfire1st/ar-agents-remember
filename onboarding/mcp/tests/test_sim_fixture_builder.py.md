# mcp/tests/test_sim_fixture_builder.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_sim_fixture_builder.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T10:30+02:00                     |
| lastVerifiedCommitHash | `4cdb1ef68e2c5f661ea11e12d46a68441ef18088` |
| lastVerifiedCommitDate | 2026-07-06T01:49:54+02:00|

## Purpose

Regression suite for the L11 review's L11R-1 finding: the rich sim fixture builder
(`mcp/tests/fixtures/build_rich_sim.py`) recorded worktree paths in its contracts without
creating the directories, so a `serve --sim` replay rendered an empty Hangar once the tasks
surface switched to the physical-existence rule. This suite pins the builder's contract:
live leaves ship their dirs, landed/abandoned leaves stay dir-less.

## Code Commentary

### Logic

Loads the builder module by file path (`importlib.util.spec_from_file_location` — the
fixtures folder is not a package), runs `main()` into a temp dir, then walks every
enclosure `series-contract.md`: a `cleanup: pending` contract's `worktree:` paths (code and
memory, parsed by regex from the contract text) must exist as directories; any other
cleanup state must have NO dirs, so the hidden states (landed, abandoned) keep being
exercised by the sim. Guards against silent fixture drift with non-zero live/hidden counts.

## Cross-Repo Evidence

No sibling repository evidence is needed for this test suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T10:30+02:00 — Created for the L11 adversarial-review follow-up (L11R-1): pins materialize_worktrees behavior in the rich sim fixture builder. Verification metadata pinned until closeout stamps the L11 commit.
