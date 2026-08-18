# mcp/src/agents_remember/worktrees/modules/code_quality_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/code_quality_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T12:13:26+02:00 |
| lastVerifiedCommitHash |  `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b`|
| lastVerifiedCommitDate |  2026-08-18T03:31:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

This module is the narrow policy and process adapter that makes the project-owned source-quality
wrapper a mandatory, fail-closed lifecycle gate. Leaf closeout runs the change-set-scoped
`--targeted` contract exactly once before creating its commit; leaf integration reuses that
certified commit without invoking this runner again. Master integration runs the full wrapper once
with container-runtime-managed RAM and swap by default inside `worktree_integrate` itself
(260731-EFA-L17/L24). An explicit settings cap remains available for Dagger-owned lifecycle runs;
neither path changes pytest's literal `-n=auto` configuration.

It also owns the latest completed gate transcript. The caller supplies a `QualityGateTarget`
containing both the checkout and its worktree enclosure; every completed run atomically replaces
`<worktree_group>/reports/test-results.md`, and success returns that path while failure publishes
the same full output before raising. Because publication occurs only after the subprocess returns,
an interrupted retry leaves the preceding completed report intact.

Applicability has two explicit layers. A consumer repository opts in by carrying the integrated
adapter. Agents Remember additionally owns a self-policy: `requires_integrated_acceptance` makes
that adapter mandatory by repository identity, so deleting the wrapper cannot turn acceptance into
the permitted consumer `wrapper-unavailable` state.

## Code Commentary

### Logic

`quality_wrapper_path(code_worktree)` is the single place the wrapper's location is spelled:
`<checkout>/mcp/src/agents_remember/code_quality/check.py` (`QUALITY_WRAPPER`).

`requires_integrated_acceptance(repo_name)` names the self-policy repositories; currently only
`agents-remember` returns true. `requires_strict_code_quality(code_worktree, *,
code_would_commit, required_when_missing=False)` then requires a run when code would commit and
either policy marks the adapter mandatory or the checkout actually carries it. The checkout path
still selects the adapter bytes; repository identity only decides whether absence is legal.

`code_quality_gate_preview(code_worktree, *, code_would_commit, diff_base="", plan=QualityGatePlan())`
reports which of three states this gate is in, via the `status` key; since 260731-EFA-L17
the payload also carries `mode` (`targeted` or `full`). Full plans carry a
`memoryPolicy` block (`mode`, `pytestProcesses=auto`, `swap=container-host-managed`), and
an explicitly capped plan additionally carries `memoryCap` (`capBytes`, policy,
mechanism):

| `status` | Constant | Meaning |
| --- | --- | --- |
| `no-code-commit` | `GATE_NO_CODE_COMMIT` | Nothing would commit, so nothing to gate. |
| `wrapper-unavailable` | `GATE_WRAPPER_UNAVAILABLE` | Code would commit in a consumer repository whose policy permits no adapter, and the checkout carries none. Agents Remember never reaches this state because its self-policy refuses missing-wrapper candidates. |
| `enforced` | `GATE_ENFORCED` | The Dagger graph runs before the commit or master integration; `command` is the symbolic `dagger call quality` command with exact source/bundle placeholders, mode, diff base, and optional cap. `diffBase` carries the base on its own key. |

`wrapper-unavailable` remains a reported consumer state, not a silent skip. When
`required_when_missing=True`, preview raises before returning a payload, so the self repository's
candidate cannot delete `QUALITY_WRAPPER` to disable its own required gate.

`run_strict_code_quality_gate(QualityGateTarget(code_worktree, worktree_group), *, diff_base="", plan=QualityGatePlan(), invocation="closeout-staged")`
requires the wrapper to exist (else `RuntimeError`), validates Dagger as the only executor, and
hands the exact candidate to `run_clean_quality`. It writes the complete exported transcript
through `_write_test_results_report`, and raises with both the stable report
path and a bounded output tail (`FAILURE_OUTPUT_LINES` = last 40 lines) on any non-zero result.
Success returns `reportPath` beside the existing command/scope/memory-cap evidence. The concrete
command and invocation label still come from `_gate_command_parts`. Dagger is the sole acceptance
executor; when a cap is requested the refusal reports the Dagger inner-wrapper cap evidence.

`_validated_quality_gate_plan` owns defaulting and the closed `targeted`/`full` plus mandatory
`dagger` validation before command construction. `run_local_quality_diagnostic` refuses
immediately; there is no host command planner or fallback executor.

`test_results_report_path` fixes the location at `reports/test-results.md` under the supplied
worktree group. `_write_test_results_report` renders status, invocation, mode, diff base, exit code,
UTC start/finish, elapsed seconds, exact shell command, applicable cap facts, and the full output,
then publishes with the shared `atomic_write_text` primitive. It creates no timestamped siblings.

