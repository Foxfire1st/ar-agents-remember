# mcp/src/agents_remember/serving/paseo/paseo_start.py

## Governing Overview

[overview](../overview.md)

## Purpose

Read-only host status and start-only supervision: it never installs, reloads or writes configuration.

## Code Commentary

`observe_host` bounds every host read by its own five-second deadline and returns one line per state — `running`, `not running`, `not answering` (a live unanswering supervisor), `not installed` and `not configured` — with version, listen, home, carried session names and the remedy. `ensure_host` returns the observation immediately unless the state is `not running` or `not answering`. Only an installed, configured, down-and-startable host reaches `_start_locked` (after the locked re-observation): it takes the home lock, removes a stale record, requires a free settings port and starts the daemon once; a live unanswering supervisor never gets a second start, `not configured`/`not installed` start nothing, and a contending caller reuses the attempt's outcome receipt instead of starting again.

A running host observation includes the expected contract Node and observed executable. An earlier executable reports the Node restart requirement and existing terminal provision remedy even when the new target already exists. This is read-only: status and dashboard start do not replace that running host.

## Evidence

- The bounded observation with its state line. [1]

- The start-only supervision entry point. [2]


- The locked start path. [3]


- The observed Node comparison and explicit provision remedy. [4]

## The authority file the host is read from

`_settings` resolves `authority_settings_path(config.config_path)` and reads it through `load_authority_paseo_runtime`, so the observation reads the same block a cold first run establishes. A read error, malformed JSON or non-object JSON raises `HostAuthorityRefused` in that reader, which names the path and the error; `_settings` catches only `PaseoRuntimeSettingsError` and `OSError`, so the refusal escapes `_settings`, `observe_host` and `ensure_host` rather than becoming a `not installed` observation. The reachable callers include the dashboard `--status` path and the serving start path; `runtime_config._paseo_runtime_block` catches the refusal for its own callers, but `_settings` bypasses that wrapper. Nothing here writes settings.

- The settings read behind every host state. [5]
