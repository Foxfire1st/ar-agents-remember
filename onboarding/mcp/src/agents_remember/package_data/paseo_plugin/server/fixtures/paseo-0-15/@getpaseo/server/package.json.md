# mcp/src/agents_remember/package_data/paseo_plugin/server/fixtures/paseo-0-15/@getpaseo/server/package.json

## Governing Overview

[Native Paseo plugin](../../../../../overview.md)

## Purpose

The version line of the synthetic host: it tells the ACP discovery which Paseo the fixture tree claims to be, and says in its own description that it is a stand-in, not copied source.

## Code Commentary

It publishes `"version": "0.15.4"` for `@getpaseo/server`, the release `paseo_host/contract.json` pins. `server/acp_providers.test.ts` asserts that the written verdict file names this version, so changing it retargets the provider assertions at another host; the tree and the tests are read again against it, not only re-run.

## Relationships

Read by the discovery in `server/acp_providers.ts` through `server/acp_providers.test.ts`; the rest of the tree is described in `README.md` beside the `@getpaseo` folder.

## Evidence

- The synthetic server package publishes version 0.15.4 and calls itself a stand-in. [1]
- The provider test expects the written file to name 0.15.4. [2]
