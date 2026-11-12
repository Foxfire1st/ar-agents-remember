# mcp/src/agents_remember/package_data/host-harness-homes.json

## Governing Overview

[overview](../../../overview.md)

## Purpose

The packaged catalog of the environment variables that set each harness's storage home, keyed by harness, with the documentation sources that name them. The host-runtime code reads it to tell whether a running host inherited a harness home that a restart would lose.

## Code Commentary

Each entry lists `variables` and `sources`; an entry may carry a `storage` note instead of variables when the harness selects its storage another way (the `eve` entry names no variable because its provider command selects the application directory with `--app`). The file holds names only, never values.

`serving/paseo/paseo_harness_homes.py` loads the catalog once at import. The process record reads the running host's values for every listed name. Status and start report inherited names that a provider's settings `env` does not supply, with a remedy to move them into `paseoRuntime.providers.<id>.env`. Before a provision stops the host, it compares the observed values with the values this run would supply and refuses with `harness-home-would-change` unless the change is explicitly accepted. Adding a harness's storage variable here brings it under both the report and the refusal; a provider entry that `extends` a listed harness inherits its variables.

## Evidence

- Each harness entry lists its home variables and documentation sources. [1]
- An entry may name no variable and explain its storage choice instead. [2]
- The serving code loads this catalog once at import. [3]
- The observed variable names are the union of every entry's variables. [4]
- A provision refuses before stopping the host when a listed home would change. [5]
