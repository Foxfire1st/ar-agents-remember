# mcp/tests/test_sim_fixture_builder.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_sim_fixture_builder.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T10:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|

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

- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 touched only `_load_builder`, which
  now registers the path-loaded module as `sys.modules[spec.name]` before `exec_module` so the
  builder's new parameter-object dataclasses can resolve their PEP 563 string annotations through
  their own module. That is still the `spec_from_file_location` direct-from-path recipe this card
  describes, `main()` still runs into a temp dir, and the contract walk is byte-identical:
  `cleanup: pending` leaves must ship both worktree dirs, every other cleanup state must have
  none, and the live/hidden counts must stay non-zero.
- 2026-07-06T10:30+02:00 — Created for the L11 adversarial-review follow-up (L11R-1): pins materialize_worktrees behavior in the rich sim fixture builder. Verification metadata pinned until closeout stamps the L11 commit.
