# mcp/src/agents_remember/canvas/presenter_native.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Real presenter sessions on the configured host, outside the AR role and acceptance seats. The launch has only a dedicated confined tool server: built-in tools and inherited MCP servers are removed, and the server admits exact input bytes and writes only the prepared presentation folder.

## Code Commentary

- `NativePresenterHarness.start` launches the confined server; `reconcile` repeats the immutable native create with no settings reread, so an uncertain start is resolved by identity rather than by a second launch.
- The host operations `message`, `status`, `transcript`, `resume`, `cancel` and `archive` are answered for the attempt's own session, and the receipt records what the host said.
- `TOOL_NAMES` is the whole tool authority the author gets; no AR tool is among them.

## Evidence

- The launch has only a dedicated confined tool server. [1]
- An uncertain start is reconciled by repeating the immutable create, not by relaunching. [2]
- The author's tool authority is the named tool set only. [3]
