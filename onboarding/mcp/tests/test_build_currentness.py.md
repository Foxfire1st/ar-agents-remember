# mcp/tests/test_build_currentness.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves how a running server tells whether the Python it loaded still matches the installed package, and how the live server inventory under the coordination root names each running server and its currentness.

## Code Commentary

The `world` fixture builds a one-file package, pins the process's `ServingBuild` to that package's digest and resets the shared comparison cache, so `serving.build_currentness` and `serving.server_registry` run against temporary trees.

- **Currentness.** A changed `.py` file reads `stale` only after the 30-second digest cache expires; the stale answer keeps the loaded digest, names the installed digest and a reconnect remedy, and its first-seen time stays fixed on repeats. Markdown never changes the Python digest, while adding or removing a `.py` file does, and a package without Python has no digest. An unreadable installed digest, a missing loaded digest or a missing package root answers `unknown` with a reason and no remedy.
- **Checkout versus installed.** A source checkout is compared only when status asks with `inspect_checkout=True`; otherwise currentness answers nothing and reads no file. A wheel installed below a checkout is still an `installed` build.
- **Inventory.** `register_server` writes `runtime/servers/<pid>.json` naming the role, loaded digest, boot time and settings path, and its cleanup removes the record idempotently and releases its `atexit` callback. The inventory reports a stale server with a role-specific remedy (a dashboard is restarted), removes dead or pid-reused records, ignores unparseable ones, and logs a failed registration write once without stopping the server. Status and inventory share one digest cache.
- **Cache reclamation.** First-seen times belong to live boot identities and are dropped when a boot is replaced or ends; digests expire with the cache window, while the observing process's own package root stays retained.

## Evidence

- The fixture pins the loaded build to a temporary package and resets the comparison cache. [1]
- Changed Python turns stale only after the cache window, keeping the loaded identity and first-seen time. [2]
- Markdown leaves the Python digest unchanged; adding or removing Python changes it. [3]
- A checkout is compared only on explicit request. [4]
- Unreadable or unavailable digests and a missing root answer unknown. [5]
- A wheel under a checkout is an installed build. [6]
- Status and inventory share one digest read. [7]
- A live record names pid, role, loaded digest, boot time and settings path and disappears on cleanup. [8]
- A stale dashboard is told to restart. [9]
- Each closed server lifetime releases its exit callback. [10]
- Dead and pid-reused records are removed and bad records hide no live one. [11]
- A failed registration write is logged once and the server continues. [12]
- Cache entries track live boots and roots at two population sizes. [13]
