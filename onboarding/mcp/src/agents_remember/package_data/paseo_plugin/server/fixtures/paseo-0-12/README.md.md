# `fixtures/paseo-0-12/README.md`

## Governing Overview

[Route overview](../../../overview.md)

The note that tells a reader what the fixture tree is — and, more usefully, what it is not.

## What it says

This tree is a synthetic Paseo 0.12.0 installation, written by hand for
`server/acp_providers.test.ts`. It is **not copied source**: it carries only the shapes that
MIK-R216 rule 1 reads from the installed `@getpaseo` packages, at the paths the discovery
expects. It then lays the tree out — `@getpaseo/server/package.json` for the published version,
`dist/server/server/plugins/plugin-process.js` for the argv1 path the plugin's own process
names, and `dist/server/server/agent/` for the provider modules.

That distinction matters when someone compares this tree to a real Paseo install and finds it
short: the gaps are deliberate, because a fixture that carried real source would need real
licensing and real maintenance, and would start asserting things about Paseo that this leaf does
not depend on.

## Why it is load-bearing

The provider verdict is exercised against this tree rather than a live install, so the README is
the only place that says which parts of a host the discovery actually depends on. A future
change to what the loader reads should be accompanied by a change here, or the next reader will
believe the fixture covers more of Paseo than it does.
