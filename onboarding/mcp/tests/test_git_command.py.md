# mcp/tests/test_git_command.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_git_command.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-14T12:13:26+02:00 |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca` |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
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
spot cannot masquerade as a clean tree. 41 tests across nine classes, all green.

## Code Commentary

### Logic

The module docstring (cit:(["The one git runner"], mcp/tests/test_git_command.py:1-15)) states the suite's own precondition, and it is the part most easily
misread. `mcp/tests/conftest.py` pops every name in `GIT_REPOSITORY_SELECTOR_ENV` out of
`os.environ` at import. That strip is correct for fixture safety and stays — but it also meant no
test anywhere could observe a call site that failed to strip them, because the harness had already
removed the hazard. So cit:([`_selectors`], mcp/tests/test_git_command.py:146-157) builds a dict pointing all eight selectors at a
decoy repository, and every redirection test re-**sets** them inside its own `patch.dict` scope,
deliberately defeating the conftest strip. `DecoyRepositoryTests` even asserts the re-set took
(cit:(["self.assertTrue(set(GIT_REPOSITORY_SELECTOR_ENV).issubset(os.environ))"], mcp/tests/test_git_command.py:182-182)) before exercising
production. These tests pass because production strips, not because the harness did.

cit:([`DecoyRepositoryTests`], mcp/tests/test_git_command.py:160-216) is the core suite. `_init()`/cit:([`_commit`], mcp/tests/test_git_command.py:81-85) build two real
throwaway repositories, `real` and `decoy`.

- L158-L183 drives `commit_if_dirty(real, ...)` — the function closeout actually runs — with the
  selectors exported, then asserts *both* halves: the real branch advanced and holds the new
  content, and `head_commit(decoy)` is unchanged with no `real.txt` in the decoy. Checking only the
  real repository would still pass if the write were duplicated into the decoy.
- L184-L203 is the read half: `run_git(real, ["rev-parse", "HEAD"])` and `["ls-files"]` must report
  the real repository's head and tracked set, not the decoy's.
- L204-L213 asserts `git_environment()` removes every name the production tuple lists, and that
  `PATH` survives — a scrub that removed too much would leave git unrunnable.

cit:([`RunnerContractTests`], mcp/tests/test_git_command.py:219-315) covers the rest of the runner's contract. L220-L238 proves
`input_text` reaches `git patch-id --stable` and that without it stdin is `DEVNULL` (under the stdio
MCP transport the inherited descriptor is the JSON-RPC request pipe). L240-L256 proves an undecodable
path is carried through `errors="surrogateescape"` rather than raising. L258-L278 is the
consolidation's precondition: a deliberately slow alias must outlive the runner's former hard-coded
five seconds, and `GIT_LOCAL_TIMEOUT_SECONDS` must be at least 60. L280-L290 proves raising the
default did not amount to removing the bound — an explicit `timeout=1` still raises
`subprocess.TimeoutExpired`. L292-L296 pins `GIT_REMOTE_TIMEOUT_SECONDS < GIT_LOCAL_TIMEOUT_SECONDS`.
*Which* band each command gets is not asserted here; that is `TimeoutClassTests` below.

L298-L315 constructs a real pre-commit hook that writes raw byte `0x81` and fails. The first assertion
proves the shared runner still carries that byte as the surrogate `\udc81`, preserving the path-safe
decode contract. The second path calls the worktree facade and proves its raised diagnostic contains
the literal escape and can be encoded by `json.dumps(..., ensure_ascii=False)`, pinning the exact MCP
serialization failure that interrupted L22 closeout without weakening the internal Git representation.

cit:([`RemoteBranchStallTests`], mcp/tests/test_git_command.py:357-388) patches `cleanup.run_git` and proves the two remote-talking
calls in `delete_remote_branch_if_present` — which previously ran with no timeout at all — now
degrade a stall into the already-handled `{"remote_deleted": False, "reason": "remote-unreachable"}`
result, and that both calls carry `GIT_REMOTE_TIMEOUT_SECONDS` as a keyword.

