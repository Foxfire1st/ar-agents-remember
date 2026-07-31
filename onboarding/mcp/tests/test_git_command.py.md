# mcp/tests/test_git_command.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_git_command.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T20:52+02:00                     |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7` |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_git_command.py` is the regression matrix for `run_git` in
`mcp/src/agents_remember/kernel/git_command.py` — the package's now-singular Git subprocess
runner. Six near-identical private `_run_git` copies were consolidated onto it, and the copies
had drifted: only the kernel's stripped the `GIT_DIR`-family repository-selection variables, so
with `GIT_DIR` exported the same logical `git commit` landed in the real repository from one call
site and in whatever repository `GIT_DIR` named from another. This suite proves the surviving
runner strips them, asserts **per command** which of the three timeout bands it gets, holds the
package to exactly one Git spawner so a seventh copy cannot reappear — and, because that last guard
passes by reporting an empty list, plants every known bypass form against its own sweep so a blind
spot cannot masquerade as a clean tree. 32 tests across eight classes, all green.

## Code Commentary

### Logic

The module docstring (L1-L15) states the suite's own precondition, and it is the part most easily
misread. `mcp/tests/conftest.py` pops every name in `GIT_REPOSITORY_SELECTOR_ENV` out of
`os.environ` at import. That strip is correct for fixture safety and stays — but it also meant no
test anywhere could observe a call site that failed to strip them, because the harness had already
removed the hazard. So `_selectors()` (L137-L148) builds a dict pointing all eight selectors at a
decoy repository, and every redirection test re-**sets** them inside its own `patch.dict` scope,
deliberately defeating the conftest strip. `DecoyRepositoryTests` even asserts the re-set took
(`self.assertTrue(set(GIT_REPOSITORY_SELECTOR_ENV).issubset(os.environ))`, L171) before exercising
production. These tests pass because production strips, not because the harness did.

`DecoyRepositoryTests` (L151-L207) is the core suite. `_init()`/`_commit()` (L62-L76) build two real
throwaway repositories, `real` and `decoy`.

- L154-L178 drives `commit_if_dirty(real, ...)` — the function closeout actually runs — with the
  selectors exported, then asserts *both* halves: the real branch advanced and holds the new
  content, and `head_commit(decoy)` is unchanged with no `real.txt` in the decoy. Checking only the
  real repository would still pass if the write were duplicated into the decoy.
- L180-L198 is the read half: `run_git(real, ["rev-parse", "HEAD"])` and `["ls-files"]` must report
  the real repository's head and tracked set, not the decoy's.
- L200-L207 asserts `git_environment()` removes every name the production tuple lists, and that
  `PATH` survives — a scrub that removed too much would leave git unrunnable.

`RunnerContractTests` (L210-L287) covers the rest of the runner's contract. L211-L229 proves
`input_text` reaches `git patch-id --stable` and that without it stdin is `DEVNULL` (under the stdio
MCP transport the inherited descriptor is the JSON-RPC request pipe). L231-L247 proves an undecodable
path is carried through `errors="surrogateescape"` rather than raising. L249-L269 is the
consolidation's precondition: a deliberately slow alias must outlive the runner's former hard-coded
five seconds, and `GIT_LOCAL_TIMEOUT_SECONDS` must be at least 60. L271-L281 proves raising the
default did not amount to removing the bound — an explicit `timeout=1` still raises
`subprocess.TimeoutExpired`. L283-L287 pins `GIT_REMOTE_TIMEOUT_SECONDS < GIT_LOCAL_TIMEOUT_SECONDS`.
*Which* band each command gets is not asserted here; that is `TimeoutClassTests` below.

`RemoteBranchStallTests` (L290-L321) patches `cleanup.run_git` and proves the two remote-talking
calls in `delete_remote_branch_if_present` — which previously ran with no timeout at all — now
degrade a stall into the already-handled `{"remote_deleted": False, "reason": "remote-unreachable"}`
result, and that both calls carry `GIT_REMOTE_TIMEOUT_SECONDS` as a keyword.

