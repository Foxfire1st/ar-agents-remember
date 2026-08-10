# mcp/src/agents_remember/worktrees/modules/code_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/code_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash |  `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |  2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

This module is the narrow policy and process adapter that makes the project-owned source-quality
wrapper a mandatory, fail-closed gate before a worktree closeout or integration lands a code
commit, and it owns the altitude routing: leaf edges run the change-set-scoped `--targeted`
contract, and master integration runs the full wrapper once, memory-capped, inside
`worktree_integrate` itself (260731-EFA-L17).

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
the payload also carries `mode` (`targeted` or `full`) and, for a full plan, a `memoryCap`
block (`capBytes`, `policy` = `orchestration.qualityGate.memoryCapBytes`, `mechanism`):

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

`run_strict_code_quality_gate(code_worktree, *, diff_base="", plan=QualityGatePlan(), invocation="closeout-staged", runner=run_subprocess)`
requires the wrapper to exist (else `RuntimeError`), selects an interpreter, executes the
current worktree's `agents_remember.code_quality.check` under the planned mode, and raises with a
bounded output tail (`FAILURE_OUTPUT_LINES` = last 40 lines) on any non-zero result. Success
returns `{"required": True, "status": GATE_ENFORCED, "passed": True, "command": ..., "diffBase": ..., "mode": ...}`,
plus `memoryCap` for full runs. The concrete command and invocation label come from
`_gate_command_parts` (lines 220-248); a full run without `memory_cap_bytes` is refused
(RuntimeError naming the settings key), and an over-cap kill (returncode -9 / shell 137) is
named by `_gate_failure_message` (lines 249-275).

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

`_gate_command(diff_base, mode=..., memory_cap_bytes=...)` (lines 42-66) renders the same string
into the payload's `command` key so a reader can rerun exactly what ran — targeted mode appends
`--targeted`, full mode wraps the command via `memory_cap.plan_capped_command` — and `diffBase`
reports the base on its own key. In the `enforced` state both the preview and the successful run
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
  `--diff-base` when the base is non-empty); full mode appends no narrowing flag but REQUIRES
  `memory_cap_bytes` — a full run without a settings-owned cap is refused. No threshold-enforcement
  flag is required or accepted.
- **A closeout must pass the leaf's own base commit.** Dropping `diff_base` at a call site does not
  weaken the gate, it makes it unpassable: the 100% changed-lines floor would then be measured
  against `main`. Both directions are failures of the same rule — the base the gate measures against
  must be the base the leaf branched from.
- Failure output is bounded to the last 40 lines while preserving the actionable exit status.
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
| `quality_wrapper_path` / `requires_strict_code_quality` decide applicability from the checkout, and `code_quality_gate_preview` reports one of the three `status` values plus the planned `mode`/`memoryCap`. | `quality_wrapper_path`, `requires_strict_code_quality`, `code_quality_gate_preview`, `QualityGatePlan` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:37-41; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:67-76; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:77-146; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:29-35 |
| `run_strict_code_quality_gate` executes the planned contract (targeted or full+capped), refuses on a missing wrapper or a cap-less full run, and raises with the bounded `_failure_output` tail; success reports `command`, `diffBase`, `mode`, and `memoryCap` for full runs. | `run_strict_code_quality_gate`, `_gate_command_parts`, `_gate_failure_message`, `_failure_output` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:162-219; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:220-248; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:249-275; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:329-333 |
| `quality_python` walks the interpreter chain through `_git_common_dir`, which uses `run_git`; `quality_environment` builds from `git_environment()`, puts this worktree's `mcp/src` first on `PYTHONPATH`, and names the invoking altitude. | `quality_python`; `quality_environment`; `_git_common_dir` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:276-293; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:294-318; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:319-328 |
| Both closeout call sites pass `contract.code_worktree`, `diff_base=contract.code_base_commit`, and the leaf targeted plan — the preview path, and the apply path where `requires_strict_code_quality` guards `_gate_staged_code` and `commit_if_dirty` follows it. | `closeout_preview_payload`, `closeout_result` | mcp/src/agents_remember/worktrees/modules/closeout.py:357-427; mcp/src/agents_remember/worktrees/modules/closeout.py:938-1035 |
| Regressions cover all three statuses, the targeted/full modes, cap-less full refusals, cap-kill naming, the checkout-not-name argument at both call sites, that the leaf base reaches the wrapper as `--diff-base`, that the spawned wrapper gets no repository selectors, worktree source precedence, bounded failures, interpreter selection, and mutation ordering. | `CodeQualityGateTests`, `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_closeout_quality_gate.py:49-423; mcp/tests/test_worktree_closeout_quality_gate.py:424-555 |
| The staging regressions added with `_gate_staged_code`: `_ScopeRecordingGate` (the wrapper's own `derive_scope` + `ruff check` pair, so the scope assertion is not a mock), `CloseoutGateSeesCreatedFilesTests`, `TaskWorktreePreconditionTests`, `ConflictedIndexTests` and `RetryStagesWhatAFirstRunWouldTests`. | `_ScopeRecordingGate`; `CloseoutGateSeesCreatedFilesTests`; `TaskWorktreePreconditionTests`; `ConflictedIndexTests`; `RetryStagesWhatAFirstRunWouldTests` | mcp/tests/test_worktree_closeout_quality_gate.py:605-641; mcp/tests/test_worktree_closeout_quality_gate.py:642-753; mcp/tests/test_worktree_closeout_quality_gate.py:791-905; mcp/tests/test_worktree_closeout_quality_gate.py:906-965; mcp/tests/test_worktree_closeout_quality_gate.py:966-1025 |
| The one git runner this module calls, and the scrubber `quality_environment` builds from: `run_git` and `git_environment` both drop `GIT_REPOSITORY_SELECTOR_ENV`, and `run_git` carries the local/remote/metadata timeout classes. | `run_git`, `git_environment` | mcp/src/agents_remember/kernel/git_command.py:76-82; mcp/src/agents_remember/kernel/git_command.py:85-151 |
| `test_the_closeout_gate_resolves_the_common_dir_of_the_worktree_it_was_given` points `GIT_DIR` at a decoy repository and proves `_git_common_dir` still answers for the worktree it was handed. | `test_the_closeout_gate_resolves_the_common_dir_of_the_worktree_it_was_given` | mcp/tests/test_git_command.py:347-370 |
| `SingleRunnerTests` sweeps the package's AST and fails if any module spawns `git` itself or defines a second runner. | `SingleRunnerTests` | mcp/tests/test_git_command.py:393-465 |
| The contributor documentation states the same three-state contract for consuming repositories. | `### Closeout` | CONTRIBUTING.md:238-245 |

## Cross-Repo References

This gate acts on whatever code worktree closeout hands it, which for a consuming repository is
that repository's checkout rather than this one.

| Finding | Anchor | Source |
| --- | --- | --- |
| Applicability is decided by the presence of the wrapper in the target checkout. | `requires_strict_code_quality` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:67-76 |
| The preview reports `wrapper-unavailable` when the target checkout lacks the wrapper. | `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:77-146 |

## Update History

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