cit:([`QualityGateGitTests`], mcp/tests/test_git_command.py:352-414) covers the call sites that run from the `pre-push` hook, where git
itself exports `GIT_DIR`. L331-L346 proves `quality_check.git_ls_files` and
`diff_coverage.run_git` derive their scope from the repository they were pointed at. L347-L371
proves `_git_common_dir` resolves the given worktree's common dir, and returns `None` for a plain
directory rather than falling through to the decoy `GIT_DIR` names. L372-L380 and L381-L392 prove
both wrappers still convert failure — a non-repository and an `OSError` from the runner — into their
own typed `DiffScopeError` / `ScopeError` rather than an empty scope that would certify nothing.

#### The sweep, and the guard on the sweep

The AST sweep lives at **module level** in four small helpers, not inside the test class, which is
what makes it exercisable on synthetic sources rather than only on the real tree:

- cit:([`_spawn_aliases`], mcp/tests/test_git_command.py:88-101) collects the bare names this module bound to a spawn via
  `from subprocess import run [as x]`, reading `alias.asname or alias.name` for any
  `ImportFrom(module="subprocess")` whose name is in `SPAWN_FUNCTIONS` (L59:
  `run`/`Popen`/`check_output`/`check_call`/`call`). Resolving aliases **per module** is what keeps
  an unrelated local `run` from being reported.
- cit:([`_spawn_calls`], mcp/tests/test_git_command.py:104-121) returns every call that starts a child process, matching either
  `subprocess.<attr>` or one of those bare names.
- cit:([`_spawns_git`], mcp/tests/test_git_command.py:124-133) reads the argv list literal's head and returns
  `PurePosixPath(head.value).name == "git"`, so `/usr/bin/git` counts as git.
- cit:([`_passes_env`], mcp/tests/test_git_command.py:136-143) requires `keyword.arg == "env"`. A `**kwargs` splat parses as
  `arg is None` and is explicitly **not** proof — the sweep sees the splat, never its contents.

cit:([`SingleRunnerTests`], mcp/tests/test_git_command.py:417-489) is the decay guard built on them. `_package_modules()`
(cit:([`_package_modules`], mcp/tests/test_git_command.py:489-494))
skips `package_data` because those are runtime assets executed outside this process.
cit:([`test_no_module_spawns_git_with_the_ambient_environment`], mcp/tests/test_git_command.py:490-509) reports any spawn that
`_spawns_git` and not `_passes_env`; cit:([`test_only_the_kernel_module_defines_a_git_runner`], mcp/tests/test_git_command.py:511-528)
asserts the set of modules that spawn git is exactly `["kernel/git_command.py"]`. The class docstring
(cit:([`SingleRunnerTests`], mcp/tests/test_git_command.py:417-489)) states the reach exactly rather than assuming it, and names the one remaining hole.

cit:([`SingleRunnerGuardReachTests`], mcp/tests/test_git_command.py:492-571) is the guard on the guard, and it exists for a specific
reason: `SingleRunnerTests` passes by reporting an **empty offender list**, which is also exactly what
it reports when the sweep cannot see the offender. A hole does not look like a failure, it looks like
a clean tree. cit:([`_offenders`], mcp/tests/test_git_command.py:542-550) reruns the guard's own composition
(`_spawns_git(node) and not _passes_env(node)` over `_spawn_calls(tree)`) against a source string, so
each bypass form can be planted and the expected line numbers asserted. Three previously-open blind
spots are closed and pinned here:

- L489-L494 / L495-L498 — `from subprocess import run` and `... as spawn`, then a bare call. Missed
  before, because the sweep required a `subprocess.<attr>` attribute access: dropping the module
  prefix at the import was enough to disappear from it.
- L499-L504 — `/usr/bin/git`. Missed before, because the head had to be the literal `"git"`, so
  pinning a binary by absolute path exempted the call from the guard.
- L505-L511 — `subprocess.run(["git", ...], **kw)`. Missed before, because a splat's
  `keyword.arg is None` was counted as an `env=`.

