# mcp/tests/conftest.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Composes the ordinary, isolated pytest process for this repository and offers certification as an
explicit option. A plain test run on a developer machine works without a daemon, a lifecycle-worker
identity or a Dagger capability; `--certify` asks for genuine Dagger admission before it loads the
certifying services.

## Code Commentary

### At import

- The candidate's `mcp/src` and `mcp/test_support` are put first on `sys.path`.
- The hermetic bootstrap activates the environment of this pytest process
  (`activate_current_pytest_environment`).
- A temporary directory under `/tmp` becomes `HOME`, the XDG config, data and cache homes and
  `CODEX_HOME`; a private `TMUX_TMPDIR` scopes tmux to this pytest process. Git's global and
  system configuration are switched off. Subprocesses of a fixture
  therefore do not inherit the developer's setup.
- Inherited opt-ins and credentials are removed from the environment: every name that starts with
  `AR_RUN_`, `AR_SPAWN_` or `AR_HOSTED_`, every name that ends with `_API_KEY`, `_ACCESS_TOKEN` or
  `_AUTH_TOKEN`, and a short list of named variables. A test that needs such an input builds its
  own environment. Inherited `TMUX` and `TMUX_PANE` are removed so a fixture cannot attach through
  the developer's launcher state.
- `pytest_plugins` registers three plugins: `pytest_bootstrap`, `evidence_lanes`, and
  `database_retirement_guard`. The second
  carries the collection hook that loads the lane manifest through `load_lane_manifest` and refuses
  the run when the loader refuses. Because that loader lists the repository's files through Git, a
  test run needs a Git checkout. The third registration watches the worker process for the
  database access and file mutation routes named by the retirement guard; the registration is
  a source fact, not evidence that this curation executed the guard.

### Hooks

- `pytest_addoption` registers the two ini names `unit_case_budget` and `integration_case_budget`
  without a default, and the option `--certify`. The budgets are declared once, in the
  repository-root `pyproject.toml` under `[tool.pytest.ini_options]`.
- `pytest_configure` reads the `[files]` table of `mcp/tests/test-evidence-lanes.toml` and keeps
  the files of the `integration` and `stress-durability` lanes as the set of integration files.
  This is the first read of the manifest in a test run and it does not go through the loader. When
  the manifest cannot be read or does not parse, the hook raises a `pytest.UsageError` with the
  text of `unreadable_catalog` from `catalog_canonical.py`: the file's name, the error and, for a
  parse error, the sentence that two rows may have been interleaved by a merge and that the file is
  restored from the landed commit. It refuses by name a manifest without a `[files]` table and a
  table that lacks the `integration` or `stress-durability` lane it reads. With `--certify` the
  hook then prepares the certifying bootstrap and imports the certifying plugin; a refused Dagger
  admission becomes a `pytest.UsageError`.
- `pytest_ignore_collect` skips the integration files before they are imported when the mark
  expression is exactly `not integration`.
- `pytest_collection_modifyitems` gives every item of an integration file the `integration` marker.
- `pytest_collection_finish` counts the collected items with and without that marker and compares
  each count with its budget. A budget below 1, which is what an undeclared budget reads as, or a
  count above the budget ends the run with a `pytest.UsageError`.
- `pytest_unconfigure` attempts bounded `tmux kill-server` while the private environment still
  targets the test-owned server. Its `finally` restores the environment, closes the bootstrap's
  lease and removes the temporary directory even when tmux cleanup times out or fails to start.
  The original cleanup exception remains visible; no developer default server is targeted.

### Fixtures

- `worktree_services` binds the default worktree services for one test and resets them afterwards.
- `_integration_composition` is automatic: a test with the `integration` marker gets
  `worktree_services` unless the run uses `--certify`. A unit test asks for the fixture only when
  it needs that boundary.

The module is a governed test artifact: `mcp/tests/evidence-lifecycle.toml` holds its row with the
scope `all-tests`.

## Evidence

- The candidate's source and test-support roots come first on the import path. [1]
- The two budget names are registered without a default, beside the certify option. [2]
- Integration files are skipped before import in a run that excludes integration. [4]
- The collected items are counted against the two budgets. [5]
- The worktree services are bound and reset by a fixture. [6]
- The environment is restored and the temporary directory removed. [7]
- The isolated home directories and the switched-off Git configuration. [8]
- The removal of inherited opt-ins and credentials. [9]

- The lane manifest is read once for the integration files, an unreadable manifest is explained, and certification asks for Dagger admission. [13]
- The refusal text for a manifest that cannot be read or parsed. [14]
- The start-up hook explains a lane manifest that does not parse, and refuses by name a manifest without a `[files]` table or without the two lanes it reads. [15]


- The pytest environment owns a private tmux directory. [16]
- Environment, lease and temporary cleanup follow an attempted private-server kill even on failure. [17]
- Inherited tmux launcher variables are scrubbed from the test environment. [18]

- The three registered plugins and the comment on the Git checkout. [10]
