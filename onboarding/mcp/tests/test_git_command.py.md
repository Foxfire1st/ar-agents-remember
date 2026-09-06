# mcp/tests/test_git_command.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_git_command.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Safe Git execution and exact private-commit preparation contracts.

## Code Commentary

### Logic

A decoy selected through Git environment variables never receives the real commit. Timeout and concurrent candidate-index cases remain bounded and isolated. Private preparation preserves logical HEAD/index, normal hook execution, exact tree/parent and raw CRLF/signature commit bytes. Forged/cancelled authority, hidden index flags, physical drift and stale bindings refuse; a failed hook returns its original failure once.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Repository selectors are deliberately reset inside the test so fixture cleanup cannot mask the runner guard. Private commit creation does not itself publish protected refs or confer lifecycle authority.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| A commit lands in the real repository not the decoy. | `test_a_commit_lands_in_the_real_repository_not_the_decoy` | mcp/tests/test_git_command.py:93-117 |
| An explicit timeout still bounds a stalled command. | `test_an_explicit_timeout_still_bounds_a_stalled_command` | mcp/tests/test_git_command.py:121-131 |
| Candidate tree isolates concurrent observers with one scratch namespace. | `test_candidate_tree_isolates_concurrent_observers_with_one_scratch_namespace` | mcp/tests/test_git_command.py:135-151 |
| Exact private commit preserves logical state and normal hook policy. | `test_exact_private_commit_preserves_logical_state_and_normal_hook_policy` | mcp/tests/test_git_command.py:202-234 |
| Raw commit readback preserves crlf and opaque signature header. | `test_raw_commit_readback_preserves_crlf_and_opaque_signature_header` | mcp/tests/test_git_command.py:236-264 |
| Cancelled owner and forged capability start no commit. | `test_cancelled_owner_and_forged_capability_start_no_commit` | mcp/tests/test_git_command.py:266-277 |
| Hidden index flags and changed physical bytes refuse commit. | `test_hidden_index_flags_and_changed_physical_bytes_refuse_commit` | mcp/tests/test_git_command.py:279-294 |
| Stale logical tip and rebound private metadata refuse before mutation. | `test_stale_logical_tip_and_rebound_private_metadata_refuse_before_mutation` | mcp/tests/test_git_command.py:296-320 |
| Failed hook returns original failure and does not retry. | `test_failed_hook_returns_original_failure_and_does_not_retry` | mcp/tests/test_git_command.py:322-337 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-29T12:52+02:00 — MCAR-L02 C009 recovery: added the 24-observer
  candidate-index isolation proof after live queue/dashboard projection exposed a shared-scratch
  deletion race. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-14T12:13:26+02:00 — R43 curator: recorded the precise non-repository refusal asserted by
  the selector-isolation test. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: replaced the removed optional quality-gate Git helper with
  the shared fail-closed probe. Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 citation maintenance: re-anchored the shared Git selector import after `conftest.py` simplification; command behavior is unchanged.
- 2026-08-12T03:31+02:00 — 260731-EFA-L22 closeout repair: added the 41st regression, a real failing
  pre-commit hook that emits invalid UTF-8. The test proves raw runner output retains surrogateescape
  and the worktree facade renders that byte as a literal escape before JSON serialization. Re-derived
  the shifted suite citations and replaced the ambiguous selector anchor with the exact assertion.
  Verification metadata remains pinned until closeout stamps the repair.

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 32 citation findings and repaired the
  accumulated drift. The suite is 40 tests across nine classes (was stated as 32/8); documented the
  previously missing `RunnerArgvTests` (794-827). Every member line reference was re-derived against
  the current file (decoy 158-213, runner-contract 215-293, quality-gate 331-392, guard-reach
  489-549, timeout 582-662, benchmark 672-793), the renamed
  `test_a_computed_argv_is_this_sweeps_documented_blind_spot` (539-549) replaces the stale name, the
  import roll-call gained `GIT_BULK_REMOTE_TIMEOUT_SECONDS` (block at L45-L53), and the
  `commands.py` claims were rewritten: it routes every command through the shared `run_git` rather
  than composing argv itself. All eleven malformed/unanchored rows were re-anchored with exact spans,
  and the eleven non-cit prose line-cites were converted to cit form. Scoped recheck clean.