`QualityGateGitTests` (L324-L386) covers the call sites that run from the `pre-push` hook, where git
itself exports `GIT_DIR`. L327-L341 proves `quality_check.git_ls_files` and
`diff_coverage.run_git` derive their scope from the repository they were pointed at. L343-L366
proves `_git_common_dir` resolves the given worktree's common dir, and returns `None` for a plain
directory rather than falling through to the decoy `GIT_DIR` names. L368-L375 and L377-L386 prove
both wrappers still convert failure — a non-repository and an `OSError` from the runner — into their
own typed `DiffScopeError` / `ScopeError` rather than an empty scope that would certify nothing.

#### The sweep, and the guard on the sweep

The AST sweep lives at **module level** in four small helpers, not inside the test class, which is
what makes it exercisable on synthetic sources rather than only on the real tree:

- `_spawn_aliases(tree)` (L79-L92) collects the bare names this module bound to a spawn via
  `from subprocess import run [as x]`, reading `alias.asname or alias.name` for any
  `ImportFrom(module="subprocess")` whose name is in `SPAWN_FUNCTIONS` (L59:
  `run`/`Popen`/`check_output`/`check_call`/`call`). Resolving aliases **per module** is what keeps
  an unrelated local `run` from being reported.
- `_spawn_calls(tree)` (L95-L112) returns every call that starts a child process, matching either
  `subprocess.<attr>` or one of those bare names.
- `_spawns_git(node)` (L115-L124) reads the argv list literal's head and returns
  `PurePosixPath(head.value).name == "git"`, so `/usr/bin/git` counts as git.
- `_passes_env(node)` (L127-L134) requires `keyword.arg == "env"`. A `**kwargs` splat parses as
  `arg is None` and is explicitly **not** proof — the sweep sees the splat, never its contents.

`SingleRunnerTests` (L389-L459) is the decay guard built on them. `_package_modules()` (L414-L419)
skips `package_data` because those are runtime assets executed outside this process.
`test_no_module_spawns_git_with_the_ambient_environment` (L421-L440) reports any spawn that
`_spawns_git` and not `_passes_env`; `test_only_the_kernel_module_defines_a_git_runner` (L442-L459)
asserts the set of modules that spawn git is exactly `["kernel/git_command.py"]`. The class docstring
(L390-L412) states the reach exactly rather than assuming it, and names the one remaining hole.

`SingleRunnerGuardReachTests` (L462-L540) is the guard on the guard, and it exists for a specific
reason: `SingleRunnerTests` passes by reporting an **empty offender list**, which is also exactly what
it reports when the sweep cannot see the offender. A hole does not look like a failure, it looks like
a clean tree. `_offenders(source)` (L474-L481) reruns the guard's own composition
(`_spawns_git(node) and not _passes_env(node)` over `_spawn_calls(tree)`) against a source string, so
each bypass form can be planted and the expected line numbers asserted. Three previously-open blind
spots are closed and pinned here:

- L483-L487 / L489-L491 — `from subprocess import run` and `... as spawn`, then a bare call. Missed
  before, because the sweep required a `subprocess.<attr>` attribute access: dropping the module
  prefix at the import was enough to disappear from it.
- L493-L497 — `/usr/bin/git`. Missed before, because the head had to be the literal `"git"`, so
  pinning a binary by absolute path exempted the call from the guard.
- L499-L504 — `subprocess.run(["git", ...], **kw)`. Missed before, because a splat's
  `keyword.arg is None` was counted as an `env=`.