Added `recover_strict_code_quality_gate`, which recovers one exact passed Dagger generation from the published attestation and `clean-quality-results.json` after a caller crash.

### The Index Is The Scope, And This Function Does Not Own It (260731-EFA-L4)

The wrapper derives its scope from the index — `derive_scope` uses `git ls-files`, `diff_coverage`
diffs against the tracked tree — so **what is staged when this runs is what gets certified**. Since
260731-EFA-L4 closeout stages the whole task worktree first (`closeout._gate_staged_code`), which is
what makes the gate's scope and the commit's content one set; before that, a file the task *created*
went into the commit with no rail of the gate having read it.

This module deliberately does not do the staging and does not describe it. The failure message
states only what is true of every caller — "code" — and **does not
say the staging was undone, because closeout does not undo it**. This function certifies the index
it is handed and says nothing about how it came to look that way. The refusals, the reset and the
`add -A` all live in `closeout.py`, where the disposable-worktree precondition that makes staging
safe is actually established.

### `diff_base` Is What Makes The Coverage Floor Passable

`diff_base` must be the task's recorded base commit. Leaf closeout passes
`contract.code_base_commit`; master integration passes the recorded super base. The lifecycle
executor materializes a separate ancestry bundle and the exact staged candidate, then the Dagger
function refuses an empty or unprovable base.

Using the wrong base is the wrong measurement for a leaf. The wrapper's per-diff floor demands **100%**
coverage of the changed statements and branch arcs, so measuring against `main` charges a leaf for
every change on the whole integration branch rather than for its own diff — a gate no leaf can pass,
which is exactly as useless as a gate that cannot fail. GitHub PR validation does not invoke this
acceptance path; the lifecycle always supplies the task-derived base.

`_gate_command(diff_base, mode=..., memory_cap_bytes=...)` renders the symbolic Dagger call
into the payload's `command` key, including exact-candidate and ancestry-bundle placeholders,
mode, base, and optional cap. `diffBase` reports the base on its own key. In the
`enforced` state both the preview and the successful run
carry both keys; the two non-enforced preview states carry `command: ""` and no `diffBase`,
because nothing would run.

### Host Execution Refuses

`run_local_quality_diagnostic` is now an explicit refusal surface. The local interpreter chain,
host environment builder, systemd/rlimit command planning, and direct subprocess runner were
removed. The only executable path is `run_clean_quality`, which reconstructs the accepted
candidate inside the pinned Dagger graph.

### Conventions

`status` is the machine-readable field; `reason` is prose for a human reading the closeout payload.
Callers should branch on `status`, not on `required` alone — `required: False` now covers two very
different situations.

### Invariants And Boundaries

- Adapter discovery takes a checkout `Path`; self-policy discovery deliberately takes the
  repository name. These inputs are separate so policy cannot accidentally become a relative path.
- No-code closeout is skipped. A no-adapter consumer is reported. An Agents Remember candidate
  missing its self-owned wrapper is refused before memory quality, approval claim, or commit.
- A required missing wrapper, non-Dagger executor, or non-zero Dagger result refuses before
  irreversible closeout or integration mutation.
- The leaf contract is the only sanctioned narrowing: targeted mode is explicit in the Dagger
  command; full mode is explicit at master integration. No threshold-enforcement flag is required
  or accepted, and no xdist worker override is introduced.
- **A closeout must pass the leaf's own base commit.** Dropping `diff_base` at a call site does not
  weaken the gate, it makes it unpassable: the 100% changed-lines floor would then be measured
  against `main`. Both directions are failures of the same rule — the base the gate measures against
  must be the base the leaf branched from.
- Failure output is bounded to the last 40 lines while preserving the actionable exit status.
- The bounded exception is only a notification surface; `reports/test-results.md` retains the
  complete stdout/stderr transcript for both pass and fail and is replaced atomically only after a
  run completes.
- **This module never stages, resets or restores.** The index it is handed is the scope it
  certifies; producing that index is the caller's job, and the failure message must stay true for a
  caller that did no staging at all. Do not add a "staging was reverted" claim here — closeout does
  not revert it.
- Consumer opt-in remains checkout-derived, while the explicit self-repository policy remains
  identity-derived. Do not collapse either rule into the other.
- This module never builds or launches a host wrapper command. `run_clean_quality` owns exact
  candidate reconstruction and Dagger execution.

### Todos

