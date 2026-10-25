# mcp/src/agents_remember/package_data/paseo_host/contract.json

## Governing Overview

[overview](../../../../overview.md)

## Purpose

The release-owned host contract: the host package, its one exact version and the Node release with per-platform archive URLs and SHA-256 digests.

## Code Commentary

`paseo_host_contract.py` loads this file and derives the names every consumer uses; the release concordance script checks the host manifest, the complete npm lock, the plugin SDK pin and each archive against it.


**L184 — INV-JS6GJ7.** This file is the contract the pin checker reads, so the answer's shape is stated here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence



- The contract file consumed by the host pin. [1]


- Official v26.11.1 distribution checksums identify the selected linux-x64 archive digest; the retained inspection is dated2026-10-08T08:39:28Z. [2]
- The official release index inspected2026-10-08T09:54:43Z lists26.11.1 as the newest26 release; this retrieval does not assert later releases. [3]