The rest fix the sweep's shape in both directions: L506-L514 asserts all five `SPAWN_FUNCTIONS`
entry points are swept (offenders at lines 2-5, not just `run`); L516-L520 asserts a named `env=`
still **clears** the sweep, because a guard that cannot be satisfied the intended way gets suppressed
instead of obeyed; L522-L524 pins `gitk` and `/usr/bin/gh` as non-offenders (this is what leaves
`landing.py`'s `gh` spawn outside the sweep, and why `test_landing.py` asserts its environment
directly); L526-L531 pins a module's own `def run(argv)` as not a spawn.

L533-L540 `test_a_computed_argv_remains_the_documented_blind_spot` is the one that asserts a **`[]`**
on purpose: `argv = ['git', 'status']` then `subprocess.run(argv)` is invisible to a call-site scan.
The limitation is stated, not closed, and this test is what stops the documented limitation from
quietly ceasing to be the true one.

`TimeoutClassTests` (L543-L653) asserts that the timeout class belongs to the **command**, not to the
module holding the call. `_recorder()` (L555-L573) is a `run_git` stand-in recording
`(command, timeout)` per call, and its `timeout` is a **required keyword-only** parameter on purpose:
a call site that leaves the band to the runner's default fails the recorder rather than quietly
recording that default.

- L575-L597 — `git_facts.read_git_facts` puts its three ref reads on `GIT_METADATA_TIMEOUT_SECONDS`
  while `status --porcelain` keeps `GIT_LOCAL_TIMEOUT_SECONDS`, because it stats the whole work tree
  and is not a constant-time read. The failure it prevents is concrete: four probes on the local
  bound let one `resolve_context` — which runs on essentially every tool call — sit for twenty
  minutes behind a held index lock, with no cancellation path for the MCP client.
- L599-L621 — `git_freshness.read_branch_freshness` classes each command by what it does:
  `branch --show-current` and `rev-parse --abbrev-ref <b>@{upstream}` at the metadata band,
  `rev-list --left-right --count` at the local band because it walks history.
- L623-L647 `test_one_command_means_one_bound_across_the_kernel` — the drift this leaf exists to end.
  It drives `cross_repo.git_branch` / `git_head_or_empty` and `git_facts.read_git_facts` through
  separate recorders and asserts the bounds agree on the two commands they share
  (`branch --show-current`, `rev-parse HEAD`), which were 30s in `cross_repo.py` and 300s in
  `git_facts.py`. Two answers for one command inside `kernel/` is how six runners got here.
- L649-L653 — the metadata band is the shortest of the three: a constant-time read that has not
  returned in 30s is blocked, not busy.

`BenchmarkRunnerEnvironmentTests` (L656-L693) exists because of the computed-argv limit.
`benchmarks/runner_modules/commands.py` composes its argv through `git_command()`, so the AST sweep
cannot see it — and it holds the most destructive argv in the package (`clone`,
`checkout --detach`, `reset --hard`, `clean -fdx`). L664-L680 runs a real `reset --hard` against
`real` with the selectors pointing at `decoy` and asserts the decoy's uncommitted work survives;
L682-L693 proves `repo_has_commit` answers from the named repository.

### Conventions

Real throwaway repositories under `tempfile.TemporaryDirectory`, never a stubbed
`CompletedProcess`, wherever the property under test is "which repository did git touch". Doubles
appear only where the boundary is a stall, an `OSError` that cannot be provoked reliably
(`RemoteBranchStallTests`, and the `OSError` arm at L377-L386), or a `run_git` call whose *keyword*
is the thing under test (`TimeoutClassTests`). Production symbols are imported, never restated: the
whole import block at L42-L49 — `GIT_LOCAL_TIMEOUT_SECONDS`, `GIT_METADATA_TIMEOUT_SECONDS`,
`GIT_REMOTE_TIMEOUT_SECONDS`, `GIT_REPOSITORY_SELECTOR_ENV`, `git_environment`, `run_git` — comes
from `kernel.git_command`, so the suite cannot drift from the inventory and bounds it exercises.
Every test docstring or leading comment names the concrete defect it encodes rather than restating
the assertion.

