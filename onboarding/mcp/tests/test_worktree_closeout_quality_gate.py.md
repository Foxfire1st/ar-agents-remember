# mcp/tests/test_worktree_closeout_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash |  `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate |  2026-08-12T17:53:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the strict worktree closeout quality gate's policy, execution authority, failure
containment, interpreter selection, and ordering before the code commit — and, since
260731-EFA-L1, that the gate is **not** hard-coded to one repository.

The suite also proves the complete fail-fast order: memory preflight → configured pre-commit
hook → strict targeted wrapper → exact-index hook-bypassed commit. The real-hook regression runs
an executable temporary hook, asserts one invocation, modifies the working tree after the wrapper,
and proves that the later modification is not smuggled into the certified commit. It configures a
relative `core.hooksPath` and repeats the certified commit with no staged delta, covering both the
relative hook resolver and no-op exact-index return.

Since 260731-EFA-L4 it also proves **what the gate is shown**. Closeout now stages the code
worktree before running the gate, and the four classes added at L452-L835 cover that staging from
both directions plus its two preconditions and its retry semantics.

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

The rest of the class pins execution: refusal when the wrapper is missing, the exact
`[python, -m, agents_remember.code_quality.check]` argv with `cwd` at the worktree and the
worktree's `mcp/src` first on `PYTHONPATH`, bounded failure output (last 40 lines: `line-0` absent,
`line-49` present), and the worktree-then-shared-clone virtualenv order.

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
- `test_the_gate_hands_the_wrapper_no_repository_selectors` sets every name in
  `GIT_REPOSITORY_SELECTOR_ENV` to a decoy path, plus a pre-existing `PYTHONPATH`, and asserts
  `quality_environment` returns an environment **disjoint** from those eight names. The wrapper is
  not inert — it runs `git ls-files` for its scope and `merge-base` for its diff base — so copying
  `os.environ` through made this gate's answer depend on a child process stripping the selectors
  itself. The same test pins that nothing else moved: `PYTHONPATH` is exactly
  `<worktree>/mcp/src` then the inherited value, and `PATH` is still present, without which the
  wrapper cannot start.

`CloseoutCodeQualityGateTests` runs against real temporary external-memory contract fixtures:

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

`closeout.py` now routes the apply path through `_gate_staged_code(code_worktree, diff_base=…)`,
which refuses two unsafe checkouts, does a mixed reset, `git add -A`, and only then runs the gate.
Four classes cover it.

**cit:([`CloseoutGateSeesCreatedFilesTests`], mcp/tests/test_worktree_closeout_quality_gate.py:350-456) — the original defect, in both directions.**
`derive_scope` picks what ruff and pyright are given with `git ls-files`, which reads the index;
`diff_coverage` diffs the base against the tracked tree, which is blind to the same files; and
closeout commits with `git add -A`. Everything in that gap — every path the task created and never
staged — went into the commit with no rail of the gate having read a line of it, while the gate
reported green. **Leaf 3's `abc7cbcc` shipped four files that way.**

- cit:([`test_a_created_file_carrying_a_lint_error_fails_the_gate`], mcp/tests/test_worktree_closeout_quality_gate.py:361-384): a created
  `pkg/leaf_addition.py` containing `import os` must make closeout raise, the message must name
  `pkg/leaf_addition.py:1:` and `F401`, the created path must appear in the gate's own
  `lint_paths`, and HEAD plus `closeout_status` must be unmoved. The assertion is that the gate
  failed **on this file, having read it** — not merely that it failed.
