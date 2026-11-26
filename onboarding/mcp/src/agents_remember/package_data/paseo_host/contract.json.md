# mcp/src/agents_remember/package_data/paseo_host/contract.json

## Governing Overview

[overview](../../../../overview.md)

## Purpose

The release-owned host contract specifies the exact host package version and the Node release, archive URL and SHA-256 for linux-x64.

## Code Commentary

`paseo_host_contract.py` loads this file for its consumers. The release concordance script checks agreement between the host manifest, lock root, host lock entry and plugin SDK pin. It also requires a version, integrity field and HTTPS resolution for each locked package. For Node, it requires only the linux-x64 platform, the canonical release archive URL and a 64-character lowercase hexadecimal digest. The Node provisioner separately hashes the downloaded archive and refuses a mismatch before extraction.

## Evidence

- The contract selects `@getpaseo/cli` 0.16.2 and Node 26.13.1 for linux-x64. [1]
- Official Node v26.13.1 distribution checksums record SHA-256 `5c063e46bab0fbc1c17cc445d7ff129cbdcd0471be6ed83b6ab864f8143bc864` for `node-v26.13.1-linux-x64.tar.xz`, matching the pinned digest. [2]
- The official Node release index lists 26.13.1 (2026-11-10, LTS Lithium) as the newest Node 26 release. [3]

- Release concordance checks the package and lock pins, the sole supported platform, the canonical archive URL and the configured digest format. [4]
- The Node provisioner computes SHA-256 from the downloaded archive and rejects a mismatch before opening it for extraction. [5]
