# mcp/src/agents_remember/package_data/paseo_host/package.json

## Governing Overview

[overview](../../../../overview.md)

## Purpose

The host package manifest whose single dependency is the contract's exact host release.

## Code Commentary

The manifest's `dependencies` names `@getpaseo/cli` at the contract's version; a drift from the contract refuses release concordance, and the provision installs from the shipped lock rather than from this manifest's resolution.

## Evidence

- The exact host dependency the manifest declares. [1]
