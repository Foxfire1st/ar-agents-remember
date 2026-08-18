# mcp/tests/test_worktree_closeout_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T04:06+02:00 |
| lastVerifiedCommitHash |  `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b`|
| lastVerifiedCommitDate |  2026-08-18T03:31:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the strict worktree closeout quality gate's policy, Dagger-only execution
authority, failure containment, and ordering before the code commit — and, since
260731-EFA-L1, that the gate is **not** hard-coded to one repository.

The suite also proves the complete fail-fast order: memory preflight → configured pre-commit
hook → strict targeted wrapper → exact-index hook-bypassed commit. The real-hook regression runs
an executable temporary hook, asserts one invocation, modifies the working tree after the wrapper,
and proves that the later modification is not smuggled into the certified commit. It configures a
relative `core.hooksPath` and repeats the certified commit with no staged delta, covering both the
relative hook resolver and no-op exact-index return.

Since 260731-EFA-L4 it also proves **what the gate is shown**. Closeout stages the code worktree
before running the gate. R42 moved the exact created/deleted-file scope fixture and class to
`test_worktree_closeout_gate_scope.py`; this file retains the linked-worktree precondition,
conflicted-index refusal, and retry-recomputation classes.

L23 adds two focused structural-rail branches: malformed/non-list memory-quality details still
produce a bounded count-only refusal, and source lineage is checked a second time after quality but
before approval claim. A source move in that window raises and the approval remains unclaimed.

## Code Commentary

### Logic

`_checkout_with_wrapper(root)` plants `mcp/src/agents_remember/code_quality/check.py` in a temp
directory. That is the whole fixture, and it is the point: after the repository-name hard-code was
removed, carrying the wrapper is what makes a checkout gated, so a bare temp directory now stands
in for a consuming repository.

`CodeQualityGateTests` covers the three states by name:

- `test_preview_requires_strict_wrapper_for_any_repo_that_carries_it` — a nameless temp checkout
  that carries the wrapper reports `GATE_ENFORCED` with the exact default command.
- `test_preview_reports_no_code_commit_when_nothing_would_commit` — `GATE_NO_CODE_COMMIT`.
- `test_preview_reports_missing_wrapper_instead_of_skipping_silently` — a consuming repository
  without the wrapper reports `GATE_WRAPPER_UNAVAILABLE`, and the reason names `QUALITY_WRAPPER`
  and says "not quality-checked". This is the regression against re-silencing that case.

The rest of the class pins execution: refusal when the wrapper is missing, symbolic Dagger command
construction, immediate host-execution refusal, bounded failure output (last 40 lines: `line-0`
absent, `line-49` present), and durable Dagger evidence publication.

The same cases now pin durable evidence. A passing gate returns the exact
`reports/test-results.md` path and writes its complete output. The replacement regression starts
with an obsolete report, runs twice, and proves only the second completed transcript remains with
no per-run siblings. The interruption regression starts with a completed report, makes the runner
raise before returning, and proves those preceding bytes survive unchanged. The failure regression
keeps the exception tail bounded while proving the stable file contains both `line-0` and `line-49`
and that the exception names its path.

Two more pin what the gate hands the wrapper:

- `test_gate_measures_the_leaf_diff_not_the_whole_branch` and
  `test_gate_preview_reports_the_diff_base_it_will_use` assert the `--diff-base` argument reaches
  the argv, `result["diffBase"]` / `preview["diffBase"]` carry the base on its own key, and both
  rendered `command` strings contain `--diff-base <base>`. Without it the wrapper falls back to
  `origin/HEAD` / `main` and its 100% per-diff coverage floor measures the whole integration
  branch — unpassable for any leaf, so the gate would block every closeout instead of enforcing
  anything.
- `test_host_quality_execution_refuses_before_resolving_or_running_a_wrapper` proves the named
  local entry fails before interpreter, environment, or subprocess planning. Dagger is the only
  executable acceptance path.

`CloseoutCodeQualityGateTests` runs against real temporary external-memory contract fixtures:

- `test_source_lineage_is_rechecked_after_quality_before_approval_claim` makes the first source
  proof pass and the post-quality proof fail, then requires two checks and proves the approval
  claim never runs.

