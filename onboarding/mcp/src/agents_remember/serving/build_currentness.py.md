# mcp/src/agents_remember/serving/build_currentness.py

## Governing Overview

[overview](overview.md)

## Purpose

Tells a running process whether the Python code it loaded is still the code at its package root: the reading behind stale-server marks, the stale-write refusal, `server_info`, the dashboard's served build state and the dashboard daemon's restart decision.

## Code Commentary

A reading (`BuildCurrentnessPayload`) carries `mode` (`installed` or `checkout`), `state` (`current`, `stale` or `unknown`), the loaded and installed digests, and for a stale build the first time the difference was seen, the reason and the remedy ("Restart the dashboard." for role `dashboard`, "Restart or reconnect this MCP server." otherwise).

- The comparison is on Python code only: the loaded digest is the boot identity's `source_digest`, and the installed digest is `build_info.runtime_source_digest` over the `*.py` files under the same package root now. A change to Markdown or other package data does not make a process stale.
- The installed digest is computed on demand, at most once per 30 s per package root (`DIGEST_CACHE_SECONDS`), behind one process-wide lock. An unknown package root or a digest that cannot be computed answers `unknown` with the reason; nothing treats `unknown` as stale.
- The first-seen time is kept per boot identity (package root, loaded digest, boot time) while the difference lasts, and is dropped when the build reads current again. `retain_live_builds`, called by a full server-registry scan, drops first-seen times of boots that are gone and expires unreferenced digest entries.
- `build_mode` says `checkout` only when the package root is exactly `<checkout>/mcp/src/agents_remember` of a resolved checkout, not by working directory or a Git call.
- `build_currentness(config, inspect_checkout=False, role="mcp")` answers `None` for a checkout process unless the caller asks with `inspect_checkout=True` (`server_info`, the dashboard's `status=true` read). So an ordinary checkout call carries no staleness mark and is never refused for it. `inspect_build` compares any given boot identity, which the server registry uses for other processes' records.

Callers: the MCP tool dispatcher reads it before each call, attaches it to the response and refuses declared publication writes of an `installed` + `stale` build (`mcp/server.py`, `mcp/build_staleness.py`); `server_info` and `runtime_install` report it; the dashboard routes put it in the served state; `serving/daemon.py` takes the installed digest as the build a running dashboard must match.

## Evidence

- Current, stale and unknown readings, the first-seen time and the role-specific remedy. [1]
- The installed digest is cached for 30 s per package root. [2]
- A registry scan reclaims first-seen times and digest entries of gone boots. [3]
- Checkout mode is decided from the resolved checkout's package path. [4]
- An ordinary checkout call gets no reading. [5]
- The digest covers `*.py` files only. [6]
- The tool dispatcher refuses a declared write of an installed stale build. [7]
- The reading's fields. [8]
