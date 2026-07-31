# mcp/tests/test_worktree_closeout_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_closeout_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31T04:28+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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
| Adapter tests cover all three gate statuses, invocation, worktree import authority, bounded failures, and interpreter selection. | L38-L165 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| The argument spy proves both closeout entry points pass the checkout path, not the repository name. | L169-L222 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| Closeout integration tests prove zero mutation on failure and quality-before-commit on success. | L224-L284 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |
| The adapter under test: wrapper-presence applicability plus the three status constants. | L15-L112 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |
| The unannotated call sites the spy guards. | L283-L285; L583-L589 | [closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |

## Cross-Repo References

The tests operate on repository-local temporary fixtures, but the behavior they pin is explicitly
about other repositories: a bare temp checkout stands in for a consuming repository.

| Finding | Citations | Source Path |
| --- | --- | --- |
| A checkout with no wrapper is reported as `wrapper-unavailable` rather than silently skipped, which is the consuming-repository case. | L66-L82 | [test_worktree_closeout_quality_gate.py](agents-remember/mcp/tests/test_worktree_closeout_quality_gate.py) |

## Update History

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
