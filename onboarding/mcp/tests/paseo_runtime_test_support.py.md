# mcp/tests/paseo_runtime_test_support.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

A fake npm and Paseo command line for the runtime tests: one home's packages, daemon, config and process record,
with the settings writers a runtime case needs. It models what the product reads back, so a case can assert on
recorded calls and file states rather than on a live daemon.

## Code Commentary

### Logic

`FakePaseo` answers the install, config, plugin, start, status and stop commands of one home and records every
call; `kinds()` reports a `(group, verb)` pair per call and `mutations()` the recorded calls whose kind is in
the fixed mutating set (attempts, not proof of change), `version_at()` and `install()` model an installed
version, and `configured()`/`invalid_config()` produce a valid
or schema-invalid configuration. `record()` writes the home's process record naming a pid, `reader()` answers
what `/proc` says about a pid the fake holds, `recorded_pid()` is the live process Paseo would act on, and
`kill_daemon()` removes the daemon and its record. `converged()` reports what the daemon runs with and whether
anything was left behind.

- **Settings writers.** `write_runtime_block()` writes the host authority into the MCP settings file a config
  names, `_write_block()` leaves every other key alone, and `write_user_settings_block()` writes the developer's
  own file through the guard — only the MIK-R137 subjects do that. `write_plugin()` writes the plugin tree.
- **Staged failures.** `Interrupted` marks a provisioning process that died before a call, `refused()`/`ok()` build
  the answers, and `file_states()` returns inode, modification time and content digest of every file below the
  roots, so a case can prove nothing changed.

### Conventions

The fake is addressed by the home it represents, and every writer takes an explicit path, so a case cannot
accidentally touch the developer's real settings.

### Invariants And Boundaries

- A call is recorded with its group and verb, so "no mutation" is provable rather than assumed.
- The user settings file is written only through the guard, and only by the subjects that own it.

## Evidence

- The fake npm and Paseo command line, its settings writers, process record and file-state observation. [1]
