# mcp/src/agents_remember/kernel/primitives/fresh_host.py

## Governing Overview

[Kernel primitives overview](overview.md)

## Purpose

Spell the `paseoRuntime` block a cold host needs before it can dispatch a start.

## Code Commentary

`fresh_host_block` answers the five-key block the installer writes: the build-pinned install prefix and daemon home under the XDG data and state homes, the dedicated listen address, an empty provider map and one embed entry per dashboard origin built from the port the settings hold. The names live in the kernel primitive vocabulary, so the settings writer asks for a fresh block instead of spelling an address of its own; the provisioning commands in `serving/paseo` consume the block; the block is created once by the host-authority owner and never rewritten over an existing one.

## Evidence

- The five-key block built from the XDG homes, the default listen address and the dashboard origins. [1]
- The host authority is created with that five-key block and an existing block is never rewritten. [2]