The rest fix the sweep's shape in both directions: L512-L521 asserts all five `SPAWN_FUNCTIONS`
entry points are swept (offenders at lines 2-5, not just `run`); L522-L527 asserts a named `env=`
still **clears** the sweep, because a guard that cannot be satisfied the intended way gets suppressed
instead of obeyed; L528-L531 pins `gitk` and `/usr/bin/gh` as non-offenders (this is what leaves
`landing.py`'s `gh` spawn outside the sweep, and why `test_landing.py` asserts its environment
directly); L532-L538 pins a module's own `def run(argv)` as not a spawn.

L539-L549 `test_a_computed_argv_is_this_sweeps_documented_blind_spot` is the one that asserts a **`[]`**
on purpose: `argv = ['git', 'status']` then `subprocess.run(argv)` is invisible to a call-site scan.
The limitation is stated, not closed, and this test is what stops the documented limitation from
quietly ceasing to be the true one.

cit:([`TimeoutClassTests`], mcp/tests/test_git_command.py:574-684) asserts that the timeout class belongs to the **command**, not to the
module holding the call. cit:([`_recorder`], mcp/tests/test_git_command.py:624-643) is a `run_git` stand-in recording
`(command, timeout)` per call, and its `timeout` is a **required keyword-only** parameter on purpose:
a call site that leaves the band to the runner's default fails the recorder rather than quietly
recording that default.

- L582-L605 — `git_facts.read_git_facts` puts its three ref reads on `GIT_METADATA_TIMEOUT_SECONDS`
  while `status --porcelain` keeps `GIT_LOCAL_TIMEOUT_SECONDS`, because it stats the whole work tree
  and is not a constant-time read. The failure it prevents is concrete: four probes on the local
  bound let one `resolve_context` — which runs on essentially every tool call — sit for twenty
  minutes behind a held index lock, with no cancellation path for the MCP client.
- L606-L629 — `git_freshness.read_branch_freshness` classes each command by what it does:
  `branch --show-current` and `rev-parse --abbrev-ref <b>@{upstream}` at the metadata band,
  `rev-list --left-right --count` at the local band because it walks history.
- L630-L655 `test_one_command_means_one_bound_across_the_kernel` — the drift this leaf exists to end.
  It drives `cross_repo.git_branch` / `git_head_or_empty` and `git_facts.read_git_facts` through
  separate recorders and asserts the bounds agree on the two commands they share
  (`branch --show-current`, `rev-parse HEAD`), which were 30s in `cross_repo.py` and 300s in
  `git_facts.py`. Two answers for one command inside `kernel/` is how six runners got here.
- L656-L662 — the metadata band is the shortest of the three: a constant-time read that has not
  returned in 30s is blocked, not busy.

cit:([`BenchmarkRunnerEnvironmentTests`], mcp/tests/test_git_command.py:663-791) exists because the benchmark runner's git step is invisible to the sweep from the
outside: `benchmarks/runner_modules/commands.py` routes every command through the shared kernel
`run_git` — it spawns nothing of its own — and it holds the most destructive argv in the package
(`clone`, `checkout --detach`, `reset --hard`, `clean -fdx`). L672-L689 runs a real `reset --hard`
against `real` with the selectors pointing at `decoy` and asserts the decoy's uncommitted work
survives; L690-L702 proves `repo_has_commit` answers from the named repository.
cit:([`RunnerArgvTests`], mcp/tests/test_git_command.py:857-886) pins the argv-facing half of the same module: the repository is named to
git itself and not only through `cwd`, a `work_dir` aims the process while the repository stays the
subject, and `core.longpaths=true` really reaches git.

### Conventions

