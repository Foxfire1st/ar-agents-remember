# mcp/src/agents_remember/package_data/paseo_plugin/server/role_agents.test.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Pin parsed role-record reuse and invalidation on rewritten registration bytes.

## Code Commentary

At two seeded population sizes, unchanged reads must reuse the same parsed object; replacing registration content produces a distinct object with exactly the new agents and then reuses it. Corrupt JSON throws and removing the file returns an empty mapping. The test owns temporary-file setup/cleanup and reference-identity assertions, not a live registration run, an elapsed-time claim or a bound on every cache in the product.

## Evidence

- Both history sizes, replacement identity, malformed input and absence. [1]