- `test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name` is the guard for a
  mistake nothing else catches. The deciders take a checkout `Path`; handing them
  `contract.repo_name` — their signature before the hard-code was removed — makes
  `quality_wrapper_path` build a relative path off the process CWD, which is not a file, so
  `requires_strict_code_quality` returns `False` and the mandatory gate silently never runs.
  `contract` is unannotated in `closeout.py`, so Pyright type-checks that mistake in silence, and
  every other test in this file patches `requires_strict_code_quality` out and therefore cannot see
  the argument. The test covers **both** entry points: the dry-run preview must report
  `GATE_ENFORCED` for a dirty checkout carrying the wrapper, and the apply path must call the real
  decider and `run_strict_code_quality_gate` with `contract.code_worktree` exactly.
- `test_gate_failure_precedes_all_closeout_commits` — a raising gate leaves code HEAD, memory HEAD,
  ledger bytes, and `closeout_status` all unchanged.
- `test_success_runs_hook_then_quality_then_verified_code_commit` — the recorded event order is
  `["pre-commit-hook", "quality", "verified-code-commit"]`.
- `test_memory_preflight_failure_never_starts_the_code_quality_gate` — an orphan entity
  fingerprint stops both the hook and wrapper.
- `CertifiedIndexCommitTests` uses a real hook to prove it runs exactly once and that
  `commit_verified_staged` commits the gate's index rather than later working-tree edits.

#### The staging half (260731-EFA-L4)

`closeout.py` imports `closeout_staged_quality.gate_staged_code` as `_gate_staged_code` and routes
the apply path through that boundary. It refuses two unsafe checkouts, proves any accepted
candidate tree, does a mixed reset, `git add -A`, and only then invokes the pinned Dagger gate.
Three classes remain here. The companion
`test_worktree_closeout_gate_scope.py` owns the created/deleted-file equality proof and uses the
real `derive_scope` plus Ruff first rail to show that the gate reads exactly the Python content
later committed. Keeping that fixture in its own file satisfies the file-size rail without
weakening or duplicating the assertion.

**cit:([`TaskWorktreePreconditionTests`], mcp/tests/test_worktree_closeout_quality_gate.py:808-931) — the linked-worktree refusal.** Staging is safe in a
task worktree because that checkout is disposable scratch space with nobody in it; it is **not**
safe in a repository's own checkout, and closeout can be handed one —
`default_series_contract` records `code_worktree = code.repo_path` for a `kind: "series"` contract.
The guard tests git's own definition of a linked worktree (`--git-dir` differing from
`--git-common-dir`) rather than the contract's `kind`, because that is the property the safety
argument rests on: `kind` is a label beside the path, the git-dir comparison constrains the path
about to be written.

