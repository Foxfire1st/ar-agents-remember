# mcp/src/agents_remember/serving/paseo/paseo_start.py

## Governing Overview

[overview](../overview.md)

## Purpose

Read-only host status and start-only supervision: it never installs, reloads or writes configuration.

## Code Commentary

`observe_host` bounds every host read by its own five-second deadline and returns one line per state — `running`, `not running`, `not answering` (a live unanswering supervisor), `not installed` and `not configured` — with version, listen, home, carried session names and the remedy. `ensure_host` returns the observation immediately unless the state is `not running` or `not answering`. Only an installed, configured, down-and-startable host reaches `_start_locked` (after the locked re-observation): it takes the home lock, removes a stale record, requires a free settings port and starts the daemon once; a live unanswering supervisor never gets a second start, `not configured`/`not installed` start nothing, and a contending caller reuses the attempt's outcome receipt instead of starting again.

## Evidence

- The bounded observation with its state line. [1]
- The start-only supervision entry point. [2]
- The locked start path. [3]
