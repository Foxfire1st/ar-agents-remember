# pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `pyproject.toml`                           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T16:10+02:00                     |
| lastVerifiedCommitHash | `00e83791d4d21bf56fd5b3cc0af194bc5e28112a` |
| lastVerifiedCommitDate | 2026-07-31T05:07:07+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

Root `pyproject.toml` holds the source-checkout quality-tool configuration shared by the
MCP package source and tests. After 260731-EFA-L2 it is also the **declaration the gate
reads at run time**: the wrapper derives where the test suite lives from this file, and
every rule it enforces is selected here.

## Code Commentary

### `[tool.ruff]` — Target Version Reconciled With The Supported Floor

`target-version` is `py311`, not `py313`. `mcp/pyproject.toml` declares
`requires-python = ">=3.11"` and CI runs 3.11, 3.12 and 3.13, so a tool told to target
py313 offers rewrites the floor cannot execute. That was not hypothetical: seven
`# noqa: UP040 / UP046 / UP047` directives in `serving/conversation/` and
`observer/projection_inputs.py` carried the reason "Python 3.11 support" — PEP 695
`type` statements and generic syntax 3.11 does not parse. Pinning the target to the floor
makes Ruff agree with the package metadata, and those seven suppressions were deleted in
the same change because the rules no longer fire. **Raising this line again means putting
them back**, which is the visible cost the mismatch used to hide.

### `[tool.ruff.lint]` — Everything Is Armed, Nothing Is Deferred

`C901` is in `select`. It was absent while `[tool.ruff.lint.mccabe] max-complexity` was set
to 10, so the configured limit reported nothing.

`PLR0911`, `PLR0912`, `PLR0915` and `PLR0913` are **not** in `ignore`, and nothing anywhere
else softens them:

- The three `PLR09xx` codes used to be ignored "because Radon reports complexity pressure",
  deferring enforcement to the one tool that cannot enforce. Arming them with `C901`
  produced **67 offenders**. Those were first parked in `quality/complexity-baseline.txt`
  behind a shrink-only ratchet with a dated burn-down; **the developer overruled that**, all
  67 were refactored, and the baseline file, its module, its test and its gate step were
  deleted. There is no per-file ignore, `noqa` or allowlist for any of the four.
- `PLR0913` runs at Ruff's **default of 5 arguments** — there is no `max-args` override —
  which is the number the memory root's `system/coding-guidelines.md` already states. It
  used to be ignored with a comment deferring 293 findings. **274 of those were refactored
  outright**, introducing 163 parameter objects across the tree, including the verbatim
  27 → 24 → 25 keyword pass-through in `serving/terminal_opener.py` that the old comment
  blamed — now 4 → 5 → 4 through `TerminalLaunchRequest` / `SpawnProvenance` /
  `HostedSessionRuntime`.

Two ignores remain, and both are about readability rather than deferral:

- `E501` — Ruff format owns wrapping; long literals stay readable as-is.
- `PLR2004` — numeric parser/state-machine sentinels are clearer inline.

### `[tool.ruff.lint.per-file-ignores]` — The One Carve-Out, And Why It Cannot Widen

`"mcp/src/agents_remember/mcp/registration/*.py" = ["PLR0913"]`. This is the remaining 19 of
the original 293, and it is a category rather than a residue: in those modules **a parameter
list is not a call burden, it IS the published MCP input schema.** FastMCP derives each
tool's JSON schema from the Python signature, so the extraction PLR0913 asks for is a wire
change, not a refactor. Measured against the installed `mcp 1.28.1`:

```text
def flat(repo_id, task_name, leaf_id)  -> properties: [repo_id, task_name, leaf_id]; no $defs
def nested(args: SomeModel)            -> properties: [args];                        has $defs
```

A model-typed parameter does not flatten — it republishes the tool as a single nested
object, so `{"leaf_key": …}` becomes `{"seat": {"leaf_key": …}}` for every client, every row
of `docs/reference/mcp-tools.md`, and every flat-kwargs call in the `c-09` and `l-01` skills.
The memory root's `system/coding-guidelines.md` already exempts "intentionally centralized
declarations", and this directory is the whole of that category in this tree.

**The carve-out is self-limiting, not a hiding place.**
`mcp/tests/test_code_quality_check.py::ToolSignatureExemptionTests` walks the AST of every
file the pattern matches and fails if any function there is anything but a `@server.tool()`
declaration or the registrar that hosts them, **and fails if the pattern is widened or a
second `PLR0913` exemption is added anywhere.**

The test-file ignores (`ARG001`/`ARG005` for patched-callable signatures, `E402` for the
`mcp/src` import insert) are unchanged.

### `[tool.pyright]` — Include Widened To The Whole Checkout

