# mcp/tests/test_worktree_closeout_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31T04:28+02:00 |
| lastVerifiedCommitHash |  `abc7cbcc74921cdcb57a61529445f61641e919e7`|
| lastVerifiedCommitDate |  2026-07-31T21:50:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite proves the strict worktree closeout quality gate's policy, execution authority, failure
containment, interpreter selection, and ordering before the code commit — and, since
260731-EFA-L1, that the gate is **not** hard-coded to one repository.

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
- `test_success_runs_quality_before_code_commit` — the recorded event order starts
  `["quality", "code-commit"]`.

### Conventions

Gate functions and process runners are injected only at the narrow boundary under test; real
worktree contract and Git behavior are retained wherever mutation ordering is the contract. The
argument-spy test deliberately does **not** patch the decider's behavior — it wraps the real one —
because a stub would hide the exact defect it exists to catch. It also plants file-level onboarding
for the planted wrapper, since the wrapper is a changed source file as far as closeout's
missing-onboarding check is concerned.

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

### Todos

No durable follow-up is recorded.

## Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md`
has no entries).

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external documentation is needed for these repository-local regressions. | — | — |

## Repo-Internal References

The suite proves the adapter and its production closeout call sites together.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `CodeQualityGateTests` covers all three gate statuses, invocation, worktree import authority, the `--diff-base` argument, the scrubbed wrapper environment, bounded failures, and interpreter selection. | L39-L236 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| The argument spy proves both closeout entry points pass the checkout path, not the repository name. | L239-L294 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| Closeout integration tests prove zero mutation on failure and quality-before-commit on success. | L296-L357 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| The adapter under test: the three status constants plus wrapper-presence applicability and the preview that reports them. | L13-L78 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |
| `quality_environment`, whose `git_environment()` base the selector test asserts. | L157-L173 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |
| The unannotated call sites the spy guards, both passing `contract.code_worktree` and `diff_base=contract.code_base_commit`. | L283-L287; L585-L593 | [closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| `GIT_REPOSITORY_SELECTOR_ENV` — the eight names the selector test plants and then requires absent — and `git_environment`, which removes them. | L24-L64 | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |

## Cross-Repo References

The tests operate on repository-local temporary fixtures, but the behavior they pin is explicitly
about other repositories: a bare temp checkout stands in for a consuming repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A checkout with no wrapper is reported as `wrapper-unavailable` rather than silently skipped, which is the consuming-repository case. | L67-L83 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |

## Update History

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
  `run_strict_code_quality_gate`) and added rows for `quality_environment` (L157-L173) and for
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