Real throwaway repositories under `tempfile.TemporaryDirectory`, never a stubbed
`CompletedProcess`, wherever the property under test is "which repository did git touch". Doubles
appear only where the boundary is a stall, an `OSError` that cannot be provoked reliably
(`RemoteBranchStallTests`, and the `OSError` arm at L381-L392), or a `run_git` call whose *keyword*
is the thing under test (`TimeoutClassTests`). Production symbols are imported, never restated: the
whole import block at L45-L53 — `GIT_BULK_REMOTE_TIMEOUT_SECONDS`, `GIT_LOCAL_TIMEOUT_SECONDS`,
`GIT_METADATA_TIMEOUT_SECONDS`, `GIT_REMOTE_TIMEOUT_SECONDS`, `GIT_REPOSITORY_SELECTOR_ENV`,
`git_environment`, `run_git` — comes
from `kernel.git_command`, so the suite cannot drift from the inventory and bounds it exercises.
Every test docstring or leading comment names the concrete defect it encodes rather than restating
the assertion.

Two seams exist purely so the tests can be tested: cit:([`_offenders`], mcp/tests/test_git_command.py:542-550) replays the guard's own
sweep composition against a source string, and cit:([`_recorder`], mcp/tests/test_git_command.py:624-643) makes `timeout` a required
keyword so an unclassed call site fails rather than silently recording the default. Both are only
possible because the four sweep helpers sit at module level
(cit:([`_spawn_aliases`], mcp/tests/test_git_command.py:88-101)) rather than inside
`SingleRunnerTests`.

### Invariants And Boundaries

- Every redirection test must keep re-setting the selectors inside its own scope. A test that
  relies on the conftest strip proves nothing about production and silently becomes vacuous.
- Both halves of a write test are required: the real repository advanced **and** the decoy did not.
- The AST guards are package-wide properties and must stay guards, not allowlists. If a module
  legitimately composes its git argv, it belongs in a direct suite like
  `BenchmarkRunnerEnvironmentTests`, not in an exemption list.
- **An empty offender list is ambiguous by construction**, so any change to a sweep helper
  (cit:([`_spawn_aliases`], mcp/tests/test_git_command.py:88-101)) owes a matching plant in `SingleRunnerGuardReachTests`. Widening the sweep without one
  produces a guard that reports zero offenders on a tree that has one, which is indistinguishable
  from success.
- The computed-argv blind spot is **deliberate and pinned**, not deferred: `_spawns_git` reads the
  argv list literal at the call site, so `argv = [...]; subprocess.run(argv)` is invisible.
  `test_a_computed_argv_is_this_sweeps_documented_blind_spot`
  (cit:([`test_a_computed_argv_is_this_sweeps_documented_blind_spot`], mcp/tests/test_git_command.py:602-610))
  asserts that `[]`. Closing it
  means deleting that test; leaving it open means any module in that shape owes a direct suite.
- The sweep matches argv heads named `git` only. A non-git spawn that nevertheless resolves a
  repository through git — currently just `landing.py`'s `gh pr list` — is outside it by design
  (cit:([`test_a_program_that_merely_starts_with_git_is_not_git`], mcp/tests/test_git_command.py:597-599)) and carries its own assertion
  in `test_landing.py`.
- Timeout bands are asserted per command, not per module. A command called from two kernel modules
  must get one bound cit:([`test_one_command_means_one_bound_across_the_kernel`], mcp/tests/test_git_command.py:693-717).
- The slow-command test asserts real elapsed time above five seconds; it is intentionally not a
  mocked clock, because the failure it prevents was a real five-second cut-off on every integrate.
- This suite owns the runner's process boundary only. Route-index census parsing, carryover
  semantics, and the quality gate's own verdicts are covered by their own suites.

### Todos

None known. The suite is the guard for the L3 single-runner consolidation and carries no deferred
work of its own. The computed-argv gap in the AST sweep is **not** a todo: it is a stated limit with
a test asserting it
(cit:([`test_a_computed_argv_is_this_sweeps_documented_blind_spot`], mcp/tests/test_git_command.py:602-610))
and a direct suite covering the one module in that shape.

## Docs References

