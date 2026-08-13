# mcp/src/agents_remember/worktrees/modules/code_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/code_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T14:32+02:00 |
| lastVerifiedCommitHash |  `b2de030c1b52f02a4543619d23ccd8e44ecac6df`|
| lastVerifiedCommitDate |  2026-08-13T14:51:34+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

This module is the narrow policy and process adapter that makes the project-owned source-quality
wrapper a mandatory, fail-closed gate before a worktree closeout or integration lands a code
commit, and it owns the altitude routing: leaf edges run the change-set-scoped `--targeted`
contract, and master integration runs the full wrapper once with host-managed
RAM and swap by default inside `worktree_integrate` itself
(260731-EFA-L17/L24). An explicit settings cap remains available for constrained
CI; neither path changes pytest's literal `-n=auto` configuration.

It also owns the latest completed gate transcript. The caller supplies a `QualityGateTarget`
containing both the checkout and its worktree enclosure; every completed run atomically replaces
`<worktree_group>/reports/test-results.md`, and success returns that path while failure publishes
the same full output before raising. Because publication occurs only after the subprocess returns,
an interrupted retry leaves the preceding completed report intact.

**It is no longer scoped to one repository.** Until 260731-EFA-L1 the decider read
`repo_name == "agents-remember"`, so for every consuming repository — the product's actual audience
— the gate the product documents as mandatory was a no-op. Availability of the wrapper now decides,
not the repository's name.

## Code Commentary

### Logic

`quality_wrapper_path(code_worktree)` is the single place the wrapper's location is spelled:
`<checkout>/mcp/src/agents_remember/code_quality/check.py` (`QUALITY_WRAPPER`).

`requires_strict_code_quality(code_worktree, *, code_would_commit)` returns
`code_would_commit and quality_wrapper_path(code_worktree).is_file()`. Note the first parameter is
a **checkout path**, not a repository name — see the boundary note below.

`code_quality_gate_preview(code_worktree, *, code_would_commit, diff_base="", plan=QualityGatePlan())`
reports which of three states this gate is in, via the `status` key; since 260731-EFA-L17
the payload also carries `mode` (`targeted` or `full`). Full plans carry a
`memoryPolicy` block (`mode`, `pytestProcesses=auto`, `swap=host-managed`), and
an explicitly capped plan additionally carries `memoryCap` (`capBytes`, policy,
mechanism):

| `status` | Constant | Meaning |
| --- | --- | --- |
| `no-code-commit` | `GATE_NO_CODE_COMMIT` | Nothing would commit, so nothing to gate. |
| `wrapper-unavailable` | `GATE_WRAPPER_UNAVAILABLE` | Code would commit, but this checkout carries no wrapper. The reason string names `QUALITY_WRAPPER` and states the commit **is not quality-checked**. |
| `enforced` | `GATE_ENFORCED` | The wrapper runs before the commit; `command` is `_gate_command(diff_base, mode=..., memory_cap_bytes=...)` — for the leaf contract `python -m agents_remember.code_quality.check --targeted --diff-base <base>` — and `diffBase` carries the base on its own key. Since 260731-EFA-L4 the `reason` also names the staging step; since L17 it states that the leaf contract is `--targeted` and that the full wrapper runs once per master at the master integration gate, not at leaf closeout. |

`wrapper-unavailable` is a *reported* state, not a silent skip: closeout still proceeds, and the
payload says plainly that the code commit was not quality-checked and why. That is the deliberate
replacement for the old behavior, which returned the same `required: False` for a consuming
repository as for "nothing to commit" and explained it with the misleading reason "no Agents
Remember code commit would be created".

`run_strict_code_quality_gate(QualityGateTarget(code_worktree, worktree_group), *, diff_base="", plan=QualityGatePlan(), invocation="closeout-staged", runner=run_subprocess)`
requires the wrapper to exist (else `RuntimeError`), selects an interpreter, executes the
current worktree's `agents_remember.code_quality.check` under the planned mode, writes the complete
captured transcript through `_write_test_results_report`, and raises with both the stable report
path and a bounded output tail (`FAILURE_OUTPUT_LINES` = last 40 lines) on any non-zero result.
Success returns `reportPath` beside the existing command/scope/memory-cap evidence. The concrete
command and invocation label still come from `_gate_command_parts`; a full run without
`memory_cap_bytes` executes the plain wrapper, while an over-cap kill remains named by
`_gate_failure_message` only when an explicit cap was configured.

