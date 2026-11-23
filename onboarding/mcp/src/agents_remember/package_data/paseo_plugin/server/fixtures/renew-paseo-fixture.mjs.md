# mcp/src/agents_remember/package_data/paseo_plugin/server/fixtures/renew-paseo-fixture.mjs

## Governing Overview

[Route overview](../../overview.md)

## Purpose

This command renews the offline ACP fixture from an installed distribution at the host contract pin.

## Code Commentary

The source argument defaults to the product install prefix. The command compares server, protocol, plugin and CLI versions with the host pin. Renewal replaces the copied `@getpaseo` subtree and writes `fixture.json`, leaving an existing README in place. `--check` requires the README and checks the recorded copy against the source.

## Evidence

- The command reads the host pin and checks the installed package versions. [1]
- The check branch verifies the README and the copy. Renewal writes the copied subtree and provenance. [2]
