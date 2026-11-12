# mcp/src/agents_remember/kernel/primitives/paseo_authority.py

## Governing Overview

[overview](overview.md)

## Purpose

Own the installation's one host authority: the `paseoRuntime` block of the MCP settings file the tool server was started with, read on every use and created exactly once.

## Code Commentary

`authority_settings_path` makes `configPath` absolute without following a link, so a symlink at that address still looks like one to the writer below. `load_authority_paseo_runtime` reads the block on every use and returns `None` when the file or the block is absent — host authority is per-use, so a block a cold first run just added is visible without restarting the server. An unreadable file, bytes that are not JSON and JSON that is not an object are `HostAuthorityRefused` with the code `host-authority-unreadable` and its own recovery, never the operating system's raw error.

`establish_authority_paseo_runtime` is the one writer. A symlinked file is refused by name; a file that already carries a block is answered as `present` with `changed: false` and is never rewritten, so the developer decides when real host settings change; otherwise it writes the five-key block from `serving.paseo.fresh_host` beside the keys the file already held, marks the document it publishes with `settingsInit: host-authority`, including an existing document that lacked the block, and fills `coordinationRoot`/`workspaceRoot` only when they are absent. `_write_authority` publishes through a private temporary beside the destination with the destination's own mode (0600 for a new file), flushes and fsyncs it, then renames it over the name; a failure attempts to remove this call’s temporary, reports a cleanup failure if removal fails, and the refusal names what the authority now actually holds and what the temporary is, so a partial publication is reported rather than guessed.

The developer's own user settings file is not this surface: MIK-R137 keeps it as the user's artifact, and `paseoRuntime` belongs to the MCP authority file. Reading a block is authority to describe a host, not permission to start one.

## Evidence

- The authority path, made absolute without following a link. [1]
- The per-use read of the authority block, absent when the file or block is absent. [2]
- The once-only establishment that leaves an existing block byte-identical. [3]
- The publication by private temporary and rename, naming what remains on failure. [4]
- The five-key block the host settings module owns. [5]

- An absent file is created and an existing block is left alone. [6]
- A symlinked authority file is refused and its target untouched. [7]
- A failed publication names the actual authority and temporary states. [8]