`run_subprocess` captures the merged quality transcript as UTF-8 with replacement for undecodable
bytes. A tool emitting one non-UTF-8 byte therefore cannot abort the adapter before the stable
report is written; the replacement is confined to diagnostic output and does not alter source or
gate status.

`_validated_quality_gate_plan` owns defaulting and the closed `targeted`/`full` plus
`local`/`dagger` validation before command construction. Keeping that policy in one helper makes
the execution coordinator smaller without adding a fallback executor.

`test_results_report_path` fixes the location at `reports/test-results.md` under the supplied
worktree group. `_write_test_results_report` renders status, invocation, mode, diff base, exit code,
UTC start/finish, elapsed seconds, exact shell command, applicable cap facts, and the full output,
then publishes with the shared `atomic_write_text` primitive. It creates no timestamped siblings.

### The Index Is The Scope, And This Function Does Not Own It (260731-EFA-L4)

The wrapper derives its scope from the index — `derive_scope` uses `git ls-files`, `diff_coverage`
diffs against the tracked tree — so **what is staged when this runs is what gets certified**. Since
260731-EFA-L4 closeout stages the whole task worktree first (`closeout._gate_staged_code`), which is
what makes the gate's scope and the commit's content one set; before that, a file the task *created*
went into the commit with no rail of the gate having read it.

This module deliberately does not do the staging and does not describe it. `runner` is a public
parameter and closeout is not the only caller this signature admits, so the failure message states
only what is true of every caller — "code" — and **does not
say the staging was undone, because closeout does not undo it**. This function certifies the index
it is handed and says nothing about how it came to look that way. The refusals, the reset and the
`add -A` all live in `closeout.py`, where the disposable-worktree precondition that makes staging
safe is actually established.

### `diff_base` Is What Makes The Coverage Floor Passable

`diff_base` must be the leaf's recorded base commit, and both closeout paths pass
`contract.code_base_commit`. When it is non-empty the gate appends `["--diff-base", diff_base]` to
`python -m agents_remember.code_quality.check`; when it is empty the flag is omitted and the wrapper
falls back through `diff_coverage.resolve_base` to `AR_GATE_DIFF_BASE` / the pull request base /
`@{upstream}` / `origin/HEAD` / `main`.

That fallback is the wrong measurement for a leaf. The wrapper's per-diff floor demands **100%**
coverage of the changed statements and branch arcs, so measuring against `main` charges a leaf for
every change on the whole integration branch rather than for its own diff — a gate no leaf can pass,
which is exactly as useless as a gate that cannot fail. CI keeps the `main` default on purpose: a
pull request genuinely is measured against `main`, a leaf closeout is measured against the leaf.

`_gate_command(diff_base, mode=..., memory_cap_bytes=...)` renders the same string
into the payload's `command` key so a reader can rerun exactly what ran — targeted mode appends
`--targeted`; full mode runs the plain wrapper when the cap is absent and otherwise wraps it via
`memory_cap.plan_capped_command` — and `diffBase` reports the base on its own key. In the
`enforced` state both the preview and the successful run
carry both keys; the two non-enforced preview states carry `command: ""` and no `diffBase`,
because nothing would run.

### Interpreter Selection And Import Precedence

`quality_python` prefers the worktree virtualenv, then the linked primary clone's shared
virtualenv, then the active server interpreter. `quality_environment` (lines 294-318) always puts
the current worktree's `mcp/src` first on `PYTHONPATH`, so a shared interpreter cannot measure the
primary clone by mistake, and it names the invoking altitude through `AR_QUALITY_INVOCATION`
(`closeout-staged`, `leaf-integration`, `master-integration`).

