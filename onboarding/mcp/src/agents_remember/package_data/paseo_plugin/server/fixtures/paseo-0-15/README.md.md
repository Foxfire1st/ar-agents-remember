# mcp/src/agents_remember/package_data/paseo_plugin/server/fixtures/paseo-0-15/README.md

## Governing Overview

[Native Paseo plugin](../../../overview.md)

## Purpose

The note that says what the fixture tree is: a synthetic Paseo 0.15.4 installation, written by hand for `server/acp_providers.test.ts`, carrying only the shapes the ACP discovery reads from the installed `@getpaseo` packages, at the paths the discovery expects. It is not copied source.

## Code Commentary

The note lays the tree out: the server package's `package.json` for the published version, `plugins/plugin-process.js` for the argv1 path the plugin's own process names, `provider-registry.js` with the class imports and `PROVIDER_CLIENT_FACTORIES`, one provider file per client class with the ACP base and the classes that extend it or carry no base class, the two mock factories, and the protocol's `provider-manifest.js` with `AGENT_PROVIDER_DEFINITIONS`. The manifest's nested `modes` carry ids of their own, which are not provider ids; the fixture is shaped so that the discovery's depth scan must not take them for any.

## Relationships

`server/acp_providers.test.ts` reads this tree as the installed host; the version it publishes is in `@getpaseo/server/package.json` beside it. A change to what the discovery reads should change this note with it.

## Evidence

- The tree is a hand-written stand-in for the installed packages, not copied source. [1]
- The registry file carries the class imports and the factory table. [2]
- The manifest's provider definitions carry nested modes whose ids are not provider ids. [3]
