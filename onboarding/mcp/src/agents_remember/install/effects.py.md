# mcp/src/agents_remember/install/effects.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Observe the mutations one installer call makes, including the ones an interrupted operation left behind, without changing what an ordinary install does.

## Code Commentary

`capture_install_effects` sets a call-local list on a context variable and resets it afterwards, so only the call that asked observes anything and every other install keeps its result and behavior. `observe_install_effect` records the entry states before the operation — a symlink by its target, a regular file by its SHA-256 and mode, a directory, an absent or unreadable path — and appends one row per entry whose state changed, comparing after the operation whether it succeeded or raised. Because `mkdir(parents=True)` can create more than one directory, the missing ancestors of the destination are included; a `remove` of a directory observes its whole tree; a `copy` leaves parent creation to the observed `ensure_dir`. An interrupted copy is observed after its error, so bytes written before a failing copy or stat are still part of the refusal's account, and the operation's own error is never masked.

## Evidence

- The call-local capture, set and reset around the one call. [1]
- The before/after observation that names changed entries without masking the error. [2]
- Missing ancestors, a removed tree and a copied file's entry states. [3]
- An installer failure reports the files already written, an occupied file returns a refusal with its partial effects, and a partial tree removal names the deleted child. [4]