`include` is `["."]`. It used to read `["mcp/src/agents_remember", "mcp/tests"]`, a second
hand-written copy of the scope constant `code_quality/check.py` no longer has. It was
already dead for the gate — the wrapper passes explicit files, which overrides `include` —
but it was live for editors and for a bare `pyright` run, where it under-covered the tree by
17 files including all three `scripts/sync-*.py`. Verified 2026-07-31: a bare `pyright` over
the widened include reports 0 errors, so widening it cost nothing and stopped the config
from disagreeing with the gate.

### `[tool.coverage.run]` — The First Coverage Configuration This Repository Has Had

`branch = true`. Until now the only coverage settings were the `--cov=` flags the wrapper
passed on the command line, so every default was whatever Coverage.py ships. CRAP is defined
over *branch* coverage and the wrapper was feeding it statement coverage — a metric that is
most forgiving exactly where complexity lives, because an `if` line counts as executed the
first time it is evaluated whether or not the false arm was ever taken.

The setting adds `executed_branches`, `missing_branches` and the branch fields of `summary`
to the JSON and leaves `executed_lines`/`missing_lines` unchanged.
**`crap_calculator.load_coverage_by_path` consumes those branch fields and refuses a report
whose `meta.branch_coverage` is not true**, so turning this line off breaks the gate loudly
rather than quietly returning CRAP to the metric it is not defined over. `diff_coverage.py`
reuses that reader and inherits the refusal.

Measured on 2026-07-31, consuming branch data moved the ratio of 1,705 of 4,469 scored
functions and dropped their mean from 87.61% to 85.62%, with individual functions falling as
far as 30.0% → 22.2% (`serving/app.py:267 _looks_like_image`). The aggregate moves too,
because Coverage.py scores branches into it: 88.59% statements alone, 74.65% branches alone,
**85.40% reported** at that measurement. Anything that pins a number to coverage must be
derived against the reported figure, not the statement one.

### `[tool.radon]` — Report Configuration, Not Gate Scope

`tests/*,*/tests/*` was removed from `exclude` on 2026-07-31. Radon applies these patterns
even to an explicitly named path, so the entry did not merely keep tests out of a default
scan — it made `radon cc mcp/tests` print **nothing at all**, hiding the only E- and F-rank
blocks in the repository (cc=52 in `test_codex_app_server_live.py:158`, cc=36 in
`test_codex_history_production_path.py:279`). A metric you cannot ask for is not a metric.
**What the gate runs over is decided by the wrapper's arguments, not here**, and in the gate
both Radon steps are labelled reports that cannot fail anything.

### `[tool.pytest.ini_options]` — The First Pytest Configuration This Repository Has Had

There was no `pytest.ini`, `setup.cfg` or `tox.ini` either, so every strictness switch was
off by default and there was nowhere to declare a marker.

- `testpaths = ["mcp/tests"]` is **the single declaration of where the suite lives**;
  `code_quality/check.py` reads this key to build its pytest step rather than carrying a
  second copy. A missing or empty value makes the gate raise rather than guess.
- `--strict-markers` and `--strict-config` in `addopts`: an unregistered marker is a typo
  that quietly selects nothing, and an unknown ini key is a setting that quietly does
  nothing.
- `python_classes = ["Test*", "*Tests"]` covers the house `<Subject>Tests` convention. All
  485 such classes currently reach `unittest.TestCase`, which pytest collects whatever this
  says — 3077 tests collected with and without it — so it changes nothing today and closes
  the prospective hole where a plain `PlainTests` class that does not subclass `TestCase` is
  silently skipped with no error.
- `xfail_strict = true`.
- `filterwarnings` is `error` plus **exactly three** pinned ignores, each pinned to a message
  *and* a category so it can only ever silence the exact notice it was measured against. A
  bare `error` does not merely fail this suite, it *hangs* it: uvicorn's websockets shim
  emits a `DeprecationWarning` while importing `websockets.server`, and raising it inside the
  server startup path leaves the conversation-active tests blocked in `epoll_wait` (observed
  2026-07-31 — the run stopped at test 496 of 3077 and never advanced). The list was produced
  by running the whole suite under `filterwarnings = ["always"]` and reading the summary.
  **All three remaining entries are third party and unreachable from here** (starlette's
  testclient deprecation; the two `websockets` deprecations uvicorn triggers). The entries
  that were *ours* were **fixed at source rather than ignored** in the same change:
  `providers/grepai/seed.py` now enters its `Popen` as a context manager, `_spawn_sleeper` in
  `test_dashboard_daemon.py` closes the readiness pipe it reads, and the dashboard sim's
  throwaway coordination root is closed by its owner.
  `test_code_quality_check.py::test_the_warning_ignore_list_is_capped` asserts the **exact
  count of 3** — exact, not a ceiling, so paying one off forces the number down in the same
  commit and adding one is a visible edit to a test.