None recorded.

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
| `quality_wrapper_path` / `requires_strict_code_quality` decide applicability from the checkout, and `code_quality_gate_preview` reports one of the three statuses plus planned mode, executor, and memory policy. | `quality_wrapper_path`; `requires_strict_code_quality`; `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:63-65; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:97-104; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:107-169 |
| `run_strict_code_quality_gate` executes the planned contract, atomically publishes the complete latest transcript, exposes `reportPath` on success, and names it before raising on failure. | `QualityGateTarget`; `test_results_report_path`; `run_strict_code_quality_gate`; `_write_test_results_report`; `_gate_failure_message` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:40-45; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:68-70; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:184-265; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:281-330; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:387-411 |
| The named local entry point refuses before resolving or executing a host wrapper. | `run_local_quality_diagnostic` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:338-348 |
| Both closeout call sites pass `contract.code_worktree`, `diff_base=contract.code_base_commit`, and the leaf targeted plan — the preview path, and the apply path where `requires_strict_code_quality` guards `_gate_staged_code` and `commit_if_dirty` follows it. | `closeout_preview_payload`, `closeout_result` | mcp/src/agents_remember/worktrees/modules/closeout.py:368-432; mcp/src/agents_remember/worktrees/modules/closeout.py:1070-1172 |
| Regressions cover all three statuses, targeted/full Dagger modes, container-managed and explicit-cap full runs, cap-kill naming, immediate host refusal, checkout-not-name arguments, exact leaf base forwarding, bounded failures, and mutation ordering. | `CodeQualityGateTests`, `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_closeout_quality_gate.py:62-591; mcp/tests/test_worktree_quality_gate_runner.py:15-465 |
| The staging regressions added with `_gate_staged_code`: `ScopeRecordingGate` (the wrapper's own `derive_scope` + `ruff check` pair, so the scope assertion is not a mock), `CloseoutGateSeesCreatedFilesTests`, `TaskWorktreePreconditionTests`, `ConflictedIndexTests` and `RetryStagesWhatAFirstRunWouldTests`. | `ScopeRecordingGate`; `CloseoutGateSeesCreatedFilesTests`; `TaskWorktreePreconditionTests`; `ConflictedIndexTests`; `RetryStagesWhatAFirstRunWouldTests` | mcp/tests/test_worktree_closeout_gate_scope.py:99-208; mcp/tests/test_worktree_closeout_quality_gate.py:808-931; mcp/tests/test_worktree_closeout_quality_gate.py:934-992; mcp/tests/test_worktree_closeout_quality_gate.py:998-1061 |
| The contributor documentation states the same three-state contract for consuming repositories. | `### Closeout` | CONTRIBUTING.md:248-258 |

## Cross-Repo References

This gate acts on whatever code worktree closeout hands it, which for a consuming repository is
that repository's checkout rather than this one.

| Finding | Anchor | Source |
| --- | --- | --- |
| Consumer opt-in is decided by the adapter in the target checkout; self-policy may separately require its presence. | `requires_integrated_acceptance`; `requires_strict_code_quality` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:98-100; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:103-116 |
| The preview reports `wrapper-unavailable` only when policy permits absence, and otherwise refuses. | `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:119-187 |

## L23 Acceptance Interpretation

This module owns only the pinned Dagger acceptance adapter. Leaf closeout runs targeted mode once;
leaf integration reuses that certified commit; master integration runs full mode once. Both
acceptance runs require the exact task-derived diff base. Host pytest and direct wrapper execution
are refused, a missing self-owned wrapper refuses, and a failed Dagger gate has no fallback.
Generated Dagger help is the executable public argument contract.

## R43 Fail-Closed Wording And Executor Proof

The runtime refusal now names a missing `self-owned wrapper`, matching repository-resolved policy.
The forcing suite also calls both command and memory-policy builders with a non-Dagger executor and
requires each to refuse with pinned-Dagger guidance; no local executor can be revived through a
lower-level builder.

## Update History

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added `recover_strict_code_quality_gate` and attestation-bound Dagger report recovery for crash-safe full-gate reuse. Verification remains closeout-owned.

- 2026-08-14T12:13:26+02:00 — R43 curator: reconciled self-owned-wrapper refusal wording and the
  new direct non-Dagger builder proof. Verification remains closeout-owned.

- 2026-08-14T11:24+02:00 — R39 curator: replaced the obsolete checkout-only/name-forbidden
  applicability claim with the two-layer policy: consumer adapter opt-in plus mandatory
  Agents Remember self-wrapper presence. Also recorded immediate host refusal and the single
  leaf-closeout/master-integration Dagger owners. Verification remains closeout-owned.

- 2026-08-14T09:37+02:00 — Reopened L23 cadence: clarified this runner's two accepting owners —
  targeted leaf closeout and full master integration — and the leaf-integration no-rerun boundary.
- 2026-08-14T05:26Z — L23 final curator: made Dagger-only acceptance and its inner-wrapper cap
  evidence explicit, and re-anchored the final failure formatter. Verification remains
  closeout-owned.
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
