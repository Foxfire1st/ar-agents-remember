# mcp/src/agents_remember/package_data/paseo_host/package.json

## Governing Overview

[overview](../../../../overview.md)

## Purpose

The host package manifest whose single dependency is the contract's exact host release.

## Code Commentary

The manifest's `dependencies` names `@getpaseo/cli` at the contract's version; a drift from the contract refuses release concordance. Provisioning copies this manifest and the shipped lock into staging and runs `npm ci` there.


## Evidence


- The manifest declares exactly one host dependency, `@getpaseo/cli` 0.16.2. [1]
