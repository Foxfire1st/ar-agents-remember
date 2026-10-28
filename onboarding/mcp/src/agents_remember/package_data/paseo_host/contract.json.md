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


- Official v26.11.1 distribution checksums identify the selected linux-x64 archive digest. Re-fetched 2026-10-28T06:12Z: the file still publishes node-v26.11.1-linux-x64.tar.xz as 3883bfc73f9a680ca4eab04b196068aaaab1373ffa77d8fc1a4408222495b651, which is the digest this contract retains. [2]
- MIK-R107 v1 rule 1 asks the contract to name the newest 26.x.y that nodejs.org lists on the day of the build, with each archive's address and SHA-256 from the official SHASUMS256.txt. On 2026-10-08, the build day, the newest was v26.11.1, and v26.11.1 is what this contract names — the pin is what satisfying the rule left behind. Re-fetched 2026-10-28T06:12Z the newest is v26.12.1, so the rule was satisfied on its build day and the contract does not claim to satisfy it today. [3]