`quality_environment` builds that environment from `kernel.git_command.git_environment()`, **not**
from `dict(os.environ)`, so the eight `GIT_DIR`-family repository selectors
(`GIT_REPOSITORY_SELECTOR_ENV`) are dropped before the wrapper is spawned. The wrapper is not an
inert subprocess: it derives its own scope from `git ls-files` and its diff base from `merge-base`,
and closeout runs from paths where `GIT_DIR` can be exported. Passing the selectors straight
through was safe only because every git call inside that child strips them itself — which makes
this gate's correctness, *which repository gets certified before a code commit*, rest on the good
behaviour of a process this one cannot see. Nothing else about the environment changes: this
worktree's `mcp/src` still leads `PYTHONPATH`, any inherited `PYTHONPATH` still follows it, and
`PATH` survives (without it the wrapper cannot start).

On non-Windows hosts the same environment normalizes `TMPDIR`, `TMP`, and `TEMP` to `/tmp`. This
keeps concurrent quality scratch process-local and Unix-domain harness-control socket paths short
when a WSL process inherited Windows temp paths. The durable latest-run transcript remains under
the enclosure's `reports/` directory; only ephemeral scratch moves. Native Windows retains the
inherited temp variables.

`_git_common_dir` — the middle step of that interpreter chain — runs
`git rev-parse --path-format=absolute --git-common-dir` through
`agents_remember.kernel.git_command.run_git`, the package's single git runner, rather than through
its own `subprocess.run`. `run_git` strips the `GIT_DIR`-family repository selectors
(`GIT_REPOSITORY_SELECTOR_ENV`) from the child environment; without that, an exported `GIT_DIR`
answers with *its* common dir, and this value decides which repository's `.venv` the closeout
quality gate then runs from. A directory that is not a repository still yields `None` (non-zero exit)
rather than falling through to whatever `GIT_DIR` names.

### Conventions

The interpreter search is necessary linked-worktree support: linked worktrees intentionally may not
carry their own `.venv`. It is an ordered authority chain, not a command fallback or an escape from
the project-owned wrapper.

`status` is the machine-readable field; `reason` is prose for a human reading the closeout payload.
Callers should branch on `status`, not on `required` alone — `required: False` now covers two very
different situations.

### Invariants And Boundaries

- **The deciders take a checkout `Path`, never a repository name.** `contract.repo_name` is a
  `str`, `contract` is unannotated in `closeout.py`, and `Path`-vs-`str` is not caught there by
  Pyright. Handing a name in makes `quality_wrapper_path` build a relative path off the process
  CWD, which is not a file, so the gate silently never runs. `test_worktree_closeout_quality_gate.py`
  spies on the actual argument for exactly this reason.
- The only deliberate skip is a closeout that would not create a code commit. A checkout without
  the wrapper is *reported*, not skipped silently.
- A missing wrapper, missing interpreter, or non-zero wrapper result refuses before closeout
  mutation.
- The leaf contract is the only sanctioned narrowing: targeted mode appends `--targeted` (and
  `--diff-base` when the base is non-empty); full mode appends no narrowing flag and runs
  host-managed when `memory_cap_bytes` is absent. No threshold-enforcement flag is required or
  accepted, and no xdist worker override is introduced.
- **A closeout must pass the leaf's own base commit.** Dropping `diff_base` at a call site does not
  weaken the gate, it makes it unpassable: the 100% changed-lines floor would then be measured
  against `main`. Both directions are failures of the same rule — the base the gate measures against
  must be the base the leaf branched from.
- Failure output is bounded to the last 40 lines while preserving the actionable exit status.
- The bounded exception is only a notification surface; `reports/test-results.md` retains the
  complete stdout/stderr transcript for both pass and fail and is replaced atomically only after a
  run completes.
- Captured subprocess text is always decoded as UTF-8 with replacement so malformed diagnostic
  bytes cannot suppress the completed-run report.
- On non-Windows hosts, quality scratch uses `/tmp`; this must not redirect or weaken the
  enclosure-owned `reports/test-results.md` durability contract.
- **This module never stages, resets or restores.** The index it is handed is the scope it
  certifies; producing that index is the caller's job, and the failure message must stay true for a
  caller that did no staging at all. Do not add a "staging was reverted" claim here — closeout does
  not revert it.