Two seams exist purely so the tests can be tested: `_offenders()` (L474-L481) replays the guard's own
sweep composition against a source string, and `_recorder()` (L555-L573) makes `timeout` a required
keyword so an unclassed call site fails rather than silently recording the default. Both are only
possible because the four sweep helpers sit at module level (L79-L134) rather than inside
`SingleRunnerTests`.

### Invariants And Boundaries

- Every redirection test must keep re-setting the selectors inside its own scope. A test that
  relies on the conftest strip proves nothing about production and silently becomes vacuous.
- Both halves of a write test are required: the real repository advanced **and** the decoy did not.
- The AST guards are package-wide properties and must stay guards, not allowlists. If a module
  legitimately composes its git argv, it belongs in a direct suite like
  `BenchmarkRunnerEnvironmentTests`, not in an exemption list.
- **An empty offender list is ambiguous by construction**, so any change to a sweep helper
  (L79-L134) owes a matching plant in `SingleRunnerGuardReachTests`. Widening the sweep without one
  produces a guard that reports zero offenders on a tree that has one, which is indistinguishable
  from success.
- The computed-argv blind spot is **deliberate and pinned**, not deferred: `_spawns_git` reads the
  argv list literal at the call site, so `argv = [...]; subprocess.run(argv)` is invisible.
  `test_a_computed_argv_remains_the_documented_blind_spot` (L533-L540) asserts that `[]`. Closing it
  means deleting that test; leaving it open means any module in that shape owes a direct suite.
- The sweep matches argv heads named `git` only. A non-git spawn that nevertheless resolves a
  repository through git — currently just `landing.py`'s `gh pr list` — is outside it by design
  (`test_a_program_that_merely_starts_with_git_is_not_git`, L522-L524) and carries its own assertion
  in `test_landing.py`.
- Timeout bands are asserted per command, not per module. A command called from two kernel modules
  must get one bound (`test_one_command_means_one_bound_across_the_kernel`, L623-L647).
- The slow-command test asserts real elapsed time above five seconds; it is intentionally not a
  mocked clock, because the failure it prevents was a real five-second cut-off on every integrate.
- This suite owns the runner's process boundary only. Route-index census parsing, carryover
  semantics, and the quality gate's own verdicts are covered by their own suites.

### Todos

None known. The suite is the guard for the L3 single-runner consolidation and carries no deferred
work of its own. The computed-argv gap in the AST sweep is **not** a todo: it is a stated limit with
a test asserting it (L533-L540) and a direct suite covering the one module in that shape.

## Docs References