The resolved `system/sources.md` registry declares no `Domain Documentation` entries, so there was
no live documentation source to check for this file. Git's environment-variable semantics are
exercised directly against a real `git` binary here rather than asserted from documentation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This suite is written against production symbols rather than copies of them, so nearly every claim
above is anchored in another file in this repository. The runner under test is the kernel module;
the call sites are the ones the consolidation moved onto it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The runner under test: the eight-name `GIT_REPOSITORY_SELECTOR_ENV` tuple, the timeout constants, `git_environment()`, and `run_git()` with `env=`, `stdin=DEVNULL`, surrogateescape decoding and a per-call `timeout`. | `GIT_REPOSITORY_SELECTOR_ENV` | mcp/src/agents_remember/kernel/git_command.py:33-42; mcp/src/agents_remember/kernel/git_command.py:85-151 |
| The conftest strip this suite deliberately defeats: it imports the production selector tuple and pops each name from `os.environ` at import. | "from agents_remember.kernel.git_command import GIT_REPOSITORY_SELECTOR_ENV" | mcp/tests/conftest.py:101-101 |
| `commit_if_dirty` and `head_commit` — the closeout write path driven by the decoy commit test. | `commit_if_dirty` | mcp/src/agents_remember/worktrees/modules/git.py:126-131 |
| The gate's own git wrappers route through the shared runner and convert failure into typed domain errors: `_git` (which owns the conversion for all three callers) and `run_git` raising `DiffScopeError`, and `git_ls_files` raising `ScopeError`. | `DiffScopeError` | mcp/src/agents_remember/code_quality/diff_coverage.py:39-40; mcp/src/agents_remember/code_quality/check.py:35-39; mcp/src/agents_remember/code_quality/scope.py:44-53 |
| The per-command timeout bands `TimeoutClassTests` asserts: the three metadata-band ref reads plus the local-band `status --porcelain`. | `TimeoutClassTests` | mcp/tests/test_git_command.py:550-660 |
| The freshness reads classed by what they do — metadata for the two ref lookups, local for the history walk. | `read_branch_freshness` | mcp/src/agents_remember/kernel/git_freshness.py:56-65; mcp/src/agents_remember/kernel/git_freshness.py:98-112 |
| The other half of `test_one_command_means_one_bound_across_the_kernel`: `git_branch` / `git_head_or_empty` on the metadata band, the two commands it shares with `git_facts`. | `git_branch` | mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:21-29 |
| The one non-git spawn the sweep deliberately does not cover (`gh pr list` with `env=git_environment()`), asserted instead by `test_landing.py`. | `_pr_for` | mcp/src/agents_remember/worktrees/modules/landing.py:93-150 |
| The two remote-talking calls: `_remote_git` applies `GIT_REMOTE_TIMEOUT_SECONDS` and turns a stall into `None`, which `delete_remote_branch_if_present` and `_push_branch_deletion` report as `remote-unreachable`. | `_remote_git` | mcp/src/agents_remember/worktrees/modules/cleanup.py:155-166 |
| The benchmark runner the AST sweep cannot see: `run_git_command` and `repo_has_commit` route every command through the shared `run_git` (with `work_dir` and per-command timeout), so no spawn is visible outside the kernel. | `run_git_command` | mcp/src/agents_remember/benchmarks/runner_modules/commands.py:21-42 |
| `test_ambient_git_repository_selectors_cannot_redirect_the_census` covers the same eight selectors from the consumer side, so selector coverage exists at both the runner and the census boundary. | `test_ambient_git_repository_selectors_cannot_redirect_the_census` | mcp/tests/test_route_index.py:592-640 |
| The worktree facade keeps raw surrogateescape inside the runner and sanitizes only failed-command diagnostics before they cross the MCP transport. | `_transport_safe_git_diagnostic` | mcp/src/agents_remember/worktrees/modules/git.py:18-29 |

## Cross-Repo References

The suite runs entirely inside `agents-remember` against a local `git` binary and throwaway
repositories. No sibling repository or external service participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## R39 Required Git Probe

The linked-worktree repository probe now uses the shared required Git command boundary. A plain
directory or failed probe raises instead of returning an optional common-directory value that a
caller could silently treat as no policy.

## R43 Repository-Identity Refusal

The selector-isolation regression now requires the precise `not a git repository` refusal for a
plain directory while hostile `GIT_DIR` selectors point at a decoy. This keeps the test bound to
the repository-identity failure rather than a generic Git-command wrapper message.

## Update History

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