- Gate applicability must stay a property of the checkout, not of any repository identity. Do not
  reintroduce a name-based branch.
- Every git call this module makes goes through `kernel.git_command.run_git`. Spawning `git`
  here again reintroduces the inherited-`GIT_DIR` defect this gate is most exposed to, and
  `test_git_command.py::SingleRunnerTests` fails the build if a second runner appears.
- **The environment handed to the wrapper carries no repository selectors.** `quality_environment`
  must keep building from `git_environment()`; reverting it to `dict(os.environ)` re-exports
  `GIT_DIR` and friends into a child that runs `git ls-files` and `merge-base` to decide what it
  certifies. `test_worktree_closeout_quality_gate.py::CodeQualityGateTests::test_the_gate_hands_the_wrapper_no_repository_selectors`
  asserts the selectors are absent and that `PYTHONPATH` ordering and `PATH` are untouched.

### Todos

- `wrapper-unavailable` is currently reported and permitted. If a consuming repository should be
  able to *require* a gate it cannot run, that is a policy decision this module does not make.

## Docs References

No external Domain Documentation source is configured for this memory repo (`system/sources.md`
has no entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for this repository-local gate. | — | — |

## Repo-Internal References

Closeout owns sequencing, while the quality wrapper owns the actual Ruff, Pyright, Radon, pytest,
coverage, and CRAP checks.

| Finding | Anchor | Source |
| --- | --- | --- |
| `quality_wrapper_path` / `requires_strict_code_quality` decide applicability from the checkout, and `code_quality_gate_preview` reports one of the three statuses plus planned mode, executor, and memory policy. | `quality_wrapper_path`; `requires_strict_code_quality`; `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:37-41; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:100-107; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:110-177 |
| `run_strict_code_quality_gate` executes the planned contract, atomically publishes the complete latest transcript, exposes `reportPath` on success, and names it before raising on failure. | `QualityGateTarget`, `test_results_report_path`, `run_strict_code_quality_gate`, `_write_test_results_report`, `_gate_failure_message` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:56-61; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:85-87; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:251-352; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:355-413; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:507-533 |
| `run_subprocess` captures merged output as UTF-8 with replacement so an undecodable diagnostic byte cannot prevent report publication. | `run_subprocess` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:234-248 |
| `quality_python` walks the interpreter chain through `_git_common_dir`, which uses `run_git`; `quality_environment` builds from `git_environment()`, puts this worktree's `mcp/src` first on `PYTHONPATH`, names the invoking altitude, and uses `/tmp` for non-Windows scratch. | `quality_python`; `quality_environment`; `_git_common_dir` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:536-551; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:554-584; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:587-594 |
| Both closeout call sites pass `contract.code_worktree`, `diff_base=contract.code_base_commit`, and the leaf targeted plan — the preview path, and the apply path where `requires_strict_code_quality` guards `_gate_staged_code` and `commit_if_dirty` follows it. | `closeout_preview_payload`, `closeout_result` | mcp/src/agents_remember/worktrees/modules/closeout.py:372-461; mcp/src/agents_remember/worktrees/modules/closeout.py:1037-1131 |
| Regressions cover all three statuses, targeted/full modes, host-managed and explicit-cap full runs, cap-kill naming, checkout-not-name arguments, exact leaf base forwarding, repository-selector scrubbing, source precedence, bounded failures, interpreter selection, and mutation ordering. | `CodeQualityGateTests`, `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_quality_gate_runner.py:19-486; mcp/tests/test_worktree_closeout_quality_gate.py:55-257 |
| The staging regressions added with `_gate_staged_code`: `_ScopeRecordingGate` (the wrapper's own `derive_scope` + `ruff check` pair, so the scope assertion is not a mock), `CloseoutGateSeesCreatedFilesTests`, `TaskWorktreePreconditionTests`, `ConflictedIndexTests` and `RetryStagesWhatAFirstRunWouldTests`. | `_ScopeRecordingGate`; `CloseoutGateSeesCreatedFilesTests`; `TaskWorktreePreconditionTests`; `ConflictedIndexTests`; `RetryStagesWhatAFirstRunWouldTests` | mcp/tests/test_worktree_closeout_quality_gate.py:360-395; mcp/tests/test_worktree_closeout_quality_gate.py:398-504; mcp/tests/test_worktree_closeout_quality_gate.py:658-781; mcp/tests/test_worktree_closeout_quality_gate.py:784-842; mcp/tests/test_worktree_closeout_quality_gate.py:848-911 |
| The one git runner this module calls, and the scrubber `quality_environment` builds from: `run_git` and `git_environment` both drop `GIT_REPOSITORY_SELECTOR_ENV`, and `run_git` carries the local/remote/metadata timeout classes. | `run_git`, `git_environment` | mcp/src/agents_remember/kernel/git_command.py:76-82; mcp/src/agents_remember/kernel/git_command.py:85-151 |
| `test_the_closeout_gate_resolves_the_common_dir_of_the_worktree_it_was_given` points `GIT_DIR` at a decoy repository and proves `_git_common_dir` still answers for the worktree it was handed. | `test_the_closeout_gate_resolves_the_common_dir_of_the_worktree_it_was_given` | mcp/tests/test_git_command.py:410-433 |
| `SingleRunnerTests` sweeps the package's AST and fails if any module spawns `git` itself or defines a second runner. | `SingleRunnerTests` | mcp/tests/test_git_command.py:393-465 |
| The contributor documentation states the same three-state contract for consuming repositories. | `### Closeout` | CONTRIBUTING.md:264-273 |

## Cross-Repo References

This gate acts on whatever code worktree closeout hands it, which for a consuming repository is
that repository's checkout rather than this one.

| Finding | Anchor | Source |
| --- | --- | --- |
| Applicability is decided by the presence of the wrapper in the target checkout. | `requires_strict_code_quality` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:149-156 |
| The preview reports `wrapper-unavailable` when the target checkout lacks the wrapper. | `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:110-177 |

## L23 Quality Environment Split

`quality_environment` keeps durable reports under the task enclosure while
routing ephemeral subprocess scratch to `/tmp/arq`. This separation preserves
operator-visible evidence and avoids the 103-byte Unix-socket address limit in
deep worktree/report paths.

## L23 Acceptance Interpretation

This module still owns the local wrapper plan and runner used for diagnostics and generic lifecycle
plumbing, but Agents Remember acceptance selects the pinned Dagger executor. Leaf/focused gates run
targeted mode and master integration runs full mode once; both require the exact task-derived diff
base. Host pytest or direct wrapper output cannot be promoted to acceptance evidence, and a failed
Dagger gate never falls back to this host path. Generated Dagger help is the executable public
argument contract.

## Update History
- 2026-08-13T14:32+02:00 — L23 final curator pass: re-read the reopened CONTRIBUTING claim and
  recorded that this host runner remains diagnostic/generic plumbing while Agents Remember
  acceptance is Dagger-only with explicit diff-base and no fallback. Verification remains
  closeout-owned.
- 2026-08-13T08:40+02:00 — L23 integration-gate repair: documented the extracted strict plan validator and preserved the fail-closed no-fallback executor boundary. Verification metadata remains closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented durable-report versus short-scratch ownership; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: recorded the
  host-managed full-gate default, explicit-cap-only wrapping, host swap,
  unchanged pytest `-n=auto`, and the `memoryPolicy` preview/result/report
  evidence. Verification metadata remains pinned until closeout stamps L24.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 citation maintenance: moved runner-policy proofs to
  `test_worktree_quality_gate_runner.py` and refreshed retained closeout ranges.

- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded deterministic UTF-8
  replacement for captured quality output and non-Windows `/tmp` normalization for ephemeral
  quality scratch. The enclosure-owned, atomically replaced `reports/test-results.md` contract is
  unchanged. Verification metadata remains pinned until governed closeout stamps the real code
  commit.

- 2026-08-11T17:50+02:00 — 260731-EFA-L19 curator: recorded the enclosure-owned,
  atomically replaced `reports/test-results.md` contract, full pass/fail transcript retention,
  stable `reportPath`, explicit checkout+enclosure target, and interrupted-run preservation.
  Verification metadata remains pinned until governed closeout stamps the L19 code commit.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the altitude-routed
  plan (`QualityGatePlan` mode `targeted`/`full`, mandatory cap for full runs,
  `memoryCap` payload, cap-kill naming, invocation labels) and refreshed the
  reference rows to the post-L17 source ranges. The "exactly one flag" invariant
  was replaced by the sanctioned-narrowing + required-cap statement. Verification
  metadata stays pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-04T15:32:44+02:00 — 260731-EFA-L6 S18-B08 curator: split wrapper applicability from preview reporting and regenerated both operative code-quality function extents.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 20 manifest citation findings plus the residual cross-repo row; scoped recheck clean.

- 2026-08-01T09:44+02:00 — 260731-EFA-L4 curator: this leaf's diff here is +13/-2 and both hunks are
  content. (1) The `enforced` preview `reason` changed from "strict project-owned quality wrapper
  runs before the code commit" to a three-line string that names the staging step; quoted the new
  text in the status table. (2) `run_strict_code_quality_gate` gained a docstring paragraph stating
  that the wrapper derives its scope from the index, that this function certifies the index it is
  handed and says nothing about how it came to look that way, and that the failure message
  deliberately does **not** claim the staging was undone because closeout does not undo it. Added
  the matching section and the invariant that this module never stages, resets or restores — the
  staging lives in `closeout._gate_staged_code`.
  **Citation repairs, all re-verified against the current files.** The two hunks moved everything
  below them: code_quality_gate.py L24-L78 → **L24-L82** (the `enforced` return block now ends at
  L82; L78 landed mid-`reason`), L96-L136 → **L100-L147** (`run_strict_code_quality_gate` is
  L100-L147; the old range started before its `def` and stopped before its return), L139-L183 →
  **L150-L194** (`quality_python` L150, `quality_environment` L168-L184, `_git_common_dir` ends at
  L194 — the old range began inside `run_strict_code_quality_gate` and stopped short of
  `_git_common_dir` entirely). closeout.py grew +188 lines: L283-L287 → **L289-L293** (the preview
  `code_quality_gate_preview(...)` call with `diff_base=contract.code_base_commit`) and L585-L594 →
  **L721-L730** (the apply preview call, `requires_strict_code_quality`, `_gate_staged_code`, and
  `commit_if_dirty` on L730). test_worktree_closeout_quality_gate.py grew +477: L39-L357 →
  **L49-L419** (`CodeQualityGateTests` L49 through the end of `CloseoutCodeQualityGateTests`), plus
  a **new row** for L422-L835, the staging regressions this leaf added. Re-verified unchanged and
  left as written: git_command.py L24-L96 and both test_git_command.py rows (L343-L366, L389-L459)
  — this leaf touches neither file — and cross-repo L24-L42, which still contains
  `requires_strict_code_quality`'s body. Verification metadata pinned until closeout stamps the L4
  commit.

- 2026-07-31T21:20+02:00 — 260731-EFA-L3 curator (second pass): after the entry below was written
  the fix worker changed `quality_environment` to build from `git_environment()` instead of
  `dict(os.environ)`, and the card still described only the `PYTHONPATH` ordering. Added the
  paragraph under "Interpreter Selection And Import Precedence" recording what that removes (the
  eight `GIT_REPOSITORY_SELECTOR_ENV` names) and why it matters here (the spawned wrapper resolves
  its own scope with `git ls-files` and its diff base with `merge-base`, so passing the selectors
  through made this gate's answer depend on a child stripping them itself), plus what deliberately
  does **not** change: `mcp/src` still leads `PYTHONPATH`, the inherited value still follows, `PATH`
  survives. Added the matching invariant naming
  `test_the_gate_hands_the_wrapper_no_repository_selectors`. Citation repairs, all verified against
  the current files: code_quality_gate.py L139-L182 → **L139-L183** (L182 stopped one line short of
  `_git_common_dir`'s `return Path(value) if value else None`); test_worktree_closeout_quality_gate.py
  L38-L335 → **L39-L357** (`CodeQualityGateTests` … `test_success_runs_quality_before_code_commit`,
  which now ends at L357); test_git_command.py **split into two rows** because the pair
  `L276-L299; L322-L402` no longer held either symbol —
  `test_the_closeout_gate_resolves_the_common_dir_of_the_worktree_it_was_given` is at **L343-L366**
  (L276-L299 landed in `RunnerContractTests`) and `class SingleRunnerTests` at **L389-L459**
  (L322-L402 covered `QualityGateGitTests` instead). Re-verified and kept unchanged: closeout.py
  L283-L287 (the preview call site with `diff_base=contract.code_base_commit`) and L585-L594
  (the apply call site plus `commit_if_dirty`) — closeout.py is untouched by this leaf;
  git_command.py L24-L96 (`GIT_REPOSITORY_SELECTOR_ENV` through the end of `run_git`);
  code_quality_gate.py L24-L78 and L96-L136; cross-repo L24-L42. The `diff_base` / `--diff-base`
  contract documented above remains current truth and remains attributable to leaf 2's `f3115ce`
  — `git log -S diff_base -- mcp/src/agents_remember/worktrees/modules/code_quality_gate.py`
  still returns that commit and no other.

- 2026-07-31T20:48+02:00 — 260731-EFA-L3 curator: rewrote the body for two facts it did not carry.
  (1) **`diff_base`.** Both deciders and both payloads take it — `code_quality_gate_preview(...,
  diff_base="")` and `run_strict_code_quality_gate(..., diff_base="")` — and the enforced command is
  `_gate_command(diff_base)`, i.e. `python -m agents_remember.code_quality.check --diff-base <base>`,
  not the bare command this card described. Added the "makes the coverage floor passable" section
  and replaced the "default wrapper command is used as-is" invariant, which was false as written.
  (2) **The one git runner.** `_git_common_dir` now calls
  `agents_remember.kernel.git_command.run_git` instead of spawning `git rev-parse` itself, so the
  `GIT_DIR`-family selectors are stripped before the probe that decides which repository's `.venv`
  the gate runs from. Citations: L15-L113 → three anchored rows (L24-L78 `quality_wrapper_path` …
  preview; L96-L136 `run_strict_code_quality_gate`; L139-L182 `quality_python`/`_git_common_dir`/
  `quality_environment`) after this leaf's +5/-8 lines moved everything below the import;
  closeout.py L283-L285 → L283-L287 and L583-L589 → L585-L594 so the ranges contain the
  `diff_base=contract.code_base_commit` arguments and `commit_if_dirty` the row names;
  test L38-L284 → L38-L335 to reach `test_success_runs_quality_before_code_commit`; cross-repo
  L22-L35 → L24-L42 so it contains `requires_strict_code_quality`'s body and not just its `def`.
  Added rows for `kernel/git_command.py` and the new `mcp/tests/test_git_command.py`.

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/src/agents_remember/worktrees/modules/code_quality_gate.py` and moved the lines this card
  cites, so the Citations column no longer pointed at the code its rows name. Corrected the ranges
  (L15-L117 → L15-L113; L24-L37 → L22-L35). The behaviour described is unchanged — the file's AST
  is identical to the base revision — this is a citation repair only. Verification metadata pinned
  until closeout stamps the L2 commit.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-31T04:28+02:00 — 260731-EFA-L1 removed the repository-name hard-code (L1-R10). The
  deciders now take the code worktree `Path` and gate on wrapper availability, so the gate applies
  to every consuming repository that carries the wrapper instead of only to `agents-remember`.
  Added `quality_wrapper_path`, the `GATE_ENFORCED` / `GATE_NO_CODE_COMMIT` /
  `GATE_WRAPPER_UNAVAILABLE` status constants, and a `status` key on both the preview and the
  successful run result; removed `AGENTS_REMEMBER_REPO` and the misleading "no Agents Remember code
  commit would be created" reason. Recorded the `Path`-not-name boundary because Pyright cannot
  catch that mistake at the unannotated closeout call sites. Verification metadata pinned to the
  pre-leaf source authority until closeout stamps the code commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: created the sidecar for mandatory
  pre-code-commit quality enforcement, linked-worktree interpreter selection, current-worktree
  import precedence, and fail-closed bounded error reporting. Verification remains blank until the
  new source is committed.
