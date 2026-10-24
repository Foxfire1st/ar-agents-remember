# mcp/tests/test_dashboard_autostart_after_discovery.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Check the shared post-discovery startup trigger in two fresh MCP processes with autoStart enabled. Dashboard/host launchers and the outside-scratch reconciliation seam are recorders: the case inspects their trigger boundary without starting a real dashboard or host or performing real reconciliation.

## Code Commentary

The discovery process asserts no autostart thread, launcher call or sweep after preparation, server creation, or while the first tools/list answer exists before the loop runs its scheduled callback. The next step asserts one sweep, one autostart thread and one ensure; ensure_host appears once after the dashboard worker drains. Later server_info and tools/list calls add no sweep, thread or launcher call. [1]

The fallback process never lists tools. Its first server_info call asserts one sweep and one dashboard start, followed by ensure_host once when drained; its second call adds nothing. The source scenarios share the process latch. A fresh child does not inherit the parent test's latch state or AR launch binding, and the subprocess timeout uses the shared hang guard. [1] [2]

Both scenarios enable autoStart, so this case supplies no bare-no-config or autoStart-disabled witness. It records the reconciliation trigger instead of real removal/report outcomes. Its list-answer snapshot precedes callback execution, not serialized client receipt. The light tool-event writer and its boot-time caller identity are outside this case's subject. These source assertions establish no execution here or installed-host acceptance.

## Evidence

- The runner uses a fresh interpreter against checkout source with inherited AR bindings removed, checks subprocess exit and reads its report under the shared hang guard. [2]

- In the autoStart-enabled scenarios, the assertions and helper checks require zero/one sweep together with the once-only dashboard trigger at discovery/call boundaries. Dashboard/host launchers and reconciliation are recorders; no no-config, serialized-delivery, real-removal or installed-host outcome is asserted. [1]