- 2026-07-31T21:46+02:00 — 260731-EFA-L3 curator: re-verified against the restructured file; the
  sidecar created below (same leaf) described a version of it that no longer exists, and being a new
  sidecar it was exempt from the body gate, so nothing would have flagged it. **Every** line range
  was re-derived and all but the module docstring
  (cit:(["The one git runner"], mcp/tests/test_git_command.py:1-15)) had moved: `_selectors` L70-L81 → L137-L148,
  the re-set assertion L104 → L171, `DecoyRepositoryTests` L84-L140 → L151-L207 (members L154-L178 /
  L180-L198 / L200-L207), `_init`/`_commit` L53-L67 → L62-L76, `RunnerContractTests` L143-L220 →
  L210-L287 (members L211-L229 / L231-L247 / L249-L269 / L271-L281 / L283-L287),
  `RemoteBranchStallTests` L223-L254 → L290-L321, `QualityGateGitTests` L257-L319 → L324-L386 (the
  old L301-L319 was two tests, now L368-L375 and L377-L386), `SingleRunnerTests` L322-L402 → L389-L459
  (`_package_modules` L352-L358 → L414-L419; the two tests → L421-L440 and L442-L459),
  `BenchmarkRunnerEnvironmentTests` L405-L442 → L656-L693 (members L664-L680 / L682-L693), and the
  `kernel.git_command` import block L39-L45 → L42-L49 (it now also imports
  `GIT_METADATA_TIMEOUT_SECONDS`, `git_environment` and `run_git`). Content that was outright false:
  `_spawns()` no longer exists — the sweep is four module-level helpers, `_spawn_aliases`
  L79-L92, `_spawn_calls` L95-L112, `_spawns_git` L115-L124, `_passes_env` L127-L134 — and the claimed
  reach ("it only recognises argv built as a list literal") understated it: bare names bound by
  `from subprocess import run [as x]` are now followed, `/usr/bin/git` counts via
  `PurePosixPath(head).name == "git"`, and a `**kwargs` splat no longer passes for an `env=` because
  `_passes_env` requires `keyword.arg == "env"`. Two whole classes were missing: documented
  `SingleRunnerGuardReachTests` (L462-L540, 9 tests planting each bypass form, including the
  deliberate `[]` of `test_a_computed_argv_remains_the_documented_blind_spot` L533-L540) and
  `TimeoutClassTests` (L543-L653, 4 tests, incl. `test_one_command_means_one_bound_across_the_kernel`
  L623-L647), and moved the per-command band claim off `RunnerContractTests`, which only pins the
  constants' ordering. Cross-file citations were checked too: `_git_common_dir` L168-L175 → L176-L183,
  and diff_coverage L137-L164 split into `_git` L137-L163 + `run_git` L166-L173. Verified still
  correct: git_command.py L24-L33 / L53-L55 / L58-L64 / L67-L96, conftest.py L34-L39, git.py L29-L30
  / L81-L86, check.py L132-L149, cleanup.py L108-L119 / L122-L133 / L136-L142, commands.py L9-L36 /
  L39-L40 / L43-L52, test_route_index.py L592-L640. Added rows for `git_facts.py`, `git_freshness.py`,
  `cross_repo.py` and `landing.py`. Test count stated (32 across eight classes) and confirmed by
  running the module. Verification metadata left pinned as the earlier entry set it.
- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: Created for the single-runner Git regression
  matrix added by this leaf. Verification metadata is pinned to the leaf's base commit until
  closeout stamps the code commit.
