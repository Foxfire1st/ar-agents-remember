# mcp/src/agents_remember/package_data/paseo_plugin/server/index.server.test.ts

## Governing Overview

[plugin overview](../overview.md)

## Purpose

The plugin's contribution takes its one subagent subscription from the first host API it is handed.

## Code Commentary

The cases drive the real contribution with a fake host context whose `addHook` records the Paseo 0.15 hook names: a lifecycle hook first, the snapshot RPC first, both, a readiness that fails and a readiness that is deferred. Every read of the activity publication is the file the publisher itself wrote, so the case cannot pass on a hand-made fixture.