- cit:([`test_a_refused_gate_commits_nothing_and_leaves_the_worktree_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:386-423): the promise is
  "nothing was committed", **not** "nothing was staged". Closeout stages the task's own worktree
  and does not put it back; what must hold is that no commit was created, the contract did not
  advance, and a further `add -A` reaches the byte-identical tree — so `commit_if_dirty`'s own add
  adds nothing to what the gate certified.
- cit:([`test_the_gates_scope_is_the_commits_content`], mcp/tests/test_worktree_closeout_quality_gate.py:425-456): the invariant as an **equality**
  rather than a trust — `sorted(gate.lint_paths) == sorted(py files in the commit tree)`. The
  deletion arm is there because the index cut both ways: a path the leaf *removed* stayed in
  `git ls-files` until the removal was staged, so the pre-fix gate handed ruff a file that no
  longer existed and took an `E902 No such file or directory` for it — the exact mirror of the
  created file it never looked at.

The fixture cit:([`_gate_scope_contract_fixture`], mcp/tests/test_worktree_closeout_quality_gate.py:263-310) is deliberately minimal: internal memory
mode keeps sidecar/ledger/memory-quality machinery out of the way, and the base commit already
carries everything `derive_scope` needs (a tracked top-level package, a `pyproject.toml` declaring
`testpaths`, the quality wrapper whose presence makes the gate mandatory), so the only thing that
differs between base and closeout is the file the leaf creates. cit:([`_ScopeRecordingGate`], mcp/tests/test_worktree_closeout_quality_gate.py:312-347)
is the wrapper's **own** `derive_scope` handed to the wrapper's **own** first rail
(`ruff check <lint_paths>`) — the pair `quality_steps` builds — so it stands in for the whole
wrapper without paying for pyright and a full pytest run. Substituting anything less real would
miss the defect entirely: it was never in ruff, it was in which files ruff was handed, and only
the real `derive_scope` can be wrong about that.

**cit:([`TaskWorktreePreconditionTests`], mcp/tests/test_worktree_closeout_quality_gate.py:536-659) — the linked-worktree refusal.** Staging is safe in a
task worktree because that checkout is disposable scratch space with nobody in it; it is **not**
safe in a repository's own checkout, and closeout can be handed one —
`default_series_contract` records `code_worktree = code.repo_path` for a `kind: "series"` contract.
The guard tests git's own definition of a linked worktree (`--git-dir` differing from
`--git-common-dir`) rather than the contract's `kind`, because that is the property the safety
argument rests on: `kind` is a label beside the path, the git-dir comparison constrains the path
about to be written.

- cit:([`test_the_repositorys_own_checkout_is_refused_before_anything_is_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:625-658) asserts the
  **damage that does not happen**, not merely a message: a partial `git add -p` selection
  (`one\ntwo` staged, `one\ntwo\nthree` on disk) survives intact, an untracked `secret.env` is
  still untracked with no object written for it, `status --porcelain` is byte-identical, and the
  gate was never called. Both losses are unrecoverable from git alone. The message must say
  "is not a task worktree" and "Nothing was staged and nothing was committed".
- cit:([`test_a_series_contracts_code_worktree_is_exactly_that_checkout`], mcp/tests/test_worktree_closeout_quality_gate.py:660-694) proves the refusal
  is aimed at a shape the system really produces: `series.kind == "series"` and
  `series.code_worktree == repo`. Without it the guard is a guess about a shape nobody builds.
- cit:([`test_a_task_worktree_passes_the_precondition_and_is_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:696-712) is the positive leg.
- cit:([`test_a_refused_gate_leaves_the_task_worktree_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:714-733) states the no-rollback design
  as a test: the created file stays in `ls-files`, and there is **no** `index.lock` and **no**
  `ar-closeout-index-*` snapshot left behind — an earlier attempt saved the index aside and copied
  it back, and that machinery is gone rather than fixed.

**cit:([`ConflictedIndexTests`], mcp/tests/test_worktree_closeout_quality_gate.py:736-794) — the conflict refusal.** `git add -A` over an unmerged index
does not refuse; it resolves every conflict to whatever the working tree holds, markers included,
and closeout then commits that.

- cit:([`test_a_conflicted_worktree_is_refused_before_anything_is_staged`], mcp/tests/test_worktree_closeout_quality_gate.py:745-767): the message names
  "closeout cannot stage the code worktree", "unmerged path", the file, and "conflict markers"; the
  gate is not called and HEAD plus `status --porcelain` are unchanged.
- cit:([`test_the_reset_runs_after_the_conflict_check_not_before_it`], mcp/tests/test_worktree_closeout_quality_gate.py:769-794) pins the **order**
  through what survives rather than through call bookkeeping. A mixed reset drops the unmerged
  index entries and removes `MERGE_HEAD`; run first, `diff --diff-filter=U` would report nothing,
  the refusal would never fire again, and `add -A` would stage the `<<<<<<<` markers. So
  `MERGE_HEAD` still existing after the refusal is the property that says the reset has not run.

**cit:([`RetryStagesWhatAFirstRunWouldTests`], mcp/tests/test_worktree_closeout_quality_gate.py:800-863) — staging is recomputed, not accumulated.**
`git add -A` applies ignore rules only to paths git does not already track or hold staged, so a
file staged by a refused gate stays staged after the leaf adds it to `.gitignore`, and the retry
commits it. **That is how a `.dmypy.json` a type checker had dropped in the worktree got into this
leaf's own first commit.** The mixed reset is what removes the path dependence.
cit:([`test_a_retry_commits_the_tree_a_first_run_would`], mcp/tests/test_worktree_closeout_quality_gate.py:835-863) asserts it as an **equality of
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

The staging classes keep git real in both directions: cit:([`_task_worktree`], mcp/tests/test_worktree_closeout_quality_gate.py:468-483) builds a
repository **and** a linked worktree off it, because the precondition under test is git's own
distinction between the two and a fixture that faked it would be testing the fixture;
cit:([`_conflicted_task_worktree`], mcp/tests/test_worktree_closeout_quality_gate.py:596-607) produces a genuine unmerged index by running a real
conflicting merge. cit:([`_refusing_gate`], mcp/tests/test_worktree_closeout_quality_gate.py:462-466) is the shared patch for "the gate raises",
and cit:([`GATE_REFUSAL`], mcp/tests/test_worktree_closeout_quality_gate.py:459-459) is the message closeout really emits. The two module constants
cit:([`CREATED_FILE`], mcp/tests/test_worktree_closeout_quality_gate.py:260-260) and cit:([`DROPPED_TOOL_ARTEFACT`], mcp/tests/test_worktree_closeout_quality_gate.py:797-797) name the paths the created-file and retry
cases turn on.

### Invariants And Boundaries

- Gate applicability is asserted from wrapper presence, never from a repository name. No test may
  reintroduce a name-based expectation.
- All three `status` values must stay covered; `wrapper-unavailable` must remain distinguishable
  from `no-code-commit` in the payload.
- The executed module must come from the current worktree even when Python is shared.
- The leaf's own base must be observed reaching the wrapper as `--diff-base`. A gate measured
  against `main` is unpassable for a leaf, which is a different bug from a gate that never runs
  but the same loss of enforcement.
- The environment handed to the wrapper must be asserted free of `GIT_REPOSITORY_SELECTOR_ENV`,
  and the `PYTHONPATH` ordering and `PATH` must be asserted alongside it — a test that only
  checks the selectors are gone would pass a `quality_environment` that returned `{}`.
- Failure evidence is useful but bounded.
- Gate failure precedes every code, memory, ledger, and contract mutation.
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
| `CodeQualityGateTests` covers all three gate statuses, invocation, worktree import authority, stable report publication/overwrite on pass and fail, the `--diff-base` argument, the scrubbed wrapper environment, bounded exceptions, and interpreter selection. | `CodeQualityGateTests`, `test_gate_replaces_one_test_report_instead_of_accumulating_runs`, `test_gate_failure_includes_bounded_wrapper_output` | mcp/tests/test_worktree_quality_gate_runner.py:19-659 |
| The argument spy proves both closeout entry points pass the checkout path, not the repository name. | `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_closeout_quality_gate.py:55-257 |
| Closeout integration tests prove zero mutation on failure and quality-before-commit on success. | `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_closeout_quality_gate.py:55-257 |
| The created-file/deleted-file scope cases: a created file must be linted, and the gate's `lint_paths` must equal the `.py` files of the commit tree. | `CloseoutGateSeesCreatedFilesTests` | mcp/tests/test_worktree_closeout_quality_gate.py:350-456 |
| The linked-worktree precondition: a repository's own checkout is refused with its `add -p` selection and untracked files intact, a `kind: "series"` contract is shown to be exactly that shape, and a refused gate leaves no rollback machinery behind. | `TaskWorktreePreconditionTests` | mcp/tests/test_worktree_closeout_quality_gate.py:536-659 |
| The conflict refusal and the ordering proof that the mixed reset runs after it (`MERGE_HEAD` survives). | `ConflictedIndexTests` | mcp/tests/test_worktree_closeout_quality_gate.py:736-794 |
| The retry tree-equality proof that staging is recomputed per attempt rather than accumulated. | `RetryStagesWhatAFirstRunWouldTests` | mcp/tests/test_worktree_closeout_quality_gate.py:800-863 |
| The adapter under test: the three status constants plus wrapper-presence applicability and the preview that reports them. | `quality_environment` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:554-584 |
| `quality_environment`, whose `git_environment()` base the selector test asserts. | `quality_environment` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:554-584 |
| The unannotated call sites the spy guards, both passing `contract.code_worktree` and `diff_base=contract.code_base_commit`. The apply path now reaches the gate through `_gate_staged_code`. | `_gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout.py:789-845 |
| `_gate_staged_code` under test: both refusals, then the mixed reset, then `add -A`, then the gate — and the recorded reasoning for the ordering and for having no rollback. | `_gate_staged_code` | mcp/src/agents_remember/worktrees/modules/closeout.py:789-845 |
| The two preconditions themselves: the linked-worktree check and the unmerged-index check. | `_refuse_outside_a_linked_worktree`; `_refuse_conflicted_worktree` | mcp/src/agents_remember/worktrees/modules/closeout.py:774-813; mcp/src/agents_remember/worktrees/modules/closeout.py:816-839 |
| The scope derivation the created-file cases exercise for real — `git ls-files` over the index is why staging changes what the gate sees. | `derive_scope`; `posix_args` | mcp/src/agents_remember/code_quality/check.py:77-78; mcp/src/agents_remember/code_quality/check.py:369-370 |
| `GIT_REPOSITORY_SELECTOR_ENV` — the eight names the selector test plants and then requires absent — and `git_environment`, which removes them. | `GIT_REPOSITORY_SELECTOR_ENV`; `git_environment` | mcp/src/agents_remember/kernel/git_command.py:34-43; mcp/src/agents_remember/kernel/git_command.py:85-91 |

## Cross-Repo References

The tests operate on repository-local temporary fixtures, but the behavior they pin is explicitly
about other repositories: a bare temp checkout stands in for a consuming repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| A checkout with no wrapper is reported as `wrapper-unavailable` rather than silently skipped, which is the consuming-repository case. | `test_preview_reports_missing_wrapper_instead_of_skipping_silently` | mcp/tests/test_worktree_quality_gate_runner.py:51-67 |

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

## Update History
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
  cit:([`_gate_staged_code`], mcp/src/agents_remember/worktrees/modules/closeout.py:789-845). Recorded all four with the property each actually
  asserts: cit:([`CloseoutGateSeesCreatedFilesTests`], mcp/tests/test_worktree_closeout_quality_gate.py:350-456) — the original defect in **both**
  directions, a created file that must be linted and a deleted file that must stop being handed to
  ruff, closed by the equality `sorted(gate.lint_paths) == sorted(.py files in the commit tree)`,
  with cit:([`_ScopeRecordingGate`], mcp/tests/test_worktree_closeout_quality_gate.py:312-347) running the wrapper's own `derive_scope` because a lesser
  double would miss a defect that was never in ruff; cit:([`TaskWorktreePreconditionTests`], mcp/tests/test_worktree_closeout_quality_gate.py:536-659) —
  the linked-worktree refusal, asserted as the damage that does not happen (the `add -p` selection
  survives, `secret.env` stays untracked with no object written, `status --porcelain` is
  byte-identical) plus the proof that `default_series_contract` really produces
  `code_worktree == repo_path`, plus the explicit no-rollback end state (no `index.lock`, no
  `ar-closeout-index-*`); cit:([`ConflictedIndexTests`], mcp/tests/test_worktree_closeout_quality_gate.py:736-794) — the conflict refusal and the
  ordering proof that the mixed reset runs **after** it, established through `MERGE_HEAD` still
  existing rather than through call bookkeeping; and cit:([`RetryStagesWhatAFirstRunWouldTests`], mcp/tests/test_worktree_closeout_quality_gate.py:800-863) — staging recomputed per attempt, asserted as tree equality against a worktree that
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
  `run_strict_code_quality_gate`) and added rows for cit:([`quality_environment`], mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:554-584) and for
  `git_command.py` L24-L64 (`GIT_REPOSITORY_SELECTOR_ENV` and `git_environment`).

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
