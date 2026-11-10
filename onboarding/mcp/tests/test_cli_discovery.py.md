# test_cli_discovery.py

## Governing Overview

[overview](overview.md)

## Purpose

Trusted CLI settings discovery from the one user-config file and the CLI help that describes it, and the runtime install's one-time copy of an older workspace settings file into that location, through temporary directory trees.

## Code Commentary

### Logic

Discovery reads only `$XDG_CONFIG_HOME/agents-remember/agents-remember-settings.json` (default `~/.config/...`): it wins over any workspace registration, never inspects the current directory, ignores malformed and foreign registrations, and a miss names the user-config path and the explicit `--config` remedy with no workspace fallback. The user config must name an existing absolute coordination root, and a relative `XDG_CONFIG_HOME` is a refusal. The CLI reports the discovered path on stderr, an explicit `--config` skips discovery, and discovery names another settings file only when a running dashboard daemon for the same coordination root reports it, without writing anything.

The install cases copy an older `.claude/mcp/agents-remember-settings.json` once to the user-config path with its bytes and mode, report `copied`, `already-present`, `would-copy` or `no-source`, and leave every harness folder and user-owned workspace file exactly as they were. A copy that cannot open, probe, create or finish its destination reports `permission` or `refused` with the source and user paths and a developer remedy, removes only its own incomplete destination, never widens directory permissions, and the rest of the install still completes.

The help cases walk the umbrella CLI parser through `_config_help_by_command`. The `--config` help of `memory-citations`, `providers-remove`, `removed-stores` and `knowledge-bootstrap` must name the user settings file `~/.config/agents-remember/agents-remember-settings.json` (under `XDG_CONFIG_HOME` when set), whatever the current directory; no `--config` help may claim discovery from the working or current directory; and the dashboard `--daemon` help must say that it restarts a daemon whose version, Python source digest, host or port differs.

The registration-example case (L84-LC-03) reads `examples/mcp/server.example.json` and splits its `args` with `_uvx_split`, a model of uvx's argument order: uvx options first, where a value-taking option such as `--refresh-package` consumes the next argument, then one package command, then the command's own arguments. It asserts the command is `uvx`, the only uvx option is `--refresh-package agents-remember-mcp`, the command is `agents-remember-mcp@latest` and the command receives `--config` with the settings path; it also shows the split refusing the earlier form `--refresh-package agents-remember-mcp@latest --config …`, where `--config` would land on uvx itself. The case needs no network and no uv binary.

### Conventions

Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Usable fixture settings point to an existing absolute coordination directory. The caller's directory never selects the settings authority.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- The user-config file wins over workspace registrations. [1]

- Discovery never inspects the current directory, so a nearer registration cannot select another authority. [2]

- Malformed and foreign registrations do not affect the user config. [3]

- A miss names the user-config path and the explicit --config remedy, with no workspace fallback. [4]

- The CLI reports the discovered settings and an explicit --config is used without discovery. [5]
- Discovery names a running same-root dashboard's other settings file and writes nothing. [6]
- The user config must name an existing absolute coordination root. [7]
- The default home and an explicit XDG config home share the user-settings folder; a relative one refuses. [8]
- The install copies the old settings once and leaves old and harness folders untouched. [9]
- A dry run creates no settings file or folder. [10]
- A denied destination reports a permission remedy without widening permissions while the install completes. [11]
- A destination created after the absence probe is refused and kept. [12]
- A missing user config never falls back to a registration that names a valid explicit path. [13]
- An interrupted copy removes only its own incomplete destination. [14]
- Every settings-copy OS error is reported as permission or refused while the install completes. [15]
- Every `--config` help of the umbrella parser is collected by subcommand. [16]
- The `--config` help of four subcommands names the user settings file whatever the current directory. [17]
- No `--config` help claims discovery from the working or current directory. [18]
- The dashboard `--daemon` help names the restart on a differing Python source digest. [19]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