- `markers` registers the **eight** environment-gated integration paths (`AR_*`, plus the
  older `AGENTS_REMEMBER_REAL_MCP_CONFIG` naming), guarding fifteen tests. Registering a
  marker is not applying one, and for a while this list was only the first: every entry was
  registered while the tests carried no `@pytest.mark.<name>` at all, so
  `pytest -m ar_run_pi_rpc_smoke` selected **0 of 3402** and reported a successful run of an
  empty selection — `--strict-markers` rejects an *unknown* marker and has nothing to say
  about a registered one decorating nothing. All eight are applied now, selecting 15, and
  `mcp/tests/test_gated_integration_runner.py` fails if any of them selects zero tests again.
  `scripts/run-gated-integration.py` is the one command per path;
  `.github/workflows/integration-gated.yml` runs the two that need no vendor account.

## Invariants And Boundaries

- Root quality-tool config governs source-checkout development checks; install package
  metadata stays in `mcp/pyproject.toml` (which also carries the supported floor and
  platforms as classifiers: Python 3.11/3.12/3.13, Linux and macOS — Windows is supported
  through WSL, which presents as Linux and has no classifier).
- `target-version` must track `requires-python`'s floor, not the newest interpreter.
- **`ignore` is not a parking space.** Every complexity code that was ever parked here was
  cleared by refactoring, and the gate carries no baseline to park a new one in.
- The single `per-file-ignores` entry for `PLR0913` covers published MCP tool signatures and
  nothing else. Widening the glob, or adding a second `PLR0913` exemption anywhere, fails an
  AST test by design.
- `[tool.pytest.ini_options] testpaths` is read by the gate. Emptying it does not widen the
  gate, it fails it.
- Radon configuration shapes a *report*. It never decides what the gate certifies.
- `branch = true` is a prerequisite, not a preference: two enforcing rails refuse to score
  without it.
- The `filterwarnings` cap and the marker inventory are both asserted by tests, in both
  directions.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The wrapper reads `testpaths` from this file and lints exactly what is selected here, with no rule routed off its command line. | [check.py](agents-remember/mcp/src/agents_remember/code_quality/check.py) |
| CRAP consumes the branch fields this file enables and refuses a report without them. | [crap_calculator.py](agents-remember/mcp/src/agents_remember/code_quality/crap_calculator.py) |
| The changed-lines coverage floor reuses that reader and inherits the same requirement. | [diff_coverage.py](agents-remember/mcp/src/agents_remember/code_quality/diff_coverage.py) |
| Tests assert the strictness switches, the exact three-entry warning cap, `python_classes`, marker/environment-gate agreement, and that the tool-signature exemption cannot widen. | [test_code_quality_check.py](agents-remember/mcp/tests/test_code_quality_check.py) |
| The one command per registered marker, and the inventory test that keeps the two in step. | [run-gated-integration.py](agents-remember/scripts/run-gated-integration.py); [test_gated_integration_runner.py](agents-remember/mcp/tests/test_gated_integration_runner.py) |
| The supported Python floor and supported platforms are declared as package classifiers. | [mcp/pyproject.toml](agents-remember/mcp/pyproject.toml) |
| Source-checkout instructions state the gate command and that Radon reports rather than enforces. | [AGENTS.md](agents-remember/AGENTS.md) |

## Update History

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 final state. **Retired this card's claims that the
  four complexity codes are held by `quality/complexity-baseline.txt` and that `PLR0913` is
  deliberately off with a named owner.** The baseline is deleted and all four codes are
  enforced by `ruff` directly; `PLR0913` runs at the default of 5 args with 274 of 293
  findings refactored (163 parameter objects) and the remaining 19 covered by the single
  `mcp/src/agents_remember/mcp/registration/*.py` per-file-ignore, which an AST test holds
  shut. Also corrected the `[tool.coverage.run]` section — CRAP now *consumes* branch data
  and refuses a report without it, rather than "branch coverage is available but not
  consumed" — and corrected the `filterwarnings` cap from five entries including two of our
  own leaks to **exactly three third-party entries**, ours having been fixed at source.
  Recorded that the eight markers are now applied (they were registered but decorated
  nothing, so `-m` selected 0 of 3402). Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 gate honesty (mid-leaf): recorded `C901` selected,
  `target-version` reconciled to py311, Pyright `include` widened, the first
  `[tool.coverage.run]`, the Radon `tests/*` exclusion removal, and the first
  `[tool.pytest.ini_options]`.
- 2026-06-06T12:28+02:00: Re-verified against current HEAD after the Pyright configuration landed; the existing Ruff, Pyright, and Radon commentary still matches.
- 2026-05-28T19:52+02:00: Created after Pyright was added to source-checkout quality configuration.