- cit:([`test_the_repositorys_own_checkout_is_refused_before_anything_is_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:869-902) asserts the
  **damage that does not happen**, not merely a message: a partial `git add -p` selection
  (`one\ntwo` staged, `one\ntwo\nthree` on disk) survives intact, an untracked `secret.env` is
  still untracked with no object written for it, `status --porcelain` is byte-identical, and the
  gate was never called. Both losses are unrecoverable from git alone. The message must say
  "is not a task worktree" and "Nothing was staged and nothing was committed".
- cit:([`test_a_series_contracts_code_worktree_is_exactly_that_checkout`], mcp/tests/test_worktree_closeout_quality_gate.py:904-938) proves the refusal
  is aimed at a shape the system really produces: `series.kind == "series"` and
  `series.code_worktree == repo`. Without it the guard is a guess about a shape nobody builds.
- cit:([`test_a_task_worktree_passes_the_precondition_and_is_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:940-956) is the positive leg.
- cit:([`test_a_refused_gate_leaves_the_task_worktree_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:958-977) states the no-rollback design
  as a test: the created file stays in `ls-files`, and there is **no** `index.lock` and **no**
  `ar-closeout-index-*` snapshot left behind — an earlier attempt saved the index aside and copied
  it back, and that machinery is gone rather than fixed.

**cit:([`ConflictedIndexTests`], mcp/tests/test_worktree_closeout_quality_gate.py:934-992) — the conflict refusal.** `git add -A` over an unmerged index
does not refuse; it resolves every conflict to whatever the working tree holds, markers included,
and closeout then commits that.

- cit:([`test_a_conflicted_worktree_is_refused_before_anything_is_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:989-1011): the message names
  "closeout cannot stage the code worktree", "unmerged path", the file, and "conflict markers"; the
  gate is not called and HEAD plus `status --porcelain` are unchanged.
- cit:([`test_the_reset_runs_after_the_conflict_check_not_before_it`], mcp/tests/test_worktree_closeout_quality_gate.py:1013-1038) pins the **order**
  through what survives rather than through call bookkeeping. A mixed reset drops the unmerged
  index entries and removes `MERGE_HEAD`; run first, `diff --diff-filter=U` would report nothing,
  the refusal would never fire again, and `add -A` would stage the `<<<<<<<` markers. So
  `MERGE_HEAD` still existing after the refusal is the property that says the reset has not run.

**cit:([`RetryStagesWhatAFirstRunWouldTests`], mcp/tests/test_worktree_closeout_quality_gate.py:998-1061) — staging is recomputed, not accumulated.**
`git add -A` applies ignore rules only to paths git does not already track or hold staged, so a
file staged by a refused gate stays staged after the leaf adds it to `.gitignore`, and the retry
commits it. **That is how a `.dmypy.json` a type checker had dropped in the worktree got into this
leaf's own first commit.** The mixed reset is what removes the path dependence.
cit:([`test_a_retry_commits_the_tree_a_first_run_would`], mcp/tests/test_worktree_closeout_quality_gate.py:1079-1107) asserts it as an **equality of
committed trees**, not as the presence of a `reset` call: one worktree is refused with the artefact
already staged, then ignored and retried; a second worktree reaches the same end state having never
seen a refusal; both run the same closeout steps, so the only thing that could make the trees
differ is history the index carried across attempts. The two `rev-parse HEAD^{tree}` values must be
equal, and `.dmypy.json` must be absent from the retried commit.

### Conventions

Gate functions and process runners are injected only at the narrow boundary under test; real
worktree contract and Git behavior are retained wherever mutation ordering is the contract. The
argument-spy test deliberately does **not** patch the decider's behavior — it wraps the real one —
because a stub would hide the exact defect it exists to catch. It also plants file-level onboarding
for the planted wrapper, since the wrapper is a changed source file as far as closeout's
missing-onboarding check is concerned.

The staging classes keep git real in both directions: cit:([`_task_worktree`], mcp/tests/test_worktree_closeout_quality_gate.py:651-665) builds a
repository **and** a linked worktree off it, because the precondition under test is git's own
distinction between the two and a fixture that faked it would be testing the fixture;
cit:([`_conflicted_task_worktree`], mcp/tests/test_worktree_closeout_quality_gate.py:840-851) produces a genuine unmerged index by running a real
conflicting merge. cit:([`_refusing_gate`], mcp/tests/test_worktree_closeout_quality_gate.py:643-648) is the shared patch for "the gate raises",
and cit:([`GATE_REFUSAL`], mcp/tests/test_worktree_closeout_quality_gate.py:644-644) is the message closeout really emits. The two module constants
cit:([`DROPPED_TOOL_ARTEFACT`], mcp/tests/test_worktree_closeout_quality_gate.py:1045-1045) names the
path the retry case turns on; the created-file fixture now lives in the companion scope suite.

### Invariants And Boundaries

- Gate applicability is asserted from wrapper presence, never from a repository name. No test may
  reintroduce a name-based expectation.
- All three `status` values must stay covered; `wrapper-unavailable` must remain distinguishable
  from `no-code-commit` in the payload.
- The Dagger graph must reconstruct the exact current candidate and ancestry bundle.
- The leaf's own base must be observed reaching the wrapper as `--diff-base`. A gate measured
  against `main` is unpassable for a leaf, which is a different bug from a gate that never runs
  but the same loss of enforcement.
- The host diagnostic entry must refuse before resolving an interpreter, building an environment,
  or spawning a subprocess.
- Failure evidence is useful but bounded.
- Gate failure precedes every code, memory, ledger, and contract mutation.
- Series/master candidate mutation during quality is detected from the durable accepted tree
  before approval claim and code commit; leaf review evidence remains a separate assertion.
- Series/master closeout calls neither the targeted quality decider nor executor, refuses dirty
  code before quality or approval, and can only record clean landed HEAD.
- At least one test must observe the *actual argument* passed from `closeout.py`, because the type
  system cannot.
- The gate's scope and the commit's content must remain **one set**, asserted as an equality rather
  than as two enumerations kept in step by hand. Both directions matter: a created file the gate
  never read, and a deleted file the gate was still handed.
- Staging must stay refused outside a linked worktree, and the refusal must be proved by the damage
  that does not happen (`add -p` selection intact, untracked file still untracked, `status`
  byte-identical), not only by a message.
- Staging must stay refused on an unmerged index, and the mixed reset must stay **after** both
  refusals. Moving it ahead of the first inflicts the damage the first prevents; ahead of the
  second it silently disarms the second.
- There is no rollback and none is wanted: no saved index file, no `index.lock`, no
  `ar-closeout-index-*` snapshot. A refused attempt leaves the task worktree staged, and that is
  the documented end state.
- A retry must commit the tree a first run would. The property is asserted as tree equality against
  a worktree that never saw the refusal, never as the presence of a `reset` call.

### Todos

No durable follow-up is recorded. Note that the two inline `closeout.py:NNN` comments inside
`test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name` (L277 and L289) still
quote pre-L4 line numbers; the real call sites are `closeout.py` L289-L293 (preview) and L721-L729
(apply).

## Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md`
has no entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is needed for these repository-local regressions. | — | — |

## Repo-Internal References

The suite proves the adapter and its production closeout call sites together.

| Finding | Anchor | Source |
| --- | --- | --- |
| `CodeQualityGateTests` covers all three gate statuses, Dagger invocation, stable report publication/overwrite on pass and fail, the diff base, immediate host refusal, and bounded exceptions. | `CodeQualityGateTests`, `test_gate_replaces_one_test_report_instead_of_accumulating_runs`, `test_gate_failure_includes_bounded_wrapper_output` | mcp/tests/test_worktree_quality_gate_runner.py:15-445 |
| The argument spy proves both closeout entry points pass the checkout path, not the repository name. | `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_closeout_quality_gate.py:55-257 |
| Closeout integration tests prove zero mutation on failure and quality-before-commit on success. | `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_closeout_quality_gate.py:55-257 |
| The companion created-file/deleted-file scope cases require the gate's `lint_paths` to equal the `.py` files of the commit tree. | `CloseoutGateSeesCreatedFilesTests` | mcp/tests/test_worktree_closeout_gate_scope.py:130-208 |
| The linked-worktree precondition: a repository's own checkout is refused with its `add -p` selection and untracked files intact, a `kind: "series"` contract is shown to be exactly that shape, and a refused gate leaves no rollback machinery behind. | `TaskWorktreePreconditionTests` | mcp/tests/test_worktree_closeout_quality_gate.py:808-931 |
| The conflict refusal and the ordering proof that the mixed reset runs after it (`MERGE_HEAD` survives). | `ConflictedIndexTests` | mcp/tests/test_worktree_closeout_quality_gate.py:934-992 |
| The retry tree-equality proof that staging is recomputed per attempt rather than accumulated. | `RetryStagesWhatAFirstRunWouldTests` | mcp/tests/test_worktree_closeout_quality_gate.py:998-1061 |
| The adapter under test: the three status constants plus wrapper-presence applicability and the preview that reports them. | `requires_strict_code_quality`; `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:76-177 |
| The explicit local entry refuses host test execution without a fallback. | `run_local_quality_diagnostic` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:338-348 |
| The closeout call site passes `contract.code_worktree`, the enclosure worktree group, `diff_base=contract.code_base_commit`, the configured Dagger executor, and the accepted candidate tree through the imported `_gate_staged_code` alias. | "code_quality_gate = _gate_staged_code(" | mcp/src/agents_remember/worktrees/modules/closeout.py:941-941 |
| `gate_staged_code` under test: both refusals and candidate checks, then the mixed reset, `add -A`, the reviewed pre-commit hook, and the targeted Dagger gate. | `gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129 |
| The two preconditions themselves: the linked-worktree check and the unmerged-index check. | `_refuse_outside_a_linked_worktree`; `_refuse_conflicted_worktree` | mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:20-36; mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:39-51 |
| The scope derivation the created-file cases exercise for real — `git ls-files` over the index is why staging changes what the gate sees. | `derive_scope`; `posix_args` | mcp/src/agents_remember/code_quality/check.py:79-80; mcp/src/agents_remember/code_quality/check.py:372-373 |

## Cross-Repo References

The tests operate on repository-local temporary fixtures, but the behavior they pin is explicitly
about other repositories: a bare temp checkout stands in for a consuming repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| A checkout with no wrapper is reported as `wrapper-unavailable` rather than silently skipped, which is the consuming-repository case. | `test_preview_reports_missing_wrapper_instead_of_skipping_silently` | mcp/tests/test_worktree_quality_gate_runner.py:48-64 |

### 260731-EFA-L17/L24 — Mode, Resource Policy, And Kill-Shape Assertions

`CodeQualityGateTests` (lines 49-423) now asserts the leaf contract command
`python -m agents_remember.code_quality.check --targeted` (and
`--targeted --diff-base <base>`), the `mode` payload key, and the new full-mode
arms: `_gate_command` refuses unknown modes, the full preview names
`memoryPolicy` and names `memoryCap` only for an explicit limit, an uncapped
full run executes host-managed, the planned rlimit mechanism reaches the runner argv, and
over-cap kills (returncode 137 and -9) raise with
`orchestration.qualityGate.memoryCapBytes` named. `CloseoutCodeQualityGateTests`
asserts the apply path passes the targeted plan alongside
`contract.code_worktree` and `contract.code_base_commit`.

### L23 — Exact Candidate And Dagger-Only Acceptance

The current suite binds closeout quality to the reviewed candidate tree before staging, after
staging, and after any configured pre-commit hook. Its argument assertions require the targeted
plan with `executor="dagger"`, and post-quality lineage and route-review checks run before approval
is claimed. Historical host-managed full-mode assertions above describe the earlier L17/L24
contract; they do not provide a second acceptance path for the current candidate.

## R39 Closeout Forcing Evidence

The closeout suite now proves an Agents Remember leaf refuses a missing self-owned wrapper before
memory quality, approval, gate execution, or commit. It also proves series/master closeout runs no
acceptance, refuses dirty code, binds an accepted candidate tree durably, and rechecks that tree
after quality before approval claim. Leaf staged-candidate and route-review protections remain.

## R43 Candidate And Self-Policy Fixtures

The two interruption/recovery closeout fixtures now carry the real current candidate tree so they
exercise the same mandatory identity admission as production. The checkout-path decider spy also
accepts and forwards `required_when_missing`, preserving the self-repository wrapper policy while
still proving both preview and apply receive the actual worktree path.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## Update History

- 2026-08-16T04:06+02:00 — Dagger fixture repair: the series candidate-drift case isolates exact named-ref revalidation, while memory-only dirt expects the unified no-series-workbench refusal.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-14T12:13:26+02:00 — R43 curator: recorded explicit candidate-tree fixtures and the
  self-wrapper-policy-aware decider spy. Verification remains closeout-owned.

- 2026-08-14T11:48:55+02:00 — R42 curator: moved exact created/deleted-file scope ownership to
  `test_worktree_closeout_gate_scope.py` and retained the precondition/conflict/retry responsibilities
  here. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: documented missing-self-wrapper refusal, clean series
  closeout, and post-quality candidate revalidation. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 cadence: added direct no-rerun and production dirty-master
  refusal proofs alongside the all-altitude candidate-drift proof. Series/master closeout cannot
  create code or spend leaf acceptance.

- 2026-08-14T09:08+02:00 — Reopened L23 repair: added the production-path series closeout race
  regression. A candidate mutation during quality must refuse before approval claim or code
  commit while the accepted durable tree remains unchanged. Verification remains closeout-owned.

- 2026-08-14T06:05+02:00 — L23 curator: updated the extracted staged-quality owner and recorded
  exact-candidate binding plus Dagger-only acceptance; earlier host-mode material is retained as
  historical context, not current authority. Verification provenance remains closeout-owned.

- 2026-08-13T12:53+02:00 — L23 Dagger-rail coverage: added the malformed/no-detail bounded
  memory-quality message branch and the post-quality lineage refusal-before-approval proof.
  Verification provenance remains closeout-owned.


- 2026-08-13T08:40+02:00 — L23 integration-gate repair: added the post-quality source-lineage refusal proof before approval claim and supplied a task-derived parent series to the internal gate-scope fixture. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 dependent-contract
  correction: replaced the obsolete cap-less refusal description with the
  host-managed full-gate path; the assertions themselves live in the runner
  suite after L22's split.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: moved `CodeQualityGateTests` into
  `test_worktree_quality_gate_runner.py`, retained closeout mutation/staging ownership here, and
  regenerated all split-sensitive citations.

- 2026-08-11T17:50+02:00 — 260731-EFA-L19 curator: recorded the pass/fail report
  assertions and the two-run replacement proof for one enclosure-local `test-results.md` without
  timestamped accumulation. Verification metadata remains pinned until governed closeout.

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: recorded the current closeout quality-gate assertions
  and staged wrapper boundary; verification metadata remains pinned until closeout.

- 2026-08-10T12:46+02:00 — L9 closeout-order regression proof: added the entity-preflight
  short-circuit, advertised order assertion, explicit hook→wrapper→verified-commit event order,
  and a real Git hook test proving no post-pytest rerun or restage; the delta coverage arm exercises
  relative hook-path resolution and the no-staged-change return. Verification metadata stays pinned
  until closeout stamps the repair commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the targeted-mode
  command assertions and the full-mode/cap/kill-shape regressions. Verification
  metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 13 citation claims (9 table rows, 4 prose citations); scoped recheck clean (0 findings).

- 2026-08-01T08:55+02:00 — 260731-EFA-L4 curator: this suite gained the staging half — four new
  classes at L452-L835, added because closeout now runs the gate over a **staged** worktree via
  cit:([`gate_staged_code`], mcp/src/agents_remember/worktrees/modules/closeout_staged_quality.py:77-129). Recorded all four with the property each actually
  asserts: cit:([`CloseoutGateSeesCreatedFilesTests`], mcp/tests/test_worktree_closeout_gate_scope.py:130-208) — the original defect in **both**
  directions, a created file that must be linted and a deleted file that must stop being handed to
  ruff, closed by the equality `sorted(gate.lint_paths) == sorted(.py files in the commit tree)`,
  with cit:([`ScopeRecordingGate`], mcp/tests/test_worktree_closeout_gate_scope.py:99-127) running the wrapper's own `derive_scope` because a lesser
  double would miss a defect that was never in ruff; cit:([`TaskWorktreePreconditionTests`], mcp/tests/test_worktree_closeout_quality_gate.py:808-931) —
  the linked-worktree refusal, asserted as the damage that does not happen (the `add -p` selection
  survives, `secret.env` stays untracked with no object written, `status --porcelain` is
  byte-identical) plus the proof that `default_series_contract` really produces
  `code_worktree == repo_path`, plus the explicit no-rollback end state (no `index.lock`, no
  `ar-closeout-index-*`); cit:([`ConflictedIndexTests`], mcp/tests/test_worktree_closeout_quality_gate.py:934-992) — the conflict refusal and the
  ordering proof that the mixed reset runs **after** it, established through `MERGE_HEAD` still
  existing rather than through call bookkeeping; and cit:([`RetryStagesWhatAFirstRunWouldTests`], mcp/tests/test_worktree_closeout_quality_gate.py:998-1061) — staging recomputed per attempt, asserted as tree equality against a worktree that
  never saw the refusal (`.dmypy.json` is this leaf's own history). Added the matching invariants
  and the fixture conventions (`_task_worktree` L570-L584 builds a real repository *and* a real
  linked worktree; `_conflicted_task_worktree` L587-L598 runs a real conflicting merge).
  **Citation repairs.** The import block grew by 10 lines (`code_quality.check`, the six-symbol
  `worktree_contract` import, `init_repo`), so every self-citation shifted by exactly +10 and was
  re-verified against the symbol it names: `CodeQualityGateTests` L39-L236 → **L49-L245**; the
  argument spy L239-L294 → **L249-L304**
  (`test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name`); the closeout
  integration pair L296-L357 → **L306-L367**; cross-repo L67-L83 → **L77-L93**
  (`test_preview_reports_missing_wrapper_instead_of_skipping_silently`). Cross-file rows also
  moved because both source modules changed this leaf: `code_quality_gate.py` L13-L78 → **L13-L82**
  (constants at L13-L19 through the end of `code_quality_gate_preview` at L82) and L157-L173 →
  **L168-L184** (`quality_environment`); `closeout.py` L283-L287; L585-L593 → **L289-L293;
  L721-L729**, the preview call site and the apply path that now routes through
  `_gate_staged_code`. `git_command.py` L24-L64 was re-verified unmoved
  (`GIT_REPOSITORY_SELECTOR_ENV` L24-L33, `git_environment` L58-L64). Added seven rows for the new
  coverage and for `_gate_staged_code`, its two refusal helpers, and `derive_scope`. Verification
  metadata pinned to the pre-leaf source authority until closeout stamps the L4 commit.

- 2026-07-31T21:20+02:00 — 260731-EFA-L3 curator: `CodeQualityGateTests` gained
  `test_the_gate_hands_the_wrapper_no_repository_selectors` this leaf, and the card's enumeration
  of "the rest of the class" read as exhaustive while omitting it and the two `--diff-base` tests
  that arrived with leaf 2's `f3115ce`. Added both groups: the selector test (every
  `GIT_REPOSITORY_SELECTOR_ENV` name planted with a decoy value, the returned environment asserted
  disjoint from them, and `PYTHONPATH` ordering plus `PATH` asserted alongside so the test cannot
  be satisfied by an empty environment) and the `--diff-base` pair
  (`test_gate_measures_the_leaf_diff_not_the_whole_branch`,
  `test_gate_preview_reports_the_diff_base_it_will_use`). Added the two matching invariants.
  Citation repairs — every range in this card pointed at pre-`f3115ce` line numbers and none of the
  three test rows still held the symbol it named: L38-L165 → **L39-L236** (`CodeQualityGateTests`,
  which now ends after the selector test; L165 stopped before even the bounded-failure test at
  L169); L169-L222 → **L239-L294** (the argument spy
  `test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name`, which L169-L222 missed
  entirely); L224-L284 → **L296-L357** (`test_gate_failure_precedes_all_closeout_commits` through
  the end of `test_success_runs_quality_before_code_commit`); cross-repo L66-L82 → **L67-L83**
  (`test_preview_reports_missing_wrapper_instead_of_skipping_silently`); closeout.py
  L283-L285 → **L283-L287** and L583-L589 → **L585-L593**, so both ranges now contain the
  `diff_base=contract.code_base_commit` argument and the apply path's
  `requires_strict_code_quality` / `run_strict_code_quality_gate` calls the spy asserts on
  (closeout.py itself is untouched by this leaf). Tightened the adapter row L15-L112 → **L13-L78**
  (constants through the end of `code_quality_gate_preview`, rather than running into
  `run_strict_code_quality_gate`) and added rows for the then-current host environment. L23 later
  removed that host path and replaced it with an unconditional refusal.

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/tests/test_worktree_closeout_quality_gate.py` and moved the lines this card cites, so the
  Citations column no longer pointed at the code its rows name. Corrected the ranges (L38-L187 →
  L38-L165; L191-L250 → L169-L222; L252-L322 → L224-L284; L76-L96 → L66-L82). The behaviour
  described is unchanged — the file's AST is identical to the base revision — this is a citation
  repair only. Verification metadata pinned until closeout stamps the L2 commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1: rewrote the policy half of this suite for the removal of
  the repository-name hard-code. Added `_checkout_with_wrapper`, three status-named preview tests
  (`enforced` / `no-code-commit` / `wrapper-unavailable`), a `status` assertion on the successful
  run result, and `test_closeout_hands_the_gate_the_code_worktree_not_the_repository_name`, which
  spies on the real argument at both closeout entry points because `contract` is unannotated and
  Pyright cannot catch a `str`-for-`Path` substitution there. Corrected this card's obsolete
  invariant "preview requires the gate only for an Agents Remember code commit". Verification
  metadata pinned to the pre-leaf source authority until closeout stamps the code commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: created the sidecar for the strict
  closeout-gate policy, linked-worktree interpreter, fail-closed mutation ordering, and success
  ordering regressions. Verification remains blank until the new test source is committed.
