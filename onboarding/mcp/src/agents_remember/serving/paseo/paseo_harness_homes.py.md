# mcp/src/agents_remember/serving/paseo/paseo_harness_homes.py

## Governing Overview

[overview](../overview.md)

## Purpose

Reports and protects the harness-home variables a running host took from the environment it was started in, so that a provision restart does not move a harness's home and sessions.

## Code Commentary

The variable list is package data, `package_data/host-harness-homes.json`: per provider the variables by which that harness finds its home, with the source of each name. A host's value for a variable counts as inherited when a provider that uses it (by id, or a configured provider that `extends` it) has no such key in its settings `env`; a catalogued built-in provider that the settings do not override always inherits.

`harness_home_status` returns `inheritedHarnessHomes` (names only, sorted) and `harnessHomeRemedy`, which points to `paseoRuntime.providers.<id>.env` in the active settings file; without readable process facts it answers `unknown`. `require_preserved_harness_homes` compares each observed value with what the new host would get (the provider's `env`, else this process's environment) and raises `harness-home-would-change` before anything is stopped, naming each variable with its running and new value and the three ways on. It adds no refusal when the operator accepted the change or the process facts are unavailable.

## Evidence

- The variable list is loaded from package data. [1]
- A variable is inherited unless every provider that uses it carries it in its settings `env`. [2]
- Status reports inherited names and the settings remedy, or `unknown`. [3]
- The refusal before a stop, with running and new values and the ways on. [4]
- The catalogued harness-home variables with their sources. [5]
