# mcp/src/agents_remember/package_data/paseo_host/contract.json

## Governing Overview

[overview](../../../../overview.md)

## Purpose

The release-owned host contract: the host package, its one exact version and the Node release with per-platform archive URLs and SHA-256 digests.

## Code Commentary

`paseo_host_contract.py` loads this file and derives the names every consumer uses; the release concordance script checks the host manifest, the complete npm lock, the plugin SDK pin and each archive against it.

## Evidence

- The contract file consumed by the host pin. [1]
