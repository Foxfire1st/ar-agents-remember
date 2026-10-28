# `fixtures/paseo-0-12/@getpaseo/server/package.json`

## Governing Overview

[Route overview](../../../../../overview.md)

The version line of the synthetic host: this manifest is what tells the loader which Paseo the
fixture tree claims to be.

## What it carries

It publishes `"version": "0.12.0"` for `@getpaseo/server`, and says in its own description that
it is a stand-in, not copied source. That version is the fact the discovery reads: a host's
`acp-providers.json` is only meaningful against a known Paseo, so the fixture pins one and the
provider tests hold the loader to 0.12.0's shapes.

Changing this number is therefore not a maintenance edit — it retargets every provider assertion
in `server/acp_providers.test.ts` at a different host. If the fixture is regenerated for a newer
Paseo, the version here moves with the tree and the tests are re-read against it, not just
re-run.
