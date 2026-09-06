# mcp/tests/test_code_quality_check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_code_quality_check.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Sample repository and shared constants for quality-selection consumers.

## Code Commentary

### Logic

write_sample_repository creates an uncommitted temporary Git fixture with product ownership for pkg, an empty verification owner list, pytest discovery, lint/type/coverage settings and representative source/test/script files. run_git is the bounded command helper. No quality tests remain in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The filename does not establish complexity or coverage enforcement. Fixture configuration supports consuming tests and must not restore removed percentage gates.

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
| Run git. | `run_git` | mcp/tests/test_code_quality_check.py:21-27 |
| Write sample repository. | `write_sample_repository` | mcp/tests/test_code_quality_check.py:30-62 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the wrapper-inventory-to-profile proof replacement in code quality check tests.


- 2026-08-28T14:18+02:00 — Reconciled quality-orchestration test citations against the committed
  PDLS candidate after final test movement and naming changes.

- 2026-08-26T10:44:52+02:00 — Added forcing for the enforcing evidence-lifecycle rail and its position in the fixed quality command sequence.

- 2026-08-24T21:23+02:00 — Adopted typed Dagger admission and pytest phase-report proof.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: reconciled hook assertions to the
  precise Dagger-only acceptance statement while preserving direct targeted Vitest as a separate
  non-certifying diagnostic route. No acceptance run was performed during curation.
- 2026-08-14T11:48:55+02:00 — R42 curator: recorded the file-size extraction of direct wrapper
  authorization and native-temp entry tests into `test_code_quality_environment_guard.py`; this
  card retains suite composition and workflow ownership. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: documented before-planning refusal and the
  PR-non-test/publish-no-rerun workflow invariants. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 cadence: repository-policy assertions now require a
  pull-request-only non-test workflow, no GitHub/host acceptance runner, and explicit leaf-closeout
  ownership in the targeted hook.
- 2026-08-14T06:38+02:00 — L23 final candidate review: wrapper regressions retain exact staged
  scope and short native scratch behavior as the Python rail inside Dagger; direct host execution
  is not acceptance. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented `/tmp/arq` ownership at the quality CLI boundary; verification remains closeout-owned.

- 2026-08-12T17:27+02:00 — 260731-EFA-L23 final Dagger diff-coverage repair: expanded the existing
  targeted-configuration test with the complementary explicit-progress-report call, proving the CLI
  path wins even while `AR_QUALITY_PROGRESS_REPORT` is set. Focused pytest is 1/1; verification
  provenance remains closeout-owned.

- 2026-08-12T16:28+02:00 — 260731-EFA-L23 final diff-coverage repair: extended the existing
  targeted-configuration regression to prove environment-derived progress-report ownership and
  to define the optional coverage/progress/pytest-report arguments explicitly. Focused test proof
  belongs to the code change; verification provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: recorded the targeted file-size-arm and exact
  Ruff-pin regressions; refreshed shifted ranges after inserting them.

- 2026-08-12T00:08+02:00 — No content impact: the repository-gate subtest reports each gate path
  as a serializable POSIX string for xdist; the gate reachability and no-opt-out assertions are
  unchanged. Verification metadata remains pinned until closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the pre-push
  targeted-tier assertions and the full-tier manual/master-gate posture.
  Verification metadata stays pinned until closeout stamps the 260731-EFA-L17
  commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-08-03T03:59:59+02:00 — Curated 19 citation findings (9 table rows, 10 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator, **correcting the mid-leaf card below**.
  The complexity baseline it described no longer exists: `complexity_baseline.py`,
  `quality/complexity-baseline.txt`, `test_complexity_baseline.py` and the wrapper's
  baseline step were deleted when the developer ruled ratchets/baselines/grandfather
  lists/burn-down schedules forbidden, and all 67 offenders were fixed by extraction.
  `EveryEnforcingStepCanFailTests` was rewritten accordingly and now ends with
  `test_the_complexity_baseline_and_its_gate_step_are_gone`. Added the two classes that
  did not exist when that card was written — `ToolSignatureExemptionTests` (the single
  `PLR0913` exemption over the MCP registration directory, held shut by an AST test) and
  `CrapThresholdEnforcementTests` (every offender named, the clearing coverage inverted
  from the CRAP formula, split-instead-of-test, no exemption file) — plus the expanded
  `GateScopeDerivationTests` refusal arms and `main`'s verdict pass-through. Corrected the
  fast-tier description (no baseline step) and dropped the baseline reference row.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 gate honesty (mid-leaf, superseded above).
  Recorded the four new test classes:
  `RadonIsAReportNotAGateTests` (exactly the two Radon steps are reports; the header and
  help text say so; a broken report step still fails), `EveryEnforcingStepCanFailTests`
  (the routed complexity rules match the baseline's exactly; format and baseline steps
  are enforcing over the derived scope; the ratchet must name an owner and a burn-down),
  `GateScopeDerivationTests` (no hand-written scope constant; the index is the scope; a
  script outside every package reaches both rails; a underivable scope refuses), and
  `PytestConfigurationTests` (strictness switches, `python_classes`, the exact-count
  warning cap, and two-way marker/environment-gate reconciliation). Corrected the fast
  tier description to include the formatter, the baseline, and the harness generated-copy
  check. Verification metadata is pinned to the leaf's reformat commit until closeout
  stamps the code commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 split the hooks into a fast staged-content tier and a full
  pre-push tier over a shared `.githooks/_gate.sh`. `test_repository_gates_use_default_strict_wrapper`
  now scans `_gate.sh` and the CI workflow instead of the two hook files, which no longer inline the
  wrapper command; the new `test_git_hooks_delegate_to_the_shared_tiered_gate` pins each hook to its
  tier so neither can be silently promoted or demoted. Corrected this card's claim that pre-commit
  invokes the wrapper. Verification metadata pinned to the pre-leaf source authority until closeout
  stamps the code commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: documented mandatory default
  threshold failure, removal of the strict opt-in surface, and repository-gate command parity;
  verification remains pinned until the code commit.

- 2026-06-08T12:06+02:00: Added coverage that the Pyright command includes
  `--pythonpath` and the active interpreter path, matching the linked-worktree
  quality gate fix. Verification metadata stays pinned until closeout.
  task/runtime-asset-canonical-sync branch.
- 2026-06-02T10:35+02:00: Added a test that the wrapper threads this checkout's source import root first onto `PYTHONPATH` (preserving any pre-existing value); the fake runners now take the `env` argument. Verification metadata stays pinned until closeout. fix/quality-gate-worktree-local branch.
- 2026-05-28T19:52+02:00: Updated after source quality wrapper tests began asserting Pyright command wiring.
- 2026-05-24T06:30+02:00: Created unit coverage for the source quality suite wrapper.