The resolved `system/sources.md` registry declares no `Domain Documentation` entries, so there was
no live documentation source to check for this file. Git's environment-variable semantics are
exercised directly against a real `git` binary here rather than asserted from documentation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This suite is written against production symbols rather than copies of them, so nearly every claim
above is anchored in another file in this repository. The runner under test is the kernel module;
the call sites are the ones the consolidation moved onto it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The runner under test: the eight-name `GIT_REPOSITORY_SELECTOR_ENV` tuple, the three timeout constants, `git_environment()`, and `run_git()` with `env=`, `stdin=DEVNULL`, surrogateescape decoding and a per-call `timeout`. | L24-L33; L53-L55; L58-L64; L67-L96 | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| The conftest strip this suite deliberately defeats: it imports the production selector tuple and pops each name from `os.environ` at import. | L34-L39 | [conftest.py](agents-remember/mcp/tests/conftest.py) |
| `commit_if_dirty` and `head_commit` — the closeout write path driven by the decoy commit test. | L29-L30; L81-L86 | [git.py](agents-remember/mcp/src/agents_remember/worktrees/modules/git.py) |
| `_git_common_dir` decides which repository the closeout quality gate certifies, and returns `None` rather than falling through to an inherited selector. | L176-L183 | [code_quality_gate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/code_quality_gate.py) |
| The gate's own git wrappers route through the shared runner and convert failure into typed domain errors: `_git` (which owns the conversion for all three callers) and `run_git` raising `DiffScopeError`, and `git_ls_files` raising `ScopeError`. | diff_coverage L97-L98; L137-L163; L166-L173; check L55-L56; L132-L149 | [diff_coverage.py](agents-remember/mcp/src/agents_remember/code_quality/diff_coverage.py); [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |
| The per-command timeout bands `TimeoutClassTests` asserts: the three metadata-band ref reads plus the local-band `status --porcelain`. | L67; L80; L84; L87 | [git_facts.py](agents-remember/mcp/src/agents_remember/kernel/git_facts.py) |
| The freshness reads classed by what they do — metadata for the two ref lookups, local for the history walk. | L44; L70; L101 | [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |
| The other half of `test_one_command_means_one_bound_across_the_kernel`: `git_branch` / `git_head_or_empty` on the metadata band, the two commands it shares with `git_facts`. | L21-L29; L32-L38 (bands at L26; L35) | [cross_repo.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/cross_repo.py) |
| The one non-git spawn the sweep deliberately does not cover (`gh pr list` with `env=git_environment()`), asserted instead by `test_landing.py`. | L104-L130 | [landing.py](agents-remember/mcp/src/agents_remember/worktrees/modules/landing.py) |
| The two remote-talking calls: `_remote_git` applies `GIT_REMOTE_TIMEOUT_SECONDS` and turns a stall into `None`, which `delete_remote_branch_if_present` and `_push_branch_deletion` report as `remote-unreachable`. | L108-L119; L122-L133; L136-L142 | [cleanup.py](agents-remember/mcp/src/agents_remember/worktrees/modules/cleanup.py) |
| The benchmark runner the AST sweep cannot see: `run_command` and `repo_has_commit` each pass `env=git_environment()` explicitly, and `git_command()` composes the argv that hides them from a list-literal scan. | L9-L36; L39-L40; L43-L52 | [commands.py](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/commands.py) |
| `test_ambient_git_repository_selectors_cannot_redirect_the_census` covers the same eight selectors from the consumer side, so selector coverage exists at both the runner and the census boundary. | L592-L640 | [test_route_index.py](agents-remember/mcp/tests/test_route_index.py) |

## Cross-Repo References

The suite runs entirely inside `agents-remember` against a local `git` binary and throwaway
repositories. No sibling repository or external service participates.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T21:46+02:00 — 260731-EFA-L3 curator: re-verified against the restructured file; the
  sidecar created below (same leaf) described a version of it that no longer exists, and being a new
  sidecar it was exempt from the body gate, so nothing would have flagged it. **Every** line range
  was re-derived and all but the module docstring (L1-L15) had moved: `_selectors` L70-L81 → L137-L148,
  the re-set assertion L104 → L171, `DecoyRepositoryTests` L84-L140 → L151-L207 (members L154-L178 /
  L180-L198 / L200-L207), `_init`/`_commit` L53-L67 → L62-L76, `RunnerContractTests` L143-L220 →
  L210-L287 (members L211-L229 / L231-L247 / L249-L269 / L271-L281 / L283-L287),
  `RemoteBranchStallTests` L223-L254 → L290-L321, `QualityGateGitTests` L257-L319 → L324-L386 (the
  old L301-L319 was two tests, now L368-L375 and L377-L386), `SingleRunnerTests` L322-L402 → L389-L459
  (`_package_modules` L352-L358 → L414-L419; the two tests → L421-L440 and L442-L459),
  `BenchmarkRunnerEnvironmentTests` L405-L442 → L656-L693 (members L664-L680 / L682-L693), and the
  `kernel.git_command` import block L39-L45 → L42-L49 (it now also imports
  `GIT_METADATA_TIMEOUT_SECONDS`, `git_environment` and `run_git`). Content that was outright false:
  `_spawns()` (L336-L346) no longer exists — the sweep is four module-level helpers, `_spawn_aliases`
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
